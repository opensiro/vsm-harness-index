#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

obs_p = BASE / "observations.json"
obs = load(obs_p)
if not any(x.get("observation_id") == "squad-shared-state-conflict-attenuation-2026-03" for x in obs):
    obs.append({
        "observation_id": "squad-shared-state-conflict-attenuation-2026-03",
        "function": "S2", "benchmark_id": None, "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "canonical-squad-project-team",
        "canonical_harness_id": "squad", "canonical_system_eligible": True,
        "canonical_assessment_ref": "2099faf51c08a912c359209447011b06decf0565",
        "canonical_state_at_review": "A", "system_compatibility": "native-system",
        "comparison_class": "descriptive-only",
        "evidence_surface": "immutable first-party repository history plus first-party public operational case study",
        "operational_commits": [
            "34925f2f5bec49742216ab9dd93c756fbe1aa8c9",
            "e7e6255aa84e04993d568a10331bf9da6661b478",
            "6e304ec6d2f1d385226fba074a1192a3eab7b5cb"
        ],
        "case_study_date": "2026-03-17",
        "disturbance": "Parallel Squad S1 agents append to shared team-state and decision surfaces; simultaneous completion can create merge interference on canonical shared state.",
        "coordination_relation": "Squad's first-party merge=union rules preserve concurrent append-only team-state contributions, while per-agent decision inbox files and Scribe consolidation separate structured concurrent writes before returning them to canonical decisions.md.",
        "subsequent_operation": "First-party operational history records decision-inbox consolidation followed by later multi-PR release work with team state preserved via merge=union.",
        "comparison_limitation": "This is descriptive canonical direct evidence from operational history, not a matched benchmark comparison or a causal numeric uplift estimate.",
        "vsm_interpretation": "This is direct descriptive S2 capability evidence at the canonical Squad project-team boundary. Distinct parallel S1 agents generate interaction-specific shared-state interference; native merge=union and Scribe/inbox coordination attenuate that interference and preserve/consolidate state for subsequent operation. It does not create a benchmark family or a matched cross-harness primary cell.",
        "primary_sources": [
            "https://github.com/bradygaster/squad/tree/2099faf51c08a912c359209447011b06decf0565",
            "https://github.com/bradygaster/squad/commit/34925f2f5bec49742216ab9dd93c756fbe1aa8c9",
            "https://github.com/bradygaster/squad/commit/e7e6255aa84e04993d568a10331bf9da6661b478",
            "https://github.com/bradygaster/squad/commit/6e304ec6d2f1d385226fba074a1192a3eab7b5cb",
            "https://www.tamirdresher.com/blog/2026/03/17/scaling-ai-part4-distributed"
        ]
    })
dump(obs_p, obs)

cov_p = BASE / "coverage.json"
cov = load(cov_p)
cov["direct_observation_count"] = 4
cov["canonical_direct_observation_count"] = 1
if "direct-native-canonical" not in cov["coverage_classes"]:
    cov["coverage_classes"].insert(2, "direct-native-canonical")
case_id = "squad-shared-state-conflict-direct-native-canonical"
if not any(x.get("case_id") == case_id for x in cov["cases"]):
    case = {
        "case_id": case_id,
        "benchmark": "Squad shared-state conflict attenuation operational evidence",
        "benchmark_fit": "direct", "coverage_class": "direct-native-canonical",
        "system_compatibility": "native-system", "canonical_harness_id": "squad",
        "canonical_state_at_review": "A",
        "canonical_review_ref": "2099faf51c08a912c359209447011b06decf0565",
        "observation_ref": "observations.json#squad-shared-state-conflict-attenuation-2026-03",
        "primary_sources": [
            "https://github.com/bradygaster/squad/tree/2099faf51c08a912c359209447011b06decf0565",
            "https://github.com/bradygaster/squad/commit/34925f2f5bec49742216ab9dd93c756fbe1aa8c9",
            "https://github.com/bradygaster/squad/commit/e7e6255aa84e04993d568a10331bf9da6661b478",
            "https://github.com/bradygaster/squad/commit/6e304ec6d2f1d385226fba074a1192a3eab7b5cb",
            "https://www.tamirdresher.com/blog/2026/03/17/scaling-ai-part4-distributed"
        ],
        "finding": "Canonical Squad S2=A is independently established by the assessment. First-party operational history and a public case study record real concurrent shared-state merge interference, native merge=union preservation, per-agent decision inboxes and Scribe consolidation, followed by subsequent project/release operation with team state preserved. This is direct descriptive native S2 evidence, not a new benchmark family or matched causal comparison.",
        "admitted": False
    }
    i = next(i for i, x in enumerate(cov["cases"]) if x["case_id"] == "squad-marble-native-proxy")
    cov["cases"].insert(i + 1, case)
