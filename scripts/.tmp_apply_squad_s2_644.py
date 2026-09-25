#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments/functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
OBS = S2 / "observations.json"
COV = S2 / "coverage.json"
CLOSURE = S2 / "matched-cell/s2-primary-search-closure.json"
BASELINES = EXP / "primary-baselines.json"
VALIDATE = S2 / "validate.py"
CLOSURE_VALIDATE = S2 / "matched-cell/validate_s2_primary_search_closure.py"
README = S2 / "README.md"
TEST = ROOT / "tests/test_s2_post_closure_shep_axocoatl.py"
REVIEW = S2 / "SQUAD-DIRECT-REVIEW.md"

OBS_ID = "squad-shared-state-conflict-attenuation-2026-03"
CASE_ID = "squad-shared-state-conflict-direct-native-canonical"
REF = "2099faf51c08a912c359209447011b06decf0565"
COMMITS = [
    "34925f2f5bec49742216ab9dd93c756fbe1aa8c9",
    "e7e6255aa84e04993d568a10331bf9da6661b478",
    "6e304ec6d2f1d385226fba074a1192a3eab7b5cb",
]
BLOG = "https://www.tamirdresher.com/blog/2026/03/17/scaling-ai-part4-distributed"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing expected source fragment for {label}")
    if text.count(old) != 1:
        raise SystemExit(f"expected one source fragment for {label}, got {text.count(old)}")
    return text.replace(old, new, 1)


# Raw observation registry: add one descriptive canonical row, no benchmark family.
obs = load(OBS)
if any(row.get("observation_id") == OBS_ID for row in obs):
    raise SystemExit("Squad observation already present on source branch")
obs.append(
    {
        "observation_id": OBS_ID,
        "function": "S2",
        "benchmark_id": None,
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "canonical-squad-project-team",
        "canonical_harness_id": "squad",
        "canonical_system_eligible": True,
        "canonical_assessment_ref": REF,
        "canonical_state_at_review": "A",
        "system_compatibility": "native-system",
        "comparison_class": "descriptive-only",
        "evidence_surface": "immutable first-party repository history plus first-party public operational case study",
        "operational_commits": COMMITS,
        "case_study_date": "2026-03-17",
        "disturbance": "Parallel Squad S1 agents append to shared team-state and decision surfaces; simultaneous completion can create merge interference on canonical shared state.",
        "coordination_relation": "Squad's first-party merge=union rules preserve concurrent append-only team-state contributions, while per-agent decision inbox files and Scribe consolidation separate structured concurrent writes before returning them to canonical decisions.md.",
        "subsequent_operation": "First-party operational history records decision-inbox consolidation followed by later multi-PR release work with team state preserved via merge=union.",
        "comparison_limitation": "This is descriptive canonical direct evidence from operational history, not a matched benchmark comparison or a causal numeric uplift estimate.",
        "vsm_interpretation": "This is direct descriptive S2 capability evidence at the canonical Squad project-team boundary. Distinct parallel S1 agents generate interaction-specific shared-state interference; native merge=union and Scribe/inbox coordination attenuate that interference and preserve/consolidate state for subsequent operation. It does not create a benchmark family or a matched cross-harness primary cell.",
        "primary_sources": [
            f"https://github.com/bradygaster/squad/tree/{REF}",
            *[f"https://github.com/bradygaster/squad/commit/{sha}" for sha in COMMITS],
            BLOG,
        ],
    }
)
dump(OBS, obs)

# Coverage: preserve the existing quantitative MARBLE proxy and add a separate direct descriptive case.
cov = load(COV)
cov["direct_observation_count"] = len(obs)
canonical_obs = [row for row in obs if row.get("canonical_system_eligible") is True]
cov["canonical_direct_observation_count"] = len(canonical_obs)
if "direct-native-canonical" not in cov["coverage_classes"]:
    insertion = cov["coverage_classes"].index("direct-native-noncanonical") + 1
    cov["coverage_classes"].insert(insertion, "direct-native-canonical")
