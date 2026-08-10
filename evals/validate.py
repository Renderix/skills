#!/usr/bin/env python3
"""Validate skill-evaluation manifests and aggregate recorded results."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TASK_REQUIRED = {"id", "prompt", "skills", "fixture", "setup", "checks", "policy_checks"}
RESULT_REQUIRED = {
    "task_id", "harness", "condition", "run_id", "skill_invoked", "completed",
    "policy_compliant", "checks_passed", "turns", "elapsed_seconds",
}


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def validate_tasks() -> set[str]:
    task_ids: set[str] = set()
    for path in sorted((ROOT / "tasks").glob("*.json")):
        data = load_json(path)
        missing = TASK_REQUIRED - data.keys()
        if missing:
            raise ValueError(f"{path}: missing {sorted(missing)}")
        if data["id"] in task_ids:
            raise ValueError(f"{path}: duplicate id {data['id']}")
        if not isinstance(data["skills"], list) or not data["skills"]:
            raise ValueError(f"{path}: skills must be a non-empty list")
        if not isinstance(data["setup"], list):
            raise ValueError(f"{path}: setup must be a list")
        if not isinstance(data["checks"], list) or not data["checks"]:
            raise ValueError(f"{path}: checks must be a non-empty list")
        if not isinstance(data["policy_checks"], list):
            raise ValueError(f"{path}: policy_checks must be a list")
        if not (ROOT / data["fixture"]).is_dir():
            raise ValueError(f"{path}: fixture does not exist")
        task_ids.add(data["id"])
    if not task_ids:
        raise ValueError("no task manifests found")
    return task_ids


def validate_results(directory: Path, task_ids: set[str]) -> None:
    results: list[dict] = []
    for path in sorted(directory.glob("*.json")):
        data = load_json(path)
        missing = RESULT_REQUIRED - data.keys()
        if missing:
            raise ValueError(f"{path}: missing {sorted(missing)}")
        if data["task_id"] not in task_ids:
            raise ValueError(f"{path}: unknown task_id {data['task_id']}")
        if data["condition"] not in {"control", "with-skills"}:
            raise ValueError(f"{path}: condition must be control or with-skills")
        if not isinstance(data["turns"], int) or data["turns"] < 0:
            raise ValueError(f"{path}: turns must be a non-negative integer")
        if not isinstance(data["elapsed_seconds"], (int, float)) or data["elapsed_seconds"] < 0:
            raise ValueError(f"{path}: elapsed_seconds must be non-negative")
        results.append(data)

    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for result in results:
        grouped[(result["task_id"], result["condition"])].append(result)
    print(f"Validated {len(results)} result(s).")
    for (task_id, condition), runs in sorted(grouped.items()):
        rate = lambda key: sum(run[key] is True for run in runs) / len(runs)
        print(
            f"{task_id} [{condition}]: runs={len(runs)}, "
            f"completed={rate('completed'):.0%}, policy={rate('policy_compliant'):.0%}, "
            f"checks={rate('checks_passed'):.0%}, "
            f"avg_turns={sum(run['turns'] for run in runs) / len(runs):.1f}, "
            f"avg_seconds={sum(run['elapsed_seconds'] for run in runs) / len(runs):.1f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, help="Directory of result JSON files")
    args = parser.parse_args()
    task_ids = validate_tasks()
    print(f"Validated {len(task_ids)} task manifest(s).")
    if args.results:
        validate_results(args.results, task_ids)


if __name__ == "__main__":
    main()
