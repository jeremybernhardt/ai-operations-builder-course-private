#!/usr/bin/env python3
"""Verify that a fresh Codex task can reconstruct the v2.0.8 course state."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CANONICAL = [
    "AGENTS.md",
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
    "COURSE_RELIABILITY_PLAN.md",
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
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    lessons = {item["lesson_id"]: item for item in progress["lessons"]}
    identity = state.get("git_identity_readiness", {})
    source = state.get("authoritative_source", {})
    repository = state.get("private_repository_readiness", {})

    lesson_pairs = [
        ("lesson/M0-L1_LOCAL_GIT_FOUNDATIONS.md", "evidence/LEARNER_CHECKPOINT_M0-C1.md"),
        ("lesson/M0-L2_LOCAL_BRANCHES_MERGES_SAFE_RECOVERY.md", "evidence/LEARNER_CHECKPOINT_M0-C2.md"),
        ("lesson/M0-L3_GIT_IDENTITY_PRIVACY_GITHUB_READINESS.md", "evidence/LEARNER_CHECKPOINT_M0-C3.md"),
        ("lesson/M0-L4_PRIVATE_GITHUB_COURSE_REPOSITORY_FIRST_VERIFIED_PUSH.md", "evidence/LEARNER_CHECKPOINT_M0-C4.md"),
        ("lesson/M0.5-L1_DEFINING_OUTCOMES_CONSTRAINTS_DONE_CRITERIA.md", "evidence/LEARNER_CHECKPOINT_M0.5-C1.md"),
        ("lesson/M0.5-L2_REVIEWING_AI_BUILDER_PLAN_ASSUMPTIONS_SCOPE.md", "evidence/LEARNER_CHECKPOINT_M0.5-C2.md"),
        ("lesson/M0.5-L3_REVIEWING_AI_GENERATED_DIFF_VERIFICATION_EVIDENCE.md", "evidence/LEARNER_CHECKPOINT_M0.5-C3.md"),
        ("lesson/M0.5-L4_DEBUGGING_FROM_EVIDENCE_BOUNDED_MODIFICATION.md", "evidence/LEARNER_CHECKPOINT_M0.5-C4.md"),
    ]

    checks = {
        "valid_state_schema": state.get("schema_version") == "2.0.0",
        "valid_progress_schema": progress.get("schema_version") == "2.0.0",
        "release_is_v2_0_8": state.get("release_version") == "2.0.8" and progress.get("release_version") == "2.0.8",
        "private_repository_is_authoritative": source.get("type") == "private_git_repository",
        "exact_repository_recoverable": source.get("repository_full_name") == "jeremybernhardt/ai-operations-builder-course-private",
        "private_visibility_recoverable": source.get("visibility") == "private" and repository.get("visibility") == "private",
        "main_branch_recoverable": source.get("default_branch") == "main" and repository.get("default_branch") == "main",
        "baseline_commit_recoverable": source.get("first_verified_push_commit") == "07170d06922211c5e4379fa4c534ea93da08dd0b",
        "backup_is_not_authority": source.get("backup_role") == "verified_backup_not_primary_authority",
        "m0_5_c4_current": state.get("current_checkpoint_id") == "M0.5-C4",
        "m0_sequence_complete_without_mastery_inflation": state.get("preserved_m0_module_status", {}).get("planned_lesson_sequence_complete") is True and state.get("preserved_m0_module_status", {}).get("independent_mastery_claimed") is False,
        "m0_5_sequence_not_overclaimed": state.get("module_status", {}).get("planned_lesson_sequence_complete") is False and state.get("module_status", {}).get("independent_mastery_claimed") is False,
        "prototype_status_honest": lessons.get("P0-L1", {}).get("mastery_status") == "Completed with substantial assistance",
        "m0_l1_status_honest": lessons.get("M0-L1", {}).get("mastery_status") == "Completed with limited assistance",
        "m0_l2_status_honest": lessons.get("M0-L2", {}).get("mastery_status") == "Completed with substantial assistance",
        "m0_l3_status_honest": lessons.get("M0-L3", {}).get("mastery_status") == "Completed with substantial assistance",
        "m0_l4_status_honest": lessons.get("M0-L4", {}).get("mastery_status") == "Completed with substantial assistance",
        "m0_5_l1_status_honest": lessons.get("M0.5-L1", {}).get("mastery_status") == "Completed with limited assistance",
        "m0_5_l2_status_honest": lessons.get("M0.5-L2", {}).get("mastery_status") == "Completed with limited assistance",
        "m0_5_l3_status_honest": lessons.get("M0.5-L3", {}).get("mastery_status") == "Completed with limited assistance",
        "m0_5_l4_status_honest": lessons.get("M0.5-L4", {}).get("mastery_status") == "Completed with limited assistance",
        "all_completed_lesson_evidence_present": all((ROOT / lesson).is_file() and (ROOT / evidence).is_file() for lesson, evidence in lesson_pairs),
        "all_completed_lesson_evidence_named": all(lesson in prompt and evidence in prompt for lesson, evidence in lesson_pairs),
        "completed_history_is_on_demand": "Recovery index" in prompt and "on demand, not startup context" in prompt,
        "guided_build_brief_present": (ROOT / "student/M0.5-L1_EXPENSE_FILE_READINESS_BUILD_BRIEF.md").is_file(),
        "original_and_reviewed_plan_present": all((ROOT / name).is_file() for name in ["student/M0.5-L2_EXPENSE_FILE_READINESS_AI_PLAN.md", "student/M0.5-L2_EXPENSE_FILE_READINESS_REVIEWED_PLAN.md"]),
        "guided_and_transfer_diff_reviews_present": all((ROOT / name).is_file() for name in ["student/M0.5-L3_ANNOTATED_DIFF_REVIEW.md", "student/M0.5-L3_CASH_SCHEDULE_TRANSFER_PACKET.md", "student/M0.5-L3_CASH_DISBURSEMENT_ACCEPTANCE_FIXTURE.xlsx.inspect.ndjson"]),
        "debugging_and_transfer_artifacts_present": all((ROOT / name).is_file() for name in ["student/M0.5-L4_DEBUGGING_AND_BOUNDED_MODIFICATION_RECORD.md", "student/m0_5_l4/payment_release.py", "student/m0_5_l4/test_payment_release.py", "student/m0_5_l4/review_routing.py", "student/m0_5_l4/test_review_routing.py"]),
        "one_lesson_per_task_recoverable": state.get("lesson_chat_policy") == "one_lesson_per_new_chat",
        "next_lesson_named": "M0.5-L5" in prompt and "Explaining Human and AI Contributions Without Inflation" in prompt,
        "next_scope_bounded": "current authorization covers only `m0.5-l5" in prompt.lower(),
        "authoritative_files_named": all(name in prompt for name in REQUIRED_CANONICAL),
        "repository_startup_instructions": "authoritative private GitHub repository" in prompt and "private visibility" in prompt,
        "zip_not_required": "recovery backup only" in prompt and "not" in prompt,
        "versioned_exports_named": all(name in handoff + prompt for name in ["SESSION_HANDOFF_M0.5-L4_v2.0.8.md", "NEXT_CHAT_PROMPT_AFTER_M0.5-L4_v2.0.8.md", "AI_Operations_Builder_Course_Prototype_v2.0.8_M0.5-L4.zip"]),
        "handoff_has_verification_and_unfinished": "Verification and limitations" in handoff and "What remains unfinished" in handoff,
        "setup_command_recoverable": "npm ci" in readme and "python3 scripts/setup.py" in readme,
        "start_command_recoverable": "npm run course" in readme,
        "beginner_entry_point_present": (ROOT / "START_HERE.html").is_file(),
        "test_command_recoverable": "npm test" in readme,
        "reliability_test_recoverable": "npm run test:reliability" in readme and (ROOT / "scripts/reliability_scan.py").is_file(),
        "external_approval_guard": "explicit informed approval" in prompt and "existing authentication" in prompt.lower(),
        "public_repository_prohibited": "public/portfolio repository" in prompt,
        "practice_repository_local_only": identity.get("practice_repository_decision") == "remain_local_only" and "local-only" in prompt,
        "identity_name_recoverable": identity.get("user_name") == "Jeremy Bernhardt",
        "identity_email_recoverable": identity.get("user_email") == "306348304+jeremybernhardt@users.noreply.github.com",
        "identity_guard_recoverable": identity.get("use_config_only") is True,
        "practice_history_excluded": repository.get("practice_history_included") is False,
        "fresh_clone_verified": repository.get("fresh_clone_reconstruction_verified") is True,
        "keychain_recoverable": repository.get("credential_storage") == "macos_keychain",
        "technical_subject_guard": "Finance is the primary application context" in contract,
        "operator_builder_target": "AI-assisted operator-builder proficiency" in contract,
        "blank_page_guard": "write substantial programs from a blank page" in contract,
        "output_plus_inspection": "Output-based testing is the primary starting point" in contract and "targeted inspection" in contract,
        "independent_modification_defined": "AI assistance is permitted but must be disclosed" in contract,
        "sql_python_balance": "Give SQL somewhat more direct practice" in contract and "tracing, troubleshooting, modifying, and reusing" in contract,
        "ai_execution_default": "AI should also execute routine local implementation" in contract,
        "command_recall_guard": "Do not grade command-sequence or syntax recall" in contract,
        "ai_execution_decision_recorded": "DEC-C2-009" in decisions,
        "teaching_decision_recorded": "DEC-C2-010" in decisions,
        "identity_decision_recorded": "DEC-M0-001" in decisions,
        "repository_decision_recorded": "DEC-M0-002" in decisions,
        "versioning_decision_recorded": "DEC-C2-011" in decisions,
        "work_practical_decision_recorded": "DEC-M0.5-001" in decisions,
        "teaching_modes_decision_recorded": "DEC-M0.5-002" in decisions,
        "evidence_precision_decision_recorded": "DEC-M0.5-003" in decisions,
        "selective_context_decision_recorded": "DEC-C2-012" in decisions,
        "accelerated_teaching_decision_recorded": "DEC-C2-013" in decisions,
        "selective_context_guard": all(term in prompt for term in ["Selective startup", "scan-only", "Recovery index"]),
        "context_baseline_bounded": state.get("reliability_maintenance", {}).get("approved_mandatory_startup_words", 99999) <= 17000,
        "build_first_guard": "accelerated, gap-based, and build-first" in contract,
        "job_search_transfer_bounded": "AI-assisted job-search monitor" in contract and "not a second curriculum" in curriculum,
        "transfer_not_repetition_guard": "do not ask Jeremy to immediately repeat" in contract and "genuinely different" in prompt,
        "teach_practice_demonstrate_guard": all(term in contract for term in ["**Teach:**", "**Practice:**", "**Demonstrate:**"]),
        "task_stage_evidence_guard": "Match evidence precision to the task stage" in contract and "deterministic" in prompt,
        "course_portal_not_dashboard_evidence": "does not count as dashboard-building evidence" in contract,
        "portal_companion_boundary": "Course Portal is non-authoritative" in prompt,
        "work_dashboard_gate_present": "GATE-WORK-DASHBOARD" in ledger and "Work Dashboard and Decision Layer" in curriculum,
        "permissioned_agent_present": "Permissioned Tool-Using Agent" in curriculum and "sandbox actions" in curriculum,
        "human_data_optional": "Optional Human-Data and AI Operations Transfer" in curriculum,
        "all_capability_gates_unstarted": all(item["status"] == "Not started" for item in progress["capability_gates"]),
        "obsolete_priority_check_removed": "work-trial priority check" not in prompt.lower() and "AfterQuery" not in prompt,
        "remote_practice_not_authorized": "remote_practice_repository" in state.get("scope_guard", {}).get("not_authorized", []),
        "repository_state_recoverable": all(value in handoff for value in ["b1bf13d", "ffdad15", "2bf6eae", "79d4537", "seven commits", "no remote"]),
        "agents_authority_updated": "authoritative source is private GitHub repository" in agents,
        "agents_selective_startup": "on-demand context" in agents and "reliability_scan.py" in agents,
        "operational_stall_guard": "two minutes without observable progress" in agents and "cannot self-report" in agents,
    }
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise SystemExit(f"Reconstruction checks failed: {failed}")
    print(f"Reconstruction check passed ({len(checks)} checks).")


if __name__ == "__main__":
    main()
