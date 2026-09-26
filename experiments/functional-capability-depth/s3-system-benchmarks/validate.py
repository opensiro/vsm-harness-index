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
    "supervisoragent-smas-runtime-control",
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

SMAS_OBSERVATION_ID = "supervisoragent-smas-gaia-pass1-2026"
SMAS_REVIEW_REF = "ab116b557b095ae8d45bdf2d61057ce19519d4ff"

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


def require_canonical_s3(harness_id: str, review_ref: str) -> None:
    fields = assessment_fields(harness_id)
    if fields.get("status") != "included":
        fail(f"{harness_id}: canonical assessment must remain included")
    if fields.get("autonomy_s3") in {None, "—", "?"}:
        fail(f"{harness_id}: canonical assessment no longer establishes S3")
    if fields.get("review_ref") != review_ref:
        fail(f"{harness_id}: canonical review_ref drift")


def validate_mao_observation(observation: dict) -> None:
    if observation.get("observation_id") != MAO_OBSERVATION_ID:
        fail("Multi-Agent Orchestration observation_id drift")
    if observation.get("function") != "S3":
        fail("Multi-Agent Orchestration observation function must be S3")
    if observation.get("benchmark_id") != "multi-agent-orchestration-supervisor-ablation":
        fail("Multi-Agent Orchestration benchmark_id drift")
    if observation.get("benchmark_fit") != "direct":
        fail("Multi-Agent Orchestration benchmark_fit must remain direct")
    if observation.get("evidence_source_class") != "first-party-reported":
        fail("Multi-Agent Orchestration evidence class drift")
    if observation.get("boundary_class") != "canonical-native-system":
        fail("Multi-Agent Orchestration boundary drift")
    if observation.get("canonical_harness_id") != MAO_HARNESS:
        fail("Multi-Agent Orchestration canonical linkage drift")
    if observation.get("canonical_system_eligible") is not True:
        fail("Multi-Agent Orchestration must remain canonical-system eligible")
    if observation.get("system_compatibility") != "native-system":
        fail("Multi-Agent Orchestration system compatibility drift")
    if observation.get("canonical_review_revision") != MAO_REVIEW_REF:
        fail("Multi-Agent Orchestration canonical review ref drift")
    if observation.get("benchmark_artifact_revision") != MAO_REVIEW_REF:
        fail("Multi-Agent Orchestration benchmark artifact ref drift")
    if observation.get("comparison_class") != "within-system-controlled-ablation":
        fail("Multi-Agent Orchestration comparison class drift")

    require_canonical_s3(MAO_HARNESS, MAO_REVIEW_REF)

    if observation.get("scenario_count") != 54 or observation.get("provider") != "MockProvider":
        fail("Multi-Agent Orchestration published scenario/provider metadata drift")

    baseline = observation.get("baseline_arm")
    supervisor = observation.get("supervisor_arm")
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
    if baseline != expected_baseline or supervisor != expected_supervisor:
        fail("Multi-Agent Orchestration published arm data drift")
    if observation.get("reported_completion_gain_percentage_points") != 68.5:
        fail("Multi-Agent Orchestration completion gain drift")
    if observation.get("reported_routing_accuracy_gain_percentage_points") != 43.3333:
        fail("Multi-Agent Orchestration routing gain drift")

    if observation.get("embedded_run_git_sha") != MAO_UNRESOLVED_RUN_SHA:
        fail("Multi-Agent Orchestration embedded run SHA drift")
    if observation.get("embedded_run_git_sha_publicly_resolvable_at_review") is not False:
        fail("Multi-Agent Orchestration unresolved-run caveat drift")
    limitation = observation.get("provenance_limitation")
    if not isinstance(limitation, str) or MAO_UNRESOLVED_RUN_SHA not in limitation:
        fail("Multi-Agent Orchestration provenance limitation lost unresolved SHA")
    if "not relabeled as an independently reproduced run" not in limitation:
        fail("Multi-Agent Orchestration non-reproduction boundary lost")

    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 3 or any(not valid_https(s) for s in sources):
        fail("Multi-Agent Orchestration requires pinned HTTPS sources")
    if not any("eval_c760d1ff9d464cbfa89e.json" in s for s in sources):
        fail("Multi-Agent Orchestration committed result source missing")
    if not any("evaluation/arms.py" in s for s in sources):
        fail("Multi-Agent Orchestration arm-definition source missing")


