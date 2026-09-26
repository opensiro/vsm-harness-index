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
OMNIGENT_DELTA = HERE / "post-closure-deltas" / "omnigent-post-assessment-recovery.json"

COVERAGE_CLASSES = {
    "direct-scaffolded",
    "direct-composed",
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
    "supervisoragent-smas-runtime-supervision",
}
REQUIRED_CASE_IDS = {
    "clawarena-team-direct-scaffolded",
    "loop-back-authority-direct-scaffolded",
    "supervisoragent-smas-direct-composed",
    "autogen-magentic-one-native-proxy-s3",
    "enterprise-arena-proxy-scaffolded",
    "astra-cross-framework-wrong-native-s3-path",
    "principalbench-model-orchestrator-proxy",
    "multi-agent-orchestration-native-s3-direct",
    "omnigent-post-assessment-recovery-direct",
    "orchestrabench-failure-recovery-candidate",
    "cadis-native-s3-no-direct-result",
    "awaken-native-s3-no-direct-result",
    "ares-native-s3-no-direct-result",
}

MAO_OBSERVATION_ID = "multi-agent-orchestration-supervisor-ablation-2026-08"
MAO_HARNESS = "multi-agent-orchestration"
MAO_REVIEW_REF = "e6c34462af045d7e53d383103346362351c96353"
MAO_UNRESOLVED_RUN_SHA = "aed23ddd56c9ff6978a72140160634ced31ecf74"

OMNIGENT_OBSERVATION_ID = "omnigent-child-session-recovery-2026-09"
OMNIGENT_HARNESS = "omnigent"
OMNIGENT_REVIEW_REF = "4d963a360e798f076d4fdbd4665e7188e4da05df"
OMNIGENT_OBSERVATION_REF = "d8d07168c05ce1385be19dbd6ea64f4574c8d144"
OMNIGENT_MANUAL_REF = "15477855d289abdcead0399c1e5be7923f7deef7"

SMAS_OBSERVATION_ID = "supervisoragent-smas-gaia-2026"
SMAS_BENCHMARK_ID = "supervisoragent-smas-runtime-supervision"
SMAS_REVIEW_REF = "ab116b557b095ae8d45bdf2d61057ce19519d4ff"

FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


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


def require_canonical_s3(harness_id: str, review_ref: str) -> None:
    fields = assessment_fields(harness_id)
    if fields.get("status") != "included":
        fail(f"{harness_id}: canonical assessment must remain included")
    if fields.get("autonomy_s3") in {None, "—", "?"}:
        fail(f"{harness_id}: canonical assessment no longer establishes S3")
    if fields.get("review_ref") != review_ref:
        fail(f"{harness_id}: canonical review_ref drift")


def require_sources(observation: dict, fragments: tuple[str, ...]) -> None:
    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or not sources or any(not valid_https(source) for source in sources):
        fail(f"{observation.get('observation_id')}: valid primary_sources required")
    for fragment in fragments:
        if not any(fragment in source for source in sources):
            fail(f"{observation.get('observation_id')}: primary source missing {fragment}")


