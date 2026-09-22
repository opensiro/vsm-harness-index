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
BENCHMARK_MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"

COVERAGE_CLASSES = {
    "direct-scaffolded",
    "native-proxy",
    "framework-scaffolded",
    "candidate-boundary-unresolved",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
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
    if reviewed_direct_s2 != {"dpbench"}:
        fail(f"unexpected committed direct-S2 benchmark map: {sorted(reviewed_direct_s2)}")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")

    seen: set[str] = set()
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in seen:
            fail(f"duplicate case_id: {case_id}")
        seen.add(case_id)

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
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S2 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
