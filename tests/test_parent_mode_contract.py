from pathlib import Path
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_tldr  # noqa: E402
import validate_tldr  # noqa: E402


class ParentModeValidationTests(unittest.TestCase):
    def row(self, **overrides):
        row = {
            "harness_id": "fixture",
            "project_name": "Fixture",
            "repository": "https://github.com/example/fixture",
            "review_ref": "a" * 40,
            "reviewed_at": "2026-09-16",
            "status": "included",
            "profile_version": "0.2.1",
            "assessment_procedure_version": "0.3.1",
            "autonomy_s1": "A",
            "autonomy_s2": "—",
            "autonomy_s3": "—",
            "autonomy_s3_star": "—",
            "autonomy_s4": "—",
            "autonomy_s5": "—",
        }
        row.update(overrides)
        return row

    def test_parent_modes_are_allowed_on_s3_s4_s5(self):
        for key in ("s3", "s4", "s5"):
            for state in ("A(P)", "C(P)", "P"):
                with self.subTest(key=key, state=state):
                    validate_tldr.validate_assessment(self.row(**{f"autonomy_{key}": state}))

    def test_parent_modes_are_rejected_on_s1_s2_s3star(self):
        for key in ("s1", "s2", "s3_star"):
            for state in ("A(P)", "C(P)", "P"):
                with self.subTest(key=key, state=state):
                    row = self.row(**{f"autonomy_{key}": state})
                    with self.assertRaisesRegex(ValueError, "valid only for S3, S4, or S5"):
                        validate_tldr.validate_assessment(row)

    def test_s3_s4_parent_only_requires_methodology_0_3_or_newer(self):
        for key in ("s3", "s4"):
            with self.subTest(key=key):
                row = self.row(
                    assessment_procedure_version="0.2.3",
                    **{f"autonomy_{key}": "P"},
                )
                with self.assertRaisesRegex(ValueError, "requires assessment_procedure_version >= 0.3.0"):
                    validate_tldr.validate_assessment(row)

    def test_composite_parent_mode_requires_methodology_0_3_or_newer(self):
        row = self.row(
            assessment_procedure_version="0.2.3",
            autonomy_s5="A(P)",
        )
        with self.assertRaisesRegex(ValueError, "requires assessment_procedure_version >= 0.3.0"):
            validate_tldr.validate_assessment(row)

    def test_legacy_s5_parent_only_remains_compatible_without_version_metadata(self):
        row = self.row(autonomy_s5="P")
        row.pop("profile_version")
        row.pop("assessment_procedure_version")
        validate_tldr.validate_assessment(row)

    def test_proposed_artifacts_may_carry_claims_for_admission_review(self):
        row = self.row(status="proposed", autonomy_s2="P")
        validate_tldr.validate_assessment(row)


class ParentModeRankingTests(unittest.TestCase):
    def assessment(self, harness_id: str, s3: str):
        return {
            "harness_id": harness_id,
            "status": "included",
            "autonomy_s1": "A",
            "autonomy_s2": "—",
            "autonomy_s3": s3,
            "autonomy_s3_star": "—",
            "autonomy_s4": "—",
            "autonomy_s5": "—",
        }

    def catalog(self, harness_id: str, created: str):
        return {
            "harness_id": harness_id,
            "project_name": harness_id,
            "repository": f"https://github.com/example/{harness_id}",
            "repository_created_at": created,
        }

    def test_base_state_helpers_preserve_unweighted_parent_modifier(self):
        self.assertEqual(render_tldr.base_state("A(P)"), "A")
        self.assertEqual(render_tldr.base_state("C(P)"), "C")
        self.assertTrue(render_tldr.has_parent_mode("A(P)"))
        self.assertTrue(render_tldr.has_parent_mode("C(P)"))
        self.assertTrue(render_tldr.has_parent_mode("P"))
        self.assertFalse(render_tldr.has_parent_mode("A"))

    def test_a_and_a_parent_receive_same_rank_key(self):
        rows = [
            (1, self.catalog("plain-a", "2025-01-01T00:00:00Z"), self.assessment("plain-a", "A"), "sig"),
            (2, self.catalog("a-parent", "2026-01-01T00:00:00Z"), self.assessment("a-parent", "A(P)"), "sig"),
        ]
        with patch.object(render_tldr, "data", return_value=rows):
            output = render_tldr.render_rankings(ROOT)
        data_lines = [line for line in output.splitlines() if "example/plain-a" in line or "example/a-parent" in line]
        self.assertEqual(len(data_lines), 2)
        self.assertTrue(all(line.startswith("| 1 |") for line in data_lines))
        parent_line = next(line for line in data_lines if "a-parent" in line)
        plain_line = next(line for line in data_lines if "plain-a" in line)
        self.assertIn("| 2/6 | 1/5 |", parent_line)
        self.assertIn("| 2/6 | 1/5 |", plain_line)
        self.assertIn("| 1 | 0 |", parent_line)
        self.assertIn("| 0 | 0 |", plain_line)


if __name__ == "__main__":
    unittest.main()
