from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = (
    ROOT
    / "experiments"
    / "functional-capability-depth"
    / "s2-system-benchmarks"
    / "loopx-native-contention"
)
VERIFIER = PACKAGE / "verify_execution_feasibility.py"


class LoopXNativeS2ExecutionFeasibilityTests(unittest.TestCase):
    def test_static_feasibility_verifier_is_ci_safe(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VERIFIER)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["schema_version"], 1)
        self.assertIsNone(payload["dynamic"])
        self.assertEqual(payload["static"]["artifact_status"], "not-identifiable")
        self.assertEqual(
            payload["static"]["protocol_status"],
            "preregistered-no-results",
        )
        self.assertEqual(payload["static"]["frozen_worker_count"], 2)
        self.assertEqual(
            payload["static"]["shared_write_surface"],
            "src/dispatch.py",
        )

    def test_feasibility_record_does_not_become_a_run_result(self) -> None:
        protocol = json.loads((PACKAGE / "protocol.json").read_text(encoding="utf-8"))
        feasibility = json.loads(
            (PACKAGE / "execution-feasibility.json").read_text(encoding="utf-8")
        )
        self.assertEqual(protocol["status"], "preregistered-no-results")
        self.assertIsNone(protocol["results"])
        self.assertEqual(feasibility["status"], "not-identifiable")
        self.assertFalse(feasibility["effects"]["live_model_runs_attempted"])
        self.assertFalse(feasibility["effects"]["capability_result_admitted"])
        self.assertEqual(feasibility["canonical_s2_state_unchanged"], "A")


if __name__ == "__main__":
    unittest.main()
