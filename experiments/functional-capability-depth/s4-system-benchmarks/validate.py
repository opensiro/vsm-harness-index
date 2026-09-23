#!/usr/bin/env python3
"""Validate the experimental direct-S4 coverage and S4-proxy system observations."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"
COVERAGE = HERE / "coverage.json"
BENCHMARK_OBSERVATIONS = HERE / "benchmark_observations.json"
CANONICAL_OBSERVATIONS = HERE / "canonical_observations.json"
PROXY_OBSERVATIONS = HERE / "proxy_observations.json"

DIRECT_S4 = {
    "a-evolve-harness-evolution",
    "skillevolbench",
    "evoharnessbench-self-evolving",
}
COVERAGE_CLASSES = {
    "direct-composed",
    "task-solver-not-adaptation-owner",
    "proxy-scaffolded",
    "proxy-observation-specific",
    "candidate-native-no-direct-results",
    "domain-native-no-matched-baseline",
    "native-adaptation-boundary-needs-freeze",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
REQUIRED_CASE_IDS = {
    "a-evolve-direct-composed",
    "skillevolbench-direct-composed",
    "evoharnessbench-self-evolving-direct-composed",
    "skillevolbench-codex-task-solver-not-owner",
    "skilllearnbench-proxy-scaffolded",
    "futuresim-proxy",
    "kadath-native-s4-no-standardized-results",
    "super-agent-tone-mirror-native-no-results",
    "bossconsole-tool-evolver-native-no-results",
    "exo-native-s4-boundary-needs-freeze",
    "headcount-strategy-domain-no-baseline",
    "henterprise-strategy-domain-no-baseline",
    "omniscientist-research-domain-no-baseline",
}
FUTURESIM_COMPARABILITY = "futuresim-v1-recommended-harness-cross-system-confounded"
EXPECTED_FUTURESIM = {
    "futuresim-v1-codex-0125-gpt55": ("codex", "0.125.0", 25, 0.05),
    "futuresim-v1-claude-code-21132-opus46": ("claude-code", "2.1.132", 20, 0.02),
    "futuresim-v1-claude-code-21132-deepseek-v4-pro": ("claude-code", "2.1.132", 13, -0.02),
    "futuresim-v1-claude-code-21132-glm51": ("claude-code", "2.1.132", 10, -0.01),
    "futuresim-v1-opencode-1411-qwen36plus": ("opencode", "1.4.11", 5, -0.07),
}
FUTURESIM_SYSTEMS = {"codex", "claude-code", "opencode"}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def assessment_fields(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    if not path.exists():
        fail(f"missing canonical assessment: {harness_id}")
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"assessment {harness_id} has no front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def main() -> None:
    benchmark_map = json.loads(MAP.read_text(encoding="utf-8"))
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))
    canonical_observations = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))
    proxy_observations = json.loads(PROXY_OBSERVATIONS.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S4":
        fail("coverage function must be S4")

    direct_s4 = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S4" and entry.get("fit") == "direct"
    }
    if direct_s4 != DIRECT_S4:
        fail(f"unexpected direct S4 benchmark map: {sorted(direct_s4)}")

    futuresim_map = [
        entry for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S4" and entry.get("benchmark_id") == "futuresim"
    ]
    if len(futuresim_map) != 1 or futuresim_map[0].get("fit") != "proxy":
        fail("FutureSim must remain proxy for S4")

    skilllearn = [
        entry for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S4" and entry.get("benchmark_id") == "skilllearnbench"
    ]
    if len(skilllearn) != 1 or skilllearn[0].get("fit") != "proxy":
        fail("SkillLearnBench must remain proxy pending a stricter future-transfer review")

    if not isinstance(benchmark_observations, list):
        fail("benchmark_observations.json must contain a list")
    if not isinstance(canonical_observations, list):
        fail("canonical_observations.json must contain a list")
    if not isinstance(proxy_observations, list):
        fail("proxy_observations.json must contain a list")
    if canonical_observations:
        fail("direct canonical S4 registry must remain empty")

    if coverage.get("direct_benchmark_family_count") != len(DIRECT_S4):
        fail("direct_benchmark_family_count mismatch")
    if coverage.get("composed_direct_observation_count") != len(benchmark_observations):
        fail("composed_direct_observation_count mismatch")
    if coverage.get("canonical_direct_observation_count") != len(canonical_observations):
        fail("canonical_direct_observation_count mismatch")
    if coverage.get("proxy_observation_count") != len(proxy_observations):
        fail("proxy_observation_count mismatch")
    if set(coverage.get("proxy_systems_observed", [])) != FUTURESIM_SYSTEMS:
        fail("proxy_systems_observed mismatch")

    if len(benchmark_observations) != 3:
        fail("expected exactly three reviewed composed direct S4 evidence records")

    observation_ids: set[str] = set()
    observed_families: set[str] = set()
    for obs in benchmark_observations:
        observation_id = obs.get("observation_id")
        if not isinstance(observation_id, str) or not observation_id:
            fail("benchmark observation requires observation_id")
        if observation_id in observation_ids:
            fail(f"duplicate observation_id: {observation_id}")
        observation_ids.add(observation_id)

        if obs.get("function") != "S4":
            fail(f"{observation_id}: function must be S4")
        benchmark_id = obs.get("benchmark_id")
        if benchmark_id not in DIRECT_S4:
            fail(f"{observation_id}: benchmark is not reviewed direct S4")
        observed_families.add(benchmark_id)
        if obs.get("benchmark_fit") != "direct":
            fail(f"{observation_id}: benchmark_fit must be direct")
        if obs.get("canonical_harness_id") is not None:
            fail(f"{observation_id}: composed evidence must not claim canonical_harness_id")
        if obs.get("canonical_system_eligible") is not False:
            fail(f"{observation_id}: composed evidence must be canonical-ineligible")
        if obs.get("system_compatibility") != "benchmark-scaffolded":
            fail(f"{observation_id}: composed evidence must remain benchmark-scaffolded")
        sources = obs.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{observation_id}: invalid primary_sources")

    if observed_families != DIRECT_S4:
        fail("benchmark observations must cover every reviewed direct S4 family exactly once")

    proxy_ids: set[str] = set()
    proxy_systems: set[str] = set()
    for obs in proxy_observations:
        observation_id = obs.get("observation_id")
        if observation_id not in EXPECTED_FUTURESIM:
            fail(f"unexpected FutureSim proxy observation: {observation_id!r}")
        if observation_id in proxy_ids:
            fail(f"duplicate FutureSim proxy observation_id: {observation_id}")
        proxy_ids.add(observation_id)

        expected_harness, expected_version, expected_accuracy, expected_bss = EXPECTED_FUTURESIM[observation_id]
        if obs.get("function") != "S4" or obs.get("benchmark_id") != "futuresim":
            fail(f"{observation_id}: must be an S4/FutureSim observation")
        if obs.get("benchmark_fit") != "proxy":
            fail(f"{observation_id}: FutureSim benchmark_fit must remain proxy")
        if obs.get("system_compatibility") != "adapter-preserved":
            fail(f"{observation_id}: expected adapter-preserved compatibility")
        if obs.get("canonical_harness_id") != expected_harness:
            fail(f"{observation_id}: canonical_harness_id mismatch")
        if obs.get("canonical_assessment_ref") != f"assessments/{expected_harness}.md":
            fail(f"{observation_id}: canonical_assessment_ref mismatch")
        if obs.get("canonical_s4_state_at_review") != "—":
            fail(f"{observation_id}: canonical_s4_state_at_review must be —")
        if obs.get("published_harness_version") != expected_version:
            fail(f"{observation_id}: published harness version mismatch")
        if obs.get("final_top1_accuracy_percent") != expected_accuracy:
            fail(f"{observation_id}: top-1 accuracy mismatch")
        if obs.get("final_brier_skill_score") != expected_bss:
            fail(f"{observation_id}: Brier skill score mismatch")
        if obs.get("question_count") != 330 or obs.get("seeds") != 3:
            fail(f"{observation_id}: expected 330 questions and 3 seeds")
        if obs.get("reasoning_setting") != "maximum reasoning effort":
            fail(f"{observation_id}: reasoning setting mismatch")
        if obs.get("comparability_group") != FUTURESIM_COMPARABILITY:
            fail(f"{observation_id}: comparability group mismatch")
        confounders = obs.get("confounders")
        if not isinstance(confounders, list) or not confounders:
            fail(f"{observation_id}: explicit confounders required")
        sources = obs.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{observation_id}: invalid primary_sources")
        non_claim = obs.get("non_claim")
        if not isinstance(non_claim, str) or len(non_claim.strip()) < 40:
            fail(f"{observation_id}: explicit non-claim required")

        fields = assessment_fields(expected_harness)
        if fields.get("status") != "included":
            fail(f"{observation_id}: canonical assessment not included")
        if fields.get("autonomy_s4") != "—":
            fail(
                f"{observation_id}: canonical {expected_harness} no longer has S4=—; "
                "review the negative-control interpretation"
            )
        proxy_systems.add(expected_harness)

    if proxy_ids != set(EXPECTED_FUTURESIM):
        fail("FutureSim proxy observation set is incomplete")
    if proxy_systems != FUTURESIM_SYSTEMS:
        fail("FutureSim canonical proxy-system set mismatch")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be non-empty")
    seen_cases: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in seen_cases:
            fail(f"duplicate case_id: {case_id}")
        seen_cases.add(case_id)
        by_id[case_id] = case

        coverage_class = case.get("coverage_class")
        if coverage_class not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if case.get("admitted_to_canonical_registry") is not False:
            fail(f"{case_id}: coverage case must remain non-admitted")
        if not isinstance(case.get("finding"), str) or len(case["finding"].strip()) < 40:
            fail(f"{case_id}: explicit finding required")
        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{case_id}: invalid primary_sources")

        harness_id = case.get("canonical_harness_id")
        fields = None
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment not included")

        if coverage_class == "task-solver-not-adaptation-owner":
            if fields is None or fields.get("autonomy_s4") != "—":
                fail(
                    f"{case_id}: negative-control task solver no longer has S4=—; "
                    "review the boundary before retaining this case"
                )

        if coverage_class == "candidate-native-no-direct-results":
            if fields is None or fields.get("autonomy_s4") in {None, "—", "?"}:
                fail(f"{case_id}: native-no-results candidate must currently establish S4")
            if case.get("system_compatibility") != "native-system":
                fail(f"{case_id}: native-no-results candidate must be native-system")
            if case.get("benchmark_fit") != "candidate-direct":
                fail(f"{case_id}: native-no-results candidate fit drift")

        if coverage_class == "domain-native-no-matched-baseline":
            if fields is None or fields.get("autonomy_s4") in {None, "—", "?"}:
                fail(f"{case_id}: domain candidate must currently establish S4")
            if case.get("system_compatibility") != "native-system":
                fail(f"{case_id}: domain candidate must be native-system")
            if case.get("benchmark_fit") != "candidate-domain-direct":
                fail(f"{case_id}: domain candidate fit drift")
            if case.get("domain") not in {"strategy", "research-science"}:
                fail(f"{case_id}: unreviewed S4 domain")

        if coverage_class == "native-adaptation-boundary-needs-freeze":
            if harness_id != "exo":
                fail(f"{case_id}: current frozen-regulator boundary case must remain Exo")
            if fields is None or fields.get("autonomy_s4") in {None, "—", "?"}:
                fail(f"{case_id}: frozen-regulator candidate must currently establish S4")
            if case.get("system_compatibility") != "native-system":
                fail(f"{case_id}: frozen-regulator candidate must be native-system")
            if case.get("benchmark_fit") != "candidate-direct":
                fail(f"{case_id}: frozen-regulator candidate fit drift")
            if case.get("ordinary_s4_baseline_rule") != (
                "freeze-s4-regulator; permit persistent change only to the declared adaptation target"
            ):
                fail(f"{case_id}: ordinary S4 frozen-regulator rule drift")

    missing_cases = REQUIRED_CASE_IDS - seen_cases
    if missing_cases:
        fail(f"required S4 coverage cases missing: {sorted(missing_cases)}")

    kadath = by_id["kadath-native-s4-no-standardized-results"]
    if not isinstance(kadath.get("ordinary_s4_boundary"), str) or len(kadath["ordinary_s4_boundary"].strip()) < 40:
        fail("KADATH ordinary-S4 boundary note is required")

    expected_domain_cases = {
        "headcount-strategy-domain-no-baseline": ("headcount", "strategy"),
        "henterprise-strategy-domain-no-baseline": ("henterprise", "strategy"),
        "omniscientist-research-domain-no-baseline": ("omniscientist", "research-science"),
    }
    for case_id, (harness_id, domain) in expected_domain_cases.items():
        case = by_id[case_id]
        if case.get("canonical_harness_id") != harness_id or case.get("domain") != domain:
            fail(f"{case_id}: domain/canonical linkage drift")

    representative = coverage.get("representative_canonical_s4_systems_inspected")
    states = coverage.get("canonical_states_at_review")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S4 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative cohort")
    if not isinstance(states, dict) or set(states) != set(representative):
        fail("canonical_states_at_review must match representative cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"{harness_id}: assessment not included")
        current = fields.get("autonomy_s4")
        if current in {None, "—", "?"}:
            fail(f"{harness_id}: current canonical assessment does not establish S4")
        if current != states[harness_id]:
            fail(f"{harness_id}: S4 state drifted from {states[harness_id]!r} to {current!r}")

    print("ok: S4 benchmark coverage validated")
    print(f"reviewed direct S4 families: {len(direct_s4)}")
    print(f"composed direct evidence records: {len(benchmark_observations)}")
    print(f"canonical direct observations: {len(canonical_observations)}")
    print(f"FutureSim proxy observations: {len(proxy_observations)}")
    print(f"FutureSim canonical proxy systems: {len(proxy_systems)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S4 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
