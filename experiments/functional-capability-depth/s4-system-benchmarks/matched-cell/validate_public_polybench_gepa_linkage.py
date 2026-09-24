#!/usr/bin/env python3
"""Fail-closed validator for the public PolyBench GEPA linkage refinement."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPERIMENT = HERE.parent.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


record = load(HERE / "public-polybench-gepa-linkage.json")
parent = load(HERE / "public-polybench-paper-controls.json")
baselines = load(EXPERIMENT / "primary-baselines.json")
canonical = load(HERE.parent / "canonical_observations.json")

require(record["schema_version"] == 1, "GEPA linkage schema_version drift")
require(record["status"] == "experimental-non-normative", "GEPA linkage status drift")
require(record["tracking_issue"] == 551, "GEPA linkage tracking issue drift")
require(
    record["refines_preflight"] == "public-polybench-paper-controls.json",
    "GEPA linkage parent preflight drift",
)
require(record["preflight_disposition"] == "blocked", "GEPA linkage must remain blocked")
require(record["execution_authorized"] is False, "GEPA linkage must not authorize execution")
require(record["primary_baseline_after_preflight"] == "gap", "GEPA linkage must preserve S4 gap")
require(record["results"] is None, "GEPA linkage must not contain admitted results")

paper = record["paper_row"]
require(paper["reported_method_label"] == "GEPA", "GEPA paper-row label drift")
require(paper["benchmark"] == "PolyBench", "GEPA paper-row benchmark drift")
require(paper["paper_level_solver_temperature"] == 0.0, "GEPA paper solver temperature drift")
require(paper["paper_level_evolver_temperature"] == 0.0, "GEPA paper evolver temperature drift")
require(paper["paper_level_polybench_batch_size"] == 100, "GEPA PolyBench batch-size drift")
require(paper["paper_level_common_chronological_order"] is True, "GEPA task-order gate drift")
require(paper["paper_level_common_temporal_reveal"] is True, "GEPA temporal-reveal gate drift")

link = record["implementation_linkage"]
require(
    link["a_evolve_pre_release_revision"] == "e4f70b949989e0abf08532e8223cb9eab447e971",
    "GEPA adapter revision drift",
)
require(link["adapter_path"] == "agent_evolve/algorithms/gepa/engine.py", "GEPA adapter path drift")
require(link["upstream_repository"] == "https://github.com/gepa-ai/gepa", "GEPA upstream identity drift")
require(link["upstream_api"] == "gepa.optimize_anything.optimize_anything", "GEPA upstream API drift")
require(link["dependency_spec"] == "gepa>=0.1.0", "GEPA dependency range drift")
require(link["exact_evaluated_package_version"] is None, "GEPA exact package version was populated without review")
require(link["exact_evaluated_upstream_revision"] is None, "GEPA exact upstream revision was populated without review")
require(link["lock_or_run_metadata_found"] is False, "GEPA lock/run provenance changed without review")
require(link["adapter_calls_upstream_package"] is True, "GEPA upstream-call linkage drift")
require(link["adapter_restores_selected_candidate_into_workspace"] is True, "GEPA workspace return-path drift")

expected_gates = {
    "paper-level-comparison-controls": "satisfied",
    "evaluated-row-adapter-identity": "satisfied",
    "upstream-gepa-system-identity": "satisfied",
    "immutable-evaluated-upstream-revision-binding": "blocked",
    "canonical-gepa-system-boundary": "not_reached",
    "canonical-gepa-s4-ownership": "not_reached",
    "matched-canonical-s4-cell": "not_reached",
}
gates = {gate["gate_id"]: gate["status"] for gate in record["gates"]}
require(gates == expected_gates, f"GEPA linkage gate set/status drift: {gates!r}")

# Historical paper-level controls are the reviewed parent membrane and must
# remain blocked at canonical attribution rather than silently turning into a
# result record underneath this refinement.
require(parent["tracking_issue"] == 538, "GEPA parent paper-controls issue drift")
require(parent["preflight_disposition"] == "blocked", "GEPA parent paper-controls disposition drift")
require(parent["execution_authorized"] is False, "GEPA parent paper-controls execution drift")
require(parent["primary_baseline_after_preflight"] == "gap", "GEPA parent paper-controls S4 state drift")
require(parent["release_provenance"]["gepa_dependency_spec"] == "gepa>=0.1.0", "GEPA parent dependency evidence drift")
require(parent["paper"]["common_batch_loop"] is True, "GEPA parent common-batch gate drift")
require(parent["paper"]["common_chronological_task_order"] is True, "GEPA parent task-order gate drift")

require(baselines["functions"]["S4"]["status"] == "gap", "GEPA refinement must not select an S4 primary")
require(
    not any(obs.get("canonical_harness_id") == "gepa" for obs in canonical),
    "GEPA canonical observation appeared before immutable evaluated revision + standalone ownership review",
)

print("public PolyBench GEPA linkage validation passed")
