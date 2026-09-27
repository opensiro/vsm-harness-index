from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
S3 = EXP / "s3-system-benchmarks"
TESTS = ROOT / "tests"

S2_EXPECTED = {
    "autogen-magentic-one-native-proxy-s2": {
        "system_compatibility": "native-system",
        "revision_relation": "historical-first-party-lineage-not-current-review-ref",
    },
    "squad-marble-native-proxy-s2": {
        "system_compatibility": "native-system",
        "revision_relation": "historical-first-party-lineage-not-current-review-ref",
    },
}
S3_EXPECTED = {
    "autogen-magentic-one-native-proxy-s3": {
        "system_compatibility": "native-system",
        "revision_relation": "historical-first-party-lineage-not-current-review-ref",
    },
    "llamar-mapthor-native-proxy-s3": {
        "system_compatibility": "native-system",
        "revision_relation": "first-party-published-artifacts-co-located-at-current-review-ref-run-revision-unknown",
    },
}


def normalize_proxy_file(path: Path, expected: dict[str, dict[str, str]]) -> None:
    rows = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise SystemExit(f"{path}: expected a list")
    actual_ids = {row.get("projection_id") for row in rows if isinstance(row, dict)}
    if actual_ids != set(expected):
        raise SystemExit(f"{path}: projection set drift: {sorted(actual_ids)}")
    for row in rows:
        pid = row["projection_id"]
        for key, value in expected[pid].items():
            if row.get(key) != value:
                raise SystemExit(f"{path}:{pid}: pre-cleanup {key} drift: {row.get(key)!r}")
            del row[key]
    path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


normalize_proxy_file(S2 / "proxy_links.json", S2_EXPECTED)
normalize_proxy_file(S3 / "proxy_links.json", S3_EXPECTED)

# S2: hydrate neutral-owned record metadata before validating proxy semantics.
s2_validate = S2 / "validate.py"
s2_text = s2_validate.read_text(encoding="utf-8")
s2_constants = '''EXPECTED_PROXY_PROJECTIONS = {\n    "autogen-magentic-one-native-proxy-s2": "autogen-agentchat",\n    "squad-marble-native-proxy-s2": "squad",\n}\n'''
s2_constants_new = s2_constants + '''EXPECTED_PROXY_RAW_METADATA = {\n    "autogen-magentic-one-native-proxy-s2": {\n        "system_compatibility": "native-system",\n        "revision_relation": "historical-first-party-lineage-not-current-review-ref",\n    },\n    "squad-marble-native-proxy-s2": {\n        "system_compatibility": "native-system",\n        "revision_relation": "historical-first-party-lineage-not-current-review-ref",\n    },\n}\n'''
if s2_constants not in s2_text:
    raise SystemExit("S2 expected-proxy constant anchor drift")
s2_text = s2_text.replace(s2_constants, s2_constants_new, 1)

s2_helper_anchor = '''def validate_proxy_links(coverage: dict, by_id: dict[str, dict]) -> None:\n'''
s2_helper = '''def hydrate_proxy_projection(projection: dict, raw_record: dict) -> dict:\n    projection_id = projection.get("projection_id")\n    effective = dict(projection)\n    published = raw_record.get("published_implementation")\n    if not isinstance(published, dict):\n        fail(f"{projection_id}: neutral raw record missing published_implementation")\n    raw_metadata = {\n        "system_compatibility": published.get("system_compatibility"),\n        "revision_relation": published.get("canonical_revision_match"),\n    }\n    for key, value in raw_metadata.items():\n        if key in projection:\n            fail(f"{projection_id}: proxy projection duplicates neutral-owned {key}")\n        if not isinstance(value, str) or not value:\n            fail(f"{projection_id}: neutral raw record missing {key}")\n        effective[key] = value\n    return effective\n\n\n''' + s2_helper_anchor
if s2_helper_anchor not in s2_text:
    raise SystemExit("S2 validate_proxy_links anchor drift")
s2_text = s2_text.replace(s2_helper_anchor, s2_helper, 1)

s2_local_check = '''        if projection.get("function") != "S2" or projection.get("benchmark_fit") != "proxy":\n            fail(f"{projection_id}: proxy semantics drift")\n        if projection.get("system_compatibility") != "native-system":\n            fail(f"{projection_id}: proxy projection must remain native-system")\n\n'''
s2_local_check_new = '''        if projection.get("function") != "S2" or projection.get("benchmark_fit") != "proxy":\n            fail(f"{projection_id}: proxy semantics drift")\n\n'''
if s2_local_check not in s2_text:
    raise SystemExit("S2 local compatibility check anchor drift")
