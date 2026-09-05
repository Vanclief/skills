---
name: grug
description: >-
  Maintenance-first coding guidance focused on reducing complexity and
  delivering the smallest practical solution. Use always when coding: writing,
  adding, refactoring, fixing, reviewing, or designing code, and choosing
  libraries or dependencies. Also use whenever the user says "simplest
  solution", "minimal solution", "yagni", "do less", or "shortest path", or
  complains about over-engineering, bloat, boilerplate, or unnecessary
  dependencies.
---

Solve the real problem with the least complexity that preserves correctness and required behavior. Optimize for the next engineer who must read, debug, and change it; fewer lines are not automatically simpler.

Before building

- Read the task and affected code; trace the relevant flow and callers. Identify required behavior and the assumptions it depends on. State consequential uncertainty briefly.
- Do not design for hypothetical future requirements. Say no to features, abstractions, layers, patterns, frameworks, services, and configuration the task does not need.

Before writing new code, check in order and stop at the first rung that meets the required behavior:

1. Does this need to exist at all?
2. Already in this codebase? Search before you write; reuse it when the semantics fit.
3. Standard library or native platform feature?
4. Already-installed dependency?
5. Only then write the minimum clear code.

- Do not add a dependency when a few clear lines solve the problem correctly. Do not hand-roll difficult correctness (e.g. cryptography or time zones) to avoid one.
- Start concrete and local. Introduce abstractions, configuration, services, or concurrency only for a present requirement the simpler design cannot meet. Preserve the application's execution model; default to one process when choosing a new architecture.

Keep code understandable

- Before adding a special case, check whether a simpler data representation removes it. Use simple types and structures to express valid states; avoid combinations of flags that admit impossible states. Do not replace a few clear branches with a dispatch framework.
- Keep control flow explicit; do not hide important behavior behind dense expressions, magic, or indirect machinery. Use guard clauses to reduce nesting and names that explain intermediate results. Split tangled responsibilities at coherent boundaries; do not fragment a clear linear function merely to shorten it. Follow the codebase's vocabulary for the same concepts.
- Avoid boolean parameters that select different operations. Prefer clearly named operations or an explicit mode when modes are part of the domain; boolean facts are fine.
- Keep mutation local with a clear owner. Pass needed values rather than shared mutable bags; do not store values that can be cheaply derived unless there is a concrete reason.
- Keep a rule that must change consistently in one place. Accept small duplication for independent behavior rather than joining unrelated cases behind flags or a generic helper.
- Handle errors where recovery is possible; otherwise propagate them with useful context. Do not silently turn failure into success or an empty result. Keep cleanup and partial-failure behavior explicit; log at the boundary that handles the failure without logging it at every layer.
- Use database constraints and transactions for invariants that must survive concurrent writers. Keep changeable application policy in application code; do not rely on a precheck for integrity.
- Mark a deliberate simplification with a `grug:` comment only when it has a known limit: name that limit and what would justify changing the approach.

Change and verify

- Make small changes that keep required behavior working. Understand why existing complexity exists before removing it; keep unrelated cleanup out of the task.
- For a bug, trace the cause and affected callers; fix the violated invariant where it belongs. Capture the failure in a regression test when practical.
- Run checks that exercise changed behavior and relevant failure paths. Changed non-trivial logic must have tests that would catch a regression; add or update coverage when existing tests would miss it. Test observable behavior, not mocked implementation details. Do not add tests merely for trivial edits.
- Optimize performance only after measurement or concrete operational evidence identifies a bottleneck.

Before calling it done

Inspect the actual diff against the task, including what you just built:

1. Does each addition serve a required behavior? Challenge weak assumptions, unnecessary layers, special cases, and hidden state.
2. What can be deleted while preserving required behavior? After deleting, simplify what remains, including now-unused support code.
3. Can a reader follow the normal path, state changes, and failures without reconstructing scattered logic? Fix concrete problems within scope, then rerun the relevant checks after changes.

For unnecessary work, prefer **delete > simplify > optimize > automate**. These are preferences, not mandatory stages; optimize or automate only when the task warrants it. Review can produce no edits: if the code meets the need clearly and robustly, leave it alone. Stop when there is no concrete remaining defect or unnecessary complexity in the change.
