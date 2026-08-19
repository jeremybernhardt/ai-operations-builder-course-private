# Prototype v1.2.0 Release Evidence

Release gate: `P0-RG1-v1.2.0`

Status: Passed

Verified: `2026-07-18`

## Deterministic checks

Command: `npm test`

Passed checks:

- clean Python setup in an isolated temporary directory;
- exact 16-row CSV-to-SQLite reconciliation and unique raw `review_id` control;
- duplicate logical review, missing outcome, rework, and denominator-policy fixtures;
- instructor-only controlled SQL result matched the private expectation;
- independent Python reconciliation matched the controlled SQL result;
- generated portal progress exactly matched canonical `PROGRESS.json` and was labeled non-authoritative;
- actual `P0-C1` attempt evidence and guided-help level were preserved without claiming independent mastery;
- learner SQL remained incomplete and contained no executable solution;
- `START_HERE.html`, the single learner start command, local stop/privacy instructions, and executable start script were present;
- secret/credential scan found no suspected values;
- all 17 fresh-chat reconstruction checks passed;
- production application build and artifact validation passed; and
- rendered output tests confirmed the approved Course Portal state, guided KPI Lab, lesson closeout, continuity-role explanation, GitHub transition, local-draft controls, and absence of the private expected result.

The private known result is deliberately omitted from student-accessible evidence.

## Static quality checks

Command: `npm run lint`

Result: Passed with no lint errors.

## Private browser preview

Verified in the supported private agent preview:

- Course Portal rendered the approved prototype state, one-lesson-per-chat rule, preserved Course Progress, Learning Objectives, accurate timing, verification boundary, stable Course Artifacts, and collapsible roadmap.
- The portal's **Open lesson closeout** action opened the fifth KPI Lab stage directly.
- The closeout first explained the completed work, honest mastery boundary, and next Module 0 lesson.
- The continuity section appeared only after that explanation and clearly distinguished the complete ZIP, factual `SESSION_HANDOFF.md`, and exact `NEXT_CHAT_PROMPT.md`.
- The post-GitHub note explained that a verified private repository will replace repeated ZIP attachments without implying access to browser-local activity.
- Desktop full-page inspection found no clipped cards, broken hierarchy, or missing closeout content.
- No public deployment was created.

## Beginner start-path check

`npm run course` retains the verified prerequisite, locked-install, deterministic data-preparation, and private Vite start path. Jeremy's physical Mac previously started the same local application architecture successfully. The first physical-Mac run of v1.2.0 remains a learner-environment confirmation, not a build blocker or mastery claim.

## Durable bundle reconstruction

The complete v1.2.0 ZIP passed archive-integrity testing and was extracted into a fresh directory. From that extracted copy:

- the start script retained its executable permission;
- Python setup and all 17 reconstruction checks passed;
- a clean locked dependency installation completed;
- `npm test` passed all deterministic, build, and rendered-output checks;
- `npm run lint` passed; and
- `npm run validate:artifact` passed.

## Release interpretation

Jeremy explicitly approved the v1.1.0 teaching design and authorized the bounded v1.2.0 transition changes. v1.2.0 is the durable prototype closeout package and authorizes only the next Module 0 lesson in a fresh chat. It does not claim independent metric, SQL, or verification mastery and does not include later lessons, a repository, backend, public deployment, or standalone product.
