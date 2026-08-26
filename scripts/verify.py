#!/usr/bin/env python3
"""Run deterministic prototype release checks without revealing known values."""

from __future__ import annotations

import csv
import json
import re
import sqlite3
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import setup as course_setup  # noqa: E402


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_clean_setup() -> None:
    with tempfile.TemporaryDirectory(prefix="course-prototype-") as tmp:
        base = Path(tmp)
        database = base / "database" / "prototype.sqlite"
        generated = base / "generated"
        artifacts = base / "artifacts"
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "setup.py"),
                "--database",
                str(database),
                "--generated-dir",
                str(generated),
                "--public-artifacts",
                str(artifacts),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        check(database.is_file() and database.stat().st_size > 0, "clean setup did not create SQLite")
        check((generated / "progress-snapshot.json").is_file(), "clean setup missed progress snapshot")
        check((artifacts / "COURSE_CONTRACT.md").is_file(), "clean setup missed portal artifacts")


def verify_database_and_edges() -> None:
    rows = course_setup.read_rows()
    database = ROOT / "database" / "prototype.sqlite"
    course_setup.build_database(rows, database)

    with sqlite3.connect(database) as connection:
        row_count = connection.execute("SELECT COUNT(*) FROM review_events").fetchone()[0]
        unique_count = connection.execute("SELECT COUNT(DISTINCT review_id) FROM review_events").fetchone()[0]
    check(row_count == len(rows), "database row count does not reconcile to CSV")
    check(unique_count == len(rows), "review_id uniqueness control failed")

    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["task_id"], row["submission_attempt"], row["review_sequence"])].append(row)
    check(any(len(group) > 1 for group in groups.values()), "duplicate-review fixture missing")
    check(any(not row["review_status"] for row in rows), "missing-data fixture missing")
    check(any(int(row["submission_attempt"]) > 1 for row in rows), "reworked-task fixture missing")
    summary = course_setup.build_quality_summary(rows)
    check(summary["tasks_requiring_policy_choice"] >= 3, "ambiguous-denominator fixture missing")


def independent_reference(rows: list[dict[str, str]]) -> dict[str, float | int]:
    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["task_id"], row["submission_attempt"], row["review_sequence"])].append(row)
    chosen = []
    for (task_id, attempt, sequence), group in groups.items():
        if int(attempt) != 1 or int(sequence) != 1:
            continue
        first = sorted(group, key=lambda row: (row["reviewed_at"], row["review_id"]))[0]
        if first["review_status"]:
            chosen.append(first)
    accepted = sum(row["review_status"] == "accepted" for row in chosen)
    eligible = len(chosen)
    return {
        "accepted_first_pass_count": accepted,
        "eligible_first_pass_count": eligible,
        "first_pass_acceptance_rate": accepted / eligible,
    }


