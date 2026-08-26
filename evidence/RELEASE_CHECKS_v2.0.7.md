# Release Checks — v2.0.7

Release checkpoint: `ARCH-RG1-v2.0.7`

Date: `2026-08-26`

## Release scope

- Record `M0.5-L3` / `M0.5-C3` as completed with limited assistance without claiming independent mastery or a resume-level gate.
- Preserve Jeremy's guided budget-variance review and recover his submitted cash-disbursement acceptance response from prior task history.
- Verify that response against the tracked text inspection record without reopening the binary workbook.
- Prepare only `M0.5-L4 — Debugging from Evidence and Directing a Bounded Modification` for a fresh task.
- Update canonical state, progress, capability evidence, continuity, portal mirrors, verification, and backup instructions.
- Make future reliability scans metadata-only for binary workbooks and exclude binary workbooks plus transient `.codex-*` verifier files from backup packaging.

## Deterministic verification

Passed locally:

- structural JSON validation for `COURSE_STATE.json` and `PROGRESS.json`;
- `npm run test:reliability`: 8 unit tests plus the bounded repository scan;
- final reliability scan: 151 files inventoried, 13 JSON files valid, one transient Excel lock ignored, one workbook recorded metadata-only, no source excerpts, and no failures or warnings;
- mandatory startup: 15,348 words, 51.87% below the 31,889-word legacy baseline and below the 17,000-word ceiling;
- `python3 scripts/reconstruction_check.py`: 85 checks;
- `npm test`: reliability, 9 deterministic prototype/course groups, reconstruction, production build, and 2 rendered tests;
- `npm run lint`;
- `npm run validate:artifact`;
- credential and secret scan inside `scripts/verify.py`; and
- `git diff --check` before proposed commit review.

## Learner-evidence decision

Jeremy correctly identified that the delivered cash schedule needed revision: row and amount controls passed, but the builder inferred a date for `INV-203`, bypassed manual review, and overstated September cash. He requested inspection of the narrow date-selection rule and explained why amount reconciliation did not prove date correctness.

The instructor supplied the exact expected refinement during recovery: September `$19,950`, October `$3,100`, one manual-review row, and `INV-203` unscheduled. Limited assistance is recorded for this refinement, the earlier clarification of “narrow implementation rule,” and guided practice corrections. Independent mastery is not claimed.

## External-action boundary

No commit, push, deployment, publication, account, paid service, visibility change, or collaborator change was performed during release preparation. Any commit and private push require Jeremy's explicit informed approval after outgoing changes, metadata, exclusions, destination, and recovery boundary are shown.

## Backup result

The versioned backup bundle is `AI_Operations_Builder_Course_Prototype_v2.0.7_M0.5-L3.zip` with 146 files. Archive CRC verification passed. Binary workbooks and the transient `.codex-m05l3-verify.mjs` file are excluded; the tracked text inspection record is included. The final size and SHA-256 are reported at delivery so the archive does not contain a self-referential digest.
