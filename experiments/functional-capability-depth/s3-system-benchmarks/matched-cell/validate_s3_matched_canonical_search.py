#!/usr/bin/env python3
"""Fail-closed validator for the current S3 matched-canonical search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S3 = HERE.parent
EXPERIMENT = S3.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


search = load(HERE / "s3-matched-canonical-search-closure.json")
primary = load(HERE / "s3-primary-search-closure.json")
coverage = load(S3 / "coverage.json")
observations = load(S3 / "observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(search["schema_version"] == 1, "S3 matched-canonical closure schema drift")
require(search["tracking_issue"] == 709, "S3 matched-canonical tracking issue drift")
require(search["status"] == "experimental-non-normative", "S3 matched-canonical status drift")
require(search["function"] == "S3", "S3 matched-canonical function drift")
require(search["scope"] == "current-public-evidence", "S3 matched-canonical scope drift")
require(
    search["disposition"] == "no-materially-matched-canonical-cell",
    "S3 matched-canonical disposition drift",
)
require(search["primary_baseline"] == "gap", "S3 matched-canonical closure must preserve gap")
require(primary.get("matched_canonical_search_issue") == 709, "S3 primary closure lost matched search pointer")
require(
    primary.get("matched_canonical_search_closure")
    == "matched-cell/s3-matched-canonical-search-closure.json",
    "S3 primary closure lost matched search artifact pointer",
)
require(primary["primary_baseline"] == "gap", "S3 primary closure no longer records gap")
require(search["reviewed_at"] == primary["reviewed_at"], "S3 matched search/primary review date drift")
require(search["reviewed_at"] == coverage["reviewed_at"], "S3 matched search/coverage review date drift")
require(baselines["functions"]["S3"]["status"] == "gap", "S3 primary baseline unexpectedly selected")

expected_depth = search["current_evidence_depth"]
primary_depth = primary["evidence_depth"]
for key in (
    "direct_benchmark_families",
    "direct_observations",
    "canonical_direct_observations",
    "native_proxy_projections",
):
    require(expected_depth[key] == primary_depth[key], f"S3 matched search {key} depth drift")
require(coverage["direct_benchmark_family_count"] == expected_depth["direct_benchmark_families"], "S3 coverage direct-family drift")
require(coverage["direct_observation_count"] == expected_depth["direct_observations"], "S3 coverage observation drift")
require(coverage["canonical_direct_observation_count"] == expected_depth["canonical_direct_observations"], "S3 coverage canonical observation drift")
require(coverage["proxy_projection_count"] == expected_depth["native_proxy_projections"], "S3 coverage proxy drift")
require(len(observations) == expected_depth["direct_observations"], "S3 observation registry count drift")

observation_rows = {row["observation_id"]: row for row in observations}
anchors = {row["canonical_harness_id"]: row for row in search["canonical_direct_anchors"]}
require(
    set(anchors) == {"multi-agent-orchestration", "omnigent"},
    "S3 matched search canonical anchor set drift",
)

mao_id = "multi-agent-orchestration-supervisor-ablation-2026-08"
mao_ref = "e6c34462af045d7e53d383103346362351c96353"
mao = anchors["multi-agent-orchestration"]
require(mao["observation_id"] == mao_id, "MAO matched-search observation drift")
require(mao["canonical_assessment_ref"] == mao_ref, "MAO matched-search review ref drift")
require(mao["comparison_class"] == "within-system-controlled-ablation", "MAO matched-search comparison class drift")
require(mao_id in observation_rows, "MAO canonical S3 observation missing")
mao_obs = observation_rows[mao_id]
require(mao_obs.get("canonical_harness_id") == "multi-agent-orchestration", "MAO canonical identity drift")
require(mao_obs.get("canonical_system_eligible") is True, "MAO canonical eligibility drift")
require(mao_obs.get("canonical_review_revision") == mao_ref, "MAO canonical observation ref drift")
require(mao_obs.get("comparison_class") == "within-system-controlled-ablation", "MAO comparison class drift")

omnigent_id = "omnigent-child-session-recovery-2026-09"
omnigent_ref = "4d963a360e798f076d4fdbd4665e7188e4da05df"
omnigent_observation_ref = "d8d07168c05ce1385be19dbd6ea64f4574c8d144"
omnigent = anchors["omnigent"]
require(omnigent["observation_id"] == omnigent_id, "Omnigent matched-search observation drift")
require(omnigent["canonical_assessment_ref"] == omnigent_ref, "Omnigent matched-search review ref drift")
require(omnigent["observation_revision"] == omnigent_observation_ref, "Omnigent matched-search observation revision drift")
require(omnigent["revision_relation"] == "post-assessment-descendant", "Omnigent matched-search temporal relation drift")
require(omnigent["comparison_class"] == "descriptive-only", "Omnigent matched-search comparison class drift")
require(omnigent_id in observation_rows, "Omnigent canonical S3 observation missing")
omnigent_obs = observation_rows[omnigent_id]
require(omnigent_obs.get("canonical_harness_id") == "omnigent", "Omnigent canonical identity drift")
require(omnigent_obs.get("canonical_system_eligible") is True, "Omnigent canonical eligibility drift")
require(omnigent_obs.get("canonical_review_revision") == omnigent_ref, "Omnigent canonical observation ref drift")
require(omnigent_obs.get("observation_revision") == omnigent_observation_ref, "Omnigent observation revision drift")
require(omnigent_obs.get("revision_relation") == "post-assessment-descendant", "Omnigent temporal relation drift")
require(omnigent_obs.get("comparison_class") == "descriptive-only", "Omnigent observation became matched without reopening search")

canonical_rows = [row for row in observations if row.get("canonical_system_eligible") is True]
require(
    {row["observation_id"] for row in canonical_rows} == {mao_id, omnigent_id},
    "S3 canonical observation cohort changed without reopening matched search",
)

routes = {row["route_id"]: row for row in search["reviewed_matched_routes"]}
require(
    set(routes)
    == {
        "existing-canonical-pair",
        "astra-cross-framework",
        "supervisoragent-smas",
        "benchmark-defined-manager-control",
    },
    "S3 matched-search route set drift",
)
require(routes["existing-canonical-pair"]["status"] == "heterogeneous-not-matched", "S3 canonical-pair blocker drift")
require(routes["astra-cross-framework"]["repository"] == "HeeManSu/astra-agi", "Astra repository drift")
require(routes["astra-cross-framework"]["review_ref"] == "129b440e531af9d053645f7fab966c172bfb3b3b", "Astra reviewed ref drift")
require(
    routes["astra-cross-framework"]["status"] == "matched-framework-wrong-native-s3-paths",
    "Astra S3 matched-route classification drift",
)
require(routes["supervisoragent-smas"]["repository"] == "LINs-lab/SupervisorAgent", "SupervisorAgent repository drift")
require(routes["supervisoragent-smas"]["review_ref"] == "ab116b557b095ae8d45bdf2d61057ce19519d4ff", "SupervisorAgent reviewed ref drift")
require(routes["supervisoragent-smas"]["status"] == "direct-composed-noncanonical", "SupervisorAgent matched-route classification drift")
require(
    routes["benchmark-defined-manager-control"]["status"]
    == "direct-but-no-multi-canonical-native-linkage",
    "benchmark-defined S3 matched-route classification drift",
)

blocking = search.get("blocking_reason", "")
require("Two canonical direct S3 observations" in blocking, "S3 matched-search blocker lost canonical depth")
require("materially heterogeneous" in blocking, "S3 matched-search blocker lost heterogeneity boundary")
require("native or adapter-preserved S3 path" in blocking, "S3 matched-search blocker lost native-path requirement")
require(isinstance(search.get("reopen_when"), list) and search["reopen_when"], "S3 matched search lost reopen conditions")
require(isinstance(search.get("do_not_reopen_for"), list) and search["do_not_reopen_for"], "S3 matched search lost anti-churn conditions")
require(
    any("Opensiro-operated" in item for item in search["do_not_reopen_for"]),
    "S3 matched search must not reopen for Opensiro-operated reproduction",
)
require(search.get("non_claim"), "S3 matched search lost non-claim boundary")

print("S3 matched-canonical search closure validation passed")
