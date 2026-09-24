#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S4 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S4 = HERE.parent
EXPERIMENT = S4.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


closure = load(HERE / "s4-primary-search-closure.json")
preflight = load(HERE / "preflight.json")
paper = load(HERE / "public-polybench-paper-controls.json")
continual = load(HERE / "public-polybench-continual-linkage.json")
gepa = load(HERE / "public-polybench-gepa-linkage.json")
meta = load(HERE / "public-polybench-meta-harness-linkage.json")
skillos = load(HERE / "public-polybench-skillos-linkage.json")
canonical = load(S4 / "canonical_observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S4 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S4 closure status drift")
require(closure["tracking_issue"] == 558, "S4 closure tracking issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S4 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S4 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S4 closure scope drift")

canonical_ids = {obs.get("canonical_harness_id") for obs in canonical}
require({"a-evolve", "kadath"}.issubset(canonical_ids), "S4 closure lost required canonical native observations")
require(
    set(closure["canonical_native_observations"]) == {"a-evolve", "kadath"},
    "S4 closure canonical observation inventory drift",
)

routes = {route["route_id"]: route for route in closure["reviewed_routes"]}
expected_route_ids = {
    "a-evolve-exo-skillsbench",
    "adaptive-auto-harness-polybench-paper-controls",
    "polybench-continual-harness",
    "polybench-gepa",
    "polybench-meta-harness",
    "polybench-skillos",
}
require(set(routes) == expected_route_ids, f"S4 closure route inventory drift: {set(routes)!r}")

require(preflight["preflight_disposition"] == "blocked", "A-Evolve x Exo preflight no longer blocked")
preflight_gates = {gate["gate_id"]: gate["status"] for gate in preflight["gates"]}
require(preflight_gates.get("exact-common-model-provider") == "blocked", "A-Evolve x Exo provider blocker changed")

require(paper["preflight_disposition"] == "blocked", "PolyBench paper-controls disposition changed")
require(paper["primary_baseline_after_preflight"] == "gap", "PolyBench paper-controls no longer preserve gap")
require(paper["paper"]["common_batch_loop"] is True, "PolyBench common batch loop drift")
require(paper["paper"]["common_chronological_task_order"] is True, "PolyBench common task order drift")

continual_gates = {gate["gate_id"]: gate["status"] for gate in continual["gates"]}
require(continual_gates.get("evaluated-row-implementation-binding") == "blocked", "Continual Harness linkage blocker changed")
require(continual["primary_baseline_after_preflight"] == "gap", "Continual Harness linkage no longer preserves gap")

gepa_gates = {gate["gate_id"]: gate["status"] for gate in gepa["gates"]}
require(gepa_gates.get("immutable-evaluated-upstream-revision-binding") == "blocked", "GEPA linkage blocker changed")
require(gepa["primary_baseline_after_preflight"] == "gap", "GEPA linkage no longer preserves gap")

meta_gates = {gate["gate_id"]: gate["status"] for gate in meta["gates"]}
require(meta_gates.get("upstream-native-implementation-identity") == "blocked", "Meta-Harness linkage blocker changed")
require(meta["primary_baseline_after_preflight"] == "gap", "Meta-Harness linkage no longer preserves gap")

skillos_gates = {gate["gate_id"]: gate["status"] for gate in skillos["gates"]}
require(skillos_gates.get("evaluated-implementation-identity") == "blocked", "SkillOS linkage blocker changed")
require(skillos["primary_baseline_after_preflight"] == "gap", "SkillOS linkage no longer preserves gap")

require(baselines["functions"]["S4"]["status"] == "gap", "S4 primary was selected without reopening closure")
require(len(closure["reopen_when"]) >= 3, "S4 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S4 closure must retain anti-churn conditions")

print("S4 primary-search closure validation passed")
