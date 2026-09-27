#!/usr/bin/env python3
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