def validate_omnigent_observation(observation: dict) -> None:
    if observation.get("observation_id") != OMNIGENT_OBSERVATION_ID:
        fail("Omnigent observation_id drift")
    if observation.get("function") != "S3":
        fail("Omnigent observation function must be S3")
    if observation.get("benchmark_id") is not None:
        fail("Omnigent operational history must not create a benchmark family")
    if observation.get("benchmark_fit") != "direct":
        fail("Omnigent recovery must remain direct S3 evidence")
    if observation.get("evidence_source_class") != "first-party-reported":
        fail("Omnigent recovery must remain first-party-reported")
    if observation.get("boundary_class") != "canonical-native-system":
        fail("Omnigent recovery boundary drift")
    if observation.get("canonical_harness_id") != OMNIGENT_HARNESS:
        fail("Omnigent canonical linkage drift")
    if observation.get("canonical_system_eligible") is not True:
        fail("Omnigent recovery must remain canonical-system eligible")
    if observation.get("system_compatibility") != "native-system":
        fail("Omnigent recovery must remain native-system")
    if observation.get("comparison_class") != "descriptive-only":
        fail("Omnigent recovery must remain descriptive-only")

    if observation.get("canonical_review_revision") != OMNIGENT_REVIEW_REF:
        fail("Omnigent canonical review ref drift")
    if observation.get("observation_revision") != OMNIGENT_OBSERVATION_REF:
        fail("Omnigent observation revision drift")
    if observation.get("manual_validation_revision") != OMNIGENT_MANUAL_REF:
        fail("Omnigent manual validation ref drift")
    if observation.get("revision_relation") != "post-assessment-descendant":
        fail("Omnigent temporal relation must remain post-assessment-descendant")
    if OMNIGENT_REVIEW_REF == OMNIGENT_OBSERVATION_REF:
        fail("Omnigent observation must not be relabeled as assessment-ref evidence")

    require_canonical_s3(OMNIGENT_HARNESS, OMNIGENT_REVIEW_REF)

    if observation.get("upstream_issue_number") != 4838:
        fail("Omnigent upstream issue drift")
    if observation.get("upstream_pull_request_number") != 7662:
        fail("Omnigent upstream PR drift")

    witness = observation.get("reported_operational_witness")
    if not isinstance(witness, dict):
        fail("Omnigent operational witness missing")
    required_true = {
        "parent_runner_interrupted",
        "unfinished_child_resumed_in_original_conversation",
        "finished_child_remained_completed",
        "same_two_child_session_ids",
        "original_dispatch_ids_preserved",
        "original_dispatch_receipts_acknowledged",
    }
    for key in required_true:
        if witness.get(key) is not True:
            fail(f"Omnigent operational witness lost {key}")
    if witness.get("replacement_workers_created") is not False:
        fail("Omnigent recovery must preserve no-replacement-worker witness")

    regressions = observation.get("regression_evidence")
    if not isinstance(regressions, dict):
        fail("Omnigent regression evidence missing")
    if regressions.get("implementation_file") != "omnigent/server/child_session_recovery.py":
        fail("Omnigent recovery implementation path drift")
    if regressions.get("dedicated_test_file") != "tests/server/test_child_session_recovery.py":
        fail("Omnigent dedicated recovery test path drift")
    if regressions.get("targeted_regressions_reported_fail_before_pass_after") is not True:
        fail("Omnigent fail-before/pass-after regression witness lost")

    limitation = observation.get("provenance_limitation")
    if not isinstance(limitation, str):
        fail("Omnigent provenance limitation missing")
    if "not independently reproduced" not in limitation:
        fail("Omnigent first-party provenance boundary lost")
    if "post-assessment descendant" not in limitation:
        fail("Omnigent temporal provenance boundary lost")

    scope_note = observation.get("scope_note")
    if not isinstance(scope_note, str) or "latency benchmark" not in scope_note:
        fail("Omnigent latency benchmark exclusion must remain explicit")

    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(s) for s in sources):
        fail("Omnigent recovery requires issue/PR/implementation/test HTTPS sources")
    required_source_fragments = (
        "/issues/4838",
        "/pull/7662",
        f"/blob/{OMNIGENT_OBSERVATION_REF}/omnigent/server/child_session_recovery.py",
        f"/blob/{OMNIGENT_OBSERVATION_REF}/tests/server/test_child_session_recovery.py",
    )
    for fragment in required_source_fragments:
        if not any(fragment in source for source in sources):
            fail(f"Omnigent primary source missing: {fragment}")

    delta = json.loads(OMNIGENT_DELTA.read_text(encoding="utf-8"))
    if delta.get("tracking_issue") != 693 or delta.get("function") != "S3":
        fail("Omnigent delta record tracking metadata drift")
    if delta.get("canonical_harness_id") != OMNIGENT_HARNESS:
        fail("Omnigent delta canonical harness drift")
    if delta.get("canonical_review_revision") != OMNIGENT_REVIEW_REF:
        fail("Omnigent delta assessment ref drift")
    if delta.get("observation_revision") != OMNIGENT_OBSERVATION_REF:
        fail("Omnigent delta observation ref drift")
    if delta.get("manual_validation_revision") != OMNIGENT_MANUAL_REF:
        fail("Omnigent delta manual validation ref drift")
    if delta.get("revision_relation") != "post-assessment-descendant":
        fail("Omnigent delta temporal relation drift")


