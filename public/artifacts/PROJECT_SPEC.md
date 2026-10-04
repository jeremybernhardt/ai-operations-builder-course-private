# Current Project Specification

Project ID: `PROJ-HDOFCC-001`  
Prototype slice: `P0-L1`  
Status: Preserved completed prototype inside the local `v2.0.9` delivery revision and approved `v2.0.0` course architecture

## Relationship to the required course

This specification governs only the preserved `P0-L1` teaching-format prototype. It is not the required flagship and does not count as work-dashboard, SQL, Python, automation, or agent proficiency. Human-data operations is now an optional later transfer specialization. The required flagship is the synthetic AI-Enabled Finance Planning, Reporting, and Decision-Support System defined in `COURSE_CONTRACT.md` and `CURRICULUM_MAP.md`. Release v2.0.1 added the course-wide AI-assisted operator-builder proficiency standard; v2.0.2 recorded the verified M0-L2 checkpoint and safe AI-execution default; v2.0.3 recorded the M0-L3 identity/privacy checkpoint and transfer-not-repetition correction; v2.0.4 recorded private-repository authority and M0-L4; v2.0.5 recorded M0.5-L1; v2.0.6 recorded M0.5-L2 and teaching-method corrections; v2.0.7 recorded the recovered and verified M0.5-L3 change-review checkpoint; and v2.0.8 records the verified M0.5-L4 debugging and bounded-modification checkpoint. These changes do not alter this prototype's decisions, implementation, or evidence.

## Scenario

The v2.0.9 delivery revision moves the first small finance app to M1 and defers standalone contribution-writing. It changes no P0 data, rules, learner evidence, or implementation. The first-app scope is in `lesson/M1-L1_FIRST_WORKING_FINANCE_APP.md`, not this preserved prototype specification.

Finance experts submit synthetic financial-reasoning tasks for an AI-training project. Reviewers record an initial decision of accepted, revise, or rejected. Some tasks are reworked, some records are incomplete, and one logical review is duplicated. An operations lead needs a defensible first-pass quality signal before deciding whether to investigate a task type, guideline version, or data-quality problem.

All people, companies, task records, and workflows are synthetic and generic.

## Primary user and decisions

The primary user is a project operations lead. The prototype supports three decisions:

1. whether the proposed first-pass metric is defined precisely enough to implement;
2. whether data-quality exceptions must be resolved before trusting the metric; and
3. where an operator should investigate after a verified result is available.

## System boundary

Included now:

- one synthetic CSV of review events;
- a local SQLite database generated from the CSV;
- a staged lesson and student-editable SQL file;
- a fixed deterministic setup and verification harness;
- a local/private Course Portal and KPI Lab application;
- generated read-only progress and data-quality snapshots; and
- private instructor reference fixtures for build verification.
- a final lesson-closeout stage that explains evidence, the next lesson, and new-chat continuity.

Excluded now:

- real company or proprietary data;
- authentication or multiple users;
- API ingestion, external databases, automation, runtime AI, or agents;
- generic browser SQL execution;
- public deployment;
- future module implementations; and
- a production operating system.
- backend synchronization of browser activity or notes.

## Functional requirements

- `REQ-P0-001`: Display Course Portal and KPI Lab as clearly labeled areas in one application.
- `REQ-P0-002`: Show only checkpoint `P0-C1` as active; later lesson stages remain locked.
- `REQ-P0-003`: Present the raw dataset and field definitions without stating the final metric definition or expected answer.
- `REQ-P0-004`: Surface duplicate-review, missing-outcome, rework, and denominator-policy issues.
- `REQ-P0-005`: Provide a student SQL scaffold with no completed metric query.
- `REQ-P0-006`: Generate SQLite deterministically from the CSV.
- `REQ-P0-007`: Verify a controlled reference query against an independent known-answer check.
- `REQ-P0-008`: Mirror canonical progress in a generated, read-only, explicitly non-authoritative portal snapshot.
- `REQ-P0-009`: Provide exact setup, start, test, and recovery commands.
- `REQ-P0-010`: Preserve the canonical continuity and handoff artifacts.
- `REQ-P0-011`: Begin the learner experience with a plain-language scenario, purpose, terminology, objectives, prior-knowledge boundary, and lesson map.
- `REQ-P0-012`: Use progressive disclosure so explanations precede the related data and decision.
- `REQ-P0-013`: Let the learner isolate duplicate, missing-outcome, and rework examples and explain why each condition affects the metric.
- `REQ-P0-014`: Preserve review choices in browser-local storage only, label them non-authoritative, and provide a reset control.
- `REQ-P0-015`: Avoid duplicate reporting between the site and chat; capture a meaningful response once.
- `REQ-P0-016`: Present Course Progress, current Learning Objectives, and stable Course Artifacts as a focused dashboard; keep unrelated glossary content out of the main portal.
- `REQ-P0-017`: Provide `START_HERE.html` as the obvious learner entry point and a single explained start command.
- `REQ-P0-018`: Separate required lesson time, optional exploration, and one-time setup time.
- `REQ-P0-019`: End every lesson with an explanation of completion, assistance/mastery boundary, unfinished work, and the next lesson before presenting continuity files.
- `REQ-P0-020`: Use one lesson per chat and provide an exact three-item new-chat packet until a verified private repository replaces repeated ZIP attachments.
- `REQ-P0-021`: Explain the distinct roles of the factual session handoff and exact next-chat instructions; do not describe them only as recovery tools.
- `REQ-P0-022`: Do not add backend synchronization for browser-local activity in the bounded prototype.

## Non-functional requirements

- Mac-compatible Node and Python tooling.
- No Python third-party packages.
- Reproducible Node dependencies through `package-lock.json`.
- No credentials or external services.
- Deterministic checks with concise failure messages.
- Responsive and keyboard-usable local application.
- Useful without a network connection after locked dependencies are installed.
- Browser-local lesson drafts never become authoritative learner progress.

## Acceptance criteria

The preserved prototype acceptance is governed by release evidence `P0-RG1-v1.2.0`. Build verification does not advance learner mastery. Jeremy approved the v1.1.0 teaching design on 2026-07-18 and the v1.2.0 transition changes. On 2026-08-08 he approved the v2.0.0 course retarget while preserving this prototype; on 2026-08-12 he clarified the AI-assisted operator-builder proficiency standard. Neither decision raises the prototype's learner evidence. The metric checkpoint remains completed with substantial assistance; no independent mastery is inferred from approval or working software.
