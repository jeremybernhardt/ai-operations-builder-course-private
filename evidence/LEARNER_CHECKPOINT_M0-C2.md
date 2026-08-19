# Learner Checkpoint Evidence — M0-C2

Checkpoint ID: `M0-C2`  
Lesson: `M0-L2 — Local Branches, Merges, and Safe Recovery`  
Date: `2026-08-14`  
Decision: **Completed with substantial assistance**  
Independent mastery claimed: **No**

## Objective and artifact

Jeremy reused the disposable local-only repository at `/Users/Jeremy/Desktop/ai-ops-git-practice-m0l1` to isolate changes on branches, compare them with `main`, merge them locally with fast-forward protection, and correct one committed mistake without rewriting history. The repository remains on Jeremy's Mac and is not embedded in this bundle.

## Starting-state evidence

Learner-reported output confirmed the exact repository path, clean `main`, three commits ending at `5c178e8`, ignored `.env`, and no configured remote. The installed Git, Node.js, npm, and Python versions were not changed or reinstalled.

## What Jeremy did

- Created and inspected `lesson/m0-l2-guided` from clean `main` at `5c178e8`.
- Added a bounded `NOTES.md` branch-practice statement, inspected unstaged and staged diffs, and created commit `79d4537` (`Add branch practice note`).
- Compared the branch with `main`, switched to `main`, and completed a fast-forward-only merge.
- Deliberately committed an incorrect verification statement as `2bf6eae`, then created corrective revert `ffdad15` and verified `NOTES.md` matched the known-good `79d4537` snapshot.
- Planned the comparable branch sequence and explained why a branch permits review before changing `main`.
- Created `lesson/m0-l2-challenge`, defined and approved a three-item safe-change checklist, and added it to `README.md`.
- Inspected the diff before staging. The inspection exposed a missing Markdown separator caused by the pre-existing missing end-of-file newline; Jeremy restored and reapplied the bounded change correctly.
- Staged only `README.md`, reviewed the staged diff, and created commit `b1bf13d` (`Add safe local change checklist`).
- Compared the branch with `main`, completed a fast-forward-only merge, and ran the full final verification set.

## What Jeremy explained

- A branch is a movable label pointing to a commit, not a copied project folder.
- New content exists in the working file, is proposed through staging, and is preserved in a commit snapshot; the current branch label advances to the new commit.
- A fast-forward merge moves the receiving branch label to an existing descendant commit.
- A clean status proves the working files and staging area match the current commit; it does not prove a merge occurred or that content is correct.
- A blank file-limited branch diff proves the compared file snapshots match, not that their content is logically correct.
- `revert` creates a new inverse commit and preserves the mistaken commit as auditable history.
- Correctly executed Git operations can still preserve incorrect business content.

## Assistance record

- Maximum help: **Full walkthrough** for the guided branch, merge, and committed-recovery cycles.
- Comparable challenge: **Substantial guided help**. Jeremy supplied the correct high-level sequence and branch rationale. The instructor supplied exact command references, verification scaffolding, a correction to an overclaimed checklist statement, detection of the Markdown separator defect, and repeated conceptual correction for branch and clean-status semantics.
- AI-generated command syntax is allowed under the course's operator-builder standard and is not, by itself, a deficiency. The substantial-assistance decision reflects the amount of conceptual and verification reasoning supplied by the instructor in this first exposure.
- Jeremy explicitly clarified that the course should emphasize AI execution, strong specifications, targeted inspection, risk judgment, and verification rather than unnecessary command or syntax memorization. This is recorded in `DEC-C2-009`.

## Verification and reconciliation

- Final `git status --short --branch` reported clean `main`.
- `git rev-list --count HEAD` reported seven commits.
- Final history ended at `b1bf13d`, with `main` and `lesson/m0-l2-challenge` pointing to that commit; `lesson/m0-l2-guided` remained at `79d4537`.
- The history preserved `2bf6eae` and corrective revert `ffdad15`.
- `git diff 79d4537 HEAD -- NOTES.md` was blank immediately after the revert, verifying restoration of the known-good file snapshot.
- `git diff main..lesson/m0-l2-challenge -- README.md` was blank after the challenge merge.
- `git remote -v` returned no output.
- `git check-ignore -v .env` identified `.gitignore:1:.env`; `git ls-files .env` returned no output.

## Limitations and unfinished work

- Command recall is not independent and is not the course target; using AI and reference notes remains appropriate.
- Branch and merge concepts required repeated guided correction during this first exposure.
- Merge conflicts and divergent-history resolution were not practiced.
- Git identity remains auto-derived as `lord0fham <Jeremy@MacBook-Pro.local>` and has not been intentionally configured.
- Branches and Git verification do not establish that business logic or content is correct.
- Remotes, pull/push, GitHub access, and the private course repository remain unfinished.
- Repository evidence was verified through learner-reported outputs rather than direct instructor filesystem access.

## Gate decision

No resume-level capability gate was earned. `M0-C2` adds foundational local branch, merge, recovery, and verification evidence only. Module 0 is not complete, and independent mastery is not claimed.
