---
name: gitgud
description: >-
  Use ALWAYS before starting repository changes and any commit, push, amend, merge,
  rebase, cherry-pick, or force-push. Commit and push task branches while working;
  guard protected branches.
---

Work reaches protected branches only through PRs. It is done on task branches with linear, rebase-based history, and each logical change is committed and pushed as soon as its checks pass, without asking first.

## Never

- Commit to, push to, or rewrite `main`, `master`, `production`, `staging`, or any other branch the repository protects. Other people deploy and branch from these.
- Stage with `git add -A` or `git add .`. Staging files by name is what keeps unrelated work, secrets, and accidental artifacts out of a commit.
- Bypass hooks through `--no-verify`, configuration, or environment. A failing hook is a check to satisfy.
- Force-push without an explicit lease; see Rewriting published history.
- Merge to resolve divergence. History stays linear, so divergence is resolved by rebasing. Merging a PR you were authorized to merge is a different thing and is fine.
- Pick `ours` or `theirs` blindly in a conflict, or leave a merge, rebase, or cherry-pick unfinished.

## Start

Run `git status` and `git branch --show-current`. If a merge, rebase, cherry-pick, or similar operation is already in progress and you did not start it, stop and report it. Neither continue nor abort it: someone else is midway through it.

## Choose the branch

Changes requested on an existing PR or branch go to its head branch in its head repository, whoever created it. Check it out (`gh pr checkout <n>` for a PR), commit there, and push there. Open no side branch and no second PR unless asked, because a second destination splits the review. If the head cannot be resolved or you cannot push to it, keep the work local and report; never substitute another destination.

All other work gets a dedicated, unprotected branch:

- Reuse an existing branch only for the same unmerged scope it was created for. When in doubt, create a new one and say so.
- Fetch, then branch from the base the repository designates, or otherwise from origin's default branch (`git ls-remote --symref origin HEAD`). Stack on another branch only when asked.
- Create it with `git switch --no-track -c <name> <remote>/<base>`. `--no-track` stops the new branch from tracking the base, so a bare `git push` can never land there.
- Name it by the repository's convention, or otherwise `<type>/<short-kebab-summary>` with type one of feat, fix, chore, refactor, docs. Include a ticket ID when one was supplied.

A branch is shared when there is evidence that others use or depend on its history: commits by other authors, a branch or PR stacked on it, or the user saying so. On a shared branch, never force-push, never amend published commits, and rebase only your own unpublished commits.

## Sync

Fetch `origin` and any other relevant remote before editing, then bring the branch up to date with its own remote:

- Only behind: fast-forward.
- Diverged: rebase your own unpublished commits onto the remote tip. If the remote was rewritten, or the rebase would rewrite commits that are already published, stop and report instead.
- Not pushed yet: bring it up to date with the latest tip of its base.

If the branch has an open PR (`gh pr view`), also fetch the PR's actual base. When the branch is behind it, rebase onto it; on a shared branch, report the lag instead and continue from the synced head. If the base cannot be determined, say so and sync only against the branch's own remote.

Uncommitted work must come through the sync intact. If the sync cannot complete, do not start editing; report what blocked it.

## Commit and push

Do this for each logical change as soon as it is finished:

1. Review `git diff` and `git diff --cached`. Stage the task's changes by file name, leave unrelated work alone, and keep secrets and accidental artifacts out.
2. Run the required checks: the tests, lint, typecheck, and build that the repository documents or its CI runs for the files touched. If you can find none, say so in your report.
3. Commit, following the repository's conventions. Each commit is one complete logical change; do not commit unfinished work just to save progress. If a hook edits files, review its edits and re-stage only the ones that belong.
4. Repeat Sync. If it changed the branch, rerun the checks on the result.
5. Check the remote, the destination, and the outgoing commits before pushing: `git push origin HEAD:main` targets `main` whatever branch you are on. Set upstream on the first push (`-u`).
6. Verify with `git log -1 --stat`, `git status`, and the push output.

At the end of the task, repeat Sync and check the result once more.

## Rewriting published history

Amending or rebasing commits that are already pushed means the next push is a force-push. Never do this on a shared branch. Elsewhere:

1. Before rewriting, fetch and save the remote tip your work already includes.
2. Push with `--force-with-lease=<branch>:<saved-sha>`, never plain `--force`. The explicit SHA makes the push fail if anyone pushed after you looked.
3. If the push is rejected, fetch and reassess whether the branch is shared. If the remote only added commits on top of the saved SHA, bring them over with `git cherry-pick <saved-sha>..<new-sha>`, check the result, and retry once with the lease on `<new-sha>`. In any other case, or if the retry is rejected too, report.

## Conflicts

Resolve a conflict only when the intent of both sides is clear. Otherwise abort your own rebase or cherry-pick and report.
