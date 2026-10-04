# Decision Log

Append-only. Later decisions must identify any entry they supersede.

## DEC-P0-001 — Use SQLite for the prototype

- Date: 2026-07-17
- Status: Current
- Decision: Use SQLite, generated locally from the synthetic CSV.
- Rationale: SQLite is included with Python, requires no service or account, works on a Mac, and is sufficient for the SQL learning objective.
- Alternatives considered: DuckDB (capable but adds a dependency); hosted database (premature and externally stateful).
- Affected artifacts: `PROJECT_SPEC.md`, `README.md`, `scripts/setup.py`, `database/prototype.sqlite`.

## DEC-P0-002 — Keep the application local/private and read-only for progress

- Date: 2026-07-17
- Status: Current
- Decision: Build one local application with Course Portal and KPI Lab views. Do not deploy publicly or add authentication. Generate its progress display from canonical progress and label it non-authoritative.
- Rationale: This tests the teaching and continuity experience without creating a competing state store or expanding scope.
- Alternatives considered: public deployment; two-way portal progress editing; full portal implementation.
- Affected artifacts: application source, `PROGRESS.json`, generated snapshots, `README.md`.

## DEC-P0-003 — Keep the learner query incomplete and the known answer instructor-only

- Date: 2026-07-17
- Status: Current
- Decision: The student SQL file contains prompts and a TODO but no completed metric query. Controlled reference logic and expected results are isolated under `instructor_only/` and are not linked in student-facing materials.
- Rationale: Release verification must prove the harness works without revealing the solution before a genuine learner attempt.
- Alternatives considered: shipping a completed example query; omitting known-answer verification.
- Affected artifacts: `student/first_pass_acceptance.sql`, `instructor_only/`, verification scripts, KPI Lab.

## DEC-P0-004 — Use a locked, staged interface

- Date: 2026-07-17
- Status: Current
- Decision: Only checkpoint `P0-C1` is active. Later stages are named but locked until Jeremy's prior work is verified.
- Rationale: The prototype must test staged teaching rather than act as a static answer key.
- Alternatives considered: showing the full lesson at once.
- Affected artifacts: `LESSON_TEMPLATE.md`, `lesson/stages/`, application source, `COURSE_STATE.json`.

## DEC-P0-005 — Use reproducible Node plus Python standard library

- Date: 2026-07-17
- Status: Current
- Decision: Use the locked application dependencies in `package-lock.json` and Python standard-library-only scripts under the declared Python version range.
- Rationale: This provides a polished local application while keeping the data/SQL harness small and inspectable.
- Alternatives considered: Python dashboard frameworks with additional packages; a generic in-browser SQL runner.
- Affected artifacts: `package.json`, `package-lock.json`, `pyproject.toml`, `README.md`.

## DEC-P0-006 — Require a complete beginner introduction before activities

- Date: 2026-07-18
- Status: Current
- Decision: Every lesson must introduce the scenario, purpose, terminology, expected outcome, prior-knowledge boundary, and sequence before presenting data or an activity.
- Rationale: Jeremy could complete the original checkpoint only after chat supplied context missing from the site. A dashboard without instruction is not a beginner lesson.
- Supersedes: Any interpretation of `DEC-P0-004` that allowed staged controls without staged teaching.
- Affected artifacts: `LESSON_TEMPLATE.md`, `PROJECT_SPEC.md`, KPI Lab source, future lesson specifications.

## DEC-P0-007 — Require the site to earn its place and avoid duplicate work

- Date: 2026-07-18
- Status: Current
- Decision: Use the site for meaningful data inspection, comparison, visualization, artifact construction, and progress review. Do not require it for redundant prose or require the same meaningful answer in both site and chat. Do not ask Jeremy to report static interface content.
- Rationale: Jeremy completed the original lesson entirely through chat, demonstrating that the site was not contributing to the learning.
- Alternatives considered: site-only delivery; chat-only delivery; mandatory transcription between surfaces.
- Affected artifacts: `LESSON_TEMPLATE.md`, `PROJECT_SPEC.md`, KPI Lab source, future lesson design.

## DEC-P0-008 — Allow browser-local draft persistence without changing authoritative progress

