from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXP = ROOT / "experiments" / "functional-capability-depth"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def row_by_id(rows: list[dict], observation_id: str) -> dict:
    matches = [row for row in rows if row.get("observation_id") == observation_id]
    assert len(matches) == 1, (observation_id, len(matches))
    return matches[0]


# Historical S3 projection: retain interpretation, remove duplicated result metrics.
s3_path = EXP / "s3-system-benchmarks" / "observations.json"
s3 = load(s3_path)
mao_id = "multi-agent-orchestration-supervisor-ablation-2026-08"
mao = row_by_id(s3, mao_id)
mao["raw_observation_ref"] = "../system-observations/multi-agent-orchestration.json#" + mao_id
for key in (
    "baseline_arm",
    "supervisor_arm",
    "reported_completion_gain_percentage_points",
    "reported_routing_accuracy_gain_percentage_points",
):
    assert key in mao, f"MAO historical payload already missing {key}"
    del mao[key]
dump(s3_path, s3)

# Historical S4 projections: retain VSM interpretation, remove duplicated result metrics.
s4_path = EXP / "s4-system-benchmarks" / "canonical_observations.json"
s4 = load(s4_path)
a_id = "a-evolve-harness-updating-2026"
a = row_by_id(s4, a_id)
a["raw_observation_ref"] = "../system-observations/a-evolve.json#" + a_id
assert "reported_harness_updating_metrics" in a
del a["reported_harness_updating_metrics"]

k_id = "kadath-ten-epoch-native-evolution-2026"
k = row_by_id(s4, k_id)
k["raw_observation_ref"] = "../system-observations/kadath.json#" + k_id
assert "reported_population_metrics" in k
del k["reported_population_metrics"]
dump(s4_path, s4)

# S3 validator: quantitative checks now hydrate the neutral raw observation.
s3v_path = EXP / "s3-system-benchmarks" / "validate.py"
text = s3v_path.read_text(encoding="utf-8")
marker = 'OMNIGENT_DELTA = HERE / "post-closure-deltas" / "omnigent-post-assessment-recovery.json"\n'
assert marker in text
text = text.replace(marker, marker + 'RAW_OBSERVATIONS = HERE.parent / "system-observations"\n', 1)

helper_marker = "\ndef validate_mao_observation(observation: dict) -> None:\n"
assert helper_marker in text
helper = '''
def load_raw_observation(filename: str, observation_id: str) -> dict:
    record = json.loads((RAW_OBSERVATIONS / filename).read_text(encoding="utf-8"))
    matches = [row for row in record.get("observations", []) if row.get("observation_id") == observation_id]
    if len(matches) != 1:
        fail(f"neutral raw observation lookup drift for {observation_id}: {len(matches)} matches")
    return matches[0]


def validate_mao_observation(observation: dict) -> None:
'''
text = text.replace(helper_marker, helper, 1)

comparison_block = '''    if observation.get("comparison_class") != "within-system-controlled-ablation":
        fail("Multi-Agent Orchestration comparison class drift")

    require_canonical_s3(MAO_HARNESS, MAO_REVIEW_REF)
'''
assert comparison_block in text
replacement = '''    if observation.get("comparison_class") != "within-system-controlled-ablation":
        fail("Multi-Agent Orchestration comparison class drift")

    expected_raw_ref = "../system-observations/multi-agent-orchestration.json#" + MAO_OBSERVATION_ID
    if observation.get("raw_observation_ref") != expected_raw_ref:
        fail("Multi-Agent Orchestration raw observation linkage drift")
    for key in (
        "baseline_arm",
        "supervisor_arm",
        "reported_completion_gain_percentage_points",
        "reported_routing_accuracy_gain_percentage_points",
    ):
        if key in observation:
            fail(f"Multi-Agent Orchestration derived record duplicates neutral numeric payload: {key}")
    raw = load_raw_observation("multi-agent-orchestration.json", MAO_OBSERVATION_ID)

    require_canonical_s3(MAO_HARNESS, MAO_REVIEW_REF)
'''
text = text.replace(comparison_block, replacement, 1)