dump(cov_p, cov)

cl_p = BASE / "matched-cell/s2-primary-search-closure.json"
cl = load(cl_p)
cl["squad_canonical_direct_issue"] = 644
cl["evidence_depth"]["direct_observations"] = 4
cl["evidence_depth"]["canonical_direct_observations"] = 1
cl["closure_claim"] = "Current public evidence contains seven direct S2 disturbance/attenuation families, four direct observations, one canonical native descriptive direct observation (Squad), and two native quantitative S2 proxy projections. The canonical layer is therefore no longer empty, but public evidence still lacks a materially matched direct comparison across two or more canonical S2 systems, so no primary baseline is selected."
cl["reopen_when"] = [
    "a second canonical S2 harness publishes a direct native or adapter-preserved inter-S1 disturbance-to-attenuation result that can form a materially comparable cell with existing canonical evidence",
    "a materially matched benchmark evaluates two or more canonical systems exercising their own native or adapter-preserved S2 paths under one disturbance definition",
    "MAO-Bench or a comparable benchmark publishes recoverable multi-orchestrator results with immutable system/model/configuration provenance and direct S2 semantics"
]
cl["non_claim"] = "This closure is not a zero S2 capability score and does not downgrade canonical S2 ownership. Squad now supplies one canonical native descriptive direct observation, while Nool, The Specification Gap and CodeCRDT remain direct non-canonical observations at their reviewed boundaries. One descriptive canonical row is not a matched cross-harness primary; S2 primary remains a gap until materially matched canonical evidence appears."
dump(cl_p, cl)

pb_p = ROOT / "experiments/functional-capability-depth/primary-baselines.json"
pb = load(pb_p)
pb["functions"]["S2"]["blocking_reason"] = "Reviewed direct S2 evidence includes seven disturbance/attenuation families. Nool and The Specification Gap provide benchmark-scaffolded direct non-canonical observations, CodeCRDT provides one descriptive direct observation at its own external native product boundary, and Squad now provides one canonical native descriptive direct observation from first-party operational history. Twining lacks recoverable exact treatment revision and CooperBench lacks pinned flash-run logs for observation admission. One canonical descriptive row is not a materially matched cross-harness comparison, so public evidence still provides no matched primary cell across multiple canonical native S2 implementations."
dump(pb_p, pb)

v_p = BASE / "validate.py"
s = v_p.read_text()
s = s.replace('    "direct-native-noncanonical",\n', '    "direct-native-noncanonical",\n    "direct-native-canonical",\n')
s = s.replace('    if len(observations) != 3:\n        fail("S2 observations.json must contain exactly three direct non-canonical observations")', '    if len(observations) != 4:\n        fail("S2 observations.json must contain exactly four direct observations")')
s = s.replace('    if coverage.get("canonical_direct_observation_count") != 0:\n        fail("S2 canonical_direct_observation_count must remain 0")', '    canonical_observations = [row for row in observations if row.get("canonical_system_eligible") is True]\n    if coverage.get("canonical_direct_observation_count") != len(canonical_observations):\n        fail("canonical_direct_observation_count does not match canonical direct observations")\n    if len(canonical_observations) != 1:\n        fail("S2 must retain exactly one canonical direct observation in this snapshot")')
fn = '''\n\ndef validate_squad_canonical_observation(observations: list[dict]) -> None:\n    observation = observation_by_id(observations, "squad-shared-state-conflict-attenuation-2026-03")\n    expected = {"function":"S2","benchmark_id":None,"benchmark_fit":"direct","evidence_source_class":"first-party-reported","boundary_class":"canonical-squad-project-team","canonical_harness_id":"squad","canonical_system_eligible":True,"canonical_assessment_ref":"2099faf51c08a912c359209447011b06decf0565","canonical_state_at_review":"A","system_compatibility":"native-system","comparison_class":"descriptive-only"}\n    for field, value in expected.items():\n        if observation.get(field) != value:\n            fail(f"Squad canonical direct S2 observation {field} drift: {observation.get(field)!r}")\n    fields = assessment_fields("squad")\n    if fields.get("status") != "included" or fields.get("review_ref") != expected["canonical_assessment_ref"] or fields.get("autonomy_s2") != "A":\n        fail("Squad canonical assessment/ref/S2 state drift")\n    if observation.get("operational_commits") != ["34925f2f5bec49742216ab9dd93c756fbe1aa8c9","e7e6255aa84e04993d568a10331bf9da6661b478","6e304ec6d2f1d385226fba074a1192a3eab7b5cb"]:\n        fail("Squad operational evidence lineage drift")\n    sources = observation.get("primary_sources")\n    if not isinstance(sources, list) or len(sources) < 5 or any(not valid_https(source) for source in sources):\n        fail("Squad canonical direct observation must retain public HTTPS provenance")\n'''
if "def validate_squad_canonical_observation" not in s:
    s = s.replace('\ndef main() -> None:\n', fn + '\n\ndef main() -> None:\n')