def validate_mao_observation(observation: dict) -> None:
    expected = {
        "observation_id": MAO_OBSERVATION_ID,
        "function": "S3",
        "benchmark_id": "multi-agent-orchestration-supervisor-ablation",
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "canonical-native-system",
        "canonical_harness_id": MAO_HARNESS,
        "canonical_system_eligible": True,
        "system_compatibility": "native-system",
        "canonical_review_revision": MAO_REVIEW_REF,
        "benchmark_artifact_revision": MAO_REVIEW_REF,
        "comparison_class": "within-system-controlled-ablation",
        "scenario_count": 54,
        "provider": "MockProvider",
    }
    for key, value in expected.items():
        if observation.get(key) != value:
            fail(f"Multi-Agent Orchestration {key} drift")
    require_canonical_s3(MAO_HARNESS, MAO_REVIEW_REF)

    baseline = observation.get("baseline_arm")
    supervisor = observation.get("supervisor_arm")
    if not isinstance(baseline, dict) or not isinstance(supervisor, dict):
        fail("Multi-Agent Orchestration arm data missing")
    if (baseline.get("scenarios_passed"), baseline.get("scenarios_run"), baseline.get("routing_accuracy")) != (11, 54, 0.566667):
        fail("Multi-Agent Orchestration baseline arm drift")
    if (supervisor.get("scenarios_passed"), supervisor.get("scenarios_run"), supervisor.get("routing_accuracy")) != (48, 54, 1.0):
        fail("Multi-Agent Orchestration supervisor arm drift")
    for arm in (baseline, supervisor):
        if arm.get("retry_enabled") is not False or arm.get("parallelism_enabled") is not False:
            fail("Multi-Agent Orchestration clean comparison controls drift")

    if observation.get("embedded_run_git_sha") != MAO_UNRESOLVED_RUN_SHA:
        fail("Multi-Agent Orchestration embedded run SHA drift")
    if observation.get("embedded_run_git_sha_publicly_resolvable_at_review") is not False:
        fail("Multi-Agent Orchestration unresolved-run caveat drift")
    limitation = observation.get("provenance_limitation", "")
    if MAO_UNRESOLVED_RUN_SHA not in limitation or "not relabeled as an independently reproduced run" not in limitation:
        fail("Multi-Agent Orchestration provenance limitation drift")
    require_sources(observation, ("eval_c760d1ff9d464cbfa89e.json", "evaluation/arms.py"))


def validate_omnigent_observation(observation: dict) -> None:
    expected = {
        "observation_id": OMNIGENT_OBSERVATION_ID,
        "function": "S3",
        "benchmark_id": None,
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "canonical-native-system",
        "canonical_harness_id": OMNIGENT_HARNESS,
        "canonical_system_eligible": True,
        "system_compatibility": "native-system",
        "comparison_class": "descriptive-only",
        "canonical_review_revision": OMNIGENT_REVIEW_REF,
        "observation_revision": OMNIGENT_OBSERVATION_REF,
        "manual_validation_revision": OMNIGENT_MANUAL_REF,
        "revision_relation": "post-assessment-descendant",
    }
    for key, value in expected.items():
        if observation.get(key) != value:
            fail(f"Omnigent {key} drift")
    require_canonical_s3(OMNIGENT_HARNESS, OMNIGENT_REVIEW_REF)

    witness = observation.get("reported_operational_witness")
    if not isinstance(witness, dict):
        fail("Omnigent operational witness missing")
    for key in {
        "parent_runner_interrupted",
        "unfinished_child_resumed_in_original_conversation",
        "finished_child_remained_completed",
        "same_two_child_session_ids",
        "original_dispatch_ids_preserved",
        "original_dispatch_receipts_acknowledged",
    }:
        if witness.get(key) is not True:
            fail(f"Omnigent operational witness lost {key}")
    if witness.get("replacement_workers_created") is not False:
        fail("Omnigent recovery must preserve no-replacement-worker witness")

    limitation = observation.get("provenance_limitation", "")
    if "not independently reproduced" not in limitation or "post-assessment descendant" not in limitation:
        fail("Omnigent provenance boundary drift")
    require_sources(
        observation,
        (
            "/issues/4838",
            "/pull/7662",
            f"/blob/{OMNIGENT_OBSERVATION_REF}/omnigent/server/child_session_recovery.py",
            f"/blob/{OMNIGENT_OBSERVATION_REF}/tests/server/test_child_session_recovery.py",
        ),
    )

    delta = json.loads(OMNIGENT_DELTA.read_text(encoding="utf-8"))
    if delta.get("tracking_issue") != 693 or delta.get("function") != "S3":
        fail("Omnigent delta tracking metadata drift")
    if delta.get("canonical_harness_id") != OMNIGENT_HARNESS:
        fail("Omnigent delta canonical identity drift")
    if delta.get("canonical_review_revision") != OMNIGENT_REVIEW_REF:
        fail("Omnigent delta assessment ref drift")
    if delta.get("observation_revision") != OMNIGENT_OBSERVATION_REF:
        fail("Omnigent delta observation ref drift")