if any(row.get("case_id") == CASE_ID for row in cov["cases"]):
    raise SystemExit("Squad direct coverage case already present")
case = {
    "case_id": CASE_ID,
    "benchmark": "Squad shared-state conflict attenuation operational evidence",
    "benchmark_fit": "direct",
    "coverage_class": "direct-native-canonical",
    "system_compatibility": "native-system",
    "canonical_harness_id": "squad",
    "canonical_state_at_review": "A",
    "canonical_review_ref": REF,
    "observation_ref": f"observations.json#{OBS_ID}",
    "primary_sources": [
        f"https://github.com/bradygaster/squad/tree/{REF}",
        *[f"https://github.com/bradygaster/squad/commit/{sha}" for sha in COMMITS],
        BLOG,
    ],
    "finding": "Canonical Squad S2=A is independently established by the assessment. First-party operational history and a public case study record real concurrent shared-state merge interference, native merge=union preservation, per-agent decision inboxes and Scribe consolidation, followed by subsequent project/release operation with team state preserved. This is direct descriptive native S2 evidence, not a new benchmark family or matched causal comparison.",
    "admitted": False,
}
idx = next(i for i, row in enumerate(cov["cases"]) if row.get("case_id") == "squad-marble-native-proxy")
cov["cases"].insert(idx + 1, case)
dump(COV, cov)

# Primary-search closure: canonical layer is no longer empty, but still has no matched primary cell.
closure = load(CLOSURE)
closure["squad_canonical_direct_issue"] = 644
closure["evidence_depth"]["direct_observations"] = len(obs)
closure["evidence_depth"]["canonical_direct_observations"] = len(canonical_obs)
families = closure["evidence_depth"]["direct_benchmark_families"]
closure["closure_claim"] = (
    f"Current public evidence contains {families} direct S2 disturbance/attenuation benchmark families, "
    f"{len(obs)} direct observations, one canonical native descriptive direct observation (Squad), and "
    f"{closure['evidence_depth']['native_proxy_projections']} native quantitative S2 proxy projections. "
    "The canonical layer is therefore no longer empty, but public evidence still lacks a materially matched "
    "direct comparison across two or more canonical S2 systems, so no primary baseline is selected."
)
closure["reopen_when"] = [
    "a second canonical S2 harness publishes a direct native or adapter-preserved inter-S1 disturbance-to-attenuation result that can form a materially comparable cell with existing canonical evidence",
    "a materially matched benchmark evaluates two or more canonical systems exercising their own native or adapter-preserved S2 paths under one disturbance definition",
    "MAO-Bench or a comparable benchmark publishes recoverable multi-orchestrator results with immutable system/model/configuration provenance and direct S2 semantics",
]
closure["non_claim"] = (
    "This closure is not a zero S2 capability score and does not downgrade canonical S2 ownership. Squad now "
    "supplies one canonical native descriptive direct observation; Nool, The Specification Gap, CodeCRDT and "
    "Grit remain direct non-canonical observations at their reviewed boundaries. One descriptive canonical row "
    "is not a matched cross-harness primary; S2 primary remains a gap until materially matched canonical evidence appears."
)
dump(CLOSURE, closure)

# Primary baseline metadata only; status remains gap and direct family set is unchanged.
baselines = load(BASELINES)
s2b = baselines["functions"]["S2"]
assert s2b["status"] == "gap"
assert len(s2b["reviewed_direct_families"]) == families
s2b["blocking_reason"] = (
    f"Reviewed direct S2 evidence includes {families} disturbance/attenuation benchmark families. Nool and The "
    "Specification Gap provide benchmark-scaffolded direct non-canonical observations; CodeCRDT and Grit provide "
    "direct observations at their own non-canonical native product boundaries; and Squad now provides one canonical "
    "native descriptive direct observation from first-party operational history. Twining lacks recoverable exact "
    "treatment revision and CooperBench lacks pinned flash-run logs for observation admission. One canonical descriptive "
    "row is not a materially matched cross-harness comparison, so public evidence still provides no matched primary cell "
    "across multiple canonical native S2 implementations."
)
dump(BASELINES, baselines)

