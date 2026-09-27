#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
REG = EXP / "system-observations"
SRC = REG / "public-system-benchmarks.jsonl"
PROJ = EXP / "s1-system-benchmarks" / "observations.jsonl"
CORE = REG / "render_registry_core.py"
WRAP = REG / "render_registry.py"
S1VAL = EXP / "s1-system-benchmarks" / "validate.py"
BASE = EXP / "render_s1_baseline.py"
TEST_MIG = ROOT / "tests" / "test_s1_neutral_registry_migration_796.py"
TEST_REG = ROOT / "tests" / "test_system_observation_registry.py"

rows = [json.loads(line) for line in SRC.read_text(encoding="utf-8").splitlines() if line.strip()]
assert len(rows) == 19
assert len({r["observation_id"] for r in rows}) == 19

groups: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
for row in rows:
    key = (
        row["canonical_harness_id"],
        row["evidence_source_class"],
        row["published_implementation"]["system_compatibility"],
    )
    groups[key].append(row)

ref_by_id: dict[str, str] = {}
for (harness_id, source_class, compatibility), members in sorted(groups.items()):
    first = members[0]
    for key in (
        "system_name",
        "canonical_harness_id",
        "canonical_assessment_ref",
        "canonical_review_ref",
        "canonical_repository",
        "evidence_source_class",
    ):
        assert all(m[key] == first[key] for m in members), (harness_id, key)
    assert all(m["published_implementation"]["system_compatibility"] == compatibility for m in members)

    filename = f"{harness_id}-benchmark-results-{source_class}-{compatibility}.json"
    primary_sources: list[str] = []
    observations: list[dict] = []
    for row in members:
        for src in (row["benchmark"]["primary_source"], row["benchmark"]["artifact_source"]):
            if src not in primary_sources:
                primary_sources.append(src)
        oid = row["observation_id"]
        ref_by_id[oid] = filename
        observations.append(
            {
                "observation_id": oid,
                "kind": "system-benchmark-result",
                "benchmark": row["benchmark"],
                "result": row["result"],
                "published_implementation": row["published_implementation"],
                "provenance": row["provenance"],
                "comparison": row["comparison"],
                "notes": row["notes"],
            }
        )

    record = {
        "schema_version": 1,
        "recorded_at": "2026-09-27",
        "evidence_source_class": source_class,
        "system_name": first["system_name"],
        "canonical_harness_id": harness_id,
        "canonical_assessment_ref": first["canonical_assessment_ref"],
        "canonical_review_ref": first["canonical_review_ref"],
        "canonical_repository": first["canonical_repository"],
        "published_implementation": {
            "system_compatibility": compatibility,
            "historical_relation": "S1 public benchmark results normalized from the #801 neutral row corpus; row-specific historical revision identity remains inside each observation.",
        },
        "primary_sources": primary_sources,
        "observations": observations,
    }
    (REG / filename).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Rewrite derived S1 projection to point to JSON object records.
projection_rows = [json.loads(line) for line in PROJ.read_text(encoding="utf-8").splitlines() if line.strip()]
assert {p["record_id"] for p in projection_rows} == set(ref_by_id)
for p in projection_rows:
    rid = p["record_id"]
    p["raw_observation_ref"] = f"../system-observations/{ref_by_id[rid]}#{rid}"
PROJ.write_text("\n".join(json.dumps(p, separators=(",", ":")) for p in projection_rows) + "\n", encoding="utf-8")

# Neutral core: structured benchmark objects are a valid evidence surface in JSON records.
text = CORE.read_text(encoding="utf-8")
old = '''    benchmark = observation.get("benchmark")\n    if benchmark is not None:\n        if not isinstance(benchmark, str) or not benchmark.strip():\n            raise RegistryError(\n                f"{record_ref}:{observation.get('observation_id')}: benchmark must be a non-empty string"\n            )\n        labels.append(benchmark.strip())\n'''
new = '''    benchmark = observation.get("benchmark")\n    if benchmark is not None:\n        if isinstance(benchmark, str):\n            if not benchmark.strip():\n                raise RegistryError(\n                    f"{record_ref}:{observation.get('observation_id')}: benchmark must be non-empty"\n                )\n            labels.append(benchmark.strip())\n        elif isinstance(benchmark, dict):\n            label = benchmark.get("name")\n            if not isinstance(label, str) or not label.strip():\n                raise RegistryError(\n                    f"{record_ref}:{observation.get('observation_id')}: structured benchmark lacks name"\n                )\n            for key in ("primary_source", "artifact_source"):\n                if not _valid_https(benchmark.get(key)):\n                    raise RegistryError(\n                        f"{record_ref}:{observation.get('observation_id')}: benchmark.{key} must be public HTTPS"\n                    )\n            labels.append(label.strip())\n        else:\n            raise RegistryError(\n                f"{record_ref}:{observation.get('observation_id')}: benchmark must be a string or object"\n            )\n'''
assert old in text
CORE.write_text(text.replace(old, new), encoding="utf-8")