def validate_smas_observation(observation: dict) -> None:
    expected = {
        "observation_id": SMAS_OBSERVATION_ID,
        "function": "S3",
        "benchmark_id": SMAS_BENCHMARK_ID,
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "composed-supervised-mas",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "benchmark-scaffolded",
        "benchmark_artifact_revision": SMAS_REVIEW_REF,
        "benchmark": "GAIA validation",
        "model": "GPT-4.1",
        "comparison_class": "within-composed-system-controlled-comparison",
        "reported_average_token_reduction_pct": 29.68,
    }
    for key, value in expected.items():
        if observation.get(key) != value:
            fail(f"SupervisorAgent/SMAS {key} drift")

    if observation.get("intervention_actions") != [
        "approve",
        "provide_guidance",
        "correct_observation",
        "run_verification",
    ]:
        fail("SupervisorAgent/SMAS intervention action set drift")

    baseline = observation.get("baseline_arm")
    treatment = observation.get("supervised_arm")
    if baseline != {
        "method": "Smolagent",
        "average_accuracy_pct": 50.91,
        "average_tokens_k": 527.76,
    }:
        fail("SupervisorAgent/SMAS baseline arm drift")
    if treatment != {
        "method": "Smolagent + SMAS",
        "average_accuracy_pct": 50.91,
        "average_tokens_k": 371.12,
    }:
        fail("SupervisorAgent/SMAS treatment arm drift")

    chain = observation.get("functional_chain", "")
    if "runtime supervisor observes current state" not in chain or "intervention returns into current operation" not in chain:
        fail("SupervisorAgent/SMAS functional chain drift")
    caveat = observation.get("mixed_function_caveat", "")
    if "S3-only" not in caveat or "S3*" not in caveat or "run_verification" not in caveat:
        fail("SupervisorAgent/SMAS mixed-function caveat lost")
    boundary = observation.get("underlying_harness_attribution_boundary", "")
    for name in ("Smolagent", "AWorld", "OAgents"):
        if name not in boundary:
            fail(f"SupervisorAgent/SMAS attribution boundary lost {name}")
    provenance = observation.get("provenance_limitation", "")
    if "Opensiro did not execute or reproduce" not in provenance:
        fail("SupervisorAgent/SMAS public-evidence-only provenance boundary lost")
    require_sources(
        observation,
        (
            f"/blob/{SMAS_REVIEW_REF}/README.md",
            f"/blob/{SMAS_REVIEW_REF}/smolagents_SMAS/src/smolagents/agents.py",
            "openreview.net/forum?id=pzFhtpkabh",
        ),
    )


