# Skills Overview

Lifecycle map: `intake → todo → specs → in-progress → in-review → verify → merge → release`.

## issue-specification

Turns a rough issue into a workable specification with acceptance criteria, scope, and risks before implementation starts.

## software-delivery

Guides repository-aware delivery work from discovery through implementation, validation, commits, pull requests, and review.

## code-implementation

Implements minimal, maintainable, compatible production-code changes.

## code-quality-evaluation

Evaluates implementation quality before test and delivery gates.

## test-engineering

Designs and runs proportional automated validation, including edge cases and failures.

## git-delivery

Safely branches, commits, pushes, and prepares pull requests.

## pull-request-review

Reviews correctness, security, tests, maintainability, and delivery risk.

## Agent definitions

- `planner` — squad leader: specs issues, then routes work to members by @-mention; never edits code.
- `backend-engineer` — implements backend issues one branch at a time, tests, PRs; never merges.
- `reviewer` — two-axis review (spec fidelity + standards) with cited severity-labeled findings; never merges.
