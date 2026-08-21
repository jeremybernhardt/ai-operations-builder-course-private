# Course Bundle Manifest

Backup bundle: `AI_Operations_Builder_Course_Prototype_v2.0.5_M0.5-L1.zip`

The backup name retains `Prototype` for continuity with the verified v1.2.0 folder. The required v2.0.0 course architecture is broader; v2.0.1-v2.0.4 added operator-builder, safe-execution, identity/privacy, teaching, and private-repository authority records. v2.0.5 adds the verified work-practical M0.5-L1 builder-specification checkpoint. Future lessons remain unbuilt beyond their bounded blueprint.

## Learner entry point

| File | Role |
|---|---|
| `START_HERE.html` | Plain-language local start, privacy, and stop instructions. |
| `README.md` | Technical setup, verification, continuity, and recovery reference. |

## Canonical files

| File | Role |
|---|---|
| `AGENTS.md` | Repository startup, authority, environment, privacy, and verification instructions. |
| `COURSE_CONTRACT.md` | v2.0.5 purpose, constraints, operator-builder and AI-execution standards, technical/finance boundaries, teaching rules, privacy, and authority. |
| `CURRICULUM_MAP.md` | Bounded required modules `M0`-`M12`, preserved `P0`, and optional `OH1`. |
| `COURSE_STATE.json` | Current checkpoint, approvals, blockers, next action, and authorization boundary. |
| `PROGRESS.json` | Learner mastery and assistance evidence; authoritative over portal progress. |
| `CAPABILITY_EVIDENCE_LEDGER.md` | Evidence requirements and status for SQL, Python, work-dashboard, automation, applied-AI, and agent claims. |
| `LESSON_TEMPLATE.md` | Stage order, technical-first objectives, help levels, failure cases, mastery, and handoff rules. |
| `PROJECT_SPEC.md` | Preserved `P0` scenario, boundaries, requirements, and relationship to the current course. |
| `METRIC_DICTIONARY.md` | Preserved first-pass metric checkpoint record. |
| `DATA_DICTIONARY.md` | Preserved synthetic prototype dataset fields and controls. |
| `DECISION_LOG.md` | Append-only decisions, including the retarget, operator-builder standard, safe AI execution, identity/privacy choice, and transfer-not-repetition correction. |
| `SESSION_HANDOFF.md` | Factual briefing for the next conversation. |
| `NEXT_CHAT_PROMPT.md` | Exact instructions for the fresh task that teaches only `M0.5-L2`. |

## Module 0 materials

| Path | Role |
|---|---|
| `lesson/M0-L1_LOCAL_GIT_FOUNDATIONS.md` | Completed first Module 0 lesson specification and mastery boundary. |
| `evidence/LEARNER_CHECKPOINT_M0-C1.md` | Verified learner evidence for local Git foundations. |
| `lesson/M0-L2_LOCAL_BRANCHES_MERGES_SAFE_RECOVERY.md` | Completed second Module 0 lesson specification and mastery boundary. |
| `evidence/LEARNER_CHECKPOINT_M0-C2.md` | Verified learner evidence for branches, merges, recovery, and verification. |
| `lesson/M0-L3_GIT_IDENTITY_PRIVACY_GITHUB_READINESS.md` | Completed third Module 0 lesson specification and mastery boundary. |
| `evidence/LEARNER_CHECKPOINT_M0-C3.md` | Verified learner evidence for Git identity, privacy, scope, and readiness. |
| `lesson/M0-L4_PRIVATE_GITHUB_COURSE_REPOSITORY_FIRST_VERIFIED_PUSH.md` | Completed fourth Module 0 lesson specification and mastery boundary. |
| `evidence/LEARNER_CHECKPOINT_M0-C4.md` | Verified learner evidence for private repository specification, approval, push, and reconstruction. |

## Module 0.5 materials

| Path | Role |
|---|---|
| `lesson/M0.5-L1_DEFINING_OUTCOMES_CONSTRAINTS_DONE_CRITERIA.md` | Completed first builder-supervision lesson specification and mastery boundary. |
| `student/M0.5-L1_EXPENSE_FILE_READINESS_BUILD_BRIEF.md` | Guided work-practical learner build brief. |
| `evidence/LEARNER_CHECKPOINT_M0.5-C1.md` | Verified learner decisions, transfer result, assistance, limitations, and advancement boundary. |