def verify_known_answer() -> None:
    rows = course_setup.read_rows()
    expected = json.loads((ROOT / "instructor_only" / "reference_expectation.json").read_text(encoding="utf-8"))
    independent = independent_reference(rows)
    for key in independent:
        check(abs(independent[key] - expected[key]) < 1e-12, f"independent reference mismatch for {key}")

    query = (ROOT / "instructor_only" / "reference_metric.sql").read_text(encoding="utf-8")
    with sqlite3.connect(ROOT / "database" / "prototype.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        result = dict(connection.execute(query).fetchone())
    for key in independent:
        check(abs(result[key] - independent[key]) < 1e-12, f"SQL reference mismatch for {key}")


def verify_progress_snapshot() -> None:
    progress = json.loads((ROOT / "PROGRESS.json").read_text(encoding="utf-8"))
    snapshot = course_setup.build_progress_snapshot()
    lesson = next(item for item in progress["lessons"] if item["lesson_id"] == "M0.5-L3")
    m0_5_l2 = next(item for item in progress["lessons"] if item["lesson_id"] == "M0.5-L2")
    m0_5_l1 = next(item for item in progress["lessons"] if item["lesson_id"] == "M0.5-L1")
    m0_l4 = next(item for item in progress["lessons"] if item["lesson_id"] == "M0-L4")
    m0_l3 = next(item for item in progress["lessons"] if item["lesson_id"] == "M0-L3")
    m0_l2 = next(item for item in progress["lessons"] if item["lesson_id"] == "M0-L2")
    m0_l1 = next(item for item in progress["lessons"] if item["lesson_id"] == "M0-L1")
    prototype = next(item for item in progress["lessons"] if item["lesson_id"] == "P0-L1")
    check(snapshot["lesson"] == lesson, "portal progress does not match canonical lesson progress")
    check(snapshot["non_authoritative"] is True, "portal progress is not labeled non-authoritative")
    check(
        lesson["mastery_status"] == "Completed with limited assistance",
        "canonical learner status does not match the recorded M0.5-C3 evidence",
    )
    check(lesson["learner_attempt_received"] is True, "learner attempt evidence is missing")
    check("limited" in lesson["assistance_level"], "M0.5-C3 transfer assistance is not recorded honestly")
    check(m0_5_l2["mastery_status"] == "Completed with limited assistance", "M0.5-C2 evidence was changed")
    check(m0_5_l1["mastery_status"] == "Completed with limited assistance", "M0.5-C1 evidence was changed")
    check(m0_l4["mastery_status"] == "Completed with substantial assistance", "M0-C4 evidence was changed")
    check(m0_l3["mastery_status"] == "Completed with substantial assistance", "M0-C3 evidence was changed")
    check(m0_l2["mastery_status"] == "Completed with substantial assistance", "M0-C2 evidence was changed")
    check(m0_l1["mastery_status"] == "Completed with limited assistance", "M0-C1 evidence was changed")
    check(prototype["mastery_status"] == "Completed with substantial assistance", "P0-C1 evidence was changed")
    check(
        (ROOT / "evidence" / "LEARNER_CHECKPOINT_P0-C1.md").is_file(),
        "prototype learner checkpoint evidence file is missing",
    )
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C1.md").is_file(), "M0-C1 evidence file is missing")
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C2.md").is_file(), "M0-C2 evidence file is missing")
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C3.md").is_file(), "M0-C3 evidence file is missing")
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C4.md").is_file(), "M0-C4 evidence file is missing")
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0.5-C1.md").is_file(), "M0.5-C1 evidence file is missing")
    check((ROOT / "student" / "M0.5-L1_EXPENSE_FILE_READINESS_BUILD_BRIEF.md").is_file(), "M0.5-L1 build brief is missing")
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0.5-C2.md").is_file(), "M0.5-C2 evidence file is missing")
    check((ROOT / "student" / "M0.5-L2_EXPENSE_FILE_READINESS_AI_PLAN.md").is_file(), "M0.5-L2 AI plan is missing")
    check((ROOT / "student" / "M0.5-L2_EXPENSE_FILE_READINESS_REVIEWED_PLAN.md").is_file(), "M0.5-L2 reviewed plan is missing")
    check((ROOT / "evidence" / "LEARNER_CHECKPOINT_M0.5-C3.md").is_file(), "M0.5-C3 evidence file is missing")
    check((ROOT / "student" / "M0.5-L3_ANNOTATED_DIFF_REVIEW.md").is_file(), "M0.5-L3 guided review is missing")
    check((ROOT / "student" / "M0.5-L3_CASH_SCHEDULE_TRANSFER_PACKET.md").is_file(), "M0.5-L3 transfer response is missing")
    check((ROOT / "student" / "M0.5-L3_CASH_DISBURSEMENT_ACCEPTANCE_FIXTURE.xlsx.inspect.ndjson").is_file(), "M0.5-L3 text inspection record is missing")


def verify_student_gate() -> None:
    sql = (ROOT / "student" / "first_pass_acceptance.sql").read_text(encoding="utf-8")
    check("TODO" in sql, "student SQL should remain incomplete before P0-C1")
    executable = [line for line in sql.splitlines() if line.strip() and not line.lstrip().startswith("--")]
    check(not executable, "student SQL contains executable solution text")


def verify_no_secrets() -> None:
    excluded = {"node_modules", ".git", ".sites-runtime", "dist", ".wrangler", ".openai"}
    suspicious = [
        re.compile(r"(?i)(api[_-]?key|password|secret|token)\s*[:=]\s*['\"][^'\"]{8,}"),
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    ]
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.name.startswith(".codex-") or any(part in excluded for part in path.parts):
            continue
        if path.suffix.lower() in {".sqlite", ".png", ".jpg", ".jpeg", ".zip", ".woff", ".woff2"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(pattern.search(text) for pattern in suspicious):
            hits.append(str(path.relative_to(ROOT)))
    check(not hits, f"possible secrets detected in: {hits}")


def verify_beginner_entry_point() -> None:
    start_here = (ROOT / "START_HERE.html").read_text(encoding="utf-8")
    start_script = ROOT / "scripts" / "start-course.sh"
    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    check("npm run course" in start_here, "START_HERE is missing the single learner start command")
    check("Control + C" in start_here, "START_HERE is missing the local stop instruction")
    check("Do not start a tunnel" in start_here, "START_HERE is missing the privacy boundary")
    check(package["scripts"].get("course") == "bash scripts/start-course.sh", "learner start command is not locked")
    check(start_script.is_file(), "learner start script is missing")
    check(start_script.stat().st_mode & 0o111, "learner start script is not executable")
    script_text = start_script.read_text(encoding="utf-8")
    check("python3 scripts/setup.py" in script_text, "learner start script does not prepare data")
    check("npm ci" in script_text, "learner start script cannot recover missing locked components")


def verify_v2_architecture() -> None:
    state = json.loads((ROOT / "COURSE_STATE.json").read_text(encoding="utf-8"))
    progress = json.loads((ROOT / "PROGRESS.json").read_text(encoding="utf-8"))
    contract = (ROOT / "COURSE_CONTRACT.md").read_text(encoding="utf-8")
    curriculum = (ROOT / "CURRICULUM_MAP.md").read_text(encoding="utf-8")
    ledger = (ROOT / "CAPABILITY_EVIDENCE_LEDGER.md").read_text(encoding="utf-8")
    prompt = (ROOT / "NEXT_CHAT_PROMPT.md").read_text(encoding="utf-8")
    check(state["schema_version"] == "2.0.0", "course state schema was not upgraded")
    check(progress["schema_version"] == "2.0.0", "progress schema was not upgraded")
    check(state["course_architecture_approval"]["status"] == "approved", "v2 architecture approval missing")
    check(state["release_version"] == "2.0.7", "v2.0.7 release state missing")
    check(state["current_checkpoint_id"] == "M0.5-C3", "M0.5-C3 checkpoint is not current")
    check(state["authoritative_source"]["repository_full_name"] == "jeremybernhardt/ai-operations-builder-course-private", "private repository authority missing")
    check(state["authoritative_source"]["visibility"] == "private", "private visibility state missing")
    check("Finance is the primary application context" in contract, "technical-subject boundary missing")
    check("AI-assisted operator-builder proficiency" in contract, "operator-builder target missing")
    check("Do not require Jeremy to memorize syntax" in contract, "syntax-memorization guard missing")
    check("Output-based testing is the primary starting point" in contract, "output-first verification rule missing")
    check("independent modification" in contract and "AI assistance is permitted" in contract, "AI-assisted independent modification rule missing")
    check("Give SQL somewhat more direct practice" in contract, "SQL practice emphasis missing")
    check("tracing, troubleshooting, modifying, and reusing" in contract, "Python/pandas modification emphasis missing")
    check("AI should also execute routine local implementation" in contract, "safe AI-execution default missing")
    check("Do not grade command-sequence or syntax recall" in contract, "command-recall guard missing")
    check("does not count as dashboard-building evidence" in contract, "Course Portal/work-dashboard boundary missing")
    check("First End-to-End Finance Data Tool" in curriculum, "early work dashboard missing")
    check("Permissioned Tool-Using Agent" in curriculum, "permissioned agent module missing")
    check("Optional Human-Data and AI Operations Transfer" in curriculum, "optional human-data module missing")
    check("GATE-WORK-DASHBOARD" in ledger, "work-dashboard evidence gate missing")
    check("M0-C2" in ledger, "M0-C2 evidence ledger entry missing")
    check("M0-C3" in ledger, "M0-C3 evidence ledger entry missing")
    check("M0-C4" in ledger, "M0-C4 evidence ledger entry missing")
    check("M0.5-C1" in ledger, "M0.5-C1 evidence ledger entry missing")
    check("M0.5-C2" in ledger, "M0.5-C2 evidence ledger entry missing")
    check("M0.5-C3" in ledger, "M0.5-C3 evidence ledger entry missing")
    check("M0.5-L4" in prompt and "Debugging from Evidence and Directing a Bounded Modification" in prompt, "next bounded lesson missing")
    check("safe local practice code" in prompt and "bounded correction" in prompt, "work-practical next-lesson context missing")
    check("DEC-C2-009" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "AI-execution decision missing")
    check("DEC-C2-010" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "teaching-strategy decision missing")
    check("DEC-M0-001" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "identity/privacy decision missing")
    check("DEC-M0-002" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "repository-authority decision missing")
    check("DEC-C2-011" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "continuity-versioning decision missing")
    check("DEC-M0.5-001" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "work-practical scenario decision missing")
    check("DEC-M0.5-002" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "teaching-modes decision missing")
    check("DEC-M0.5-003" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "evidence-precision decision missing")
    check("DEC-C2-012" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "selective-context reliability decision missing")
    check("DEC-C2-013" in (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8"), "accelerated teaching decision missing")
    check("do not ask Jeremy to immediately repeat" in contract, "transfer-not-repetition teaching guard missing")
    check(all(term in contract for term in ["**Teach:**", "**Practice:**", "**Demonstrate:**"]), "visible teaching modes missing")
    check("Match evidence precision to the task stage" in contract, "task-stage evidence precision missing")
    check("accelerated, gap-based, and build-first" in contract, "build-first teaching rule missing")
    check("AI-assisted job-search monitor" in contract, "job-search transfer boundary missing")
    check("Selective startup" in prompt and "scan-only" in prompt and "Recovery index" in prompt, "selective startup prompt missing")
    check(state["reliability_maintenance"]["approved_mandatory_startup_words"] <= 17000, "context baseline exceeds ceiling")
    check(state["git_identity_readiness"]["use_config_only"] is True, "Git identity no-guessing safeguard missing")
    check(state["git_identity_readiness"]["practice_repository_decision"] == "remain_local_only", "practice repository privacy decision missing")
    check("AfterQuery" not in prompt and "work-trial priority check" not in prompt.lower(), "obsolete priority check remains")
    check(all(item["status"] == "Not started" for item in progress["capability_gates"]), "unearned capability gate advanced")


def main() -> None:
    course_setup.main if False else None
    course_setup.write_json(ROOT / "app" / "generated" / "data-quality-summary.json", course_setup.build_quality_summary(course_setup.read_rows()))
    course_setup.write_json(ROOT / "app" / "generated" / "progress-snapshot.json", course_setup.build_progress_snapshot())
    checks = [
        ("clean setup", verify_clean_setup),
        ("database controls and edge cases", verify_database_and_edges),
        ("controlled known-answer SQL", verify_known_answer),
        ("canonical progress mirror", verify_progress_snapshot),
        ("student solution gate", verify_student_gate),
        ("beginner entry point", verify_beginner_entry_point),
        ("v2 architecture and capability gates", verify_v2_architecture),
        ("credential and secret scan", verify_no_secrets),
    ]
    for label, function in checks:
        function()
        print(f"PASS: {label}")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "reconstruction_check.py")], cwd=ROOT, check=True)
    print(f"PASS: all deterministic prototype checks ({len(checks) + 1} groups)")


if __name__ == "__main__":
    main()