old = '    baseline = observation.get("baseline_arm")\n    supervisor = observation.get("supervisor_arm")\n'
assert old in text
text = text.replace(old, '    baseline = raw.get("baseline_arm")\n    supervisor = raw.get("supervisor_arm")\n', 1)
old = '    if observation.get("reported_completion_gain_percentage_points") != 68.5:\n'
assert old in text
text = text.replace(old, '    if raw.get("reported_completion_gain_percentage_points") != 68.5:\n', 1)
old = '    if observation.get("reported_routing_accuracy_gain_percentage_points") != 43.3333:\n'
assert old in text
text = text.replace(old, '    if raw.get("reported_routing_accuracy_gain_percentage_points") != 43.3333:\n', 1)
s3v_path.write_text(text, encoding="utf-8")

# S4 validator: quantitative checks now hydrate A-Evolve/KADATH from neutral raw observations.
s4v_path = EXP / "s4-system-benchmarks" / "validate.py"
text = s4v_path.read_text(encoding="utf-8")
marker = 'PROXY_OBSERVATIONS = HERE / "proxy_observations.json"\n'
assert marker in text
text = text.replace(marker, marker + 'RAW_OBSERVATIONS = HERE.parent / "system-observations"\n', 1)

main_marker = "\ndef main() -> None:\n"
assert main_marker in text
helper = '''
def load_raw_observation(filename: str, observation_id: str) -> dict:
    record = json.loads((RAW_OBSERVATIONS / filename).read_text(encoding="utf-8"))
    matches = [row for row in record.get("observations", []) if row.get("observation_id") == observation_id]
    if len(matches) != 1:
        fail(f"neutral raw observation lookup drift for {observation_id}: {len(matches)} matches")
    return matches[0]


def main() -> None:
'''
text = text.replace(main_marker, helper, 1)

a_block = '''    if canonical_obs.get("comparison_class") != "controlled-within-system-evolver-study":
        fail("canonical A-Evolve comparison class drift")
    if canonical_obs.get("benchmarks") != ["SWE-bench Verified", "MCP-Atlas", "SkillsBench"]:
'''
assert a_block in text
a_replacement = '''    if canonical_obs.get("comparison_class") != "controlled-within-system-evolver-study":
        fail("canonical A-Evolve comparison class drift")
    expected_a_raw_ref = "../system-observations/a-evolve.json#a-evolve-harness-updating-2026"
    if canonical_obs.get("raw_observation_ref") != expected_a_raw_ref:
        fail("canonical A-Evolve raw observation linkage drift")
    if "reported_harness_updating_metrics" in canonical_obs:
        fail("canonical A-Evolve derived record duplicates neutral numeric payload")
    a_evolve_raw = load_raw_observation("a-evolve.json", "a-evolve-harness-updating-2026")
    if canonical_obs.get("benchmarks") != ["SWE-bench Verified", "MCP-Atlas", "SkillsBench"]:
'''
text = text.replace(a_block, a_replacement, 1)
old = '    metrics = canonical_obs.get("reported_harness_updating_metrics")\n'
assert old in text
text = text.replace(old, '    metrics = a_evolve_raw.get("reported_harness_updating_metrics")\n', 1)

k_block = '''    if kadath_obs.get("comparison_class") != "within-system-longitudinal-population-evolution":
        fail("KADATH comparison class drift")
    if kadath_obs.get("epochs") != 10:
'''
assert k_block in text
k_replacement = '''    if kadath_obs.get("comparison_class") != "within-system-longitudinal-population-evolution":
        fail("KADATH comparison class drift")
    expected_k_raw_ref = "../system-observations/kadath.json#kadath-ten-epoch-native-evolution-2026"
    if kadath_obs.get("raw_observation_ref") != expected_k_raw_ref:
        fail("KADATH raw observation linkage drift")
    if "reported_population_metrics" in kadath_obs:
        fail("KADATH derived record duplicates neutral numeric payload")
    kadath_raw = load_raw_observation("kadath.json", "kadath-ten-epoch-native-evolution-2026")
    if kadath_obs.get("epochs") != 10:
'''
text = text.replace(k_block, k_replacement, 1)
old = '    if kadath_obs.get("reported_population_metrics") != expected_kadath_metrics:\n'
assert old in text
text = text.replace(old, '    if kadath_raw.get("reported_population_metrics") != expected_kadath_metrics:\n', 1)
s4v_path.write_text(text, encoding="utf-8")

