from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


class NeutralSemanticKeyCleanup818Tests(unittest.TestCase):
    def test_raw_registry_has_no_function_interpretation_keys(self):
        forbidden = {"function_interpretation", "mixed_function_caveat"}
        hits = []
        for path in sorted(RAW.glob("*.json")):
            for key in walk_keys(load(path)):
                if key in forbidden:
                    hits.append((path.name, key))
        self.assertEqual(hits, [])

    def test_llamar_interpretation_remains_in_derived_layers(self):
        proxy_rows = load(EXP / "s3-system-benchmarks" / "proxy_links.json")
        proxy = next(row for row in proxy_rows if row["projection_id"] == "llamar-mapthor-native-proxy-s3")
        self.assertIn("whole-team planner", proxy["mechanism_interpretation"])
        self.assertIn("rather than isolating", proxy["why_proxy_not_direct"])
        self.assertIn("proxy evidence", proxy["non_claim"])

        s2_delta = load(EXP / "s2-system-benchmarks" / "post-closure-deltas" / "llamar-2026-09-26.json")
        self.assertEqual(s2_delta["disposition"], "canonical-native-disturbance-evidence-no-direct-attenuation-result")
        self.assertEqual(s2_delta["result_surface_review"], "no-direct-s2-result")
        self.assertIn("crowding, blocking and collisions", s2_delta["finding"])
        self.assertFalse(s2_delta["reopen_condition_satisfied"])

    def test_smas_claim_boundary_is_derived_and_raw_results_unchanged(self):
        raw = load(RAW / "supervisoragent-smas.json")
        observation = raw["observations"][0]
        self.assertEqual(observation["reported_average_token_reduction_percent"], 29.68)
        self.assertEqual(observation["baseline_arm"]["average_accuracy_percent"], 50.91)
        self.assertEqual(observation["supervised_arm"]["average_accuracy_percent"], 50.91)
        self.assertNotIn("mixed_function_caveat", observation)

        derived_rows = load(EXP / "s3-system-benchmarks" / "observations.json")
        derived = next(row for row in derived_rows if row["observation_id"] == "supervisoragent-smas-gaia-pass1-2026")
        caveat = derived["mixed_function_caveat"]
        self.assertIn("verification-like", caveat)
        self.assertIn("not claimed as an isolated S3-only", caveat)
        self.assertEqual(derived["boundary_class"], "composed-supervised-mas")
        self.assertFalse(derived["canonical_system_eligible"])


if __name__ == "__main__":
    unittest.main()
