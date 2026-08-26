# Course Reliability Checkpoints

## REL-0 — Baseline preserved

- Date: 2026-08-25
- Legacy broad-startup reference: 31,889 source words.
- Pre-change selective mandatory set: 15,078 source words.
- Existing current-lesson files were identified as untracked learner/work artifacts and left unchanged.
- Excel's transient `~$*.xlsx` lock file was preserved locally.
- No course server process was running.
- Learner progress, mastery, and lesson authorization were not advanced.

## REL-1 through REL-3 — Passed

- Date: 2026-08-25
- `REL-1`: answer acknowledgement, bounded-process/stall handling, interruption recovery, and Excel lock exclusions are active. The lock file remains on disk but is ignored by Git and excluded from packages.
- `REL-2`: mandatory startup is authoritative core plus current lesson, prerequisite evidence, and explicitly relevant submission artifacts. Older history is indexed for targeted on-demand fallback.
- `REL-3`: mandatory startup measured 16,145 source words before the final operational-stall wording, 49.37% below the 31,889-word legacy reference and below the 17,000-word ceiling. The approved baseline in `COURSE_STATE.json` records the final exact measurement.
- Scanner result: pass across 145 files, with 13 JSON files structurally valid and the transient Excel lock recorded only as an ignored observation. Output remained below 8,192 bytes and emitted no source excerpts.
- Reliability tests: 7 passed, covering canary non-emission, bounded output, content hashing without disclosure, Excel lock exclusion, critical quality facts, non-mutating interrupted-submission recovery, and deliberate conflict detection.
- Reconstruction: 83 checks passed, including the operational-stall guard. A clean recovery snapshot also passed with the preserved L3 work present and the transient Excel lock excluded.
- Full release checks: `npm test`, production build, rendered tests, lint, artifact validation, and credential/secret scan passed.
- A material routing-change semantic audit was performed in direct context. No additional completed-lesson history was needed beyond the mandatory prerequisite; the repository-wide check remained scan-only.
- No Course Portal process was started, no backup bundle was created, and no external action occurred.
- Learner progress, mastery, capability gates, and M0.5-L3 authorization were not advanced. The existing L3 submission remains unverified pending lesson recovery.

## Future checkpoints

- `REL-4` is deferred until the M0.5 boundary and two successful selective-context lesson tasks.
- `REL-5` runs only after a recorded context-growth trigger.
- `REL-6` is a lightweight closeout health record, not another learner step.
