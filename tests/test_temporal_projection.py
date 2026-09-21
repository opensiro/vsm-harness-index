from pathlib import Path
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_tldr  # noqa: E402


class TemporalProjectionTests(unittest.TestCase):
    def catalog(self, created_at: str, pinned_at: str = "2026-09-21") -> dict[str, str]:
        return {
            "harness_id": created_at[:10],
            "project_name": created_at[:10],
            "repository": "https://github.com/example/project",
            "repository_created_at": created_at,
            "pinned_at": pinned_at,
        }

    def assessment(self, states: list[str]) -> dict[str, str]:
        keys = ("s1", "s2", "s3", "s3_star", "s4", "s5")
        row = {"status": "included"}
        row.update({f"autonomy_{key}": state for key, state in zip(keys, states)})
        return row

    def test_calendar_quarter_boundaries(self):
        cases = {
            "2026-03-31T23:59:59Z": "Q1",
            "2026-04-01T00:00:00Z": "Q2",
            "2026-06-30T23:59:59Z": "Q2",
            "2026-07-01T00:00:00Z": "Q3",
            "2026-09-30T23:59:59Z": "Q3",
            "2026-10-01T00:00:00Z": "Q4",
        }
        for timestamp, expected in cases.items():
            with self.subTest(timestamp=timestamp):
                self.assertEqual(render_tldr.quarter_from_timestamp(timestamp), expected)

    def test_period_is_derived_from_repository_created_at(self):
        catalog = self.catalog("2026-07-04T12:00:00Z")
        self.assertEqual(render_tldr.year(catalog), "2026")
        self.assertEqual(render_tldr.quarter(catalog), "Q3")
        self.assertEqual(render_tldr.period(catalog), "2026-Q3")

    @patch("render_tldr.data")
    def test_current_year_and_quarter_are_marked_partial(self, mocked_data):
        mocked_data.return_value = [
            (
                1,
                self.catalog("2026-05-01T00:00:00Z", "2026-06-15"),
                self.assessment(["A", "A", "A", "A", "A", "A"]),
                "",
            ),
            (
                2,
                self.catalog("2026-08-01T00:00:00Z", "2026-09-21"),
                self.assessment(["A", "A", "A(P)", "A", "A(P)", "P"]),
                "",
            ),
        ]

        rendered = render_tldr.render_temporal(ROOT)

        self.assertIn("2026-Q3 (partial)", rendered)
        self.assertIn("2026 (YTD)", rendered)
        self.assertIn("**Projection as-of:** 2026-09-21", rendered)
        self.assertIn("`A(P)` collapses to base `A`", rendered)

    def test_base_state_preserves_existing_ranking_semantics(self):
        self.assertEqual(render_tldr.base_state("A(P)"), "A")
        self.assertEqual(render_tldr.base_state("C(P)"), "C")
        for state in ("A", "C", "P", "—", "?"):
            with self.subTest(state=state):
                self.assertEqual(render_tldr.base_state(state), state)


if __name__ == "__main__":
    unittest.main()
