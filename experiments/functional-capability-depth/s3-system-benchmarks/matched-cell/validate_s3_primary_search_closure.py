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
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S3 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S3 closure status drift")
require(closure["tracking_issue"] == 567, "S3 closure tracking issue drift")
require(closure["canonical_delta_review_issue"] == 592, "S3 canonical delta review issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S3 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S3 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S3 closure scope drift")
require(closure["reviewed_at"] == coverage["reviewed_at"], "S3 closure/coverage review date drift")

expected = closure["evidence_depth"]
require(coverage["direct_benchmark_family_count"] == expected["direct_benchmark_families"], "S3 direct family count drift")
require(coverage["direct_observation_count"] == expected["canonical_direct_observations"], "S3 direct observation count drift")
require(coverage["proxy_projection_count"] == expected["native_proxy_projections"], "S3 proxy projection count drift")
representative = coverage["representative_canonical_s3_systems_inspected"]
require(
    len(representative) == expected["representative_canonical_s3_systems_inspected"],
    "S3 representative canonical cohort size drift",
)

native = closure["canonical_native_observation"]
require(native["harness_id"] == "multi-agent-orchestration", "S3 canonical native observation identity drift")
require(native["baseline_passed"] == 11 and native["supervisor_passed"] == 48, "S3 native pass-count drift")
require(native["task_count"] == 54, "S3 native task-count drift")
require(native["baseline_routing_accuracy"] == 0.567, "S3 baseline routing accuracy drift")
require(native["supervisor_routing_accuracy"] == 1.0, "S3 supervisor routing accuracy drift")

routes = {route["route_id"]: route["status"] for route in closure["reviewed_route_classes"]}
require(
    routes == {
        "direct-manager-control-benchmarks": "benchmark-scaffolded",
        "canonical-native-direct-within-system": "single-system-only",
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
    "autogen-magentic-one-native-proxy-s3",
    "astra-cross-framework-wrong-native-s3-path",
    "multi-agent-orchestration-native-s3-direct",
    "orchestrabench-failure-recovery-candidate",
    "cadis-native-s3-no-direct-result",
    "awaken-native-s3-no-direct-result",
    "ares-native-s3-no-direct-result",
}:
    require(required_case in cases, f"S3 closure lost required reviewed case: {required_case}")

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
require(len(closure["reopen_when"]) >= 3, "S3 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S3 closure must retain anti-churn conditions")

print("S3 primary-search closure validation passed")
