from __future__ import annotations

import copy
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"
BASE = "8fb9de2275d7b2f2df57d7a0785fd466f710d5dc"
TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:S3\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",
    re.IGNORECASE,
)

current_main = subprocess.check_output(
    ["git", "rev-parse", "origin/main"], cwd=ROOT, text=True
).strip()
if current_main != BASE:
    raise SystemExit(f"main drift: expected {BASE}, got {current_main}")

REPLACEMENTS = (
    ("universal S1 capability", "universal operational-execution capability"),
    ("adapter-preserved S1 evidence", "adapter-preserved operational-execution evidence"),
    ("Coding/SWE-specific S1 evidence", "Coding/SWE-specific operational-execution evidence"),
    ("technical Coding/SWE-domain S1 evidence", "technical Coding/SWE-domain operational-execution evidence"),
    ("historical OpenHands S1 implementation", "historical OpenHands operational-execution implementation"),
    ("historical OpenHands S1 execution", "historical OpenHands operational execution"),
    ("the S1 implementation under test", "the operational-execution implementation under test"),
    (
        "No higher VSM function, ownership state, or self-organizing S claim",
        "No higher organizational function, ownership state, or self-organizing behavior claim",
    ),
    (
        "No S2-S5, ownership, or self-organizing S inference",
        "No other organizational-function, ownership, or self-organizing behavior inference",
    ),
    (
        "does not establish S2-S5 or self-organizing S",
        "does not establish other organizational functions or self-organizing behavior",
    ),
    (
        "PawBench capability slice labels do not establish S2, S3, S3*, S4 or S5 ownership or capability by naming alone.",
        "PawBench capability slice labels do not establish organizational-function ownership or capability by naming alone.",
    ),
    (
        "PawBench slice names do not establish any other VSM function.",
        "PawBench slice names do not establish any other organizational function.",
    ),
    (
        "PawBench capability slice labels such as Planning, Self_Verification or Skill_Use must not be mapped directly to VSM S3, S3*, S4 or other organizational functions.",
        "PawBench capability slice labels such as Planning, Self_Verification or Skill_Use must not be mapped directly to organizational functions by name alone.",
    ),
)

