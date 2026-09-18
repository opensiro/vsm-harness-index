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

    @patch("render_full_a.data")
    def test_only_exact_six_a_rows_are_rendered(self, mocked_data):
        mocked_data.return_value = [
            (
                1,
                self.catalog("exact", "Exact"),
                self.assessment("exact", ["A", "A", "A", "A", "A", "A"]),
                "Exact full autonomous coverage.",
            ),
            (
                2,
                self.catalog("parent", "Parent"),
                self.assessment("parent", ["A", "A", "A(P)", "A", "A", "A"]),
                "Contains a parent-governed mode.",
            ),
        ]

        rendered = render_full_a.render_full_a(ROOT)

        self.assertIn("[Exact]", rendered)
        self.assertIn("Exact full autonomous coverage.", rendered)
        self.assertNotIn("[Parent]", rendered)
        self.assertNotIn("Contains a parent-governed mode.", rendered)

    @patch("render_full_a.data", return_value=[])
    def test_empty_view_still_renders_the_pivot_header(self, _mocked_data):
        rendered = render_full_a.render_full_a(ROOT)
        self.assertIn("| Harness | S1 | S2 | S3 | S3* | S4 | S5 | TL;DR |", rendered)


if __name__ == "__main__":
    unittest.main()
