# AI Operations Builder Course Repository v2.0.9

The 2026-10-03 delivery revision is prepared for private main. Verify publication through live local/remote commits and working state; preserve any pending canonical edits until the approved push is verified.

Learner entry point: open `START_HERE.html`. This README is the technical setup, verification, continuity, and recovery reference.

This private repository contains:

- the approved v2.0.0 bounded course architecture and v2.0.1-v2.0.8 operator-builder, execution, teaching, repository-authority, reliability, and verified-checkpoint records;
- the preserved v1.2.0 prototype **From Raw Project Data to a Verified Operating Metric**;
- canonical course state, progress, decisions, capability gates, handoff, and next-chat instructions; and
- the verified Module 0 sequence, completed M0.5-L1 through M0.5-L4 builder-supervision checkpoints, and repository-level `AGENTS.md`; and
- a bounded next-lesson specification for `M1-L1 — First Working Finance App`, with standalone M0.5-L5 deferred by `DEC-C2-014`; and
- no later lesson implementations, production portal, public deployment, public repository, or standalone course product.

The required course teaches AI-assisted SQL, Python/pandas, data pipelines, work dashboards, automation, document tools, and permissioned agents using finance as the primary application context. It targets AI-assisted operator-builder proficiency, not unaided software development. It is not a broad finance curriculum or a software-engineering curriculum. The Course Portal facilitates lessons and never counts as evidence that Jeremy can build work dashboards.

## Requirements

- Node.js 24 LTS with npm
- Python 3.11-3.13 using only the standard library for the preserved prototype
- macOS and a modern browser

Jeremy's observed environment is Node.js `24.18.0`, npm `11.16.0`, Python `3.13.14`, and Git `2.50.1 (Apple Git-155)`. Do not reinstall them.

## Beginner start command

From the unzipped course folder:

```bash
npm run course
```

The command checks local prerequisites, runs `npm ci` only when locked supporting components are absent, prepares the synthetic SQLite data, and starts the private application. Open the address labeled `Local`. Stop it with `Control-C`.

No account, public deployment, external database, model API, or Python package installation is required for the preserved prototype.

## Explicit clean setup

For reconstruction or troubleshooting:

```bash
npm ci
python3 scripts/setup.py
```

`npm ci` installs the exact supporting components in `package-lock.json` inside this folder. `setup.py` validates the synthetic CSV, rebuilds `database/prototype.sqlite`, and regenerates read-only portal snapshots and artifact copies.

## Development start

```bash
npm run dev
```

## Verification

Run the deterministic checks, production build, and rendered-output tests:

```bash
npm test
```

Run the bounded scan-only continuity and context checks by themselves:

```bash
npm run test:reliability
```

Run static checks:

```bash
npm run lint
```

Run the Sites artifact validator:

```bash
npm run validate:artifact
```

Passing software tests does not imply learner mastery or satisfy a capability gate.

## Current learner and course position

- `P0-C1` is completed with substantial assistance.
- Independent metric mastery, SQL implementation, teach-back, and limitation work are not claimed.
- The prototype is preserved as a pre-course teaching-format artifact and optional human-data transfer case.
- The v2.0.0 architecture and v2.0.1-v2.0.8 clarifications, continuity decisions, and verified checkpoints are approved.
- `M0-L1 — Local Git Foundations` is completed with limited assistance; independent mastery and Module 0 completion are not claimed.
- `M0-L2 — Local Branches, Merges, and Safe Recovery` is completed with substantial assistance; independent mastery and Module 0 completion are not claimed.
- `M0-L3 — Git Identity, Privacy, and GitHub Readiness` is completed with substantial assistance; an approved privacy-preserving future identity is verified.
- `M0-L4 — Private GitHub Course Repository and First Verified Push` is completed with substantial assistance. The exact private destination, first commit/tree, metadata, exclusions, tracking, and fresh-clone reconstruction were independently verified.
- `M0.5-L1 — Defining Outcomes, Constraints, and Done Criteria` is completed with limited assistance. The guided expense-file brief used substantial instructor/AI structure; a different variance-report transfer passed after one targeted revision.
- `M0.5-L2 — Reviewing an AI Builder Plan, Assumptions, and Scope` is completed with limited assistance. Jeremy made material guided plan decisions and independently reviewed a different accounts-payable plan; direct teaching and limited file-integrity help are recorded honestly.
- `M0.5-L4 — Debugging from Evidence and Directing a Bounded Modification` is completed with limited assistance. Jeremy diagnosed and constrained an inclusive seven-day correction, then independently diagnosed and bounded a different rule-precedence repair.
- Every resume-level capability gate remains `Not started`.
- The planned Module 0 lesson sequence is complete with substantial assistance; independent mastery and resume-level proficiency are not claimed.
- `M0.5-L5` is deferred without a passed checkpoint; the original five-lesson sequence is not complete. `DEC-C2-014` permits progression on verified C1-C4 evidence.
- The next authorized work is only `M1-L1 — First Working Finance App`, in a fresh task. Expense-checker implementation and later lessons remain postponed.

## Required course direction

The main project is the synthetic **AI-Enabled Finance Planning, Reporting, and Decision-Support System**. Jeremy now builds a small local app in M1, then learns SQL/Python by inspecting, changing, and verifying its data and behavior. M4 strengthens the integrated data path; later milestones add a full dashboard, controlled automation, evaluated AI tools, and a permissioned agent. Concepts are taught in context with enough explanation to understand the next action. A bounded job-search monitor reuses those skills at selected milestones without becoming a second curriculum. Human-Data and AI Operations remains optional.

See `CURRICULUM_MAP.md` for the bounded module sequence and `CAPABILITY_EVIDENCE_LEDGER.md` for the evidence required before any resume-level skill label is defensible.

## Continuing in a new task

The authoritative remote source is private repository `jeremybernhardt/ai-operations-builder-course-private` on `main`. Verify that main and this checkout contain v2.0.9; if its approved publication is incomplete, preserve the pending local canonical edits and report the boundary. Read `NEXT_CHAT_PROMPT.md`. Repeated complete-ZIP attachment is no longer required.

For Jeremy's saved lesson archive, the M0.5-L4 closeout exports are:

- `SESSION_HANDOFF_M0.5-L4_v2.0.8.md`;
- `NEXT_CHAT_PROMPT_AFTER_M0.5-L4_v2.0.8.md`; and
- `AI_Operations_Builder_Course_Prototype_v2.0.8_M0.5-L4.zip`.

The canonical in-repository filenames remain `SESSION_HANDOFF.md` and `NEXT_CHAT_PROMPT.md` so setup and verification stay stable. The ZIP is a verified backup, not the authoritative live source.

## Recovery

Rebuild local data and snapshots:

```bash
python3 scripts/setup.py
```

Reinstall locked Node components:

```bash
npm ci
```

If port 5173 is busy:

```bash
npm run dev -- --port 4174
```

Use the verified private repository or the v2.0.8 M0.5-L4 backup bundle to restore intentionally incomplete learner files. Do not delete canonical state, progress, capability evidence, or preserved learner evidence.

## Source of truth

Private repository `jeremybernhardt/ai-operations-builder-course-private` on `main` is authoritative. `COURSE_STATE.json`, `PROGRESS.json`, and `CAPABILITY_EVIDENCE_LEDGER.md` record course position, mastery, and skill evidence. The Course Portal is a generated read-only mirror; backup ZIPs, browser-local notes, chat history, and saved memory are non-authoritative.

See `MANIFEST.md` for file roles.