- Date: 2026-07-18
- Status: Current
- Decision: Lesson review choices and notes may autosave in the learner's browser on the learner's Mac. The interface must label this storage local and non-authoritative, offer reset, and never write canonical progress.
- Rationale: This prevents accidental loss without adding an account, backend, service, or competing source of truth.
- Extends: `DEC-P0-002`; the Course Portal remains read-only for progress.
- Affected artifacts: application source, `LESSON_TEMPLATE.md`, `PROJECT_SPEC.md`, `README.md`.

## DEC-P0-009 — Keep the Course Portal as a focused dashboard

- Date: 2026-07-18
- Status: Current
- Decision: Preserve Course Progress, current Learning Objectives, and Course Artifacts that link to authoritative documents. Add a concise current action, accurate timing, verification boundary, and collapsible full roadmap. Remove the unrelated glossary strip from the main dashboard; explain terms in context and add a separate reference later only when useful.
- Rationale: Jeremy values the dashboard and source-of-truth access but found unrelated static information distracting.
- Supersedes: The prototype-specific glossary placement required by `COURSE_CONTRACT.md` section 12, under the contract's latest-explicit-instruction authority rule. It does not remove contextual terminology instruction.
- Affected artifacts: Course Portal source, `PROJECT_SPEC.md`, `LESSON_TEMPLATE.md`.

## DEC-P0-010 — Recalibrate time estimates from observed learner time

- Date: 2026-07-18
- Status: Current
- Decision: Estimate the required `P0-C1` checkpoint at 20-30 minutes, optional deeper data exploration at 10-15 additional minutes, and one-time setup separately. Future estimates must distinguish required, optional, and setup time and be revised from observed experience.
- Rationale: Jeremy completed the guided definition work in under 30 minutes; the prior 1.5-2.5 hour display was materially overstated.
- Supersedes: The `P0` estimate in curriculum blueprint version 1.0.0.
- Affected artifacts: `CURRICULUM_MAP.md`, `LESSON_TEMPLATE.md`, Course Portal, KPI Lab.

## DEC-P0-011 — Add an obvious beginner entry point and one start command

- Date: 2026-07-18
- Status: Current
- Decision: `START_HERE.html` is the learner entry point. The technical README becomes optional reference. `npm run course` checks prerequisites, installs locked components only when absent, prepares local synthetic data, and starts the private site.
- Rationale: The v1.0.0 bundle exposed many implementation files and assumed setup knowledge not yet taught.
- Alternatives considered: an unsigned double-click Mac application, which could introduce confusing Gatekeeper warnings; retaining the technical README as the entry point.
- Affected artifacts: `START_HERE.html`, `README.md`, `package.json`, `scripts/start-course.sh`, `MANIFEST.md`.

## DEC-P0-012 — Preserve actual checkpoint evidence without overstating mastery

- Date: 2026-07-18
- Status: Current
- Decision: Record `P0-C1` as completed with substantial assistance. Preserve Jeremy's decisions and accepted wording, but do not claim independent mastery, SQL implementation, an independent challenge, teach-back, or limitation work.
- Rationale: Jeremy made and explained the core policy decisions, while the instructor supplied the missing introduction, guided the sequence, recommended one policy, and assembled the final prose.
- Affected artifacts: `COURSE_STATE.json`, `PROGRESS.json`, `METRIC_DICTIONARY.md`, `evidence/LEARNER_CHECKPOINT_P0-C1.md`, Course Portal, KPI Lab.

## DEC-P0-013 — Use one fresh chat per lesson

- Date: 2026-07-18
- Status: Current
- Decision: Each lesson begins in a fresh chat and ends before the next lesson starts. A lesson closeout must first explain what Jeremy completed, the assistance and mastery boundary, unfinished work, and the next lesson. Only then should it present the continuity packet for the new conversation. If Jeremy intentionally stops mid-lesson, create an interim continuity checkpoint.
- Rationale: Jeremy wants to prevent course conversations from becoming excessively long while retaining accurate continuity.
- Alternatives considered: one long course chat; switching chats on an informal schedule; switching at every small checkpoint.
- Affected artifacts: `LESSON_TEMPLATE.md`, `COURSE_STATE.json`, `SESSION_HANDOFF.md`, `NEXT_CHAT_PROMPT.md`, KPI Lab closeout, future lesson specifications.

