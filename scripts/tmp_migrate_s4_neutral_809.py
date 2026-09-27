#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S4 = EXP / "s4-system-benchmarks"
REG = EXP / "system-observations"
BENCH = S4 / "benchmark_observations.json"
CANON = S4 / "canonical_observations.json"
VALIDATOR = S4 / "validate.py"
TEST = ROOT / "tests" / "test_s4_neutral_registry_migration_809.py"

benchmark_old = json.loads(BENCH.read_text(encoding="utf-8"))
canonical_old = json.loads(CANON.read_text(encoding="utf-8"))
assert len(benchmark_old) == 4
assert len(canonical_old) == 2
assert len({r["observation_id"] for r in benchmark_old + canonical_old}) == 6

BENCH_DERIVED = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "vsm_interpretation",
}
CANON_DERIVED = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_assessment_ref",
    "canonical_system_eligible",
    "ordinary_s4_boundary",
    "comparison_scope_note",
    "vsm_interpretation",
}
TOP_LEVEL = {
    "evidence_source_class",
    "system_compatibility",
    "primary_sources",
    "canonical_review_revision",
}

COMPOSED_META = {
    "a-evolve-harness-evolution-protocol-2026": (
        "a-evolve-composed.json",
        "A-Evolve benchmark-defined evolving system",
        "A-Evolve harness-evolution protocol",
        "first-party-reported",
    ),
    "skillevolbench-frozen-deployment-protocol-2026": (
        "skillevolbench.json",
        "SkillEvolBench benchmark organization",
        "SkillEvolBench frozen-deployment protocol",
        "first-party-reported",
    ),
    "evoharnessbench-self-evolving-adaptation-v2": (
        "evoharnessbench.json",
        "EvoHarnessBench self-evolving benchmark organization",
        "EvoHarnessBench self-evolving adaptation protocol",
        "first-party-reported",
    ),
    "evo-bench-heldout-harness-evolution-2026": (
        "evo-bench.json",
        "Evo-Bench benchmark organization",
        "Evo-Bench held-out harness-evolution study",
        "external-reproduced",
    ),
}

refs: dict[str, str] = {}

# Four benchmark-defined/composed S4 systems become neutral raw records.
for old in benchmark_old:
    oid = old["observation_id"]
    filename, system_name, benchmark_label, default_source = COMPOSED_META[oid]
    raw_obs = {
        k: v
        for k, v in old.items()
        if k not in BENCH_DERIVED and k not in TOP_LEVEL and k != "raw_observation_ref"
    }
    raw_obs["observation_id"] = oid
    raw_obs["kind"] = "persistent-adaptation-study"
    raw_obs["benchmark"] = benchmark_label

    source_class = old.get("evidence_source_class", default_source)
    record = {
        "schema_version": 1,
        "recorded_at": "2026-09-27",
        "evidence_source_class": source_class,
        "system_name": system_name,
        "canonical_harness_id": None,
        "published_implementation": {
            "system_compatibility": old["system_compatibility"],
            "historical_relation": "Benchmark-defined S4 evidence migrated from the function-specific direct-observation registry. The neutral record preserves public protocol/result provenance without assigning canonical harness ownership.",
        },
        "primary_sources": old["primary_sources"],
        "observations": [raw_obs],
    }
    if old.get("reviewed_revision"):
        record["published_implementation"]["source_revision"] = old["reviewed_revision"]
    elif old.get("protocol_version"):
        record["published_implementation"]["protocol_version"] = old["protocol_version"]
        if old.get("code_revision_status"):
            record["published_implementation"]["code_revision_status"] = old["code_revision_status"]
    (REG / filename).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    refs[oid] = filename

# Reuse the two existing canonical neutral records, enriching only neutral public-evidence payload.
for old in canonical_old:
    oid = old["observation_id"]
    if oid == "a-evolve-harness-updating-2026":
        filename = "a-evolve.json"
    elif oid == "kadath-ten-epoch-native-evolution-2026":
        filename = "kadath.json"
    else:
        raise AssertionError(oid)
    path = REG / filename
    record = json.loads(path.read_text(encoding="utf-8"))
    matches = [row for row in record.get("observations", []) if row.get("observation_id") == oid]
    assert len(matches) == 1
    raw_obs = matches[0]
    for key, value in old.items():
        if key in CANON_DERIVED or key in TOP_LEVEL or key == "raw_observation_ref":
            continue
        raw_obs[key] = value
    record["evidence_source_class"] = old["evidence_source_class"]
    record["published_implementation"]["system_compatibility"] = old["system_compatibility"]
    record["primary_sources"] = old["primary_sources"]
    record["canonical_review_ref"] = old["canonical_review_revision"]
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    refs[oid] = filename

