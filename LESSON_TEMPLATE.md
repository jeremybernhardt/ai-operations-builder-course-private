# Staged Lesson Template

Template ID: `LESSON-TEMPLATE-001`  
Version: `2.0.7`

## Required lesson metadata

- Stable module, lesson, checkpoint, and skill IDs
- Operational scenario and user
- Prerequisites
- Estimated learner time
- Current project contribution
- Definition of done
- Verification evidence paths
- Scope and non-goals
- Primary technical capability and applicable evidence gate
- Required finance/business context, limited to what the technical work needs

## Learner-facing introduction requirement

Before work begins, use a brief plain-language opening that states:

1. what Jeremy will build, debug, or change;
2. why it is useful;
3. the genuinely new skill; and
4. what success looks like.

Introduce unfamiliar terms only when they are needed for the next action. Keep versions, inventories, test commands, and maintenance details in instructor records unless they matter to a learner decision or approval.

No required lesson may exist solely to teach finance. Finance concepts are supplied only to the depth needed for the technical attempt. No required lesson may exist solely to teach coding abstractions; coding is taught to support practical understanding, verification, debugging, and modification.

The target is AI-assisted operator-builder proficiency, not unaided software development. AI may generate initial SQL, Python, dashboard, automation, and agent code. Do not use blank-page syntax recall, substantial unaided program creation, or whole-codebase reading as default teaching or assessment methods.

When available and authorized, AI should execute routine local commands and implementation steps. Teach the intended effect, material risk, and verification boundary before consequential actions, but do not turn repeated command entry into the learning objective. Jeremy may use exact command references. Assess his specification, plan approval, targeted inspection, interpretation of evidence, diagnosis, bounded correction, and final verification. Use manual execution when it exposes a useful operational boundary or AI cannot safely act.

The introduction is part of the lesson, not optional instructor commentary. A learner should not have to infer the scenario from a dashboard or ask chat to supply missing context.

## Visible teaching modes

Keep these purposes clear, but shorten or combine a stage when prior evidence genuinely proves it:

1. **Teach** — show where the capability fits, explain the missing gap directly, and model only the reasoning needed to begin.
2. **Practice** — apply the taught concepts to one coherent workplace scenario with enough context and scaffolding to make each decision meaningful.
3. **Demonstrate** — use genuinely different evidence or a scenario with reduced scaffolding to assess transfer, then complete verification and limitation work.

Questions should help Jeremy apply or examine a concept after it has been taught. Do not make a chain of questions, line-picking exercise, or comparison between unexplained files carry the instructional burden. Files, plans, diffs, dashboards, and other artifacts are evidence and practice surfaces; they are not substitutes for the direct teaching section. Explain the connection to prior and later modules at the beginning and reinforce it at closeout.

Default to accelerated, gap-based, build-first delivery: roughly 65-75% building, debugging, modifying, and testing; 15-25% verification and explanation; and 10-15% concepts. Ask at most one or two substantive questions before hands-on work unless unresolved risk or scope makes action unsafe. Use real artifacts early. Excel may be a familiar validation bridge, then move promptly to SQL, Python, databases, dashboards, APIs, and automations.

Calibrate specificity to what the lesson actually verifies. Conceptual transfer may be established by a correct decision, material-risk explanation, and appropriate verification design without forcing Jeremy to invent arbitrary numbers. Require exact inputs, outputs, totals, hashes, or other deterministic evidence when a real file, calculation, implementation, or ambiguous business rule is under test. If Jeremy already demonstrates the conceptual distinction, do not add artificial precision merely to prolong the exercise.

## Site and chat roles

- Use the site when interaction materially helps: inspecting or comparing data, visualizing a process or metric, constructing an artifact, or reviewing progress.
- Do not require the site merely to repeat prose that is more naturally handled in instruction.
- Do not ask Jeremy to transcribe static headings, warnings, counts, or other content that the course already knows.
- Do not require the same meaningful answer in both the site and chat.
- Chat provides personalized explanation, coaching, evaluation, and troubleshooting. The site must remain understandable without chat substituting for missing lesson content.
- Distinguish the presentation-only Course Portal from learner-built work dashboards. Course Portal work never counts toward `GATE-WORK-DASHBOARD`.
- Use one fresh chat per lesson so the instructional conversation remains bounded. Do not move to a new chat mid-lesson unless Jeremy intentionally stops; if that happens, create an interim continuity checkpoint.
- Browser-local draft persistence is allowed only for learner convenience. It must be labeled local and non-authoritative, provide a reset control, and never edit canonical progress.
- Required, optional, and one-time setup time must be estimated separately and recalibrated from observed learner experience.

## Adaptive stage sequence