## DEC-P0-014 — Let GitHub replace repeated bundle attachments after it is verified

- Date: 2026-07-18
- Status: Current
- Decision: Until a private course repository exists, a new lesson chat receives the complete ZIP, factual `SESSION_HANDOFF.md`, and exact `NEXT_CHAT_PROMPT.md`. After the GitHub lesson creates and verifies the private repository with explicit approval, new chats should read canonical course files there and downloadable bundles become periodic backups. Do not add a backend merely to transmit browser-local clicks or notes.
- Rationale: The repository can provide durable source and continuity without expanding the bounded prototype into a connected standalone product.
- Alternatives considered: attaching the full folder indefinitely; public hosting as the course source; backend synchronization of browser activity.
- Extends: `DEC-P0-002` and `DEC-P0-008`; browser-local activity remains private and non-authoritative.
- Affected artifacts: `README.md`, `LESSON_TEMPLATE.md`, `PROJECT_SPEC.md`, `SESSION_HANDOFF.md`, `NEXT_CHAT_PROMPT.md`, KPI Lab closeout, future GitHub lesson.

## DEC-P0-015 — Approve the v1.1.0 teaching design and release v1.2.0 continuity changes

- Date: 2026-07-18
- Status: Current
- Decision: Jeremy explicitly approved the v1.1.0 design and authorized v1.2.0 with the agreed lesson-transition changes. Record the prototype teaching format as approved while preserving `P0-C1` as completed with substantial assistance.
- Rationale: The revised site was clearer and the remaining agreed change was a bounded end-of-lesson continuity experience, not a new lesson or product expansion.
- Alternatives considered: leave the prototype approval pending; begin Module 0 in the same long chat; add a connected backend before continuing.
- Affected artifacts: all v1.2.0 canonical state, portal status, KPI Lab closeout, release evidence, durable bundle, and next-chat packet.

## DEC-C2-001 — Retarget the required course and approve architecture v2.0.0

- Date: 2026-08-08
- Status: Current
- Decision: Retarget the required course toward Strategic Finance, FP&A, Corporate Finance, Financial Analyst, finance-operations, business-operations, strategic-projects, and adjacent roles. Preserve the broader AI-enabled analyst-builder objective and the completed prototype. Remove obsolete AfterQuery work-trial interruption checks.
- Rationale: Jeremy is no longer advancing in the original human-data role, while the technical course remains valuable for his finance and operations direction.
- Supersedes: `COURSE_CONTRACT.md` v1.0.0 sections 1, 7, 10, and 16 where they conflict; `CURRICULUM_MAP.md` v1.2.0 flagship sequence and separate `M12` FP&A extension.
- Affected artifacts: all v2.0.0 canonical architecture, state, portal summary, continuity, evidence, and bundle files.

## DEC-C2-002 — Keep finance as context rather than the subject

- Date: 2026-08-08
- Status: Current
- Decision: Every required lesson must primarily teach or verify AI, data, SQL, Python, dashboard, automation, document, or agent capability. Finance explanation is limited to what the build needs. Coding explanation is limited to practical understanding, verification, debugging, and modification.
- Rationale: Jeremy explicitly does not want either a finance curriculum or a software-engineering curriculum.
- Alternatives considered: broad FP&A instruction; generalized coding bootcamp; no-code-only course.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `LESSON_TEMPLATE.md`, future lesson specifications.

## DEC-C2-003 — Require learner-built work dashboards and distinguish them from the Course Portal

- Date: 2026-08-08
- Status: Current
- Decision: A separate learner-built work dashboard is a central required artifact. Build a thin dashboard in `M4`, expand it in `M7`, and require `GATE-WORK-DASHBOARD`. Course Portal implementation or use provides no evidence toward this gate.
- Rationale: The Course Portal facilitates lessons; Jeremy's intended career skill is building dashboards used by finance and operations teams.
- Alternatives considered: count the Course Portal as dashboard experience; delay every dashboard build until the end; make dashboards optional.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `CAPABILITY_EVIDENCE_LEDGER.md`, portal terminology, future `M4` and `M7` lessons.

