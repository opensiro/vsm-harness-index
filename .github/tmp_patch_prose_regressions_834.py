from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "tests"


def replace_exact(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"{label}: expected exactly one patch anchor, got {text.count(old)}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# #815 owns raw/derived key ownership. #834 now owns the wording of the
# neutral comparison limitation, so normalize that one later prose leaf before
# comparing the pre-ownership and current effective S2 rows.
path = TESTS / "test_direct_projection_neutral_ownership_815.py"
replace_exact(
    path,
    '''            after = hydrate_s2(row, inject_record_level=True)\n            self.assertEqual(after, before, row["observation_id"])\n''',
    '''            after = hydrate_s2(row, inject_record_level=True)\n            if "comparison_limitation" in before and "comparison_limitation" in after:\n                before["comparison_limitation"] = after["comparison_limitation"]\n            self.assertEqual(after, before, row["observation_id"])\n''',
    "#815 S2 prose composition",
)

# #749 still verifies the same proxy/non-admission facts, but raw wording is now
# implementation-independent rather than S-numbered.
path = TESTS / "test_llamar_capability_evidence_749.py"
replace_exact(
    path,
    '        self.assertIn("do not isolate a pure S3", ablation.get("non_claim", ""))\n',
    '        self.assertIn("do not isolate a pure current-control", ablation.get("non_claim", ""))\n',
    "#749 current-control wording",
)
replace_exact(
    path,
    '        self.assertIn("not an S2 attenuation treatment", disturbance.get("non_claim", ""))\n',
    '        self.assertIn("not a coordination-attenuation treatment", disturbance.get("non_claim", ""))\n',
    "#749 coordination wording",
)

# #831 is a historical transaction regression. Compare its before/after commits
# directly so later raw prose cleanups cannot invalidate the historical proof.
path = TESTS / "test_neutral_migration_provenance_values_831.py"
replace_exact(
    path,
    'BASE_REF = "dc534a53c072d392f5cfff26923fbeee407e992c"\n',
    'BASE_REF = "dc534a53c072d392f5cfff26923fbeee407e992c"\nRESULT_REF = "8fb9de2275d7b2f2df57d7a0785fd466f710d5dc"\n',
    "#831 result ref",
)
replace_exact(
    path,
    '''def old_json(path: Path):\n    rel = path.relative_to(ROOT).as_posix()\n    text = subprocess.check_output(["git", "show", f"{BASE_REF}:{rel}"], cwd=ROOT, text=True)\n    return json.loads(text)\n''',
    '''def json_at(ref: str, path: Path):\n    rel = path.relative_to(ROOT).as_posix()\n    text = subprocess.check_output(["git", "show", f"{ref}:{rel}"], cwd=ROOT, text=True)\n    return json.loads(text)\n''',
    "#831 snapshot loader",
)
replace_exact(
    path,
    '''            before = old_json(path)\n            after = json.loads(path.read_text(encoding="utf-8"))\n''',
    '''            before = json_at(BASE_REF, path)\n            after = json_at(RESULT_REF, path)\n''',
    "#831 historical transaction comparison",
)

# #796 proves the S1 migration preserved every structural/result field. Notes are
# now independently owned by #834, so normalize only that prose leaf.
path = TESTS / "test_s1_neutral_registry_migration_796.py"
replace_exact(
    path,
    '''    def test_migration_is_lossless_from_801(self):\n        by={r["observation_id"]:r for r in self.new}\n        for old in self.old: self.assertEqual(by[old["observation_id"]],old,old["observation_id"])\n''',
    '''    def test_migration_is_lossless_from_801(self):\n        by={r["observation_id"]:r for r in self.new}\n        for old in self.old:\n            current=dict(by[old["observation_id"]])\n            current["notes"]=old["notes"]\n            self.assertEqual(current,old,old["observation_id"])\n''',
    "#796 notes composition",
)

# #807 owns the S3 migration shape/result payload; #834 owns the later neutral
# wording of these two caveat fields.
path = TESTS / "test_s3_neutral_registry_migration_807.py"
replace_exact(
    path,
    '''            for key,value in old.items():\n                self.assertEqual(effective.get(key),value,f"{oid}:{key}")\n''',
    '''            for key,value in old.items():\n                if key in {"scope_note","ownership_caveat"}:\n                    self.assertIsInstance(effective.get(key),str,f"{oid}:{key}")\n                    continue\n                self.assertEqual(effective.get(key),value,f"{oid}:{key}")\n''',
    "#807 prose composition",
)

# #824 owns the removed function-specific boolean. Normalize the later #834 prose
# leaves before its whole-record comparison, and assert the new neutral phrase.
path = TESTS / "test_s3star_metric_boundary_824.py"
replace_exact(
    path,
    '''        before_without_boundary["published_implementation"]["historical_relation"] = (\n            after["published_implementation"]["historical_relation"]\n        )\n        self.assertEqual(after, before_without_boundary)\n''',
    '''        before_without_boundary["published_implementation"]["historical_relation"] = (\n            after["published_implementation"]["historical_relation"]\n        )\n        after_observation = next(\n            row for row in after["observations"]\n            if row.get("observation_id") == OBSERVATION_ID\n        )\n        for key in ("metric_note", "comparison_scope_note"):\n            observations[0][key] = after_observation[key]\n        self.assertEqual(after, before_without_boundary)\n''',
    "#824 whole-record prose composition",
)
replace_exact(
    path,
    '        self.assertIn("does not report an aggregate S3*-specific", raw_observation["metric_note"])\n',
    '        self.assertIn("does not report an aggregate independent-review-specific", raw_observation["metric_note"])\n',
    "#824 neutral metric note",
)

# #802 preserves the S3* migration except for prose leaves subsequently owned by #834.
path = TESTS / "test_s3star_neutral_registry_migration_802.py"
replace_exact(
    path,
    '''            for key,value in old.items(): self.assertEqual(eff.get(key),value,f"{old['observation_id']}:{key}")\n''',
    '''            for key,value in old.items():\n                if key in {"external_validation_surface","comparison_scope_note","metric_note","publisher_boundary_note"}:\n                    self.assertIsInstance(eff.get(key),str,f"{old['observation_id']}:{key}")\n                    continue\n                self.assertEqual(eff.get(key),value,f"{old['observation_id']}:{key}")\n''',
    "#802 prose composition",
)

# #809 preserves S4 migration data; these three raw prose leaves are now #834-owned.
path = TESTS / "test_s4_neutral_registry_migration_809.py"
replace_exact(
    path,
    '''            for key,value in old.items():\n                if key=="raw_observation_ref": continue\n                self.assertEqual(effective.get(key),value,f"{oid}:{key}")\n''',
    '''            for key,value in old.items():\n                if key=="raw_observation_ref": continue\n                if key in {"metric_note","mode_boundary","comparability_limitation"}:\n                    self.assertIsInstance(effective.get(key),str,f"{oid}:{key}")\n                    continue\n                self.assertEqual(effective.get(key),value,f"{oid}:{key}")\n''',
    "#809 prose composition",
)

# #810's only later prose rewrite is nested in the G1 aggregate. Preserve exact
# equality for every other field and normalize only the nested scope_note.
path = TESTS / "test_s5_neutral_registry_migration_810.py"
replace_exact(
    path,
    '''            for key,value in old.items(): self.assertEqual(eff.get(key),value,f"{oid}:{key}")\n''',
    '''            for key,value in old.items():\n                if key=="broader_g1_result":\n                    current=dict(eff.get(key))\n                    current["scope_note"]=value["scope_note"]\n                    self.assertEqual(current,value,f"{oid}:{key}")\n                    continue\n                self.assertEqual(eff.get(key),value,f"{oid}:{key}")\n''',
    "#810 nested prose composition",
)

print("patched legacy regressions to compose with #834 neutral prose ownership")
