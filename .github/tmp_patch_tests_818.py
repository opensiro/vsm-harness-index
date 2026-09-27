from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"

# The SMAS claim-boundary caveat is now correctly owned by the S3 projection.
path = TESTS / "test_s3_neutral_registry_migration_807.py"
text = path.read_text(encoding="utf-8")
old = 'DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}\n'
new = 'DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","mixed_function_caveat","raw_observation_ref"}\n'
if text.count(old) != 1:
    raise SystemExit("S3 migration test DERIVED_ALLOWED anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

# Tighten the new LLaMAR regression; require the actual proxy rationale rather than a vacuous fallback.
path = TESTS / "test_neutral_semantic_key_cleanup_818.py"
text = path.read_text(encoding="utf-8")
old = '        self.assertIn("rather than isolating", proxy["why_proxy_not_direct"] if "rather than isolating" in proxy["why_proxy_not_direct"] else "rather than isolating")\n'
new = '        self.assertIn("rather than isolating", proxy["why_proxy_not_direct"])\n'
if text.count(old) != 1:
    raise SystemExit("#818 LLaMAR regression assertion anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

print("aligned #818 tests with derived S3 ownership")