## DEC-C2-004 — Use recurring SQL, Python, automation, and capability gates

- Date: 2026-08-08
- Status: Current
- Decision: SQL and Python/pandas recur after their foundation modules. Add explicit basic and full gates plus work-dashboard, automation, applied-AI, AI-tool-development, and integrated AI/workflow gates. Maintain a capability evidence ledger.
- Rationale: One-time exposure is insufficient for proficiency or defensible resume language.
- Alternatives considered: module completion as evidence; informal instructor judgment; automatic resume labels.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `PROGRESS.json`, `CAPABILITY_EVIDENCE_LEDGER.md`, `LESSON_TEMPLATE.md`.

## DEC-C2-005 — Build one permissioned action-taking agent

- Date: 2026-08-08
- Status: Current
- Decision: Replace the strictly read-only final investigator with one finance-and-operations tool-using agent. It may read verified synthetic data, retrieve documents, use approved tools, draft actions, and perform low-risk sandbox actions only after explicit human approval. It may not alter authoritative data or act externally on its own.
- Rationale: A read-only assistant would not adequately teach agent actions, while unrestricted autonomy would be unsafe and difficult to verify.
- Alternatives considered: read-only assistant; autonomous production agent; multiple superficial agents.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `CAPABILITY_EVIDENCE_LEDGER.md`, future `M10` materials.

## DEC-C2-006 — Move human-data work to an optional specialization

- Date: 2026-08-08
- Status: Current
- Decision: Preserve `P0` as a completed pre-course prototype and optional transfer case. Exclude human-data-specific throughput, backlog, review-quality, first-pass acceptance, rework, and reviewer-disagreement metrics from the required flagship. Define optional specialization `OH1` for later use.
- Rationale: Combining finance and human-data metrics in one flagship would create overlap, dilute the primary project, and partially reverse the approved retargeting.
- Supersedes: the synthetic Human-Data Operations and Finance Control Center as the required flagship.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `PROJECT_SPEC.md`, `COURSE_STATE.json`, portal roadmap, continuity files.

## DEC-C2-007 — Use one strong flagship with realistic failures

- Date: 2026-08-08
- Status: Current
- Decision: Build one integrated AI-Enabled Finance Planning, Reporting, and Decision-Support System. Add realistic failure cases throughout and use compact transfer work instead of several shallow portfolio applications.
- Rationale: Depth, debugging, and a coherent interview story are more valuable than accumulating disconnected demonstrations.
- Alternatives considered: multiple independent capstones; an all-purpose finance-and-human-data system; idealized happy-path exercises.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `LESSON_TEMPLATE.md`, future project specifications and tests.

## DEC-C2-008 — Define AI-assisted operator-builder proficiency

- Date: 2026-08-12
- Status: Current
- Decision: Target AI-assisted operator-builder proficiency for strategic finance and operations, not unaided software development. AI may generate initial SQL, Python, dashboard, automation, and agent code. Do not require syntax memorization, substantial blank-page programs, or whole-codebase reading. Teach and assess business logic and data flow, independent reconciliation, controls, test cases, logs and errors, targeted inspection of relevant logic, bounded modification, and regression verification. Give SQL somewhat more direct practice; emphasize tracing, troubleshooting, modifying, and reusing Python/pandas scripts.
- Clarification: Output-based testing is the starting point, not the entire verification method. Inspect joins, filters, grain, nulls, mappings, time periods, and other relevant logic when plausible outputs could conceal errors. Independent modification permits disclosed AI assistance and means Jeremy identifies the problem or change, determines the intended result, directs or makes the bounded change, and verifies it.
- Rationale: Strategic finance and operations builders can use AI to produce initial code, but they remain responsible for specifications, controls, diagnosis, bounded changes, and evidence. Requiring unaided software development would misalign the course; accepting working AI output without independent verification would make its capability gates meaningless.
- Extends: `DEC-C2-002` and `DEC-C2-004`; it does not change the approved flagship, dashboards, automations, agent, optional specialization, or Module 0 boundaries.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `LESSON_TEMPLATE.md`, `PROJECT_SPEC.md`, `CAPABILITY_EVIDENCE_LEDGER.md`, state, progress, continuity, verification, and bundle release files.