block = '''    squad_direct = by_id.get("squad-shared-state-conflict-direct-native-canonical")\n    if squad_direct is None:\n        fail("missing Squad canonical direct-S2 coverage case")\n    if squad_direct.get("benchmark_fit") != "direct" or squad_direct.get("coverage_class") != "direct-native-canonical":\n        fail("Squad operational evidence must remain direct-native-canonical S2")\n    if squad_direct.get("system_compatibility") != "native-system" or squad_direct.get("canonical_harness_id") != "squad":\n        fail("Squad canonical direct S2 linkage drift")\n    if squad_direct.get("canonical_state_at_review") != "A" or squad_direct.get("canonical_review_ref") != "2099faf51c08a912c359209447011b06decf0565":\n        fail("Squad canonical direct S2 assessment anchor drift")\n    if squad_direct.get("observation_ref") != "observations.json#squad-shared-state-conflict-attenuation-2026-03":\n        fail("Squad canonical direct coverage/observation linkage drift")\n\n'''
if "squad_direct = by_id.get" not in s:
    s = s.replace('    codecrdt = by_id.get("codecrdt-observation-driven-direct-native-noncanonical")', block + '    codecrdt = by_id.get("codecrdt-observation-driven-direct-native-noncanonical")')
s = s.replace('    validate_codecrdt_observation(observations)\n', '    validate_codecrdt_observation(observations)\n    validate_squad_canonical_observation(observations)\n')
v_p.write_text(s)

cv_p = BASE / "matched-cell/validate_s2_primary_search_closure.py"
s = cv_p.read_text()
s = s.replace('require(closure["codecrdt_public_evidence_issue"] == 640, "S2 CodeCRDT public-evidence issue drift")', 'require(closure["codecrdt_public_evidence_issue"] == 640, "S2 CodeCRDT public-evidence issue drift")\nrequire(closure["squad_canonical_direct_issue"] == 644, "S2 Squad canonical-direct issue drift")')
s = s.replace('    "squad-marble-native-proxy",\n', '    "squad-marble-native-proxy",\n    "squad-shared-state-conflict-direct-native-canonical",\n')
s = s.replace('require(len(observations) == 3, "S2 closure expects three direct non-canonical observations")', 'require(len(observations) == 4, "S2 closure expects four direct observations")')
s = s.replace('        "codecrdt-parallel-convergence-2025-10",\n', '        "codecrdt-parallel-convergence-2025-10",\n        "squad-shared-state-conflict-attenuation-2026-03",\n')
s = s.replace('    "codecrdt-parallel-convergence-2025-10": ("codecrdt-observation-coordination", "native-system"),\n', '    "codecrdt-parallel-convergence-2025-10": ("codecrdt-observation-coordination", "native-system"),\n    "squad-shared-state-conflict-attenuation-2026-03": (None, "native-system"),\n')
old = '''    observation = observation_rows[observation_id]\n    require(observation["benchmark_id"] == benchmark_id, f"{observation_id}: benchmark drift")\n    require(observation["canonical_harness_id"] is None, f"{observation_id}: must remain non-canonical")\n    require(observation["canonical_system_eligible"] is False, f"{observation_id}: must remain non-canonical")\n    require(observation["system_compatibility"] == compatibility, f"{observation_id}: system compatibility drift")'''
new = '''    observation = observation_rows[observation_id]\n    require(observation["benchmark_id"] == benchmark_id, f"{observation_id}: benchmark drift")\n    require(observation["system_compatibility"] == compatibility, f"{observation_id}: system compatibility drift")\n    if observation_id == "squad-shared-state-conflict-attenuation-2026-03":\n        require(observation["canonical_harness_id"] == "squad", "Squad canonical observation identity drift")\n        require(observation["canonical_system_eligible"] is True, "Squad canonical observation eligibility drift")\n        require(observation.get("canonical_assessment_ref") == "2099faf51c08a912c359209447011b06decf0565", "Squad canonical observation ref drift")\n        require(observation.get("canonical_state_at_review") == "A", "Squad canonical observation S2 state drift")\n    else:\n        require(observation["canonical_harness_id"] is None, f"{observation_id}: must remain non-canonical")\n        require(observation["canonical_system_eligible"] is False, f"{observation_id}: must remain non-canonical")'''
s = s.replace(old, new)
s = s.replace('''require(\n    observation_rows["codecrdt-parallel-convergence-2025-10"].get("comparison_class") == "descriptive-only",\n    "CodeCRDT direct observation must remain descriptive-only",\n)''','''require(\n    observation_rows["codecrdt-parallel-convergence-2025-10"].get("comparison_class") == "descriptive-only",\n    "CodeCRDT direct observation must remain descriptive-only",\n)\nrequire(\n    observation_rows["squad-shared-state-conflict-attenuation-2026-03"].get("comparison_class") == "descriptive-only",\n    "Squad canonical direct observation must remain descriptive-only",\n)''')
cv_p.write_text(s)

