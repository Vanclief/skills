---
name: gitgud
description: >-
  Use ALWAYS before starting repository changes and any commit, push, amend, merge,
  rebase, cherry-pick, or force-push. Commit and push task branches while working;
  guard protected branches.
---

1. Run `git status` and `git branch --show-current`; stop for operations you did not start. Never commit to, push to, or rewrite `main`, `master`, `production`, or `staging`. The same ban covers repository-protected branches.
2. Each feature or fix needs a dedicated, unprotected branch. Reuse a branch only for the same unmerged scope it was created for; when in doubt, create a new one and report. Fetch before branching from the repository's designated base, otherwise origin's default (`git ls-remote --symref origin HEAD`); stack only when requested. Use `git switch --no-track -c <name> <remote>/<base>`. Follow repository naming; otherwise `<type>/<short-kebab-summary>` (feat, fix, chore, refactor, docs), include any supplied ticket ID. Evidence others use or depend on its history stops automatic rewriting.
3. Before editing, fetch `origin` and relevant remotes. Fast-forward if only behind; if diverged, rebase onto the remote tip. Unpublished branches sync their base. For open PRs (`gh pr view`), fetch/rebase the actual base when behind. Report lookup failures; continue branch sync alone. Preserve dirty work; blocked branch sync stops edits.
4. Review `git diff` and `git diff --cached`; stage named task changes, never `git add -A` or `git add .`. Preserve unrelated work; exclude secrets and accidental artifacts. Follow repository conventions. Never bypass hooks through `--no-verify`, configuration, or environment; review and selectively re-stage hook edits.
5. Commit and push each logical change after required checks pass, without asking. No automatic WIP. Set upstream on first push (`-u`). Before each push and at task end, repeat rule 3 and check the integrated result.
6. Resolve conflicts only with clear intent; otherwise abort your rebase or cherry-pick and report. Never choose ours/theirs blindly or leave operations unfinished. Never merge to resolve divergence; authorized PR merges remain allowed.
7. Check the remote, destination, and outgoing commits: `git push origin HEAD:main` targets main. Save the integrated remote SHA before rewriting; use `--force-with-lease=<branch>:<saved-sha>`, never plain force. After rejection, fetch and reassess sharing. If review confirms a linear advance from the saved SHA, use `git cherry-pick <saved-sha>..<new-sha>`. Recheck, save the integrated new tip, and retry once; otherwise report.
8. Verify `git log -1 --stat`, `git status`, and push results.
