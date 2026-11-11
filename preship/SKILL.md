---
name: preship
description: >-
  Use when the user explicitly invokes preship on a branch or PR that is
  already implemented, to make it ready to ship. Run two independent reviewers
  and fix what they find, round after round, until the change is clean, needs
  the user's judgement, or the fixes go back and forth; then rebase and tidy
  the history. Does not merge or deploy.
disable-model-invocation: true
---

The change is already written: the current branch, or the branch or PR the user names. Make it ready to ship; do not merge or deploy it. You own it from here to a reviewed, tidy branch. Subagents review and make the larger fixes; you decide what to ask, check what they return, and end the loop.

A subagent is a fresh context your harness can start with its own tool, such as Claude Code's Agent tool. Give each one the paths of the skills it must follow. If you cannot start one, say so and stop: a review of your own fixes is not independent.

## Mechanical or judgement

This line decides everything below. A question or finding is mechanical when the change's intent, the code, or the repository's conventions leave one right answer: a bug with a known correct behavior, a missing test, a broken check, a convention the surrounding code already follows. It needs the user's judgement when the valid answers differ in something the user would care about: what the change does or leaves out, a public interface, the data model, a new dependency, a trade-off with a real cost on each side, or accepting a known defect.

Settle mechanical questions yourself and record the assumption. Never pick for the user on a judgement question, and never ask about a mechanical one.

A finding about a comment, a doc page, the changelog, or the PR description is a text finding. It is a defect only when the statement is false, describes behaviour the code does not have, or leaves out a change a consumer must act on. If the statement is right and the code is wrong, it is a finding about the code. Fix a false statement with the smallest true one: correct the word, narrow the claim, or delete it. Every sentence you add is a claim no reviewer has read, so add one only for a change that was left out. Phrasing, reflow, ordering, and "could be clearer" are wording notes: log them and leave them for the documentation pass. Text never costs a review round.

A finding about code outside the change, or a defect the change neither created, made worse, nor exposed, is out of scope: report it and leave it. It becomes a judgement call only when the change cannot be correct without that work.

## Understand

Git follows gitgud: work on the change's own branch. Commit uncommitted work that clearly belongs to the change; ask about work that might not.

Establish the intent from what the user said, the PR description, and the commits, then read the diff against the base and the code around it. If you cannot tell what the change is meant to do, ask. Otherwise do not ask for approval; start.

Find the checks the repository runs and run them. For each failure, find out whether it also fails on the base; a temporary worktree of the base works. What fails there too is the baseline: report it and leave it, unless fixing it is part of the intent. The rest the change broke: those are mechanical findings, fixed and committed before any review. From here on, "the checks pass" means nothing fails that does not fail on the base, and that is what gitgud needs before a commit. Take the baseline again if a sync moves the base. A check that cannot run here is reported; it blocks only when nothing else verifies the change.

## Review loop

Each round:

