# AI Operations Builder Course Bundle v2.0.3

Learner entry point: open `START_HERE.html`. This README is the technical setup, verification, continuity, and recovery reference.

This local/private bundle contains:

- the approved v2.0.0 bounded course architecture, v2.0.1 operator-builder standard, v2.0.2 safe AI-execution clarification, and v2.0.3 transfer-not-repetition teaching correction;
- the preserved v1.2.0 prototype **From Raw Project Data to a Verified Operating Metric**;
- canonical course state, progress, decisions, capability gates, handoff, and next-chat instructions; and
- no future full lesson, production portal, public deployment, remote repository, or standalone course product.

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
- The v2.0.0 architecture, v2.0.1 operator-builder standard, v2.0.2 safe AI-execution clarification, and v2.0.3 teaching-strategy correction are approved.
- `M0-L1 — Local Git Foundations` is completed with limited assistance; independent mastery and Module 0 completion are not claimed.
- `M0-L2 — Local Branches, Merges, and Safe Recovery` is completed with substantial assistance; independent mastery and Module 0 completion are not claimed.
- `M0-L3 — Git Identity, Privacy, and GitHub Readiness` is completed with substantial assistance; an approved privacy-preserving future identity is verified, while independent mastery and Module 0 completion are not claimed.
- Every resume-level capability gate remains `Not started`.
- The next authorized work is only `M0-L4 — Private GitHub Course Repository and First Verified Push` in a fresh chat. Creation, connection, and push still require separate explicit approval at the relevant boundary.

## Required course direction

The main project is the synthetic **AI-Enabled Finance Planning, Reporting, and Decision-Support System**. Jeremy will build an early work-dashboard slice after SQL/Python foundations, a full work dashboard later, a controlled automation, evaluated document/AI tools, and one permissioned agent with approval-gated sandbox actions. Human-Data and AI Operations is an optional later specialization, not the required flagship.

See `CURRICULUM_MAP.md` for the bounded module sequence and `CAPABILITY_EVIDENCE_LEDGER.md` for the evidence required before any resume-level skill label is defensible.

## Continuing Module 0 in a new chat

Until the private GitHub course repository exists, use this three-item continuity packet:

1. `AI_Operations_Builder_Course_Prototype_v2.0.3.zip` — complete authoritative pre-GitHub bundle;
2. `SESSION_HANDOFF.md` — factual briefing about verified state, boundaries, and next action; and
3. `NEXT_CHAT_PROMPT.md` — exact instructions for the new conversation.

Open a new chat, attach all three items, paste the text beneath **Then send this prompt** in `NEXT_CHAT_PROMPT.md`, and send it.

After Module 0 creates and verifies the private course repository with Jeremy's explicit approval, later chats should read canonical files from that repository. Repeated ZIP attachments should end, while periodic versioned bundles remain backups.

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

Use a fresh copy of the durable v2.0.3 bundle to restore intentionally incomplete learner files. Do not delete canonical state, progress, capability evidence, or preserved learner evidence.

## Source of truth

Before a private course repository exists, this complete v2.0.3 bundle is authoritative. `COURSE_STATE.json`, `PROGRESS.json`, and `CAPABILITY_EVIDENCE_LEDGER.md` record course position, mastery, and skill evidence. The Course Portal is a generated read-only mirror; browser-local notes, chat history, and saved memory are non-authoritative.

See `MANIFEST.md` for file roles.