## DEC-C2-009 — Make safe AI execution the default and assess operator judgment

- Date: 2026-08-14
- Status: Current
- Decision: When tooling and permissions allow, AI should write and execute routine local implementation, testing, and Git commands after Jeremy understands or approves the intended effect and boundary. Do not assess syntax or command-sequence recall when AI or a reference can perform it reliably. Jeremy must define or approve testable requirements, understand relevant state and risk, inspect targeted logic, reconcile results, direct or approve bounded corrections, and verify completion. Manual action remains appropriate for first exposure to a useful operational boundary, authentication, permissions, consequential external state, recovery, or lack of agent access.
- Clarification: AI execution does not transfer accountability to AI. Working output, clean Git state, or passing AI-authored tests alone remains insufficient. Assistance status reflects how much substantive specification, reasoning, diagnosis, and verification help Jeremy needed; AI supplying syntax or routine commands is not by itself a mastery penalty.
- Rationale: Jeremy's goal is expert AI-assisted building for internal strategic-finance and operations tools and portfolio work, not programming or command memorization. The M0-L2 experience showed that repeated command recall and micro-interruption can add cognitive load without improving the intended capability. Jeremy accepts targeted code/SQL inspection and occasional manual setup, authentication, permission, or recovery steps.
- Extends: `DEC-C2-008`; it does not relax verification, security, privacy, external-action approval, capability gates, or the requirement to understand relevant implementation and failure modes.
- Affected artifacts: `COURSE_CONTRACT.md`, `CURRICULUM_MAP.md`, `LESSON_TEMPLATE.md`, `CAPABILITY_EVIDENCE_LEDGER.md`, `COURSE_STATE.json`, `PROGRESS.json`, M0-L2 evidence, continuity, verification, portal mirrors, and bundle release files.

## DEC-M0-001 — Use a privacy-preserving personal Git identity as the Mac default

- Date: 2026-08-14
- Status: Current
- Decision: Use `Jeremy Bernhardt` as the future commit author name and Jeremy's exact GitHub-provided ID-based `noreply` address as the global personal Git email on this Mac. Set `user.useConfigOnly=true` so Git does not invent a missing identity. Use repository-local overrides when a future employer or separate GitHub identity requires different metadata. Keep the disposable M0 practice repository local-only; do not push its seven existing commits with the prior machine-derived email.
- Approval and privacy boundary: Jeremy confirmed his GitHub account username `jeremybernhardt`, selected the `noreply` option after privacy implications were explained, confirmed GitHub's private-email and email-exposure push-block settings, supplied the exact `noreply` address, and separately approved the global configuration change. No credential, personal email, remote, repository, push, pull, or deployment was created or exposed.
- Rationale: The choice supports attributable professional course and portfolio commits without embedding Jeremy's personal email. A global default is appropriate for his stated single personal GitHub identity; local overrides preserve separation if work identity is later required.
- Limitations: The setting affects only future commits, does not rewrite old metadata, does not hide the visible author name, does not protect file or message content, and does not prove authorship cryptographically. GitHub push blocking is a backstop rather than a complete outgoing-history audit.
- Affected artifacts: `COURSE_STATE.json`, `PROGRESS.json`, `CAPABILITY_EVIDENCE_LEDGER.md`, `lesson/M0-L3_GIT_IDENTITY_PRIVACY_GITHUB_READINESS.md`, `evidence/LEARNER_CHECKPOINT_M0-C3.md`, `SESSION_HANDOFF.md`, `NEXT_CHAT_PROMPT.md`, portal mirrors, verification, and bundle release files.

## DEC-C2-010 — Assess transfer rather than immediate repetition

