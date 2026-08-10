---
name: code-implementation
description: Implement features, bug fixes, and refactors in an existing codebase with minimal, maintainable, compatible changes. Use when writing or modifying production code after requirements and repository conventions are understood.
compatibility: Requires access to the target repository and its normal development tooling.
---

# Code Implementation

Implement the smallest clear change that fulfills the requested objective.

## Discover the Local Design

Before editing, read repository guidance and inspect the affected code, callers, tests, types, configuration, and nearby patterns. Let the existing codebase establish naming, error handling, dependency direction, API, and formatting conventions.

Identify the observable behavior to preserve or change, the relevant inputs and failure modes, and compatibility-sensitive callers, data, and interfaces.

## Choose the Right Scope

- Prefer a direct change over a new abstraction.
- Apply KISS and DRY as heuristics, not rituals. Remove duplication only when the shared concept is stable and meaningful.
- Preserve existing architecture. Add clean/onion boundaries only when they solve a real dependency or testability problem.
- Avoid unrelated refactors, formatting churn, and speculative extensibility.
- Preserve backward compatibility unless the user explicitly authorizes a breaking change.

Proceed for well-specified, low-risk, reversible work. State a concise plan before medium-sized changes. Ask before acting on ambiguous behavior, public API changes, cross-cutting architectural changes, migrations, new dependencies, major upgrades, or significant uncertainty.

## Implement Defensively

Make data flow, invariants, errors, and ownership clear. Validate inputs at appropriate boundaries, handle expected failures intentionally, and avoid silently swallowing errors. Do not introduce secrets, credentials, unsafe logging, or hidden external side effects.

Keep changes narrowly scoped and readable. Update documentation or configuration when behavior, setup, operations, or public interfaces change.

## Before Hand-off

Review the diff as a maintainer: verify the objective is met, compatibility is preserved, error paths make sense, and no accidental files or unrelated changes are included. Then use the repository's build, test, and quality checks as required by `software-delivery`.
