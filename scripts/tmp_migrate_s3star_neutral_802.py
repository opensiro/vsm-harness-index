#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S3 = EXP / "s3star-system-benchmarks"
REG = EXP / "system-observations"
BENCH = S3 / "benchmark_observations.json"
CANON = S3 / "canonical_observations.json"
VALIDATOR = S3 / "validate.py"
APPLIED = REG / "appliedscientist.json"
TEST = ROOT / "tests" / "test_s3star_neutral_registry_migration_802.py"

benchmark_old = json.loads(BENCH.read_text(encoding="utf-8"))
canonical_old = json.loads(CANON.read_text(encoding="utf-8"))
all_old = benchmark_old + canonical_old
assert len(benchmark_old) == 3 and len(canonical_old) == 2
assert len({o["observation_id"] for o in all_old}) == 5

DERIVED_KEYS = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "vsm_interpretation",
}
TOP_KEYS = {"evidence_source_class", "system_compatibility", "primary_sources", "canonical_review_revision"}

RAW_TARGETS = {
    "truecall-tau2-retail-silent-failure-2026-06": (
        "truecall-tau2-silent-failure.json",
        "TrueCall + tau2-bench",
        "first-party-reported",
        "TrueCall tau2-bench silent-failure verification",
        "system-benchmark-result",
    ),
    "swe-review-generate-review-revise-2026-07": (
        "swe-review.json",
        "SWE-Review-Bench",
        "first-party-reported",
        None,
        "system-benchmark-result",
    ),
    "harness-bench-pilot4-review-revise-reverify-2026-07": (
        "harness-bench-pilot4.json",
        "harness-bench Pilot 4",
        "first-party-reported",
        None,
        "system-benchmark-result",
    ),
    "appliedscientist-iterative-review-2026-09": (
        "appliedscientist.json",
        "TheAppliedScientist",
        "first-party-reported",
        None,
        "iterative-review-revision-study",
    ),
    "data-to-paper-review-revision-2024": (
        "data-to-paper-review-revision.json",
        "data-to-paper",
        "first-party-reported",
        "Data-to-Paper reviewer-feedback-to-revision publication example",
        "operational-publication-witness",
    ),
}

# Read canonical repository metadata when needed.
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)
def assessment_fields(hid: str) -> dict[str, str]:
    text = (ROOT / "assessments" / f"{hid}.md").read_text(encoding="utf-8")
    m = FRONT.match(text)
    assert m
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out

refs: dict[str, str] = {}
for old in all_old:
    oid = old["observation_id"]
    filename, system_name, source_class, fallback_surface, kind = RAW_TARGETS[oid]
    refs[oid] = filename
    raw_obs = {k: v for k, v in old.items() if k not in DERIVED_KEYS and k not in TOP_KEYS}
    raw_obs["observation_id"] = oid
    raw_obs["kind"] = kind
    if "benchmark" not in raw_obs and fallback_surface:
        raw_obs["evidence_surface"] = fallback_surface

    canonical_harness_id = old.get("canonical_harness_id")
    record: dict = {
        "schema_version": 1,
        "recorded_at": "2026-09-27",
        "evidence_source_class": old.get("evidence_source_class", source_class),
        "system_name": system_name,
        "canonical_harness_id": canonical_harness_id,
        "published_implementation": {
            "system_compatibility": old["system_compatibility"],
            "historical_relation": "Public evidence payload migrated from the pre-neutral S3* function-specific record; S3* interpretation remains derived.",
        },
        "primary_sources": old["primary_sources"],
        "observations": [raw_obs],
    }

    if canonical_harness_id:
        fields = assessment_fields(canonical_harness_id)
        record["canonical_assessment_ref"] = f"assessments/{canonical_harness_id}.md"
        record["canonical_review_ref"] = old["canonical_review_revision"]
        record["canonical_repository"] = fields["repository"]
        assert fields["review_ref"] == old["canonical_review_revision"]
    else:
        revision = old.get("reviewed_system_revision")
        if revision:
            record["published_implementation"]["source_revision"] = revision

    # Preserve the established AppliedScientist neutral evidence-surface label/non-claim.
    if oid == "appliedscientist-iterative-review-2026-09":
        existing = json.loads(APPLIED.read_text(encoding="utf-8"))
        existing_obs = existing["observations"][0]
        raw_obs["benchmark"] = existing_obs["benchmark"]
        if "non_claim" in existing_obs:
            raw_obs["non_claim"] = existing_obs["non_claim"]
        record["published_implementation"] = existing["published_implementation"]
        record["canonical_assessment_ref"] = existing["canonical_assessment_ref"]
        record["canonical_review_ref"] = existing["canonical_review_ref"]
        record["canonical_repository"] = assessment_fields(canonical_harness_id)["repository"]

    (REG / filename).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def projection(old: dict) -> dict:
    out = {k: old[k] for k in DERIVED_KEYS if k in old}
    oid = old["observation_id"]
    out["raw_observation_ref"] = f"../system-observations/{refs[oid]}#{oid}"
    return out

