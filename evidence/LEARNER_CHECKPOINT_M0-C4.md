# Learner Checkpoint Evidence — M0-C4

Checkpoint ID: `M0-C4`
Lesson: `M0-L4 — Private GitHub Course Repository and First Verified Push`
Date: `2026-08-19`
Decision: **Completed with substantial assistance**
Independent mastery claimed: **No**

## Objective and learner deliverable

Move the authoritative private course into a separately initialized GitHub repository that a fresh task can access and reconstruct, without publishing the disposable practice history, secrets, personal email, or unexpected files. Add concise repository-level agent instructions and preserve a verified versioned backup.

## Jeremy's intended outcome and decisions

Before the detailed implementation explanation, Jeremy stated that:

- the course material must remain private because the lessons are for him;
- the disposable practice history is separate because its exercise is finished; and
- a push would not prove that the content was accurate.

He approved this bounded specification:

- owner: `jeremybernhardt`;
- repository: `ai-operations-builder-course-private`;
- local course folder: `/Users/Jeremy/Documents/Codex/AI_Operations_Builder_Course`;
- visibility: private only;
- contents: the complete canonical course bundle, hidden setup files, lessons, evidence, `instructor_only/`, source/tests, and root `AGENTS.md`;
- exclusions: the outer source ZIP, duplicate external continuity copies, disposable practice `.git` history, actual `.env`, credentials, dependencies, build/runtime caches, logs, and unexpected files; and
- done: independently verified owner, visibility, branch, commit, complete intended tree, metadata, exclusions, local tracking, clean reconstruction, canonical authority transition, and a versioned backup.

Jeremy separately gave explicit informed approval immediately before:

1. creating the empty private GitHub repository;
2. connecting the local course repository to it as `origin`; and
3. pushing local `main` at `07170d0` to `origin/main`.

He also approved installation of the verified official GitHub CLI, browser-device authentication, entering the one-time code, and the displayed GitHub CLI permissions.

## Verified local preparation

- The v2.0.3 ZIP passed complete CRC and path-safety checks and contained every required canonical, lesson, and evidence file.
- A separate local repository was created from the bundle; no `.git` directory or commit object came from the practice repository.
- The root `AGENTS.md` records startup, authority, environment, privacy, and verification requirements.
- The initial commit contained 118 intended files and one root commit only.
- Root commit: `07170d06922211c5e4379fa4c534ea93da08dd0b`.
- Tree: `5386ba81e934717323a1256237cc380106ef0a78`.
- Author and committer: `Jeremy Bernhardt <306348304+jeremybernhardt@users.noreply.github.com>`.
- No actual `.env`, credential, archive, dependency folder, cache, log, or practice-history object was included.
- Pre-push JSON, reconstruction, release, build, rendered-output, lint, artifact, and secret checks passed.

## Authentication and credential handling

The official GitHub CLI v2.97.0 arm64 release was downloaded from GitHub. Its archive SHA-256 matched GitHub's published checksum, and its macOS code signature was valid. Browser-device authentication completed for `jeremybernhardt` with the permissions Jeremy approved.

An initial sandbox fallback stored the credential in the user configuration file. Work stopped before push, and the credential was immediately migrated into macOS Keychain without displaying it. Verification showed the active token source as the keyring and no token marker in `~/.config/gh/hosts.yml`; that file remained permission-restricted. The local course repository uses a repository-only Git credential helper pointing to the verified CLI. No password, token, personal email, or credential was requested from Jeremy or committed.

## Independent remote verification

After the approved first push, independent checks confirmed:

- exact repository: `jeremybernhardt/ai-operations-builder-course-private`;
- visibility: private;
- default branch: `main`;
- remote commit: `07170d06922211c5e4379fa4c534ea93da08dd0b`;
- local and remote tree: 118 blobs with no missing or extra path;
- expected canonical, lesson, evidence, instructor-only, hidden/setup, source, and test files present;
- correct `noreply` author and committer metadata;
- one root commit only, with no disposable-practice commits or old machine-derived email history;
- local `main` tracking `origin/main` at the same commit; and
- excluded runtime files, actual `.env`, credentials, personal email, archives, and unexpected files absent.

A fresh private clone in a new temporary folder reproduced the exact commit and passed 55 reconstruction checks, locked dependency installation, the full test/build suite, two rendered-output tests, lint, and artifact validation. This proved the repository can restore the course without the original working folder or chat memory.

## Learner reasoning and limitation evidence

Jeremy correctly identified the intended privacy boundary, the need to keep the disposable history separate, and a materially relevant verification limitation: a push does not prove the content is accurate. The instructor expanded the explanation to cover cloud/account risk and the fact that a push also does not prove owner, visibility, branch, exact files, metadata, secrets, tracking, or reconstruction. Under `DEC-C2-010`, Jeremy was not asked to echo that supplied expansion immediately.

## Assistance record

- Maximum help: **Full walkthrough** for the local/remote model, authentication, permissions, credential handling, complete-history review, implementation, and independent verification design.
- Jeremy personally defined or approved the intended outcome, private/external-action boundary, repository specification, and every consequential external action.
- AI performed the authorized routine local implementation, Git operations, installation checks, and deterministic verification under `DEC-C2-009`.
- The instructor supplied most detailed risk and evidence interpretation, so the result is **Completed with substantial assistance**.

## Gate and advancement decision

No resume-level capability gate was earned; every v2 gate remains `Not started`. A working repository and successful push are not proficiency evidence by themselves. `M0-C4` adds non-resume-level evidence for private repository specification, approval boundaries, GitHub authentication, exact remote verification, and reconstruction.

The planned Module 0 lesson sequence is complete with substantial assistance. Independent Module 0 mastery is not claimed. The private repository becomes the authoritative course source after the v2.0.4 closeout commit is pushed and independently verified; the versioned ZIP is retained as a backup.