## Preserved prototype materials

| Path | Role |
|---|---|
| `lesson/stages/` | Preserved staged `P0-L1` learner materials. |
| `student/first_pass_acceptance.sql` | Intentionally incomplete learner SQL scaffold. |
| `data/project_task_reviews.csv` | Fully synthetic review-event data. |
| `database/prototype.sqlite` | Reproducible local SQLite database. |
| `instructor_only/` | Controlled reference logic, expected results, and challenge fixture; never linked from student materials. |
| `evidence/LEARNER_CHECKPOINT_P0-C1.md` | Honest learner evidence for the completed prototype checkpoint. |
| `evidence/RELEASE_CHECKS.md` | Preserved v1.2.0 prototype release evidence. |
| `evidence/RECONSTRUCTION_CHECK.md` | Preserved v1.2.0 reconstruction evidence. |

## Application

| Path | Role |
|---|---|
| `app/page.tsx` | Local application entry. |
| `app/course-experience.tsx` | Course Portal summary, preserved KPI Lab review, and continuity closeout. |
| `app/globals.css` | Responsive visual system. |
| `app/layout.tsx` | Page metadata and root layout. |
| `app/generated/` | Generated data-quality and read-only progress snapshots. |
| `public/artifacts/` | Generated read-only canonical copies linked from the Course Portal. |

## Setup and verification

| Path | Role |
|---|---|
| `scripts/setup.py` | Validates CSV, rebuilds SQLite, and generates snapshots/artifact copies. |
| `scripts/start-course.sh` | Checks prerequisites, installs locked components when absent, prepares data, and starts the local site. |
| `scripts/verify.py` | Deterministic prototype plus v2.0.5 course-state, M0/M0.5 evidence, repository authority, and capability-gate checks. |
| `scripts/reconstruction_check.py` | Confirms a fresh task can recover v2.0.5 private-repository authority, boundaries, evidence, and next action. |
| `scripts/package_bundle.py` | Creates the clean v2.0.5 M0.5-L1 backup ZIP without dependencies, runtime files, Git history, or macOS metadata. |
| `tests/rendered-html.test.mjs` | Verifies rendered Course Portal, preserved KPI Lab, and v2.0.5 continuity labels. |
| `package.json` / `package-lock.json` | Reproducible Node application dependencies and commands. |
| `pyproject.toml` / `.python-version` | Prototype Python compatibility declaration. |
| `.env.example` / `.gitignore` | Secret boundary and transient-file exclusions. |
| `evidence/RELEASE_CHECKS_v2.0.0.md` | v2.0.0 release results. |
| `evidence/RECONSTRUCTION_CHECK_v2.0.0.md` | v2.0.0 continuity results. |
| `evidence/RELEASE_CHECKS_v2.0.1.md` | v2.0.1 release results. |
| `evidence/RECONSTRUCTION_CHECK_v2.0.1.md` | v2.0.1 continuity results. |
| `evidence/RELEASE_CHECKS_v2.0.2.md` | v2.0.2 release results. |
| `evidence/RECONSTRUCTION_CHECK_v2.0.2.md` | v2.0.2 continuity results. |
| `evidence/RELEASE_CHECKS_v2.0.3.md` | v2.0.3 release results. |
| `evidence/RECONSTRUCTION_CHECK_v2.0.3.md` | v2.0.3 continuity results. |
| `evidence/RELEASE_CHECKS_v2.0.4.md` | v2.0.4 release results. |
| `evidence/RECONSTRUCTION_CHECK_v2.0.4.md` | v2.0.4 continuity results. |
| `evidence/RELEASE_CHECKS_v2.0.5.md` | v2.0.5 release results. |
| `evidence/RECONSTRUCTION_CHECK_v2.0.5.md` | v2.0.5 continuity results. |

## Intentionally absent

- Future full lessons, future datasets, solution code, and answer keys
- The finance flagship implementation or learner-built work dashboard
- External database, API, automation, runtime AI, or agent implementation
- Optional `OH1` implementation
- Public GitHub course repository
- Public deployment or public portfolio repository
- Standalone multi-user course product
