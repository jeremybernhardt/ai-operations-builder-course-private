# Release Checks — v2.0.6

Release checkpoint: `ARCH-RG1-v2.0.6`
Date: `2026-08-21`
Result: **Passed locally; approved private push verification follows this record**

## Scope verified

- Record `M0.5-L2` / `M0.5-C2` as completed with limited assistance without claiming independent mastery or a resume-level gate.
- Preserve the original AI plan, guided reviewed plan, different transfer, assistance boundary, limitations, and unresolved implementation questions.
- Record the course-wide Teach, Practice, and Demonstrate method in `DEC-M0.5-002`.
- Record task-stage evidence precision in `DEC-M0.5-003` without weakening real-file or implementation verification.
- Preserve all earlier learner evidence, private-repository authority, verified first-push baseline, credential boundary, and disposable-practice separation.
- Bound the next fresh task to only `M0.5-L3 — Reviewing an AI-Generated Diff and Verification Evidence`.
- Prohibit Expense File Readiness Checker implementation and later lessons.
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
unzip -t AI_Operations_Builder_Course_Prototype_v2.0.6_M0.5-L2.zip
```

Every repository JSON file was parsed structurally. The deterministic suite includes the secret scan. The complete closeout diff, proposed tracked-file set, outgoing history, author and committer metadata, origin URL, branch/tracking state, exclusions, ignored files, and secret patterns are inspected before approval. The final commit SHA cannot be embedded inside the same commit without changing it; it is verified against GitHub after the approved push.

## Learner-evidence boundary

`M0.5-C2` is **Completed with limited assistance**. The instructor supplied the direct concept lesson, complete adjacent worked example, artifact organization, and source-integrity explanation. Jeremy made the material guided plan decisions and independently reviewed a different accounts-payable plan. Independent mastery and every resume-level capability gate remain unearned.

## Results

- JSON structure and diff whitespace: passed.
- v2.0.6 clean setup, known-answer controls, progress mirror, student-solution gate, beginner entry point, architecture/scope, and secret checks: passed (9 groups).
- v2.0.6 fresh-task reconstruction: passed (73 checks).
- Production build: passed.
- Rendered HTML tests: 2 passed, 0 failed.
- Static lint: passed.
- Sites artifact validation: passed.
- Lesson, original/reviewed plan, transfer, assistance, teaching decisions, gate, and next-authorization consistency: passed.
- Backup ZIP creation, CRC, required-member, and exclusion checks: passed with 133 intended files.
- Final private-remote commit/tree/tracking and fresh-clone verification: required after Jeremy's approved closeout push.

The build emitted only the existing route-classification notice. GNU `timeout` remains unavailable on Jeremy's Mac, so the verified build script used its existing direct local fallback.