# Retire special JSONL registry parser; one JSON raw schema remains.
WRAP.write_text('''#!/usr/bin/env python3\n"""Render the neutral public-evidence <-> system observation registry."""\n\nfrom render_registry_core import (\n    RegistryError,\n    collect_rows,\n    main,\n)\n\n\nif __name__ == "__main__":\n    main()\n''', encoding="utf-8")

# Shared compact S1 validator over derived refs + hydrated JSON observations.
S1VAL.write_text(r'''#!/usr/bin/env python3
"""Validate the derived S1 projection against neutral JSON observations."""
from __future__ import annotations
import json, re
from pathlib import Path
from urllib.parse import urlparse

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OBS=HERE/"observations.jsonl"
RAW_DIR=HERE.parent/"system-observations"
ALLOWED_COMPAT={"native-system","adapter-preserved"}
ALLOWED_REVISION={"exact-historical","version-known","unknown"}
ALLOWED_COMPARE={"matched-model","partially-matched","descriptive-only"}
ALLOWED_FAMILIES={"swe-bench","terminal-bench","pawbench","claw-swe-bench","frontierharness-v1.0"}
FRONTMATTER=re.compile(r"^---\n(.*?)\n---\n",re.S)
PROJECTION_KEYS={"record_id","function","raw_observation_ref"}
RAW_PREFIX="../system-observations/"

def fail(msg:str)->None: raise SystemExit(f"error: {msg}")
def https(value:object)->bool:
    if not isinstance(value,str): return False
    p=urlparse(value); return p.scheme=="https" and bool(p.netloc)
def assessment_fields(harness_id:str)->dict[str,str]:
    path=ROOT/"assessments"/f"{harness_id}.md"
    if not path.exists(): fail(f"missing canonical assessment for {harness_id}")
    m=FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not m: fail(f"assessment {path} has no front matter")
    out={}
    for line in m.group(1).splitlines():
        if ":" in line:
            k,v=line.split(":",1); out[k.strip()]=v.strip()
    return out
def load_jsonl(path:Path,id_key:str)->list[dict]:
    out=[]
    for lineno,raw in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not raw.strip(): continue
        try: rec=json.loads(raw)
        except json.JSONDecodeError as exc: fail(f"{path.name}:{lineno}: {exc}")
        if not isinstance(rec,dict) or not isinstance(rec.get(id_key),str) or not rec[id_key]: fail(f"{path.name}:{lineno}: missing {id_key}")
        out.append(rec)
    return out
def hydrate(ref:str,rid:str)->dict:
    if not isinstance(ref,str) or not ref.startswith(RAW_PREFIX) or "#" not in ref: fail(f"{rid}: invalid raw_observation_ref")
    rel,oid=ref[len(RAW_PREFIX):].rsplit("#",1)
    if oid!=rid or not rel.endswith(".json") or "/" in rel: fail(f"{rid}: raw_observation_ref drift")
    path=RAW_DIR/rel
    if not path.is_file(): fail(f"{rid}: neutral raw record missing: {rel}")
    record=json.loads(path.read_text(encoding="utf-8"))
    matches=[o for o in record.get("observations",[]) if o.get("observation_id")==rid]
    if len(matches)!=1: fail(f"{rid}: expected exactly one raw observation in {rel}")
    obs=matches[0]
    return {
        "schema_version":record["schema_version"],"observation_id":rid,
        "evidence_source_class":record["evidence_source_class"],"system_name":record["system_name"],
        "canonical_harness_id":record["canonical_harness_id"],"canonical_assessment_ref":record["canonical_assessment_ref"],
        "canonical_review_ref":record["canonical_review_ref"],"canonical_repository":record["canonical_repository"],
        "published_implementation":obs["published_implementation"],"benchmark":obs["benchmark"],"result":obs["result"],
        "provenance":obs["provenance"],"comparison":obs["comparison"],"notes":obs["notes"],
    }
def main()->None:
    records=load_jsonl(OBS,"record_id")
    if not records: fail("no S1 projection observations")
    seen=set(); systems=set(); groups={}
    for rec in records:
        rid=rec["record_id"]
        if rid in seen: fail(f"duplicate record_id: {rid}")
        seen.add(rid)
        if set(rec)!=PROJECTION_KEYS: fail(f"{rid}: S1 projection must not duplicate raw benchmark payload")
        if rec.get("function")!="S1": fail(f"{rid}: function must be S1")
        raw=hydrate(rec.get("raw_observation_ref"),rid)
        harness_id=raw.get("canonical_harness_id")
        if not isinstance(harness_id,str) or not harness_id: fail(f"{rid}: neutral raw observation missing canonical_harness_id")
        systems.add(harness_id)
        assessment=assessment_fields(harness_id)
        if assessment.get("status")!="included": fail(f"{rid}: canonical assessment is not included")
        if assessment.get("autonomy_s1") not in {"A","C","P","A(P)","C(P)"}: fail(f"{rid}: canonical assessment does not establish S1")
        if raw.get("canonical_repository")!=assessment.get("repository"): fail(f"{rid}: canonical_repository drift")
        if raw.get("canonical_review_ref")!=assessment.get("review_ref"): fail(f"{rid}: canonical_review_ref drift")
        if raw.get("canonical_assessment_ref")!=f"assessments/{harness_id}.md": fail(f"{rid}: canonical_assessment_ref drift")
        benchmark=raw.get("benchmark") or {}
        if benchmark.get("family_id") not in ALLOWED_FAMILIES: fail(f"{rid}: benchmark family is not an accepted direct S1 family")
        for key in ("primary_source","artifact_source"):
            if not https(benchmark.get(key)): fail(f"{rid}: benchmark.{key} must be https")
        result=raw.get("result") or {}
        if not isinstance(result.get("model"),str) or not result["model"]: fail(f"{rid}: model is required")
        if not isinstance(result.get("metric"),str) or not result["metric"]: fail(f"{rid}: metric is required")
        if not isinstance(result.get("value"),(int,float)): fail(f"{rid}: numeric metric value is required")
        identity=raw.get("published_implementation") or {}
        if identity.get("system_compatibility") not in ALLOWED_COMPAT: fail(f"{rid}: invalid system_compatibility")
        if identity.get("revision_match") not in ALLOWED_REVISION: fail(f"{rid}: invalid revision_match")
        comparison=raw.get("comparison") or {}; mode=comparison.get("mode"); group=comparison.get("group")
        if mode not in ALLOWED_COMPARE: fail(f"{rid}: invalid comparison mode")
        if not isinstance(group,str) or not group: fail(f"{rid}: comparison group required")
        groups.setdefault(group,[]).append(raw)
        notes=raw.get("notes")
        if not isinstance(notes,str) or len(notes.strip())<20: fail(f"{rid}: explicit interpretation notes required")
    partially=0
    for group,members in groups.items():
        modes={m["comparison"]["mode"] for m in members}; member_systems={m["canonical_harness_id"] for m in members}
        if "matched-model" in modes and len(member_systems)<2: fail(f"{group}: matched-model requires at least two systems")
        if "partially-matched" in modes and len(member_systems)>=2: partially+=1
    print(f"ok: {len(records)} derived S1 observations across {len(systems)} canonical systems")
    print("neutral raw source: experiments/functional-capability-depth/system-observations/*.json")
    print(f"comparison groups: {len(groups)}")
    print(f"cross-system partially-matched groups: {partially}")
if __name__=="__main__": main()
''', encoding="utf-8")

