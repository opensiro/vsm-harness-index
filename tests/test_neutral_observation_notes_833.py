from __future__ import annotations

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
