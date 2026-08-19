# M0-L2 — Local Branches, Merges, and Safe Recovery

Lesson ID: `M0-L2`  
Checkpoint: `M0-C2`  
Status: Completed on `2026-08-14` with substantial assistance  
Evidence: `evidence/LEARNER_CHECKPOINT_M0-C2.md`

## Scenario and purpose

An operator-builder supervising AI-generated work needs a safe way to isolate a proposed change, compare it with a known-working state, incorporate it deliberately, and correct a committed mistake without concealing history. This lesson added that local Git control layer before GitHub, remotes, or the private course repository.

## Deliverable

A disposable local-only repository containing a guided branch change, a comparable branch change, two verified fast-forward merges, and one committed mistake corrected with an auditable revert.

## Verification method

Learner-reported Terminal outputs for path, clean state, branch positions, commit graph, working and staged diffs, branch comparisons, fast-forward merges, revert history, ignored/untracked `.env`, and absence of remotes; plus learner planning, content decisions, teach-back, and limitation analysis.

## Scope completed

- Branches as movable commit labels rather than copied folders.
- The relationship among working files, staging, commits, `HEAD`, and the current branch.
- Creating and inspecting local branches with a clean starting state.
- Making, staging, committing, and comparing a bounded branch change.
- Fast-forward-only local merges and post-merge comparison.
- Correcting a committed mistake with `revert` while preserving history.
- A comparable README checklist change with a detected and corrected formatting defect.
- The distinction between clean repository state, equal branch snapshots, and logical correctness.

## Not completed

Merge conflicts, branch cleanup conventions, intentional Git identity configuration, remotes, pull, push, GitHub access, the private course repository, and later modules.

## Mastery boundary

The guided branch and recovery cycles used full walkthroughs. The comparable challenge used an explained command reference and substantial guided help. Jeremy chose the safe sequence and branch rationale, contributed the intended checklist content, executed the workflow, and ultimately explained the commit/branch model, revert, verification evidence, and a correctness limitation. Repeated conceptual correction was required for the branch-as-label model and the meaning of clean status. Status is `Completed with substantial assistance`. Independent mastery and completion of Module 0 are not claimed.