# Regression contract: derived records must no longer own the result metrics.
test_path = ROOT / "tests" / "test_neutral_registry_bootstrap_790.py"
test_path.write_text('''from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments" / "functional-capability-depth"
RAW = EXPERIMENT / "system-observations"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(rows: list[dict], observation_id: str) -> dict:
    for row in rows:
        if row.get("observation_id") == observation_id:
            return row
    raise AssertionError(f"missing observation {observation_id}")


def raw_observation(filename: str, observation_id: str) -> tuple[dict, dict]:
    record = load(RAW / filename)
    return record, by_id(record["observations"], observation_id)


class NeutralRegistryBootstrap790Tests(unittest.TestCase):
    def test_multi_agent_orchestration_neutral_record_owns_numeric_payload(self) -> None:
        historical = load(EXPERIMENT / "s3-system-benchmarks" / "observations.json")
        derived = by_id(historical, "multi-agent-orchestration-supervisor-ablation-2026-08")
        record, raw = raw_observation(
            "multi-agent-orchestration.json",
            "multi-agent-orchestration-supervisor-ablation-2026-08",
        )
        self.assertEqual(
            derived["raw_observation_ref"],
            "../system-observations/multi-agent-orchestration.json#multi-agent-orchestration-supervisor-ablation-2026-08",
        )
        for key in (
            "baseline_arm",
            "supervisor_arm",
            "reported_completion_gain_percentage_points",
            "reported_routing_accuracy_gain_percentage_points",
        ):
            self.assertNotIn(key, derived)
        self.assertEqual(raw["baseline_arm"]["scenarios_passed"], 11)
        self.assertEqual(raw["supervisor_arm"]["scenarios_passed"], 48)
        self.assertEqual(raw["reported_completion_gain_percentage_points"], 68.5)
        self.assertEqual(raw["reported_routing_accuracy_gain_percentage_points"], 43.3333)
        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])

    def test_a_evolve_neutral_record_owns_numeric_payload(self) -> None:
        historical = load(EXPERIMENT / "s4-system-benchmarks" / "canonical_observations.json")
        derived = by_id(historical, "a-evolve-harness-updating-2026")
        record, raw = raw_observation("a-evolve.json", "a-evolve-harness-updating-2026")
        self.assertEqual(
            derived["raw_observation_ref"],
            "../system-observations/a-evolve.json#a-evolve-harness-updating-2026",
        )
        self.assertNotIn("reported_harness_updating_metrics", derived)
        self.assertEqual(
            raw["reported_harness_updating_metrics"],
            {
                "maximum_best_vs_worst_evolver_spread_pp": 3.1,
                "qwen3_235b_swe_gain_pp": 8.2,
                "qwen3_235b_mcp_gain_pp": 0.6,
                "qwen3_5_9b_skillsbench_gain_pp": 3.8,
                "opus_4_6_skillsbench_gain_pp": 2.3,
                "qwen3_235b_skillsbench_gain_pp": 1.5,
            },
        )
        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])

    def test_kadath_neutral_record_owns_numeric_payload(self) -> None:
        historical = load(EXPERIMENT / "s4-system-benchmarks" / "canonical_observations.json")
        derived = by_id(historical, "kadath-ten-epoch-native-evolution-2026")
        record, raw = raw_observation("kadath.json", "kadath-ten-epoch-native-evolution-2026")
        self.assertEqual(
            derived["raw_observation_ref"],
            "../system-observations/kadath.json#kadath-ten-epoch-native-evolution-2026",
        )
        self.assertNotIn("reported_population_metrics", derived)
        self.assertEqual(
            raw["reported_population_metrics"],
            {
                "best_fitness_epoch_1": 18,
                "best_fitness_epoch_10": 91,
                "best_fitness_improvement": 73,
                "top5_median_epoch_1": 8,
                "top5_median_epoch_10": 77,
                "top5_median_improvement": 69,
                "top5_floor_epoch_1": 1,
                "top5_floor_epoch_10": 71,
                "top5_floor_improvement": 70,
            },
        )
        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])

    def test_bootstrap_raw_records_do_not_encode_function_attribution(self) -> None:
        for filename, observation_id in (
            ("multi-agent-orchestration.json", "multi-agent-orchestration-supervisor-ablation-2026-08"),
            ("a-evolve.json", "a-evolve-harness-updating-2026"),
            ("kadath.json", "kadath-ten-epoch-native-evolution-2026"),
        ):
            record, observation = raw_observation(filename, observation_id)
            self.assertNotIn("function", record)
            self.assertNotIn("benchmark_fit", record)
            self.assertNotIn("vsm_interpretation", record)
            self.assertNotIn("function", observation)
            self.assertNotIn("benchmark_fit", observation)
            self.assertNotIn("vsm_interpretation", observation)


if __name__ == "__main__":
    unittest.main()
''', encoding="utf-8")
