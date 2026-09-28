from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"
RENDER = RAW / "render_registry_core.py"
TESTS = ROOT / "tests"
BASE_REF = "dc534a53c072d392f5cfff26923fbeee407e992c"

TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:S3\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",
    re.IGNORECASE,
)

REPLACEMENTS = (
    ("S1 public benchmark results", "Public benchmark results"),
    ("pre-neutral S2 evidence record", "predecessor function-specific evidence record"),
    ("no canonical S2 linkage", "no canonical organizational-function linkage"),
    ("Benchmark-defined S4 evidence", "Benchmark-defined evidence"),
    ("pre-neutral S3* function-specific record", "predecessor function-specific record"),
    ("S3* interpretation", "organizational interpretation"),
    ("canonical S4 ownership", "canonical organizational-function ownership"),
    ("VSM-function meaning", "organizational-function meaning"),
)

changed: list[str] = []
for path in sorted(RAW.glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    implementation = data.get("published_implementation")
    if not isinstance(implementation, dict):
        continue
    relation = implementation.get("historical_relation")
    if not isinstance(relation, str) or not TOKEN_RE.search(relation):
        continue

    original = relation
    for old, new in REPLACEMENTS:
        relation = relation.replace(old, new)
    if TOKEN_RE.search(relation):
        raise SystemExit(
            f"{path.name}: historical_relation still contains explicit VSM/function vocabulary after rewrite: {relation!r}"
        )
    if relation == original:
        raise SystemExit(f"{path.name}: semantic hit was not rewritten")

    implementation["historical_relation"] = relation
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    changed.append(path.name)

if len(changed) != 28:
    raise SystemExit(f"expected 28 historical_relation rewrites, got {len(changed)}: {changed}")

# Add a fail-closed value-level guard specifically for neutral migration/provenance prose.
text = RENDER.read_text(encoding="utf-8")
anchor = 'HEX40_RE = re.compile(r"^[0-9a-f]{40}$")\n'
insert = '''HEX40_RE = re.compile(r"^[0-9a-f]{40}$")\nFORBIDDEN_VSM_VALUE_RE = re.compile(\n    r"(?<![A-Za-z0-9])(?:S3\\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",\n    re.IGNORECASE,\n)\n'''
if text.count(anchor) != 1:
    raise SystemExit("render_registry_core.py regex anchor drift")
if "FORBIDDEN_VSM_VALUE_RE" in text:
    raise SystemExit("render_registry_core.py value guard already present")
text = text.replace(anchor, insert, 1)

anchor = '''        compatibility = implementation.get("system_compatibility")\n        if compatibility not in SYSTEM_COMPATIBILITY:\n            raise RegistryError(\n                f"{record_ref}: system_compatibility must be one of {sorted(SYSTEM_COMPATIBILITY)}"\n            )\n\n'''
insert = anchor + '''        historical_relation = implementation.get("historical_relation")\n        if historical_relation is not None:\n            if not isinstance(historical_relation, str) or not historical_relation.strip():\n                raise RegistryError(\n                    f"{record_ref}: published_implementation.historical_relation must be a non-empty string when present"\n                )\n            if FORBIDDEN_VSM_VALUE_RE.search(historical_relation):\n                raise RegistryError(\n                    f"{record_ref}: published_implementation.historical_relation must remain implementation-independent and VSM-neutral"\n                )\n\n'''
if text.count(anchor) != 1:
    raise SystemExit("render_registry_core.py implementation anchor drift")
text = text.replace(anchor, insert, 1)
RENDER.write_text(text, encoding="utf-8")

(TESTS / "test_neutral_migration_provenance_values_831.py").write_text(
    f'''from __future__ import annotations\n\nimport copy\nimport json\nimport re\nimport subprocess\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nRAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"\nBASE_REF = "{BASE_REF}"\nTOKEN_RE = re.compile(\n    r"(?<![A-Za-z0-9])(?:S3\\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",\n    re.IGNORECASE,\n)\n\n\ndef old_json(path: Path):\n    rel = path.relative_to(ROOT).as_posix()\n    text = subprocess.check_output(["git", "show", f"{{BASE_REF}}:{{rel}}"], cwd=ROOT, text=True)\n    return json.loads(text)\n\n\nclass NeutralMigrationProvenanceValues831Tests(unittest.TestCase):\n    def test_only_historical_relation_changed_in_exact_28_raw_records(self):\n        changed = []\n        for path in sorted(RAW.glob("*.json")):\n            before = old_json(path)\n            after = json.loads(path.read_text(encoding="utf-8"))\n            before_relation = (before.get("published_implementation") or {{}}).get("historical_relation")\n            after_relation = (after.get("published_implementation") or {{}}).get("historical_relation")\n\n            if before_relation == after_relation:\n                continue\n\n            changed.append(path.name)\n            self.assertIsInstance(before_relation, str, path.name)\n            self.assertRegex(before_relation, TOKEN_RE, path.name)\n            self.assertIsInstance(after_relation, str, path.name)\n            self.assertIsNone(TOKEN_RE.search(after_relation), path.name)\n\n            normalized = copy.deepcopy(before)\n            normalized["published_implementation"]["historical_relation"] = after_relation\n            self.assertEqual(normalized, after, path.name)\n\n        self.assertEqual(len(changed), 28, changed)\n\n    def test_all_current_historical_relation_values_are_vsm_neutral(self):\n        for path in sorted(RAW.glob("*.json")):\n            data = json.loads(path.read_text(encoding="utf-8"))\n            relation = (data.get("published_implementation") or {{}}).get("historical_relation")\n            if relation is not None:\n                self.assertIsInstance(relation, str, path.name)\n                self.assertIsNone(TOKEN_RE.search(relation), (path.name, relation))\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print(f"prepared #831: rewrote {len(changed)} neutral historical_relation values")
