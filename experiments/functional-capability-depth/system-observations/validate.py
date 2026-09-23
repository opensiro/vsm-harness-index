#!/usr/bin/env python3
"""Validate shared Magentic-One raw observations and S2/S3 proxy projections."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RAW = HERE / "magentic-one.json"
S2_PROJECTIONS = HERE.parent / "s2-system-benchmarks" / "proxy_links.json"
S3_PROJECTIONS = HERE.parent / "s3-system-benchmarks" / "proxy_links.json"
S2_COVERAGE = HERE.parent / "s2-system-benchmarks" / "coverage.json"
S3_COVERAGE = HERE.parent / "s3-system-benchmarks" / "coverage.json"
ASSESSMENT = ROOT / "assessments" / "autogen-agentchat.md"
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)

EXPECTED_REVIEW_REF = "027ecf0a379bcc1d09956d46d12d44a3ad9cee14"
EXPECTED_RAW_IDS = {
    "magentic-one-gpt4o-test-results",
    "magentic-one-gpt4o-o1-test-results",
    "magentic-one-simple-orchestrator-gaia-ablation",
}
EXPECTED_PROJECTIONS = {
    "S2": "autogen-magentic-one-native-proxy-s2",
    "S3": "autogen-magentic-one-native-proxy-s3",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def assessment_fields() -> dict[str, str]:
    match = FRONTMATTER.match(ASSESSMENT.read_text(encoding="utf-8"))
    if not match:
        fail("autogen-agentchat assessment has no front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def metric(obs: dict, benchmark: str, metric_name: str) -> dict:
    rows = [
        row for row in obs.get("benchmark_results", [])
        if row.get("benchmark") == benchmark and row.get("metric") == metric_name
    ]
    if len(rows) != 1:
        fail(f"{obs.get('observation_id')}: expected one {benchmark}/{metric_name} row")
    return rows[0]


def main() -> None:
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    s2 = json.loads(S2_PROJECTIONS.read_text(encoding="utf-8"))
    s3 = json.loads(S3_PROJECTIONS.read_text(encoding="utf-8"))
    s2_coverage = json.loads(S2_COVERAGE.read_text(encoding="utf-8"))
    s3_coverage = json.loads(S3_COVERAGE.read_text(encoding="utf-8"))
    fm = assessment_fields()

    if raw.get("schema_version") != 1:
        fail("raw schema_version must be 1")
    if raw.get("canonical_harness_id") != "autogen-agentchat":
        fail("raw canonical_harness_id mismatch")
    if raw.get("canonical_assessment_ref") != "assessments/autogen-agentchat.md":
        fail("raw canonical_assessment_ref mismatch")
    if raw.get("canonical_review_ref") != EXPECTED_REVIEW_REF:
        fail("raw canonical_review_ref mismatch")
    if raw.get("canonical_states_at_review") != {"S2": "A", "S3": "A"}:
        fail("raw canonical state snapshot mismatch")

    implementation = raw.get("published_implementation", {})
    if implementation.get("platform") != "AutoGen 0.4":
        fail("published platform must be AutoGen 0.4")
    if implementation.get("system_compatibility") != "native-system":
        fail("published implementation must remain native-system")
    if implementation.get("canonical_revision_match") != "historical-first-party-lineage-not-current-review-ref":
        fail("historical/current revision relation must remain explicit")

    sources = raw.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 2 or any(not valid_https(s) for s in sources):
        fail("raw primary_sources invalid")

    observations = raw.get("observations")
    if not isinstance(observations, list) or len(observations) != 3:
        fail("expected exactly three shared Magentic-One observations")
    by_id = {obs.get("observation_id"): obs for obs in observations if isinstance(obs, dict)}
    if set(by_id) != EXPECTED_RAW_IDS:
        fail(f"unexpected raw observation IDs: {sorted(by_id)}")

    gpt4o = by_id["magentic-one-gpt4o-test-results"]
    if metric(gpt4o, "GAIA", "exact task completion rate percent").get("value") != 32.33:
        fail("GPT-4o GAIA metric mismatch")
    if metric(gpt4o, "AssistantBench", "exact match percent").get("value") != 11.0:
        fail("GPT-4o AssistantBench EM mismatch")
    if metric(gpt4o, "AssistantBench", "accuracy percent").get("value") != 25.3:
        fail("GPT-4o AssistantBench accuracy mismatch")
    if metric(gpt4o, "WebArena", "exact task completion rate percent").get("value") != 32.8:
        fail("GPT-4o WebArena metric mismatch")

    mixed = by_id["magentic-one-gpt4o-o1-test-results"]
    if metric(mixed, "GAIA", "exact task completion rate percent").get("value") != 38.0:
        fail("GPT-4o/o1 GAIA metric mismatch")
    if metric(mixed, "AssistantBench", "exact match percent").get("value") != 13.3:
        fail("GPT-4o/o1 AssistantBench EM mismatch")
    if metric(mixed, "AssistantBench", "accuracy percent").get("value") != 27.7:
        fail("GPT-4o/o1 AssistantBench accuracy mismatch")
    if metric(mixed, "WebArena", "not reported").get("value") is not None:
        fail("GPT-4o/o1 WebArena must remain unreported")

    ablation = by_id["magentic-one-simple-orchestrator-gaia-ablation"]
    if ablation.get("kind") != "native-mechanism-ablation":
        fail("orchestrator observation must be native-mechanism-ablation")
    if ablation.get("reported_relative_change_percent") != -31:
        fail("orchestrator ablation must preserve reported -31% change")
    removed = set(ablation.get("ablation", {}).get("removed_mechanisms", []))
    for required in {"progress tracking", "loop detection", "explicit instructions/direction to other agents"}:
        if required not in removed:
            fail(f"orchestrator ablation missing mechanism: {required}")

    if fm.get("status") != "included":
        fail("autogen-agentchat is no longer included")
    if fm.get("review_ref") != EXPECTED_REVIEW_REF:
        fail("autogen-agentchat canonical review_ref changed; reassess proxy linkage")
    if fm.get("autonomy_s2") != "A" or fm.get("autonomy_s3") != "A":
        fail("autogen-agentchat canonical S2/S3 state changed; reassess projection")

    for function, projections, coverage in (("S2", s2, s2_coverage), ("S3", s3, s3_coverage)):
        if not isinstance(projections, list) or len(projections) != 1:
            fail(f"{function}: expected exactly one Magentic-One proxy projection")
        projection = projections[0]
        if projection.get("projection_id") != EXPECTED_PROJECTIONS[function]:
            fail(f"{function}: projection_id mismatch")
        if projection.get("function") != function:
            fail(f"{function}: projection function mismatch")
        if projection.get("canonical_harness_id") != "autogen-agentchat":
            fail(f"{function}: canonical_harness_id mismatch")
        if projection.get("canonical_state_at_review") != "A":
            fail(f"{function}: canonical_state_at_review must be A")
        if projection.get("benchmark_fit") != "proxy":
            fail(f"{function}: benchmark_fit must remain proxy")
        if projection.get("system_compatibility") != "native-system":
            fail(f"{function}: system_compatibility must remain native-system")
        if projection.get("revision_relation") != "historical-first-party-lineage-not-current-review-ref":
            fail(f"{function}: revision relation must remain explicit")
        if set(projection.get("raw_observation_ids", [])) != EXPECTED_RAW_IDS:
            fail(f"{function}: raw observation references mismatch")
        if coverage.get("direct_observation_count") != 0:
            fail(f"{function}: direct observation count changed unexpectedly")
        if coverage.get("proxy_projection_count") != 1:
            fail(f"{function}: proxy_projection_count mismatch")

    print("ok: shared Magentic-One evidence validated")
    print("raw observations: 3")
    print("S2 proxy projections: 1")
    print("S3 proxy projections: 1")
    print("canonical AutoGen states: S2=A, S3=A")


if __name__ == "__main__":
    main()
