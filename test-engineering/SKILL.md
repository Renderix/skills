---
name: test-engineering
description: Design, add, run, and assess automated tests for code changes, including edge cases and failures. Use when creating or updating tests, diagnosing test coverage, or validating a feature, fix, or refactor.
compatibility: Requires access to the target repository and its normal test tooling.
---

# Test Engineering

Build confidence in observable behavior, not implementation trivia.

## Discover the Test System

Read repository guidance and inspect existing test layout, framework, fixtures, helpers, naming, test commands, and CI configuration. Extend the local testing style rather than introducing a new framework or pattern without approval.

Identify the changed contract: successful behavior, invalid input, boundary conditions, error behavior, state transitions, integrations, and compatibility-sensitive cases.

## Design Proportional Coverage

For every change, briefly assess risk and select meaningful cases:

- normal and representative paths;
- boundaries, empty or missing values, and malformed input where relevant;
- expected failures and error propagation;
- state, concurrency, authorization, persistence, network, and external-side-effect behavior when applicable; and
- regressions implied by the bug or changed contract.

Favor a small set of independent, intention-revealing tests over exhaustive or brittle implementation-coupled tests. Test externally observable behavior. Use unit, integration, and end-to-end levels according to the risk and the repository's established practice.

## Add and Run Tests

Add or update automated tests for changed behavior whenever reasonably feasible. Do not call work complete solely because old tests pass. Run focused tests while iterating, then the relevant broader suite and required build, lint, format, or type checks.

If no suitable automated test exists, add one unless automation is genuinely impractical. In that case, document exact manual validation steps, inputs, expected results, and any remaining gap.

## Treat Failures Honestly

Investigate failures rather than weakening assertions or deleting tests to obtain green output. If a required check appears pre-existing or unrelated, record the exact command and result, establish separation where possible, and report validation as blocked—not passed. Fix unrelated failures only when authorized or in scope.