# S2 validator: add the canonical class and bind the Squad observation to current canonical assessment state.
s = VALIDATE.read_text(encoding="utf-8")
s = replace_once(
    s,
    '    "direct-native-noncanonical",\n    "native-proxy",',
    '    "direct-native-noncanonical",\n    "direct-native-canonical",\n    "native-proxy",',
    "coverage class",
)
s = replace_once(
    s,
    '    if len(observations) != 4:\n        fail("S2 observations.json must contain exactly four direct non-canonical observations")\n    if coverage.get("direct_observation_count") != len(observations):\n        fail("direct_observation_count does not match observations.json")\n    if coverage.get("canonical_direct_observation_count") != 0:\n        fail("S2 canonical_direct_observation_count must remain 0")',
    '    if len(observations) != 5:\n        fail("S2 observations.json must contain exactly five direct observations")\n    if coverage.get("direct_observation_count") != len(observations):\n        fail("direct_observation_count does not match observations.json")\n    canonical_observations = [row for row in observations if row.get("canonical_system_eligible") is True]\n    if coverage.get("canonical_direct_observation_count") != len(canonical_observations):\n        fail("canonical_direct_observation_count does not match canonical direct observations")\n    if len(canonical_observations) != 1:\n        fail("S2 must retain exactly one canonical direct observation in this snapshot")',
    "observation counts",
)
validate_fn = '''\n\ndef validate_squad_canonical_observation(observations: list[dict]) -> None:\n    observation = observation_by_id(observations, "squad-shared-state-conflict-attenuation-2026-03")\n    expected = {\n        "function": "S2",\n        "benchmark_id": None,\n        "benchmark_fit": "direct",\n        "evidence_source_class": "first-party-reported",\n        "boundary_class": "canonical-squad-project-team",\n        "canonical_harness_id": "squad",\n        "canonical_system_eligible": True,\n        "canonical_assessment_ref": "2099faf51c08a912c359209447011b06decf0565",\n        "canonical_state_at_review": "A",\n        "system_compatibility": "native-system",\n        "comparison_class": "descriptive-only",\n    }\n    for field, value in expected.items():\n        if observation.get(field) != value:\n            fail(f"Squad canonical direct S2 observation {field} drift: {observation.get(field)!r}")\n    fields = assessment_fields("squad")\n    if fields.get("status") != "included":\n        fail("Squad canonical assessment no longer included")\n    if fields.get("review_ref") != expected["canonical_assessment_ref"]:\n        fail("Squad canonical assessment ref drift")\n    if fields.get("autonomy_s2") != "A":\n        fail("Squad canonical S2 state drift")\n    if observation.get("operational_commits") != [\n        "34925f2f5bec49742216ab9dd93c756fbe1aa8c9",\n        "e7e6255aa84e04993d568a10331bf9da6661b478",\n        "6e304ec6d2f1d385226fba074a1192a3eab7b5cb",\n    ]:\n        fail("Squad operational evidence lineage drift")\n    sources = observation.get("primary_sources")\n    if not isinstance(sources, list) or len(sources) < 5 or any(not valid_https(source) for source in sources):\n        fail("Squad canonical direct observation must retain public HTTPS provenance")\n'''
s = replace_once(s, '\n\ndef main() -> None:\n', validate_fn + '\n\ndef main() -> None:\n', "Squad validator function")
coverage_check = '''    squad_direct = by_id.get("squad-shared-state-conflict-direct-native-canonical")\n    if squad_direct is None:\n        fail("missing Squad canonical direct-S2 coverage case")\n    if squad_direct.get("benchmark_fit") != "direct" or squad_direct.get("coverage_class") != "direct-native-canonical":\n        fail("Squad operational evidence must remain direct-native-canonical S2")\n    if squad_direct.get("system_compatibility") != "native-system" or squad_direct.get("canonical_harness_id") != "squad":\n        fail("Squad canonical direct S2 linkage drift")\n    if squad_direct.get("canonical_state_at_review") != "A" or squad_direct.get("canonical_review_ref") != "2099faf51c08a912c359209447011b06decf0565":\n        fail("Squad canonical direct S2 assessment anchor drift")\n    if squad_direct.get("observation_ref") != "observations.json#squad-shared-state-conflict-attenuation-2026-03":\n        fail("Squad canonical direct coverage/observation linkage drift")\n\n'''
s = replace_once(
    s,
    '    codecrdt = by_id.get("codecrdt-observation-driven-direct-native-noncanonical")',
    coverage_check + '    codecrdt = by_id.get("codecrdt-observation-driven-direct-native-noncanonical")',
    "Squad coverage validation",
)
s = replace_once(
    s,
    '    validate_grit_observation(observations)\n    validate_proxy_links(coverage, by_id)',
    '    validate_grit_observation(observations)\n    validate_squad_canonical_observation(observations)\n    validate_proxy_links(coverage, by_id)',
    "Squad observation validation call",
)
VALIDATE.write_text(s, encoding="utf-8")