BENCH.write_text(json.dumps([projection(o) for o in benchmark_old], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
CANON.write_text(json.dumps([projection(o) for o in canonical_old], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Hydrate raw evidence before running the existing S3* semantic/coverage checks.
text = VALIDATOR.read_text(encoding="utf-8")
needle = 'CANONICAL_OBSERVATIONS = HERE / "canonical_observations.json"\n'
assert needle in text
text = text.replace(needle, needle + 'RAW_DIR = HERE.parent / "system-observations"\nRAW_PREFIX = "../system-observations/"\n')
insert_at = text.index('\ndef validate_canonical_observation(')
helper = r'''

def hydrate_observation(link: dict) -> dict:
    oid = link.get("observation_id")
    ref = link.get("raw_observation_ref")
    if not isinstance(oid, str) or not oid:
        fail("S3* projection requires observation_id")
    if not isinstance(ref, str) or not ref.startswith(RAW_PREFIX) or "#" not in ref:
        fail(f"{oid}: invalid raw_observation_ref")
    rel, ref_oid = ref[len(RAW_PREFIX):].rsplit("#", 1)
    if ref_oid != oid or not rel.endswith(".json") or "/" in rel:
        fail(f"{oid}: raw_observation_ref drift")
    path = RAW_DIR / rel
    if not path.is_file():
        fail(f"{oid}: neutral raw record missing: {rel}")
    record = json.loads(path.read_text(encoding="utf-8"))
    matches = [obs for obs in record.get("observations", []) if obs.get("observation_id") == oid]
    if len(matches) != 1:
        fail(f"{oid}: expected exactly one neutral raw observation in {rel}")
    raw = matches[0]
    effective = dict(link)
    for key, value in raw.items():
        if key in {"kind", "evidence_surface", "non_claim"}:
            continue
        if key == "observation_id":
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
    return effective
'''
text = text[:insert_at] + helper + text[insert_at:]
old_load = '''    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))\n    canonical_observations = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))\n'''
new_load = '''    benchmark_links = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))\n    canonical_links = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))\n    benchmark_observations = [hydrate_observation(obs) for obs in benchmark_links]\n    canonical_observations = [hydrate_observation(obs) for obs in canonical_links]\n'''
assert old_load in text
text = text.replace(old_load, new_load)
VALIDATOR.write_text(text, encoding="utf-8")

TEST.write_text(r'''from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"; S3=EXP/"s3star-system-benchmarks"
SOURCE_REF="6317c2c57070f50225949104911a90fcdcd58abd"
FILES=("benchmark_observations.json","canonical_observations.json")
DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}
def old_rows():
    out=[]
    for name in FILES:
        txt=subprocess.check_output(["git","show",f"{SOURCE_REF}:experiments/functional-capability-depth/s3star-system-benchmarks/{name}"],cwd=ROOT,text=True)
        out.extend(json.loads(txt))
    return out
def hydrate(link):
    ref=link["raw_observation_ref"]; rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    record=json.loads((REG/rel).read_text(encoding="utf-8")); raw=[o for o in record["observations"] if o["observation_id"]==oid]
    assert len(raw)==1; effective=dict(link)
    for k,v in raw[0].items():
        if k in {"observation_id","kind","evidence_surface","non_claim"}: continue
        effective[k]=v
    effective["evidence_source_class"]=record["evidence_source_class"]
    effective["system_compatibility"]=record["published_implementation"]["system_compatibility"]
    effective["primary_sources"]=record["primary_sources"]
    if record.get("canonical_harness_id"): effective["canonical_review_revision"]=record["canonical_review_ref"]
    return effective
class S3StarNeutralRegistryMigration802Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows(); cls.links=[]
        for name in FILES: cls.links.extend(json.loads((S3/name).read_text(encoding="utf-8")))
        cls.effective={x["observation_id"]:hydrate(x) for x in cls.links}
    def test_five_observations_resolve_once(self):
        self.assertEqual(len(self.old),5); self.assertEqual(len(self.links),5)
        ids={o["observation_id"] for o in self.old}; self.assertEqual(ids,set(self.effective))
        counts={oid:0 for oid in ids}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            for obs in rec.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertTrue(all(v==1 for v in counts.values()),counts)
    def test_moved_fields_are_lossless(self):
        for old in self.old:
            eff=self.effective[old["observation_id"]]
            for key,value in old.items(): self.assertEqual(eff.get(key),value,f"{old['observation_id']}:{key}")
    def test_derived_files_own_only_s3star_interpretation(self):
        for link in self.links:
            self.assertLessEqual(set(link),DERIVED_ALLOWED)
            self.assertIn("raw_observation_ref",link)
            for raw_key in ("primary_sources","paired_runs","reported_mean_baseline_reward","reported_execution_weaknesses_total","audit_loop","published_result_summary"):
                self.assertNotIn(raw_key,link)
    def test_neutral_records_are_vsm_free(self):
        ids={o["observation_id"] for o in self.old}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            selected=[o for o in rec.get("observations",[]) if o.get("observation_id") in ids]
            if not selected: continue
            for forbidden in ("function","benchmark_fit","vsm_interpretation"):
                self.assertNotIn(forbidden,rec)
                for obs in selected: self.assertNotIn(forbidden,obs)
    def test_appliedscientist_reuses_existing_record(self):
        oid="appliedscientist-iterative-review-2026-09"
        hits=[]
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            if any(o.get("observation_id")==oid for o in rec.get("observations",[])): hits.append(path.name)
        self.assertEqual(hits,["appliedscientist.json"])
if __name__=="__main__": unittest.main()
''', encoding="utf-8")

print("migrated 5 S3* evidence payloads to neutral raw ownership")
