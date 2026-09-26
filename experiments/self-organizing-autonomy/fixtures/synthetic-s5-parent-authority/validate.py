#!/usr/bin/env python3
"""Fail-closed structural validator for the synthetic S5 parent-authority fixture."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCENARIO = json.loads((HERE / "scenario.json").read_text(encoding="utf-8"))
PACKET = (HERE / "PACKET.md").read_text(encoding="utf-8")
TEMPLATE = (HERE / "REVIEW-TEMPLATE.md").read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


require(SCENARIO["schema_version"] == 1, "schema_version drift")
require(
    SCENARIO["fixture_id"] == "synthetic-s5-higher-recursion-authority-v1",
    "fixture identity drift",
)
require(SCENARIO["fixture_version"] == "1.0.0", "fixture version drift")
require(SCENARIO["status"] == "judgment-free-review-input", "fixture must remain judgment-free")
require(SCENARIO["tracking_issue"] == 728, "tracking issue drift")
require(
    SCENARIO["protocol"]["revision"] == "8ab5fcbcb96e38eb02be4a6157c5d4a48cd39b23",
    "pinned Skills protocol drift",
)
require(SCENARIO["target"]["function"] == "S5", "target function must remain S5")
require(SCENARIO["target"]["released_state_prerequisite"] == "P", "released S5=P baseline drift")
require(
    SCENARIO["target"]["candidate_eligible_under_S_test"] is False,
    "parent-governed S5 must remain ineligible under current S test",
)
require(SCENARIO["target"]["experimental_finding"] is None, "fixture must not pre-judge outcome")

boundary = SCENARIO["declared_boundary"]
require(boundary["higher_recursion_id"] == "parent-root", "higher recursion identity drift")
require("parent root constitutional authority" in boundary["outside"], "parent authority must remain outside lower boundary")
require(boundary["new_viable_recursion_created"] is False, "fixture must remain non-recursive")

baseline = SCENARIO["baseline"]
require(baseline["released_s5_state"] == "P", "released parent-governed state drift")
require(baseline["lower_local_policy_discretion"] is True, "local policy discretion must remain present")
require(baseline["lower_can_edit_proposed_policy"] is True, "local proposal editing must remain present")
require(
    baseline["lower_can_activate_ultimate_identity_change_without_parent"] is False,
    "lower system may not gain ultimate identity authority",
)
require(baseline["ultimate_identity_authority_owner"] == "parent-root", "ultimate authority owner drift")
require(baseline["constitutive_signature_required"] is True, "parent constitutive signature requirement lost")

pressure = SCENARIO["adaptation_pressure"]
require(pressure["condition"] == "regulated-medical-domain-request", "adaptation-pressure identity drift")
require(pressure["requires_constitutive_change"] is True, "fixture must require constitutive change")

timeline = {event["time"]: event for event in SCENARIO["timeline"]}
for required_time in ("T0.1", "T1.1", "T1.2", "T1.3", "T1.4", "T2.1"):
    require(required_time in timeline, f"missing timeline event {required_time}")

initial = timeline["T0.1"]
require(initial["lower_can_authorize"] is False, "T0 must expose lower authority limit")
require(initial["escalated_to"] == "parent-root", "T0 must escalate to higher recursion")

recognition = timeline["T1.1"]
require(recognition["owner"] == "internal-S4-support", "recognition owner drift")
require(recognition["external_constructor_involved"] is False, "external constructor entered recognition path")

construction = timeline["T1.2"]
require(construction["owner"] == "lower-policy-council", "local policy-construction owner drift")
require(construction["proposal_id"] == "constitution-C2", "proposal identity drift")
require(construction["missing_policy_logic_supplied_by_parent"] is False, "parent must not author proposal content")
require(construction["external_constructor_involved"] is False, "external constructor supplied policy content")

staging = timeline["T1.3"]
require(staging["local_configuration_written"] is True, "local self-edit must remain observable")
require(staging["production_constitutive_verifier_accepts"] is False, "unsigned local change must remain ineffective")
require(staging["effective_identity_changed"] is False, "identity may not change before parent ratification")

ratification = timeline["T1.4"]
require(ratification["owner"] == "parent-root", "ratification owner drift")
require(ratification["parent_supplies_missing_policy_logic"] is False, "fixture isolates authority, not external authorship")
require(ratification["parent_exercises_decisive_constitutive_authority"] is True, "parent decisiveness lost")
require(ratification["constitutive_signature_added"] is True, "constitutive ratification missing")
require(ratification["effective_identity_changed"] is True, "identity must change only after ratification")

post = timeline["T2.1"]
require(post["lower_operation_admitted"] is True, "post-change operation must close")
require(post["parent_ratification_required_for_effective_change"] is True, "post-change closure must retain authority provenance")
require(post["return_to_operation"] is True, "return-to-operation missing")

edges = SCENARIO["candidate_test_edges"]
require(edges["released_A_prerequisite"] is False, "counterexample must retain failed A prerequisite")
require(edges["released_parent_governed_S5"] is True, "released S5=P edge lost")
for key in (
    "material_adaptation_pressure",
    "lower_endogenous_policy_construction",
    "local_staging",
    "later_operational_closure",
    "higher_recursion_authority_decisive",
):
    require(edges[key] is True, f"counterexample support edge lost: {key}")
require(edges["external_constructor_supplied_missing_policy_logic"] is False, "fixture must isolate authority from policy authorship")
require(edges["ultimate_policy_authority_owned_by_lower_system"] is False, "lower system must not own ultimate authority")
require(edges["strong_recursive_witness"] == "no", "fixture must remain non-recursive")

for phrase in (
    "no independent judgment yet",
    "S5 = P",
    "proposal authorship = lower system",
    "ultimate-policy authority = parent root",
    "current experiment does not define `S(P)`",
    "Review 2 must not see Review 1",
):
    require(phrase in PACKET, f"PACKET.md lost required authority boundary: {phrase}")

require("Released S5 baseline: `P` accepted" in TEMPLATE, "review template lost released-P check")
require("Candidate-witness eligibility under current `S` experiment" in TEMPLATE, "review template lost A-prerequisite gate")
require("Is parent constitutive ratification decisive?" in TEMPLATE, "review template lost parent authority test")
require("Does the current protocol define `S(P)`?" in TEMPLATE, "review template lost composition control")

print("synthetic S5 higher-recursion authority fixture validation passed")
