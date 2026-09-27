from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"

SOURCES = (
    ("s1-system-benchmarks/observations.jsonl", "jsonl"),
    ("s2-system-benchmarks/observations.json", "json"),
    ("s2-system-benchmarks/proxy_links.json", "json"),
    ("s3-system-benchmarks/observations.json", "json"),
    ("s3-system-benchmarks/proxy_links.json", "json"),
    ("s3star-system-benchmarks/benchmark_observations.json", "json"),
    ("s3star-system-benchmarks/canonical_observations.json", "json"),
    ("s4-system-benchmarks/benchmark_observations.json", "json"),
    ("s4-system-benchmarks/canonical_observations.json", "json"),
    ("s4-system-benchmarks/proxy_observations.json", "json"),
    ("s5-system-benchmarks/benchmark_observations.json", "json"),
    ("s5-system-benchmarks/canonical_observations.json", "json"),
)

# These are identity/linkage fields, not reusable result/provenance payload.
OBSERVATION_LINKAGE_KEYS = {"observation_id", "benchmark_id"}
RECORD_LINKAGE_KEYS = {"canonical_harness_id", "canonical_assessment_ref"}


def load_rows(path: Path, kind: str) -> list[dict]:
    if kind == "jsonl":
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise AssertionError(f"{path}: expected list")
    return value


def load_raw_path(source_dir: Path, ref_path: str) -> dict:
    path = (source_dir / ref_path).resolve()
    if path.parent != RAW.resolve() or not path.is_file():
        raise AssertionError(f"raw link escapes shared registry or is missing: {ref_path}")
    return json.loads(path.read_text(encoding="utf-8"))


class FunctionProjectionOwnershipOracle825Tests(unittest.TestCase):
    def test_raw_linked_projection_ownership_is_disjoint_except_explicit_linkage(self) -> None:
        checked = 0

        for rel, kind in SOURCES:
            path = EXP / rel
            rows = load_rows(path, kind)
            self.assertTrue(rows, rel)

            for row in rows:
                self.assertIsInstance(row, dict, rel)
                row_id = (
                    row.get("observation_id")
                    or row.get("record_id")
                    or row.get("projection_id")
                    or "<unknown>"
                )
                raw_ref = row.get("raw_observation_ref")
                raw_record_ref = row.get("raw_record")
                self.assertTrue(
                    isinstance(raw_ref, str) ^ isinstance(raw_record_ref, str),
                    f"{rel}:{row_id}: every active projection must have exactly one raw linkage form",
                )

                if isinstance(raw_ref, str):
                    self.assertIn("#", raw_ref, f"{rel}:{row_id}: malformed raw_observation_ref")
                    raw_path_part, raw_observation_id = raw_ref.rsplit("#", 1)
                    record = load_raw_path(path.parent, raw_path_part)
                    matches = [
                        item
                        for item in record.get("observations", [])
                        if isinstance(item, dict)
                        and item.get("observation_id") == raw_observation_id
                    ]
                    self.assertEqual(
                        len(matches),
                        1,
                        f"{rel}:{row_id}: raw_observation_ref must resolve exactly once",
                    )
                    selected = matches
                else:
                    record = load_raw_path(path.parent, raw_record_ref)
                    requested = row.get("raw_observation_ids")
                    self.assertIsInstance(requested, list, f"{rel}:{row_id}: raw_observation_ids required")
                    self.assertTrue(requested, f"{rel}:{row_id}: raw_observation_ids must be non-empty")
                    self.assertEqual(
                        len(requested),
                        len(set(requested)),
                        f"{rel}:{row_id}: duplicate raw_observation_ids",
                    )
                    by_id = {
                        item.get("observation_id"): item
                        for item in record.get("observations", [])
                        if isinstance(item, dict)
                    }
                    missing = set(requested) - set(by_id)
                    self.assertFalse(missing, f"{rel}:{row_id}: missing raw observations: {sorted(missing)}")
                    selected = [by_id[observation_id] for observation_id in requested]

                record_overlap = (set(row) & set(record)) - {"observations"}
                unexpected_record = record_overlap - RECORD_LINKAGE_KEYS
                self.assertFalse(
                    unexpected_record,
                    f"{rel}:{row_id}: derived row re-owns neutral record fields: {sorted(unexpected_record)}",
                )
                for key in record_overlap:
                    self.assertEqual(
                        row[key],
                        record[key],
                        f"{rel}:{row_id}: linkage field {key} conflicts with neutral record",
                    )

                observation_overlap = {
                    key
                    for raw in selected
                    for key in (set(row) & set(raw))
                }
                allowed_observation = set(OBSERVATION_LINKAGE_KEYS)
                if isinstance(raw_record_ref, str):
                    # Proxy rows may own a function-specific claim boundary under the
                    # same generic key as a raw evidence limitation. It must not be a
                    # verbatim second copy of any selected raw non_claim.
                    allowed_observation.add("non_claim")
                unexpected_observation = observation_overlap - allowed_observation
                self.assertFalse(
                    unexpected_observation,
                    f"{rel}:{row_id}: derived row re-owns neutral observation fields: "
                    f"{sorted(unexpected_observation)}",
                )

                for raw in selected:
                    for key in OBSERVATION_LINKAGE_KEYS & set(row) & set(raw):
                        self.assertEqual(
                            row[key],
                            raw[key],
                            f"{rel}:{row_id}: linkage field {key} conflicts with neutral observation",
                        )
                    if "non_claim" in row and "non_claim" in raw:
                        self.assertNotEqual(
                            row["non_claim"],
                            raw["non_claim"],
                            f"{rel}:{row_id}: proxy non_claim duplicates neutral raw evidence verbatim",
                        )

                checked += 1

        self.assertGreaterEqual(checked, 1)


if __name__ == "__main__":
    unittest.main()