# Function-specific files now retain only classification/linkage/interpretation.
def bench_projection(old: dict) -> dict:
    out = {k: old[k] for k in BENCH_DERIVED if k in old}
    oid = old["observation_id"]
    out["raw_observation_ref"] = f"../system-observations/{refs[oid]}#{oid}"
    return out


def canon_projection(old: dict) -> dict:
    out = {k: old[k] for k in CANON_DERIVED if k in old}
    oid = old["observation_id"]
    out["raw_observation_ref"] = f"../system-observations/{refs[oid]}#{oid}"
    return out


BENCH.write_text(json.dumps([bench_projection(x) for x in benchmark_old], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
CANON.write_text(json.dumps([canon_projection(x) for x in canonical_old], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# S4 validator hydrates neutral raw evidence, then applies the existing semantic checks.
text = VALIDATOR.read_text(encoding="utf-8")
insert_at = text.index("\ndef main() -> None:")
helper = r'''

def hydrate_s4_projection(link: dict) -> dict:
    oid = link.get("observation_id")
    ref = link.get("raw_observation_ref")
    prefix = "../system-observations/"
    if not isinstance(oid, str) or not oid:
        fail("S4 projection requires observation_id")
    if not isinstance(ref, str) or not ref.startswith(prefix) or "#" not in ref:
        fail(f"{oid}: invalid raw_observation_ref")
    rel, ref_oid = ref[len(prefix):].rsplit("#", 1)
    if ref_oid != oid or not rel.endswith(".json") or "/" in rel:
        fail(f"{oid}: raw_observation_ref drift")
    path = RAW_OBSERVATIONS / rel
    if not path.is_file():
        fail(f"{oid}: neutral raw record missing: {rel}")
    record = json.loads(path.read_text(encoding="utf-8"))
    matches = [row for row in record.get("observations", []) if row.get("observation_id") == oid]
    if len(matches) != 1:
        fail(f"{oid}: expected exactly one neutral raw observation in {rel}")
    effective = dict(link)
    for key, value in matches[0].items():
        if key in {"observation_id", "kind", "benchmark", "evidence_surface", "non_claim"}:
            continue
        if key in effective and effective[key] != value:
            fail(f"{oid}: derived/raw field conflict: {key}")
        effective[key] = value
    effective["evidence_source_class"] = record.get("evidence_source_class")
    effective["system_compatibility"] = (record.get("published_implementation") or {}).get("system_compatibility")
    effective["primary_sources"] = record.get("primary_sources")
    raw_harness = record.get("canonical_harness_id")
    if effective.get("canonical_harness_id") != raw_harness:
        fail(f"{oid}: canonical_harness_id raw/derived drift")
    if raw_harness:
        effective["canonical_review_revision"] = record.get("canonical_review_ref")
        if "canonical_assessment_ref" not in effective:
            effective["canonical_assessment_ref"] = record.get("canonical_assessment_ref")
    return effective
'''
assert "def hydrate_s4_projection(" not in text
text = text[:insert_at] + helper + text[insert_at:]
old_load = '''    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))\n    canonical_observations = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))\n    proxy_observations = json.loads(PROXY_OBSERVATIONS.read_text(encoding="utf-8"))\n'''
new_load = '''    benchmark_links = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))\n    canonical_links = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))\n    benchmark_observations = [hydrate_s4_projection(row) for row in benchmark_links]\n    canonical_observations = [hydrate_s4_projection(row) for row in canonical_links]\n    proxy_observations = json.loads(PROXY_OBSERVATIONS.read_text(encoding="utf-8"))\n'''
assert old_load in text
text = text.replace(old_load, new_load)
text = text.replace('if "reported_harness_updating_metrics" in canonical_obs:\n', 'if "reported_harness_updating_metrics" in canonical_links[0]:\n')
text = text.replace('if "reported_population_metrics" in kadath_obs:\n', 'if "reported_population_metrics" in canonical_links[1]:\n')
VALIDATOR.write_text(text, encoding="utf-8")

TEST.write_text(r'''from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"; S4=EXP/"s4-system-benchmarks"
SOURCE_REF="d0753a1375548d1db09cfbcae047f119d0cbba03"
FILES=("benchmark_observations.json","canonical_observations.json")
BENCH_DERIVED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}
CANON_DERIVED=BENCH_DERIVED|{"canonical_assessment_ref","ordinary_s4_boundary","comparison_scope_note"}


def old_rows():
    out=[]
    for name in FILES:
        txt=subprocess.check_output(["git","show",f"{SOURCE_REF}:experiments/functional-capability-depth/s4-system-benchmarks/{name}"],cwd=ROOT,text=True)
        out.extend(json.loads(txt))
    return {row["observation_id"]:row for row in out}


def hydrate(link):
    ref=link["raw_observation_ref"]
    rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    record=json.loads((REG/rel).read_text(encoding="utf-8"))
    matches=[o for o in record["observations"] if o.get("observation_id")==oid]
    assert len(matches)==1
    effective=dict(link)
    for k,v in matches[0].items():
        if k in {"observation_id","kind","benchmark","evidence_surface","non_claim"}: continue
        effective[k]=v
    effective["evidence_source_class"]=record["evidence_source_class"]
    effective["system_compatibility"]=record["published_implementation"]["system_compatibility"]
    effective["primary_sources"]=record["primary_sources"]
    if record.get("canonical_harness_id"):
        effective["canonical_review_revision"]=record["canonical_review_ref"]
    return effective


class S4NeutralRegistryMigration809Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows(); cls.links={}
        for name in FILES:
            for row in json.loads((S4/name).read_text(encoding="utf-8")):
                cls.links[row["observation_id"]]=row
        cls.effective={oid:hydrate(link) for oid,link in cls.links.items()}
    def test_six_direct_rows_resolve_once(self):
        self.assertEqual(len(self.old),6); self.assertEqual(set(self.old),set(self.links))
        counts={oid:0 for oid in self.old}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            for obs in rec.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertEqual(counts,{oid:1 for oid in self.old})
    def test_moved_fields_are_lossless(self):
        for oid,old in self.old.items():
            effective=self.effective[oid]
            for key,value in old.items():
                if key=="raw_observation_ref": continue
                self.assertEqual(effective.get(key),value,f"{oid}:{key}")
    def test_function_files_are_derived_only(self):
        for oid,link in self.links.items():
            allowed=CANON_DERIVED if oid in {"a-evolve-harness-updating-2026","kadath-ten-epoch-native-evolution-2026"} else BENCH_DERIVED
            self.assertLessEqual(set(link),allowed,oid)
            self.assertIn("raw_observation_ref",link)
            for raw_key in ("primary_sources","system_compatibility","evidence_source_class","adaptation_loop","published_results","epochs","source_artifact_revision"):
                self.assertNotIn(raw_key,link,oid)
    def test_raw_records_are_vsm_free(self):
        for oid,link in self.links.items():
            rel=link["raw_observation_ref"][len("../system-observations/"):].split("#",1)[0]
            rec=json.loads((REG/rel).read_text(encoding="utf-8"))
            obs=next(o for o in rec["observations"] if o["observation_id"]==oid)
            for container in (rec,obs):
                for forbidden in ("function","benchmark_fit","vsm_interpretation","ordinary_s4_boundary","comparison_scope_note"):
                    self.assertNotIn(forbidden,container)
    def test_composed_and_canonical_boundaries_stay_separate(self):
        a_comp=json.loads((REG/"a-evolve-composed.json").read_text(encoding="utf-8"))
        self.assertIsNone(a_comp["canonical_harness_id"])
        a_native=json.loads((REG/"a-evolve.json").read_text(encoding="utf-8"))
        self.assertEqual(a_native["canonical_harness_id"],"a-evolve")
        k=json.loads((REG/"kadath.json").read_text(encoding="utf-8"))
        self.assertEqual(k["canonical_harness_id"],"kadath")
        evo=json.loads((REG/"evoharnessbench.json").read_text(encoding="utf-8"))
        self.assertIsNone(evo["canonical_harness_id"])
        self.assertEqual(evo["published_implementation"].get("code_revision_status"),"unresolved-official-github-repository")
if __name__=="__main__": unittest.main()
''',encoding="utf-8")

print("migrated 6 direct S4 observations to neutral raw ownership")
