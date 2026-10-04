# Course Reliability Plan

This procedure keeps lesson tasks small without weakening course continuity or verification. It is maintenance guidance, not mandatory lesson context. `COURSE_STATE.json` says when a stage is due.

## Ordered rollout

| Stage | Timing | Required result | Stop or fallback condition |
|---|---|---|---|
| `REL-0` | Before changes | Preserve dirty learner work, record startup size, and confirm course-owned processes. | Stop if the current submission cannot be distinguished from generated or canonical work. |
| `REL-1` | Before the next lesson resumes | Add answer acknowledgement, bounded-process recovery, interrupted-work recovery, and Excel lock-file exclusions. | Preserve artifacts and leave progress unchanged if recovery is uncertain. |
| `REL-2` | Before the next lesson resumes | Replace full-history startup with mandatory core, current lesson, prerequisite evidence, and explicitly relevant artifacts. | Expand to the relevant module history if a critical fact conflicts or cannot be reconciled. |
| `REL-3` | Before the next lesson resumes | Pass scan-only, canary, context-size, recovery, quality, JSON, reconstruction, test, lint, artifact, and secret gates. | Do not resume teaching if a critical gate fails. Revert only the failing reliability change, not learner work. |
| `REL-4` | M0.5 progression boundary, after two successful selective-context lesson tasks, including an explicit prerequisite exception | Evaluate generator/state decoupling using representative reconstruction tests. | Defer implementation if benefits are unproven or context grows. |
| `REL-5` | Only after a context-growth trigger | Compact mandatory core without deleting authoritative history. | Require a tested maintenance change and a new approved baseline. |
| `REL-6` | Every lesson closeout | Record task health, stopped processes, context mode, fallbacks, and any interruption recovery. | Escalate repeated failures; do not create a parallel curriculum workflow. |

## Context and quality controls

- The one-time selective-startup target is no more than 17,000 source words and at least 40% below the measured legacy startup of 31,889 words.
- After `REL-3`, more than 5% growth from the approved mandatory-core baseline requires an audit. More than 10% unexplained growth blocks the next release change.
- Baselines change only through tested maintenance with the reason and result recorded here and in the checkpoint evidence.
- Normal lesson tasks use `scripts/reliability_scan.py`, which reads repository files locally and returns only paths, counts, IDs, hashes, statuses, and bounded failure codes. It never returns source excerpts.
- A canary test proves scanned text is not emitted. Scanner output may not exceed 8,192 bytes.
- Quality checks reconcile current lesson, prerequisite, assistance, mastery, scope, decisions, limitations, and next action. A failed or ambiguous check triggers targeted on-demand reading, not blind trust in a count or hash.
- A full semantic audit is necessarily direct-context work. Use it only for material routing changes, module boundaries, or unresolved conflicts, and disclose it.
- The two-minute stall threshold applies to an observable course-owned command after the learner answer is acknowledged. Progress is surfaced at least every 60 seconds and a quiet command is interrupted or retried safely. A host or task freeze cannot time or report itself; canonical state and saved artifacts provide recovery instead of a false self-monitoring guarantee.

## User impact and authority

Reliability stages run at the listed milestones rather than across every lesson. Jeremy should not need extra lesson tasks or repeated prompts. No stage authorizes a commit, push, deployment, publication, account change, destructive remote action, or paid service. Those actions still require explicit informed approval.
