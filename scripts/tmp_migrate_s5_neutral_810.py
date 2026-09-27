#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S5 = EXP / "s5-system-benchmarks"
REG = EXP / "system-observations"
BENCH = S5 / "benchmark_observations.json"
CANON = S5 / "canonical_observations.json"
VALIDATOR = S5 / "validate.py"
PRIMARY = S5 / "matched-cell" / "validate_s5_primary_search_closure.py"
SECOND = S5 / "matched-cell" / "validate_second_canonical_search.py"
TEST = ROOT / "tests" / "test_s5_neutral_registry_migration_810.py"

bench_old = json.loads(BENCH.read_text(encoding="utf-8"))
canon_old = json.loads(CANON.read_text(encoding="utf-8"))
assert len(bench_old) == 1 and len(canon_old) == 1
GOV = "govsim-selfgovern-membership-authority-2026-09"
OURO = "ouroboros-parent-governed-cyber-pro-policy-enactment-2026-09"
assert bench_old[0]["observation_id"] == GOV
assert canon_old[0]["observation_id"] == OURO

GOV_DERIVED = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "s5_boundary",
    "result_scope_note",
    "vsm_interpretation",
}
OURO_DERIVED = {
    "observation_id",
    "function",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "canonical_s5_state",
    "ownership_mode_observed",
    "comparison_class",
    "vsm_interpretation",
    "non_claim",
}
TOP_RAW = {
    "evidence_source_class",
    "system_compatibility",
    "primary_sources",
    "canonical_review_revision",
}

