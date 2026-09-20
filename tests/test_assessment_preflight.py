import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "assessment_preflight", ROOT / "scripts" / "assessment_preflight.py"
)
assert SPEC and SPEC.loader
preflight = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = preflight
SPEC.loader.exec_module(preflight)


ISSUE = {
    "title": "[Assessment batch] Multi-agent runtime/orchestration harnesses 07 — IronClaw, ZeroClaw",
    "body": """## Frozen candidate set

| # | Project | Canonical repository | Review ref | Role / why in scope |
| ---: | --- | --- | --- | --- |
| 1 | IronClaw | `nearai/ironclaw` | `b0b999d96781516ee05e6ba961d6f3ead900da96` | runtime |
| 2 | ZeroClaw | `zeroclaw-labs/zeroclaw` | `757db6c356c61861256a87222e30c7c92e8f166f` | runtime |
""",
}

COMMENTS = [
    {
        "body": """## Manual assessment board — runtime/orchestration batch 07

| # | Project | Frozen ref | State |
| ---: | --- | --- | --- |
| 1 | IronClaw | `b0b999d96781516ee05e6ba961d6f3ead900da96` | **NEXT** |
| 2 | ZeroClaw | `757db6c356c61861256a87222e30c7c92e8f166f` | QUEUED |
"""
    }
]


class AssessmentPreflightTests(unittest.TestCase):
    def test_extracts_current_next_and_frozen_candidate(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            contract = root / "active-contract.psv"
            contract.write_text(
                "profile_version|methodology_version\n0.2.3|0.3.5\n", encoding="utf-8"
            )
            task = preflight.build_envelope(
                159, ISSUE, COMMENTS, root=root, contract_path=contract
            )

        self.assertEqual(task.row, 1)
        self.assertEqual(task.project, "IronClaw")
        self.assertEqual(task.repository, "nearai/ironclaw")
        self.assertEqual(task.review_ref, "b0b999d96781516ee05e6ba961d6f3ead900da96")
        self.assertEqual(task.assessment_path, "assessments/ironclaw.md")
        self.assertEqual(task.assessment_path_state, "new")
        self.assertEqual(task.profile_version, "0.2.3")
        self.assertEqual(task.methodology_version, "0.3.5")

    def test_rejects_board_ref_drift(self):
        comments = [{"body": COMMENTS[0]["body"].replace(
            "b0b999d96781516ee05e6ba961d6f3ead900da96",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        )}]
        with tempfile.TemporaryDirectory() as temp:
            contract = Path(temp) / "active-contract.psv"
            contract.write_text(
                "profile_version|methodology_version\n0.2.3|0.3.5\n", encoding="utf-8"
            )
            with self.assertRaises(preflight.PreflightError):
                preflight.build_envelope(
                    159, ISSUE, comments, root=Path(temp), contract_path=contract
                )

    def test_rejects_issue_without_next(self):
        with self.assertRaises(preflight.PreflightError):
            preflight.extract_next_row(["## Manual assessment board\n| 1 | IronClaw | `b0b999d96781516ee05e6ba961d6f3ead900da96` | QUEUED |"])


if __name__ == "__main__":
    unittest.main()
