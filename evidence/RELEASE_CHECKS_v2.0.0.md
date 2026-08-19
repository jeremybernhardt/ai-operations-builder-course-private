# Course Architecture v2.0.0 Release Evidence

Release gate: `ARCH-RG1-v2.0.0`  
Status: Passed  
Verified: `2026-08-08`

## Scope verified

This release changes only the bounded architecture, canonical state, decisions, evidence gates, continuity files, generated artifact copies, and minimal Course Portal summary labels. It preserves the completed v1.2.0 KPI prototype and does not implement Module 0, future lessons, the finance flagship, optional `OH1`, a remote repository, external service, public deployment, or standalone product.

## Canonical architecture checks

- `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, state, progress, lesson template, project specification, decision log, handoff, and next-chat instructions identify v2.0.0 consistently.
- Finance is the primary application context while AI/data/dashboard/automation/agent building remains the subject.
- Finance-only and software-engineering-only lesson drift is explicitly prohibited.
- The required finance planning/reporting/decision-support flagship replaces the prior human-data flagship.
- The completed prototype is preserved as a pre-course artifact and optional transfer case.
- Human-Data and AI Operations is optional specialization `OH1`.
- An early learner-built work-dashboard slice appears in `M4`; the full work dashboard and evidence gate appear in `M7`.
- The Course Portal is explicitly excluded from work-dashboard evidence.
- SQL and Python/pandas have recurring basic and full gates.
- Workflow automation, applied AI, AI tool development, work-dashboard, and integrated AI/workflow gates are present.
- The final agent uses multiple controlled tools and approval-gated sandbox actions rather than being either strictly read-only or autonomously consequential.
- Obsolete job-specific priority interruption requirements are removed from active state and next-chat execution.
- Every new capability gate remains Not started.

## Deterministic and build checks

Command: `npm test`

Passed:

- clean isolated Python setup;
- exact CSV-to-SQLite reconciliation and unique raw identifiers;
- duplicate, missing-outcome, rework, and denominator fixtures;
- controlled instructor-only SQL and independent Python reconciliation;
- canonical progress mirroring and honest learner evidence;
- incomplete learner SQL gate;
- beginner start-path checks;
- v2.0.0 architecture and capability-gate checks;
- credential/secret scan;
- all 26 fresh-chat reconstruction checks;
- production Vinext/Vite build and Sites artifact validation; and
- two rendered-output test suites covering Course Portal, KPI Lab, v2.0.0 labels, continuity, and absence of private expected results.

Commands: `npm run lint` and `npm run validate:artifact`

Result: passed with no lint errors; the built ESM worker and hosting manifest validated.

## Portal QA boundary

The supported agent-preview service was unavailable in this execution environment, so no new browser screenshot or interaction claim is made. This is an infrastructure limitation rather than a source failure. v1.2.0's prior private visual QA remains preserved; v2.0.0 changes only text, roadmap entries, one artifact link, and continuity labels. Production rendering, responsive source review, artifact-link generation, and rendered client/server assertions passed.

No public deployment was created.

## Durable bundle reconstruction

The clean v2.0.0 ZIP was integrity-tested, extracted into a fresh directory, and checked for the required top-level folder, canonical files, executable start script, absence of unsafe paths, and absence of macOS metadata. From the extracted copy, locked dependency installation, `npm test`, lint, artifact validation, and the 26-check reconstruction test passed.

## Interpretation

This release verifies the approved v2.0.0 blueprint and transition. It does not advance learner mastery or authorize more than the first Module 0 lesson in a fresh chat.
