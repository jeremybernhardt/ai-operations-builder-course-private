# Learner Checkpoint Evidence — M0.5-C2

Checkpoint ID: `M0.5-C2`
Lesson: `M0.5-L2 — Reviewing an AI Builder Plan, Assumptions, and Scope`
Date: `2026-08-21`
Decision: **Completed with limited assistance**
Independent mastery claimed: **No**

## Objective and learner artifact

Jeremy reviewed an AI-drafted implementation plan before code was authorized. The guided artifact is `student/M0.5-L2_EXPENSE_FILE_READINESS_REVIEWED_PLAN.md`; the unchanged proposal is preserved at `student/M0.5-L2_EXPENSE_FILE_READINESS_AI_PLAN.md`.

No expense checker, dataset, test suite, database, dashboard, source-file transformation, account, deployment, publication, or external action was created.

## Course-delivery correction

The initial delivery turned plan review into a chain of questions and file comparisons without enough direct instruction or curriculum context. Jeremy identified that the questions prompted thought but did not feel connected to a coherent lesson.

The instructor agreed and restarted the lesson with a direct explanation of where plan review fits between a build brief and implementation, a complete worked example, guided practice, and a different transfer demonstration. Jeremy approved using this visible **Teach → Practice → Demonstrate** method for the rest of the course, subject to later adjustment. `DEC-M0.5-002` records the course-wide correction.

## Guided expense-plan decisions

Jeremy independently decided that:

- every row sharing a duplicate transaction ID must be flagged because file order does not prove which record is authoritative;
- a human reviewer, not the checker, determines whether one duplicate should later be retained;
- the cleaned valid-row export must be rejected because excluded rows could be material and the export would bypass the rule that any blocking exception makes the file not ready;
- SQLite history and future dashboarding are not needed for the current one-file result and should be deferred;
- blocked rows must not influence the high-amount warning median because erroneous values could skew the threshold; and
- the warning can use valid positive rows from the run, while a later corrected-file rerun remains possible.

Jeremy designed a duplicate known-answer check using four otherwise valid rows with one repeated transaction ID. He required `Ready: No`, both repeated-ID rows to be flagged for human review, direct source inspection, and an unchanged source boundary.

## Direct instruction and assistance

The instructor supplied:

- the explicit curriculum connection from build brief to reviewed plan to later implementation and verification;
- the four-control framework of requirement traceability, assumption ownership, scope control, and approval evidence;
- the distinction between plan approval and implementation acceptance;
- a complete adjacent worked example;
- organization of Jeremy's decisions into the guided review artifact; and
- the SHA-256 before/after content-comparison method for future real-file verification.

Jeremy did not need to recall commands or testing-tool names. Maximum help was direct instruction plus a full worked example; his material guided decisions were his own, and the later transfer required limited help only on the real-file integrity concept.

## Genuinely different transfer

Jeremy reviewed a synthetic accounts-payable plan comparing an approved-invoice file with a proposed-payment file. Without answer-specific help, he rejected the plan because all proposed work beyond exact invoice-ID matching conflicted with the approved outcome or boundary.

He identified:

- an unapproved assumption that vendor name and amount could replace a missing invoice ID;
- an incorrect cleaned-payment output that would delete exception rows despite the unchanged-source boundary;
- unauthorized vendor contact;
- an unnecessary database and future dashboard; and
- acceptance based only on automated tests and a reasonable-looking report.

He required missing or nonmatching records to be flagged for human review and proposed manually checking a small matching-versus-nonmatching case.

## Evidence-precision correction

After Jeremy had demonstrated the intended plan-review judgment, the instructor asked him to invent exact invoice identifiers and amounts for the theoretical transfer. Jeremy correctly objected that arbitrary numbers added no evidence in that setting and distinguished the exercise from work with a real file. The instructor accepted the correction and recorded `DEC-M0.5-003`: conceptual evidence must demonstrate the judgment and verification design, while exact known answers and file-integrity checks are mandatory for real calculations, files, and implementations.

The objection is positive evidence of scope and assessment judgment, not a learner deficiency. Jeremy was not asked to repeat the supplied SHA-256 explanation.

## Verification and limitations

- The original AI plan and reviewed plan are preserved separately, so the proposed and approved states remain inspectable.
- Every retained plan step maps to a build-brief requirement or verification condition.
- Jeremy identified business-rule, data-completeness, scope, permission, and circular-evidence risks in two scenarios.
- No software exists to test; this checkpoint verifies plan-review judgment rather than implementation correctness.
- The plan's column-normalization and nonnumeric-total details still require explicit treatment before any future implementation.
- A future real-file lesson must use exact fixtures, independent reconciliation, and content-integrity evidence; conceptual review does not substitute for those checks.

## Assistance and mastery boundary

- Guided instruction: direct concept lesson and complete worked example after a learner-requested delivery correction.
- Guided project: Jeremy made the material duplicate, cleaned-output, optional-scope, and warning-population decisions; AI organized the artifact.
- Transfer: material review completed independently; limited instructor help explained source-file integrity verification.
- Checkpoint status: **Completed with limited assistance**.
- Independent mastery: not claimed.

## Gate and advancement decision

No resume-level capability gate was earned. `M0.5-C2` provides foundational evidence for `SK-AI-BUILDER-PLAN-REVIEW-001` only.

The next fresh task may prepare and teach only `M0.5-L3 — Reviewing an AI-Generated Diff and Verification Evidence`. It must use the course-wide Teach, Practice, and Demonstrate method and remain bounded to a safe work-practical scenario. It may not implement the Expense File Readiness Checker, begin `M0.5-L4`, begin the finance flagship or `M1`, or perform a consequential external action.