s2_text = s2_text.replace(s2_local_check, s2_local_check_new, 1)

s2_raw_anchor = '''        raw = json.loads(raw_path.read_text(encoding="utf-8"))\n        if raw.get("canonical_harness_id") != harness_id:\n            fail(f"{projection_id}: raw record canonical_harness_id mismatch")\n        raw_ids = {\n'''
s2_raw_new = '''        raw = json.loads(raw_path.read_text(encoding="utf-8"))\n        if raw.get("canonical_harness_id") != harness_id:\n            fail(f"{projection_id}: raw record canonical_harness_id mismatch")\n        effective_projection = hydrate_proxy_projection(projection, raw)\n        actual_raw_metadata = {\n            "system_compatibility": effective_projection.get("system_compatibility"),\n            "revision_relation": effective_projection.get("revision_relation"),\n        }\n        if actual_raw_metadata != EXPECTED_PROXY_RAW_METADATA.get(projection_id):\n            fail(f"{projection_id}: neutral raw proxy metadata drift: {actual_raw_metadata!r}")\n        raw_ids = {\n'''
if s2_raw_anchor not in s2_text:
    raise SystemExit("S2 raw proxy validation anchor drift")
s2_text = s2_text.replace(s2_raw_anchor, s2_raw_new, 1)
s2_validate.write_text(s2_text, encoding="utf-8")

# S3: add the missing proxy_links validation and hydrate the same neutral-owned metadata.
s3_validate = S3 / "validate.py"
s3_text = s3_validate.read_text(encoding="utf-8")
s3_path_anchor = '''COVERAGE = HERE / "coverage.json"\nOBSERVATIONS = HERE / "observations.json"\nBENCHMARK_MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"\n'''
s3_path_new = '''COVERAGE = HERE / "coverage.json"\nOBSERVATIONS = HERE / "observations.json"\nPROXY_LINKS = HERE / "proxy_links.json"\nBENCHMARK_MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"\n'''
if s3_path_anchor not in s3_text:
    raise SystemExit("S3 path constant anchor drift")
s3_text = s3_text.replace(s3_path_anchor, s3_path_new, 1)

s3_constants_anchor = '''SYSTEM_COMPATIBILITY = {\n    "native-system",\n    "adapter-preserved",\n    "benchmark-scaffolded",\n    "unclear",\n}\nDIRECT_S3_BENCHMARKS = {\n'''
s3_constants_new = '''SYSTEM_COMPATIBILITY = {\n    "native-system",\n    "adapter-preserved",\n    "benchmark-scaffolded",\n    "unclear",\n}\nEXPECTED_PROXY_PROJECTIONS = {\n    "autogen-magentic-one-native-proxy-s3": "autogen-agentchat",\n    "llamar-mapthor-native-proxy-s3": "llamar",\n}\nEXPECTED_PROXY_RAW_METADATA = {\n    "autogen-magentic-one-native-proxy-s3": {\n        "system_compatibility": "native-system",\n        "revision_relation": "historical-first-party-lineage-not-current-review-ref",\n    },\n    "llamar-mapthor-native-proxy-s3": {\n        "system_compatibility": "native-system",\n        "revision_relation": "first-party-published-artifacts-co-located-at-current-review-ref-run-revision-unknown",\n    },\n}\nDIRECT_S3_BENCHMARKS = {\n'''
if s3_constants_anchor not in s3_text:
    raise SystemExit("S3 constants anchor drift")
s3_text = s3_text.replace(s3_constants_anchor, s3_constants_new, 1)