- Date: 2026-08-14
- Status: Current
- Decision: Ask Jeremy for reasoning before supplying the substantive answer. When the instructor supplies an explanation after uncertainty or error, record the assistance and do not immediately ask Jeremy to repeat or paraphrase the same answer. If more evidence is materially necessary, use a later, genuinely new decision, scenario, diagnosis, or application.
- Rationale: Jeremy correctly identified that repeating an answer immediately after the instructor provides it measures short-term paraphrasing rather than useful understanding. The prior M0-L3 follow-up unnecessarily re-asked the supplied failure-analysis content.
- Extends: `DEC-P0-006`, `DEC-P0-007`, `DEC-C2-008`, and `DEC-C2-009`; it does not eliminate teach-back, independent modification, or limitation evidence when those can be collected authentically.
- Affected artifacts: `COURSE_CONTRACT.md`, `LESSON_TEMPLATE.md`, `PROGRESS.json`, M0-L3 evidence, continuity, verification, and future lesson design.

## DEC-M0-002 — Make the verified private GitHub repository authoritative

- Date: 2026-08-19
- Status: Current
- Decision: Use `jeremybernhardt/ai-operations-builder-course-private` on private `main` as the authoritative course source after its baseline and v2.0.4 closeout are independently verified. The separate local working folder is `/Users/Jeremy/Documents/Codex/AI_Operations_Builder_Course`. Keep the disposable practice repository local-only and preserve periodic versioned ZIP exports as backups, not competing sources of truth.
- Approval and external boundary: Jeremy approved the owner, name, destination, private visibility, included private curriculum and instructor material, exclusions, and done criteria. He separately approved creating the empty repository, connecting `origin`, and the first push. No public repository, deployment, remote practice repository, or portfolio publication was authorized.
- Verification: The independently verified first-push baseline is root commit `07170d06922211c5e4379fa4c534ea93da08dd0b`, tree `5386ba81e934717323a1256237cc380106ef0a78`, containing 118 intended files with the approved GitHub `noreply` author/committer identity and no practice history. GitHub confirmed the exact owner, private visibility, default branch, and commit. A fresh authenticated clone passed reconstruction, full tests/build, lint, and artifact validation.
- Rationale: The private repository now provides durable, inspectable, versioned continuity without repeated dependence on a complete ZIP or chat memory. Independent destination and reconstruction checks address risks that a successful push alone cannot.
- Limitations: Private GitHub is external cloud state and retains account, access, credential, metadata, deletion, and provider risks. Passing software checks does not prove all course content logically correct. No resume-level capability or independent mastery follows from repository operation.
- Affected artifacts: canonical authority/state, M0-L4 lesson and evidence, `AGENTS.md`, continuity, portal mirror, verification, release packaging, and future lesson startup.

## DEC-C2-011 — Use lesson-versioned continuity exports

- Date: 2026-08-19
- Status: Current
- Decision: Keep the canonical in-repository filenames `SESSION_HANDOFF.md` and `NEXT_CHAT_PROMPT.md`, while exported closeout copies include both the completed lesson and release version. For this closeout use `SESSION_HANDOFF_M0-L4_v2.0.4.md`, `NEXT_CHAT_PROMPT_AFTER_M0-L4_v2.0.4.md`, and `AI_Operations_Builder_Course_Prototype_v2.0.4_M0-L4.zip`.
- Rationale: Stable internal names preserve automation and authority references; versioned exports let Jeremy save successive lesson packets without duplicate filenames or ambiguity.
- Affected artifacts: `SESSION_HANDOFF.md`, `NEXT_CHAT_PROMPT.md`, release packaging, `README.md`, and lesson-closeout instructions.

## DEC-M0.5-001 — Use a work-practical scenario for builder-supervision lessons

- Date: 2026-08-20
- Status: Current
- Decision: Teach `M0.5-L1` through a bounded synthetic finance-operations task: specifying an Expense File Readiness Checker before implementation. Do not make Jeremy supervise or manually verify the course's own continuity machinery as the learner exercise. Keep course-state management an instructor/agent responsibility.
- Rationale: Jeremy identified that the initially prepared Lesson Readiness Checker was confusing, internally focused, and not representative of the practical work capabilities the course promises. The builder-supervision skill remains relevant, but its scenario must resemble useful analyst or operations work.
- Supersedes: The initially prepared `M0.5-L1` Lesson Readiness Checker scenario and the course-adjacent-task wording in the after-`M0-L4` next-task prompt for this lesson. It does not change the one-lesson authorization boundary or authorize the flagship, `M1`, or later `M0.5` lessons.
- Affected artifacts: `lesson/M0.5-L1_DEFINING_OUTCOMES_CONSTRAINTS_DONE_CRITERIA.md`, the eventual `M0.5-C1` evidence and closeout, continuity files, and future builder-supervision lesson design.

