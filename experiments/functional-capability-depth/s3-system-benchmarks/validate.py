#!/usr/bin/env python3
"""Validate the experimental S3 benchmark coverage/gap record."""

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
    "proxy-scaffolded",
    "framework-scaffolded",
    "candidate-boundary-unresolved",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
REQUIRED_CASE_IDS = {
    "clawarena-team-direct-scaffolded",
    "loop-back-authority-direct-scaffolded",
    "autogen-magentic-one-native-proxy-s3",
    "enterprise-arena-proxy-scaffolded",
    "astra-cross-framework-wrong-native-s3-path",
    "principalbench-model-orchestrator-proxy",
    "multi-agent-orchestration-native-s3-candidate",
    "orchestrabench-failure-recovery-candidate",
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
    if coverage.get("function") != "S3":
        fail("coverage function must be S3")
    if not isinstance(observations, list):
        fail("observations.json must contain a list")
    if coverage.get("direct_observation_count") != len(observations):
        fail("direct_observation_count does not match observations.json")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    reviewed_direct_s3 = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S3" and entry.get("fit") == "direct"
    }
    if reviewed_direct_s3 != {"clawarena-team", "loop-back-authority"}:
        fail(f"unexpected committed direct-S3 benchmark map: {sorted(reviewed_direct_s3)}")

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
            fail(f"{case_id}: coverage case must remain non-admitted")
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
            if case["coverage_class"] == "native-proxy" and fields.get("autonomy_s3") in {None, "—", "?"}:
                fail(f"{case_id}: native-proxy system does not currently establish S3")

    missing_cases = REQUIRED_CASE_IDS - seen
    if missing_cases:
        fail(f"required S3 search cases missing: {sorted(missing_cases)}")

    loop_back = by_id["loop-back-authority-direct-scaffolded"]
    if loop_back.get("benchmark_fit") != "direct":
        fail("Loop-Back Authority must remain direct S3 at its benchmark-defined boundary")
    if loop_back.get("coverage_class") != "direct-scaffolded":
        fail("Loop-Back Authority coverage class drift")
    if loop_back.get("system_compatibility") != "benchmark-scaffolded":
        fail("Loop-Back Authority must remain benchmark-scaffolded")
    if loop_back.get("canonical_harness_id") is not None:
        fail("Loop-Back Authority must not claim canonical harness ownership")

    # A matched framework benchmark is not sufficient when it bypasses the
    # exact canonical S3 mode. Keep the current positive and negative controls
    # mechanically tied to their canonical assessments so later reassessment
    # forces this coverage interpretation to be revisited.
    astra = by_id["astra-cross-framework-wrong-native-s3-path"]
    inspected = set(astra.get("canonical_harness_ids_inspected", []))
    expected_inspected = {"agno", "autogen-agentchat", "crewai", "langgraph"}
    if inspected != expected_inspected:
        fail("Astra framework-control cohort drift")

    for harness_id in ("agno", "autogen-agentchat"):
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included" or fields.get("autonomy_s3") in {None, "—", "?"}:
            fail(f"Astra positive control {harness_id} no longer establishes S3; review coverage semantics")

    for harness_id in ("crewai", "langgraph"):
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included" or fields.get("autonomy_s3") != "—":
            fail(f"Astra negative control {harness_id} no longer has S3=—; review coverage semantics")

    native_candidate = by_id["multi-agent-orchestration-native-s3-candidate"]
    if native_candidate.get("system_compatibility") != "native-system":
        fail("Multi-Agent Orchestration candidate must remain native-system at its own benchmark boundary")
    if native_candidate.get("canonical_harness_id") is not None:
        fail("Multi-Agent Orchestration candidate must not acquire canonical linkage inside this coverage record")
    if native_candidate.get("benchmark_fit") != "candidate-direct":
        fail("Multi-Agent Orchestration candidate fit drift")

    representative = coverage.get("representative_canonical_s3_systems_inspected")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S3 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative S3 cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"representative {harness_id}: assessment not included")
        if fields.get("autonomy_s3") in {None, "—", "?"}:
            fail(f"representative {harness_id}: current canonical assessment does not establish S3")

    if observations:
        fail("direct S3 observation registry is expected to remain empty")

    print("ok: S3 coverage gap validated")
    print(f"reviewed direct S3 families: {len(reviewed_direct_s3)}")
    print(f"admitted direct observations: {len(observations)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S3 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