r_p = BASE / "README.md"
s = r_p.read_text()
s = s.replace('direct S2 benchmark families reviewed:          6', 'direct S2 benchmark families reviewed:          7').replace('direct S2 observations:                         2', 'direct S2 observations:                         4').replace('canonical native direct-S2 observations:        0', 'canonical native direct-S2 observations:        1')
s = s.replace('The two admitted direct observations are Nool Track D and The Specification Gap recovery experiment. Both are direct at benchmark-defined organization boundaries and neither is a canonical native observation.', 'Four direct observations are admitted: Nool Track D, The Specification Gap, CodeCRDT, and a descriptive canonical Squad operational observation. The first three remain non-canonical; Squad is the first canonical native direct S2 row.')
if '- `CodeCRDT observation-driven coordination evaluation`.' not in s:
    s = s.replace('- `CooperBench team-harness coordination ablation`.\n', '- `CooperBench team-harness coordination ablation`;\n- `CodeCRDT observation-driven coordination evaluation`.\n')
section = '''## Canonical direct descriptive observation: Squad shared-state conflict attenuation\n\nCanonical Squad independently establishes `S2=A` at `2099faf51c08a912c359209447011b06decf0565`. First-party repository history records native `merge=union` rules for append-only team state, Scribe consolidation of per-agent decision inboxes, and later release work with team state preserved. A first-party public operational case study separately describes simultaneous agent writes creating a real `.squad/decisions.md` merge conflict, then native `merge=union` preservation and inbox/Scribe consolidation.\n\nThis is admitted as `direct-native-canonical`, `descriptive-only`. It creates no benchmark family and no causal numeric uplift. The separate Squad/MARBLE quantitative surface remains a `native-proxy` because it scores broad collaboration outcomes rather than an explicit S2 disturbance.\n\n'''
if section not in s:
    s = s.replace('## Native proxy: Squad / MARBLE\n', section + '## Native proxy: Squad / MARBLE\n')
s = s.replace('`observations.json` — admitted direct S2 observations; currently two non-canonical rows (Nool Track D and The Specification Gap);', '`observations.json` — admitted direct S2 observations; currently three non-canonical rows plus one canonical descriptive Squad row;')
r_p.write_text(s)

t_p = ROOT / "tests/test_s2_post_closure_shep_axocoatl.py"
s = t_p.read_text().replace('        self.assertEqual(coverage["canonical_direct_observation_count"], 0)\n', '        canonical = [row for row in observations if row.get("canonical_system_eligible") is True]\n        self.assertEqual(coverage["canonical_direct_observation_count"], len(canonical))\n')
t_p.write_text(s)
