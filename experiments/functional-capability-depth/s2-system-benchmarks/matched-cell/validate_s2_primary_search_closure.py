#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S2 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S2 = HERE.parent
EXPERIMENT = S2.parent
ROOT = EXPERIMENT.parents[1]

CANONICAL_DELTAS = {
    "cadis": ("C", "52c55854b1abbcda82839b7a934cbdb16a69b635", "cadis-native-s2-no-direct-result"),
    "ares": ("C", "f03153acace190c555c3721019407a7df47c139f", "ares-native-s2-no-direct-result"),
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


closure = load(HERE / "s2-primary-search-closure.json")
coverage = load(S2 / "coverage.json")
observations = load(S2 / "observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S2 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S2 closure status drift")
require(closure["tracking_issue"] == 564, "S2 closure tracking issue drift")
require(closure["current_state_update_issue"] == 586, "S2 closure current update issue drift")
require(closure["canonical_delta_review_issue"] == 592, "S2 canonical delta review issue drift")
require(closure["benchmark_family_review_issue"] == 622, "S2 benchmark-family review issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S2 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S2 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S2 closure scope drift")
require(closure["reviewed_at"] == coverage["reviewed_at"], "S2 closure/coverage review date drift")

expected = closure["evidence_depth"]
require(coverage["direct_benchmark_family_count"] == expected["direct_benchmark_families"], "S2 direct family count drift")
require(coverage["direct_observation_count"] == expected["direct_observations"], "S2 direct observation count drift")
require(
    coverage["canonical_direct_observation_count"] == expected["canonical_direct_observations"],
    "S2 canonical direct observation count drift",
)
require(len(observations) == expected["direct_observations"], "S2 observation registry count drift")
require(coverage["proxy_projection_count"] == expected["native_proxy_projections"], "S2 proxy projection count drift")
representative = coverage["representative_canonical_s2_systems_inspected"]
require(
    len(representative) == expected["representative_canonical_s2_systems_inspected"],
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

cases = {case["case_id"]: case for case in coverage["cases"]}
for required_case in {
    "dpbench-direct-scaffolded",
    "stale-semantic-coordination-direct-scaffolded",
    "nool-fleet-coordination-direct-scaffolded",
    "twining-conflict-resolution-direct-scaffolded",
    "grit-parallel-agent-contention-direct-noncanonical",
    "autogen-magentic-one-native-proxy",
    "squad-marble-native-proxy",
    "deepseek-harness-native-mechanism-no-direct-benchmark",
    "cadis-native-s2-no-direct-result",
    "ares-native-s2-no-direct-result",
    "mao-bench-candidate-no-results",
}:
    require(required_case in cases, f"S2 closure lost required reviewed case: {required_case}")

for harness_id, (state, review_ref, case_id) in CANONICAL_DELTAS.items():
    fields = assessment_fields(harness_id)
    require(fields.get("status") == "included", f"{harness_id}: canonical assessment no longer included")
    require(fields.get("autonomy_s2") == state, f"{harness_id}: canonical S2 state drift")
    require(fields.get("review_ref") == review_ref, f"{harness_id}: canonical review_ref drift")
    require(harness_id in representative, f"{harness_id}: missing from representative S2 cohort")
    case = cases[case_id]
    require(case.get("canonical_harness_id") == harness_id, f"{case_id}: canonical identity drift")
    require(case.get("canonical_state_at_review") == state, f"{case_id}: reviewed S2 state drift")
    require(case.get("canonical_review_ref") == review_ref, f"{case_id}: reviewed ref drift")
    require(case.get("admitted") is False, f"{case_id}: delta review must remain non-admitted")

require(len(observations) == 1, "S2 closure expects one direct non-canonical observation")
observation = observations[0]
require(observation["benchmark_id"] == "nool-fleet-coordination", "S2 direct observation benchmark drift")
require(observation["canonical_harness_id"] is None, "Nool S2 observation must remain non-canonical")
require(observation["canonical_system_eligible"] is False, "Nool S2 observation must remain non-canonical")
require(observation["system_compatibility"] == "benchmark-scaffolded", "Nool S2 system compatibility drift")

grit = cases["grit-parallel-agent-contention-direct-noncanonical"]
require(grit["review_ref"] == "0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe", "Grit S2 review ref drift")
require(grit["result_claim_commit"] == "a2c48735e0a16c49ca1541c4865fce438c479405", "Grit result claim commit drift")
require(grit["canonical_harness_id"] is None, "Grit S2 review must remain non-canonical")
require("observation_ref" not in grit, "Grit S2 review must not acquire an observation without run-level provenance")

s2_baseline = baselines["functions"]["S2"]
require(s2_baseline["status"] == "gap", "S2 primary was selected without reopening closure")
require(
    [row["benchmark_id"] for row in s2_baseline["reviewed_direct_families"]]
    == [
        "dpbench",
        "stale-semantic-coordination",
        "nool-fleet-coordination",
        "twining-conflict-resolution",
        "grit-parallel-agent-contention",
    ],
    "S2 gap metadata direct-family set drift",
)
require(len(closure["reopen_when"]) >= 3, "S2 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S2 closure must retain anti-churn conditions")

print("S2 primary-search closure validation passed")