def main() -> None:
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
    benchmark_map = json.loads(BENCHMARK_MAP.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1 or coverage.get("function") != "S3":
        fail("coverage schema/function drift")
    if coverage.get("reviewed_at") != "2026-09-26":
        fail("S3 coverage review date drift")
    if not isinstance(observations, list):
        fail("observations.json must contain a list")
    if coverage.get("direct_observation_count") != len(observations):
        fail("direct_observation_count does not match observations.json")

    if set(coverage.get("coverage_classes", [])) != COVERAGE_CLASSES:
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

    by_observation_id = {row.get("observation_id"): row for row in observations if isinstance(row, dict)}
    expected_observations = {MAO_OBSERVATION_ID, OMNIGENT_OBSERVATION_ID, SMAS_OBSERVATION_ID}
    if set(by_observation_id) != expected_observations or len(observations) != 3:
        fail("expected exactly three typed direct S3 observations")
    validate_mao_observation(by_observation_id[MAO_OBSERVATION_ID])
    validate_omnigent_observation(by_observation_id[OMNIGENT_OBSERVATION_ID])
    validate_smas_observation(by_observation_id[SMAS_OBSERVATION_ID])

    canonical_observations = [row for row in observations if row.get("canonical_system_eligible") is True]
    if {row.get("observation_id") for row in canonical_observations} != {MAO_OBSERVATION_ID, OMNIGENT_OBSERVATION_ID}:
        fail("canonical direct S3 observation set drift")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")
    seen: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id or case_id in seen:
            fail(f"invalid or duplicate case_id: {case_id!r}")
        seen.add(case_id)
        by_id[case_id] = case

        coverage_class = case.get("coverage_class")
        if coverage_class not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if coverage_class in {"direct-native", "direct-composed"}:
            if case.get("admitted") is not True:
                fail(f"{case_id}: admitted direct evidence must remain admitted")
        elif case.get("admitted") is not False:
            fail(f"{case_id}: non-admitted coverage case changed admission state")
        if not isinstance(case.get("finding"), str) or len(case["finding"].strip()) < 40:
            fail(f"{case_id}: explicit finding required")
        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(source) for source in sources):
            fail(f"{case_id}: valid primary_sources required")

        harness_id = case.get("canonical_harness_id")
        if coverage_class == "direct-composed" and harness_id is not None:
            fail(f"{case_id}: direct-composed evidence must not acquire canonical linkage")
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment is not included")
            if coverage_class in {"native-proxy", "direct-native"} and fields.get("autonomy_s3") in {None, "—", "?"}:
                fail(f"{case_id}: canonical system does not currently establish S3")

    missing = REQUIRED_CASE_IDS - seen
    if missing:
        fail(f"required S3 search cases missing: {sorted(missing)}")

    smas_case = by_id["supervisoragent-smas-direct-composed"]
    if smas_case.get("benchmark_fit") != "direct" or smas_case.get("coverage_class") != "direct-composed":
        fail("SupervisorAgent/SMAS coverage semantics drift")
    if smas_case.get("system_compatibility") != "benchmark-scaffolded" or smas_case.get("canonical_harness_id") is not None:
        fail("SupervisorAgent/SMAS must remain composed/non-canonical")
    if smas_case.get("observation_ref") != f"observations.json#{SMAS_OBSERVATION_ID}":
        fail("SupervisorAgent/SMAS observation_ref drift")
    if smas_case.get("review_ref") != SMAS_REVIEW_REF:
        fail("SupervisorAgent/SMAS review ref drift")

    mao_case = by_id["multi-agent-orchestration-native-s3-direct"]
    if mao_case.get("canonical_harness_id") != MAO_HARNESS or mao_case.get("observation_ref") != f"observations.json#{MAO_OBSERVATION_ID}":
        fail("Multi-Agent Orchestration coverage linkage drift")
    omnigent_case = by_id["omnigent-post-assessment-recovery-direct"]
    if omnigent_case.get("canonical_harness_id") != OMNIGENT_HARNESS:
        fail("Omnigent coverage linkage drift")
    if omnigent_case.get("canonical_review_ref") != OMNIGENT_REVIEW_REF or omnigent_case.get("observation_revision") != OMNIGENT_OBSERVATION_REF:
        fail("Omnigent coverage revision drift")
    if omnigent_case.get("observation_ref") != f"observations.json#{OMNIGENT_OBSERVATION_ID}":
        fail("Omnigent coverage observation_ref drift")

    astra = by_id["astra-cross-framework-wrong-native-s3-path"]
    if set(astra.get("canonical_harness_ids_inspected", [])) != {"agno", "autogen-agentchat", "crewai", "langgraph"}:
        fail("Astra framework-control cohort drift")
    for harness_id in ("agno", "autogen-agentchat"):
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included" or fields.get("autonomy_s3") in {None, "—", "?"}:
            fail(f"Astra positive control {harness_id} no longer establishes S3")
    for harness_id in ("crewai", "langgraph"):
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included" or fields.get("autonomy_s3") != "—":
            fail(f"Astra negative control {harness_id} no longer has S3=—")

    representative = coverage.get("representative_canonical_s3_systems_inspected")
    if not isinstance(representative, list) or len(representative) != len(set(representative)):
        fail("representative canonical S3 cohort invalid")
    for harness_id in (MAO_HARNESS, OMNIGENT_HARNESS):
        if harness_id not in representative:
            fail(f"direct canonical S3 system missing from representative cohort: {harness_id}")
    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included" or fields.get("autonomy_s3") in {None, "—", "?"}:
            fail(f"representative {harness_id}: current canonical assessment does not establish S3")

    print("ok: S3 coverage validated")
    print(f"reviewed direct S3 families: {len(reviewed_direct_s3)}")
    print(f"direct observations: {len(observations)}")
    print(f"canonical direct observations: {len(canonical_observations)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S3 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
