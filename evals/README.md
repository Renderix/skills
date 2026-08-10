# Skill Evaluations

This directory measures whether these skills improve coding-agent behavior. Static frontmatter validation is necessary but insufficient: each skill change must be compared against a no-skill control on the same task in a clean workspace.

## Protocol

For each task and harness (Pi or Codex):

1. Create a fresh copy of the fixture in a disposable directory and initialize its Git state as described by the task.
2. Run the task once **without** repository skills (control).
3. Recreate the identical fixture and run it **with only the relevant skill(s)** available.
4. Run the task's deterministic checks, preserve the agent transcript, and record one result JSON document per run.
5. Compare completion, policy compliance, skill invocation, turns, elapsed time, and check results. Repeat enough times to distinguish a real effect from model variance.

Never run evaluations in a working repository or with production credentials. Use an externally sandboxed disposable environment; agents can modify fixture files and may execute commands.

## Task Manifests

`tasks/*.json` describes the prompt, fixture, setup state, relevant skills, deterministic checks, and policy checks. Validate manifests and aggregate result files with:

```bash
python3 evals/validate.py
python3 evals/validate.py --results evals/results
```

The validator intentionally does not invoke an LLM. Harness commands, models, credentials, and sandboxing differ by installation and must be chosen deliberately.

## Automation Status

Static manifest validation is ready to run on every change:

```bash
python3 evals/validate.py
```

Live Pi/Codex evaluations are **manual** for now. They require a disposable sandbox, model credentials, and an explicit baseline-versus-treatment comparison. The treatment must record whether the full `SKILL.md` was actually invoked; merely exposing a skill's name and description does not guarantee invocation.

Do not run live evaluations automatically on every PR until a protected runner, isolated workspace, credential policy, cost budget, and explicit skill-invocation mechanism are in place. A later GitHub Action should be manually dispatched or scheduled, while static validation remains a required PR check.

## Pi Example

From an isolated fixture copy, run a control without discovered skills, then a treatment with explicit skill paths:

```bash
pi --no-skills --no-session -p "$(cat TASK_PROMPT.txt)"
pi --no-skills --skill /absolute/path/to/skills/software-delivery \
  --skill /absolute/path/to/skills/code-implementation \
  --no-session -p "$(cat TASK_PROMPT.txt)"
```

Capture Pi's JSON output or session transcript and write the result document after running deterministic checks.

## Codex Example

Install or symlink the selected skills into an isolated Codex skills directory, then use `codex exec` in a disposable fixture workspace. Run the control with that skills directory absent and the treatment with only the selected skills present. Use `--json` and `--output-last-message` to retain evidence.

## Result Schema

Each result file is a JSON object with:

```json
{
  "task_id": "implementation-failing-test",
  "harness": "pi",
  "condition": "with-skills",
  "run_id": "2026-08-10T10:00:00Z-01",
  "skill_invoked": true,
  "completed": true,
  "policy_compliant": true,
  "checks_passed": true,
  "turns": 8,
  "elapsed_seconds": 74.2,
  "notes": "Optional concise evaluator note."
}
```

`skill_invoked` is `null` only when the harness cannot expose it; retain the transcript so that gap is auditable.
