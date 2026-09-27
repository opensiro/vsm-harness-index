from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 1) Grit: reusable provenance belongs to the neutral raw record, not the S2 projection.
path = ROOT / "tests/test_grit_s2_public_evidence_review.py"
text = path.read_text(encoding="utf-8")
old = '''        observation = grit_rows[0]\n        self.assertEqual(\n            observation["benchmark_artifact_revision"],\n            "a2c48735e0a16c49ca1541c4865fce438c479405",\n        )\n        self.assertEqual(observation["evidence_source_class"], "first-party-reported")\n        self.assertEqual(observation["system_compatibility"], "native-system")\n        self.assertEqual(observation["comparison_class"], "partially-matched")\n        self.assertIsNone(observation["canonical_harness_id"])\n        self.assertFalse(observation["canonical_system_eligible"])\n'''
new = '''        observation = grit_rows[0]\n        self.assertEqual(\n            observation["raw_observation_ref"],\n            "../system-observations/grit.json#grit-synthetic-merge-contention-2026-04",\n        )\n        raw_record = json.loads(\n            (ROOT / "experiments" / "functional-capability-depth" / "system-observations" / "grit.json").read_text(encoding="utf-8")\n        )\n        raw_rows = [\n            row\n            for row in raw_record["observations"]\n            if row.get("observation_id") == "grit-synthetic-merge-contention-2026-04"\n        ]\n        self.assertEqual(len(raw_rows), 1)\n        raw = raw_rows[0]\n        self.assertEqual(\n            raw["benchmark_artifact_revision"],\n            "a2c48735e0a16c49ca1541c4865fce438c479405",\n        )\n        self.assertEqual(raw_record["evidence_source_class"], "first-party-reported")\n        self.assertEqual(\n            raw_record["published_implementation"]["system_compatibility"],\n            "native-system",\n        )\n        self.assertEqual(raw["comparison_class"], "partially-matched")\n        self.assertIsNone(raw_record["canonical_harness_id"])\n        self.assertIsNone(observation["canonical_harness_id"])\n        self.assertFalse(observation["canonical_system_eligible"])\n        for neutral_owned in (\n            "benchmark_artifact_revision",\n            "evidence_source_class",\n            "system_compatibility",\n            "comparison_class",\n            "primary_sources",\n        ):\n            self.assertNotIn(neutral_owned, observation)\n'''
if old not in text:
    raise SystemExit("Grit legacy test anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

# 2) LLaMAR: canonical S-state stays in assessment/derived layers, never neutral raw.
path = ROOT / "tests/test_llamar_capability_evidence_749.py"
text = path.read_text(encoding="utf-8")
old = '''        self.assertEqual(raw.get("canonical_review_ref"), REVIEW_REF)\n        self.assertEqual(raw.get("canonical_states_at_review"), {"S2": "A", "S3": "A"})\n        relation = raw["published_implementation"]["canonical_revision_match"]\n'''
new = '''        self.assertEqual(raw.get("canonical_review_ref"), REVIEW_REF)\n        self.assertNotIn("canonical_states_at_review", raw)\n        self.assertNotIn("function", raw)\n        self.assertNotIn("benchmark_fit", raw)\n        self.assertNotIn("vsm_interpretation", raw)\n        relation = raw["published_implementation"]["canonical_revision_match"]\n'''
if old not in text:
    raise SystemExit("LLaMAR legacy test anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

# 3) Bootstrap #790: MAO canonical review identity is neutral-owned now.
path = ROOT / "tests/test_neutral_registry_bootstrap_790.py"
text = path.read_text(encoding="utf-8")
old = '''        self.assertEqual(raw["reported_completion_gain_percentage_points"], 68.5)\n        self.assertEqual(raw["reported_routing_accuracy_gain_percentage_points"], 43.3333)\n        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])\n'''
new = '''        self.assertEqual(raw["reported_completion_gain_percentage_points"], 68.5)\n        self.assertEqual(raw["reported_routing_accuracy_gain_percentage_points"], 43.3333)\n        self.assertNotIn("canonical_review_revision", derived)\n        self.assertEqual(derived["canonical_harness_id"], "multi-agent-orchestration")\n        self.assertEqual(\n            record["canonical_review_ref"],\n            "e6c34462af045d7e53d383103346362351c96353",\n        )\n'''
if old not in text:
    raise SystemExit("bootstrap #790 legacy test anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

# 4) New #815 regression: compare stable reusable evidence + function linkage,
# not pre-neutral wording that intentionally moved to neutral/non-VSM phrasing.
path = ROOT / "tests/test_direct_projection_neutral_ownership_815.py"
text = path.read_text(encoding="utf-8")
old_helper = '''    if record.get("canonical_harness_id"):\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    return effective\n'''
new_helper = '''    if record.get("canonical_harness_id"):\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    if row.get("observation_id") == MAO_ID:\n        effective["benchmark_artifact_revision"] = record.get("canonical_review_ref")\n        if "comparison_class" not in effective and isinstance(raw.get("comparison_design"), str):\n            effective["comparison_class"] = raw["comparison_design"]\n    return effective\n'''
if old_helper not in text:
    raise SystemExit("#815 hydrate_s3 test helper anchor drift")
text = text.replace(old_helper, new_helper, 1)
old_test = '''        self.assertEqual(hydrate_s3(new), hydrate_s3(old))\n        self.assertEqual(\n            set(new),\n            {\n                "observation_id", "function", "benchmark_id", "benchmark_fit",\n                "boundary_class", "canonical_harness_id", "canonical_system_eligible",\n                "vsm_interpretation", "raw_observation_ref",\n            },\n        )\n'''
new_test = '''        before = old\n        after = hydrate_s3(new)\n        stable_keys = (\n            "observation_id",\n            "function",\n            "benchmark_id",\n            "benchmark_fit",\n            "evidence_source_class",\n            "boundary_class",\n            "canonical_harness_id",\n            "canonical_system_eligible",\n            "system_compatibility",\n            "canonical_review_revision",\n            "benchmark_artifact_revision",\n            "result_artifact",\n            "result_id",\n            "result_started_at",\n            "embedded_run_git_sha",\n            "embedded_run_git_sha_publicly_resolvable_at_review",\n            "scenario_count",\n            "provider",\n            "provider_configuration",\n            "comparison_class",\n            "held_constant",\n            "primary_sources",\n            "raw_observation_ref",\n        )\n        for key in stable_keys:\n            self.assertEqual(after[key], before[key], key)\n        self.assertEqual(new["vsm_interpretation"], before["vsm_interpretation"])\n        self.assertIn("HeuristicRouter-only", after["treatment"])\n        self.assertIn("six retry scenarios", after["scope_note"])\n        self.assertIn("committed result artifact", after["provenance_limitation"])\n        self.assertEqual(\n            set(new),\n            {\n                "observation_id", "function", "benchmark_id", "benchmark_fit",\n                "boundary_class", "canonical_harness_id", "canonical_system_eligible",\n                "vsm_interpretation", "raw_observation_ref",\n            },\n        )\n'''
if old_test not in text:
    raise SystemExit("#815 MAO regression test anchor drift")
path.write_text(text.replace(old_test, new_test, 1), encoding="utf-8")

print("patched legacy tests for neutral evidence ownership contract")
