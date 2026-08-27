# Learner Checkpoint Evidence — M0.5-C4

Checkpoint ID: `M0.5-C4`

Lesson: `M0.5-L4 — Debugging from Evidence and Directing a Bounded Modification`

Date: `2026-08-27`

Decision: **Completed with limited assistance**

Independent mastery claimed: **No**

## Objective and artifacts

Jeremy used deterministic failures to isolate two bounded defects, directed narrow corrections, inspected the relevant rules in plain language, selected regression evidence, and made a readiness decision. Durable artifacts are:

- `student/M0.5-L4_DEBUGGING_AND_BOUNDED_MODIFICATION_RECORD.md`;
- `student/m0_5_l4/payment_release.py`;
- `student/m0_5_l4/test_payment_release.py`;
- `student/m0_5_l4/review_routing.py`; and
- `student/m0_5_l4/test_review_routing.py`.

The files contain synthetic local practice only. No Expense File Readiness Checker, finance flagship, external service, account, publication, deployment, or remote action was created.

## Guided practice evidence

The initial exact-seven-day check deterministically failed: expected `RELEASE_NOW`, actual `SCHEDULE_LATER`. Jeremy identified the symptom as an incorrectly classified invoice and the underlying issue as an exclusive boundary conflicting with an inclusive “within seven days” rule.

Jeremy authorized only an inclusive seven-day change and stated that the other rules and tests must not change. AI changed `< 7` to `<= 7`. Jeremy correctly explained both the changed comparison and why hold and approval remained unaffected: those rules are checked first and return before timing is evaluated.

The corrected known-answer case passed. Six days, eight days, hold, and missing approval also passed, for five successful checks total.

## Genuinely different transfer evidence

The transfer failure involved precedence rather than a numeric boundary. A changed-bank, `$12,000` invoice incorrectly returned `MANAGER_REVIEW` instead of `MANUAL_REVIEW`, while four other checks passed.

Before seeing the implementation, Jeremy diagnosed that the manager-review criterion was probably checked before the manual-review criterion. He authorized changing only the order, selected the passing `$500` changed-bank case as a regression check, and did not request unrelated changes.

Targeted inspection confirmed the diagnosis. AI moved the changed-bank rule ahead of the amount rule while preserving missing-approval precedence. The failed case, Jeremy's selected regression, and all five transfer checks passed afterward.

Jeremy marked the helper **ready** and identified a material limitation: it trusts the changed-bank indicator and cannot detect bank details that are unchanged but incorrect.

## Assistance and mastery boundary

- Jeremy owned both defect diagnoses, corrected business behavior, bounded-change authorization, relevant implementation explanations, regression selection, readiness decision, and limitation.
- AI supplied the synthetic fixtures, test presentation, question structure, implementation edits, command execution, and evidence organization.
- The guided work included direct prompts and explanation; the different transfer was diagnosed without answer-specific help.
- Checkpoint status: **Completed with limited assistance**.
- Independent mastery: not claimed.
- Resume-level capability: none earned.

## Reliability and recovery boundary

The first M0.5-L4 task suffered a response-transport failure after Jeremy submitted the correct guided diagnosis. The answer and partial artifacts were recovered without asking him to repeat his work, and canonical progress was not advanced until the checkpoint passed. The recovery controls worked, but repository changes cannot prevent an upstream Codex response-stream disconnection.

## Gate and advancement decision

`M0.5-C4` provides foundational evidence for `SK-AI-BUILDER-DEBUG-MODIFY-001`. Every resume-level capability gate remains `Not started`.

The next fresh task may prepare and teach only `M0.5-L5 — Explaining Human and AI Contributions Without Inflation`. It may use completed Module 0.5 evidence to create an accurate contribution statement, but it may not implement the Expense File Readiness Checker, begin the finance flagship or `M1`, or perform a consequential external action without explicit informed approval.
