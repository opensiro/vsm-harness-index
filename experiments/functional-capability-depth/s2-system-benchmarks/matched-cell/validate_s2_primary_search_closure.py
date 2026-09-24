#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S2 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S2 = HERE.parent
EXPERIMENT = S2.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


closure = load(HERE / "s2-primary-search-closure.json")
coverage = load(S2 / "coverage.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S2 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S2 closure status drift")
require(closure["tracking_issue"] == 564, "S2 closure tracking issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S2 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S2 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S2 closure scope drift")

expected = closure["evidence_depth"]
require(coverage["direct_benchmark_family_count"] == expected["direct_benchmark_families"], "S2 direct family count drift")
require(coverage["direct_observation_count"] == expected["canonical_direct_observations"], "S2 direct observation count drift")
require(coverage["proxy_projection_count"] == expected["native_proxy_projections"], "S2 proxy projection count drift")
require(
    len(coverage["representative_canonical_s2_systems_inspected"]) == expected["representative_canonical_s2_systems_inspected"],
    "S2 representative canonical cohort size drift",
)

routes = {route["route_id"]: route["status"] for route in closure["reviewed_route_classes"]}
require(
    routes == {
        "direct-disturbance-benchmarks": "benchmark-scaffolded",
        "native-quantitative-proxies": "native-but-not-direct-s2",
        "matched-framework-campaigns": "framework-scaffolded-or-no-s2-disturbance",
        "native-mechanism-without-direct-results": "no-direct-results",
        "promising-multi-orchestrator-benchmark": "no-published-results",
    },
    f"S2 closure route-state drift: {routes!r}",
)

case_ids = {case["case_id"] for case in coverage["cases"]}
for required_case in {
    "dpbench-direct-scaffolded",
    "stale-semantic-coordination-direct-scaffolded",
    "autogen-magentic-one-native-proxy",
    "squad-marble-native-proxy",
    "deepseek-harness-native-mechanism-no-direct-benchmark",
    "mao-bench-candidate-no-results",
}:
    require(required_case in case_ids, f"S2 closure lost required reviewed case: {required_case}")

require(baselines["functions"]["S2"]["status"] == "gap", "S2 primary was selected without reopening closure")
require(len(closure["reopen_when"]) >= 3, "S2 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S2 closure must retain anti-churn conditions")

print("S2 primary-search closure validation passed")
