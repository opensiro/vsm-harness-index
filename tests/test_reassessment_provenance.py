import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_index import validate_reassessment_history


class ReassessmentProvenanceTests(unittest.TestCase):
    def base(self):
        previous = "1" * 40
        newer = "2" * 40
        catalog = {"demo": {"harness_id": "demo"}}
        assessment = {
            "harness_id": "demo",
            "status": "included",
            "review_ref": previous,
            "last_checked_ref": newer,
            "last_checked_at": "2026-09-17",
            "last_reassessment_round": "R2",
            "profile_version": "0.2.1",
            "assessment_procedure_version": "0.3.1",
        }
        row = {
            "round_id": "R2",
            "harness_id": "demo",
            "previous_review_ref": previous,
            "checked_ref": newer,
            "accepted_review_ref": previous,
            "checked_at": "2026-09-17",
            "profile_version": "0.2.1",
            "assessment_procedure_version": "0.3.1",
            "outcome": "same-ref-correction",
            "changed_functions": "S3",
            "evidence": "https://example.invalid/evidence",
        }
        return previous, newer, catalog, assessment, row

    def test_same_ref_correction_can_advance_freshness_only(self):
        _, _, catalog, assessment, row = self.base()
        validate_reassessment_history([row], catalog, {"demo": assessment})

    def test_same_ref_correction_cannot_advance_accepted_boundary(self):
        _, newer, catalog, assessment, row = self.base()
        row["accepted_review_ref"] = newer
        assessment["review_ref"] = newer
        with self.assertRaisesRegex(SystemExit, "cannot advance accepted_review_ref"):
            validate_reassessment_history([row], catalog, {"demo": assessment})


if __name__ == "__main__":
    unittest.main()