# Baseline renderer: hydrate the same projection refs instead of a special JSONL source.
text = BASE.read_text(encoding="utf-8")
text = text.replace('RAW_OBSERVATIONS = HERE / "system-observations" / "public-system-benchmarks.jsonl"\n', 'RAW_DIR = HERE / "system-observations"\n')
text = text.replace('RAW_PREFIX = "../system-observations/public-system-benchmarks.jsonl#"\n', 'RAW_PREFIX = "../system-observations/"\n')
start = text.index('def load_observations() -> list[dict]:')
end = text.index('\n\ndef matching(', start)
new_loader = r'''def hydrate_raw(ref: str, rid: str) -> dict:
    if not isinstance(ref, str) or not ref.startswith(RAW_PREFIX) or "#" not in ref:
        fail(f"{rid}: invalid raw_observation_ref")
    rel, oid = ref[len(RAW_PREFIX):].rsplit("#", 1)
    if oid != rid or not rel.endswith(".json") or "/" in rel:
        fail(f"{rid}: raw_observation_ref drift")
    path = RAW_DIR / rel
    if not path.is_file():
        fail(f"{rid}: neutral raw record missing: {rel}")
    record = json.loads(path.read_text(encoding="utf-8"))
    matches = [obs for obs in record.get("observations", []) if obs.get("observation_id") == rid]
    if len(matches) != 1:
        fail(f"{rid}: expected exactly one raw observation in {rel}")
    obs = matches[0]
    return {
        "schema_version": record["schema_version"],
        "observation_id": rid,
        "evidence_source_class": record["evidence_source_class"],
        "system_name": record["system_name"],
        "canonical_harness_id": record["canonical_harness_id"],
        "canonical_assessment_ref": record["canonical_assessment_ref"],
        "canonical_review_ref": record["canonical_review_ref"],
        "canonical_repository": record["canonical_repository"],
        "published_implementation": obs["published_implementation"],
        "benchmark": obs["benchmark"],
        "result": obs["result"],
        "provenance": obs["provenance"],
        "comparison": obs["comparison"],
        "notes": obs["notes"],
    }


def load_observations() -> list[dict]:
    projections = load_jsonl(PROJECTION, "record_id")
    selected: list[dict] = []
    seen: set[str] = set()
    for projection in projections:
        rid = projection["record_id"]
        if projection.get("function") != "S1":
            fail(f"{rid}: projection function must be S1")
        if rid in seen:
            fail(f"duplicate S1 projection record_id: {rid}")
        seen.add(rid)
        selected.append(hydrate_raw(projection.get("raw_observation_ref"), rid))
    return selected
'''
text = text[:start] + new_loader + text[end:]
text = text.replace('neutral raw `system-observations/public-system-benchmarks.jsonl` results.', 'neutral raw `system-observations/*.json` results.')
BASE.write_text(text, encoding="utf-8")

