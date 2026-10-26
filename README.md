# skills

Personal, stack-agnostic coding and software-delivery skills for AI coding agents.

## Skills

- [`issue-specification`](issue-specification/SKILL.md) — turns a rough issue into a workable specification with acceptance criteria, scope, and risks before implementation starts.

## Agents

Agent definitions (instructions and boundaries) for the SDLC squad, kept reviewed in this repo. Skills have source-linked refresh in Multica; agents do not — applying a change here means re-running the workspace update by hand, and this directory is the drift reference.

- [`agents/planner.md`](agents/planner.md) — squad leader: specs issues, then routes work to members by @-mention; never edits code.
- [`agents/backend-engineer.md`](agents/backend-engineer.md) — implements backend issues one branch at a time, tests, PRs; never merges.
- [`agents/reviewer.md`](agents/reviewer.md) — two-axis review (spec fidelity + standards) with cited severity-labeled findings; never merges.
- [`software-delivery`](software-delivery/SKILL.md) — guides repository-aware delivery work from discovery through implementation, validation, commits, pull requests, and review.
- [`code-implementation`](code-implementation/SKILL.md) — implements minimal, maintainable, compatible production-code changes.
- [`code-quality-evaluation`](code-quality-evaluation/SKILL.md) — evaluates implementation quality before test and delivery gates.
- [`test-engineering`](test-engineering/SKILL.md) — designs and runs proportional automated validation, including edge cases and failures.
- [`git-delivery`](git-delivery/SKILL.md) — safely branches, commits, pushes, and prepares pull requests.
- [`pull-request-review`](pull-request-review/SKILL.md) — reviews correctness, security, tests, maintainability, and delivery risk.
- [`web-testing`](web-testing/SKILL.md) — captures screenshot and video evidence from web builds via Playwright; the default evidence platform.
- [`android-testing`](android-testing/SKILL.md) — captures emulator-based Android evidence (screenshots, video, hardware back) via adb.
- [`ios-testing`](ios-testing/SKILL.md) — captures simulator-based iOS evidence via xcrun simctl.

## Compatibility

Skills follow the [Agent Skills](https://agentskills.io/) `SKILL.md` format and are intended for Pi and Codex.

This is a curated personal repository. External contributions are not accepted at this time.

## Evaluation

[`evals/`](evals/README.md) contains reproducible task manifests and fixtures for comparing coding-agent behavior with and without skills. Static validation is local and repeatable; live Pi/Codex evaluations are currently manual and require isolated workspaces and credentials.

## License

[MIT](LICENSE)
