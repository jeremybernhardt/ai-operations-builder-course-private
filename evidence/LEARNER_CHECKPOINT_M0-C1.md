# Learner Checkpoint Evidence — M0-C1

Checkpoint ID: `M0-C1`  
Lesson: `M0-L1 — Local Git Foundations`  
Date: `2026-08-12`  
Decision: **Completed with limited assistance**  
Independent mastery claimed: **No**

## Objective and artifact

Jeremy used a disposable local-only repository at `/Users/Jeremy/Desktop/ai-ops-git-practice-m0l1` to learn the working-file, staging, commit, history, ignore, restore, and local-versus-remote boundaries. The repository remains on Jeremy's Mac and is not embedded in this bundle.

## Environment evidence

Learner-reported Terminal output confirmed:

- current home path `/Users/Jeremy`;
- Apple Command Line Tools path `/Library/Developer/CommandLineTools`;
- Git `2.50.1 (Apple Git-155)`;
- Node.js `24.18.0`;
- npm `11.16.0`; and
- Python `3.13.14`.

Git was initially unavailable. After the download was explained, Jeremy approved and completed Apple's Command Line Tools installation. Previously verified Node, npm, and Python were not reinstalled.

## What Jeremy did

- Created and entered a bounded disposable Desktop folder, verified its path, and initialized a local repository on `main`.
- Created `README.md`, `.gitignore`, `.env.example`, and a simulated `.env` secret.
- Used Git output to verify that `.env` was ignored while the three safe files were staged.
- Inspected the staged diff and created commit `449f723` (`Create safe Git practice repository`).
- Modified `README.md`, interpreted `M`, inspected the diff including an invisible newline change, staged it, and created commit `0f2e55c` (`Add Git learning note`).
- Added a deliberate unwanted change and restored the file from the latest commit.
- Completed a comparable `NOTES.md` cycle, including recognizing the `AM` state after editing a staged file, restaging the current content, reviewing the staged diff, verifying `.env` remained ignored, and creating commit `5c178e8` (`Added the NOTES.md file`).
- Verified a clean working tree, a three-commit history, four tracked files, no tracked or historical `.env`, and no configured Git remote.

## What Jeremy explained

- `.env` contains local private settings; `.env.example` is a safe template showing required setting names.
- Saving changes the visible file; committing records the staged state in local Git history.
- `M` indicates a modified tracked file; `AM` occurred because `NOTES.md` was staged and then modified again.
- A green `+` in a diff marks added content; a `-`/`+` pair can represent an invisible newline change rather than a visible wording change.
- The repository remained local and was not on GitHub.
- `.gitignore` does not encrypt the secret; the ignored `.env` remains plain text on the Mac.

## Assistance record

- Maximum help: **Full walkthrough** during the guided first Git cycle.
- Comparable challenge: **Limited assistance**. Jeremy independently chose and ran the Git inspection, staging, diff, ignore verification, commit, history, and clean-state checks. Assistance addressed `printf` file-creation syntax, not the Git process.
- AI/instructor supplied the initial commands, mental model, safety boundaries, and explanations. Jeremy executed them on his Mac, inspected actual outputs, asked clarifying questions, corrected one malformed `git log` command, and performed the comparable Git cycle.

## Verification and reconciliation

- `git status` reported a clean tree after every completed commit cycle.
- `git log --oneline` showed exactly three commits in the expected order.
- `git ls-files` listed `.env.example`, `.gitignore`, `NOTES.md`, and `README.md`.
- `git ls-files .env` and `git log --all -- .env` returned no output.
- `git remote -v` returned no output.
- The restored README no longer contained the deliberate unwanted sentence.

## Limitations and unfinished work

- Git command recall is not independent; using notes or AI remains appropriate.
- Git identity was auto-derived as `lord0fham <Jeremy@MacBook-Pro.local>` and has not been intentionally configured.
- `.gitignore` is not encryption, can be overridden, and cannot remove a secret already committed.
- Branches, merges, broader recovery, remotes, pull/push, GitHub access, and the private course repository have not been taught or verified.
- The local practice repository was verified through learner-reported outputs rather than direct instructor filesystem access.

## Gate decision

No resume-level capability gate was earned. `M0-C1` establishes foundational local Git evidence only. Module 0 is not complete, and independent mastery is not claimed.
