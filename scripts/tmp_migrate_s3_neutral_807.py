#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S3 = EXP / "s3-system-benchmarks"
REG = EXP / "system-observations"
OBS = S3 / "observations.json"
VALIDATOR = S3 / "validate.py"
TEST = ROOT / "tests" / "test_s3_neutral_registry_migration_807.py"

rows = json.loads(OBS.read_text(encoding="utf-8"))
by_id = {row["observation_id"]: row for row in rows}
OMNI = "omnigent-child-session-recovery-2026-09"
SMAS = "supervisoragent-smas-gaia-pass1-2026"
assert set(by_id) >= {OMNI, SMAS}

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
TOP_RAW_KEYS = {
    "evidence_source_class",
    "system_compatibility",
    "primary_sources",
    "canonical_review_revision",
}

# Omnigent: canonical identity is the assessment snapshot, while the observation itself is a post-assessment descendant.
omni = by_id[OMNI]
omni_raw_obs = {k: v for k, v in omni.items() if k not in DERIVED_KEYS and k not in TOP_RAW_KEYS}
omni_raw_obs["observation_id"] = OMNI
omni_raw_obs["kind"] = "operational-recovery-witness"
omni_raw_obs["evidence_surface"] = "Omnigent child-session recovery operational witness"
omni_record = {
    "schema_version": 1,
    "recorded_at": "2026-09-27",
    "evidence_source_class": omni["evidence_source_class"],
    "system_name": "Omnigent",
    "canonical_harness_id": "omnigent",
    "canonical_assessment_ref": "assessments/omnigent.md",
    "canonical_review_ref": omni["canonical_review_revision"],
    "canonical_repository": "https://github.com/omnigent-ai/omnigent",
    "published_implementation": {
        "system_compatibility": omni["system_compatibility"],
        "source_revision": omni["observation_revision"],
        "manual_validation_revision": omni["manual_validation_revision"],
        "revision_relation": omni["revision_relation"],
        "historical_relation": "The canonical harness identity is bound to the assessment review ref, but this operational witness is explicitly a post-assessment descendant and must not be relabeled as evidence observed at the canonical review revision.",
    },
    "primary_sources": omni["primary_sources"],
    "observations": [omni_raw_obs],
}
(REG / "omnigent-child-session-recovery.json").write_text(
    json.dumps(omni_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

# SupervisorAgent / SMAS: composed benchmark-defined system, deliberately non-canonical.
smas = by_id[SMAS]
smas_raw_obs = {k: v for k, v in smas.items() if k not in DERIVED_KEYS and k not in TOP_RAW_KEYS}
smas_raw_obs["observation_id"] = SMAS
smas_raw_obs["kind"] = "system-benchmark-result"
smas_raw_obs["benchmark"] = "SupervisorAgent SMAS GAIA validation pass@1"
smas_record = {
    "schema_version": 1,
    "recorded_at": "2026-09-27",
    "evidence_source_class": smas["evidence_source_class"],
    "system_name": "SupervisorAgent + SMAS",
    "canonical_harness_id": None,
    "published_implementation": {
        "system_compatibility": smas["system_compatibility"],
        "source_revision": smas["benchmark_artifact_revision"],
        "historical_relation": "Published composed SupervisorAgent/SMAS result. No canonical harness identity is introduced and no capability is transferred to the wrapped base MAS by association.",
    },
    "primary_sources": smas["primary_sources"],
    "observations": [smas_raw_obs],
}
(REG / "supervisoragent-smas.json").write_text(
    json.dumps(smas_record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

# Function-specific projection keeps only S3 classification/linkage for the two migrated rows.
refs = {
    OMNI: "../system-observations/omnigent-child-session-recovery.json#" + OMNI,
    SMAS: "../system-observations/supervisoragent-smas.json#" + SMAS,
}
new_rows = []
for row in rows:
    oid = row["observation_id"]
    if oid not in refs:
        new_rows.append(row)
        continue
    derived = {k: row[k] for k in DERIVED_KEYS if k in row}
    derived["raw_observation_ref"] = refs[oid]
    new_rows.append(derived)
OBS.write_text(json.dumps(new_rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Hydrate only the newly migrated rows before applying the existing semantic checks.
text = VALIDATOR.read_text(encoding="utf-8")
insert_at = text.index("\ndef validate_mao_observation(")
helper = r'''

def hydrate_s3_projection(link: dict) -> dict:
    oid = link.get("observation_id")
    ref = link.get("raw_observation_ref")
    prefix = "../system-observations/"
    if not isinstance(oid, str) or not oid:
        fail("S3 projection requires observation_id")
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
    raw = matches[0]
    effective = dict(link)
    for key, value in raw.items():
        if key in {"observation_id", "kind", "evidence_surface", "benchmark"}:
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
old = '''    validate_mao_observation(by_observation_id[MAO_OBSERVATION_ID])\n    validate_omnigent_observation(by_observation_id[OMNIGENT_OBSERVATION_ID])\n    validate_smas_observation(by_observation_id[SMAS_OBSERVATION_ID])\n'''
new = '''    validate_mao_observation(by_observation_id[MAO_OBSERVATION_ID])\n    validate_omnigent_observation(hydrate_s3_projection(by_observation_id[OMNIGENT_OBSERVATION_ID]))\n    validate_smas_observation(hydrate_s3_projection(by_observation_id[SMAS_OBSERVATION_ID]))\n'''
assert old in text
VALIDATOR.write_text(text.replace(old, new), encoding="utf-8")

TEST.write_text(r'''from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"
S3=EXP/"s3-system-benchmarks"
SOURCE_REF="da303195717b9db468e1993d3e1f988637141d73"
SOURCE_PATH="experiments/functional-capability-depth/s3-system-benchmarks/observations.json"
IDS={"omnigent-child-session-recovery-2026-09","supervisoragent-smas-gaia-pass1-2026"}
DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}

def old_rows():
    text=subprocess.check_output(["git","show",f"{SOURCE_REF}:{SOURCE_PATH}"],cwd=ROOT,text=True)
    return {row["observation_id"]:row for row in json.loads(text) if row["observation_id"] in IDS}

def hydrate(link):
    ref=link["raw_observation_ref"]
    rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    record=json.loads((REG/rel).read_text(encoding="utf-8"))
    matches=[o for o in record["observations"] if o["observation_id"]==oid]
    assert len(matches)==1
    raw=matches[0]
    effective=dict(link)
    for k,v in raw.items():
        if k in {"observation_id","kind","evidence_surface","benchmark"}: continue
        effective[k]=v
    effective["evidence_source_class"]=record["evidence_source_class"]
    effective["system_compatibility"]=record["published_implementation"]["system_compatibility"]
    effective["primary_sources"]=record["primary_sources"]
    if record.get("canonical_harness_id"):
        effective["canonical_review_revision"]=record["canonical_review_ref"]
    return effective

class S3NeutralRegistryMigration807Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows()
        current=json.loads((S3/"observations.json").read_text(encoding="utf-8"))
        cls.links={row["observation_id"]:row for row in current if row["observation_id"] in IDS}
        cls.effective={oid:hydrate(link) for oid,link in cls.links.items()}
    def test_two_rows_migrated_and_resolve_once(self):
        self.assertEqual(set(self.old),IDS); self.assertEqual(set(self.links),IDS)
        counts={oid:0 for oid in IDS}
        for path in REG.glob("*.json"):
            record=json.loads(path.read_text(encoding="utf-8"))
            for obs in record.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertEqual(counts,{oid:1 for oid in IDS})
    def test_moved_fields_are_lossless(self):
        for oid,old in self.old.items():
            effective=self.effective[oid]
            for key,value in old.items():
                self.assertEqual(effective.get(key),value,f"{oid}:{key}")
    def test_derived_rows_own_only_s3_interpretation(self):
        for link in self.links.values():
            self.assertLessEqual(set(link),DERIVED_ALLOWED)
            self.assertIn("raw_observation_ref",link)
            for key in ("primary_sources","reported_operational_witness","regression_evidence","baseline_arm","supervised_arm","reported_average_token_reduction_percent"):
                self.assertNotIn(key,link)
    def test_raw_records_are_vsm_free(self):
        for oid,link in self.links.items():
            rel=link["raw_observation_ref"][len("../system-observations/"):].split("#",1)[0]
            record=json.loads((REG/rel).read_text(encoding="utf-8"))
            obs=next(o for o in record["observations"] if o["observation_id"]==oid)
            for container in (record,obs):
                for forbidden in ("function","benchmark_fit","vsm_interpretation"):
                    self.assertNotIn(forbidden,container)
    def test_boundaries_remain_distinct(self):
        omni=json.loads((REG/"omnigent-child-session-recovery.json").read_text(encoding="utf-8"))
        self.assertEqual(omni["canonical_harness_id"],"omnigent")
        self.assertEqual(omni["canonical_review_ref"],"4d963a360e798f076d4fdbd4665e7188e4da05df")
        self.assertEqual(omni["published_implementation"]["revision_relation"],"post-assessment-descendant")
        smas=json.loads((REG/"supervisoragent-smas.json").read_text(encoding="utf-8"))
        self.assertIsNone(smas["canonical_harness_id"])
        self.assertEqual(smas["published_implementation"]["system_compatibility"],"benchmark-scaffolded")
if __name__=="__main__": unittest.main()
''',encoding="utf-8")

print("migrated remaining 2 direct S3 raw evidence payloads")
