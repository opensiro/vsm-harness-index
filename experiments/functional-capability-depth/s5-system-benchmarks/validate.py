#!/usr/bin/env python3
"""Validate experimental S5 benchmark coverage and canonical/composed separation."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAP_PATH = HERE.parent / "vsm-benchmark-family-map" / "map.json"
BASELINES_PATH = HERE.parent / "primary-baselines.json"
COVERAGE_PATH = HERE / "coverage.json"
BENCHMARK_OBSERVATIONS_PATH = HERE / "benchmark_observations.json"
CANONICAL_OBSERVATIONS_PATH = HERE / "canonical_observations.json"

EXPECTED_S5_MAP = {
    "govsim-selfgovern": "direct",
    "agentgovbench": "unsuitable",
    "rolecde": "proxy",
    "agent-valuebench": "proxy",
    "agentcity": "proxy",
    "cgst-framework": "proxy",
}

EXPECTED_CANONICAL = {
    "headcount": "A",
    "henterprise": "A",
    "ouroboros": "A(P)",
    "thclaws": "P",
    "masters-of-ai-harness": "C(P)",
}

EXPECTED_BENCHMARK_STATUS = {
    "headcount": "candidate-native-no-direct-results",
    "henterprise": "candidate-native-no-direct-results",
    "ouroboros": "direct-native-descriptive-observation",
    "thclaws": "candidate-native-no-direct-results",
    "masters-of-ai-harness": "candidate-native-no-direct-results",
}

EXPECTED_COVERAGE_CLASSES = {
    "direct-composed",
    "direct-canonical",
    "proxy",
    "unsuitable",
    "protocol-not-benchmark",
    "governance-process-not-harness-benchmark",
    "candidate-native-mechanism-not-benchmark",
    "candidate-native-no-direct-results",
}

REQUIRED_FOLLOWUP_CASES = {
    "govsim-selfgovern-membership-authority-direct-composed": ("direct-composed", None),
    "ouroboros-parent-governed-policy-change-direct-canonical": ("direct-canonical", None),
    "constitutional-agent-governance-amendment-mechanism": (
        "candidate-native-mechanism-not-benchmark",
        "368717cb50b70826412f85022d23b3fd8a0dec77",
    ),
    "agent-parliament-ratified-amendment-process": (
        "governance-process-not-harness-benchmark",
        None,
    ),
    "mac-constitution-optimization-proxy": (
        "proxy",
        "76aea7ce2cd95e46cfcf015a70895fdc267a0f4f",
    ),
    "cmag-fixed-constitution-governance-proxy": ("proxy", None),
    "gps-bench-policy-analysis-not-organizational-s5": ("unsuitable", None),
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"missing frontmatter: {path}")
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    fail(f"unterminated frontmatter: {path}")


def main() -> None:
    coverage = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))
    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS_PATH.read_text(encoding="utf-8"))
    canonical_observations = json.loads(CANONICAL_OBSERVATIONS_PATH.read_text(encoding="utf-8"))
    benchmark_map = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    baselines = json.loads(BASELINES_PATH.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S5":
        fail("coverage function must be S5")
    if coverage.get("direct_family_count") != 1:
        fail("S5 direct_family_count must remain 1")
    if coverage.get("composed_direct_observation_count") != 1:
        fail("S5 composed_direct_observation_count must remain 1")
    if coverage.get("canonical_direct_observation_count") != 1:
        fail("S5 canonical_direct_observation_count must be 1")

    s5_baseline = (baselines.get("functions") or {}).get("S5") or {}
    if s5_baseline.get("status") != "gap":
        fail("primary-baselines.json must preserve S5 status=gap")
    reviewed = s5_baseline.get("reviewed_direct_families")
    if not isinstance(reviewed, list) or [row.get("benchmark_id") for row in reviewed] != ["govsim-selfgovern"]:
        fail("S5 gap metadata must keep GovSim-SelfGovern as the only reviewed direct benchmark family")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != EXPECTED_COVERAGE_CLASSES:
        fail(f"S5 coverage_classes vocabulary drift: {sorted(declared_classes)}")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")

    seen_ids: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        if not isinstance(case, dict):
            fail("every S5 coverage case must be an object")
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("every S5 coverage case requires case_id")
        if case_id in seen_ids:
            fail(f"duplicate S5 coverage case_id: {case_id}")
        seen_ids.add(case_id)
        by_id[case_id] = case

        classification = case.get("classification")
        if classification not in EXPECTED_COVERAGE_CLASSES - {"candidate-native-no-direct-results"}:
            fail(f"{case_id}: invalid S5 coverage classification {classification!r}")
        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{case_id}: primary_sources must be non-empty HTTPS URLs")
        finding = case.get("finding")
        if not isinstance(finding, str) or len(finding.strip()) < 40:
            fail(f"{case_id}: explicit finding required")

    for case_id, (expected_class, expected_ref) in REQUIRED_FOLLOWUP_CASES.items():
        case = by_id.get(case_id)
        if case is None:
            fail(f"missing required S5 coverage case: {case_id}")
        if case.get("classification") != expected_class:
            fail(f"{case_id}: expected classification {expected_class}")
        if expected_ref is not None and case.get("review_ref") != expected_ref:
            fail(f"{case_id}: review_ref drift")

    govsim_case = by_id["govsim-selfgovern-membership-authority-direct-composed"]
    if govsim_case.get("benchmark_fit") != "direct":
        fail("GovSim-SelfGovern coverage case must remain direct")
    if govsim_case.get("system_compatibility") != "benchmark-scaffolded":
        fail("GovSim-SelfGovern must remain benchmark-scaffolded")
    if govsim_case.get("canonical_harness_id") is not None:
        fail("GovSim-SelfGovern composed evidence must not acquire a canonical harness id")
    if govsim_case.get("code_revision_status") != "unresolved-authoritative-public-repository":
        fail("GovSim-SelfGovern code provenance limitation drift")

    ouroboros_case = by_id["ouroboros-parent-governed-policy-change-direct-canonical"]
    if ouroboros_case.get("benchmark_fit") != "direct":
        fail("Ouroboros repository-history case must remain direct S5 evidence")
    if ouroboros_case.get("system_compatibility") != "native-system":
        fail("Ouroboros direct observation must remain native-system")
    if ouroboros_case.get("canonical_harness_id") != "ouroboros":
        fail("Ouroboros direct observation lost canonical identity")
    if ouroboros_case.get("ownership_mode_observed") != "parent-governed":
        fail("Ouroboros observation must remain limited to parent-governed ownership")
    if ouroboros_case.get("comparison_class") != "descriptive-only":
        fail("Ouroboros observation must remain descriptive-only")

    if not isinstance(benchmark_observations, list) or len(benchmark_observations) != 1:
        fail("S5 benchmark_observations.json must contain exactly one composed observation")
    observation = benchmark_observations[0]
    expected_observation_fields = {
        "function": "S5",
        "benchmark_id": "govsim-selfgovern",
        "benchmark_fit": "direct",
        "boundary_class": "composed-system",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "benchmark-scaffolded",
        "code_revision_status": "unresolved-authoritative-public-repository",
        "society_size": 5,
        "max_rounds": 12,
        "model_settings": 8,
        "seeds_per_model_game_cell": 5,
    }
    for field, expected in expected_observation_fields.items():
        if observation.get(field) != expected:
            fail(f"GovSim-SelfGovern observation {field} drift: {observation.get(field)!r}")
    if observation.get("membership_action") != "agent.active = False":
        fail("GovSim-SelfGovern membership action drift")
    if observation.get("non_thinking_exile") != {"enacted": 8, "proposed": 460, "pass_rate": 0.017}:
        fail("GovSim-SelfGovern non-thinking exile result drift")
    if observation.get("thinking_exile") != {"enacted": 31, "proposed": 122, "pass_rate": 0.254}:
        fail("GovSim-SelfGovern thinking exile result drift")

    if not isinstance(canonical_observations, list) or len(canonical_observations) != 1:
        fail("S5 canonical_observations.json must contain exactly one canonical direct observation")
    canonical = canonical_observations[0]
    expected_canonical_fields = {
        "function": "S5",
        "evidence_surface": "immutable-repository-history",
        "benchmark_family": None,
        "benchmark_fit": "direct",
        "boundary_class": "canonical-native-system",
        "canonical_harness_id": "ouroboros",
        "canonical_system_eligible": True,
        "system_compatibility": "native-system",
        "canonical_review_revision": "86806ee123ce8e26cc063cc1a618f975eea64f26",
        "canonical_s5_state": "A(P)",
        "ownership_mode_observed": "parent-governed",
        "comparison_class": "descriptive-only",
        "policy_change_commit": "25fbd3615a97e6ec3277c470eac9862d448aee10",
        "enactment_pr": 855,
        "enactment_merge_commit": "dd5aded8fef7884774e2ccba3802f4bf0200d124",
        "legitimate_parent_authority": "razzant",
        "owner_selected_work": True,
    }
    for field, expected in expected_canonical_fields.items():
        if canonical.get(field) != expected:
            fail(f"Ouroboros canonical observation {field} drift: {canonical.get(field)!r}")
    lineage = canonical.get("lineage") or {}
    if lineage.get("merge_commit_is_ancestor") is not True or lineage.get("canonical_revision_commits_ahead") != 673:
        fail("Ouroboros canonical lineage evidence drift")
    if not canonical.get("non_claim") or "autonomous" not in canonical["non_claim"]:
        fail("Ouroboros observation must retain autonomous-mode non-claim")

    s5_entries = [entry for entry in benchmark_map.get("entries", []) if entry.get("function") == "S5"]
    actual_map = {entry.get("benchmark_id"): entry.get("fit") for entry in s5_entries}
    for benchmark_id, expected_fit in EXPECTED_S5_MAP.items():
        actual_fit = actual_map.get(benchmark_id)
        if actual_fit != expected_fit:
            fail(f"S5 map mismatch for {benchmark_id}: expected {expected_fit}, got {actual_fit}")
    direct = [entry for entry in s5_entries if entry.get("fit") == "direct"]
    if [entry.get("benchmark_id") for entry in direct] != ["govsim-selfgovern"]:
        fail(f"unexpected direct S5 family set: {[e.get('benchmark_id') for e in direct]}")
    if direct[0].get("system_linkage") != "benchmark-scaffolded":
        fail("GovSim-SelfGovern map entry must remain benchmark-scaffolded")

    anchors = coverage.get("representative_canonical_s5_systems")
    if not isinstance(anchors, list):
        fail("representative_canonical_s5_systems must be a list")
    declared = {row.get("harness_id"): row.get("expected_state") for row in anchors if isinstance(row, dict)}
    if declared != EXPECTED_CANONICAL:
        fail(f"canonical anchor declaration mismatch: {declared!r}")
    statuses = {row.get("harness_id"): row.get("benchmark_status") for row in anchors if isinstance(row, dict)}
    if statuses != EXPECTED_BENCHMARK_STATUS:
        fail(f"canonical S5 evidence-status mismatch: {statuses!r}")

    for harness_id, expected_state in EXPECTED_CANONICAL.items():
        path = ROOT / "assessments" / f"{harness_id}.md"
        if not path.exists():
            fail(f"missing canonical assessment: {path}")
        fm = frontmatter(path)
        if fm.get("status") != "included":
            fail(f"{harness_id}: expected status included, got {fm.get('status')!r}")
        actual_state = fm.get("autonomy_s5")
        if actual_state != expected_state:
            fail(f"{harness_id}: expected autonomy_s5={expected_state}, got {actual_state!r}")

    direct_requirements = coverage.get("direct_benchmark_requirements")
    if not isinstance(direct_requirements, list) or len(direct_requirements) != 5:
        fail("direct_benchmark_requirements must preserve the five-step direct S5 chain")
    primary_requirements = coverage.get("primary_baseline_additional_requirements")
    if not isinstance(primary_requirements, list) or len(primary_requirements) != 1:
        fail("primary_baseline_additional_requirements must preserve the matched canonical gate")
    if "matched" not in primary_requirements[0].lower() or "canonical" not in primary_requirements[0].lower():
        fail("S5 primary gap must retain matched canonical-harness requirement")

    print(
        f"ok: {len(cases)} S5 coverage cases, 1 direct family, "
        "1 composed direct observation, 1 canonical direct observation, primary gap preserved"
    )


if __name__ == "__main__":
    main()
