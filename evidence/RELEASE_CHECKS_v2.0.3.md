# Release Checks — v2.0.3

Release checkpoint: `ARCH-RG1-v2.0.3`  
Date: `2026-08-14`  
Result: **Passed**

## Scope to verify

- Preserve the approved v2.0.0 architecture, v2.0.1 operator-builder standard, and v2.0.2 safe AI-execution clarification.
- Record `M0-L3` / `M0-C3` as completed with substantial assistance without claiming independent mastery, Module 0 completion, or a resume-level gate.
- Preserve the exact identity/privacy decision, separate approval, effective future configuration, unchanged historical metadata, local-only practice repository, and no-remote boundary.
- Record `DEC-C2-010` and enforce transfer rather than immediate repetition after instructor-supplied explanations.
- Bound the next lesson to `M0-L4 — Private GitHub Course Repository and First Verified Push`, with separate approval before every consequential external action.
- Keep every v2 resume-level capability gate `Not started`.
- Preserve the v1.2.0 prototype logic, incomplete learner SQL, fixtures, and known-answer controls.

## Verification commands

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
python3 scripts/package_bundle.py
unzip -t AI_Operations_Builder_Course_Prototype_v2.0.3.zip
```

## Learner-evidence boundary

Software verification cannot raise learner mastery. `M0-C3` is `Completed with substantial assistance`. Jeremy made the consequential identity, privacy, scope, and external-action decisions; the instructor supplied the beginner model and failure/limitation analysis. No repeated paraphrase after an instructor-supplied answer was counted as evidence. Module 0 remains incomplete, and no SQL, Python, dashboard, automation, applied-AI, or agent capability gate was earned.

## External-action boundary

No remote repository, GitHub repository, account, push, pull, fetch, clone, deployment, public artifact, API, or paid service was created or connected. The only external account change was Jeremy's learner-confirmed GitHub email-privacy settings. The only local configuration change was the separately approved global Git identity.

## Results

- JSON structure: passed.
- Clean deterministic setup: passed.
- Synthetic database controls and edge cases: passed.
- Controlled known-answer SQL and independent reference reconciliation: passed.
- Canonical M0-L3 progress and generated read-only portal mirror: passed.
- Incomplete student-solution gate: passed.
- Beginner entry point: passed.
- v2.0.3 identity/privacy, teaching-strategy, operator-builder, architecture, scope, and capability-gate checks: passed.
- Credential and secret scan: passed.
- Fresh-chat reconstruction: passed, 55 checks.
- Production build: passed.
- Rendered HTML tests: 2 passed, 0 failed.
- Static lint: passed.
- Sites artifact validation: passed.
- Bundle CRC and required-member checks: passed.

The clean bundle excluded dependencies, so `npm ci` restored the versions already locked in `package-lock.json`. The sandboxed attempt could not reach the npm registry; an approved network retry succeeded. GNU `timeout` remains unavailable on Jeremy's Mac, so the existing build fallback ran the same local vinext build directly. The build emitted only its existing route-classification notice; it did not represent a test, lint, artifact, security, or reconstruction failure.