def validate_smas_observation(observation: dict) -> None:
    if observation.get("observation_id") != SMAS_OBSERVATION_ID:
        fail("SupervisorAgent / SMAS observation_id drift")
    if observation.get("function") != "S3":
        fail("SupervisorAgent / SMAS observation function must be S3")
    if observation.get("benchmark_id") != "supervisoragent-smas-runtime-control":
        fail("SupervisorAgent / SMAS benchmark_id drift")
    if observation.get("benchmark_fit") != "direct":
        fail("SupervisorAgent / SMAS benchmark_fit must remain direct")
    if observation.get("evidence_source_class") != "first-party-reported":
        fail("SupervisorAgent / SMAS evidence class drift")
    if observation.get("boundary_class") != "composed-supervised-mas":
        fail("SupervisorAgent / SMAS composed boundary drift")
    if observation.get("canonical_harness_id") is not None:
        fail("SupervisorAgent / SMAS must not acquire a canonical harness identity")
    if observation.get("canonical_system_eligible") is not False:
        fail("SupervisorAgent / SMAS must remain ineligible for canonical primary selection")
    if observation.get("system_compatibility") != "benchmark-scaffolded":
        fail("SupervisorAgent / SMAS compatibility drift")
    if observation.get("comparison_class") != "within-base-system-composed-addition":
        fail("SupervisorAgent / SMAS comparison class drift")
    if observation.get("benchmark_artifact_revision") != SMAS_REVIEW_REF:
        fail("SupervisorAgent / SMAS pinned review ref drift")
    if observation.get("model") != "GPT-4.1":
        fail("SupervisorAgent / SMAS published model drift")

    baseline = observation.get("baseline_arm")
    treatment = observation.get("supervised_arm")
    if baseline != {
        "system": "Smolagent",
        "average_accuracy_percent": 50.91,
        "average_tokens_k": 527.76,
    }:
        fail("SupervisorAgent / SMAS baseline result drift")
    if treatment != {
        "system": "Smolagent + SMAS",
        "average_accuracy_percent": 50.91,
        "average_tokens_k": 371.12,
    }:
        fail("SupervisorAgent / SMAS treatment result drift")
    if observation.get("reported_average_token_reduction_percent") != 29.68:
        fail("SupervisorAgent / SMAS reported token reduction drift")

    mixed = observation.get("mixed_function_caveat")
    if not isinstance(mixed, str) or "verification-like" not in mixed or "not claimed as an isolated S3-only" not in mixed:
        fail("SupervisorAgent / SMAS mixed-function caveat lost")
    ownership = observation.get("ownership_caveat")
    if not isinstance(ownership, str) or not all(name in ownership for name in ("Smolagent", "AWorld", "OAgents")):
        fail("SupervisorAgent / SMAS ownership boundary lost")
    limitation = observation.get("provenance_limitation")
    if not isinstance(limitation, str) or "did not execute or reproduce" not in limitation:
        fail("SupervisorAgent / SMAS public-evidence-only boundary lost")

    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(s) for s in sources):
        fail("SupervisorAgent / SMAS requires pinned repository/code/paper HTTPS sources")
    if not any(f"/tree/{SMAS_REVIEW_REF}" in source for source in sources):
        fail("SupervisorAgent / SMAS pinned repository source missing")
    if not any("smolagents_SMAS/src/smolagents/agents.py" in source for source in sources):
        fail("SupervisorAgent / SMAS implementation source missing")
    if not any("openreview.net/forum?id=pzFhtpkabh" in source for source in sources):
        fail("SupervisorAgent / SMAS paper source missing")


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

    by_observation_id = {o.get("observation_id"): o for o in observations if isinstance(o, dict)}
    expected_observations = {MAO_OBSERVATION_ID, OMNIGENT_OBSERVATION_ID, SMAS_OBSERVATION_ID}
    if set(by_observation_id) != expected_observations or len(observations) != 3:
        fail("expected exactly three typed direct S3 observations")
    validate_mao_observation(by_observation_id[MAO_OBSERVATION_ID])
    validate_omnigent_observation(by_observation_id[OMNIGENT_OBSERVATION_ID])
    validate_smas_observation(by_observation_id[SMAS_OBSERVATION_ID])

    canonical_observations = [o for o in observations if o.get("canonical_system_eligible") is True]
    if {o.get("observation_id") for o in canonical_observations} != {MAO_OBSERVATION_ID, OMNIGENT_OBSERVATION_ID}:
        fail("canonical direct S3 observation cohort drift")

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
    if loop_back.get("benchmark_fit") != "direct" or loop_back.get("coverage_class") != "direct-scaffolded":
        fail("Loop-Back Authority direct-scaffolded semantics drift")
    if loop_back.get("system_compatibility") != "benchmark-scaffolded" or loop_back.get("canonical_harness_id") is not None:
        fail("Loop-Back Authority must remain benchmark-scaffolded and non-canonical")

    smas_case = by_id["supervisoragent-smas-direct-composed"]
    if smas_case.get("benchmark_fit") != "direct" or smas_case.get("coverage_class") != "direct-scaffolded":
        fail("SupervisorAgent / SMAS direct-composed semantics drift")
    if smas_case.get("system_compatibility") != "benchmark-scaffolded" or smas_case.get("canonical_harness_id") is not None:
        fail("SupervisorAgent / SMAS must remain composed/non-canonical")
    if smas_case.get("review_ref") != SMAS_REVIEW_REF:
        fail("SupervisorAgent / SMAS coverage review ref drift")
    if smas_case.get("observation_ref") != f"observations.json#{SMAS_OBSERVATION_ID}":
        fail("SupervisorAgent / SMAS observation_ref drift")

    mao_case = by_id["multi-agent-orchestration-native-s3-direct"]
    if mao_case.get("canonical_harness_id") != MAO_HARNESS:
        fail("Multi-Agent Orchestration coverage linkage drift")
    if mao_case.get("observation_ref") != f"observations.json#{MAO_OBSERVATION_ID}":
        fail("Multi-Agent Orchestration observation_ref drift")

    omnigent_case = by_id["omnigent-post-assessment-recovery-direct"]
    if omnigent_case.get("canonical_harness_id") != OMNIGENT_HARNESS:
        fail("Omnigent coverage linkage drift")
    if omnigent_case.get("canonical_review_ref") != OMNIGENT_REVIEW_REF:
        fail("Omnigent coverage canonical review ref drift")
    if omnigent_case.get("observation_revision") != OMNIGENT_OBSERVATION_REF:
        fail("Omnigent coverage observation revision drift")
    if omnigent_case.get("revision_relation") != "post-assessment-descendant":
        fail("Omnigent coverage temporal relation drift")
    if omnigent_case.get("observation_ref") != f"observations.json#{OMNIGENT_OBSERVATION_ID}":
        fail("Omnigent coverage observation_ref drift")
    if omnigent_case.get("delta_record") != "post-closure-deltas/omnigent-post-assessment-recovery.json":
        fail("Omnigent delta-record linkage drift")

    astra = by_id["astra-cross-framework-wrong-native-s3-path"]
    inspected = set(astra.get("canonical_harness_ids_inspected", []))
    expected_inspected = {"agno", "autogen-agentchat", "crewai", "langgraph"}
    if inspected != expected_inspected:
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
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S3 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative S3 cohort")
    for harness_id in (MAO_HARNESS, OMNIGENT_HARNESS):
        if harness_id not in representative:
            fail(f"direct canonical S3 system missing from representative cohort: {harness_id}")
    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"representative {harness_id}: assessment not included")
        if fields.get("autonomy_s3") in {None, "—", "?"}:
            fail(f"representative {harness_id}: current canonical assessment does not establish S3")

    print("ok: S3 coverage validated")
    print(f"reviewed direct S3 families: {len(reviewed_direct_s3)}")
    print(f"direct observations: {len(observations)}")
    print(f"canonical direct observations: {len(canonical_observations)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S3 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