# GovSim-SelfGovern: composed benchmark society, no canonical harness identity and no invented code revision.
gov = bench_old[0]
gov_obs = {k: v for k, v in gov.items() if k not in GOV_DERIVED and k not in TOP_RAW}
gov_obs["observation_id"] = GOV
gov_obs["kind"] = "membership-authority-study"
gov_record = {
    "schema_version": 1,
    "recorded_at": "2026-09-27",
    "evidence_source_class": gov["evidence_source_class"],
    "system_name": "GovSim-SelfGovern benchmark society",
    "canonical_harness_id": None,
    "published_implementation": {
        "system_compatibility": gov["system_compatibility"],
        "code_revision_status": gov["code_revision_status"],
        "paper_version": gov["paper_version"],
        "historical_relation": "Publication-defined benchmark society. No authoritative public code repository/revision is asserted; no unrelated GovSim repository is attached by name similarity.",
    },
    "primary_sources": gov["primary_sources"],
    "observations": [gov_obs],
}
(REG / "govsim-selfgovern.json").write_text(json.dumps(gov_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Ouroboros: canonical native descriptive repository-history witness for the already-established parent-governed S5 path.
our = canon_old[0]
our_obs = {k: v for k, v in our.items() if k not in OURO_DERIVED and k not in TOP_RAW}
our_obs["observation_id"] = OURO
our_obs["kind"] = "repository-history-policy-enactment-witness"
our_record = {
    "schema_version": 1,
    "recorded_at": "2026-09-27",
    "evidence_source_class": our["evidence_source_class"],
    "system_name": "Ouroboros",
    "canonical_harness_id": "ouroboros",
    "canonical_assessment_ref": "assessments/ouroboros.md",
    "canonical_review_ref": our["canonical_review_revision"],
    "canonical_repository": "https://github.com/razzant/ouroboros",
    "published_implementation": {
        "system_compatibility": our["system_compatibility"],
        "historical_relation": "First-party repository-history witness whose enactment merge is an ancestor of the canonical review revision. It is descriptive evidence, not an independently reproduced numeric benchmark run.",
    },
    "primary_sources": our["primary_sources"],
    "observations": [our_obs],
}
(REG / "ouroboros-policy-enactment.json").write_text(json.dumps(our_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Function-specific projections retain only S5 interpretation/linkage and explicit claim boundaries.
def project(row: dict, allowed: set[str], raw_file: str) -> dict:
    out = {k: row[k] for k in allowed if k in row}
    oid = row["observation_id"]
    out["raw_observation_ref"] = f"../system-observations/{raw_file}#{oid}"
    return out

BENCH.write_text(json.dumps([project(gov, GOV_DERIVED, "govsim-selfgovern.json")], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
CANON.write_text(json.dumps([project(our, OURO_DERIVED, "ouroboros-policy-enactment.json")], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

HYDRATE = r'''

def hydrate_s5_projection(link: dict) -> dict:
    oid = link.get("observation_id")
    ref = link.get("raw_observation_ref")
    prefix = "../system-observations/"
    if not isinstance(oid, str) or not oid:
        fail("S5 projection requires observation_id")
    if not isinstance(ref, str) or not ref.startswith(prefix) or "#" not in ref:
        fail(f"{oid}: invalid raw_observation_ref")
    rel, ref_oid = ref[len(prefix):].rsplit("#", 1)
    if ref_oid != oid or not rel.endswith(".json") or "/" in rel:
        fail(f"{oid}: raw_observation_ref drift")
    raw_path = HERE.parent / "system-observations" / rel
    if not raw_path.is_file():
        fail(f"{oid}: neutral raw record missing: {rel}")
    record = json.loads(raw_path.read_text(encoding="utf-8"))
    matches = [row for row in record.get("observations", []) if row.get("observation_id") == oid]
    if len(matches) != 1:
        fail(f"{oid}: expected exactly one neutral raw observation in {rel}")
    effective = dict(link)
    for key, value in matches[0].items():
        if key in {"observation_id", "kind", "evidence_surface"}:
            continue
        if key in effective and effective[key] != value:
            fail(f"{oid}: derived/raw field conflict: {key}")
        effective[key] = value
    effective["evidence_source_class"] = record.get("evidence_source_class")
    effective["system_compatibility"] = (record.get("published_implementation") or {}).get("system_compatibility")
    effective["primary_sources"] = record.get("primary_sources")
    if (record.get("published_implementation") or {}).get("code_revision_status") is not None:
        effective["code_revision_status"] = record["published_implementation"]["code_revision_status"]
    if (record.get("published_implementation") or {}).get("paper_version") is not None:
        effective["paper_version"] = record["published_implementation"]["paper_version"]
    raw_harness = record.get("canonical_harness_id")
    if effective.get("canonical_harness_id") != raw_harness:
        fail(f"{oid}: canonical_harness_id raw/derived drift")
    if raw_harness:
        effective["canonical_review_revision"] = record.get("canonical_review_ref")
    return effective
'''

# Main validator: hydrate both effective observations before existing checks.
text = VALIDATOR.read_text(encoding="utf-8")
insert = text.index("\ndef main() -> None:")
assert "def hydrate_s5_projection(" not in text
text = text[:insert] + HYDRATE + text[insert:]
old = '''    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS_PATH.read_text(encoding="utf-8"))\n    canonical_observations = json.loads(CANONICAL_OBSERVATIONS_PATH.read_text(encoding="utf-8"))\n'''
new = '''    benchmark_links = json.loads(BENCHMARK_OBSERVATIONS_PATH.read_text(encoding="utf-8"))\n    canonical_links = json.loads(CANONICAL_OBSERVATIONS_PATH.read_text(encoding="utf-8"))\n    benchmark_observations = [hydrate_s5_projection(row) for row in benchmark_links]\n    canonical_observations = [hydrate_s5_projection(row) for row in canonical_links]\n'''
assert old in text
VALIDATOR.write_text(text.replace(old, new), encoding="utf-8")

# Closure consumers need the same effective canonical row rather than restoring factual payload to the projection.
CLOSURE_HYDRATE = r'''

def hydrate_canonical_projection(link: dict) -> dict:
    oid = link.get("observation_id")
    ref = link.get("raw_observation_ref")
    prefix = "../system-observations/"
    require(isinstance(oid, str) and oid, "S5 canonical projection requires observation_id")
    require(isinstance(ref, str) and ref.startswith(prefix) and "#" in ref, f"{oid}: invalid raw_observation_ref")
    rel, ref_oid = ref[len(prefix):].rsplit("#", 1)
    require(ref_oid == oid and rel.endswith(".json") and "/" not in rel, f"{oid}: raw_observation_ref drift")
    raw_path = EXPERIMENT / "system-observations" / rel
    require(raw_path.is_file(), f"{oid}: neutral raw record missing: {rel}")
    record = load(raw_path)
    matches = [row for row in record.get("observations", []) if row.get("observation_id") == oid]
    require(len(matches) == 1, f"{oid}: expected exactly one neutral raw observation in {rel}")
    effective = dict(link)
    for key, value in matches[0].items():
        if key in {"observation_id", "kind", "evidence_surface"}:
            continue
        require(key not in effective or effective[key] == value, f"{oid}: derived/raw field conflict: {key}")
        effective[key] = value
    effective["evidence_source_class"] = record.get("evidence_source_class")
    effective["system_compatibility"] = (record.get("published_implementation") or {}).get("system_compatibility")
    effective["primary_sources"] = record.get("primary_sources")
    effective["canonical_review_revision"] = record.get("canonical_review_ref")
    return effective
'''

text = PRIMARY.read_text(encoding="utf-8")
needle = 'closure = load(HERE / "s5-primary-search-closure.json")\n'
assert needle in text and "def hydrate_canonical_projection(" not in text
text = text.replace(needle, CLOSURE_HYDRATE + "\n" + needle)
old = 'canonical = canonical_observations[0]\n'
assert old in text
text = text.replace(old, 'canonical = hydrate_canonical_projection(canonical_observations[0])\n')
PRIMARY.write_text(text, encoding="utf-8")

text = SECOND.read_text(encoding="utf-8")
needle = 'search = load(SEARCH_PATH)\n'
assert needle in text and "def hydrate_canonical_projection(" not in text
text = text.replace(needle, CLOSURE_HYDRATE + "\n" + needle)
old = 'observation = canonical[0]\n'
assert old in text
text = text.replace(old, 'observation = hydrate_canonical_projection(canonical[0])\n')
SECOND.write_text(text, encoding="utf-8")

TEST.write_text(r'''from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"; S5=EXP/"s5-system-benchmarks"
SOURCE_REF="faf351e02ae48d205bcd1d1a9b46d221e52bad84"
FILES=("benchmark_observations.json","canonical_observations.json")
GOV="govsim-selfgovern-membership-authority-2026-09"
OURO="ouroboros-parent-governed-cyber-pro-policy-enactment-2026-09"
GOV_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","s5_boundary","result_scope_note","vsm_interpretation","raw_observation_ref"}
OURO_ALLOWED={"observation_id","function","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","canonical_s5_state","ownership_mode_observed","comparison_class","vsm_interpretation","non_claim","raw_observation_ref"}

def old_rows():
    out=[]
    for name in FILES:
        txt=subprocess.check_output(["git","show",f"{SOURCE_REF}:experiments/functional-capability-depth/s5-system-benchmarks/{name}"],cwd=ROOT,text=True)
        out.extend(json.loads(txt))
    return {row["observation_id"]:row for row in out}

def hydrate(link):
    ref=link["raw_observation_ref"]; rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    rec=json.loads((REG/rel).read_text(encoding="utf-8")); matches=[o for o in rec["observations"] if o["observation_id"]==oid]
    assert len(matches)==1
    eff=dict(link)
    for k,v in matches[0].items():
        if k in {"observation_id","kind","evidence_surface"}: continue
        eff[k]=v
    eff["evidence_source_class"]=rec["evidence_source_class"]
    eff["system_compatibility"]=rec["published_implementation"]["system_compatibility"]
    eff["primary_sources"]=rec["primary_sources"]
    if rec["published_implementation"].get("code_revision_status") is not None: eff["code_revision_status"]=rec["published_implementation"]["code_revision_status"]
    if rec["published_implementation"].get("paper_version") is not None: eff["paper_version"]=rec["published_implementation"]["paper_version"]
    if rec.get("canonical_harness_id"): eff["canonical_review_revision"]=rec["canonical_review_ref"]
    return eff

class S5NeutralRegistryMigration810Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows(); cls.links={}
        for name in FILES:
            for row in json.loads((S5/name).read_text(encoding="utf-8")): cls.links[row["observation_id"]]=row
        cls.effective={oid:hydrate(link) for oid,link in cls.links.items()}
    def test_two_direct_observations_resolve_once(self):
        self.assertEqual(set(self.old),{GOV,OURO}); self.assertEqual(set(self.links),{GOV,OURO})
        counts={GOV:0,OURO:0}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            for obs in rec.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertEqual(counts,{GOV:1,OURO:1})
    def test_moved_fields_are_lossless(self):
        for oid,old in self.old.items():
            eff=self.effective[oid]
            for key,value in old.items(): self.assertEqual(eff.get(key),value,f"{oid}:{key}")
    def test_function_files_are_derived_only(self):
        self.assertLessEqual(set(self.links[GOV]),GOV_ALLOWED)
        self.assertLessEqual(set(self.links[OURO]),OURO_ALLOWED)
        for oid in (GOV,OURO):
            self.assertIn("raw_observation_ref",self.links[oid])
            for raw_key in ("primary_sources","evidence_source_class","system_compatibility","authority_path","non_thinking_exile","thinking_exile","policy_change_commit","enactment_pr","lineage","decision_chain","executable_effects"):
                self.assertNotIn(raw_key,self.links[oid],f"{oid}:{raw_key}")
    def test_neutral_records_are_vsm_free(self):
        for oid,link in self.links.items():
            rel=link["raw_observation_ref"][len("../system-observations/"):].split("#",1)[0]
            rec=json.loads((REG/rel).read_text(encoding="utf-8")); obs=next(o for o in rec["observations"] if o["observation_id"]==oid)
            for container in (rec,obs):
                for forbidden in ("function","benchmark_fit","vsm_interpretation","canonical_s5_state","ownership_mode_observed"):
                    self.assertNotIn(forbidden,container)
    def test_boundaries_remain_distinct(self):
        gov=json.loads((REG/"govsim-selfgovern.json").read_text(encoding="utf-8"))
        self.assertIsNone(gov["canonical_harness_id"])
        self.assertEqual(gov["published_implementation"]["system_compatibility"],"benchmark-scaffolded")
        self.assertEqual(gov["published_implementation"]["code_revision_status"],"unresolved-authoritative-public-repository")
        ouro=json.loads((REG/"ouroboros-policy-enactment.json").read_text(encoding="utf-8"))
        self.assertEqual(ouro["canonical_harness_id"],"ouroboros")
        self.assertEqual(ouro["canonical_review_ref"],"86806ee123ce8e26cc063cc1a618f975eea64f26")
        self.assertTrue(next(o for o in ouro["observations"] if o["observation_id"]==OURO)["lineage"]["merge_commit_is_ancestor"])
if __name__=="__main__": unittest.main()
''',encoding="utf-8")

print("migrated 2 direct S5 observations to neutral raw ownership")
