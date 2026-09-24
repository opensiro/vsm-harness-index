#!/usr/bin/env python3
"""Validate the fail-closed public PolyBench matched-S4 preflight."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREFLIGHT = HERE / "public-polybench-preflight.json"
DOC = HERE / "PUBLIC-POLYBENCH.md"
PRIMARY_BASELINES = HERE.parents[1] / "primary-baselines.json"
CANONICAL_OBSERVATIONS = HERE.parent / "canonical_observations.json"

EXPECTED_GATES = {
    "public-cross-method-comparison": "satisfied",
    "common-polybench-stream": "satisfied",
    "common-result-surface": "satisfied",
    "mirror-independent-system-identity": "satisfied",
    "native-baseline-implementation-provenance": "blocked",
    "immutable-upstream-revision-binding": "not_reached",
    "canonical-s4-linkage": "not_reached",
    "matched-model-provider-and-budget": "not_reached",
    "ordinary-s4-regulator-freeze": "not_reached",
}
EXPECTED_METHODS = {
    "A-Evolve",
    "GEPA",
    "Meta-Harness",
    "Continual Harness",
    "SkillOS",
    "Adaptive Auto-Harness",
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


def main() -> None:
    data = load_json(PREFLIGHT)
    if not isinstance(data, dict):
        fail("public-polybench-preflight.json must contain an object")
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if data.get("status") != "experimental-non-normative":
        fail("status must remain experimental-non-normative")
    if data.get("tracking_issue") != 534:
        fail("tracking_issue must remain #534")
    if data.get("candidate_cell_id") != "adaptive-auto-harness-polybench-public-baselines-v1":
        fail("candidate_cell_id drift")
    if data.get("preflight_disposition") != "blocked":
        fail("public PolyBench preflight must remain blocked until a reviewed new revision replaces it")
    if data.get("execution_authorized") is not False:
        fail("blocked public-results preflight must not authorize execution")
    if data.get("primary_baseline_after_preflight") != "gap":
        fail("blocked preflight must preserve the S4 primary gap")
    if data.get("evidence_mode") != "public-results-only":
        fail("evidence mode must remain public-results-only")
    if data.get("results") is not None:
        fail("preflight artifact must not invent or duplicate result rows")

    evidence = data.get("candidate_evidence")
    if not isinstance(evidence, dict):
        fail("candidate_evidence object required")
    if evidence.get("public_mirror_revision") != "c1ea7d60c009519f5c037f7db9d47e97063bb353":
        fail("AdaptiveHarness mirror revision drift")
    if evidence.get("benchmark") != "PolyBench":
        fail("benchmark must remain PolyBench")
    methods = evidence.get("reported_methods")
    if not isinstance(methods, list) or set(methods) != EXPECTED_METHODS:
        fail("reported method set drift")
    for field in ("paper", "public_mirror_repository", "mirror_declared_canonical_lineage"):
        if not valid_https(evidence.get(field)):
            fail(f"{field}: valid HTTPS source required")

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
        fail("public PolyBench gate set drift")
    for gate_id, expected_status in EXPECTED_GATES.items():
        if gate_by_id[gate_id].get("status") != expected_status:
            fail(f"{gate_id}: expected status {expected_status}")

    blocker = gate_by_id["native-baseline-implementation-provenance"]
    if "not shipped" not in blocker["finding"]:
        fail("implementation-provenance finding lost released-code blocker")
    blocking_effect = blocker.get("blocking_effect")
    if not isinstance(blocking_effect, str) or "Do not admit" not in blocking_effect:
        fail("implementation-provenance blocker must explicitly prohibit admission")

    doc = DOC.read_text(encoding="utf-8") if DOC.exists() else ""
    for phrase in (
        "This is a mirror.",
        "native baseline implementation provenance: blocked",
        "execution authorized: no",
        "S4 primary baseline: gap",
        "not shipped in the released version",
    ):
        if phrase not in doc:
            fail(f"PUBLIC-POLYBENCH.md missing required statement: {phrase}")

    non_claim = data.get("non_claim")
    if not isinstance(non_claim, str) or len(non_claim.strip()) < 120:
        fail("explicit non-claim required")

    baselines = load_json(PRIMARY_BASELINES)
    s4 = baselines.get("functions", {}).get("S4", {}) if isinstance(baselines, dict) else {}
    if s4.get("status") != "gap":
        fail("public PolyBench preflight is valid only while S4 primary baseline remains gap")

    canonical_obs = load_json(CANONICAL_OBSERVATIONS)
    if not isinstance(canonical_obs, list):
        fail("canonical_observations.json must contain a list")
    canonical_ids = {obs.get("canonical_harness_id") for obs in canonical_obs if isinstance(obs, dict)}
    if not {"a-evolve", "kadath"}.issubset(canonical_ids):
        fail("expected existing A-Evolve and KADATH canonical S4 observations")

    print("ok: public PolyBench matched-S4 preflight validated")
    print("candidate: Adaptive Auto-Harness public PolyBench comparison")
    print("disposition: blocked")
    print("blocking gate: native-baseline-implementation-provenance")
    print("execution authorized: no")
    print("S4 primary baseline: gap")


if __name__ == "__main__":
    main()
