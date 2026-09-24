#!/usr/bin/env python3
"""Validate the experimental direct-S3 benchmark coverage layer."""

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
    "direct-native",
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
DIRECT_S3_BENCHMARKS = {
    "clawarena-team",
    "loop-back-authority",
    "multi-agent-orchestration-supervisor-ablation",
}
REQUIRED_CASE_IDS = {
    "clawarena-team-direct-scaffolded",
    "loop-back-authority-direct-scaffolded",
    "autogen-magentic-one-native-proxy-s3",
    "enterprise-arena-proxy-scaffolded",
    "astra-cross-framework-wrong-native-s3-path",
    "principalbench-model-orchestrator-proxy",
    "multi-agent-orchestration-native-s3-direct",
    "orchestrabench-failure-recovery-candidate",
}
DIRECT_OBSERVATION_ID = "multi-agent-orchestration-supervisor-ablation-2026-08"
DIRECT_CANONICAL_HARNESS = "multi-agent-orchestration"
DIRECT_REVIEW_REF = "e6c34462af045d7e53d383103346362351c96353"
UNRESOLVED_RUN_SHA = "aed23ddd56c9ff6978a72140160634ced31ecf74"
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


def validate_direct_observation(observation: dict) -> None:
    if observation.get("observation_id") != DIRECT_OBSERVATION_ID:
        fail("unexpected direct S3 observation_id")
    if observation.get("function") != "S3":
        fail("direct observation function must be S3")
    if observation.get("benchmark_id") != "multi-agent-orchestration-supervisor-ablation":
        fail("direct observation benchmark_id drift")
    if observation.get("benchmark_fit") != "direct":
        fail("direct observation benchmark_fit must be direct")
    if observation.get("evidence_source_class") != "first-party-reported":
        fail("Multi-Agent Orchestration result must remain first-party-reported")
    if observation.get("boundary_class") != "canonical-native-system":
        fail("direct observation must retain canonical-native-system boundary")
    if observation.get("canonical_harness_id") != DIRECT_CANONICAL_HARNESS:
        fail("direct observation canonical_harness_id drift")
    if observation.get("canonical_system_eligible") is not True:
        fail("direct observation must remain canonical-system eligible")
    if observation.get("system_compatibility") != "native-system":
        fail("direct observation must remain native-system")
    if observation.get("canonical_review_revision") != DIRECT_REVIEW_REF:
        fail("direct observation canonical review ref drift")
    if observation.get("benchmark_artifact_revision") != DIRECT_REVIEW_REF:
        fail("benchmark artifact revision must remain the pinned canonical review ref")

    fields = assessment_fields(DIRECT_CANONICAL_HARNESS)
    if fields.get("status") != "included":
        fail("Multi-Agent Orchestration canonical assessment must remain included")
    if fields.get("autonomy_s3") != "A":
        fail("Multi-Agent Orchestration no longer establishes canonical S3=A")
    if fields.get("review_ref") != DIRECT_REVIEW_REF:
        fail("Multi-Agent Orchestration assessment review_ref drift")

    if observation.get("scenario_count") != 54:
        fail("published scenario_count drift")
    if observation.get("provider") != "MockProvider":
        fail("published deterministic provider identity drift")
    if observation.get("comparison_class") != "within-system-controlled-ablation":
        fail("direct observation comparison class drift")

    baseline = observation.get("baseline_arm")
    supervisor = observation.get("supervisor_arm")
    if not isinstance(baseline, dict) or not isinstance(supervisor, dict):
        fail("direct observation requires baseline_arm and supervisor_arm")

    expected_baseline = {
        "uses_supervisor": False,
        "retry_enabled": False,
        "parallelism_enabled": False,
        "scenarios_passed": 11,
        "scenarios_run": 54,
        "completion_rate": 0.204,
        "routing_accuracy": 0.566667,
        "total_tokens": 14669,
    }
    expected_supervisor = {
        "uses_supervisor": True,
        "retry_enabled": False,
        "parallelism_enabled": False,
        "scenarios_passed": 48,
        "scenarios_run": 54,
        "completion_rate": 0.889,
        "routing_accuracy": 1.0,
        "total_tokens": 23784,
    }
    if baseline != expected_baseline:
        fail(f"published baseline arm drift: {baseline!r}")
    if supervisor != expected_supervisor:
        fail(f"published supervisor arm drift: {supervisor!r}")

    if observation.get("reported_completion_gain_percentage_points") != 68.5:
        fail("published completion gain drift")
    if observation.get("reported_routing_accuracy_gain_percentage_points") != 43.3333:
        fail("published routing-accuracy gain drift")

    if observation.get("embedded_run_git_sha") != UNRESOLVED_RUN_SHA:
        fail("embedded result git_sha drift")
    if observation.get("embedded_run_git_sha_publicly_resolvable_at_review") is not False:
        fail("unresolved embedded run SHA caveat must remain explicit")
    limitation = observation.get("provenance_limitation")
    if not isinstance(limitation, str) or UNRESOLVED_RUN_SHA not in limitation:
        fail("provenance limitation must retain the unresolved run SHA")
    if "not relabeled as an independently reproduced run" not in limitation:
        fail("provenance limitation must preserve non-reproduction boundary")

    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 3 or any(not valid_https(s) for s in sources):
        fail("direct observation requires pinned HTTPS benchmark/doc/result sources")
    if not any("eval_c760d1ff9d464cbfa89e.json" in s for s in sources):
        fail("direct observation must retain immutable committed result-artifact source")
    if not any("evaluation/arms.py" in s for s in sources):
        fail("direct observation must retain first-party arm-definition source")


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
    if reviewed_direct_s3 != DIRECT_S3_BENCHMARKS:
        fail(f"unexpected committed direct-S3 benchmark map: {sorted(reviewed_direct_s3)}")
    if coverage.get("direct_benchmark_family_count") != len(reviewed_direct_s3):
        fail("direct_benchmark_family_count does not match reviewed direct-S3 map")

    if len(observations) != 1:
        fail("expected exactly one canonical direct S3 observation")
    validate_direct_observation(observations[0])

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

        coverage_class = case.get("coverage_class")
        if coverage_class not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if coverage_class == "direct-native":
            if case.get("admitted") is not True:
                fail(f"{case_id}: direct-native coverage must be admitted")
        elif case.get("admitted") is not False:
            fail(f"{case_id}: non-direct-native coverage case must remain non-admitted")
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
            if coverage_class in {"native-proxy", "direct-native"} and fields.get("autonomy_s3") in {None, "—", "?"}:
                fail(f"{case_id}: canonical system does not currently establish S3")

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

    direct_native = by_id["multi-agent-orchestration-native-s3-direct"]
    if direct_native.get("benchmark_fit") != "direct":
        fail("Multi-Agent Orchestration native S3 case must remain direct")
    if direct_native.get("coverage_class") != "direct-native":
        fail("Multi-Agent Orchestration native S3 coverage class drift")
    if direct_native.get("system_compatibility") != "native-system":
        fail("Multi-Agent Orchestration direct S3 case must remain native-system")
    if direct_native.get("canonical_harness_id") != DIRECT_CANONICAL_HARNESS:
        fail("Multi-Agent Orchestration direct S3 canonical linkage drift")
    if direct_native.get("observation_ref") != f"observations.json#{DIRECT_OBSERVATION_ID}":
        fail("Multi-Agent Orchestration direct S3 observation_ref drift")

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

    representative = coverage.get("representative_canonical_s3_systems_inspected")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S3 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative S3 cohort")
    if DIRECT_CANONICAL_HARNESS not in representative:
        fail("direct canonical S3 system missing from representative cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"representative {harness_id}: assessment not included")
        if fields.get("autonomy_s3") in {None, "—", "?"}:
            fail(f"representative {harness_id}: current canonical assessment does not establish S3")

    print("ok: S3 coverage validated")
    print(f"reviewed direct S3 families: {len(reviewed_direct_s3)}")
    print(f"canonical direct observations: {len(observations)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S3 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
