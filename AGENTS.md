# Course Repository Instructions

## Startup

1. Read `COURSE_CONTRACT.md`, `COURSE_STATE.json`, `PROGRESS.json`, `CAPABILITY_EVIDENCE_LEDGER.md`, `DECISION_LOG.md`, `SESSION_HANDOFF.md`, and `NEXT_CHAT_PROMPT.md` in full.
2. Read the current lesson specification and its prerequisite learner evidence before acting.
3. Apply the authority hierarchy in `COURSE_CONTRACT.md`; Jeremy's latest explicit instruction is highest authority.
4. Work on only the lesson authorized by `COURSE_STATE.json`. Use one fresh task per lesson and never infer mastery from working software alone.

## Authority and privacy

- The authoritative source is the location recorded in `COURSE_STATE.json`. Until its GitHub transition is recorded and verified, the complete versioned bundle remains authoritative.
- This repository contains private curriculum, instructor-only material, learner evidence, and assistance history. It must remain private and must never be converted into the public portfolio repository.
- Treat chat history, saved memory, portal state, browser-local notes, and generated snapshots as non-authoritative.
- Never request, display, commit, or publish passwords, tokens, credentials, personal email addresses, or actual `.env` files.
- Obtain Jeremy's explicit informed approval before consequential external actions, including repository creation, remote connection, push, publication, deployment, account creation, or paid services.

## Environment and startup

- Verified environment: Git `2.50.1 (Apple Git-155)`, Node.js `24.18.0`, npm `11.16.0`, and Python `3.13.14`. Verify rather than reinstall.
- Learner entry point: `START_HERE.html`.
- Start the local Course Portal with `npm run course`.
- Use `.env.example` only as a placeholder template; keep actual secrets in an ignored local `.env`.

## Verification

- Run `python3 scripts/reconstruction_check.py`, `npm test`, `npm run lint`, and `npm run validate:artifact` for relevant release changes.
- Validate every JSON file structurally and run a secret scan before any push or packaging.
- Inspect the relevant implementation whenever plausible output could conceal a material logic, data, privacy, permission, or destination error.
- Before a push, inspect the complete outgoing commit history, tracked file list, author and committer metadata, remote URL, branch, exclusions, and destination.
- After a push, verify the GitHub owner, private visibility, default branch, commit ID, expected files, local tracking relationship, exclusions, and clean reconstruction independently.
- Record deterministic evidence, Jeremy's reasoning, the maximum assistance used, limitations, and any mastery boundary honestly.
