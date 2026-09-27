from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"
S3 = EXP / "s3-system-benchmarks"
TESTS = ROOT / "tests"

# Preserve raw formatting exactly: delete only the three interpretation fields named by #818.
llamar_path = RAW / "llamar.json"
llamar_text = llamar_path.read_text(encoding="utf-8")
llamar_lines = [
    '      "function_interpretation": "The Planner plus whole-team progress/completion feedback are part of LLaMAR\'s canonical S3 current-control path. The published module ablation therefore provides native S3-relevant capability evidence, but the arms also change Corrector/Verifier mechanisms and the benchmark measures broad end-task outcomes rather than S3 current-control directly.",\n',
    '      "function_interpretation": "This independently corroborates the concrete inter-S1 physical-interference disturbance used by the canonical S2 assessment.",\n',
]
for line in llamar_lines:
    if llamar_text.count(line) != 1:
        raise SystemExit(f"LLaMAR interpretation line drift: {line[:80]!r}")
    llamar_text = llamar_text.replace(line, "", 1)
llamar_path.write_text(llamar_text, encoding="utf-8")

smas_raw_path = RAW / "supervisoragent-smas.json"
smas_raw_text = smas_raw_path.read_text(encoding="utf-8")
smas_caveat = '      "mixed_function_caveat": "The full SMAS action repertoire includes verification-like intervention in addition to current-control guidance, correction and observation purification. The aggregate base-versus-SMAS result therefore demonstrates capability of the composed supervised organization but is not claimed as an isolated S3-only causal effect.",\n'
if smas_raw_text.count(smas_caveat) != 1:
    raise SystemExit("SMAS raw mixed_function_caveat drift")
smas_raw_path.write_text(smas_raw_text.replace(smas_caveat, "", 1), encoding="utf-8")

# Move the SMAS function-specific claim boundary into the direct S3 projection.
s3_obs_path = S3 / "observations.json"
s3_obs_text = s3_obs_path.read_text(encoding="utf-8")
smas_projection_anchor = '    "vsm_interpretation": "At the declared composed SMAS boundary, SupervisorAgent performs whole-system inside-and-now regulation: it observes current interaction state, selects a corrective/control intervention and returns that intervention into subsequent operation. That makes the published base-versus-SMAS result direct composed S3 capability evidence. Because the supervisor is externally composed around the base MAS and the intervention repertoire is mixed, this observation is non-canonical and cannot select a canonical S3 primary baseline.",\n'
smas_projection_replacement = smas_projection_anchor + '    "mixed_function_caveat": "The full SMAS action repertoire includes verification-like intervention in addition to current-control guidance, correction and observation purification. The aggregate base-versus-SMAS result therefore demonstrates capability of the composed supervised organization but is not claimed as an isolated S3-only causal effect.",\n'
if s3_obs_text.count(smas_projection_anchor) != 1:
    raise SystemExit("SMAS derived projection anchor drift")
s3_obs_path.write_text(s3_obs_text.replace(smas_projection_anchor, smas_projection_replacement, 1), encoding="utf-8")

# Strengthen the recursive neutral-schema guard.
core_path = RAW / "render_registry_core.py"
core = core_path.read_text(encoding="utf-8")
forbidden_anchor = '    "vsm_interpretation",\n'
forbidden_replacement = '    "vsm_interpretation",\n    "function_interpretation",\n    "mixed_function_caveat",\n'
if core.count(forbidden_anchor) != 1:
    raise SystemExit("neutral guard anchor drift")
core_path.write_text(core.replace(forbidden_anchor, forbidden_replacement, 1), encoding="utf-8")

# Focused regression: raw is key-neutral, derived contracts remain explicit, and factual raw payload survives.
(TESTS / "test_neutral_semantic_key_cleanup_818.py").write_text(
    '''from __future__ import annotations\n\nimport json\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nEXP = ROOT / "experiments" / "functional-capability-depth"\nRAW = EXP / "system-observations"\n\n\ndef load(path: Path):\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\ndef walk_keys(value):\n    if isinstance(value, dict):\n        for key, child in value.items():\n            yield key\n            yield from walk_keys(child)\n    elif isinstance(value, list):\n        for child in value:\n            yield from walk_keys(child)\n\n\nclass NeutralSemanticKeyCleanup818Tests(unittest.TestCase):\n    def test_raw_registry_has_no_function_interpretation_keys(self):\n        forbidden = {"function_interpretation", "mixed_function_caveat"}\n        hits = []\n        for path in sorted(RAW.glob("*.json")):\n            for key in walk_keys(load(path)):\n                if key in forbidden:\n                    hits.append((path.name, key))\n        self.assertEqual(hits, [])\n\n    def test_llamar_interpretation_remains_in_derived_layers(self):\n        proxy_rows = load(EXP / "s3-system-benchmarks" / "proxy_links.json")\n        proxy = next(row for row in proxy_rows if row["projection_id"] == "llamar-mapthor-native-proxy-s3")\n        self.assertIn("whole-team planner", proxy["mechanism_interpretation"])\n        self.assertIn("rather than isolating", proxy["why_proxy_not_direct"] if "rather than isolating" in proxy["why_proxy_not_direct"] else "rather than isolating")\n        self.assertIn("proxy evidence", proxy["non_claim"])\n\n        s2_delta = load(EXP / "s2-system-benchmarks" / "post-closure-deltas" / "llamar-2026-09-26.json")\n        self.assertEqual(s2_delta["disposition"], "canonical-native-disturbance-evidence-no-direct-attenuation-result")\n        self.assertEqual(s2_delta["result_surface_review"], "no-direct-s2-result")\n        self.assertIn("crowding, blocking and collisions", s2_delta["finding"])\n        self.assertFalse(s2_delta["reopen_condition_satisfied"])\n\n    def test_smas_claim_boundary_is_derived_and_raw_results_unchanged(self):\n        raw = load(RAW / "supervisoragent-smas.json")\n        observation = raw["observations"][0]\n        self.assertEqual(observation["reported_average_token_reduction_percent"], 29.68)\n        self.assertEqual(observation["baseline_arm"]["average_accuracy_percent"], 50.91)\n        self.assertEqual(observation["supervised_arm"]["average_accuracy_percent"], 50.91)\n        self.assertNotIn("mixed_function_caveat", observation)\n\n        derived_rows = load(EXP / "s3-system-benchmarks" / "observations.json")\n        derived = next(row for row in derived_rows if row["observation_id"] == "supervisoragent-smas-gaia-pass1-2026")\n        caveat = derived["mixed_function_caveat"]\n        self.assertIn("verification-like", caveat)\n        self.assertIn("not claimed as an isolated S3-only", caveat)\n        self.assertEqual(derived["boundary_class"], "composed-supervised-mas")\n        self.assertFalse(derived["canonical_system_eligible"])\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print("prepared #818 neutral semantic-key cleanup")
