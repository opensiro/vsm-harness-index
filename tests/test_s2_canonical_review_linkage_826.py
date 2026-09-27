from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
RAW = EXP / "system-observations"
TARGETS = {
    "squad-shared-state-conflict-attenuation-2026-03": (
        "squad-operational-history.json", "assessments/squad.md",
        "2099faf51c08a912c359209447011b06decf0565",
    ),
    "thclaws-team-workspace-interference-attenuation-2026": (
        "thclaws-operational-history.json", "assessments/thclaws.md",
        "cd700937a71a391f052438d139b7b1c5a6456755",
    ),
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class S2CanonicalReviewLinkage826Tests(unittest.TestCase):
    def test_raw_path_and_review_revision_have_distinct_schema_fields(self):
        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}
        for observation_id, (filename, assessment_path, review_ref) in TARGETS.items():
            derived = rows[observation_id]
            self.assertNotIn("canonical_assessment_ref", derived, observation_id)
            self.assertNotIn("canonical_review_ref", derived, observation_id)

            record = load(RAW / filename)
            self.assertEqual(record["canonical_assessment_ref"], assessment_path)
            self.assertEqual(record["canonical_review_ref"], review_ref)
            self.assertNotEqual(record["canonical_assessment_ref"], record["canonical_review_ref"])

            raw = next(
                row for row in record["observations"]
                if row["observation_id"] == observation_id
            )
            effective = dict(raw)
            effective["canonical_review_ref"] = record["canonical_review_ref"]
            effective.update(derived)
            self.assertEqual(effective["canonical_review_ref"], review_ref)
            self.assertNotIn("canonical_assessment_ref", effective)


if __name__ == "__main__":
    unittest.main()
