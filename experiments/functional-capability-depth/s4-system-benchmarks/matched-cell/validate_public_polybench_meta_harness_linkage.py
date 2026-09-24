#!/usr/bin/env python3
"""Fail-closed validator for the public PolyBench Meta-Harness linkage."""

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


record = load(HERE / "public-polybench-meta-harness-linkage.json")
parent = load(HERE / "public-polybench-paper-controls.json")
baselines = load(EXPERIMENT / "primary-baselines.json")
canonical = load(HERE.parent / "canonical_observations.json")

require(record["schema_version"] == 1, "Meta-Harness linkage schema_version drift")
require(record["status"] == "experimental-non-normative", "Meta-Harness linkage status drift")
require(record["tracking_issue"] == 553, "Meta-Harness linkage tracking issue drift")
require(
    record["refines_preflight"] == "public-polybench-paper-controls.json",
    "Meta-Harness linkage parent drift",
)
require(record["preflight_disposition"] == "blocked", "Meta-Harness linkage must remain blocked")
require(record["execution_authorized"] is False, "Meta-Harness linkage must not authorize execution")
require(record["primary_baseline_after_preflight"] == "gap", "Meta-Harness linkage must preserve S4 gap")
require(record["results"] is None, "Meta-Harness linkage must not contain admitted results")

paper = record["paper_row"]
require(paper["reported_method_label"] == "Meta-Harness", "Meta-Harness row label drift")
require(paper["benchmark"] == "PolyBench", "Meta-Harness row benchmark drift")
require(paper["paper_level_solver_temperature"] == 0.0, "Meta-Harness solver temperature drift")
require(paper["paper_level_evolver_temperature"] == 0.0, "Meta-Harness evolver temperature drift")
require(paper["paper_level_polybench_batch_size"] == 100, "Meta-Harness PolyBench batch-size drift")
require(paper["paper_level_common_chronological_order"] is True, "Meta-Harness task-order drift")
require(paper["paper_level_common_temporal_reveal"] is True, "Meta-Harness temporal-reveal drift")

link = record["implementation_linkage"]
require(
    link["a_evolve_pre_release_revision"] == "e4f70b949989e0abf08532e8223cb9eab447e971",
    "Meta-Harness local implementation revision drift",
)
require(link["local_engine_path"] == "agent_evolve/algorithms/meta_harness/engine.py", "Meta-Harness local path drift")
require(link["upstream_paper"] == "https://arxiv.org/abs/2603.28052", "Meta-Harness paper identity drift")
require(link["upstream_repository"] == "https://github.com/stanford-iris-lab/meta-harness", "Meta-Harness upstream repository drift")
require(
    link["upstream_reference_revision_inspected"] == "0cbc31e97c9e6d24232d1dc754827c02e1ec415c",
    "Meta-Harness inspected upstream revision drift",
)
require(
    link["upstream_reference_runtime_path"] == "experimental/harbor_meta_harness/agents/meta_harness.py",
    "Meta-Harness upstream runtime path drift",
)
require(link["local_imports_upstream_runtime"] is False, "Meta-Harness upstream import claim changed without review")
require(link["local_vendors_upstream_runtime"] is False, "Meta-Harness vendoring claim changed without review")
require(link["immutable_evaluated_upstream_revision"] is None, "Meta-Harness evaluated upstream revision populated without review")

expected_gates = {
    "paper-level-comparison-controls": "satisfied",
    "meta-harness-paper-identity": "satisfied",
    "design-correspondence": "satisfied",
    "upstream-native-implementation-identity": "blocked",
    "immutable-evaluated-upstream-revision-binding": "not_reached",
    "canonical-meta-harness-system-boundary": "not_reached",
    "matched-canonical-s4-cell": "not_reached",
}
gates = {gate["gate_id"]: gate["status"] for gate in record["gates"]}
require(gates == expected_gates, f"Meta-Harness linkage gate set/status drift: {gates!r}")

require(parent["tracking_issue"] == 538, "Meta-Harness parent paper-controls issue drift")
require(parent["preflight_disposition"] == "blocked", "Meta-Harness parent paper-controls disposition drift")
require(parent["execution_authorized"] is False, "Meta-Harness parent execution drift")
require(parent["primary_baseline_after_preflight"] == "gap", "Meta-Harness parent S4 state drift")
require(parent["paper"]["common_batch_loop"] is True, "Meta-Harness parent common-batch gate drift")
require(parent["paper"]["common_chronological_task_order"] is True, "Meta-Harness parent task-order gate drift")

require(baselines["functions"]["S4"]["status"] == "gap", "Meta-Harness refinement must not select an S4 primary")
require(
    not any(obs.get("canonical_harness_id") in {"meta-harness", "metaharness"} for obs in canonical),
    "Meta-Harness canonical observation appeared before native implementation linkage review",
)

print("public PolyBench Meta-Harness linkage validation passed")
