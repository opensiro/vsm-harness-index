"""One-off accepted re-review events preserve real longitudinal-round provenance."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_index import validate_reassessment_history


class SingleTargetReassessmentTests(unittest.TestCase):
    OLD = "1" * 40
    NEW = "2" * 40
    NEXT = "3" * 40
    ISSUE = "https://github.com/opensiro/vsm-harness-index/issues/3230"
    PR = "https://github.com/opensiro/vsm-harness-index/pull/3235"

    def case(self):
        assessment = {
            "harness_id": "demo",
            "status": "included",
            "review_ref": self.NEW,
            "reviewed_at": "2026-11-17",
            "profile_version": "0.2.4",
            "assessment_procedure_version": "0.3.8",
        }
        row = {
            "round_id": "S3230",
            "harness_id": "demo",
            "previous_review_ref": self.OLD,
            "checked_ref": self.NEW,
            "accepted_review_ref": self.NEW,
            "checked_at": "2026-11-17",
            "profile_version": "0.2.4",
            "assessment_procedure_version": "0.3.8",
            "outcome": "reassessed-unchanged",
            "changed_functions": "—",
            "evidence": f"{self.ISSUE} ; {self.PR}",
        }
        return {"demo": {"harness_id": "demo"}}, assessment, row

    def validate(self, rows, assessment):
        validate_reassessment_history(rows, {"demo": {"harness_id": "demo"}}, {"demo": assessment})

    def test_one_off_new_ref_without_fictitious_round_metadata(self):
        _, assessment, row = self.case()
        self.validate([row], assessment)
        self.assertNotIn("last_reassessment_round", assessment)
        self.assertNotIn("last_checked_ref", assessment)

    def test_one_off_rejected_without_correct_issue_link(self):
        _, assessment, row = self.case()
        row["evidence"] = self.PR
        with self.assertRaisesRegex(SystemExit, "missing exact Index issue"):
            self.validate([row], assessment)

    def test_one_off_does_not_accept_issue_prefix_collision(self):
        _, assessment, row = self.case()
        row["evidence"] = f"{self.ISSUE}0 ; {self.PR}"
        with self.assertRaisesRegex(SystemExit, "missing exact Index issue"):
            self.validate([row], assessment)

    def test_unchanged_result_cannot_claim_changed_functions(self):
        _, assessment, row = self.case()
        row["changed_functions"] = "S4"
        with self.assertRaisesRegex(SystemExit, "unchanged result must record"):
            self.validate([row], assessment)

    def test_one_off_rejected_without_index_pr_link(self):
        _, assessment, row = self.case()
        row["evidence"] = self.ISSUE
        with self.assertRaisesRegex(SystemExit, "missing accepted Index PR"):
            self.validate([row], assessment)

    def test_one_off_rejected_if_blocked_claimed_as_success(self):
        _, assessment, row = self.case()
        row["outcome"] = "blocked"
        with self.assertRaisesRegex(SystemExit, "requires an accepted review outcome"):
            self.validate([row], assessment)

    def test_one_off_rejected_if_not_issue_number(self):
        _, assessment, row = self.case()
        row["round_id"] = "S0"
        with self.assertRaisesRegex(SystemExit, "invalid reassessment review event id"):
            self.validate([row], assessment)

    def test_one_off_rejected_if_duplicate_id(self):
        _, assessment, row = self.case()
        with self.assertRaisesRegex(SystemExit, "duplicate reassessment event"):
            self.validate([row, dict(row)], assessment)

    def test_one_off_rejected_if_accepted_ref_not_current(self):
        _, assessment, row = self.case()
        assessment["review_ref"] = self.OLD
        with self.assertRaisesRegex(SystemExit, "canonical review_ref differs"):
            self.validate([row], assessment)

    def test_one_off_rejected_if_reviewed_date_not_accepted(self):
        _, assessment, row = self.case()
        assessment["reviewed_at"] = "2026-11-16"
        with self.assertRaisesRegex(SystemExit, "reviewed_at differs"):
            self.validate([row], assessment)

    def test_one_off_rejected_if_claimed_round_freshness_without_round(self):
        _, assessment, row = self.case()
        assessment["last_checked_ref"] = self.NEW
        with self.assertRaisesRegex(SystemExit, "round freshness metadata exists without a successful round"):
            self.validate([row], assessment)

    def test_one_off_same_ref_correction_must_not_claim_newer_checked_ref(self):
        _, assessment, row = self.case()
        row["outcome"] = "same-ref-correction"
        row["accepted_review_ref"] = self.OLD
        assessment["review_ref"] = self.OLD
        with self.assertRaisesRegex(SystemExit, "cannot claim newer inspected freshness"):
            self.validate([row], assessment)

    def test_earlier_round_freshness_survives_newer_single_ref(self):
        _, assessment, single = self.case()
        round_row = dict(single,
            round_id="R1",
            previous_review_ref=self.OLD,
            checked_ref=self.OLD,
            accepted_review_ref=self.OLD,
            checked_at="2026-10-01",
            outcome="no-upstream-change",
            evidence="https://github.com/example/demo/compare/base...checked")
        assessment.update(
            last_checked_ref=self.OLD,
            last_checked_at="2026-10-01",
            last_reassessment_round="R1",
        )
        self.validate([round_row, single], assessment)

    def test_actual_round_after_single_ref_advances_round_freshness(self):
        _, assessment, single = self.case()
        round_row = dict(single,
            round_id="R2",
            previous_review_ref=self.NEW,
            checked_ref=self.NEXT,
            accepted_review_ref=self.NEXT,
            checked_at="2026-11-19",
            outcome="reassessed-unchanged",
            evidence="https://github.com/example/demo/compare/new...next")
        assessment.update(
            review_ref=self.NEXT,
            reviewed_at="2026-11-19",
            last_checked_ref=self.NEXT,
            last_checked_at="2026-11-19",
            last_reassessment_round="R2",
        )
        self.validate([single, round_row], assessment)

    def test_history_chain_rejected_if_single_previous_ref_wrong(self):
        _, assessment, single = self.case()
        prior = dict(single,
            round_id="R1",
            previous_review_ref=self.OLD,
            checked_ref=self.OLD,
            accepted_review_ref=self.OLD,
            checked_at="2026-10-01",
            outcome="no-upstream-change",
            evidence="https://github.com/example/demo")
        single["previous_review_ref"] = self.NEXT
        with self.assertRaisesRegex(SystemExit, "does not continue prior accepted boundary"):
            self.validate([prior, single], assessment)


if __name__ == "__main__":
    unittest.main()
