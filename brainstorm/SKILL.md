---
name: brainstorm
description: >-
  Use when the user wants to explore ideas, weigh approaches, or think through
  a design or problem during a coding session. Thinking and proposing only —
  never edit, create, or modify files.
---

# Brainstorm

When the user wants to brainstorm, your job is to generate and pressure-test ideas with them, not to start building. Stay in exploration mode until they explicitly ask you to implement.

## When to Use

Use this skill when the user asks you to:

- Explore options, approaches, or designs ("how could we...", "what are some ways to...")
- Weigh tradeoffs between alternatives
- Think through a problem, architecture, or naming decision before committing
- Sketch a plan without writing the code yet

Do NOT use this skill when the user has asked you to fix, refactor, implement, or edit code.

## Rules

- Read and inspect freely: open files, grep, trace call paths to ground ideas in the actual codebase.
- Do NOT edit, create, delete, or move any files — including scratch files, notes, or "just a quick draft."
- Do NOT run state-changing commands (installs, migrations, formatters, git writes). Read-only inspection is fine.
- Favor breadth before depth: offer several distinct options rather than locking onto the first one.
- Surface tradeoffs, risks, and assumptions, not just upsides. Disagree when an idea is weak.
- Don't converge prematurely. Keep thinking until the user signals they're ready to pick a direction.

## Output

- Present multiple distinct options when the space allows; name each one briefly.
- For each, give the core idea, the main tradeoff, and when you'd reach for it.
- End by laying out the open questions or the decision that would unblock progress — not by writing the code.
- Move to implementation only after the user explicitly asks.
