# Learner Checkpoint Evidence — M0.5-C1

Checkpoint ID: `M0.5-C1`
Lesson: `M0.5-L1 — Defining Outcomes, Constraints, and Done Criteria`
Date: `2026-08-20`
Decision: **Completed with limited assistance**
Independent mastery claimed: **No**

## Objective and learner artifact

Jeremy practiced defining a work outcome, material constraints and non-goals, observable acceptance criteria, an independent verification plan, explicit done criteria, and a plausible failure before allowing AI to implement a tool.

The guided artifact is `student/M0.5-L1_EXPENSE_FILE_READINESS_BUILD_BRIEF.md`, a build brief for a synthetic finance-operations Expense File Readiness Checker. No checker code, finance flagship component, later lesson, account, deployment, or external action was created.

## Course-design correction during the lesson

The initially prepared exercise asked Jeremy to specify a checker for the course's own continuity state. Jeremy stated that he should not need to supervise course-building mechanics and that lessons should be practical for work. That objection was correct: the scenario was internally focused, unclear, and misaligned with the course's promised workplace capability.

The instructor replaced it with the bounded synthetic expense-file scenario and recorded `DEC-M0.5-001`. Course-state management remains an instructor/agent responsibility. The correction did not broaden authorization into the finance flagship or `M1`.

## Jeremy's guided decisions and reasoning

Jeremy:

- distinguished the user outcome from a proposed Python implementation after the first scenario was clarified;
- identified that a polished `Ready: Yes` result could be materially wrong if duplicate transactions or other field-level exceptions were concealed;
- identified duplicate IDs, zero-dollar rows, unusually high expenses, and column-dependent validation issues as conditions requiring explicit treatment;
- chose to make an unusually high expense a nonblocking warning until the business supplies an approved blocking limit;
- approved a temporary warning for valid expenses greater than three times the valid-file median; and
- explained that the median is resistant to distortion from the magnitude of unusually large expenses.

The instructor refined the last explanation: a median is much less sensitive to extreme magnitudes than an average, but it is not literally unaffected by changes in sample composition. Small samples and mixed expense populations remain limitations.

## Guided artifact and verification design

The final brief specifies:

- the finance operations manager and reporting-readiness decision;
- required synthetic input fields and blocking validation rules;
- a separate nonblocking high-amount warning;
- reconciled row counts and totals;
- row-level reasons rather than silent data repair;
- explicit scope exclusions;
- clean, duplicate, combined-error, missing-column, and high-amount test fixtures;
- independent count and total reconciliation; and
- a done threshold requiring all acceptance evidence and unchanged source data.

AI organized the complete artifact after Jeremy made or approved the material anomaly and failure-handling decisions. The working brief itself was not treated as independent mastery evidence.

## Genuinely new transfer application

Jeremy then applied the concepts to a synthetic September actual-versus-approved-budget variance exception report.

On his first attempt, he correctly:

- required material variances to be flagged rather than visually ranking every small variance;
- stated that immaterial rows should not be flagged; and
- identified an actual-versus-actual comparison as a plausible hidden error in a convincing-looking report.

His initial outcome emphasized an easy-to-read department summary rather than the finance director's investigation decision, and his proposed test said only to use a large variance without exact inputs or expected outputs. The instructor gave one targeted correction: preserve the department-and-account decision grain and make the known-answer test numerically exact.

Jeremy then stated that the director must identify account-level variances above the investigation threshold and supplied an exact test row: `$100,000` budget versus `$150,000` actual, producing a `$50,000` and `50%` variance that must be flagged. This satisfies both the dollar and percentage thresholds. The instructor made only a non-substantive wording correction to preserve the department-and-account context.

## Assistance record

- Guided brief: substantial instructor/AI structure. The instructor supplied the corrected workplace scenario, stakeholder validation rules, distinction between blocking failures and nonblocking anomalies, median recommendation, and final brief organization.
- Transfer challenge: limited targeted help. Jeremy independently identified the materiality constraint and hidden actual-versus-actual failure; one nudge was needed to recenter the outcome and make the test exact.
- Maximum help for the guided exercise was effectively a full structured walkthrough, but the genuinely new transfer was completed with limited assistance. Consistent with the course's prior comparable-challenge treatment, the checkpoint status is **Completed with limited assistance**, not demonstrated independently.

## Verification and limitation evidence

- The guided brief contains observable pass/fail cases and an independent reconciliation plan rather than relying on AI's claim that the checker works.
- Jeremy's exact transfer row reconciles manually: `$150,000 - $100,000 = $50,000`; `$50,000 / $100,000 = 50%`; both thresholds are exceeded.
- Jeremy independently identified a hidden lineage/comparison failure: comparing actuals with actuals could create plausible zero variances.
- The temporary median warning can behave poorly with small or mixed samples and cannot become a blocking rule without an authoritative approved limit.
- A correct-looking summary can still conceal wrong source versions, periods, grain, or comparison data; later implementation lessons must inspect those boundaries directly.

## Gate and advancement decision

No resume-level capability gate was earned. `M0.5-C1` provides foundational evidence for `SK-AI-BUILDER-BRIEF-001` only. The lesson is **Completed with limited assistance**; independent mastery is not claimed.

The next fresh task may prepare and teach only `M0.5-L2 — Reviewing an AI Builder Plan, Assumptions, and Scope`. It must remain work-practical and bounded; it may use the approved expense-file brief as context but may not begin implementation, the finance flagship, `M1`, or a later `M0.5` lesson.
