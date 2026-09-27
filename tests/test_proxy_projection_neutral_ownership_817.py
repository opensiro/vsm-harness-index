from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"

EXPECTED = {
    "S2": {
        "autogen-magentic-one-native-proxy-s2": ("magentic-one.json", "native-system", "historical-first-party-lineage-not-current-review-ref"),
        "squad-marble-native-proxy-s2": ("squad.json", "native-system", "historical-first-party-lineage-not-current-review-ref"),
    },
    "S3": {
        "autogen-magentic-one-native-proxy-s3": ("magentic-one.json", "native-system", "historical-first-party-lineage-not-current-review-ref"),
        "llamar-mapthor-native-proxy-s3": ("llamar.json", "native-system", "first-party-published-artifacts-co-located-at-current-review-ref-run-revision-unknown"),
    },
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class ProxyProjectionNeutralOwnership817Tests(unittest.TestCase):
    def test_proxy_projections_are_interpretation_and_linkage_only(self):
        for function, expected in EXPECTED.items():
            rows = load(EXP / f"{function.lower()}-system-benchmarks" / "proxy_links.json")
            by_id = {row["projection_id"]: row for row in rows}
            self.assertEqual(set(by_id), set(expected))
            for projection_id, row in by_id.items():
                self.assertNotIn("system_compatibility", row, projection_id)
                self.assertNotIn("revision_relation", row, projection_id)
                self.assertEqual(row["function"], function)
                self.assertEqual(row["benchmark_fit"], "proxy")
                self.assertTrue(row["raw_observation_ids"])

    def test_neutral_raw_records_own_proxy_compatibility_and_revision_relation(self):
        for function, expected in EXPECTED.items():
            rows = load(EXP / f"{function.lower()}-system-benchmarks" / "proxy_links.json")
            by_id = {row["projection_id"]: row for row in rows}
            for projection_id, (filename, compatibility, relation) in expected.items():
                row = by_id[projection_id]
                self.assertEqual(row["raw_record"], f"../system-observations/{filename}")
                raw = load(RAW / filename)
                published = raw["published_implementation"]
                self.assertEqual(published["system_compatibility"], compatibility)
                self.assertEqual(published["canonical_revision_match"], relation)
                raw_ids = {item["observation_id"] for item in raw["observations"]}
                self.assertTrue(set(row["raw_observation_ids"]).issubset(raw_ids))


if __name__ == "__main__":
    unittest.main()
