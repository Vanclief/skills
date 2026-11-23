---
name: gitgud
description: >-
  Use ALWAYS before starting repository changes and any commit, push, amend, merge,
  rebase, cherry-pick, or force-push. Commit and push task branches while working;
  guard protected branches.
---

This skill is the user's standing request to commit and push task branches. Do both for each logical change as soon as its checks pass, without asking, even where general agent instructions say to commit only on request. History stays linear and rebase-based.

The repository's own instructions and the user's explicit instructions override this and the defaults below. The Never list gives way only to an explicit instruction from the user that names both the branch and the action, and only for that action: "commit to main" allows a commit and a normal push to `main`, never rewriting or force-pushing it.

## Never

- Commit to, push to, or rewrite `main`, `master`, `production`, `staging`, the repository's default branch, or any branch it protects (`gh api repos/{owner}/{repo}/branches/<branch> --jq .protected`). Other people deploy and branch from these.
- Stage with `git add -A` or `git add .`. Staging by name is what keeps unrelated work, secrets, and accidental artifacts out of a commit.
- Bypass hooks through `--no-verify`, configuration, or environment. A failing hook is a check to satisfy or report.
- Force-push without an explicit lease (see Rewriting published history).
- Merge to resolve divergence; rebase instead, because history stays linear. Merging a PR you were authorized to merge is a different thing and is fine.
- Pick `ours` or `theirs` blindly in a conflict, or leave unfinished a merge, rebase, cherry-pick, or similar operation that you started.
- Discard, reset, or overwrite uncommitted changes you did not make. They are the user's work.
- Make WIP or checkpoint commits on your own, whether to save progress or to clear the tree for a sync.

## Start

Run `git status` and `git branch --show-current`.

- At any point, if a merge, rebase, cherry-pick, or similar operation is in progress that you did not start, or you cannot tell whether you did, stop and report it. Neither continue nor abort it: someone else is midway through it.
- If `HEAD` is detached, create the branch where you are (`git switch -c <name>`) and say which commit it starts from. That commit is its base: branching from the default branch instead would leave it behind, and so would rebasing onto another base unasked.
- If the repository has no remote, branch from the local default branch, commit locally, skip the fetch and push steps, and say so in your report.

## Choose the branch

Changes requested on an existing PR or branch go to its head branch in its head repository, whoever created it. Check it out (`gh pr checkout <n>` for a PR), commit there, and push there. Open no side branch and no second PR unless asked, because a second destination splits the review. If the head cannot be resolved or you cannot push to it (a fork PR whose `maintainerCanModify` is false, for example), keep the work local and report; never substitute another destination.

All other work gets a dedicated, unprotected branch:

- If you start on a branch that has no commits beyond its base and is not on the remote, typically one a worktree tool created for this task, use it. If it tracks the base (`git rev-parse --abbrev-ref @{u}` shows `origin/main` or similar), run `git branch --unset-upstream` first.
- Otherwise reuse an existing branch only for the same unmerged scope it was created for. When in doubt, create a new one and say so.
- Fetch, then branch from the base the repository designates, or otherwise from origin's default branch (`git ls-remote --symref origin HEAD`). Stack on another branch only when asked.
- Create it with `git switch --no-track -c <name> <remote>/<base>`. `--no-track` keeps the base from becoming the upstream, so a bare `git push` cannot target it under default settings.
- Name it by the repository's convention, or otherwise `<type>/<short-kebab-summary>` with type one of feat, fix, chore, refactor, docs. Include a ticket ID when one was supplied.

A branch is shared when there is evidence that others use or depend on its history, for example commits by other people on the branch itself (not its base), a branch or PR stacked on it, or the user saying so. On a shared branch, never force-push, never amend published commits, and rebase only your own unpublished commits.

## Sync

Before editing and before every push, fetch `origin` and any other relevant remote, then bring the branch up to date with its own remote:

- Only behind: fast-forward (`git merge --ff-only --autostash <remote>/<branch>`).
- Diverged because you rewrote pushed commits yourself: do not rebase; Sync is done. The push uses the lease if the remote tip is still the SHA you saved, and step 3 of Rewriting published history if the tip has moved.
- Diverged any other way: rebase your own unpublished commits onto the remote tip (`git rebase --autostash <remote>/<branch>`). If the remote was rewritten (`git fetch` reports a forced update, or `git reflog <remote>/<branch>` shows one since you last synced), or the rebase would rewrite commits that are already published, stop and report instead.
- Not pushed yet: rebase onto the latest tip of its base (`git rebase --autostash <remote>/<base>`). A branch started from a detached commit or tag has no newer tip: leave it where it is and use that commit as `<base>`.