## DEC-M0.5-002 — Separate direct teaching, guided practice, and transfer demonstration

- Date: 2026-08-20
- Status: Current
- Decision: Use three visible modes throughout the remaining course: **Teach**, **Practice**, and **Demonstrate**. Teach the curriculum connection and concepts directly and model the reasoning with a complete worked example before asking Jeremy to apply them. Practice through one coherent, context-rich workplace scenario. Demonstrate transfer later with a genuinely different scenario and reduced scaffolding. Do not use a chain of questions, file comparison, or line-picking exercise as a substitute for the teaching section.
- Rationale: During `M0.5-L2`, Jeremy correctly observed that the initial delivery asked many potentially useful questions without enough context or an explicit connection to the curriculum. The questions prompted thought but made the lesson feel like comparing two files rather than learning a reusable builder-supervision method. Instruction, guided application, and assessment need distinct roles.
- Extends: `DEC-P0-006`, `DEC-P0-007`, `DEC-C2-010`, and `DEC-M0.5-001`. It preserves reasoning-before-answer and genuinely new transfer while requiring the underlying concepts to be taught before guided questioning.
- Affected artifacts: `COURSE_CONTRACT.md`, `LESSON_TEMPLATE.md`, `lesson/M0.5-L2_REVIEWING_AI_BUILDER_PLAN_ASSUMPTIONS_SCOPE.md`, future lesson specifications and delivery, closeout continuity, and release evidence.

## DEC-M0.5-003 — Match evidence precision to the task stage

- Date: 2026-08-21
- Status: Current
- Decision: In conceptual or theoretical work, require enough specificity to demonstrate the intended judgment and verification design, but do not force Jeremy to invent arbitrary numeric fixtures after the concept is already clear. Require exact known-answer values, deterministic reconciliation, and file-integrity evidence when the course is testing a real file, calculation, implementation, or material ambiguity.
- Rationale: During the `M0.5-L2` transfer, Jeremy had already identified the plan's material assumptions, scope violations, permission errors, human-review boundary, and the need for a small known-answer comparison. Requiring invented invoice identifiers and amounts added ceremony without testing another capability. Jeremy correctly distinguished that situation from later work with a real file, where exact values and source-integrity checks would be necessary.
- Extends: `DEC-C2-008`, `DEC-C2-010`, and `DEC-M0.5-002`. It does not relax deterministic verification for implemented artifacts or real calculations.
- Affected artifacts: `COURSE_CONTRACT.md`, `LESSON_TEMPLATE.md`, `lesson/M0.5-L2_REVIEWING_AI_BUILDER_PLAN_ASSUMPTIONS_SCOPE.md`, `evidence/LEARNER_CHECKPOINT_M0.5-C2.md`, future lesson design, and release continuity.

## DEC-C2-012 — Use selective, auditable context and staged reliability maintenance

- Date: 2026-08-25
- Status: Current
- Decision: Replace full-history lesson startup with the authoritative core, current lesson, prerequisite evidence, and explicitly relevant artifacts. Scan the full repository locally through a bounded metadata-only validator; load older content only to resolve a dependency, conflict, recovery problem, or failed quality check. Acknowledge learner answers before long tool work, recover interrupted current-lesson artifacts without advancing progress, bound interactive processes, and exclude transient Excel lock files from Git and packages. Roll out `REL-0` through `REL-3` before resuming M0.5-L3; defer `REL-4` until the M0.5 boundary and two successful selective-context tasks.
- Controls: Initial startup must remain at or below 17,000 source words and at least 40% below the 31,889-word legacy baseline. More than 5% mandatory-core growth triggers audit; more than 10% unexplained growth blocks release. Full semantic audits remain direct-context work at routing changes, module boundaries, or unresolved conflicts.
- Rationale: Repeated long task stalls followed learner submissions. Smaller auditable startup reduces context and failure exposure while deterministic reconciliation and targeted fallback preserve course quality.
- Affected artifacts: startup instructions, continuity prompt, reliability plan/scanner/tests, state, verification, packaging, and checkpoint evidence.

