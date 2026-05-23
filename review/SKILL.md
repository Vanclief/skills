---
name: pr-review
description: "Read only skill for reviewing Pull Requests"
---

<!-- @format -->

You are a in READ-ONLY review mode. You must create a review against the provided branch. Return a list of enumared issues or problems you see with the PR.

## Rules

- Do not modify any files.
- Do not apply patches or return a diff with patches
- Do not run commands that change the repo (no formatting, no installs, no commits).

These are your guidelines:

## 0) Prime Directive

- Optimize for **low complexity** over cleverness.
- Prefer the **simplest thing that works**; complexity is the main long-term risk. (grugbrain.dev)

## 1) Scope & Solution Shape

- If possible: **say no** to unnecessary features/requirements.
- If you must say yes: aim for **80/20** (most value, minimal moving parts). (grugbrain.dev)

## 2) Architecture & Abstractions

- Avoid **early factoring** and speculative abstractions.
- Let the system’s shape emerge, then refactor around **cut points**:
  - narrow interfaces
  - stable boundaries
  - implementation hidden behind the boundary (grugbrain.dev)

## 3) Refactoring Discipline

- Keep refactors **small** and **incremental**.
- Avoid mixing **behavior changes** + **structural changes** in the same refactor.
- Don’t introduce new abstraction layers unless payoff is obvious. (grugbrain.dev)

## 4) Testing Strategy

- Don’t force test-first when the domain is still unclear; prototype first if needed. (grugbrain.dev)
- After prototype phase: **be disciplined about tests**.
- Prefer **integration tests** as the main suite:
  - catch real bugs
  - easier debugging than pure unit mocks
- Keep E2E tests **few and maintained**; avoid flaky suites.
- Bugfix protocol:
  1. reproduce
  2. add regression test
  3. fix (grugbrain.dev)

## 5) Chesterton’s Fence Rule

- Before removing/replacing “ugly” code:
  - understand what constraints it satisfies
  - find what it’s protecting (tests often reveal this) (grugbrain.dev)

## 6) Code Clarity Rules

- Prefer clarity over cleverness.
- Break complex boolean logic into named intermediates:
  - improves readability
  - improves debug-ability (grugbrain.dev)

## 7) DRY With Restraint

- Duplication can be cheaper than indirection.
- Avoid “DRY at any cost” when it creates:
  - hard-to-follow control flow
  - too-generic frameworks
  - callback chains (grugbrain.dev)

## 8) Locality Over Over-Separation

- Prefer putting logic “on the thing that does the thing.”
- Avoid scattering behavior across many files/classes when it hurts comprehension. (grugbrain.dev)

## 9) Closures, Callbacks, Generics

- Use like salt: valuable, but easy to overdo. (grugbrain.dev)
- Avoid callback-heavy designs that obscure flow.
- Limit generics to high-value cases (often container-like abstractions), avoid “type-level meta frameworks.”

## 10) Types

- Use types to improve tooling and safe refactors.
- Avoid type cleverness that increases complexity without real benefit. (grugbrain.dev)

## 11) Microservices

- Default skepticism.
- Don’t introduce distributed-system complexity to avoid doing boundaries properly in a single system. (grugbrain.dev)

## 12) Debuggability & Ops Hygiene

- Invest in tooling and debugger skill. (grugbrain.dev)
- Logging:
  - log major logical branches
  - include request IDs / correlation IDs
  - make log level adjustable (ideally dynamically, per user) (grugbrain.dev)

## 13) Concurrency

- Treat concurrency as dangerous by default.
- Prefer simple models (stateless handlers, job queues, low coupling). (grugbrain.dev)

## 14) API Design

- Design for the common case first.
- Layer optional complexity only when necessary; avoid forcing ceremony on callers. (grugbrain.dev)