s3_main_anchor = '''def main() -> None:\n'''
s3_proxy_validation = '''def hydrate_proxy_projection(projection: dict, raw_record: dict) -> dict:\n    projection_id = projection.get("projection_id")\n    effective = dict(projection)\n    published = raw_record.get("published_implementation")\n    if not isinstance(published, dict):\n        fail(f"{projection_id}: neutral raw record missing published_implementation")\n    raw_metadata = {\n        "system_compatibility": published.get("system_compatibility"),\n        "revision_relation": published.get("canonical_revision_match"),\n    }\n    for key, value in raw_metadata.items():\n        if key in projection:\n            fail(f"{projection_id}: proxy projection duplicates neutral-owned {key}")\n        if not isinstance(value, str) or not value:\n            fail(f"{projection_id}: neutral raw record missing {key}")\n        effective[key] = value\n    return effective\n\n\ndef validate_proxy_links(coverage: dict, by_id: dict[str, dict]) -> None:\n    proxy_links = json.loads(PROXY_LINKS.read_text(encoding="utf-8"))\n    if not isinstance(proxy_links, list):\n        fail("proxy_links.json must contain a list")\n    if coverage.get("proxy_projection_count") != len(proxy_links):\n        fail("proxy_projection_count does not match proxy_links.json")\n\n    projections: dict[str, dict] = {}\n    for projection in proxy_links:\n        if not isinstance(projection, dict):\n            fail("every S3 proxy projection must be an object")\n        projection_id = projection.get("projection_id")\n        if not isinstance(projection_id, str) or not projection_id:\n            fail("every S3 proxy projection requires projection_id")\n        if projection_id in projections:\n            fail(f"duplicate S3 proxy projection_id: {projection_id}")\n        projections[projection_id] = projection\n\n        if projection.get("function") != "S3" or projection.get("benchmark_fit") != "proxy":\n            fail(f"{projection_id}: proxy semantics drift")\n        harness_id = projection.get("canonical_harness_id")\n        if harness_id != EXPECTED_PROXY_PROJECTIONS.get(projection_id):\n            fail(f"{projection_id}: canonical proxy linkage drift")\n        fields = assessment_fields(harness_id)\n        if fields.get("status") != "included":\n            fail(f"{projection_id}: canonical assessment is not included")\n        current_s3 = fields.get("autonomy_s3")\n        if current_s3 in {None, "—", "?"}:\n            fail(f"{projection_id}: canonical system no longer establishes S3")\n        if projection.get("canonical_state_at_review") != current_s3:\n            fail(f"{projection_id}: canonical S3 state drift")\n\n        raw_record = projection.get("raw_record")\n        if not isinstance(raw_record, str) or not raw_record.startswith("../system-observations/"):\n            fail(f"{projection_id}: raw_record must point to shared system-observations")\n        raw_path = (HERE / raw_record).resolve()\n        if raw_path.parent != RAW_OBSERVATIONS.resolve() or not raw_path.is_file():\n            fail(f"{projection_id}: raw observation record missing or outside shared directory")\n        raw = json.loads(raw_path.read_text(encoding="utf-8"))\n        if raw.get("canonical_harness_id") != harness_id:\n            fail(f"{projection_id}: raw record canonical_harness_id mismatch")\n        effective_projection = hydrate_proxy_projection(projection, raw)\n        actual_raw_metadata = {\n            "system_compatibility": effective_projection.get("system_compatibility"),\n            "revision_relation": effective_projection.get("revision_relation"),\n        }\n        if actual_raw_metadata != EXPECTED_PROXY_RAW_METADATA.get(projection_id):\n            fail(f"{projection_id}: neutral raw proxy metadata drift: {actual_raw_metadata!r}")\n\n        raw_ids = {\n            row.get("observation_id")\n            for row in raw.get("observations", [])\n            if isinstance(row, dict)\n        }\n        requested_ids = projection.get("raw_observation_ids")\n        if not isinstance(requested_ids, list) or not requested_ids:\n            fail(f"{projection_id}: raw_observation_ids required")\n        if any(not isinstance(value, str) or not value for value in requested_ids):\n            fail(f"{projection_id}: invalid raw_observation_ids")\n        missing = set(requested_ids) - raw_ids\n        if missing:\n            fail(f"{projection_id}: raw observation ids missing from shared record: {sorted(missing)}")\n\n        case = by_id.get(projection_id)\n        if case is None:\n            fail(f"missing S3 coverage case for proxy projection {projection_id}")\n        if case.get("benchmark_fit") != "proxy" or case.get("coverage_class") != "native-proxy":\n            fail(f"{projection_id}: coverage case proxy semantics drift")\n        if case.get("canonical_harness_id") != harness_id:\n            fail(f"{projection_id}: coverage case canonical linkage drift")\n        if case.get("proxy_projection_ref") != f"proxy_links.json#{projection_id}":\n            fail(f"{projection_id}: coverage proxy_projection_ref drift")\n        if case.get("raw_observation_ref") != raw_record:\n            fail(f"{projection_id}: coverage raw_observation_ref drift")\n        if case.get("system_compatibility") != effective_projection.get("system_compatibility"):\n            fail(f"{projection_id}: coverage/raw system compatibility drift")\n\n    if {key: projections[key].get("canonical_harness_id") for key in projections} != EXPECTED_PROXY_PROJECTIONS:\n        fail("S3 native proxy projection set drift")\n\n\n''' + s3_main_anchor
if s3_main_anchor not in s3_text:
    raise SystemExit("S3 main anchor drift")
