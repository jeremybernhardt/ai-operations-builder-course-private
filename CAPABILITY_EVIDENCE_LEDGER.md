# Capability Evidence Ledger

Ledger version: `2.0.3`  
Learner: Jeremy Bernhardt  
Current status: no v2 resume-level gate has been earned

This file records evidence for potential skill claims. Completing a lesson, viewing a tool, or passing a software build is not enough. Every gate requires a working artifact, deterministic verification, plain-language explanation, independent modification or unfamiliar problem, and honest assistance history. AI may generate initial code, but a working AI-generated output alone cannot earn a gate.

## Evidence fields required at every gate

- Artifact and stable evidence paths
- Business or operational decision supported
- What Jeremy decided personally
- What AI generated
- What Jeremy inspected, changed, directed, and debugged
- Maximum assistance level used
- Deterministic checks and independent reconciliation
- Teach-back result
- Independent or unfamiliar modification
- Known limitations and failure modes
- Gate decision and defensible resume wording, if any

Independent modification means Jeremy independently identifies the problem or requested change, determines the intended result, directs or makes the bounded change, and verifies it without introducing another error. AI assistance is permitted and disclosed; all-code-from-scratch performance is not required.

## Current gates

| Gate ID | Resume label | Planned checkpoint | Evidence requirement | Current status |
|---|---|---|---|---|
| `GATE-SQL-BASIC` | SQL (Basic) | `M2` | Schema inspection; filters, aggregates, joins, `CASE`, dates/nulls; reconciliation; debugging; independent query change | Not started |
| `GATE-PYTHON-PANDAS-BASIC` | Python (pandas, Basic) | `M3` | File I/O, cleaning, filtering, grouping, merging, dates/nulls, function change, error diagnosis, reconciliation | Not started |
| `GATE-SQL` | SQL | `M6` | Repeated multi-table analysis, CTE/subquery use, duplicate-amplification prevention, unfamiliar schema investigation, independent repair | Not started |
| `GATE-PYTHON-PANDAS` | Python (pandas) | `M6` | Reusable validated pipeline/analysis, functions, error handling, database/API/file use, independent business-rule change | Not started |
| `GATE-WORK-DASHBOARD` | Dashboard Development | `M7` | Learner-built work dashboard, decision design, SQL/Python lineage, filters/drilldowns, error repair, independent new view | Not started |
| `GATE-WORKFLOW-AUTOMATION` | Workflow Automation | `M8` | Trigger-to-action workflow, success/failure/rerun paths, logs, retries/idempotency, missing-input handling, approval, independent change | Not started |
| `GATE-APPLIED-AI` | Applied AI | `M9` | Structured outputs, grounded document/number use, separate evaluation, failure taxonomy, injection defense, escalation | Not started |
| `GATE-AI-TOOL-DEVELOPMENT` | AI Tool Development | `M10` | Working multi-tool agent, permissions, traces, failures, approval-gated sandbox action, independently modified tool | Not started |
| `GATE-APPLIED-AI-WORKFLOW-AUTOMATION` | Applied AI & Workflow Automation | `M10` | Evaluated AI integrated into controlled workflow without overriding deterministic calculations or human decisions | Not started |

## Preserved prototype evidence

`P0-C1` supports only these current statements:

- Jeremy defined an operational metric and its edge-case policies with guided help.
- Jeremy recognized duplicate, missing-outcome, denominator, and rework issues.

It does not support SQL, Python, work-dashboard, automation, agent, or independent-mastery claims. Evidence: `evidence/LEARNER_CHECKPOINT_P0-C1.md`.

## Module 0 foundational evidence

`M0-C1` supports these non-resume-level statements:

- Jeremy created and used a disposable local-only Git repository on his Mac.
- He distinguished working files, staging, commits, and GitHub; inspected unstaged and staged diffs; created three commits; and restored a deliberate unwanted change.
- In a comparable challenge, he staged only `NOTES.md`, reviewed the staged content, verified `.env` remained ignored and absent from history, committed the file, and confirmed a clean three-commit repository with no configured remote.
- He explained `M`, `AM`, `.env` versus `.env.example`, local versus remote, and the plain-text limitation of `.gitignore`.

Maximum help was a full walkthrough for the guided cycle; the comparable Git challenge required limited help, with assistance confined to file-creation syntax. Checkpoint status is **Completed with limited assistance**, not independent mastery and not completion of Module 0. Evidence: `evidence/LEARNER_CHECKPOINT_M0-C1.md`.

`M0-C2` supports these additional non-resume-level statements:

- Jeremy used local branches to isolate and compare bounded changes, then completed two fast-forward-only merges.
- He corrected a committed mistake with an auditable revert and verified the restored file against a known-good commit.
- He completed a comparable README change, used a diff to expose and correct a formatting defect before commit, and verified clean final state, equal merged branch content, no remote, and an ignored/untracked `.env`.
- He explained commits as stored snapshots with parent history, branches as movable commit labels, fast-forward as movement of the receiving label, and the difference between clean state, equal snapshots, and logical correctness.

Maximum help was a full walkthrough for the guided branch and recovery cycles and substantial guided help for the comparable challenge. Exact command references are permitted and do not by themselves reduce operator-builder evidence; substantial assistance is recorded because core branch and status concepts required repeated instructor correction. Checkpoint status is **Completed with substantial assistance**, not independent mastery and not completion of Module 0. Evidence: `evidence/LEARNER_CHECKPOINT_M0-C2.md`.

`M0-C3` supports these additional non-resume-level statements:

- Jeremy chose and separately approved a privacy-preserving future commit identity using his real name and GitHub-provided ID-based `noreply` address.
- He distinguished future configuration from existing commit metadata, selected global scope for his personal default, and correctly chose a repository-local override for a future employer identity.
- Direct checks verified the configuration source and effective future identity while proving the disposable repository remained clean, local-only, remote-free, and unchanged at seven commits.
- He recognized that a private repository retains metadata and that push crosses an external boundary, although his initial public-visibility wording required correction.

Maximum help was a full walkthrough for the identity/privacy model and failure/limitation analysis plus guided help for the identity and scope decisions. Jeremy did not independently identify the full outgoing-history checks or an additional limitation after the explanation; no immediate repetition was counted as evidence. Checkpoint status is **Completed with substantial assistance**, not independent mastery and not completion of Module 0. Evidence: `evidence/LEARNER_CHECKPOINT_M0-C3.md`.

## Claim rule

Resume wording is created only after the corresponding gate passes. It must distinguish a verified synthetic course project from professional experience and describe AI assistance accurately.
