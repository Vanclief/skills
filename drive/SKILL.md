---
name: drive
description: >-
  Claude Code only. Use when the user invokes /drive: plan with Astra, wait for
  the user's approval, build with Opus subagents, then review with Astra. When
  the user asks only to plan or only to review, run that phase alone.
disable-model-invocation: true
---

Run only as Fable in Claude Code. If a tool or model required for the requested phase is unavailable, report it and stop; do not substitute. A review-only request authorizes no repository edits.

Astra is gpt-6-astra. Load the orchestration guide and start each Astra worker with `--worktree current --agent codex --model gpt-6-astra --effort xhigh`. Give it the task, this protocol, and absolute paths to the skills that apply: brainstorm for planning, grug for design, pr-review for review. Astra reads code and writes proposals; it changes no repository files and starts no workers. Release each settled worker through orchestration.

Keep artifacts in `<scratchpad>/<task>/plan/` and `review/`: `context.md` with the user's request verbatim, verified constraints, and your own position, then `astra-round-N.md` and `claude-round-N.md`. Debate messages carry the path and a two-sentence summary. Before approval, only read, write the scratchpad, and create Orca state.

Plan until both of you accept the same proposal: scope, approach, assumptions, and acceptance checks. Counter with evidence and record why you concede. Reply `AGREED <path>` only to a proposal Astra has accepted; send amendments back first. Astra then writes `agreed.md` (recommendation, ranked reasons, main downside, what would change it, who conceded what) and `agreed-<name>.md` for any exact text, unfenced. Ask the user as soon as a question blocks progress, batching what you know; settle factual questions from the code and record assumptions.

Present the agreed plan and stop until the user approves. Debate material amendments with Astra; the user's explicit override wins. Approval covers building and fixing within the agreed behavior and constraints. Changes to either, or accepting a known defect, go back to the user.

Build with one fresh general-purpose Agent, `model: "opus"`, never a fork. Split work across subagents only for independent slices with disjoint write ownership and an agreed interface. Give each the approved plan, its scope, the skill paths that apply, and its checks. It edits only its scope, runs its checks, touches no Git state, and launches no agents. Inspect its diff and run the acceptance checks yourself. Git follows gitgud and the user's overrides. Opus also makes review fixes.

Review with a fresh Astra worker given the approved plan, the base ref, whether the head is `HEAD` or the working tree, and the check results. Include task uncommitted and new files; exclude unrelated edits. Freeze edits during each pass. Verify each finding: send confirmed ones to Opus, dispute the rest with evidence, and reuse the reviewer for the fixes and open findings. Finish when Astra reports no actionable findings, you have no evidenced objection, the checks pass, and no consequential question or material review gap remains. If later edits or Git sync change the reviewed result, revalidate before reporting.

Each debate gets four rounds, a round being Astra's reply plus yours; waiting on the user does not count. If a dispute repeats without new evidence or the cap hits, put the exact choice to the user and pause dependent work; never call it agreed to meet the cap. Report the reviewed state, checks and results, each disputed finding and how it ended, and what remains.