1. Start two fresh reviewers on the head commit, in parallel where the harness allows, never forks and never a reviewer from an earlier round. Each follows the pr-review skill and the language's skill. Each reviews the whole diff: do not divide it between them by file or by topic. Each gets the intent, the user's decisions, the head SHA, the base, your check results with the baseline failures, which it relies on instead of rerunning the whole suite, and the rule that only a false statement counts in documentation. The base is `git merge-base <remote>/<base> HEAD`, taken each round because a sync can move it. Neither reviewer gets the other's findings, earlier rounds, or your opinion of the change. Edit nothing until both return.
2. If a reviewer failed, or skipped part of the diff that needs review (generated and vendored files do not), start one replacement for that part. A second failure is a blocker.
3. Check every finding and open question against the code. Each is confirmed (the defect, or the cost it names, is real), disproven with evidence a reader can check (a cited code path, or a throwaway test kept out of the repository), out of scope, settled by an answer the user already gave, or a judgement call. A finding you can neither confirm nor disprove is a judgement call, and so are two confirmed findings that want opposite things. A disproven finding that returns stays disproven unless it brings evidence your disproof does not answer.
4. Before fixing a confirmed finding that would undo an earlier fix, recheck the earlier finding. If it was wrong, undo its fix and log the reversal. If both hold, it is a judgement call. Never reverse the same code a second time: that is stuck.
5. Fix the confirmed mechanical findings that do not depend on an open judgement call. A fix is the smallest change that removes the defect; it does not widen what the change does. Make a fix of a few lines yourself. Give a larger one to an implementer subagent, using the harness's implementer agent type if it defines one, with the finding, the files in scope, the checks, the baseline failures, and the skills that apply (grug, the language's skill). It edits only its scope, leaves Git alone, starts no agents, and returns a judgement question unanswered. Its report is a claim: read the diff and run the checks yourself, and take out what it added beyond its finding unless the fix needs it. Fix what the change broke, and commit.
6. Log the round in a scratch file outside the repository, named for the branch: each finding, who raised it, your verdict, and what changed. Read the log before testing the endings; your memory of early rounds will not survive a long loop.

A change to behaviour means another round: code, tests, configuration, anything the checks or a user of the program could tell apart from before. A change to text alone does not: check each sentence you wrote against the code, note the evidence in the log, and rerun the checks. A Git sync counts only when it changes the diff against the base or needed a conflict resolved; a clean rebase needs just the checks rerun. After each round, test the endings in this order:

- **Needs judgement.** A finding or question is a judgement call. Stop and ask.
- **Stuck.** A fix would reverse the same code a second time, or the same finding or broken check is still there after two attempts to fix it. The number of rounds is not a reason to stop: a round that confirms new findings and fixes them is progress. The only limit is a backstop of twenty rounds, counted from the user's last answer.
- **Clean.** Both reviewers covered the whole diff, the round confirmed no finding whose fix changes behaviour, nothing is waiting on the user, and the checks pass. Go to the documentation pass, then Finish.

Otherwise run the next round. Do not call the change clean to end the loop. The only other stop is a blocker you cannot work around, such as a stop gitgud requires or a reviewer that fails twice: report it as blocked.

## Documentation pass

Once, after the clean round. Read the wording notes in the log and make the edits worth making to comments, docs, and the changelog in one commit, after the checks pass, and to the PR description. These edits are text, so they get no review round and no reviewers: check your own sentences against the code. A note that turns out to be a false statement is fixed here too. Skip the pass when the log holds no wording notes.

## Finish

Only after a clean round, tidy the history. Note the head SHA, then start one subagent that follows gitgud. It rebases the branch onto the latest base, which is origin's default branch (`git ls-remote --symref origin HEAD`, often staging or master) unless the branch was deliberately based elsewhere. It keeps only the commits that matter: one per logical change, with review fixes folded into the commit they fix. It does not push. If gitgud forbids rewriting this branch because others depend on its history, skip the tidy and say so.

Check its work as you would any subagent's: the diff against the new base must match the diff as it stood before the tidy, which is what the reviewers approved plus the text edits made since, and the checks must pass. If the rebase needed a conflict resolved or the diff changed, run another round and finish again. Otherwise push the rewritten branch as gitgud requires, with a lease on the SHA you noted, and report.

## Report

Open with the ending: `Clean after <n> rounds.`, `Needs your judgement.`, `Stuck after <n> rounds.`, or `Blocked.`, where `<n>` counts every round run. Then say what you changed, the checks run and their results, the checks that could not run, the findings fixed in each round, the findings you disproved with the evidence, the findings left as out of scope or already settled, the wording notes you applied and the ones you left, and the assumptions you made.

For a judgement stop, give the exact choice, what each option costs, your recommendation, and what is already done. For a stuck stop, give both positions and the rounds they came from, or what kept failing, and the state the code is in now. For a blocked stop, give the blocker, what is done, and what is not. When the user answers, apply the decision and resume where you stopped; the result still needs a clean round.
