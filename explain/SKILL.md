---
name: explain
description: >-
  Use when the user asks to explain, understand, walk through, or clarify how
  code works during a coding session. Explanation only — never edit, create,
  or modify files.
---

# Explain

When the user asks you to explain something about the codebase, your job is to help them understand it, not to change it.

## When to Use

Use this skill when the user asks you to:

- Explain, describe, or summarize how some code works
- Walk through a function, file, data flow, or architecture
- Answer a "what does this do / why is this here / how does X work" question

Do NOT use this skill when the user has asked you to fix, refactor, implement, or edit code.

## Rules

- Read and inspect freely: open files, grep, trace call paths.
- Do NOT edit, create, delete, or move any files.
- Do NOT run state-changing commands (installs, migrations, formatters, git writes). Read-only inspection is fine.
- If your explanation naturally points to a change, describe what you'd change and why, then stop and ask before touching anything.

## Output

- Lead with a 1–2 sentence answer to the question.
- Then give detail: cite the relevant files and line ranges, quoting only the small snippets needed to make the point.
- Make the change only after the user explicitly asks you to.
