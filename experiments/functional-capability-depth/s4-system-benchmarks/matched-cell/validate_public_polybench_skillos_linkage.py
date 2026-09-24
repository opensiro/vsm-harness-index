#!/usr/bin/env python3
"""Fail-closed validator for the public PolyBench SkillOS linkage."""

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


record = load(HERE / "public-polybench-skillos-linkage.json")
parent = load(HERE / "public-polybench-paper-controls.json")
baselines = load(EXPERIMENT / "primary-baselines.json")
canonical = load(HERE.parent / "canonical_observations.json")

require(record["schema_version"] == 1, "SkillOS linkage schema_version drift")
require(record["status"] == "experimental-non-normative", "SkillOS linkage status drift")
require(record["tracking_issue"] == 555, "SkillOS linkage tracking issue drift")
require(
    record["refines_preflight"] == "public-polybench-paper-controls.json",
    "SkillOS linkage parent drift",
)
require(record["preflight_disposition"] == "blocked", "SkillOS linkage must remain blocked")
require(record["execution_authorized"] is False, "SkillOS linkage must not authorize execution")
require(record["primary_baseline_after_preflight"] == "gap", "SkillOS linkage must preserve S4 gap")
require(record["results"] is None, "SkillOS linkage must not contain admitted results")

paper = record["paper_row"]
require(paper["reported_method_label"] == "SkillOS", "SkillOS row label drift")
require(
    paper["reported_method_paper"] == "https://arxiv.org/abs/2605.06614",
    "SkillOS paper identity drift",
)
require(paper["benchmark"] == "PolyBench", "SkillOS row benchmark drift")
require(paper["paper_level_solver_temperature"] == 0.0, "SkillOS solver temperature drift")
require(paper["paper_level_evolver_temperature"] == 0.0, "SkillOS evolver temperature drift")
require(paper["paper_level_polybench_batch_size"] == 100, "SkillOS PolyBench batch-size drift")
require(paper["paper_level_common_chronological_order"] is True, "SkillOS task-order drift")
require(paper["paper_level_common_temporal_reveal"] is True, "SkillOS temporal-reveal drift")

link = record["implementation_linkage"]
require(
    link["a_evolve_pre_release_revision"] == "e4f70b949989e0abf08532e8223cb9eab447e971",
    "SkillOS inspected A-Evolve revision drift",
)
require(
    link["adaptive_harness_release_revision"] == "c1ea7d60c009519f5c037f7db9d47e97063bb353",
    "SkillOS inspected release revision drift",
)
require(
    link["release_declares_comparison_implementation_omitted"] is True,
    "SkillOS release-omission finding changed without review",
)
require(link["pre_release_contains_skillos_path"] is False, "SkillOS implementation path appeared without review")
require(
    link["pre_release_commit_history_binding_found"] is False,
    "SkillOS commit-history binding changed without review",
)
require(link["first_party_upstream_repository_bound"] is None, "SkillOS upstream repository populated without review")
require(link["immutable_evaluated_revision"] is None, "SkillOS evaluated revision populated without review")
require(
    link["third_party_reproductions_admissible_as_row_identity"] is False,
    "SkillOS reproduction substitution must remain forbidden",
)

expected_gates = {
    "paper-level-comparison-controls": "satisfied",
    "skillos-paper-identity": "satisfied",
    "evaluated-implementation-identity": "blocked",
    "immutable-evaluated-revision-binding": "not_reached",
    "canonical-skillos-system-boundary": "not_reached",
    "matched-canonical-s4-cell": "not_reached",
}
gates = {gate["gate_id"]: gate["status"] for gate in record["gates"]}
require(gates == expected_gates, f"SkillOS linkage gate set/status drift: {gates!r}")

require(parent["tracking_issue"] == 538, "SkillOS parent paper-controls issue drift")
require(parent["preflight_disposition"] == "blocked", "SkillOS parent paper-controls disposition drift")
require(parent["execution_authorized"] is False, "SkillOS parent execution drift")
require(parent["primary_baseline_after_preflight"] == "gap", "SkillOS parent S4 state drift")
require(parent["paper"]["common_batch_loop"] is True, "SkillOS parent common-batch gate drift")
require(parent["paper"]["common_chronological_task_order"] is True, "SkillOS parent task-order gate drift")

require(baselines["functions"]["S4"]["status"] == "gap", "SkillOS refinement must not select an S4 primary")
require(
    not any("skillos" in str(obs.get("canonical_harness_id", "")).lower() for obs in canonical),
    "SkillOS canonical observation appeared before evaluated implementation linkage review",
)

print("public PolyBench SkillOS linkage validation passed")
