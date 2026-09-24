#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S3* primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S3STAR = HERE.parent
EXPERIMENT = S3STAR.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


closure = load(HERE / "s3star-primary-search-closure.json")
canonical = load(S3STAR / "canonical_observations.json")
coverage = load(S3STAR / "coverage.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S3* closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S3* closure status drift")
require(closure["tracking_issue"] == 561, "S3* closure tracking issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S3* closure disposition drift")
require(closure["primary_baseline"] == "gap", "S3* closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S3* closure scope drift")

canonical_ids = {obs.get("canonical_harness_id") for obs in canonical}
require(canonical_ids == {"appliedscientist", "data-to-paper"}, f"S3* canonical observation set drift: {canonical_ids!r}")
require(
    set(closure["canonical_native_observations"]) == canonical_ids,
    "S3* closure canonical observation inventory drift",
)

expected_depth = closure["evidence_depth"]
require(coverage["direct_benchmark_family_count"] == expected_depth["direct_benchmark_families"], "S3* direct family depth drift")
require(coverage["composed_direct_observation_count"] == expected_depth["composed_direct_observations"], "S3* composed observation depth drift")
require(coverage["canonical_direct_observation_count"] == expected_depth["canonical_direct_observations"], "S3* canonical observation depth drift")

negative = closure["strongest_matched_negative_control"]
require(negative["paper"] == "https://arxiv.org/abs/2607.28631", "S3* matched negative-control paper drift")
require(negative["canonical_anchor"] == "data-to-paper", "S3* matched negative-control anchor drift")
require(negative["disposition"] == "not-s3star-native-comparison", "S3* negative-control disposition drift")
flags = negative["integrated_review_flags"]
require(flags["Data-to-Paper"] is False, "S3* closure assumes evaluated Data-to-Paper review path remains inactive")
require(flags["Sakana v1"] is False and flags["Sakana v2"] is False, "S3* Sakana integrated-review control drift")
require(flags["CycleResearcher"] is True, "S3* CycleResearcher control drift")

routes = {route["route_id"]: route["status"] for route in closure["reviewed_route_classes"]}
require(
    routes == {
        "canonical-native-within-system": "heterogeneous",
        "direct-composed-review-benchmarks": "not-native-cross-harness",
        "ai-scientist-head-to-head-2607.28631": "matched-whole-system-not-s3star",
    },
    f"S3* closure reviewed-route state drift: {routes!r}",
)

require(baselines["functions"]["S3*"]["status"] == "gap", "S3* primary was selected without reopening closure")
require(len(closure["reopen_when"]) >= 3, "S3* closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 3, "S3* closure must retain anti-churn conditions")

print("S3* primary-search closure validation passed")
