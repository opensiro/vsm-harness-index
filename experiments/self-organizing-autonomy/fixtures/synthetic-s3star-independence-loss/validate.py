#!/usr/bin/env python3
"""Fail-closed structural validator for the synthetic S3* independence-loss fixture."""

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
    SCENARIO["fixture_id"] == "synthetic-s3star-complementary-independence-loss-v1",
    "fixture identity drift",
)
require(SCENARIO["fixture_version"] == "1.0.0", "fixture version drift")
require(SCENARIO["status"] == "judgment-free-review-input", "fixture must remain judgment-free")
require(SCENARIO["tracking_issue"] == 727, "tracking issue drift")
require(
    SCENARIO["protocol"]["revision"] == "8ab5fcbcb96e38eb02be4a6157c5d4a48cd39b23",
    "pinned Skills protocol drift",
)
require(SCENARIO["target"]["function"] == "S3*", "target function must remain S3*")
require(
    SCENARIO["target"]["released_state_prerequisite"] == "A",
    "released-A prerequisite must remain explicit",
)
require(SCENARIO["target"]["experimental_finding"] is None, "fixture must not pre-judge outcome")

baseline = SCENARIO["baseline"]
require(baseline["s3star_autonomous_closure_established"] is True, "baseline S3*=A witness lost")
require(baseline["sampling_owner"] == "audit-unit", "baseline sampling ownership drift")
require(baseline["evidence_selection_owner"] == "audit-unit", "baseline evidence ownership drift")
require(baseline["raw_evidence_access"] == "direct", "baseline direct evidence access lost")
require(baseline["audited_s1_can_suppress_evidence"] is False, "baseline S1 suppression must remain false")
require(baseline["complementary_independence"] is True, "baseline complementary independence lost")
require(baseline["target_defect_class_detected_reliably"] is False, "baseline must retain target audit inadequacy")

pressure = SCENARIO["adaptation_pressure"]
require(pressure["defect_class"] == "silent-cache-poisoning", "defect class drift")
require(pressure["domain"] == "in-domain operational defect", "defect must remain in-domain")
require(pressure["repeated_misses"] >= 2, "adaptation pressure requires recurring audit misses")
require(pressure["ordinary_retry_only"] is False, "fixture may not collapse to retry")
require(pressure["pre_authored_probe_exists"] is False, "fixture may not select a pre-authored probe")

timeline = {event["time"]: event for event in SCENARIO["timeline"]}
for required_time in ("T0.1", "T0.2", "T1.1", "T1.2", "T1.3", "T2.1"):
    require(required_time in timeline, f"missing timeline event {required_time}")

for time in ("T0.1", "T0.2"):
    event = timeline[time]
    require(event["event"] == "audit-cycle", f"{time} must be an audit cycle")
    require(event["defect_class"] == pressure["defect_class"], f"{time} defect class drift")
    require(event["audit_detected"] is False, f"{time} must witness baseline miss")
    require(event["evidence_selection_owner"] == "audit-unit", f"{time} baseline independence drift")
    require(event["complementary_independence"] is True, f"{time} must remain independent")

recognition = timeline["T1.1"]
require(recognition["owner"] == "internal-S4-support", "recognition owner drift")
require(recognition["external_constructor_involved"] is False, "external constructor entered recognition path")

construction = timeline["T1.2"]
require(construction["target_function"] == "S3*", "change must target S3*")
require(construction["change_id"] == "R-audit-manifest", "changed repertoire identity drift")
require(construction["pre_authored_specific_route_selected"] is False, "fixture may not select a pre-authored route")
require(construction["external_constructor_involved"] is False, "external constructor supplied the audit change")

integration = timeline["T1.3"]
require(integration["authorization_owner"] == "audit-unit", "audit authorization owner drift")
require(integration["missing_logic_supplied_by_authorizer"] is False, "authorizer supplied missing audit logic")
require(integration["integrated_change"] == "R-audit-manifest", "audit change not integrated")
require(integration["integration_persistent"] is True, "audit change must persist")
require(integration["sampling_owner_after"] == "audit-unit", "sampling execution owner drift")
require(integration["evidence_selection_owner_after"] == "delivery-s1", "designed independence-loss owner drift")
require(integration["audited_s1_can_suppress_evidence_after"] is True, "S1 suppression edge must be explicit")
require(integration["complementary_independence_after"] is False, "counterexample must retain independence loss")

post = timeline["T2.1"]
require(post["defect_class"] == pressure["defect_class"], "D-prime defect class drift")
require(post["changed_repertoire_used"] == "R-audit-manifest", "post-change path must use changed repertoire")
require(post["audit_detected"] is True, "post-change target defect must be detected")
require(post["finding_returned_to"] == "S3", "corrective return destination drift")
require(post["corrective_return_closed"] is True, "post-change corrective return must close")
require(post["evidence_selection_owner"] == "delivery-s1", "post-change evidence ownership drift")
require(post["audited_s1_can_suppress_evidence"] is True, "post-change suppression edge lost")
require(post["complementary_independence"] is False, "post-change independence loss must remain explicit")

edges = SCENARIO["candidate_test_edges"]
for key in (
    "released_A_prerequisite",
    "material_repertoire_inadequacy",
    "endogenous_functional_improvement_attempt",
    "legitimate_authorization",
    "integration",
    "post_change_detection_and_corrective_return",
    "external_constructor_absent",
):
    require(edges[key] is True, f"candidate-test edge lost: {key}")
require(edges["complementary_independence_preserved"] is False, "fixture must isolate the independence failure edge")
require(edges["strong_recursive_witness"] == "no", "fixture must remain non-recursive")

for phrase in (
    "no independent judgment yet",
    "complementary independence = false",
    "better audit score/outcome",
    "Review 2 must not see Review 1",
    "canonical assessments",
):
    require(phrase in PACKET, f"PACKET.md lost required boundary text: {phrase}")

require(
    "Is complementary independence preserved? yes / no / inconclusive" in TEMPLATE,
    "review template lost independence judgment",
)
require(
    "does the relation still qualify as S3*" in TEMPLATE,
    "review template lost function-first recheck",
)
require(
    "Do not read another reviewer's reasoning or finding" in TEMPLATE,
    "review independence warning lost",
)

print("synthetic S3* complementary-independence-loss fixture validation passed")
