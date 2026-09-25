#!/usr/bin/env python3
"""Extract preregistered raw metrics without producing an S2 score."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


WORKER_B = "codex-worker-b"


def classify_contract_key(patch_text: str) -> str:
    has_code = '"code"' in patch_text or "'code'" in patch_text
    has_status = '"status"' in patch_text or "'status'" in patch_text
    if has_code and not has_status:
        return "code"
    if has_status and not has_code:
        return "status"
    return "other"


def extract(summary: dict[str, Any], worker_b_patch: str) -> dict[str, Any]:
    arm = summary.get("arm")
    bases = summary.get("worker_start_base_commits") or {}
    baseline = summary.get("baseline_commit")
    schedule = summary.get("coordinator_classification")
    worker_b_base = bases.get(WORKER_B)
    return {
        "arm": arm,
        "coordinator_scheduling_classification": schedule,
        "distinct_worker_s1_executions_observed": set(
            (summary.get("worker_returncodes") or {}).keys()
        ) == {"codex-worker-a", "codex-worker-b"},
        "worker_a_start_base_commit": bases.get("codex-worker-a"),
        "worker_b_start_base_commit": worker_b_base,
        "worker_b_started_after_a_integration": (
            bool(worker_b_base and baseline) and worker_b_base != baseline
            if schedule == "a_then_b"
            else False
        ),
        "control_concurrent_live_overlap_observed": (
            arm == "control" and summary.get("schedule_stages") == [["codex-worker-a", "codex-worker-b"]]
        ),
        "composed_acceptance": summary.get("composed_acceptance"),
        "worker_b_contract_key": classify_contract_key(worker_b_patch),
        "scalar_s2_score": None,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-summary", type=Path, required=True)
    parser.add_argument("--worker-b-patch", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    summary = json.loads(args.run_summary.read_text(encoding="utf-8"))
    metrics = extract(summary, args.worker_b_patch.read_text(encoding="utf-8"))
    text = json.dumps(metrics, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
