from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROXY = ROOT / "experiments/functional-capability-depth/s4-system-benchmarks/proxy_observations.json"
VALIDATOR = ROOT / "experiments/functional-capability-depth/s4-system-benchmarks/validate.py"
RAW_DIR = ROOT / "experiments/functional-capability-depth/system-observations"
TEST = ROOT / "tests/test_futuresim_neutral_registry_migration_813.py"
BASE_REF = "ae8e242c34ba8e57766b79896936a035a12fca85"

DERIVED_KEYS = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "canonical_harness_id",
    "canonical_assessment_ref",
    "canonical_s4_state_at_review",
    "non_claim",
}
SYSTEM_NAMES = {
    "codex": "Codex",
    "claude-code": "Claude Code",
    "opencode": "OpenCode",
}
FILENAMES = {
    "codex": "futuresim-codex.json",
    "claude-code": "futuresim-claude-code.json",
    "opencode": "futuresim-opencode.json",
}


def frontmatter(harness_id: str) -> dict[str, str]:
    text = (ROOT / "assessments" / f"{harness_id}.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit(f"missing front matter: {harness_id}")
    out: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


rows = json.loads(PROXY.read_text(encoding="utf-8"))
if len(rows) != 5:
    raise SystemExit(f"expected 5 FutureSim proxy rows, got {len(rows)}")
if {row["canonical_harness_id"] for row in rows} != set(SYSTEM_NAMES):
    raise SystemExit("unexpected FutureSim system set")
if any(row.get("function") != "S4" or row.get("benchmark_id") != "futuresim" or row.get("benchmark_fit") != "proxy" for row in rows):
    raise SystemExit("FutureSim proxy semantics drift before migration")

groups: dict[str, list[dict]] = defaultdict(list)
for row in rows:
    groups[row["canonical_harness_id"]].append(row)

projection: list[dict] = []
for harness_id in sorted(groups):
    fields = frontmatter(harness_id)
    if fields.get("status") != "included":
        raise SystemExit(f"{harness_id}: canonical assessment not included")
    if fields.get("autonomy_s4") != "—":
        raise SystemExit(f"{harness_id}: FutureSim proxy migration assumes canonical S4=—")

    source_rows = groups[harness_id]
    sources: list[str] = []
    observations: list[dict] = []
    for old in source_rows:
        for source in old.get("primary_sources", []):
            if source not in sources:
                sources.append(source)

        moved = {
            key: value
            for key, value in old.items()
            if key not in DERIVED_KEYS
            and key not in {"system_compatibility", "primary_sources"}
        }
        raw = {
            "observation_id": old["observation_id"],
            "kind": "forecasting-benchmark-result",
            "benchmark": "FutureSim v1",
            **moved,
        }
        observations.append(raw)

        projection.append(
            {
                key: old[key]
                for key in (
                    "observation_id",
                    "function",
                    "benchmark_id",
                    "benchmark_fit",
                    "canonical_harness_id",
                    "canonical_assessment_ref",
                    "canonical_s4_state_at_review",
                    "non_claim",
                )
            }
            | {
                "raw_observation_ref": f"../system-observations/{FILENAMES[harness_id]}#{old['observation_id']}"
            }
        )

    record = {
        "schema_version": 1,
        "recorded_at": "2026-09-28",
        "evidence_source_class": "external-reproduced",
        "system_name": SYSTEM_NAMES[harness_id],
        "canonical_harness_id": harness_id,
        "canonical_assessment_ref": f"assessments/{harness_id}.md",
        "canonical_review_ref": fields["review_ref"],
        "canonical_repository": fields["repository"],
        "published_implementation": {
            "system_compatibility": "adapter-preserved",
            "historical_relation": "Published FutureSim v1 recommended/native-harness configuration; benchmark supplies chronological environment, search interface and forecast actions. This neutral record does not imply canonical S4 ownership or isolate a harness effect.",
        },
        "primary_sources": sources,
        "observations": observations,
    }
    (RAW_DIR / FILENAMES[harness_id]).write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

PROXY.write_text(json.dumps(projection, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

text = VALIDATOR.read_text(encoding="utf-8")
needle = '    proxy_observations = json.loads(PROXY_OBSERVATIONS.read_text(encoding="utf-8"))\n'
replacement = (
    '    proxy_links = json.loads(PROXY_OBSERVATIONS.read_text(encoding="utf-8"))\n'
    '    proxy_observations = [hydrate_s4_projection(row) for row in proxy_links]\n'
)
if needle not in text:
    raise SystemExit("S4 validator proxy-load anchor drift")
VALIDATOR.write_text(text.replace(needle, replacement, 1), encoding="utf-8")

TEST.write_text(
    '''from __future__ import annotations

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
''',
    encoding="utf-8",
)

print("prepared FutureSim S4 proxy neutral-registry migration")