# Lossless migration regression against the exact #801 raw corpus.
TEST_MIG.write_text(r'''from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/"experiments"/"functional-capability-depth"/"system-observations"
SOURCE_REF="fe99079baaf48d6fdb23310c13751cbfaef9e2b8"
SOURCE_PATH="experiments/functional-capability-depth/system-observations/public-system-benchmarks.jsonl"

def load_jsonl(text:str)->list[dict]: return [json.loads(line) for line in text.splitlines() if line.strip()]
def expand(record:dict,obs:dict)->dict:
    return {"schema_version":record["schema_version"],"observation_id":obs["observation_id"],
        "evidence_source_class":record["evidence_source_class"],"system_name":record["system_name"],
        "canonical_harness_id":record["canonical_harness_id"],"canonical_assessment_ref":record["canonical_assessment_ref"],
        "canonical_review_ref":record["canonical_review_ref"],"canonical_repository":record["canonical_repository"],
        "published_implementation":obs["published_implementation"],"benchmark":obs["benchmark"],"result":obs["result"],
        "provenance":obs["provenance"],"comparison":obs["comparison"],"notes":obs["notes"]}
class S1NeutralRegistryMigration796Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        old=subprocess.check_output(["git","show",f"{SOURCE_REF}:{SOURCE_PATH}"],cwd=ROOT,text=True)
        cls.old=load_jsonl(old); ids={r["observation_id"] for r in cls.old}; cls.new=[]
        for path in sorted(REG.glob("*.json")):
            record=json.loads(path.read_text(encoding="utf-8"))
            for obs in record.get("observations",[]):
                if obs.get("observation_id") in ids: cls.new.append(expand(record,obs))
    def test_all_19_rows_are_migrated_once(self):
        self.assertEqual(len(self.old),19); self.assertEqual(len(self.new),19)
        self.assertEqual({r["observation_id"] for r in self.old},{r["observation_id"] for r in self.new})
    def test_migration_is_lossless_from_801(self):
        by={r["observation_id"]:r for r in self.new}
        for old in self.old: self.assertEqual(by[old["observation_id"]],old,old["observation_id"])
    def test_raw_records_have_no_vsm_attribution(self):
        ids={r["observation_id"] for r in self.old}
        for path in sorted(REG.glob("*.json")):
            record=json.loads(path.read_text(encoding="utf-8"))
            selected=[o for o in record.get("observations",[]) if o.get("observation_id") in ids]
            if not selected: continue
            for forbidden in ("function","benchmark_fit","vsm_interpretation"):
                self.assertNotIn(forbidden,record)
                for obs in selected: self.assertNotIn(forbidden,obs)
    def test_qwenpaw_pawbench_provenance_preserved(self):
        target=next(r for r in self.new if r["observation_id"]=="qwenpaw__pawbench-v1.0__qwen3.6-35b-a3b__20260529")
        self.assertEqual(target["evidence_source_class"],"first-party-reported")
    def test_neutral_registry_has_one_raw_format(self):
        self.assertEqual(list(REG.glob("*.jsonl")),[])
if __name__=="__main__": unittest.main()
''', encoding="utf-8")

