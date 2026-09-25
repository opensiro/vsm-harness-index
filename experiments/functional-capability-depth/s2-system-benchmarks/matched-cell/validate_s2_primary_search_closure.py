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
    "shep": ("C", "a874b3238fd01ebdbafc11015cccd9a63ed6e2f2", "shep-native-s2-no-direct-result"),
    "axocoatl": ("C", "edfe5031463686dc782cf3539e5aabae4e8eb9ab", "axocoatl-native-s2-no-direct-result"),
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
delta = load(S2 / "post-closure-deltas" / "shep-axocoatl-2026-09-25.json")

require(closure["schema_version"] == 1, "S2 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S2 closure status drift")
require(closure["tracking_issue"] == 564, "S2 closure tracking issue drift")
require(closure["current_state_update_issue"] == 586, "S2 closure current update issue drift")
require(closure["canonical_delta_review_issue"] == 592, "S2 canonical delta review issue drift")
require(closure["post_closure_delta_review_issue"] == 626, "S2 post-closure delta review issue drift")
require(closure["benchmark_family_review_issue"] == 596, "S2 benchmark-family review issue drift")
require(closure["public_evidence_admission_issue"] == 629, "S2 public evidence admission issue drift")
require(closure["codecrdt_public_evidence_issue"] == 640, "S2 CodeCRDT public-evidence issue drift")
require(closure["squad_canonical_direct_issue"] == 644, "S2 Squad canonical-direct issue drift")
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
        "direct-disturbance-benchmarks": "mixed-noncanonical-boundaries",
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
    "specification-gap-recovery-direct-scaffolded",
    "cooperbench-team-harness-direct-scaffolded",
    "codecrdt-observation-driven-direct-native-noncanonical",
    "autogen-magentic-one-native-proxy",
    "squad-marble-native-proxy",
    "squad-shared-state-conflict-direct-native-canonical",
    "deepseek-harness-native-mechanism-no-direct-benchmark",
    "cadis-native-s2-no-direct-result",
    "ares-native-s2-no-direct-result",
    "shep-native-s2-no-direct-result",
    "axocoatl-native-s2-no-direct-result",
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

require(delta["schema_version"] == 1, "S2 Shep/Axocoatl delta schema drift")
require(delta["function"] == "S2", "S2 Shep/Axocoatl delta function drift")
require(delta["disposition"] == "canonical-mechanisms-no-direct-results", "S2 delta disposition drift")
require(delta["capability_counts_changed"] is False, "S2 delta must not change capability counts")
require(delta["observation_registry_mutated"] is False, "S2 delta must not mutate observation registry")
require(delta["primary_baseline_changed"] is False, "S2 delta must not select a primary")
require(delta["reopen_condition_satisfied"] is False, "S2 delta unexpectedly reopens primary search")
delta_rows = {row["canonical_harness_id"]: row for row in delta["systems"]}
require(set(delta_rows) == {"shep", "axocoatl"}, "S2 delta system set drift")
for harness_id in ("shep", "axocoatl"):
    state, review_ref, _ = CANONICAL_DELTAS[harness_id]
    row = delta_rows[harness_id]
    require(row["canonical_state_at_review"] == state, f"{harness_id}: delta state drift")
    require(row["canonical_review_ref"] == review_ref, f"{harness_id}: delta ref drift")
    require(row["result_surface_review"] == "no-direct-s2-result", f"{harness_id}: delta result disposition drift")

require(len(observations) == 4, "S2 closure expects four direct observations")
observation_rows = {row["observation_id"]: row for row in observations}
require(
    set(observation_rows) == {
        "nool-trackd-scaleup1-contention-2026-08-21",
        "specification-gap-recovery-2026-03",
        "codecrdt-parallel-convergence-2025-10",
        "squad-shared-state-conflict-attenuation-2026-03",
    },
    "S2 direct observation identity set drift",
)
for observation_id, (benchmark_id, compatibility) in {
    "nool-trackd-scaleup1-contention-2026-08-21": ("nool-fleet-coordination", "benchmark-scaffolded"),
    "specification-gap-recovery-2026-03": ("specification-gap-recovery", "benchmark-scaffolded"),
    "codecrdt-parallel-convergence-2025-10": ("codecrdt-observation-coordination", "native-system"),
    "squad-shared-state-conflict-attenuation-2026-03": (None, "native-system"),
}.items():
    observation = observation_rows[observation_id]
    require(observation["benchmark_id"] == benchmark_id, f"{observation_id}: benchmark drift")
    require(observation["system_compatibility"] == compatibility, f"{observation_id}: system compatibility drift")
    if observation_id == "squad-shared-state-conflict-attenuation-2026-03":
        require(observation["canonical_harness_id"] == "squad", "Squad canonical observation identity drift")
        require(observation["canonical_system_eligible"] is True, "Squad canonical observation eligibility drift")
        require(observation.get("canonical_assessment_ref") == "2099faf51c08a912c359209447011b06decf0565", "Squad canonical observation ref drift")
        require(observation.get("canonical_state_at_review") == "A", "Squad canonical observation S2 state drift")
    else:
        require(observation["canonical_harness_id"] is None, f"{observation_id}: must remain non-canonical")
        require(observation["canonical_system_eligible"] is False, f"{observation_id}: must remain non-canonical")

require(
    observation_rows["codecrdt-parallel-convergence-2025-10"].get("comparison_class") == "descriptive-only",
    "CodeCRDT direct observation must remain descriptive-only",
)
require(
    observation_rows["squad-shared-state-conflict-attenuation-2026-03"].get("comparison_class") == "descriptive-only",
    "Squad canonical direct observation must remain descriptive-only",
)

s2_baseline = baselines["functions"]["S2"]
require(s2_baseline["status"] == "gap", "S2 primary was selected without reopening closure")
require(
    [row["benchmark_id"] for row in s2_baseline["reviewed_direct_families"]]
    == [
        "dpbench",
        "stale-semantic-coordination",
        "nool-fleet-coordination",
        "twining-conflict-resolution",
        "specification-gap-recovery",
        "cooperbench-team-harness",
        "codecrdt-observation-coordination",
    ],
    "S2 gap metadata direct-family set drift",
)
require(len(closure["reopen_when"]) >= 3, "S2 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S2 closure must retain anti-churn conditions")

print("S2 primary-search closure validation passed")
