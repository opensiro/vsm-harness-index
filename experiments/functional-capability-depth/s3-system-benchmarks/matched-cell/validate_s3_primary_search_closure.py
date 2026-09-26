#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S3 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S3 = HERE.parent
EXPERIMENT = S3.parent
ROOT = EXPERIMENT.parents[1]

CANONICAL_DELTAS = {
    "cadis": ("A(P)", "52c55854b1abbcda82839b7a934cbdb16a69b635", "cadis-native-s3-no-direct-result"),
    "awaken": ("C(P)", "2b0d375004ec8723cf40d8a59c0bb486ebce57e0", "awaken-native-s3-no-direct-result"),
    "ares": ("C(P)", "f03153acace190c555c3721019407a7df47c139f", "ares-native-s3-no-direct-result"),
}

OMNIGENT_REVIEW_REF = "4d963a360e798f076d4fdbd4665e7188e4da05df"
OMNIGENT_OBSERVATION_REF = "d8d07168c05ce1385be19dbd6ea64f4574c8d144"
SMAS_OBSERVATION_ID = "supervisoragent-smas-gaia-pass1-2026"
SMAS_REVIEW_REF = "ab116b557b095ae8d45bdf2d61057ce19519d4ff"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def assessment_fields(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    require(path.exists(), f"missing canonical assessment for {harness_id}")
    text = path.read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"{harness_id}: missing assessment front matter")
    front = text.split("---\n", 2)[1]
    fields: dict[str, str] = {}
    for line in front.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


closure = load(HERE / "s3-primary-search-closure.json")
coverage = load(S3 / "coverage.json")
observations = load(S3 / "observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S3 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S3 closure status drift")
require(closure["tracking_issue"] == 567, "S3 closure tracking issue drift")
require(closure["canonical_delta_review_issue"] == 592, "S3 canonical delta review issue drift")
require(closure["current_state_update_issue"] == 693, "S3 current-state update issue drift")
require(closure["public_evidence_admission_issue"] == 685, "S3 SupervisorAgent admission issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S3 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S3 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S3 closure scope drift")
require(closure["reviewed_at"] == coverage["reviewed_at"], "S3 closure/coverage review date drift")
require(closure["reviewed_at"] == "2026-09-26", "S3 closure review date drift")

expected = closure["evidence_depth"]
require(coverage["direct_benchmark_family_count"] == expected["direct_benchmark_families"], "S3 direct family count drift")
require(coverage["direct_observation_count"] == expected["direct_observations"], "S3 direct observation count drift")
require(len(observations) == expected["direct_observations"], "S3 observation registry/closure count drift")
canonical_observations = [row for row in observations if row.get("canonical_system_eligible") is True]
require(len(canonical_observations) == expected["canonical_direct_observations"], "S3 canonical observation count drift")
require(coverage["proxy_projection_count"] == expected["native_proxy_projections"], "S3 proxy projection count drift")
representative = coverage["representative_canonical_s3_systems_inspected"]
require(
    len(representative) == expected["representative_canonical_s3_systems_inspected"],
    "S3 representative canonical cohort size drift",
)

native = closure["canonical_native_observations"]
require(isinstance(native, list) and len(native) == 2, "S3 closure must retain exactly two canonical native observations")
native_by_harness = {row["harness_id"]: row for row in native}
require(set(native_by_harness) == {"multi-agent-orchestration", "omnigent"}, "S3 canonical observation cohort drift")

mao = native_by_harness["multi-agent-orchestration"]
require(mao["observation_id"] == "multi-agent-orchestration-supervisor-ablation-2026-08", "S3 MAO observation identity drift")
require(mao["comparison_class"] == "within-system-controlled-ablation", "S3 MAO comparison class drift")
require(mao["baseline_passed"] == 11 and mao["supervisor_passed"] == 48, "S3 MAO pass-count drift")
require(mao["task_count"] == 54, "S3 MAO task-count drift")
require(mao["baseline_routing_accuracy"] == 0.567, "S3 MAO baseline routing accuracy drift")
require(mao["supervisor_routing_accuracy"] == 1.0, "S3 MAO supervisor routing accuracy drift")

omnigent = native_by_harness["omnigent"]
require(omnigent["observation_id"] == "omnigent-child-session-recovery-2026-09", "S3 Omnigent observation identity drift")
require(omnigent["comparison_class"] == "descriptive-only", "S3 Omnigent comparison class drift")
require(omnigent["canonical_review_revision"] == OMNIGENT_REVIEW_REF, "S3 Omnigent review ref drift")
require(omnigent["observation_revision"] == OMNIGENT_OBSERVATION_REF, "S3 Omnigent observation ref drift")
require(omnigent["revision_relation"] == "post-assessment-descendant", "S3 Omnigent temporal relation drift")

omnigent_fields = assessment_fields("omnigent")
require(omnigent_fields.get("status") == "included", "Omnigent canonical assessment no longer included")
require(omnigent_fields.get("autonomy_s3") == "A", "Omnigent canonical S3 state drift")
require(omnigent_fields.get("review_ref") == OMNIGENT_REVIEW_REF, "Omnigent canonical assessment ref drift")
require("omnigent" in representative, "Omnigent missing from representative S3 cohort")

