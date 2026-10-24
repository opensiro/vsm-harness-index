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

    def test_occupied_project_slug_uses_owner_qualified_path(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "assessments").mkdir()
            (root / "assessments/agent-os.md").write_text(
                "repository: https://github.com/andrewgolovanov/agent-os\n"
            )
            self.assertEqual(
                preflight.resolve_assessment_path(root, "Agent OS", "earthwalker17/agent-os"),
                ("assessments/earthwalker17-agent-os.md", "new"),
            )
            (root / "assessments/earthwalker17-agent-os.md").write_text(
                "repository: https://github.com/earthwalker17/agent-os\n"
            )
            self.assertEqual(
                preflight.resolve_assessment_path(root, "Agent OS", "earthwalker17/agent-os"),
                ("assessments/earthwalker17-agent-os.md", "existing"),
            )

    def test_occupied_owner_qualified_slug_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "assessments").mkdir()
            for name in ("agent-os", "earthwalker17-agent-os"):
                (root / "assessments" / f"{name}.md").write_text(
                    "repository: https://github.com/different/project\n"
                )
            with self.assertRaisesRegex(preflight.PreflightError, "slug collision"):
                preflight.resolve_assessment_path(root, "Agent OS", "earthwalker17/agent-os")

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

    def test_compact_board_resolves_ref_only_from_frozen_map(self):
        compact = """## Manual assessment board

| # | Project | Status |
| ---: | --- | --- |
| 1 | IronClaw | ADMITTED |
| 2 | ZeroClaw | **NEXT** |
"""
        with tempfile.TemporaryDirectory() as temp:
            contract = Path(temp) / "active-contract.psv"
            contract.write_text(
                "profile_version|methodology_version\n0.2.4|0.3.7\n", encoding="utf-8"
            )
            task = preflight.build_envelope(
                159, ISSUE, [{"body": compact}], root=Path(temp), contract_path=contract
            )
        self.assertEqual(task.row, 2)
        self.assertEqual(task.repository, "zeroclaw-labs/zeroclaw")
        self.assertEqual(task.review_ref, "757db6c356c61861256a87222e30c7c92e8f166f")

    def test_compact_board_project_mismatch_fails_closed(self):
        compact = "## Manual assessment board\n| 1 | Wrong Project | **NEXT** |"
        with self.assertRaisesRegex(preflight.PreflightError, "project mismatch"):
            preflight.build_envelope(159, ISSUE, [{"body": compact}])

    def test_multiple_next_rows_fail_closed_in_compact_board(self):
        compact = """## Manual assessment board
| 1 | IronClaw | **NEXT** |
| 2 | ZeroClaw | **NEXT** |
"""
        with self.assertRaisesRegex(preflight.PreflightError, "multiple NEXT"):
            preflight.extract_next_row([compact])

    def test_duplicate_frozen_candidate_row_fails_closed(self):
        duplicated = ISSUE["body"] + (
            "| 2 | Another | `elsewhere/project` | "
            "`757db6c356c61861256a87222e30c7c92e8f166f` | duplicate |\n"
        )
        with self.assertRaisesRegex(preflight.PreflightError, "exactly one frozen"):
            preflight.extract_candidate(duplicated, 2, None)

    def test_checkpoint_mention_does_not_shadow_actual_board(self):
        checkpoint = """## Row 1 follow-up — review gate

**Manual assessment board remains unchanged:** 0/10 terminal;
Impulse row 1 NEXT; all remaining rows WAITING. This is not a new snapshot.
"""
        result = preflight.extract_next_row([COMMENTS[0]["body"], checkpoint])
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], "IronClaw")

    def test_non_board_heading_does_not_shadow_snapshot(self):
        note = "## Manual assessment board remains unchanged\n\nNo new row admitted."
        self.assertEqual(preflight.extract_next_row([COMMENTS[0]["body"], note])[0], 1)

    def test_terminal_latest_board_does_not_fall_back_to_stale_next(self):
        terminal = """## Manual assessment board — runtime/orchestration batch 07 — COMPLETE\n\n| # | Project | Frozen ref | State |\n| ---: | --- | --- | --- |\n| 1 | IronClaw | `b0b999d96781516ee05e6ba961d6f3ead900da96` | DONE |\n| 2 | ZeroClaw | `757db6c356c61861256a87222e30c7c92e8f166f` | DONE |\n\nQueue complete. No `NEXT` row remains.\n"""
        with self.assertRaisesRegex(
            preflight.PreflightError,
            "latest Manual assessment board has no row marked NEXT",
        ):
            preflight.extract_next_row([COMMENTS[0]["body"], terminal])


if __name__ == "__main__":
    unittest.main()
