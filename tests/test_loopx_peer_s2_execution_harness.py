from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PKG = (
    ROOT
    / "experiments"
    / "functional-capability-depth"
    / "s2-system-benchmarks"
    / "loopx-peer-semantic-contention"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class LoopXPeerS2ExecutionHarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.adapter = load_module("loopx_peer_s2_adapter_test", PKG / "adapter.py")
        cls.metrics = load_module("loopx_peer_s2_metrics_test", PKG / "extract_metrics.py")

    def test_static_identifiability_verifier(self) -> None:
        result = subprocess.run(
            [sys.executable, str(PKG / "verify_execution_identifiability.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(
            payload["static"]["status"],
            "identifiable-for-local-live-harness",
        )
        self.assertTrue(all(payload["static"]["gates"].values()))
        self.assertFalse(payload["static"]["live_model_runs_attempted"])
        self.assertIsNone(payload["static"]["scalar_s2_score"])
        self.assertIsNone(payload["dynamic"])

    def test_coordinator_classifications_map_only_to_frozen_schedules(self) -> None:
        expected = {
            "parallel": (("codex-worker-a", "codex-worker-b"),),
            "a_then_b": (("codex-worker-a",), ("codex-worker-b",)),
            "b_then_a": (("codex-worker-b",), ("codex-worker-a",)),
        }
        for classification, stages in expected.items():
            schedule = self.adapter.treatment_schedule(
                {"classification": classification}
            )
            self.assertEqual(schedule.stages, stages)
        with self.assertRaises(self.adapter.AdapterProtocolError):
            self.adapter.treatment_schedule({"classification": "guess"})

    def test_coordinator_result_validator_fails_closed(self) -> None:
        good = subprocess.run(
            [sys.executable, str(PKG / "validate_coordinator_result.py")],
            cwd=ROOT,
            input=json.dumps({"classification": "a_then_b"}),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
        bad = subprocess.run(
            [sys.executable, str(PKG / "validate_coordinator_result.py")],
            cwd=ROOT,
            input=json.dumps({"classification": "inspect_and_choose"}),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(bad.returncode, 0)

    def test_dry_runner_is_model_free_for_both_arms(self) -> None:
        for arm in ("treatment", "control"):
            result = subprocess.run(
                [
                    sys.executable,
                    str(PKG / "run_local.py"),
                    "--arm",
                    arm,
                    "--model-id",
                    "fake-model",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["plan"]["mode"], "dry-plan")
            self.assertFalse(payload["plan"]["live_model_runs_attempted"])
            self.assertNotIn("--execute-live", payload["plan"]["shared_worker_turn_surface"])

    def test_metric_extractor_is_posthoc_and_unscored(self) -> None:
        summary = {
            "arm": "treatment",
            "baseline_commit": "base",
            "coordinator_classification": "a_then_b",
            "schedule_stages": [["codex-worker-a"], ["codex-worker-b"]],
            "worker_start_base_commits": {
                "codex-worker-a": "base",
                "codex-worker-b": "after-a",
            },
            "worker_returncodes": {
                "codex-worker-a": 0,
                "codex-worker-b": 0,
            },
            "composed_acceptance": True,
        }
        metrics = self.metrics.extract(summary, '+ value = response["code"]\n')
        self.assertEqual(metrics["worker_b_contract_key"], "code")
        self.assertTrue(metrics["worker_b_started_after_a_integration"])
        self.assertTrue(metrics["distinct_worker_s1_executions_observed"])
        self.assertIsNone(metrics["scalar_s2_score"])

    def test_execution_plan_preserves_no_result_boundary(self) -> None:
        plan = json.loads((PKG / "execution-plan.json").read_text(encoding="utf-8"))
        self.assertEqual(plan["status"], "execution-harness-no-live-runs")
        self.assertFalse(plan["live_execution_default"])
        self.assertFalse(plan["ci_live_execution_allowed"])
        self.assertTrue(all(value is False for value in plan["effects"].values()))


if __name__ == "__main__":
    unittest.main()
