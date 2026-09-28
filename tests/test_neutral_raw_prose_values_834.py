from __future__ import annotations

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
PROSE_FIELDS = {
    "historical_relation", "notes", "non_claim", "metric_note",
    "comparison_scope_note", "scope_note", "external_validation_surface",
    "mode_boundary", "publisher_boundary_note", "comparability_limitation",
    "ownership_caveat", "comparison_limitation",
}
EXPECTED_TARGETS = {tuple(item) for item in [('a-evolve.json', '$.observations[0].metric_note'), ('a-evolve.json', '$.observations[0].non_claim'), ('appliedscientist.json', '$.observations[0].external_validation_surface'), ('appliedscientist.json', '$.observations[0].comparison_scope_note'), ('appliedscientist.json', '$.observations[0].non_claim'), ('claude-code-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('codex-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('codex-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[3].notes'), ('data-to-paper-review-revision.json', '$.observations[0].metric_note'), ('data-to-paper-review-revision.json', '$.observations[0].comparison_scope_note'), ('evoharnessbench.json', '$.observations[0].mode_boundary'), ('govsim-selfgovern.json', '$.observations[0].broader_g1_result.scope_note'), ('harness-bench-pilot4.json', '$.observations[0].publisher_boundary_note'), ('hermes-agent-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('hermes-agent-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[1].notes'), ('hermes-agent-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[3].notes'), ('kadath.json', '$.observations[0].comparability_limitation'), ('kadath.json', '$.observations[0].non_claim'), ('llamar.json', '$.observations[0].non_claim'), ('llamar.json', '$.observations[1].non_claim'), ('magentic-one.json', '$.observations[0].non_claim'), ('magentic-one.json', '$.observations[1].non_claim'), ('magentic-one.json', '$.observations[2].non_claim'), ('multi-agent-orchestration.json', '$.observations[0].non_claim'), ('oh-my-pi-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('omnigent-child-session-recovery.json', '$.observations[0].scope_note'), ('openclaw-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('openclaw-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[1].notes'), ('opencode-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('openhands-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('openhands-benchmark-results-external-reproduced-native-system.json', '$.observations[0].notes'), ('pi-benchmark-results-external-reproduced-adapter-preserved.json', '$.observations[0].notes'), ('qwenpaw-benchmark-results-first-party-reported-adapter-preserved.json', '$.observations[0].notes'), ('squad.json', '$.observations[0].non_claim'), ('squad.json', '$.observations[1].non_claim'), ('supervisoragent-smas.json', '$.observations[0].ownership_caveat'), ('thclaws-operational-history.json', '$.observations[0].comparison_limitation')]}


def old_json(path: Path):
    rel = path.relative_to(ROOT).as_posix()
    text = subprocess.check_output(["git", "show", f"{BASE_REF}:{rel}"], cwd=ROOT, text=True)
    return json.loads(text)


def leaf_diffs(before, after, path="$"):
    if type(before) is not type(after):
        return [(path, before, after)]
    if isinstance(before, dict):
        if set(before) != set(after):
            return [(path, before, after)]
        out = []
        for key in before:
            out.extend(leaf_diffs(before[key], after[key], f"{path}.{key}"))
        return out
    if isinstance(before, list):
        if len(before) != len(after):
            return [(path, before, after)]
        out = []
        for index, (left, right) in enumerate(zip(before, after)):
            out.extend(leaf_diffs(left, right, f"{path}[{index}]"))
        return out
    return [] if before == after else [(path, before, after)]


def walk(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            yield key, child_path, child
            yield from walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


class NeutralRawProseValues834Tests(unittest.TestCase):
    def test_exact_37_raw_string_leaves_changed_and_nothing_else(self):
        actual = set()
        for path in sorted(RAW.glob("*.json")):
            before = old_json(path)
            after = json.loads(path.read_text(encoding="utf-8"))
            for json_path, old, new in leaf_diffs(before, after):
                actual.add((path.name, json_path))
                self.assertIsInstance(old, str, (path.name, json_path))
                self.assertIsInstance(new, str, (path.name, json_path))
                self.assertIsNotNone(TOKEN_RE.search(old), (path.name, json_path, old))
                self.assertIsNone(TOKEN_RE.search(new), (path.name, json_path, new))
        self.assertEqual(actual, EXPECTED_TARGETS)
        self.assertEqual(len(actual), 37)

    def test_all_guarded_neutral_prose_is_free_of_explicit_vsm_tokens(self):
        hits = []
        for path in sorted(RAW.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            for key, json_path, value in walk(data):
                if key in PROSE_FIELDS and isinstance(value, str) and TOKEN_RE.search(value):
                    hits.append((path.name, json_path, value))
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
