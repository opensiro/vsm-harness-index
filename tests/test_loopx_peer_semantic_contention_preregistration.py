from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = (
    ROOT
    / "experiments"
    / "functional-capability-depth"
    / "s2-system-benchmarks"
    / "loopx-peer-semantic-contention"
    / "validate.py"
)


class LoopXPeerSemanticContentionPreregistrationTests(unittest.TestCase):
    def test_preregistration_validator(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(
            "LoopX registered-peer semantic-contention preregistration validation passed",
            result.stdout,
        )


if __name__ == "__main__":
    unittest.main()
