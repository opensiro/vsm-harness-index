from pathlib import Path
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_full_a  # noqa: E402


class FullAViewTests(unittest.TestCase):
    def assessment(self, harness_id: str, states: list[str]) -> dict[str, str]:
        keys = ("s1", "s2", "s3", "s3_star", "s4", "s5")
        row = {"harness_id": harness_id, "status": "included"}
        row.update({f"autonomy_{key}": state for key, state in zip(keys, states)})
        return row

    def catalog(self, harness_id: str, project_name: str) -> dict[str, str]:
        return {
            "harness_id": harness_id,
            "project_name": project_name,
            "repository": f"https://github.com/example/{harness_id}",
        }

    def test_a_parent_counts_as_autonomous_coverage(self):
        assessment = self.assessment(
            "parent-option",
            ["A", "A", "A(P)", "A", "A(P)", "A(P)"],
        )
        self.assertTrue(render_full_a.has_full_a_coverage(assessment))

    def test_parent_only_and_constructor_states_do_not_count(self):
        for state in ("P", "C", "C(P)", "—", "?"):
            with self.subTest(state=state):
                assessment = self.assessment(
                    "not-full-a",
                    ["A", "A", "A", "A", "A", state],
                )
                self.assertFalse(render_full_a.has_full_a_coverage(assessment))

    @patch("render_full_a.data")
    def test_pivot_includes_exact_a_and_a_parent_rows(self, mocked_data):
        mocked_data.return_value = [
            (
                1,
                self.catalog("exact", "Exact"),
                self.assessment("exact", ["A", "A", "A", "A", "A", "A"]),
                "Exact full autonomous coverage.",
            ),
            (
                2,
                self.catalog("parent-option", "Parent Option"),
                self.assessment(
                    "parent-option",
                    ["A", "A", "A(P)", "A", "A(P)", "A(P)"],
                ),
                "Autonomous coverage with optional parent modes.",
            ),
            (
                3,
                self.catalog("parent-only", "Parent Only"),
                self.assessment("parent-only", ["A", "A", "A", "A", "A", "P"]),
                "Parent owns the final function.",
            ),
        ]

        rendered = render_full_a.render_full_a(ROOT)

        self.assertIn("[Exact]", rendered)
        self.assertIn("[Parent Option]", rendered)
        self.assertIn("Autonomous coverage with optional parent modes.", rendered)
        self.assertNotIn("[Parent Only]", rendered)
        self.assertNotIn("Parent owns the final function.", rendered)

    @patch("render_full_a.data", return_value=[])
    def test_empty_view_still_renders_the_pivot_header(self, _mocked_data):
        rendered = render_full_a.render_full_a(ROOT)
        self.assertIn("| Harness | S1 | S2 | S3 | S3* | S4 | S5 | TL;DR |", rendered)


if __name__ == "__main__":
    unittest.main()
