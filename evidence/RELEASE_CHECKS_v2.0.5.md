# Release Checks — v2.0.5

Release checkpoint: `ARCH-RG1-v2.0.5`
Date: `2026-08-20`
Result: **Passed locally; approved private push verification follows this record**

## Scope verified

- Record `M0.5-L1` / `M0.5-C1` as completed with limited assistance without claiming independent mastery or a resume-level gate.
- Preserve all earlier learner evidence and keep every v2 capability gate `Not started`.
- Preserve the approved private-repository authority, verified first-push baseline, credential boundary, and disposable-practice separation.
- Record Jeremy's correction from an internally focused lesson exercise to a bounded work-practical finance-operations scenario in `DEC-M0.5-001`.
- Preserve the guided Expense File Readiness Checker brief with exact learner/AI assistance boundaries.
- Bound the next fresh task to only `M0.5-L2 — Reviewing an AI Builder Plan, Assumptions, and Scope` and prohibit implementation.
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
git diff --check
python3 scripts/package_bundle.py
unzip -t AI_Operations_Builder_Course_Prototype_v2.0.5_M0.5-L1.zip
```

The complete closeout diff, tracked-file set, outgoing history, author and committer metadata, origin URL, branch/tracking state, exclusions, ignored files, and secret patterns are inspected before approval. The final commit SHA cannot be embedded inside the same commit without changing it; it is verified against GitHub after the approved push and reported in the lesson delivery record.

## Learner-evidence boundary

`M0.5-C1` is **Completed with limited assistance**. The guided brief used a full instructor/AI structure. Jeremy made or approved material warning and failure-handling decisions and then completed a genuinely different variance-report transfer after one targeted revision. Independent mastery and every resume-level capability gate remain unearned.

## Results

- JSON structure and diff whitespace: passed.
- v2.0.5 clean setup, known-answer controls, progress mirror, student-solution gate, beginner entry point, architecture/scope, and secret checks: passed (9 groups).
- v2.0.5 fresh-task reconstruction: passed (67 checks).
- Production build: passed.
- Rendered HTML tests: 2 passed, 0 failed.
- Static lint: passed.
- Sites artifact validation: passed.
- Work-practical lesson, learner artifact, evidence, assistance, gate, and next-authorization consistency: passed.
- Backup ZIP creation, CRC, required-member, and exclusion checks: passed with 127 intended files.
- Final private-remote commit/tree/tracking and fresh-clone verification: required after Jeremy's approved closeout push.

The build emitted only the existing route-classification notice. GNU `timeout` remains unavailable on Jeremy's Mac, so the verified build script used its existing direct local fallback.
