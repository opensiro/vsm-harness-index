#!/usr/bin/env python3
"""Verify why the frozen LoopX native-S2 execution is not identifiable.

The default mode validates only the committed Index artifacts and is safe for CI.
Pass --loopx-checkout to additionally import the *exact pinned LoopX checkout* and
exercise its first-party admission/host projection code. No model/provider call is
made in either mode.
"""

from __future__ import annotations

import argparse
import importlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "execution-feasibility.json"
PROTOCOL = HERE / "protocol.json"
TASK_A = HERE / "fixture" / "task-a.md"
TASK_B = HERE / "fixture" / "task-b.md"
CANONICAL_LOOPX_REVISION = "ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f"
SHARED_WRITE_SURFACE = "src/dispatch.py"


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return value


def _validate_static() -> dict[str, Any]:
    artifact = _load_json(ARTIFACT)
    protocol = _load_json(PROTOCOL)

    assert artifact["schema_version"] == 1
    assert artifact["status"] == "not-identifiable"
    assert artifact["tracking_issue"] == 606
    assert artifact["canonical_harness_id"] == "loopx"
    assert artifact["canonical_loopx_revision"] == CANONICAL_LOOPX_REVISION
    assert artifact["canonical_s2_state_unchanged"] == "A"
    assert artifact["protocol_status_unchanged"] == "preregistered-no-results"
    assert artifact["reason_code"] == (
        "frozen_two_task_overlap_has_no_native_child_topology"
    )
    assert artifact["frozen_fixture"] == {
        "worker_count": 2,
        "task_a": "fixture/task-a.md",
        "task_b": "fixture/task-b.md",
        "shared_write_surface": SHARED_WRITE_SURFACE,
    }
    assert artifact["treatment_identifiability"]["identifiable"] is False
    assert artifact["control_identifiability"]["identifiable"] is False
    assert artifact["effects"] == {
        "live_model_runs_attempted": False,
        "observations_registry_mutated": False,
        "canonical_assessment_changed": False,
        "capability_result_admitted": False,
        "scalar_s2_score_produced": False,
    }

    assert protocol["status"] == "preregistered-no-results"
    assert protocol["canonical_harness_id"] == "loopx"
    assert protocol["upstream_revision"] == CANONICAL_LOOPX_REVISION
    assert protocol["canonical_state_at_design"] == "A"
    execution = protocol["execution"]
    assert execution["worker_count"] == 2
    assert protocol["results"] is None
    assert protocol["observation_registry_mutation_allowed"] is False

    task_a = TASK_A.read_text(encoding="utf-8")
    task_b = TASK_B.read_text(encoding="utf-8")
    assert "Known write surface at preregistration: `src/dispatch.py`." in task_a
    assert "Known write surface at preregistration: `src/dispatch.py`." in task_b
    assert "Do not implement retryability classification" in task_a
    assert "Do not implement request-id propagation" in task_b

    evidence_paths = {item["path"] for item in artifact["evidence"]}
    assert evidence_paths == {
        "loopx/control_plane/quota/task_orchestration_admission.py",
        "loopx/control_plane/turn_driver/driver.py",
        "tests/control_plane/test_task_orchestration_admission.py",
        "tests/test_loopx_turn_codex_cli.py",
        "docs/integrations/codex-subagent-orchestration.md",
    }
    for item in artifact["evidence"]:
        assert CANONICAL_LOOPX_REVISION in item["url"]

    return {
        "artifact_status": artifact["status"],
        "protocol_status": protocol["status"],
        "canonical_loopx_revision": CANONICAL_LOOPX_REVISION,
        "frozen_worker_count": execution["worker_count"],
        "shared_write_surface": SHARED_WRITE_SURFACE,
    }