# Closure validator: bind the new canonical row without weakening existing non-canonical checks.
s = CLOSURE_VALIDATE.read_text(encoding="utf-8")
s = replace_once(
    s,
    'require(closure["grit_public_evidence_issue"] == 663, "S2 Grit public-evidence issue drift")',
    'require(closure["grit_public_evidence_issue"] == 663, "S2 Grit public-evidence issue drift")\nrequire(closure["squad_canonical_direct_issue"] == 644, "S2 Squad canonical-direct issue drift")',
    "closure issue binding",
)
s = replace_once(
    s,
    '    "squad-marble-native-proxy",\n    "deepseek-harness-native-mechanism-no-direct-benchmark",',
    '    "squad-marble-native-proxy",\n    "squad-shared-state-conflict-direct-native-canonical",\n    "deepseek-harness-native-mechanism-no-direct-benchmark",',
    "closure required case",
)
s = replace_once(
    s,
    'require(len(observations) == 4, "S2 closure expects four direct non-canonical observations")',
    'require(len(observations) == 5, "S2 closure expects five direct observations")',
    "closure observation count",
)
s = replace_once(
    s,
    '        "grit-synthetic-merge-contention-2026-04",\n    },',
    '        "grit-synthetic-merge-contention-2026-04",\n        "squad-shared-state-conflict-attenuation-2026-03",\n    },',
    "closure observation ids",
)
old_loop = '''for observation_id, (benchmark_id, compatibility) in {\n    "nool-trackd-scaleup1-contention-2026-08-21": ("nool-fleet-coordination", "benchmark-scaffolded"),\n    "specification-gap-recovery-2026-03": ("specification-gap-recovery", "benchmark-scaffolded"),\n    "codecrdt-parallel-convergence-2025-10": ("codecrdt-observation-coordination", "native-system"),\n    "grit-synthetic-merge-contention-2026-04": ("grit-merge-contention", "native-system"),\n}.items():\n    observation = observation_rows[observation_id]\n    require(observation["benchmark_id"] == benchmark_id, f"{observation_id}: benchmark drift")\n    require(observation["canonical_harness_id"] is None, f"{observation_id}: must remain non-canonical")\n    require(observation["canonical_system_eligible"] is False, f"{observation_id}: must remain non-canonical")\n    require(observation["system_compatibility"] == compatibility, f"{observation_id}: system compatibility drift")'''
new_loop = '''for observation_id, (benchmark_id, compatibility) in {\n    "nool-trackd-scaleup1-contention-2026-08-21": ("nool-fleet-coordination", "benchmark-scaffolded"),\n    "specification-gap-recovery-2026-03": ("specification-gap-recovery", "benchmark-scaffolded"),\n    "codecrdt-parallel-convergence-2025-10": ("codecrdt-observation-coordination", "native-system"),\n    "grit-synthetic-merge-contention-2026-04": ("grit-merge-contention", "native-system"),\n    "squad-shared-state-conflict-attenuation-2026-03": (None, "native-system"),\n}.items():\n    observation = observation_rows[observation_id]\n    require(observation["benchmark_id"] == benchmark_id, f"{observation_id}: benchmark drift")\n    require(observation["system_compatibility"] == compatibility, f"{observation_id}: system compatibility drift")\n    if observation_id == "squad-shared-state-conflict-attenuation-2026-03":\n        require(observation["canonical_harness_id"] == "squad", "Squad canonical observation identity drift")\n        require(observation["canonical_system_eligible"] is True, "Squad canonical observation eligibility drift")\n        require(observation.get("canonical_assessment_ref") == "2099faf51c08a912c359209447011b06decf0565", "Squad canonical observation ref drift")\n        require(observation.get("canonical_state_at_review") == "A", "Squad canonical observation S2 state drift")\n    else:\n        require(observation["canonical_harness_id"] is None, f"{observation_id}: must remain non-canonical")\n        require(observation["canonical_system_eligible"] is False, f"{observation_id}: must remain non-canonical")'''
s = replace_once(s, old_loop, new_loop, "closure canonical/noncanonical observation loop")
s = replace_once(
    s,
    'require(\n    observation_rows["grit-synthetic-merge-contention-2026-04"].get("evidence_source_class") == "first-party-reported",\n    "Grit direct observation must remain first-party-reported",\n)\n',
    'require(\n    observation_rows["grit-synthetic-merge-contention-2026-04"].get("evidence_source_class") == "first-party-reported",\n    "Grit direct observation must remain first-party-reported",\n)\nrequire(\n    observation_rows["squad-shared-state-conflict-attenuation-2026-03"].get("comparison_class") == "descriptive-only",\n    "Squad canonical direct observation must remain descriptive-only",\n)\nrequire(\n    observation_rows["squad-shared-state-conflict-attenuation-2026-03"].get("evidence_source_class") == "first-party-reported",\n    "Squad canonical direct observation must remain first-party-reported",\n)\n',
    "closure Squad source/class checks",
)
CLOSURE_VALIDATE.write_text(s, encoding="utf-8")

