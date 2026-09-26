#!/usr/bin/env python3
"""Fail-closed structural validator for the synthetic S1 escalation-boundary-shift fixture."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCENARIO = json.loads((HERE / "scenario.json").read_text(encoding="utf-8"))
PACKET = (HERE / "PACKET.md").read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


require(SCENARIO["schema_version"] == 1, "schema_version drift")
require(
    SCENARIO["fixture_id"] == "synthetic-s1-escalation-boundary-shift-v1",
    "fixture identity drift",
)
require(SCENARIO["fixture_version"] == "1.0.0", "fixture version drift")
require(SCENARIO["status"] == "judgment-free-review-input", "fixture must remain judgment-free")
require(SCENARIO["tracking_issue"] == 311, "tracking issue drift")
require(
    SCENARIO["protocol"]["revision"] == "96e16eba5882e98c6261b541521bc88862e00195",
    "pinned Skills protocol drift",
)
require(SCENARIO["target"]["function"] == "S1", "target function must remain S1")
require(
    SCENARIO["target"]["released_state_prerequisite"] == "A",
    "released-A prerequisite must remain explicit",
)
require(SCENARIO["target"]["experimental_finding"] is None, "fixture must not pre-judge outcome")

boundary = SCENARIO["declared_boundary"]
require(boundary["new_viable_recursion_created"] is False, "fixture must remain non-recursive")
require(
    "fixture author" in boundary["outside"],
    "external fixture author must remain outside the assessed synthetic boundary",
)

baseline = SCENARIO["baseline"]
require(baseline["s1_autonomous_closure_established"] is True, "S1 A prerequisite lost")
require(baseline["regulator_r_pre_authored"] is False, "R must not be pre-authored")
require(baseline["disturbance_d_supported_locally"] is False, "D must exceed the prior S1 repertoire")
require(
    "escalate-unknown-to-s3" in baseline["s1_prior_repertoire"],
    "prior escalation path missing",
)

D = SCENARIO["disturbance_class"]
require(D["domain"] == "in-domain", "disturbance must remain in-domain")
require(D["ordinary_hard_task_only"] is False, "fixture may not collapse to an ordinary hard task")
require(D["pre_authored_route_exists"] is False, "D-specific pre-authored route invalidates the fixture")

timeline = {event["time"]: event for event in SCENARIO["timeline"]}
for required_time in ("T0.1", "T0.2", "T1.1", "T1.2", "T1.3", "T2.1", "T2.2"):
    require(required_time in timeline, f"missing timeline event {required_time}")

for time in ("T0.1", "T0.2"):
    event = timeline[time]
    require(event["event"] == "disturbance", f"{time} must be a disturbance")
    require(event["equivalence_key"] == D["equivalence_key"], f"{time} disturbance class drift")
    require(event["s1_regulator_available"] is False, f"{time} must exceed local repertoire")
    require(event["s1_outcome"] == "cannot-absorb-locally", f"{time} must fail local closure")
    require(event["escalated_to"] == "S3", f"{time} must escalate to S3")
    require(event["s3_resolves_instance"] is True, f"{time} S3 return path missing")
    require(event["s1_return_to_operation"] is True, f"{time} must return to operation")

recognition = timeline["T1.1"]
require(recognition["owner"] == "internal-S4-support", "adaptation recognition must stay internal")
require(recognition["external_constructor_involved"] is False, "external constructor entered recognition path")

construction = timeline["T1.2"]
require(construction["target_function"] == "S1", "constructed regulator must target S1")
require(construction["new_regulator_id"] == "R", "regulator identity drift")
require(
    construction["pre_authored_specific_regulator_selected"] is False,
    "fixture may not select a pre-authored D-specific regulator",
)
require(construction["external_constructor_involved"] is False, "external constructor supplied R")
require(construction["s4_repertoire_changed"] is False, "fixture must not imply S4=S")

integration = timeline["T1.3"]
require(integration["authorization_owner"] == "S1-operational-owner", "S1 authority owner drift")
require(integration["missing_logic_supplied_by_authorizer"] is False, "authorizer supplied missing logic")
require(integration["integrated_regulator"] == "R", "R was not integrated")
require(integration["target_function_repertoire_changed"] == "S1", "wrong repertoire changed")
require(integration["integration_persistent"] is True, "regulator change must persist")
require(integration["parent_or_external_approval_required"] is False, "external approval entered fixture")

post = timeline["T2.1"]
require(post["equivalence_key"] == D["equivalence_key"], "D-prime is not materially equivalent")
require(post["s1_regulator_available"] is True, "R must be available post-integration")
require(post["regulator_used"] == "R", "post-change closure must use R")
require(post["s1_outcome"] == "absorbed-locally", "D-prime must close locally")
require(post["escalated_to"] is None, "post-change D-prime must no longer escalate")
require(post["s1_return_to_operation"] is True, "post-change return-to-operation missing")

control = timeline["T2.2"]
require(control["escalated_to"] == "S3", "S3 must remain necessary for unrelated variety")

edges = SCENARIO["candidate_test_edges"]
for key in (
    "released_A_prerequisite",
    "material_repertoire_inadequacy",
    "endogenous_functional_improvement",
    "legitimate_authorization",
    "integration",
    "post_change_closure",
    "escalation_boundary_shift",
    "external_constructor_absent",
):
    require(edges[key] is True, f"candidate-test edge lost: {key}")
require(edges["strong_recursive_witness"] == "no", "fixture must remain a non-recursive control")

for phrase in (
    "no independent judgment yet",
    "S4=S",
    "strong_recursive_witness: no",
    "Review 2 must not see Review 1",
    "canonical assessments",
):
    require(phrase in PACKET, f"PACKET.md lost required boundary text: {phrase}")

print("synthetic S1 escalation-boundary-shift fixture validation passed")
