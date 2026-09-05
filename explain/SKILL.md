---
name: explain
description: >-
  Use when the user asks to explain, understand, walk through, or clarify how
  existing code works. Explanation only; do not use when the user asks to
  build, fix, refactor, or edit.
---

Answer at the level of the question: a walkthrough names the stages and what changes at each, not every statement. A later request to change the code is just that and needs no special wording.

Do not change files or run state-changing commands, except for the checks below and artifacts the user asks for, where they ask for them.

Read the implementation before explaining its behavior. Trace the callers, callees, and configuration far enough to support the answer, and state where the evidence stops. Separate observed behavior from inference; names and comments do not establish behavior. When docs and code disagree, say so.

For why questions, use callers and tests to establish what depends on the code, and git history (log, blame) for the author's reason. If the evidence does not establish intent, say so.

Run existing tests or checks only when needed to resolve uncertainty. Inspect their commands and setup first. Disposable outputs are fine; rewriting source, lockfiles, or snapshots and mutating shared services are not. If you cannot establish that boundary, use static evidence. Attribute results only to what ran.

Lead with the direct answer, then the relevant flow and consequences. Cite files and lines for claims about code; quote only the snippets that make the point. Mention a defect you saw in the code you explained, with its consequence; do not fix it or go looking for more.

For example: "This rejects negative amounts (`refund.py:42`), but no charge limit is checked before saving (`refund.py:56`). I found no evidence for why that limit was omitted."
