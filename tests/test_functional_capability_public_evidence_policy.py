from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments" / "functional-capability-depth"
LOOPX = EXPERIMENT / "s2-system-benchmarks" / "loopx-peer-semantic-contention"


class FunctionalCapabilityPublicEvidencePolicyTest(unittest.TestCase):
    def test_capability_depth_is_public_evidence_only(self) -> None:
        text = (EXPERIMENT / "PUBLIC-EVIDENCE.md").read_text(encoding="utf-8")
        self.assertIn(
            "Opensiro does not run or reproduce benchmark experiments on assessed harnesses",
            text,
        )
        self.assertIn(
            "S2-S5 gaps therefore remain gaps until public upstream or third-party evidence",
            text,
        )
        self.assertNotIn(
            "Opensiro-operated benchmark execution is optional validation or reproduction evidence",
            text,
        )

    def test_loopx_execution_path_is_retired_without_rewriting_preregistration(self) -> None:
        status = (LOOPX / "EXECUTION_STATUS.md").read_text(encoding="utf-8")
        readme = (LOOPX / "README.md").read_text(encoding="utf-8")
        protocol = json.loads((LOOPX / "protocol.json").read_text(encoding="utf-8"))

        self.assertIn("retired historical experiment artifact", status)
        self.assertIn("no live execution planned", status)
        self.assertIn("retired historical preregistration", readme)
        self.assertIn("public upstream / third-party evidence discovery", readme)

        # Preserve the frozen historical preregistration rather than rewriting it
        # to look as if the original design had never existed.
        self.assertEqual(protocol["status"], "preregistered-no-results")
        self.assertIsNone(protocol["results"])
        self.assertFalse(protocol["observation_registry_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