def _git_head(checkout: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git rev-parse failed")
    return result.stdout.strip()


def _todo(todo_id: str, write_scope: str) -> dict[str, Any]:
    return {
        "todo_id": todo_id,
        "status": "open",
        "task_class": "advancement_task",
        "priority": "P0",
        "text": f"Advance {todo_id}",
        "action_kind": "implement",
        "task_domain": "code",
        "required_write_scopes": [write_scope],
    }


def _dynamic_proof(loopx_checkout: Path) -> dict[str, Any]:
    checkout = loopx_checkout.expanduser().resolve()
    if not checkout.is_dir():
        raise ValueError(f"LoopX checkout does not exist: {checkout}")
    head = _git_head(checkout)
    if head != CANONICAL_LOOPX_REVISION:
        raise ValueError(
            "LoopX checkout HEAD mismatch: "
            f"expected {CANONICAL_LOOPX_REVISION}, got {head}"
        )

    sys.path.insert(0, str(checkout))
    try:
        task_orchestration = importlib.import_module(
            "loopx.control_plane.quota.task_orchestration"
        )
        codex_cli = importlib.import_module(
            "loopx.control_plane.turn_driver.codex_cli"
        )
        driver = importlib.import_module("loopx.control_plane.turn_driver.driver")

        apply_contract = task_orchestration.apply_task_orchestration_contract
        summary = {
            "items": [
                _todo("todo_task_a", SHARED_WRITE_SURFACE),
                _todo("todo_task_b", SHARED_WRITE_SURFACE),
            ]
        }
        common = {
            "fallback_work_lane_contract": {"lane": "advancement_task"},
            "goal_boundary": {
                "write_scope": ["src/**", "tests/**"],
                "orchestration": {
                    "mode": "multi_subagent",
                    "spawn_allowed": True,
                    "max_children": 2,
                },
            },
            "agent_identity": {
                "agent_id": "codex-main",
                "registered_agents": ["codex-main"],
            },
            "raw_user_todo_summary": {"items": []},
            "available_capabilities": ["subagent_spawn"],
        }
        frozen_contract, frozen_lane = apply_contract(
            agent_todo_summary=summary,
            raw_agent_todo_summary=summary,
            **common,
        )
        assert frozen_contract is None
        assert frozen_lane == {"lane": "advancement_task"}

        diagnostic_summary = {
            "items": [
                *summary["items"],
                _todo("todo_diagnostic_independent", "tests/**"),
            ]
        }
        diagnostic_contract, _ = apply_contract(
            agent_todo_summary=diagnostic_summary,
            raw_agent_todo_summary=diagnostic_summary,
            **common,
        )
        assert diagnostic_contract is not None
        assert diagnostic_contract["schema_version"] == "task_orchestration_contract_v2"
        assert [
            lane["todo_id"] for lane in diagnostic_contract["eligible_child_lanes"]
        ] == ["todo_diagnostic_independent"]
        assert diagnostic_contract["blocked_lanes"] == [
            {
                "todo_id": "todo_task_b",
                "task_domain": "code",
                "reason_codes": ["write_scope_conflict"],
                "conflicts_with_todo_id": "todo_task_a",
            }
        ]

        assert driver._child_host_operations(  # noqa: SLF001 - verifier targets frozen internals
            {"task_orchestration_contract": {}}, host="codex-cli"
        ) == []

        request = {
            "schema_version": "loopx_turn_host_request_v0",
            "turn_key": "sha256:" + "a" * 64,
            "route": "ready_for_host",
            "session": {
                "schema_version": "loopx_turn_session_binding_v0",
                "action": "start_new",
            },
            "turn_envelope": {
                "schema_version": "loopx_turn_envelope_v0",
                "goal_id": "fixture-goal",
                "agent_id": "codex-main",
                "action": {
                    "selected_todo": {
                        "todo_id": "todo_task_a",
                        "text": "Advance the frozen fixture",
                    }
                },
            },
            "result_contract": {
                "schema_version": "loopx_turn_result_v0",
                "completed_phases": ["host_execute", "typed_result"],
            },
        }
        result_schema = codex_cli.codex_cli_result_schema(request)
        assert "child_execution_receipts" not in result_schema["properties"]
        prompt = codex_cli._prompt(request)  # noqa: SLF001 - exact frozen host contract
        assert "spawn_agent" not in prompt
        assert "subagent_execution_topology" not in prompt

        return {
            "loopx_head": head,
            "frozen_two_task_contract": None,
            "diagnostic_block_reason": "write_scope_conflict",
            "diagnostic_independent_child": "todo_diagnostic_independent",
            "child_operations_without_adaptive_contract": 0,
            "typed_child_receipts_without_topology": False,
            "spawn_instruction_without_topology": False,
            "status": "not-identifiable",
        }
    finally:
        try:
            sys.path.remove(str(checkout))
        except ValueError:
            pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--loopx-checkout",
        type=Path,
        help=(
            "Optional local LoopX checkout. When provided, HEAD must equal the "
            "canonical pinned revision and the verifier imports its first-party code."
        ),
    )
    args = parser.parse_args()

    payload: dict[str, Any] = {
        "schema_version": 1,
        "static": _validate_static(),
    }
    if args.loopx_checkout is not None:
        payload["dynamic"] = _dynamic_proof(args.loopx_checkout)
    else:
        payload["dynamic"] = None
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
