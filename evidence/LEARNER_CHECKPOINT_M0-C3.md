# Learner Checkpoint Evidence — M0-C3

Checkpoint ID: `M0-C3`  
Lesson: `M0-L3 — Git Identity, Privacy, and GitHub Readiness`  
Date: `2026-08-14`  
Decision: **Completed with substantial assistance**  
Independent mastery claimed: **No**

## Objective and deliverable

Jeremy established an explicit privacy-preserving personal Git identity and a verified readiness boundary before any GitHub repository or remote action. The deliverable was the identity/privacy/readiness decision and verified current state, not a remote repository.

## Verified starting state

Direct instructor filesystem access confirmed the disposable repository at `/Users/Jeremy/Desktop/ai-ops-git-practice-m0l1` was on clean `main` at `b1bf13d` with seven commits. `main` and `lesson/m0-l2-challenge` pointed to `b1bf13d`; `lesson/m0-l2-guided` pointed to `79d4537`. History preserved mistake `2bf6eae` and revert `ffdad15`; `.env` existed locally, was ignored and untracked, and had no Git history; no remote was configured. The restored `NOTES.md` and merged challenge `README.md` comparisons remained blank.

Identity inspection showed:

- global `user.name=lord0fham` from `/Users/Jeremy/.gitconfig`;
- no local, global, or system `user.email`;
- no configured `user.useConfigOnly` value; and
- effective derived author/committer identity `lord0fham <Jeremy@MacBook-Pro.local>`.

All seven existing commits stored that same prior author and committer metadata. The observation refined the handoff wording: the name was explicitly present in global configuration, while the email was machine-derived; whether the name had been intentionally chosen could not be inferred.

## Official guidance verified

Current GitHub documentation was checked on 2026-08-14. It confirmed that:

- the Git commit name is not the same as a GitHub username;
- local configuration can override global configuration for one repository;
- GitHub associates command-line commits with an account through the commit email;
- a GitHub-provided `noreply` address can preserve personal-email privacy and attribution;
- changing name or email affects future commits rather than prior commits;
- GitHub's command-line email-exposure block is a backstop that checks the most recent commit; and
- push sends local commits to a named remote, while pull retrieves and integrates remote changes.

References: `https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git`, `https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address`, `https://docs.github.com/en/account-and-profile/reference/email-addresses-reference`, `https://docs.github.com/en/account-and-profile/how-tos/email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address`, `https://docs.github.com/en/get-started/git-basics/about-remote-repositories`, `https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository`, and `https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository`.

## Jeremy's decisions and actions

- Confirmed an existing personal GitHub account with username `jeremybernhardt` and access to its email settings.
- Selected `Jeremy Bernhardt` as the visible future commit-author name.
- Chose the recommended GitHub-provided ID-based `noreply` address instead of embedding his personal email.
- Confirmed that **Keep my email addresses private** and **Block command line pushes that expose my email** are enabled.
- Supplied the exact `noreply` address without sharing a credential, token, password, or personal email.
- Confirmed this should be the default personal GitHub identity across repositories on his Mac.
- Gave separate informed approval after the exact scope, privacy effects, and non-retroactive limitation were explained.
- Correctly chose a repository-local override rather than replacing the personal global identity if a future employer repository requires a work identity.
- Agreed that the disposable practice repository should remain local-only because its old metadata is unnecessary to publish.

## Configuration applied and deterministic verification

With separate informed approval, AI set these global values:

- `user.name=Jeremy Bernhardt`;
- `user.email=306348304+jeremybernhardt@users.noreply.github.com`; and
- `user.useConfigOnly=true`.

Post-change checks proved all three values came from `/Users/Jeremy/.gitconfig`, and Git reported the effective future author and committer identity as `Jeremy Bernhardt <306348304+jeremybernhardt@users.noreply.github.com>`. No test commit was needed.

The repository remained on clean `main` at `b1bf13d` with seven commits and unchanged branch positions. `.env` remained ignored and untracked, no remote appeared, and each existing commit still stored `lord0fham <Jeremy@MacBook-Pro.local>`. This reconciled the intended prospective change with unchanged historical evidence.

## Learner explanation and assistance record

Jeremy explained that Git configuration controls name/email metadata attached to commits, that a private repository does not remove the metadata it stores, and that a push crosses an external boundary. His initial wording overclaimed that any push makes the information public; the instructor corrected this to distinguish private authorized access from public visibility. He identified selecting the correct outgoing commits as an important pre-push check.

After global-versus-local implications were explained, Jeremy correctly applied the concept to a new work-repository scenario by choosing a local override to keep identities separate. He correctly stated that new configuration would not conceal old commit metadata. He was unsure which full-history and destination evidence to inspect after an accidental push and could not independently identify another privacy limitation; the instructor supplied that failure analysis.

- Maximum help: **Full walkthrough** for the beginner identity/privacy model and failure/limitation analysis.
- Decision help: **Guided help** for choosing `noreply`, global scope, and the no-guessing safeguard.
- AI executed the approved configuration and all routine verification checks under `DEC-C2-009`.
- Jeremy supplied the consequential identity, privacy, scope, external-action, and approval decisions.
- Status is therefore **Completed with substantial assistance**, not independent mastery.

## Teaching correction

After the instructor supplied the missing failure-analysis answer, Jeremy objected that asking him to repeat the same answer did not make instructional sense. The objection was correct. The repeated prompt was withdrawn, no echo was treated as evidence, and `DEC-C2-010` now requires reasoning before explanation and a genuinely new application if later evidence is necessary.

## Limitations and unfinished work

- The seven existing practice commits retain the prior machine-derived email; new configuration does not rewrite them.
- The practice repository must remain local-only unless a later, separately approved plan addresses that history.
- `noreply` hides the personal email but not the visible name, commit content, messages, filenames, or secrets.
- A global personal identity can be inappropriate for employer work unless both name and email are overridden locally.
- Git metadata is not cryptographic proof of authorship.
- GitHub's email-exposure block does not replace a full outgoing-commit, author-email, secret, branch, destination, and visibility review.
- No remote authentication, repository access, push, pull, or private course repository has been verified.

## Gate and advancement decision

No resume-level capability gate was earned. `M0-C3` adds foundational Git identity, privacy, configuration-scope, and external-action-boundary evidence only. Module 0 remains incomplete, and independent mastery is not claimed. The next lesson may prepare and teach only `M0-L4 — Private GitHub Course Repository and First Verified Push` in a fresh chat, with separate explicit approval before creating or connecting the repository or pushing anything.