observation_by_id = {row["observation_id"]: row for row in observations}
require(
    set(observation_by_id) == {
        "multi-agent-orchestration-supervisor-ablation-2026-08",
        "omnigent-child-session-recovery-2026-09",
        SMAS_OBSERVATION_ID,
    },
    "S3 observation registry identity drift",
)
require(
    {row["observation_id"] for row in canonical_observations}
    == {
        "multi-agent-orchestration-supervisor-ablation-2026-08",
        "omnigent-child-session-recovery-2026-09",
    },
    "S3 canonical observation identity drift",
)
smas = observation_by_id[SMAS_OBSERVATION_ID]
require(smas.get("canonical_harness_id") is None, "SMAS observation must remain non-canonical")
require(smas.get("canonical_system_eligible") is False, "SMAS observation must remain canonical-ineligible")
require(smas.get("boundary_class") == "composed-supervised-mas", "SMAS composed boundary drift")
require(smas.get("system_compatibility") == "benchmark-scaffolded", "SMAS compatibility drift")
require(smas.get("benchmark_artifact_revision") == SMAS_REVIEW_REF, "SMAS review ref drift")
require(smas.get("reported_average_token_reduction_percent") == 29.68, "SMAS published result drift")

routes = {route["route_id"]: route["status"] for route in closure["reviewed_route_classes"]}
require(
    routes == {
        "direct-manager-control-benchmarks": "benchmark-scaffolded",
        "direct-composed-runtime-supervision": "composed-noncanonical",
        "canonical-native-direct-within-system": "multiple-heterogeneous-not-matched",
        "canonical-native-mechanisms-without-direct-results": "no-direct-results",
        "native-quantitative-proxy": "not-isolated-s3",
        "matched-framework-campaign": "wrong-native-s3-paths",
        "direct-orchestration-benchmark-without-native-linkage": "benchmark-defined",
    },
    f"S3 closure route-state drift: {routes!r}",
)

cases = {case["case_id"]: case for case in coverage["cases"]}
for required_case in {
    "clawarena-team-direct-scaffolded",
    "loop-back-authority-direct-scaffolded",
    "supervisoragent-smas-direct-composed",
    "autogen-magentic-one-native-proxy-s3",
    "astra-cross-framework-wrong-native-s3-path",
    "multi-agent-orchestration-native-s3-direct",
    "omnigent-post-assessment-recovery-direct",
    "orchestrabench-failure-recovery-candidate",
    "cadis-native-s3-no-direct-result",
    "awaken-native-s3-no-direct-result",
    "ares-native-s3-no-direct-result",
}:
    require(required_case in cases, f"S3 closure lost required reviewed case: {required_case}")

smas_case = cases["supervisoragent-smas-direct-composed"]
require(smas_case.get("admitted") is False, "SMAS coverage case must remain non-canonical/non-admitted")
require(smas_case.get("canonical_harness_id") is None, "SMAS coverage identity drift")
require(smas_case.get("review_ref") == SMAS_REVIEW_REF, "SMAS coverage review ref drift")
require(smas_case.get("observation_ref") == f"observations.json#{SMAS_OBSERVATION_ID}", "SMAS coverage observation linkage drift")

omnigent_case = cases["omnigent-post-assessment-recovery-direct"]
require(omnigent_case.get("admitted") is True, "Omnigent S3 observation must remain admitted")
require(omnigent_case.get("canonical_harness_id") == "omnigent", "Omnigent coverage identity drift")
require(omnigent_case.get("canonical_review_ref") == OMNIGENT_REVIEW_REF, "Omnigent coverage review ref drift")
require(omnigent_case.get("observation_revision") == OMNIGENT_OBSERVATION_REF, "Omnigent coverage observation ref drift")
require(omnigent_case.get("revision_relation") == "post-assessment-descendant", "Omnigent coverage temporal relation drift")

for harness_id, (state, review_ref, case_id) in CANONICAL_DELTAS.items():
    fields = assessment_fields(harness_id)
    require(fields.get("status") == "included", f"{harness_id}: canonical assessment no longer included")
    require(fields.get("autonomy_s3") == state, f"{harness_id}: canonical S3 state drift")
    require(fields.get("review_ref") == review_ref, f"{harness_id}: canonical review_ref drift")
    require(harness_id in representative, f"{harness_id}: missing from representative S3 cohort")
    case = cases[case_id]
    require(case.get("canonical_harness_id") == harness_id, f"{case_id}: canonical identity drift")
    require(case.get("canonical_state_at_review") == state, f"{case_id}: reviewed S3 state drift")
    require(case.get("canonical_review_ref") == review_ref, f"{case_id}: reviewed ref drift")
    require(case.get("admitted") is False, f"{case_id}: delta review must remain non-admitted")

require(baselines["functions"]["S3"]["status"] == "gap", "S3 primary was selected without reopening closure")
blocking = baselines["functions"]["S3"].get("blocking_reason", "")
require("two canonical native observations" in blocking, "S3 baseline blocker must reflect two canonical observations")
require("SupervisorAgent / SMAS" in blocking, "S3 baseline blocker must preserve composed SMAS boundary")
require("materially matched" in blocking, "S3 baseline blocker must preserve matched-comparison requirement")
require(len(closure["reopen_when"]) >= 3, "S3 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 5, "S3 closure must retain anti-churn conditions")
require(
    any("another descriptive canonical S3 observation" in item for item in closure["do_not_reopen_for"]),
    "S3 closure must reject unmatched descriptive-row churn",
)
require(
    any("direct composed" in item for item in closure["do_not_reopen_for"]),
    "S3 closure must reject non-canonical composed-row churn",
)

print("S3 primary-search closure validation passed")
