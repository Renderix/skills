---
name: software-delivery
description: Deliver code changes safely and autonomously across an existing repository: discover conventions, assess risk, implement, test, commit, push, open or review pull requests, and report results. Use for features, bug fixes, refactors, tests, commits, pushes, pull requests, and code reviews.
compatibility: Requires Git access and the target repository's normal build and test tooling.
---

# Software Delivery

Deliver the requested objective while preserving the target repository's conventions and the user's control over high-impact decisions.

## 1. Discover Before Changing

1. Read applicable repository instructions and constraints first, including `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, and relevant build, test, lint, type-check, CI, and Git configuration.
2. Inspect the affected code, tests, documentation, and recent Git history before proposing a solution.
3. Follow established repository conventions. They override this skill except where they conflict with safety requirements or explicit user instructions.
4. If unknown uncommitted work exists, preserve it, ask the user how to proceed, and only then continue. Never discard, stash, or silently absorb it.

## 2. Decide Whether to Proceed

Proceed autonomously for low-risk, reversible, well-specified work.

State a concise plan and proceed for medium-sized changes. Request approval before acting when requirements or product behavior are ambiguous, or for cross-cutting architecture, migrations, public API or behavior changes, significant uncertainty, new dependencies, or major dependency upgrades.

Never expose secrets, tokens, keys, credentials, or private data in source, logs, commits, or pull requests. Request explicit approval for destructive or high-blast-radius operations, including deletion, data migrations, force pushes, history rewrites, production actions, or unclear commands.

## 3. Branch and Git Policy

- If the user specifies a base branch, create the working branch from it. Otherwise, fetch and use the latest default branch.
- Create and work on a descriptive non-default branch, such as `feat/token-refresh`, `fix/null-session`, or `chore/update-ci`.
- Never work, commit, or push directly to the default branch.
- Commit and push autonomously on a non-default branch. Follow repository commit conventions; if none exist, use an imperative Conventional Commit, for example `feat: add token refresh`.
- Agents may create and update pull requests autonomously. A PR must summarize the change, validation, and remaining risks.
- Never merge a pull request without the user's explicit approval.

## 4. Implement Clearly

Make the smallest clear change that completes the objective. Treat KISS, DRY, and clean/onion architecture as heuristics, not mandates: preserve established architecture and add abstractions or layers only to solve a demonstrated boundary or dependency problem.

Avoid unrelated cleanup. Explain material assumptions and preserve compatibility unless a breaking change is explicitly intended.

## 5. Validate Thoroughly

A change is done only when:

- the requested feature or objective is complete;
- the relevant build has run successfully;
- automated tests for changed behavior have been written and run, when reasonably feasible; and
- meaningful edge cases have been identified through brief risk-based analysis and tested proportionally.

Use the repository's normal lint, format, type-check, build, and test commands where applicable. If relevant automated coverage does not exist, add it unless automation is genuinely impractical; in that case, document a concrete manual validation procedure.

If a required build or check fails for an apparent pre-existing reason, capture the exact command and result, establish that it is unrelated where possible, and report validation as blocked rather than passed. Fix it only when it is in scope or authorized.

## 6. Review Pull Requests

Use a risk-based rubric for both self-review before opening a PR and review of others' PRs:

- correctness and regressions;
- security, privacy, and secret exposure;
- tests and failure/edge-case coverage;
- maintainability and adherence to local conventions;
- API, data, and backward compatibility; and
- observability and operational impact where relevant.

Separate self-review findings from formal PR review comments. Prioritize concrete, actionable findings; do not invent issues merely to produce feedback.

## 7. Report Completion

Report concisely:

- what changed;
- validation commands and results;
- meaningful edge cases considered;
- the branch, commit, and PR created or updated, if applicable; and
- assumptions, blocked checks, and remaining risks.
