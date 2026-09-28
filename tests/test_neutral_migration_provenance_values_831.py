from __future__ import annotations

import copy
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"
BASE_REF = "dc534a53c072d392f5cfff26923fbeee407e992c"
RESULT_REF = "8fb9de2275d7b2f2df57d7a0785fd466f710d5dc"
TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:S3\*|S[1-5]|VSM|Viable System Model)(?![A-Za-z0-9])",
    re.IGNORECASE,
)


def json_at(ref: str, path: Path):
    rel = path.relative_to(ROOT).as_posix()
    text = subprocess.check_output(["git", "show", f"{ref}:{rel}"], cwd=ROOT, text=True)
    return json.loads(text)


class NeutralMigrationProvenanceValues831Tests(unittest.TestCase):
    def test_only_historical_relation_changed_in_exact_28_raw_records(self):
        changed = []
        for path in sorted(RAW.glob("*.json")):
            before = json_at(BASE_REF, path)
            after = json_at(RESULT_REF, path)
            before_relation = (before.get("published_implementation") or {}).get("historical_relation")
            after_relation = (after.get("published_implementation") or {}).get("historical_relation")

            if before_relation == after_relation:
                continue

            changed.append(path.name)
            self.assertIsInstance(before_relation, str, path.name)
            self.assertRegex(before_relation, TOKEN_RE, path.name)
            self.assertIsInstance(after_relation, str, path.name)
            self.assertIsNone(TOKEN_RE.search(after_relation), path.name)

            normalized = copy.deepcopy(before)
            normalized["published_implementation"]["historical_relation"] = after_relation
            self.assertEqual(normalized, after, path.name)

        self.assertEqual(len(changed), 28, changed)

    def test_all_current_historical_relation_values_are_vsm_neutral(self):
        for path in sorted(RAW.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            relation = (data.get("published_implementation") or {}).get("historical_relation")
            if relation is not None:
                self.assertIsInstance(relation, str, path.name)
                self.assertIsNone(TOKEN_RE.search(relation), (path.name, relation))


if __name__ == "__main__":
    unittest.main()
