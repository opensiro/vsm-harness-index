#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S5 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S5 = HERE.parent
EXPERIMENT = S5.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


closure = load(HERE / "s5-primary-search-closure.json")
coverage = load(S5 / "coverage.json")
benchmark_observations = load(S5 / "benchmark_observations.json")
canonical_observations = load(S5 / "canonical_observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S5 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S5 closure status drift")
require(closure["tracking_issue"] == 569, "S5 closure tracking issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S5 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S5 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S5 closure scope drift")
require(closure["reviewed_at"] == coverage["reviewed_at"], "S5 closure/coverage review date drift")

expected = closure["evidence_depth"]
require(len(coverage["cases"]) == expected["reviewed_cases"], "S5 reviewed case count drift")
require(coverage["direct_family_count"] == expected["direct_benchmark_families"], "S5 direct family count drift")
require(
    coverage["composed_direct_observation_count"] == expected["composed_direct_observations"],
    "S5 composed observation count drift",
)
require(
    coverage["canonical_direct_observation_count"] == expected["canonical_direct_observations"],
    "S5 canonical observation count drift",
)
require(
    len(coverage["representative_canonical_s5_systems"]) == expected["representative_canonical_s5_systems"],
    "S5 representative canonical cohort drift",
)
require(closure["required_direct_chain"] == coverage["direct_benchmark_requirements"], "S5 direct criterion drift")
require(
    coverage["primary_baseline_additional_requirements"] == [closure["primary_additional_requirement"]],
    "S5 primary additional requirement drift",
)

routes = {route["route_id"]: route["status"] for route in closure["reviewed_route_classes"]}
require(
    routes == {
        "direct-composed-membership-authority": "direct-composed-not-canonical-primary",
        "fixed-policy-enforcement-and-governance": "not-direct-s5",
        "value-and-policy-reasoning-proxies": "proxy",
        "live-constitutional-governance-processes": "process-not-harness-benchmark",
        "parent-escalation-protocol": "protocol-not-benchmark",
        "native-constitutional-mechanism": "mechanism-not-benchmark",
        "constitution-policy-optimization": "authority-not-established",
    },
    f"S5 closure route-state drift: {routes!r}",
)

case_ids = {case["case_id"] for case in coverage["cases"]}
for required_case in {
    "govsim-selfgovern-membership-authority-direct-composed",
    "agentgovbench-enforcement-not-authority",
    "agent-parliament-ratified-amendment-process",
    "hem-parent-escalation-protocol",
    "constitutional-agent-governance-amendment-mechanism",
    "mac-constitution-optimization-proxy",
    "cmag-fixed-constitution-governance-proxy",
}:
    require(required_case in case_ids, f"S5 closure lost required reviewed case: {required_case}")

require(len(benchmark_observations) == 1, "S5 closure expects one direct composed observation")
require(
    benchmark_observations[0]["benchmark_id"] == "govsim-selfgovern",
    "S5 closure direct composed observation drift",
)
require(canonical_observations == [], "S5 closure must retain zero canonical direct observations")

s5_baseline = baselines["functions"]["S5"]
require(s5_baseline["status"] == "gap", "S5 primary was selected without reopening closure")
require(
    [row["benchmark_id"] for row in s5_baseline["reviewed_direct_families"]] == ["govsim-selfgovern"],
    "S5 gap metadata lost GovSim-SelfGovern",
)
require(len(closure["reopen_when"]) >= 3, "S5 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S5 closure must retain anti-churn conditions")

print("S5 primary-search closure validation passed")