changed_notes: list[tuple[str, str]] = []
for path in sorted(RAW.glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for obs in data.get("observations", []):
        notes = obs.get("notes")
        if not isinstance(notes, str) or TOKEN_RE.search(notes) is None:
            continue
        new_notes = notes
        for old, new in REPLACEMENTS:
            new_notes = new_notes.replace(old, new)
        if new_notes == notes or TOKEN_RE.search(new_notes) is not None:
            raise SystemExit(
                f"unhandled notes vocabulary: {path.name}:{obs.get('observation_id')}: {new_notes}"
            )
        obs["notes"] = new_notes
        changed_notes.append((path.name, obs["observation_id"]))
        changed = True
    if changed:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

if len(changed_notes) != 14 or len({name for name, _ in changed_notes}) != 10:
    raise SystemExit(f"notes scope drift: {changed_notes!r}")

# Field-specific fail-closed neutral value guard.
path = RAW / "render_registry_core.py"
text = path.read_text(encoding="utf-8")
anchor = '''            kind = observation.get("kind")
            if not isinstance(kind, str) or not kind.strip():
                raise RegistryError(f"{record_ref}:{observation_id}: kind must be a non-empty string")

'''
insert = anchor + '''            notes = observation.get("notes")
            if notes is not None:
                if not isinstance(notes, str) or not notes.strip():
                    raise RegistryError(
                        f"{record_ref}:{observation_id}: notes must be a non-empty string when present"
                    )
                if FORBIDDEN_VSM_VALUE_RE.search(notes):
                    raise RegistryError(
                        f"{record_ref}:{observation_id}: notes must remain implementation-independent and VSM-neutral"
                    )

'''
if text.count(anchor) != 1 or "notes must remain implementation-independent" in text:
    raise SystemExit("renderer notes-guard anchor drift")
path.write_text(text.replace(anchor, insert, 1), encoding="utf-8")

# Compose the original S1 migration oracle with the later notes-only cleanup.
path = ROOT / "tests" / "test_s1_neutral_registry_migration_796.py"
text = path.read_text(encoding="utf-8")
old = '''    def test_migration_is_lossless_from_801(self):
        by={r["observation_id"]:r for r in self.new}
        for old in self.old: self.assertEqual(by[old["observation_id"]],old,old["observation_id"])
'''
new = '''    def test_migration_is_lossless_from_801(self):
        by={r["observation_id"]:r for r in self.new}
        for old in self.old:
            current=by[old["observation_id"]]
            expected=dict(old)
            # #833 later neutralizes only function vocabulary in raw notes;
            # the pinned #833 regression owns the exact old -> new note rewrite.
            expected["notes"]=current["notes"]
            self.assertEqual(current,expected,old["observation_id"])
'''
if text.count(old) != 1:
    raise SystemExit("#796 composition anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

# Compose #831's historical_relation oracle with this later notes-only cleanup.
path = ROOT / "tests" / "test_neutral_migration_provenance_values_831.py"
text = path.read_text(encoding="utf-8")
old = '''            normalized = copy.deepcopy(before)
            normalized["published_implementation"]["historical_relation"] = after_relation
            self.assertEqual(normalized, after, path.name)
'''
new = '''            normalized = copy.deepcopy(before)
            normalized["published_implementation"]["historical_relation"] = after_relation

            # #833 later neutralizes function vocabulary in observation notes.
            # Its pinned regression owns the exact notes-only deltas; keep #831
            # strict for every other field in these same raw records.
            after_by_id = {row["observation_id"]: row for row in after.get("observations", [])}
            for row in normalized.get("observations", []):
                current = after_by_id[row["observation_id"]]
                if row.get("notes") != current.get("notes"):
                    row["notes"] = current.get("notes")

            self.assertEqual(normalized, after, path.name)
'''
if text.count(old) != 1:
    raise SystemExit("#831 composition anchor drift")
path.write_text(text.replace(old, new, 1), encoding="utf-8")

# Pinned regression for the exact notes-only transaction.
test = r'''from __future__ import annotations

import copy
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"
BASE_REF = "8fb9de2275d7b2f2df57d7a0785fd466f710d5dc"
TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:S3\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",
    re.IGNORECASE,
)


def old_json(path: Path):
    rel = path.relative_to(ROOT).as_posix()
    text = subprocess.check_output(["git", "show", f"{BASE_REF}:{rel}"], cwd=ROOT, text=True)
    return json.loads(text)


def by_id(rows: list[dict]) -> dict[str, dict]:
    return {row["observation_id"]: row for row in rows}


class NeutralObservationNotes833Tests(unittest.TestCase):
    def test_exactly_14_notes_changed_and_nothing_else_in_raw_json(self) -> None:
        changed_notes = []
        changed_files = []
        for path in sorted(RAW.glob("*.json")):
            before = old_json(path)
            after = json.loads(path.read_text(encoding="utf-8"))
            if before == after:
                continue

            old_rows = by_id(before.get("observations", []))
            new_rows = by_id(after.get("observations", []))
            self.assertEqual(set(old_rows), set(new_rows), path.name)

            normalized = copy.deepcopy(before)
            normalized_rows = by_id(normalized.get("observations", []))
            file_changes = 0
            for oid, old_obs in old_rows.items():
                new_obs = new_rows[oid]
                if old_obs == new_obs:
                    continue
                self.assertIn("notes", old_obs, (path.name, oid))
                self.assertIn("notes", new_obs, (path.name, oid))
                old_note = old_obs["notes"]
                new_note = new_obs["notes"]
                self.assertIsInstance(old_note, str)
                self.assertIsInstance(new_note, str)
                self.assertRegex(old_note, TOKEN_RE, (path.name, oid))
                self.assertIsNone(TOKEN_RE.search(new_note), (path.name, oid, new_note))
                expected_obs = copy.deepcopy(old_obs)
                expected_obs["notes"] = new_note
                self.assertEqual(new_obs, expected_obs, (path.name, oid))
                normalized_rows[oid]["notes"] = new_note
                changed_notes.append((path.name, oid))
                file_changes += 1

            self.assertGreater(file_changes, 0, path.name)
            self.assertEqual(after, normalized, path.name)
            changed_files.append(path.name)

        self.assertEqual(len(changed_notes), 14, changed_notes)
        self.assertEqual(len(changed_files), 10, changed_files)

    def test_all_current_notes_are_vsm_neutral(self) -> None:
        for path in sorted(RAW.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            for obs in data.get("observations", []):
                notes = obs.get("notes")
                if notes is None:
                    continue
                self.assertIsInstance(notes, str, (path.name, obs.get("observation_id")))
                self.assertIsNone(
                    TOKEN_RE.search(notes),
                    (path.name, obs.get("observation_id"), notes),
                )


if __name__ == "__main__":
    unittest.main()
'''
(ROOT / "tests" / "test_neutral_observation_notes_833.py").write_text(test, encoding="utf-8")

print(f"prepared #833: {len(changed_notes)} notes in {len(set(name for name, _ in changed_notes))} files")
