# Course Repository Instructions

## Startup

1. Read `COURSE_CONTRACT.md`, `COURSE_STATE.json`, `PROGRESS.json`, `CAPABILITY_EVIDENCE_LEDGER.md`, `DECISION_LOG.md`, `SESSION_HANDOFF.md`, and `NEXT_CHAT_PROMPT.md` in full.
2. Read the current lesson specification, its prerequisite learner evidence, and artifacts explicitly required for the current learner submission or decision.
3. Apply the authority hierarchy in `COURSE_CONTRACT.md`; Jeremy's latest explicit instruction is highest authority.
4. Work on only the lesson authorized by `COURSE_STATE.json`. Use one fresh task per lesson and never infer mastery from working software alone.
5. Run `python3 scripts/reliability_scan.py`. Use its compact structured result to check the repository; do not paste or load the scanned source text into the task.

Completed lessons, older evidence, dictionaries, and architecture references are on-demand context. Read only the files needed to resolve a cited dependency, conflict, ambiguity, recovery problem, or quality failure. Record which files were read directly and which were handled by scan-only or on-demand checks. If selective context cannot reconcile a critical fact, expand first to the relevant module history and disclose that fallback.

Inspect `COURSE_STATE.json` for a due reliability-maintenance stage. Read `COURSE_RELIABILITY_PLAN.md` only when a stage or threshold is due; do not add its maintenance procedure to every lesson task.

## Authority and privacy

- The authoritative source is private GitHub repository `jeremybernhardt/ai-operations-builder-course-private` on `main`, as recorded in `COURSE_STATE.json`. Versioned ZIP exports are recovery backups, not competing sources of truth.
- This repository contains private curriculum, instructor-only material, learner evidence, and assistance history. It must remain private and must never be converted into the public portfolio repository.
- Treat chat history, saved memory, portal state, browser-local notes, and generated snapshots as non-authoritative.
- Never request, display, commit, or publish passwords, tokens, credentials, personal email addresses, or actual `.env` files.
- Obtain Jeremy's explicit informed approval before consequential external actions, including push, publication, deployment, repository or account creation, visibility or collaborator changes, destructive remote operations, or paid services. Existing authentication is capability, not continuing authorization.

## Environment and startup

- Verified environment: Git `2.50.1 (Apple Git-155)`, GitHub CLI `2.97.0`, Node.js `24.18.0`, npm `11.16.0`, and Python `3.13.14`. Verify rather than reinstall.
- Learner entry point: `START_HERE.html`.
- Start the local Course Portal with `npm run course`.
- Do not start the Course Portal merely to validate source files. Bound interactive commands and stop course-owned processes at closeout.
- Use `.env.example` only as a placeholder template; keep actual secrets in an ignored local `.env`.

## Lesson recovery and delivery

- Acknowledge a learner answer before beginning lengthy tool work. If a task is interrupted, recover the latest answer and current-lesson artifacts before asking Jeremy to repeat anything.
- During tool work, provide visible progress at least every 60 seconds. Treat two minutes without observable progress from a course-owned command as a stall: stop or interrupt it when safe, preserve the recovery boundary, and retry a bounded step. A host or task freeze cannot self-report; recover from canonical state and saved artifacts rather than claiming an invisible timer worked.
- Treat current-lesson artifacts as unverified until the checkpoint passes. Preserve them without advancing progress, mastery, or authorization.
- Use accelerated, gap-based, build-first instruction. Count prior evidence when it genuinely proves a capability, but do not infer technical verification skill from general AI supervision or working output.
- Keep learner-facing openings and endings brief and plain. Put inventories, versions, test commands, hashes, and maintenance detail in the background unless Jeremy needs them for a decision or approval.

## Verification

- Run `npm run test:reliability`, `python3 scripts/reconstruction_check.py`, `npm test`, `npm run lint`, and `npm run validate:artifact` for relevant release changes.
- Validate every JSON file structurally and run a secret scan before any push or packaging.
- Inspect the relevant implementation whenever plausible output could conceal a material logic, data, privacy, permission, or destination error.
- Before a push, inspect the complete outgoing commit history, tracked file list, author and committer metadata, remote URL, branch, exclusions, and destination.
- After a push, verify the GitHub owner, private visibility, default branch, commit ID, expected files, local tracking relationship, exclusions, and clean reconstruction independently.
- Record deterministic evidence, Jeremy's reasoning, the maximum assistance used, limitations, and any mastery boundary honestly.