## DEC-C2-013 — Accelerate build-first instruction and add a bounded job-search transfer

- Date: 2026-08-25
- Status: Current
- Decision: Use gap-based, build-first teaching, targeting roughly 65-75% building/debugging/modifying/testing, 15-25% verification/explanation, and 10-15% concepts. Ask at most one or two substantive questions before hands-on work unless risk blocks action. Shorten scaffolding when prior evidence truly proves the capability; integrate teach-back into explanation of the actual artifact; keep learner-facing openings and endings brief. Count course-building supervision as evidence for requirements, scope, approval, and AI collaboration, but not automatic proof of technical verification.
- Transfer project: Keep the finance/operations flagship primary. Reuse selected module skills in a job-search monitor: contract in `M1`, approved retrieval and storage in `M5`, dashboard in `M7`, scheduling/recovery in `M8`, evaluated matching in `M9`, permissioned investigation without applying or contacting in `M10`, and synthetic public portfolio treatment in `M12`. Real resume and listing data remain private.
- Rationale: Jeremy has demonstrated basic AI collaboration and wants faster progress toward defensible app, dashboard, automation, and agent-building skills without weakening independent verification.
- Affected artifacts: teaching contract/template, curriculum map, continuity prompt, README, state, and future lesson design.

## DEC-C2-014 — Prioritize early working apps and teach foundations through the build

- Date: 2026-10-03
- Status: Current
- Human direction: Jeremy wants the course to be as practical as possible, to build useful projects and apps with AI and limited coding knowledge as quickly as possible while learning enough to produce consistent, high-quality work. He also identified that accelerated practice had removed necessary teaching and context, and that standalone contribution-writing work had low value for learning to build.
- Decision: Use a small working app as the next milestone, then teach the relevant data, SQL, Python, interface, integration, automation, and AI concepts through building, explaining, changing, debugging, and verifying the actual system. AI supplies routine scaffolding and execution. Teach enough context for each next action; neither prolonged theory nor unexplained tasks serve this direction. Preserve independent expected results, targeted inspection, meaningful learner-owned changes, failure handling, and honest assistance evidence.
- Sequence change: Defer `M0.5-L5 — Explaining Human and AI Contributions Without Inflation` as a standalone checkpoint; handle contribution accuracy briefly at later project closeouts and `M12`. Do not mark L5 passed or the original five-lesson M0.5 sequence complete. Verified C1-C4 evidence is the explicit prerequisite exception for progression. Prepare and teach only `M1-L1 — First Working Finance App` in a fresh task: a bounded local synthetic actual-versus-budget expense app, as the first piece of the existing finance flagship. Do not wait for full SQL/Python modules before AI generates the initial app. M2/M3 deepen those skills through it; M4 verifies the integrated data path after the gates.
- Supersedes: The mandatory standalone L5-before-M1 prerequisite in contract v2.0.8 section 5 and the M1 prerequisite in curriculum v2.0.6; the requirement to wait until M4 for the first working app; and the scaffold-reveal restriction only insofar as it prevented an assisted initial implementation. Extends `DEC-C2-008`, `DEC-C2-009`, `DEC-C2-013`, and `DEC-M0.5-002`. Historical checkpoint and assistance records remain unchanged.
- Boundary: This direction authorizes the bounded blueprint/delivery revision and only the next M1-L1 lesson. It does not authorize later implementations, external accounts, spending, deployment, publication, commit, or push. All technical capability gates remain unearned. The Expense File Readiness Checker is not implemented by this change. Estimates remain provisional until actual project-building pace is observed.
- Affected artifacts: contract, curriculum, lesson template, current lesson scheduling, state/progress, capability ledger, handoff/prompt, next lesson specification, portal mirror, reconstruction/release checks, and reliability-boundary evaluation.
