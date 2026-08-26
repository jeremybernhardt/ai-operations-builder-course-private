# Learner Checkpoint Evidence — M0.5-C3

Checkpoint ID: `M0.5-C3`

Lesson: `M0.5-L3 — Reviewing an AI-Generated Diff and Verification Evidence`

Date: `2026-08-26`

Decision: **Completed with limited assistance**

Independent mastery claimed: **No**

## Objective and artifacts

Jeremy reviewed a static AI-proposed budget-variance change, then completed a genuinely different implementation-acceptance transfer using a synthetic cash-disbursement workbook. The durable artifacts are:

- `student/M0.5-L3_ANNOTATED_DIFF_REVIEW.md`;
- `student/M0.5-L3_CASH_SCHEDULE_TRANSFER_PACKET.md`; and
- `student/M0.5-L3_CASH_DISBURSEMENT_ACCEPTANCE_FIXTURE.xlsx.inspect.ndjson`.

The workbook was not reopened during recovery. The submitted Excel answer was recovered verbatim from prior Codex task history and evaluated against the tracked text inspection record committed with the fixture.

## Guided budget-variance review

Jeremy identified that the builder's plausible `28.6%` result used actual rather than budget as the denominator. He supplied an exact `$250,000` budget and `$275,000` actual boundary case with `$25,000`, `10%`, and `investigate = true`, decided the proposed change needed revision, and recognized that the builder's evidence omitted material boundary and completeness cases.

The instructor corrected Jeremy's initial overclassification by distinguishing two aligned behaviors from four conflicting behaviors. The instructor also explained why checking only the final flag would not isolate the denominator and threshold-combination defects, and taught targeted inspection using the small rules controlling denominator, threshold operator, zero-budget behavior, and row preservation.

## Genuinely different cash-disbursement transfer

Before a task disconnect, Jeremy submitted:

- decision: **needs revision**;
- passing controls: row count and approved amount total reconcile;
- material defect: the third invoice has a blank approved scheduled date, but the builder supplied a date instead of sending the row to manual review;
- consequence: the inferred date incorrectly increases September cash;
- narrow inspection request: expose and explain the rule that chooses a scheduled date; and
- evidence limitation: amount reconciliation does not prove dates are correct.

The saved inspection record confirms the source and output each contain four rows totaling `$31,850`. It also confirms that `INV-203` has no approved scheduled date, while the builder assigns `2026-09-30`, sets September as its month, and leaves `manual_review` false.

To satisfy exact real-file evidence without asking Jeremy to redo the exercise, the instructor supplied the deterministic refinement: `INV-203` should remain unscheduled with manual review true; September should be `$19,950`, October `$3,100`, and the manual-review count `1`. Jeremy's answer was substantively correct before that refinement.

## Explanation and limitation evidence

Jeremy's transfer demonstrates why output evidence and targeted inspection complement each other: row and amount controls can pass while a date-defaulting rule remains wrong, so the operator must inspect the narrow date-selection behavior and reconcile date-sensitive totals.

Jeremy identified the evidence limitation that matching amounts do not prove dates are correct. A further recovery limitation remains: the answer was evaluated against a durable text inspection snapshot rather than a fresh parse of the binary workbook, in accordance with Jeremy's explicit instruction after repeated stalls.

## Assistance and mastery boundary

- Practice: guided correction and explanation after learner-owned material risk and boundary reasoning.
- Transfer: learner-owned decision, defect diagnosis, consequence, targeted rule, and limitation.
- Limited help: prior clarification of “narrow implementation rule” and instructor-supplied exact expected totals during recovery.
- Checkpoint status: **Completed with limited assistance**.
- Independent mastery: not claimed.
- Resume-level capability: none earned.

## Gate and advancement decision

`M0.5-C3` provides foundational evidence for `SK-AI-BUILDER-DIFF-REVIEW-001`. Every resume-level capability gate remains `Not started`.

The next fresh task may prepare and teach only `M0.5-L4 — Debugging from Evidence and Directing a Bounded Modification`. It may use safe local practice code, but it may not implement the Expense File Readiness Checker, begin the finance flagship or `M1`, or perform a consequential external action without explicit informed approval.