If the branch has an open PR (`gh pr view`), also fetch the PR's actual base. Rebase onto it only when the PR conflicts with the base, the repository requires an up-to-date branch to merge, or the user asks; `gh pr view --json mergeable,mergeStateStatus` reports `CONFLICTING` and `BEHIND` for the first two. Otherwise report how far behind it is and carry on: every rebase of a pushed PR forces a push that reruns CI and loses reviewers their place. For the same reason, add new commits to an open PR rather than amending pushed ones. On a shared branch, report the lag and continue from the synced head even then. If `gh pr view` or the base fetch fails, say so and sync only against the branch's own remote.

Uncommitted work must come through the sync intact: after an `--autostash`, confirm it was reapplied. An `autostash` entry left in `git stash list` means it was not, even when the command exits 0. Then, or if a switch or rebase refuses because of uncommitted work, stop and report without touching the stash or the tree. If a sync cannot complete, at the start or before a push, stop editing and pushing and report what blocked it.

## Commit

For each logical change, as soon as it is finished:

1. Review `git diff` and `git diff --cached`. Stage the task's changes by file name, leave unrelated work alone, and keep secrets and accidental artifacts out. If a file holds someone else's uncommitted edits as well as yours, stage only your hunks.
2. Run the required checks: the ones the user asked for and the ones the repository says to run before committing, plus any CI checks that can run locally for this change. Report any you could not run, or that none exist. A failure already present on the base is not yours to fix: confirm your change adds none, and report it.
3. Commit, following the repository's conventions. If a hook edits files, review its edits and re-stage only the ones that belong. If a hook blocks the commit for reasons outside your change, leave the change uncommitted and report.

A change that adds a check failure stays uncommitted. Report it with the failure and continue with changes that do not depend on it.

## Push

Every push goes through these steps, including force-pushes and retries:

1. Repeat Sync. If it changed the branch, rerun the checks on the result.
2. Check the remote, the destination, and the outgoing commits (`git log <remote>/<branch>..HEAD`, or `<remote>/<base>..HEAD` before the first push), and name the destination explicitly: `git push origin HEAD:main` targets `main` whatever branch you are on. For a branch you created, the first push is `git push -u origin HEAD`. For a PR checked out with `gh pr checkout`, push to the remote and branch it configured (`git config branch.<branch>.remote` and `branch.<branch>.merge`), which for a fork PR is usually not `origin`. If that remote is a URL, there is no `<remote>/<branch>` ref: fetch the branch from the URL and use `FETCH_HEAD` wherever this skill says `<remote>/<branch>`. If `merge` is `refs/pull/...`, you cannot push to the head: keep the work local and report.
3. If the push is denied, or the destination is not the user's to write to, keep the commits local and report. Never fork, add a remote, or push elsewhere to get around it.
4. Verify with `git log -1 --stat`, `git status`, and the push output. `git ls-remote <remote> refs/heads/<branch>` should match `git rev-parse HEAD`.

At the end of the task, repeat Sync; if it changed the branch, rerun the checks and push again. Pushing the branch is where the task ends: open a PR only when asked.

## Rewriting published history

Amending or rebasing commits that are already pushed means the next push is a force-push. Never do this on a shared branch. Elsewhere:

1. Before rewriting, fetch and confirm your branch contains the remote tip (`git merge-base --is-ancestor <remote>/<branch> HEAD`); if it does not, Sync first. Save that tip's SHA (`git rev-parse <remote>/<branch>`).
2. Push with `--force-with-lease=<branch>:<saved-sha>`, never plain `--force`, and pass the SHA itself, not a ref name. The explicit SHA makes the push fail if anyone pushed after you looked; a bare lease or a ref name is defeated by any fetch in between.
3. If the push is rejected, or the remote tip moved before you pushed, fetch. Recover only if all of these hold: the new commits sit on top of the saved SHA (`git merge-base --is-ancestor <saved-sha> <new-sha>`), none is a merge (`git rev-list --merges <saved-sha>..<new-sha>` is empty), and all are your own, since anyone else's make the branch shared. Then run `git cherry-pick <saved-sha>..<new-sha>`, rerun the checks, and retry once with the lease on `<new-sha>`, which is now the saved SHA. Otherwise, or if the retry is rejected too, abort any pick in progress, keep your rewrite local, and report.

## Conflicts

Resolve a conflict only when the intent of both sides is clear. Otherwise abort your own rebase or cherry-pick and report.