s3_text = s3_text.replace(s3_main_anchor, s3_proxy_validation, 1)

s3_call_anchor = '''    missing_cases = REQUIRED_CASE_IDS - seen\n'''
s3_call_new = '''    validate_proxy_links(coverage, by_id)\n\n    missing_cases = REQUIRED_CASE_IDS - seen\n'''
if s3_call_anchor not in s3_text:
    raise SystemExit("S3 proxy validation call anchor drift")
s3_text = s3_text.replace(s3_call_anchor, s3_call_new, 1)
s3_validate.write_text(s3_text, encoding="utf-8")

# Existing LLaMAR test should now assert physical projection minimality; raw metadata is tested below.
llamar_test = TESTS / "test_llamar_capability_evidence_749.py"
llamar_text = llamar_test.read_text(encoding="utf-8")
old_assert = '''        self.assertEqual(projection.get("system_compatibility"), "native-system")\n'''
new_assert = '''        self.assertNotIn("system_compatibility", projection)\n        self.assertNotIn("revision_relation", projection)\n'''
if old_assert not in llamar_text:
    raise SystemExit("LLaMAR proxy assertion anchor drift")
llamar_test.write_text(llamar_text.replace(old_assert, new_assert, 1), encoding="utf-8")

# Regression contract for all four proxy projections.
(TESTS / "test_proxy_projection_neutral_ownership_817.py").write_text(
    '''from __future__ import annotations\n\nimport json\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nEXP = ROOT / "experiments" / "functional-capability-depth"\nRAW = EXP / "system-observations"\n\nEXPECTED = {\n    "S2": {\n        "autogen-magentic-one-native-proxy-s2": ("magentic-one.json", "native-system", "historical-first-party-lineage-not-current-review-ref"),\n        "squad-marble-native-proxy-s2": ("squad.json", "native-system", "historical-first-party-lineage-not-current-review-ref"),\n    },\n    "S3": {\n        "autogen-magentic-one-native-proxy-s3": ("magentic-one.json", "native-system", "historical-first-party-lineage-not-current-review-ref"),\n        "llamar-mapthor-native-proxy-s3": ("llamar.json", "native-system", "first-party-published-artifacts-co-located-at-current-review-ref-run-revision-unknown"),\n    },\n}\n\n\ndef load(path: Path):\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\nclass ProxyProjectionNeutralOwnership817Tests(unittest.TestCase):\n    def test_proxy_projections_are_interpretation_and_linkage_only(self):\n        for function, expected in EXPECTED.items():\n            rows = load(EXP / f"{function.lower()}-system-benchmarks" / "proxy_links.json")\n            by_id = {row["projection_id"]: row for row in rows}\n            self.assertEqual(set(by_id), set(expected))\n            for projection_id, row in by_id.items():\n                self.assertNotIn("system_compatibility", row, projection_id)\n                self.assertNotIn("revision_relation", row, projection_id)\n                self.assertEqual(row["function"], function)\n                self.assertEqual(row["benchmark_fit"], "proxy")\n                self.assertTrue(row["raw_observation_ids"])\n\n    def test_neutral_raw_records_own_proxy_compatibility_and_revision_relation(self):\n        for function, expected in EXPECTED.items():\n            rows = load(EXP / f"{function.lower()}-system-benchmarks" / "proxy_links.json")\n            by_id = {row["projection_id"]: row for row in rows}\n            for projection_id, (filename, compatibility, relation) in expected.items():\n                row = by_id[projection_id]\n                self.assertEqual(row["raw_record"], f"../system-observations/{filename}")\n                raw = load(RAW / filename)\n                published = raw["published_implementation"]\n                self.assertEqual(published["system_compatibility"], compatibility)\n                self.assertEqual(published["canonical_revision_match"], relation)\n                raw_ids = {item["observation_id"] for item in raw["observations"]}\n                self.assertTrue(set(row["raw_observation_ids"]).issubset(raw_ids))\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print("prepared #817 S2/S3 proxy neutral-ownership cleanup")