# Existing post-closure delta regression follows the mutable global canonical count.
s = TEST.read_text(encoding="utf-8")
s = replace_once(
    s,
    '        self.assertEqual(coverage["canonical_direct_observation_count"], 0)',
    '        self.assertEqual(coverage["canonical_direct_observation_count"], 1)',
    "post-closure canonical observation count",
)
TEST.write_text(s, encoding="utf-8")

# Focused review artifact; this records evidence/interpretation, not a new canonical assessment.
REVIEW.write_text(
    '''# Squad canonical direct S2 public-evidence review\n\nStatus: **experimental, non-normative capability evidence**  \nTracking issue: #644\n\n## Boundary\n\nCanonical system: `squad`  \nCanonical assessment ref: `2099faf51c08a912c359209447011b06decf0565`  \nCanonical state at review: `S2=A`\n\nThis review does not change the canonical assessment. It asks whether already-public operational evidence shows the canonical Squad coordination relation attenuating an interaction-generated S2 disturbance.\n\n## Evidence chain\n\n1. `34925f2f5bec49742216ab9dd93c756fbe1aa8c9` introduces worktree-aware shared-state coordination and `merge=union` for append-only team-state surfaces so concurrent branch contributions combine without manual conflict resolution.\n2. `e7e6255aa84e04993d568a10331bf9da6661b478` is an operational Scribe session that merges 12 decision-inbox files, consolidates three overlapping decisions and deletes inbox files after merge.\n3. `6e304ec6d2f1d385226fba074a1192a3eab7b5cb` records later project operation: three PRs merged, eight issues closed, a release wave completed, four inbox decisions merged and team state preserved through `merge=union`.\n4. All three commits are direct ancestors of the canonical review ref.\n5. The canonical review ref retains `.squad/decisions.md`, agent histories, logs and orchestration logs under `merge=union`.\n6. Tamir Dresher's first-party March 17, 2026 operational case study explicitly records four parallel Squad agents, simultaneous writes to `.squad/decisions.md`, a real merge conflict, `merge=union` preserving both contributions, and the unique-inbox/Scribe consolidation pattern for structured decisions.\n\n## Functional mapping\n\n```text\nparallel Squad S1 agents\n→ concurrent shared team-state writes\n→ merge interference on shared state\n→ native merge=union and inbox/Scribe coordination\n→ both contributions preserved / structured decisions consolidated\n→ later project and release work proceeds with shared state intact\n```\n\nThis is direct descriptive S2 evidence at the canonical Squad project-team boundary. The disturbance is generated by interaction among distinct S1s; the attenuation relation is first-party and native; operational history establishes return to later work.\n\n## Classification\n\n- evidence source: `first-party-reported`;\n- benchmark family: none;\n- benchmark fit: `direct`;\n- compatibility: `native-system`;\n- canonical harness: `squad`;\n- canonical system eligible: true;\n- comparison class: `descriptive-only`.\n\nThe evidence supports a canonical direct observation but not a numeric effect size or a matched cross-harness comparison. It therefore does not select an S2 primary baseline.\n\n## Separation from MARBLE\n\nThe existing Squad/MARBLE projection remains a **native quantitative proxy**. MARBLE evaluates completion, milestone and judged-quality outcomes under controlled Squad ablations, but does not expose an explicit inter-S1 disturbance variable. This operational observation is separate and does not relabel MARBLE as direct.\n\n## Result\n\nThe S2 canonical evidence layer moves from zero to one direct canonical observation. The direct benchmark-family count is unchanged. S2 primary remains `gap` until materially matched direct evidence exists across at least two canonical systems.\n''',
    encoding="utf-8",
)

