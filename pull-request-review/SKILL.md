---
name: pull-request-review
description: Review pull requests for correctness, regressions, security, tests, maintainability, and delivery risk. Use when reviewing another change, self-reviewing before opening a PR, or responding to review feedback.
compatibility: Requires access to the repository, pull request diff, and relevant test or CI results.
---

# Pull Request Review

Review for material risk, not for the appearance of activity.

## Establish Context

Read the PR description, linked requirements, repository guidance, changed files, relevant surrounding code, tests, configuration, and CI results. Understand the intended behavior before judging the implementation.

Separate self-review findings from formal review comments. For self-review, fix clear issues directly before opening or updating the PR when appropriate.

## Review in Risk Order

Assess the diff for:

1. correctness, behavior changes, and regressions;
2. security, privacy, authorization, validation, and secret exposure;
3. data/API compatibility, migrations, and failure handling;
4. test coverage for changed behavior, edge cases, and failures;
5. maintainability, clarity, and adherence to local conventions; and
6. observability, performance, reliability, and operational impact where relevant.

Confirm that generated files, lockfiles, configuration, documentation, and migrations are intentional and complete.

## Write Useful Findings

Report only concrete, actionable findings. Each finding should state the severity, affected location, failure scenario, and why it matters. Prioritize correctness and risk over style preferences. Do not invent concerns to fill a review.

If no material finding remains, summarize residual risks, validation gaps, or assumptions rather than claiming certainty. Never approve a merge on the user's behalf; merging always requires explicit user approval.
