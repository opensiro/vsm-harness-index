from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGACY_REF = "cb9378131d19eb8362b1a2e5800ca366baefb094"
LEGACY_PATH = "experiments/functional-capability-depth/s1-system-benchmarks/observations.jsonl"
RAW_PATH = ROOT / "experiments" / "functional-capability-depth" / "system-observations" / "public-system-benchmarks.jsonl"

SYSTEM_NAMES = {
    "codex": "Codex",
    "openhands": "OpenHands",
    "swe-agent": "SWE-agent",
    "qwenpaw": "QwenPaw",
    "openclaw": "OpenClaw",
    "hermes-agent": "Hermes Agent",
    "claude-code": "Claude Code",
    "pi": "Pi",
    "oh-my-pi": "oh-my-pi",
    "opencode": "OpenCode",
}


def load_jsonl(text: str) -> list[dict]:
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def expected_neutral(old: dict) -> dict:
    harness_id = old["harness_id"]
    return {
        "schema_version": 1,
        "observation_id": old["record_id"],
        "evidence_source_class": (
            "first-party-reported"
            if harness_id == "qwenpaw" and old["benchmark"]["family_id"] == "pawbench"
            else "external-reproduced"
        ),
        "system_name": SYSTEM_NAMES[harness_id],
        "canonical_harness_id": harness_id,
        "canonical_assessment_ref": f"assessments/{harness_id}.md",
        "canonical_review_ref": old["assessment_ref"],
        "canonical_repository": old["canonical_repository"],
        "published_implementation": old["identity"],
        "benchmark": old["benchmark"],
        "result": old["observation"],
        "provenance": old["provenance"],
        "comparison": old["comparison"],
        "notes": old["notes"],
    }


class S1NeutralRegistryMigration796Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        legacy = subprocess.check_output(
            ["git", "show", f"{LEGACY_REF}:{LEGACY_PATH}"],
            cwd=ROOT,
            text=True,
        )
        cls.old_rows = load_jsonl(legacy)
        cls.new_rows = load_jsonl(RAW_PATH.read_text(encoding="utf-8"))

    def test_all_19_legacy_rows_are_migrated_once(self) -> None:
        self.assertEqual(len(self.old_rows), 19)
        self.assertEqual(len(self.new_rows), 19)
        old_ids = [row["record_id"] for row in self.old_rows]
        new_ids = [row["observation_id"] for row in self.new_rows]
        self.assertEqual(len(new_ids), len(set(new_ids)))
        self.assertEqual(set(new_ids), set(old_ids))

    def test_migration_is_lossless_except_for_neutral_schema_mapping(self) -> None:
        new_by_id = {row["observation_id"]: row for row in self.new_rows}
        for old in self.old_rows:
            expected = expected_neutral(old)
            self.assertEqual(new_by_id[old["record_id"]], expected, old["record_id"])

    def test_raw_rows_have_no_vsm_function_attribution(self) -> None:
        for row in self.new_rows:
            self.assertNotIn("function", row)
            self.assertNotIn("benchmark_fit", row)
            self.assertNotIn("vsm_interpretation", row)

    def test_qwenpaw_pawbench_does_not_overstate_independence(self) -> None:
        qwenpaw = next(
            row
            for row in self.new_rows
            if row["observation_id"]
            == "qwenpaw__pawbench-v1.0__qwen3.6-35b-a3b__20260529"
        )
        self.assertEqual(qwenpaw["evidence_source_class"], "first-party-reported")
        other = [
            row
            for row in self.new_rows
            if row["observation_id"] != qwenpaw["observation_id"]
        ]
        self.assertTrue(all(row["evidence_source_class"] == "external-reproduced" for row in other))


if __name__ == "__main__":
    unittest.main()
