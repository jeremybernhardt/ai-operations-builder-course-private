#!/usr/bin/env python3
"""Scan course continuity without emitting repository source text."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "course_reliability_scan.v1"
MAX_OUTPUT_BYTES = 8192
LEGACY_STARTUP_WORDS = 31_889
ONE_TIME_WORD_TARGET = 17_000
ONE_TIME_REDUCTION_TARGET = 40.0
EXCLUDED_PARTS = {
    ".git",
    ".next",
    ".sites-runtime",
    ".wrangler",
    "__pycache__",
    "dist",
    "node_modules",
}
TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".py",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}
CORE_STARTUP_PATHS = [
    "AGENTS.md",
    "COURSE_CONTRACT.md",
    "COURSE_STATE.json",
    "PROGRESS.json",
    "CAPABILITY_EVIDENCE_LEDGER.md",
    "DECISION_LOG.md",
    "SESSION_HANDOFF.md",
    "NEXT_CHAT_PROMPT.md",
]


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_excluded(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return path.name.startswith(".codex-") or any(part in EXCLUDED_PARTS for part in rel.parts) or path.suffix.lower() in {
        ".log",
        ".pyc",
        ".zip",
    }


def is_transient_excel_lock(path: Path) -> bool:
    return path.name.startswith("~$") and path.suffix.lower() == ".xlsx"


def scan_inventory(root: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    files_scanned = 0
    text_files_scanned = 0
    json_files_scanned = 0
    bytes_scanned = 0
    invalid_json_paths: list[str] = []
    ignored_excel_locks = 0
    workbook_files_metadata_only = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file() or is_excluded(path, root):
            continue
        if is_transient_excel_lock(path):
            ignored_excel_locks += 1
            continue
        rel = relative(path, root)
        if path.suffix.lower() == ".xlsx":
            size = path.stat().st_size
            digest.update(rel.encode("utf-8"))
            digest.update(b"\0xlsx-metadata-only\0")
            digest.update(str(size).encode("ascii"))
            files_scanned += 1
            bytes_scanned += size
            workbook_files_metadata_only += 1
            continue
        data = path.read_bytes()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(data)
        files_scanned += 1
        bytes_scanned += len(data)
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text_files_scanned += 1
        if path.suffix.lower() == ".json":
            json_files_scanned += 1
            try:
                json.loads(data.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                invalid_json_paths.append(rel)

    return {
        "bytes_scanned": bytes_scanned,
        "files_scanned": files_scanned,
        "ignored_transient_excel_locks": ignored_excel_locks,
        "invalid_json_paths": invalid_json_paths[:25],
        "json_files_scanned": json_files_scanned,
        "repository_digest_sha256": digest.hexdigest(),
        "text_files_scanned": text_files_scanned,
        "workbook_files_metadata_only": workbook_files_metadata_only,
    }


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def find_lesson(root: Path, lesson_id: str) -> list[Path]:
    return sorted((root / "lesson").glob(f"{lesson_id}_*.md"))


def evidence_paths(progress: dict[str, Any]) -> list[str]:
    found: set[str] = set()
    for lesson in progress.get("lessons", []):
        if not isinstance(lesson, dict):
            continue
        for path in lesson.get("verification_evidence", []):
            if isinstance(path, str):
                found.add(path)
    return sorted(found)


def word_count(path: Path) -> int:
    text = read_text(path)
    return len(text.split()) if text is not None else 0


def gate_statuses(value: Any) -> list[str]:
    statuses: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "status" and isinstance(child, str):
                statuses.append(child)
            else:
                statuses.extend(gate_statuses(child))
    elif isinstance(value, list):
        for child in value:
            statuses.extend(gate_statuses(child))
    return statuses


def build_report(root: Path = ROOT) -> dict[str, Any]:
    root = root.resolve()
    inventory = scan_inventory(root)
    checks: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    observations: list[dict[str, Any]] = []

    def add_check(check_id: str, passed: bool, paths: list[str], warning: bool = False) -> None:
        status = "pass" if passed else ("warning" if warning else "fail")
        checks.append({"id": check_id, "paths": paths[:12], "status": status})
        if not passed:
            target = warnings if warning else failures
            target.append({"code": check_id.upper(), "paths": paths[:12]})

    core_missing = [path for path in CORE_STARTUP_PATHS if not (root / path).is_file()]
    add_check("core_startup_files", not core_missing, core_missing)
    add_check("json_structure", not inventory["invalid_json_paths"], inventory["invalid_json_paths"])

    state = load_json(root / "COURSE_STATE.json") or {}
    progress = load_json(root / "PROGRESS.json") or {}
    next_lesson_id = str(progress.get("course_architecture", {}).get("required_next_lesson", ""))
    next_lessons = find_lesson(root, next_lesson_id) if next_lesson_id else []
    lesson_problem_paths = [relative(path, root) for path in next_lessons]
    if not next_lessons:
        lesson_problem_paths = [f"lesson/{next_lesson_id}_*.md" if next_lesson_id else "PROGRESS.json"]
    add_check("next_lesson_spec_unique", len(next_lessons) == 1, lesson_problem_paths)

    prerequisite_path = ""
    if len(next_lessons) == 1:
        lesson_text = read_text(next_lessons[0]) or ""
        match = re.search(r"Prerequisite evidence:\s*`([^`]+)`", lesson_text)
        prerequisite_path = match.group(1) if match else ""
    add_check(
        "prerequisite_evidence",
        bool(prerequisite_path and (root / prerequisite_path).is_file()),
        [prerequisite_path or (lesson_problem_paths[0] if lesson_problem_paths else "lesson")],
    )

    referenced_evidence = evidence_paths(progress)
    missing_evidence = [path for path in referenced_evidence if not (root / path).is_file()]
    add_check("recorded_evidence_paths", not missing_evidence, missing_evidence)

    lesson_records = {
        item.get("lesson_id"): item
        for item in progress.get("lessons", [])
        if isinstance(item, dict) and isinstance(item.get("lesson_id"), str)
    }
    current_lesson_id = str(state.get("current_lesson_id", ""))
    current_record = lesson_records.get(current_lesson_id, {})
    current_checkpoint_id = str(state.get("current_checkpoint_id", ""))
    last_checkpoint_id = str(state.get("last_verified_learner_checkpoint", {}).get("checkpoint_id", ""))
    next_action = str(state.get("next_action", ""))
    prompt_text = read_text(root / "NEXT_CHAT_PROMPT.md") or ""
    handoff_text = read_text(root / "SESSION_HANDOFF.md") or ""
    ledger_text = read_text(root / "CAPABILITY_EVIDENCE_LEDGER.md") or ""
    critical_consistent = all(
        [
            bool(current_record),
            current_checkpoint_id == last_checkpoint_id,
            str(current_record.get("current_checkpoint_id", "")) == current_checkpoint_id,
            next_lesson_id in next_action,
            next_lesson_id in prompt_text,
            state.get("module_status", {}).get("independent_mastery_claimed") is False,
        ]
    )
    add_check(
        "critical_course_facts",
        critical_consistent,
        ["COURSE_STATE.json", "PROGRESS.json", "NEXT_CHAT_PROMPT.md"],
    )

    expected_mastery = "Completed with limited assistance"
    assistance_consistent = all(
        [
            current_record.get("mastery_status") == expected_mastery,
            state.get("last_verified_learner_checkpoint", {}).get("status")
            == "completed_with_limited_assistance",
            expected_mastery in handoff_text,
            current_checkpoint_id in ledger_text and expected_mastery in ledger_text,
            "not independent mastery" in prompt_text,
        ]
    )
    add_check(
        "assistance_and_mastery_boundary",
        assistance_consistent,
        ["COURSE_STATE.json", "PROGRESS.json", "CAPABILITY_EVIDENCE_LEDGER.md", "SESSION_HANDOFF.md", "NEXT_CHAT_PROMPT.md"],
    )

    scope_consistent = all(
        [
            next_lesson_id in handoff_text,
            "current authorization covers only" in prompt_text.lower(),
            "M0.5-L5_or_later_without_checkpoint_authorization"
            in state.get("scope_guard", {}).get("not_authorized", []),
            "do not implement the Expense File Readiness Checker" in next_action,
        ]
    )
    add_check(
        "scope_and_next_action_boundary",
        scope_consistent,
        ["COURSE_STATE.json", "SESSION_HANDOFF.md", "NEXT_CHAT_PROMPT.md"],
    )

    limitations_consistent = all(
        [
            "Verification and limitations" in handoff_text,
            "Known limitations" in ledger_text,
            "limitations" in prompt_text,
        ]
    )
    add_check(
        "limitations_boundary",
        limitations_consistent,
        ["CAPABILITY_EVIDENCE_LEDGER.md", "SESSION_HANDOFF.md", "NEXT_CHAT_PROMPT.md"],
    )

    statuses = gate_statuses(progress.get("capability_gates", {}))
    add_check(
        "capability_gate_boundary",
        bool(statuses) and all(status == "Not started" for status in statuses),
        ["PROGRESS.json"],
    )

    decisions_text = read_text(root / "DECISION_LOG.md") or ""
    required_decisions = ["DEC-C2-012", "DEC-C2-013"]
    missing_decisions = [decision for decision in required_decisions if decision not in decisions_text]
    add_check("approved_reliability_teaching_decisions", not missing_decisions, ["DECISION_LOG.md"])

    prompt_lower = prompt_text.lower()
    selective_terms_present = all(
        term in prompt_lower
        for term in ["selective startup", "recovery index", "scan-only", "current authorization covers only"]
    )
    add_check("selective_startup_prompt", selective_terms_present, ["NEXT_CHAT_PROMPT.md"])

    gitignore_text = read_text(root / ".gitignore") or ""
    bundle_text = read_text(root / "scripts/package_bundle.py") or ""
    lock_excluded = all(
        [
            "~$*.xlsx" in gitignore_text,
            "is_transient_lock_file" in bundle_text,
            "is_binary_workbook" in bundle_text,
            "xlsx-metadata-only" in (read_text(root / "scripts/reliability_scan.py") or ""),
        ]
    )
    add_check("excel_lock_exclusion", lock_excluded, [".gitignore", "scripts/package_bundle.py"])

    maintenance = state.get("reliability_maintenance", {})
    completed_stages = maintenance.get("completed_stages", []) if isinstance(maintenance, dict) else []
    rel3_active = (
        maintenance.get("active_stage") == "REL-3"
        and maintenance.get("active_stage_status") == "verification_pending"
    )
    maintenance_valid = isinstance(completed_stages, list) and all(
        stage in completed_stages for stage in ["REL-0", "REL-1", "REL-2"]
    ) and ("REL-3" in completed_stages or rel3_active)
    add_check("reliability_stage_state", maintenance_valid, ["COURSE_STATE.json"])

    mandatory_paths = list(CORE_STARTUP_PATHS)
    if len(next_lessons) == 1:
        mandatory_paths.append(relative(next_lessons[0], root))
    if prerequisite_path and (root / prerequisite_path).is_file():
        mandatory_paths.append(prerequisite_path)
    mandatory_paths = list(dict.fromkeys(mandatory_paths))
    mandatory_words = sum(word_count(root / path) for path in mandatory_paths if (root / path).is_file())
    reduction_percent = round((1 - mandatory_words / LEGACY_STARTUP_WORDS) * 100, 2)
    add_check(
        "one_time_context_target",
        mandatory_words <= ONE_TIME_WORD_TARGET and reduction_percent >= ONE_TIME_REDUCTION_TARGET,
        mandatory_paths,
    )

    approved_baseline = maintenance.get("approved_mandatory_startup_words") if isinstance(maintenance, dict) else None
    growth_percent: float | None = None
    if isinstance(approved_baseline, int) and approved_baseline > 0:
        growth_percent = round((mandatory_words / approved_baseline - 1) * 100, 2)
        add_check("mandatory_context_growth_stop", growth_percent <= 10, mandatory_paths)
        add_check("mandatory_context_growth_audit", growth_percent <= 5, mandatory_paths, warning=True)
    else:
        add_check("approved_context_baseline", False, ["COURSE_STATE.json"])

    history_paths = {
        relative(path, root)
        for path in (root / "lesson").glob("*.md")
        if path.is_file()
    }
    history_paths.update(referenced_evidence)
    on_demand_count = len(history_paths - set(mandatory_paths))

    if inventory["ignored_transient_excel_locks"]:
        observations.append({"code": "TRANSIENT_EXCEL_LOCK_IGNORED", "paths": []})
    if inventory["workbook_files_metadata_only"]:
        observations.append({"code": "WORKBOOK_CONTENT_SKIPPED", "paths": []})

    status = "fail" if failures else ("warning" if warnings else "pass")
    return {
        "checks": checks,
        "context": {
            "approved_baseline_words": approved_baseline,
            "growth_percent": growth_percent,
            "legacy_startup_words": LEGACY_STARTUP_WORDS,
            "mandatory_paths": mandatory_paths,
            "mandatory_startup_words": mandatory_words,
            "on_demand_history_paths_indexed": on_demand_count,
            "reduction_percent": reduction_percent,
        },
        "failures": failures,
        "inventory": inventory,
        "max_output_bytes": MAX_OUTPUT_BYTES,
        "observations": observations,
        "schema": SCHEMA,
        "status": status,
        "warnings": warnings,
    }


def serialize_report(report: dict[str, Any], pretty: bool = False) -> str:
    if pretty:
        encoded = json.dumps(report, indent=2, sort_keys=True)
    else:
        encoded = json.dumps(report, separators=(",", ":"), sort_keys=True)
    output_bytes = len(encoded.encode("utf-8"))
    if output_bytes <= MAX_OUTPUT_BYTES:
        return encoded
    bounded = {
        "failures": [{"code": "OUTPUT_LIMIT_EXCEEDED", "paths": []}],
        "max_output_bytes": MAX_OUTPUT_BYTES,
        "original_output_bytes": output_bytes,
        "schema": SCHEMA,
        "status": "fail",
    }
    return json.dumps(bounded, separators=(",", ":"), sort_keys=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    report = build_report(args.root)
    print(serialize_report(report, pretty=args.pretty))
    return 1 if report["status"] == "fail" else 0


if __name__ == "__main__":
    sys.exit(main())
