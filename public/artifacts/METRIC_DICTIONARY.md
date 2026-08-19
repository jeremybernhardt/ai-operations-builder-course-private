# Metric Dictionary

Dictionary version: `0.2.0-checkpoint`  
Preserved prototype checkpoint: `P0-CLOSEOUT` (current course checkpoint is recorded in `COURSE_STATE.json`)

## METRIC-FPA-001 — First-pass acceptance rate

Status: **Checkpoint definition accepted with substantial assistance; implementation definition not yet frozen**

Business purpose: provide an early quality signal that helps an operations lead decide whether to investigate work mix, guideline clarity, reviewer behavior, or contributor support.

Jeremy completed the bounded `P0-C1` definition checkpoint. The accepted checkpoint wording is:

> First-pass acceptance rate is the percentage of unique eligible work items accepted on their first review without revisions or rework. The numerator is the number of eligible work items accepted on their first review with no rework required. The denominator is the number of unique eligible work items with a known first-review outcome. Duplicate logical reviews are counted only once. Work items with a missing first-review outcome are excluded until corrected and reported separately as a data-quality issue. Acceptance after revision or a later review does not count as first-pass acceptance. The metric helps managers determine whether instructions and training are sufficient and whether review standards are clear and consistently calibrated.

Formula in words: unique eligible work items accepted on their first review without rework, divided by unique eligible work items with a known first-review outcome.

Before any later SQL implementation, the implementation definition must still explicitly settle:

- unit of analysis;
- numerator event and accepted-status mapping;
- denominator eligibility;
- first-pass event selection when multiple review records exist;
- duplicate-review treatment;
- missing-outcome treatment;
- reworked-submission treatment;
- time-window basis;
- filters and exclusions;
- output precision; and
- limitations and non-comparable cases.

Definition freeze record: The `P0-C1` learner definition is preserved in `evidence/LEARNER_CHECKPOINT_P0-C1.md`. Full implementation freeze remains pending because reporting-window basis, filters, precision, and a limitation review were not completed in the bounded prototype-format evaluation.

Implementation status: Student SQL not started and remains locked. A private controlled reference exists only to verify that the learning environment and test harness function; it is not evidence of learner SQL mastery.

Change rule: once frozen, a material definition change requires a superseding entry in `DECISION_LOG.md`, an updated dictionary version, updated tests, and an explicit statement about whether historical values are restated.
