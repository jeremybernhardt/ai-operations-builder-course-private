#!/usr/bin/env python3
"""Verify that a fresh Work chat can reconstruct the v2.0.3 next objective."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CANONICAL = [
    "COURSE_CONTRACT.md",
    "CURRICULUM_MAP.md",
    "COURSE_STATE.json",
    "PROGRESS.json",
    "CAPABILITY_EVIDENCE_LEDGER.md",
    "LESSON_TEMPLATE.md",
    "PROJECT_SPEC.md",
    "METRIC_DICTIONARY.md",
    "DATA_DICTIONARY.md",
    "DECISION_LOG.md",
    "SESSION_HANDOFF.md",
    "NEXT_CHAT_PROMPT.md",
]


def main() -> None:
    missing = [name for name in REQUIRED_CANONICAL if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit(f"Missing canonical files: {missing}")

    state = json.loads((ROOT / "COURSE_STATE.json").read_text(encoding="utf-8"))
    progress = json.loads((ROOT / "PROGRESS.json").read_text(encoding="utf-8"))
    prompt = (ROOT / "NEXT_CHAT_PROMPT.md").read_text(encoding="utf-8")
    handoff = (ROOT / "SESSION_HANDOFF.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    contract = (ROOT / "COURSE_CONTRACT.md").read_text(encoding="utf-8")
    curriculum = (ROOT / "CURRICULUM_MAP.md").read_text(encoding="utf-8")
    ledger = (ROOT / "CAPABILITY_EVIDENCE_LEDGER.md").read_text(encoding="utf-8")
    decisions = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")

    lessons = {item["lesson_id"]: item for item in progress["lessons"]}
    identity = state.get("git_identity_readiness", {})

    checks = {
        "valid_state_schema": state.get("schema_version") == "2.0.0",
        "valid_progress_schema": progress.get("schema_version") == "2.0.0",
        "release_is_v2_0_3": state.get("release_version") == "2.0.3" and progress.get("release_version") == "2.0.3",
        "bundle_is_authoritative": state.get("authoritative_source", {}).get("bundle_name") == "AI_Operations_Builder_Course_Prototype_v2.0.3.zip",
        "architecture_approved": state.get("course_architecture_approval", {}).get("status") == "approved",
        "m0_position_recoverable": state.get("current_module_id") == "M0" and state.get("current_checkpoint_id") == "M0-C3",
        "m0_c3_evidence_preserved": state.get("last_verified_learner_checkpoint", {}).get("status") == "completed_with_substantial_assistance",
        "prototype_evidence_preserved": lessons.get("P0-L1", {}).get("mastery_status") == "Completed with substantial assistance",
        "m0_l1_status_honest": lessons.get("M0-L1", {}).get("mastery_status") == "Completed with limited assistance",
        "m0_l2_status_honest": lessons.get("M0-L2", {}).get("mastery_status") == "Completed with substantial assistance",
        "m0_l3_status_honest": lessons.get("M0-L3", {}).get("mastery_status") == "Completed with substantial assistance",
        "one_lesson_per_chat_recoverable": state.get("lesson_chat_policy") == "one_lesson_per_new_chat",
        "next_lesson_named": "M0-L4" in prompt and "Private GitHub Course Repository and First Verified Push" in prompt,
        "attachments_named": all(name in prompt for name in ["AI_Operations_Builder_Course_Prototype_v2.0.3.zip", "SESSION_HANDOFF.md", "NEXT_CHAT_PROMPT.md"]),
        "authoritative_files_named": all(name in prompt for name in REQUIRED_CANONICAL[:7]),
        "m0_evidence_files_named": all(
            name in prompt
            for name in [
                "lesson/M0-L1_LOCAL_GIT_FOUNDATIONS.md",
                "evidence/LEARNER_CHECKPOINT_M0-C1.md",
                "lesson/M0-L2_LOCAL_BRANCHES_MERGES_SAFE_RECOVERY.md",
                "evidence/LEARNER_CHECKPOINT_M0-C2.md",
                "lesson/M0-L3_GIT_IDENTITY_PRIVACY_GITHUB_READINESS.md",
                "evidence/LEARNER_CHECKPOINT_M0-C3.md",
            ]
        ),
        "handoff_has_verification_and_unfinished": "Verification" in handoff and "Unfinished" in handoff,
        "continuity_roles_explained": "factual briefing" in handoff and "exact instructions" in handoff,
        "github_transition_explained": "becomes authoritative" in prompt and "Repeated ZIP attachments should end" in handoff,
        "setup_command_recoverable": "npm ci" in readme and "python3 scripts/setup.py" in readme,
        "start_command_recoverable": "npm run course" in readme,
        "beginner_entry_point_present": (ROOT / "START_HERE.html").is_file(),
        "m0_l1_evidence_present": (ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C1.md").is_file(),
        "m0_l2_evidence_present": (ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C2.md").is_file(),
        "m0_l3_evidence_present": (ROOT / "evidence" / "LEARNER_CHECKPOINT_M0-C3.md").is_file(),
        "test_command_recoverable": "npm test" in readme,
        "external_approval_guard": "separate explicit informed approval" in prompt,
        "public_repository_prohibited": "Do not create a remote practice repository, public repository" in prompt,
        "practice_repository_local_only": identity.get("practice_repository_decision") == "remain_local_only" and "must remain local-only" in prompt,
        "identity_name_recoverable": identity.get("user_name") == "Jeremy Bernhardt",
        "identity_email_recoverable": identity.get("user_email") == "306348304+jeremybernhardt@users.noreply.github.com",
        "identity_guard_recoverable": identity.get("use_config_only") is True,
        "old_commits_unchanged": identity.get("existing_practice_commits_changed") is False and "all seven existing practice commits retain" in prompt,
        "technical_subject_guard": "Finance is the primary application context" in contract,
        "operator_builder_target": "AI-assisted operator-builder proficiency" in contract,
        "blank_page_guard": "write substantial programs from a blank page" in contract,
        "output_plus_inspection": "Output-based testing is the primary starting point" in contract and "targeted inspection" in contract,
        "independent_modification_defined": "AI assistance is permitted but must be disclosed" in contract,
        "sql_python_balance": "Give SQL somewhat more direct practice" in contract and "tracing, troubleshooting, modifying, and reusing" in contract,
        "ai_execution_default": "AI should also execute routine local implementation" in contract,
        "command_recall_guard": "Do not grade command-sequence or syntax recall" in contract,
        "ai_execution_decision_recorded": "DEC-C2-009" in decisions,
        "identity_decision_recorded": "DEC-M0-001" in decisions,
        "teaching_decision_recorded": "DEC-C2-010" in decisions,
        "transfer_not_repetition_guard": "do not ask Jeremy to immediately repeat" in contract and "genuinely new" in prompt,
        "course_portal_not_dashboard_evidence": "does not count as dashboard-building evidence" in contract,
        "work_dashboard_gate_present": "GATE-WORK-DASHBOARD" in ledger and "Work Dashboard and Decision Layer" in curriculum,
        "permissioned_agent_present": "Permissioned Tool-Using Agent" in curriculum and "sandbox actions" in curriculum,
        "human_data_optional": "Optional Human-Data and AI Operations Transfer" in curriculum,
        "all_capability_gates_unstarted": all(item["status"] == "Not started" for item in progress["capability_gates"]),
        "obsolete_priority_check_removed": "work-trial priority check" not in prompt.lower() and "AfterQuery" not in prompt,
        "scope_remains_bounded": "current authorization covers only `M0-L4" in prompt,
        "remote_practice_not_authorized": "remote_practice_repository" in state.get("scope_guard", {}).get("not_authorized", []),
        "repository_state_recoverable": all(value in handoff for value in ["b1bf13d", "ffdad15", "2bf6eae", "79d4537", "seven commits", "no remote"]),
        "m0_l3_lesson_present": (ROOT / "lesson" / "M0-L3_GIT_IDENTITY_PRIVACY_GITHUB_READINESS.md").is_file(),
    }
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise SystemExit(f"Reconstruction checks failed: {failed}")
    print(f"Reconstruction check passed ({len(checks)} checks).")


if __name__ == "__main__":
    main()