# Refresh human-readable S2 overview from the current source-of-truth counts.
s = README.read_text(encoding="utf-8")
start = s.index("## Current result\n")
end = s.index("\n## Evidence separation\n", start)
family_count = cov["direct_benchmark_family_count"]
replacement = f'''## Current result\n\n```text\ndirect S2 benchmark families reviewed:          {family_count}\ndirect S2 observations:                         {len(obs)}\ncanonical native direct-S2 observations:        {len(canonical_obs)}\nnative canonical proxy projections:             {cov["proxy_projection_count"]}\nprimary S2 baseline:                             gap\n```\n\nThe direct benchmark-family set is unchanged by the Squad admission. Existing direct families remain tracked in the machine-readable benchmark-family map.\n\nThe observation layer now contains four non-canonical direct observations (Nool, The Specification Gap, CodeCRDT and Grit) plus one canonical native descriptive observation for Squad. Squad/MARBLE remains a separate quantitative proxy rather than being relabeled as direct.\n\nA `gap` therefore no longer means the canonical direct layer is empty. It means the reviewed public evidence still lacks a materially matched direct primary comparison across two or more canonical S2 implementations.\n\n### Canonical direct observation: Squad operational shared-state coordination\n\nPinned canonical ref: `{REF}`. Public first-party repository history plus the March 17, 2026 operational case study record real concurrent shared-state interference and the native `merge=union` / per-agent inbox / Scribe consolidation paths that preserve and reconcile team state before later project operation. This is descriptive direct evidence; it supplies no matched numeric cross-harness effect estimate.\n'''
s = s[:start] + replacement + s[end:]
README.write_text(s, encoding="utf-8")

print(f"applied Squad S2 evidence: families={family_count}, observations={len(obs)}, canonical={len(canonical_obs)}")
