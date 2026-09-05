---
name: brainstorm
description: >-
  Use when the user asks to explore ideas or compare approaches for a coding
  problem or design. Thinking and proposing only; do not use when the user
  asks to build, fix, refactor, or edit.
---

Deliver a recommendation the user can act on; do not start building. A later request to build is just that and needs no special wording.

Read the relevant code and constraints before proposing anything. Do not change files or run state-changing commands, except to save notes or proposals the user asks for, where they ask for them.

Check first whether doing nothing, deleting, or reusing what exists meets the need. Consider distinct alternatives before choosing; present only real contenders, without padding or a cap. Explain material tradeoffs, risks, and assumptions. Challenge weak ideas, including the user's.

Recommend one direction and rank the reasons. State its main downside and what evidence or requirement would change your recommendation. Ask only for missing information needed to choose; otherwise state the assumption and proceed. If the user asks to explore without choosing, honor that.

For example: "Keep the existing query: it meets the latency target and avoids cache invalidation. Each request still reads the database. Reconsider caching if measurements show that read is the bottleneck."