TEST_REG.write_text(r'''from __future__ import annotations
import csv, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REGISTRY_DIR=ROOT/"experiments"/"functional-capability-depth"/"system-observations"
PSV=REGISTRY_DIR/"registry.psv"; MARKDOWN=REGISTRY_DIR/"REGISTRY.md"
class SystemObservationRegistryTests(unittest.TestCase):
    def object_records(self): return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(REGISTRY_DIR.glob("*.json"))]
    def registry_rows(self):
        with PSV.open(encoding="utf-8",newline="") as h: return list(csv.DictReader(h,delimiter="|"))
    def test_registry_is_one_row_per_raw_observation(self):
        raw=[o["observation_id"] for r in self.object_records() for o in r["observations"]]
        rows=self.registry_rows(); ids=[r["observation_id"] for r in rows]
        self.assertEqual(len(raw),len(set(raw))); self.assertEqual(len(ids),len(set(ids))); self.assertEqual(set(ids),set(raw))
    def test_registry_projection_is_neutral(self):
        rows=self.registry_rows(); self.assertTrue(rows); fields=set(rows[0])
        for key in ("observation_id","system_name","canonical_harness_id","evidence_surfaces","evidence_source_class","system_compatibility"): self.assertIn(key,fields)
        for key in ("function","benchmark_fit","canonical_state","autonomy_state"): self.assertNotIn(key,fields)
    def test_registry_does_not_duplicate_numeric_payloads(self):
        rows=self.registry_rows(); allowed={"observation_id","system_name","canonical_harness_id","evidence_surfaces","kind","evidence_source_class","system_compatibility","record_ref"}
        self.assertEqual(set(rows[0]),allowed)
        for row in rows: self.assertTrue((REGISTRY_DIR/row["record_ref"]).is_file())
    def test_generated_markdown_states_interpretation_boundary(self):
        text=MARKDOWN.read_text(encoding="utf-8"); self.assertIn("Raw observations:",text); self.assertIn("VSM-function relevance is intentionally absent",text); self.assertNotIn("| Function |",text)
    def test_current_raw_records_have_explicit_provenance_and_compatibility(self):
        self.assertEqual(list(REGISTRY_DIR.glob("*.jsonl")),[])
        for record in self.object_records():
            self.assertIn(record["evidence_source_class"],{"external-reproduced","first-party-reported","mechanism-only"})
            self.assertIn(record["published_implementation"]["system_compatibility"],{"native-system","adapter-preserved","benchmark-scaffolded","unclear"})
            self.assertTrue(record["primary_sources"]); self.assertTrue(all(s.startswith("https://") for s in record["primary_sources"]))
if __name__=="__main__": unittest.main()
''', encoding="utf-8")

SRC.unlink()
print(f"normalized 19 S1 observations into {len(groups)} JSON records")
