from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_REF = "ae8e242c34ba8e57766b79896936a035a12fca85"
OLD_PATH = "experiments/functional-capability-depth/s4-system-benchmarks/proxy_observations.json"
PROXY = ROOT / OLD_PATH
RAW_DIR = ROOT / "experiments/functional-capability-depth/system-observations"
PREFIX = "../system-observations/"


class FutureSimNeutralRegistryMigration813Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        old_text = subprocess.check_output(
            ["git", "show", f"{BASE_REF}:{OLD_PATH}"], cwd=ROOT, text=True
        )
        cls.old = {row["observation_id"]: row for row in json.loads(old_text)}
        cls.links = json.loads(PROXY.read_text(encoding="utf-8"))

    def hydrate(self, link: dict) -> dict:
        ref = link["raw_observation_ref"]
        self.assertTrue(ref.startswith(PREFIX))
        rel, oid = ref[len(PREFIX):].rsplit("#", 1)
        self.assertEqual(oid, link["observation_id"])
        record = json.loads((RAW_DIR / rel).read_text(encoding="utf-8"))
        matches = [o for o in record["observations"] if o["observation_id"] == oid]
        self.assertEqual(len(matches), 1)
        raw = matches[0]
        effective = dict(link)
        for key, value in raw.items():
            if key in {"observation_id", "kind", "benchmark", "evidence_surface", "non_claim"}:
                continue
            effective[key] = value
        effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]
        effective["primary_sources"] = record["primary_sources"]
        return effective

    def test_all_five_rows_reconstruct_losslessly(self) -> None:
        self.assertEqual(len(self.old), 5)
        self.assertEqual(len(self.links), 5)
        self.assertEqual({x["observation_id"] for x in self.links}, set(self.old))
        for link in self.links:
            reconstructed = self.hydrate(link)
            reconstructed.pop("raw_observation_ref", None)
            self.assertEqual(reconstructed, self.old[link["observation_id"]], link["observation_id"])

    def test_projection_is_interpretation_only(self) -> None:
        forbidden = {
            "published_harness_version", "model", "benchmark_revision", "benchmark_window",
            "question_count", "seeds", "reasoning_setting", "prompt_condition",
            "final_top1_accuracy_percent", "final_brier_skill_score", "metric_provenance",
            "comparability_group", "confounders", "primary_sources", "system_compatibility",
        }
        for link in self.links:
            self.assertFalse(forbidden & set(link), link["observation_id"])
            self.assertEqual(link["function"], "S4")
            self.assertEqual(link["benchmark_fit"], "proxy")

    def test_raw_records_are_vsm_neutral(self) -> None:
        expected = {"futuresim-codex.json", "futuresim-claude-code.json", "futuresim-opencode.json"}
        ids: list[str] = []
        for name in expected:
            record = json.loads((RAW_DIR / name).read_text(encoding="utf-8"))
            self.assertEqual(record["evidence_source_class"], "external-reproduced")
            self.assertEqual(record["published_implementation"]["system_compatibility"], "adapter-preserved")
            for obs in record["observations"]:
                ids.append(obs["observation_id"])
                for forbidden in ("function", "benchmark_fit", "vsm_interpretation", "canonical_s4_state_at_review", "non_claim"):
                    self.assertNotIn(forbidden, obs)
        self.assertEqual(set(ids), set(self.old))
        self.assertEqual(len(ids), 5)


if __name__ == "__main__":
    unittest.main()