1. **Business problem** — establish the decision, user, stakes, and raw inputs.
2. **Technical learning objectives** — state observable capabilities, not vague familiarity or finance-topic coverage.
3. **Context and short concept lesson** — explain only the business context and technical ideas needed for the next attempt.
4. **Guided example when needed** — demonstrate a smaller or adjacent case without solving the learner's checkpoint; omit it when comparable evidence proves the capability.
5. **Guided project implementation** — Jeremy attempts the current project step.
6. **Different demonstration** — use a comparable new case or already-recorded genuinely different evidence; do not repeat a proved skill merely to fill a stage.
7. **Verification** — deterministic checks plus independent reconciliation appropriate to risk.
8. **Artifact explanation** — integrate teach-back into Jeremy's explanation of the actual rule, implementation, evidence, and failure points.
9. **Reflection and limitations** — Jeremy identifies at least one limitation or failure mode.
10. **Lesson closeout** — summarize the completed work, assistance and mastery boundary, evidence, unfinished items, and next lesson before presenting continuity files.
11. **Progress and handoff** — update canonical state immediately after a passed checkpoint and prepare the next-chat transition.

Stages may be combined, but verification, honest assistance, limitation analysis, and any required unfamiliar transfer may not be silently removed. If Jeremy demonstrates the gap during the build, stop asking similar questions and continue to the next useful capability.

Inject realistic failures progressively: duplicates, missing inputs, incorrect joins, changed columns, stale data, mapping errors, API failures, rerun duplication, AI hallucinations, malicious document instructions, and permission violations as relevant. Do not wait until an advanced module to teach verification and debugging.

Begin verification with observable outputs, control totals, known-answer cases, logs, and error messages. Add targeted inspection of the relevant query, function, mapping, filter, join, grain, null treatment, or time rule whenever a plausible output could hide a material defect. A working AI-generated output alone cannot satisfy a checkpoint.

Give SQL somewhat more direct practice because of its usefulness in finance and operations. For Python/pandas, emphasize tracing execution, diagnosing failures, modifying bounded functions or rules, and reusing practical scripts rather than unaided program creation.

## Reveal discipline

- Reveal one stage at a time and stop at explicit checkpoints.
- Prefer coherent work blocks over unnecessary command-by-command interruption once the effect and safety boundary are understood.
- Never reveal a final definition, completed query/script, expected test output, answer key, or independent-challenge solution before a genuine attempt.
- Instructor-only fixtures may exist for deterministic grading but must not be linked or displayed in student-facing material.
- Never simulate Jeremy's answer or mark an unattempted stage complete.
- Evaluate each submission against the frozen definition and evidence before advancing.
- Ask for reasoning before giving the substantive answer. If an explanation has already supplied that answer, record the help and do not ask Jeremy to restate it immediately. Use a genuinely new application later when additional evidence is necessary; do not turn teach-back into short-term paraphrasing.

## Help ladder

1. **Nudge:** directional hint only.
2. **Guided help:** diagnostic question, smaller step, or partial structure.
3. **Full walkthrough:** complete explanation, then require a comparable new exercise before independent mastery.

Record the highest help level used at each checkpoint. A full walkthrough cannot produce independent mastery on the same exercise.

## Verification and mastery

Software readiness and learner mastery are recorded separately. Advancement normally requires:

- applicable deterministic checks pass;
- Jeremy teaches back the logic accurately;
- Jeremy makes one independent change or solves a comparable exercise; and
- Jeremy identifies a limitation or failure mode.

Use only the five mastery statuses defined in `COURSE_CONTRACT.md`. Record exceptions and rationale rather than silently lowering standards.

Passing a resume-level gate additionally requires the evidence fields in `CAPABILITY_EVIDENCE_LEDGER.md`. Exposure, guided completion, or a passing software build is insufficient.

For assessment, **independent modification** means Jeremy independently identifies the problem or requested change, states the intended result, directs or makes the bounded modification, and verifies the corrected behavior without introducing another error. AI help is permitted and must be recorded; independent modification does not mean all code was produced unaided.

## Instructor closeout

After a passed checkpoint:

1. update `COURSE_STATE.json`;
2. update `PROGRESS.json` with assistance and evidence;
3. update `CAPABILITY_EVIDENCE_LEDGER.md` when a gate or material skill claim is affected;
4. update the factual checkpoint portion of `SESSION_HANDOFF.md`;
5. update affected definitions or specifications;
6. append material decisions to `DECISION_LOG.md`; and
7. briefly explain what Jeremy completed, how it was verified, what he can explain or modify, the honest mastery boundary, and what comes next;
8. present a clearly labeled **Continue in a New Conversation** section only after that explanation;
9. update `NEXT_CHAT_PROMPT.md` with exact new-chat instructions;
10. save a durable checkpoint immediately; and
11. end the lesson chat. Begin the next lesson only in a fresh chat.

Before the private GitHub repository exists, the continuity packet contains the complete ZIP, `SESSION_HANDOFF.md`, and `NEXT_CHAT_PROMPT.md`. After the repository is established and its access is verified, the repository becomes the durable course source and should replace repeated ZIP attachments. Keep periodic downloadable bundles as backups. Do not add a backend merely to expose browser-local activity to chat.
