#!/usr/bin/env python3
"""Validate the fail-closed matched canonical S4 preflight."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREFLIGHT = HERE / "preflight.json"
PROTOCOL = HERE / "PROTOCOL.md"
PRIMARY_BASELINES = HERE.parents[1] / "primary-baselines.json"
CANONICAL_OBSERVATIONS = HERE.parent / "canonical_observations.json"
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)

EXPECTED_SYSTEMS = {
    "a-evolve": ("18ba996dac9843f2759b2cdf8a94022f58fbfeb9", "A"),
    "exo": ("6164288895a5851b2118492c880fb37b543e2ac6", "A(P)"),
}
EXPECTED_GATES = {
    "canonical-s4-ownership": "satisfied",
    "common-persistent-target": "satisfied",
    "skillsbench-provenance": "satisfied",
    "exact-common-model-provider": "blocked",
    "common-task-evaluator-runtime": "not_reached",
    "frozen-regulator-hash-plan": "not_reached",
    "heldout-future-use-closure": "not_reached",
}
EXPECTED_SKILLSBENCH_REF = "828bb921fb94dc065bfefd6bac4e8938be3f71e0"
EXPECTED_A_Evolve_PROTECTED = {
    "agent_evolve/algorithms/",
    "agent_evolve/benchmarks/",
    "agent_evolve/agents/skillbench/agent.py",
    "agent_evolve/config.py",
}
EXPECTED_EXO_PROTECTED = {
    "exo/harness.ts",
    "exo/prompts/me.md",
    "exo/tools/guardian-tools.ts",
    "exoharness/typescript/model-runtime/",
    "exoharness/typescript/harness/skill-tools.ts",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: {exc}")


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
    data = load_json(PREFLIGHT)
    if not isinstance(data, dict):
        fail("preflight.json must contain an object")
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if data.get("status") != "experimental-non-normative":
        fail("preflight must remain experimental-non-normative")
    if data.get("tracking_issue") != 527:
        fail("tracking_issue must remain #527")
    if data.get("candidate_cell_id") != "a-evolve-exo-skillsbench-skills-only-v1":
        fail("candidate_cell_id drift")
    if data.get("preflight_disposition") != "blocked":
        fail("current preflight must remain blocked until a reviewed new revision replaces it")
    if data.get("execution_authorized") is not False:
        fail("blocked preflight must not authorize execution")
    if data.get("primary_baseline_after_preflight") != "gap":
        fail("blocked preflight must preserve the S4 primary gap")
    if data.get("results") is not None:
        fail("preflight-only artifact must not contain execution results")

    protocol = PROTOCOL.read_text(encoding="utf-8") if PROTOCOL.exists() else ""
    for phrase in (
        "preflight: blocked",
        "execution authorized: no",
        "S4 primary baseline: gap",
        "BedrockModel",
        "provider-prefixed Bedrock/Vertex",
    ):
        if phrase not in protocol:
            fail(f"PROTOCOL.md missing required blocked-preflight statement: {phrase}")

    systems = data.get("systems")
    if not isinstance(systems, list) or len(systems) != len(EXPECTED_SYSTEMS):
        fail("systems must contain exactly A-Evolve and Exo")
    system_by_id = {item.get("harness_id"): item for item in systems if isinstance(item, dict)}
    if set(system_by_id) != set(EXPECTED_SYSTEMS):
        fail("unexpected matched-cell system set")
    for harness_id, (review_ref, s4_state) in EXPECTED_SYSTEMS.items():
        item = system_by_id[harness_id]
        if item.get("canonical_assessment_ref") != f"assessments/{harness_id}.md":
            fail(f"{harness_id}: assessment linkage drift")
        if item.get("canonical_review_revision") != review_ref:
            fail(f"{harness_id}: preflight review ref drift")
        if item.get("canonical_s4_state") != s4_state:
            fail(f"{harness_id}: preflight S4 state drift")
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"{harness_id}: canonical assessment no longer included")
        if fields.get("review_ref") != review_ref:
            fail(f"{harness_id}: canonical review_ref changed; reassess preflight")
        if fields.get("autonomy_s4") != s4_state:
            fail(f"{harness_id}: canonical S4 state changed; reassess preflight")

    membrane = data.get("candidate_membrane")
    if not isinstance(membrane, dict):
        fail("candidate_membrane object required")
    if membrane.get("benchmark_repository") != "https://github.com/benchflow-ai/skillsbench":
        fail("SkillsBench repository binding drift")
    if membrane.get("benchmark_revision") != EXPECTED_SKILLSBENCH_REF:
        fail("SkillsBench revision drift")
    if membrane.get("persistent_adaptation_target") != "skills":
        fail("first matched-cell target must remain skills-only")
    if membrane.get("split_design") != ["B0", "A", "H", "R"]:
        fail("split design drift")
    if membrane.get("result_shape") != "vector-only-no-global-score":
        fail("result shape must remain vector-only")

    gates = data.get("gates")
    if not isinstance(gates, list):
        fail("gates must be a list")
    gate_by_id: dict[str, dict] = {}
    for gate in gates:
        if not isinstance(gate, dict):
            fail("gate entries must be objects")
        gate_id = gate.get("gate_id")
        if not isinstance(gate_id, str) or not gate_id:
            fail("gate_id required")
        if gate_id in gate_by_id:
            fail(f"duplicate gate_id: {gate_id}")
        gate_by_id[gate_id] = gate
        finding = gate.get("finding")
        if not isinstance(finding, str) or len(finding.strip()) < 60:
            fail(f"{gate_id}: substantive finding required")
        sources = gate.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{gate_id}: valid HTTPS primary_sources required")
    if set(gate_by_id) != set(EXPECTED_GATES):
        fail("preflight gate set drift")
    for gate_id, expected_status in EXPECTED_GATES.items():
        if gate_by_id[gate_id].get("status") != expected_status:
            fail(f"{gate_id}: expected status {expected_status}")

    model_gate = gate_by_id["exact-common-model-provider"]
    blocking_effect = model_gate.get("blocking_effect")
    if not isinstance(blocking_effect, str) or "Do not execute" not in blocking_effect:
        fail("model/provider blocker must explicitly prohibit execution")
    model_finding = model_gate["finding"]
    for marker in ("BedrockModel", "Vertex", "provider-prefixed Bedrock/Vertex"):
        if marker not in model_finding:
            fail(f"model/provider finding missing {marker}")

    protected = data.get("protected_surfaces")
    if not isinstance(protected, dict):
        fail("protected_surfaces required")
    if set(protected.get("a-evolve", [])) != EXPECTED_A_Evolve_PROTECTED:
        fail("A-Evolve protected-surface set drift")
    if set(protected.get("exo", [])) != EXPECTED_EXO_PROTECTED:
        fail("Exo protected-surface set drift")

    excluded = data.get("excluded_substitution")
    if not isinstance(excluded, dict) or excluded.get("harness_id") != "kadath":
        fail("KADATH exclusion record required")
    if "user-authored benchmark file or script" not in str(excluded.get("reason", "")):
        fail("KADATH exclusion reason lost native benchmark-contract boundary")
    if not valid_https(excluded.get("primary_source")):
        fail("KADATH exclusion primary_source invalid")

    non_claim = data.get("non_claim")
    if not isinstance(non_claim, str) or len(non_claim.strip()) < 100:
        fail("explicit preflight non-claim required")

    baselines = load_json(PRIMARY_BASELINES)
    s4 = baselines.get("functions", {}).get("S4", {}) if isinstance(baselines, dict) else {}
    if s4.get("status") != "gap":
        fail("matched preflight is valid only while S4 primary baseline remains gap")

    canonical_obs = load_json(CANONICAL_OBSERVATIONS)
    if not isinstance(canonical_obs, list):
        fail("canonical_observations.json must contain a list")
    canonical_ids = {obs.get("canonical_harness_id") for obs in canonical_obs if isinstance(obs, dict)}
    if not {"a-evolve", "kadath"}.issubset(canonical_ids):
        fail("expected existing A-Evolve and KADATH canonical S4 observations")

    print("ok: matched canonical S4 preflight validated")
    print("candidate: A-Evolve x Exo / SkillsBench / skills-only")
    print("disposition: blocked")
    print("blocking gate: exact-common-model-provider")
    print("execution authorized: no")
    print("S4 primary baseline: gap")


if __name__ == "__main__":
    main()
