#!/usr/bin/env python3
"""Validate the experimental S2 benchmark coverage/gap record."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COVERAGE = HERE / "coverage.json"
OBSERVATIONS = HERE / "observations.json"
PROXY_LINKS = HERE / "proxy_links.json"
BENCHMARK_MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"
SYSTEM_OBSERVATIONS = HERE.parent / "system-observations"

COVERAGE_CLASSES = {
    "direct-scaffolded",
    "native-proxy",
    "framework-scaffolded",
    "candidate-boundary-unresolved",
    "candidate-no-results",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
EXPECTED_PROXY_PROJECTIONS = {
    "autogen-magentic-one-native-proxy-s2": "autogen-agentchat",
    "squad-marble-native-proxy-s2": "squad",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def assessment_fields(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    if not path.exists():
        fail(f"missing canonical assessment for {harness_id}")
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"assessment {path} has no front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_proxy_links(coverage: dict, by_id: dict[str, dict]) -> None:
    proxy_links = json.loads(PROXY_LINKS.read_text(encoding="utf-8"))
    if not isinstance(proxy_links, list):
        fail("proxy_links.json must contain a list")
    if coverage.get("proxy_projection_count") != len(proxy_links):
        fail("proxy_projection_count does not match proxy_links.json")

    projections: dict[str, dict] = {}
    for projection in proxy_links:
        if not isinstance(projection, dict):
            fail("every S2 proxy projection must be an object")
        projection_id = projection.get("projection_id")
        if not isinstance(projection_id, str) or not projection_id:
            fail("every S2 proxy projection requires projection_id")
        if projection_id in projections:
            fail(f"duplicate S2 proxy projection_id: {projection_id}")
        projections[projection_id] = projection

        if projection.get("function") != "S2":
            fail(f"{projection_id}: function must be S2")
        if projection.get("benchmark_fit") != "proxy":
            fail(f"{projection_id}: benchmark_fit must remain proxy")
        if projection.get("system_compatibility") != "native-system":
            fail(f"{projection_id}: proxy projection must remain native-system")

        harness_id = projection.get("canonical_harness_id")
        if not isinstance(harness_id, str) or not harness_id:
            fail(f"{projection_id}: canonical_harness_id required")
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"{projection_id}: canonical assessment is not included")
        current_s2 = fields.get("autonomy_s2")
        if current_s2 in {None, "—", "?"}:
            fail(f"{projection_id}: canonical system no longer establishes S2")
        if projection.get("canonical_state_at_review") != current_s2:
            fail(
                f"{projection_id}: canonical S2 state drifted from projection "
                f"{projection.get('canonical_state_at_review')!r} to {current_s2!r}"
            )

        raw_record = projection.get("raw_record")
        if not isinstance(raw_record, str) or not raw_record.startswith("../system-observations/"):
            fail(f"{projection_id}: raw_record must point to shared system-observations")
        raw_path = (HERE / raw_record).resolve()
        if raw_path.parent != SYSTEM_OBSERVATIONS.resolve() or not raw_path.exists():
            fail(f"{projection_id}: raw observation record missing or outside shared directory")
        raw = json.loads(raw_path.read_text(encoding="utf-8"))
        if raw.get("canonical_harness_id") != harness_id:
            fail(f"{projection_id}: raw record canonical_harness_id mismatch")
        raw_ids = {
            row.get("observation_id")
            for row in raw.get("observations", [])
            if isinstance(row, dict)
        }
        requested_ids = projection.get("raw_observation_ids")
        if not isinstance(requested_ids, list) or not requested_ids:
            fail(f"{projection_id}: raw_observation_ids required")
        if any(not isinstance(value, str) or not value for value in requested_ids):
            fail(f"{projection_id}: invalid raw_observation_ids")
        missing = set(requested_ids) - raw_ids
        if missing:
            fail(f"{projection_id}: raw observation ids missing from shared record: {sorted(missing)}")

    if {key: projections[key].get("canonical_harness_id") for key in projections} != EXPECTED_PROXY_PROJECTIONS:
        fail("S2 native proxy projection set drift")

    expected_cases = {
        "autogen-magentic-one-native-proxy-s2": "autogen-magentic-one-native-proxy",
        "squad-marble-native-proxy-s2": "squad-marble-native-proxy",
    }
    for projection_id, case_id in expected_cases.items():
        projection = projections[projection_id]
        case = by_id.get(case_id)
        if case is None:
            fail(f"missing coverage case for {projection_id}: {case_id}")
        if case.get("coverage_class") != "native-proxy":
            fail(f"{case_id}: coverage_class must remain native-proxy")
        if case.get("canonical_harness_id") != projection.get("canonical_harness_id"):
            fail(f"{case_id}: canonical linkage differs from proxy projection")
        if case.get("proxy_projection_ref") != f"proxy_links.json#{projection_id}":
            fail(f"{case_id}: proxy_projection_ref drift")
        if case.get("raw_observation_ref") != projection.get("raw_record"):
            fail(f"{case_id}: raw_observation_ref drift")


def main() -> None:
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
    benchmark_map = json.loads(BENCHMARK_MAP.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S2":
        fail("coverage function must be S2")
    if not isinstance(observations, list):
        fail("observations.json must contain a list")
    if coverage.get("direct_observation_count") != len(observations):
        fail("direct_observation_count does not match observations.json")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    reviewed_direct_s2 = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S2" and entry.get("fit") == "direct"
    }
    expected_direct_s2 = {"dpbench", "stale-semantic-coordination"}
    if reviewed_direct_s2 != expected_direct_s2:
        fail(f"unexpected committed direct-S2 benchmark map: {sorted(reviewed_direct_s2)}")
    if coverage.get("direct_benchmark_family_count") != len(reviewed_direct_s2):
        fail("direct_benchmark_family_count does not match reviewed direct-S2 map")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")

    seen: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in seen:
            fail(f"duplicate case_id: {case_id}")
        seen.add(case_id)
        by_id[case_id] = case

        if case.get("coverage_class") not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if case.get("admitted") is not False:
            fail(f"{case_id}: first-pass coverage case must remain non-admitted")
        if not isinstance(case.get("finding"), str) or len(case["finding"].strip()) < 40:
            fail(f"{case_id}: explicit finding required")

        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources:
            fail(f"{case_id}: primary_sources required")
        if any(not valid_https(source) for source in sources):
            fail(f"{case_id}: all primary_sources must be https URLs")

        harness_id = case.get("canonical_harness_id")
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment is not included")

            if harness_id == "langgraph":
                if fields.get("autonomy_s2") != "—":
                    fail("LangGraph negative control no longer has S2=—; review coverage semantics")
            elif case["coverage_class"] == "native-proxy":
                if fields.get("autonomy_s2") in {None, "—", "?"}:
                    fail(f"{case_id}: native-proxy system does not currently establish S2")

    stale = by_id.get("stale-semantic-coordination-direct-scaffolded")
    if stale is None:
        fail("missing STALE direct-S2 coverage case")
    if stale.get("benchmark_fit") != "direct":
        fail("STALE must remain direct S2 at its benchmark-defined boundary")
    if stale.get("coverage_class") != "direct-scaffolded":
        fail("STALE coverage class drift")
    if stale.get("system_compatibility") != "benchmark-scaffolded":
        fail("STALE must remain benchmark-scaffolded")
    if stale.get("canonical_harness_id") is not None:
        fail("STALE must not claim canonical harness S2 ownership")

    validate_proxy_links(coverage, by_id)

    representative = coverage.get("representative_canonical_s2_systems_inspected")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S2 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative S2 cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"representative {harness_id}: assessment not included")
        if fields.get("autonomy_s2") in {None, "—", "?"}:
            fail(f"representative {harness_id}: current canonical assessment does not establish S2")

    if observations:
        fail("first-pass direct S2 observation registry is expected to remain empty")

    print("ok: S2 coverage gap validated")
    print(f"reviewed direct S2 families: {len(reviewed_direct_s2)}")
    print(f"admitted direct observations: {len(observations)}")
    print(f"native proxy projections: {coverage.get('proxy_projection_count')}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S2 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
