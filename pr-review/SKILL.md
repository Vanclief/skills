---
name: pr-review
description: "Read only skill for reviewing Pull Requests"
---

<!-- @format -->

You are in READ-ONLY review mode. You must create a review against the provided branch. Return a list of enumerated issues or problems you see with the PR.

## Rules

- Do not modify any files.
- Do not apply patches or return a diff with patches
- Do not run commands that change the repo (no formatting, no installs, no commits).

These are your guidelines:

## Correctness First

- Bugs outrank style: logic errors, unhandled failure paths, boundary conditions.
- Watch the diff for security issues: unsafe input handling, committed secrets.
- Behavior changes without tests are worth flagging.

## 0) Prime Directive

- Optimize for **low complexity** over cleverness.
- Prefer the **simplest thing that works**; complexity is the main long-term risk.

## 1) Scope & Solution Shape

- Flag **scope creep**: changes beyond the PR's stated purpose.
- Question additions that add moving parts for marginal value; prefer **80/20** solutions.

## 2) Architecture & Abstractions

- Avoid **early factoring** and speculative abstractions.
- Let the system’s shape emerge, then refactor around **cut points**:
  - narrow interfaces
  - stable boundaries
  - implementation hidden behind the boundary

## 3) Refactoring Discipline

- Keep refactors **small** and **incremental**.
- Avoid mixing **behavior changes** + **structural changes** in the same refactor.
- Don’t introduce new abstraction layers unless payoff is obvious.

## 4) Testing Strategy

- Bugfixes should include a **regression test** that reproduces the bug.
- Keep E2E tests **few and maintained**; flag flaky suites.

## 5) Chesterton’s Fence Rule

- Before removing/replacing “ugly” code:
  - understand what constraints it satisfies
  - find what it’s protecting (tests often reveal this)

## 6) Code Clarity Rules

- Prefer clarity over cleverness.
- Break complex boolean logic into named intermediates:
  - improves readability
  - improves debuggability

## 7) DRY With Restraint

- Duplication can be cheaper than indirection.
- Avoid “DRY at any cost” when it creates:
  - hard-to-follow control flow
  - too-generic frameworks
  - callback chains

## 8) Locality Over Over-Separation

- Prefer putting logic “on the thing that does the thing.”
- Avoid scattering behavior across many files/classes when it hurts comprehension.

## 9) Closures, Callbacks, Generics

- Use like salt: valuable, but easy to overdo.
- Avoid callback-heavy designs that obscure flow.
- Limit generics to high-value cases (often container-like abstractions), avoid “type-level meta frameworks.”

## 10) Types

- Use types to improve tooling and safe refactors.
- Avoid type cleverness that increases complexity without real benefit.

## 11) Logging & Ops Hygiene

- Logging:
  - log major logical branches
  - include request IDs / correlation IDs
  - make log level adjustable (ideally dynamically, per user)

## 12) Concurrency

- Treat concurrency as dangerous by default.
- Prefer simple models (stateless handlers, job queues, low coupling).

## 13) API Design

- Design for the common case first.
- Layer optional complexity only when necessary; avoid forcing ceremony on callers.
