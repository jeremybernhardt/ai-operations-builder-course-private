# Release Checks — v2.0.1

Release checkpoint: `ARCH-RG1-v2.0.1`  
Date: `2026-08-12`  
Result: **Passed**

## Scope verified

- The approved v2.0.0 course architecture remains intact.
- `DEC-C2-008` and the course-wide AI-assisted operator-builder proficiency standard are present and consistent across the contract, curriculum, lesson template, project boundary, evidence ledger, state, progress, and continuity files.
- `M0-L1` and learner checkpoint `M0-C1` are recorded with limited assistance and no independent-mastery or resume-gate inflation.
- The next authorization is bounded to local-only `M0-L2`; no remote repository or later lesson was created.
- Every v2 resume-level capability gate remains `Not started`.
- The preserved v1.2.0 prototype logic, incomplete learner SQL, fixtures, and known-answer controls remain intact.

## Commands run

```text
python3 -m json.tool COURSE_STATE.json
python3 -m json.tool PROGRESS.json
python3 scripts/setup.py
python3 scripts/reconstruction_check.py
python3 scripts/verify.py
npm ci
npm test
npm run lint
npm run validate:artifact
```

## Results

- JSON structure: passed.
- Clean deterministic setup: passed.
- Synthetic database controls and edge cases: passed.
- Controlled known-answer SQL and independent reference reconciliation: passed.
- Canonical progress and generated read-only portal mirror: passed.
- Incomplete student-solution gate: passed.
- Beginner entry point: passed.
- v2.0.1 operator-builder, M0 evidence, architecture, and capability-gate checks: passed.
- Credential and secret scan: passed.
- Fresh-chat reconstruction: passed, 38 checks.
- Production build: passed.
- Rendered HTML tests: 2 passed, 0 failed.
- Static lint: passed.
- Sites artifact validation: passed.

The build emitted only environment/proxy and route-classification warnings; none represented a test, lint, artifact, security, or reconstruction failure.

## Learner-evidence boundary

Software verification does not raise learner mastery. `M0-C1` is `Completed with limited assistance`; the guided cycle used a full walkthrough, and the comparable challenge required limited help. Module 0 is incomplete. No SQL, Python, dashboard, automation, applied-AI, or agent capability gate was earned.

## External-action boundary

No remote repository, GitHub repository, account, deployment, public artifact, API, or paid service was created or connected.
