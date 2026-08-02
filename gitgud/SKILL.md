---
name: gitgud
description: >-
  Use ALWAYS before running any git commit, git push, amend, merge, or
  force-push — no exceptions. Blocks commits and pushes to protected branches
  (production, staging, master, main) and enforces commit best practices.
---

# Gitgud

Always run this checklist before committing or pushing.

## Guard — protected branches

- Check the current branch first: `git branch --show-current`.
- If it is `production`, `staging`, `master`, or `main`, REFUSE to commit or push. Tell the user to create a branch instead (e.g. `git checkout -b <feature-branch>`).
- Never push directly to these branches under any circumstances.

## Best practices

1. Review what you're committing: `git status` and `git diff` — stage only related changes, never `git add -A` blindly.
2. One logical change per commit; split unrelated changes.
3. Message: imperative mood, concise subject (≤50 chars), no trailing period. Add a body only if the "why" isn't obvious.
4. Never commit secrets, credentials, or generated/temp files.
5. Don't amend or force-push published commits.
6. Keep history linear: rebase on top of the target branch instead of merging into your branch (`git pull --rebase`, never merge commits).
