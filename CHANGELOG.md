# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-10-23

### Added

- `issue-specification` skill — turns a rough issue into a workable specification with acceptance criteria, scope, and risks before implementation starts.
- `software-delivery` skill — guides repository-aware delivery work from discovery through implementation, validation, commits, pull requests, and review.
- `code-implementation` skill — implements minimal, maintainable, compatible production-code changes.
- `code-quality-evaluation` skill — evaluates implementation quality before test and delivery gates.
- `test-engineering` skill — designs and runs proportional automated validation, including edge cases and failures.
- `git-delivery` skill — safely branches, commits, pushes, and prepares pull requests.
- `pull-request-review` skill — reviews correctness, security, tests, maintainability, and delivery risk.
- `planner` agent — squad leader: specs issues, then routes work to members by @-mention; never edits code.
- `backend-engineer` agent — implements backend issues one branch at a time, tests, PRs; never merges.
- `reviewer` agent — two-axis review (spec fidelity + standards) with cited severity-labeled findings; never merges.
