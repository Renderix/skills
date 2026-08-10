---
name: code-quality-evaluation
description: Evaluate whether an implemented code change meets an engineering quality bar before delivery. Use after implementation to assess correctness, clarity, design, maintainability, reliability, security, and readiness for testing.
compatibility: Requires access to the target repository, the changed code, and relevant requirements or acceptance criteria.
---

# Code Quality Evaluation

Evaluate the implementation itself before treating tests, commits, or pull-request review as the final gate. This is not a PR review: assess whether the code fulfills its objective and is worth delivering; then hand off delivery-risk analysis to `pull-request-review`.

## Establish the Intended Outcome

Read the request, acceptance criteria, repository guidance, affected code, and relevant callers. Identify the observable behavior, constraints, invariants, compatibility expectations, and failure modes the change must satisfy.

Do not score code against abstract preferences while ignoring established repository conventions. Local conventions take precedence unless they conflict with safety requirements or explicit user instructions.

## Evaluate the Rubric

Assess the change proportionally against these dimensions:

1. **Correctness** — Does it fulfill the requested behavior, preserve required behavior, and handle expected errors intentionally?
2. **Scope** — Is it the smallest clear change, without unrelated cleanup or speculative features?
3. **Clarity** — Are control flow, names, data flow, invariants, and ownership understandable to a maintainer?
4. **Design** — Does it use KISS and DRY pragmatically, preserve local architecture, and introduce abstractions only for a demonstrated need?
5. **Maintainability** — Is duplication meaningful, is coupling controlled, and can a future change be made safely?
6. **Reliability and compatibility** — Are boundaries, invalid inputs, state transitions, failures, and public/data/API compatibility addressed where relevant?
7. **Security and privacy** — Does it validate at appropriate boundaries and avoid secret exposure, unsafe logging, authorization gaps, or unnecessary side effects?
8. **Operability** — Are configuration, documentation, errors, logging, metrics, and migrations adequate for the change's operational impact?

## Act on Findings

Fix clear, in-scope quality defects before proceeding. For material design trade-offs, ambiguous requirements, public API changes, migrations, cross-cutting architecture, new dependencies, or major upgrades, explain the issue and ask for direction.

Do not manufacture concerns to satisfy every rubric category. Mark non-applicable dimensions as such and state residual risks plainly.

## Hand-off

Summarize the evaluation: what meets the bar, material issues fixed or deferred, non-applicable dimensions, assumptions, and remaining risks. Then add and run proportional tests with `test-engineering`; use `pull-request-review` for the separate review of the completed diff.
