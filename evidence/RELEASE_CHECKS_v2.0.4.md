# Release Checks — v2.0.4

Release checkpoint: `ARCH-RG1-v2.0.4`
Date: `2026-08-19`
Result: **Passed**

## Scope verified

- Preserve the approved v2.0.0 architecture and v2.0.1-v2.0.3 clarifications.
- Record `M0-L4` / `M0-C4` as completed with substantial assistance without claiming independent mastery or a resume-level gate.
- Preserve all earlier learner evidence and keep every v2 capability gate `Not started`.
- Record the exact private repository, separately approved external actions, verified first-push baseline, credential boundary, and disposable-practice separation.
- Make private repository `jeremybernhardt/ai-operations-builder-course-private` on `main` authoritative and make the v2.0.4 M0-L4 ZIP a backup.
- Record `DEC-M0-002` and the lesson-versioned export naming rule `DEC-C2-011`.
- Bound the next fresh task to only `M0.5-L1 — Defining Outcomes, Constraints, and Done Criteria`.
- Preserve the v1.2.0 prototype logic, intentionally incomplete learner SQL, fixtures, and known-answer controls.

## Commands and checks

```text
python3 -m json.tool COURSE_STATE.json
python3 -m json.tool PROGRESS.json
python3 scripts/setup.py
python3 scripts/reconstruction_check.py
python3 scripts/verify.py
npm test
npm run lint
npm run validate:artifact
python3 scripts/package_bundle.py
unzip -t AI_Operations_Builder_Course_Prototype_v2.0.4_M0-L4.zip
```

The complete local closeout diff, tracked-file set, outgoing history, author and committer metadata, origin URL, branch/tracking state, exclusions, ignored files, and secret patterns were inspected before the closeout commit. The final commit SHA cannot be embedded inside that same commit without changing it; it is verified against GitHub after the approved push and reported in the lesson delivery record.

## Learner-evidence boundary

`M0-C4` is **Completed with substantial assistance**. Jeremy owned the intended repository specification, privacy boundary, and three consequential external approvals. The instructor supplied the repository/authentication model, detailed risk and verification framework, implementation, and most evidence interpretation. A successful push, passing software build, or completed Module 0 sequence does not establish independent mastery. No resume-level gate was earned.

## External and credential boundary

- Created only the approved empty private repository.
- Connected only the separate local course repository.
- Pushed only the inspected course history after explicit approval.
- Did not create a remote practice repository, public repository, deployment, paid resource, account, collaborator, or public artifact.
- Stored GitHub CLI authentication in macOS Keychain; no password, token, personal email, or credential was requested, displayed, or committed.
- Existing authentication remains distinct from future action approval.

## Results

- JSON structure: passed.
- Complete v2.0.3 source ZIP integrity and required inventory: passed before preparation.
- Effective Git identity/source and exact `noreply` address: passed.
- Disposable practice repository unchanged and remote-free: passed.
- First-push owner, name, private visibility, default branch, root commit/tree, 118-file equality, metadata, exclusions, tracking, and no-practice-history checks: passed.
- First-push fresh authenticated clone reconstruction, tests/build, lint, and artifact validation: passed.
- v2.0.4 clean setup, known-answer controls, progress mirror, student-solution gate, beginner entry point, architecture/scope, and secret checks: passed (9 groups).
- v2.0.4 fresh-task reconstruction: passed (63 checks).
- Production build: passed.
- Rendered HTML tests: 2 passed, 0 failed.
- Static lint: passed.
- Sites artifact validation: passed.
- Backup ZIP CRC, path, required-member, exclusion, and secret checks: passed.
- Final v2.0.4 private-remote commit/tree/tracking and fresh-clone verification: required immediately after the approved closeout push and included in the delivery report.

The build emitted only the existing route-classification notice. GNU `timeout` remains unavailable on Jeremy's Mac, so the verified build script used its existing direct local fallback.
