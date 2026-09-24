#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S3 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S3 = HERE.parent
EXPERIMENT = S3.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


closure = load(HERE / "s3-primary-search-closure.json")
coverage = load(S3 / "coverage.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S3 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S3 closure status drift")
require(closure["tracking_issue"] == 567, "S3 closure tracking issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S3 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S3 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S3 closure scope drift")

expected = closure["evidence_depth"]
require(coverage["direct_benchmark_family_count"] == expected["direct_benchmark_families"], "S3 direct family count drift")
require(coverage["direct_observation_count"] == expected["canonical_direct_observations"], "S3 direct observation count drift")
require(coverage["proxy_projection_count"] == expected["native_proxy_projections"], "S3 proxy projection count drift")
require(
    len(coverage["representative_canonical_s3_systems_inspected"]) == expected["representative_canonical_s3_systems_inspected"],
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
        "native-quantitative-proxy": "not-isolated-s3",
        "matched-framework-campaign": "wrong-native-s3-paths",
        "direct-orchestration-benchmark-without-native-linkage": "benchmark-defined",
    },
    f"S3 closure route-state drift: {routes!r}",
)

case_ids = {case["case_id"] for case in coverage["cases"]}
for required_case in {
    "clawarena-team-direct-scaffolded",
    "loop-back-authority-direct-scaffolded",
    "autogen-magentic-one-native-proxy-s3",
    "astra-cross-framework-wrong-native-s3-path",
    "multi-agent-orchestration-native-s3-direct",
    "orchestrabench-failure-recovery-candidate",
}:
    require(required_case in case_ids, f"S3 closure lost required reviewed case: {required_case}")

require(baselines["functions"]["S3"]["status"] == "gap", "S3 primary was selected without reopening closure")
require(len(closure["reopen_when"]) >= 3, "S3 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S3 closure must retain anti-churn conditions")

print("S3 primary-search closure validation passed")
