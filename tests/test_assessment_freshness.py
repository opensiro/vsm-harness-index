import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_tldr import validate_assessment


class AssessmentFreshnessTests(unittest.TestCase):
    def base(self):
        return {
            "harness_id": "demo",
            "project_name": "Demo",
            "repository": "https://github.com/example/demo",
            "review_ref": "1" * 40,
            "reviewed_at": "2026-09-17",
            "profile_version": "0.2.1",
            "assessment_procedure_version": "0.3.1",
            "status": "included",
            "autonomy_s1": "A",
            "autonomy_s2": "—",
            "autonomy_s3": "—",
            "autonomy_s3_star": "—",
            "autonomy_s4": "—",
            "autonomy_s5": "—",
        }

    def test_baseline_can_record_assessment_changed_at_without_round_freshness(self):
        row = self.base()
        row["assessment_changed_at"] = "2026-09-17"
        validate_assessment(row)

    def test_partial_round_freshness_still_requires_complete_round_metadata(self):
        row = self.base()
        row["assessment_changed_at"] = "2026-09-17"
        row["last_checked_ref"] = "2" * 40
        with self.assertRaisesRegex(ValueError, "reassessment freshness metadata must be complete"):
            validate_assessment(row)

    def test_complete_round_freshness_remains_valid(self):
        row = self.base()
        row.update(
            {
                "assessment_changed_at": "2026-09-17",
                "last_checked_ref": "2" * 40,
                "last_checked_at": "2026-09-17",
                "last_reassessment_round": "R2",
            }
        )
        validate_assessment(row)


if __name__ == "__main__":
    unittest.main()
