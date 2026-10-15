"""Offline tests for non-canonical GitHub star analytics."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/github_stars.py"
spec = importlib.util.spec_from_file_location("github_stars", SCRIPT)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


def fixture(stars):
    return {
        "schema_version": 1, "source_commit": "f" * 40,
        "started_at_utc": "2026-10-11T17:00:00Z", "finished_at_utc": "2026-10-11T17:01:00Z",
        "records": [{"harness_id": str(i), "project_name": str(i), "repository": f"https://github.com/x/r{i}",
                     "stars": n, "fetch_status": "ok" if n is not None else "not_found"}
                    for i, n in enumerate(stars)],
    }


class GitHubStarsTests(unittest.TestCase):
    def test_bins_cover_all_boundaries_without_overlap(self):
        data = fixture([0, 1, 4, 5, 9, 10, 24, 25, 49, 50, 99, 100,
                        249, 250, 499, 500, 999, 1000, 2499, 2500,
                        4999, 5000, 9999, 10000, 24999, 25000, 49999,
                        50000, 99999, 100000, None])
        s = mod.summarize(data)
        self.assertEqual(s["counted"], 30)
        self.assertEqual(s["under_100"], 11)
        self.assertEqual(len(s["unavailable"]), 1)
        self.assertEqual(sum(v["count"] for v in s["bars"]), 30)

    def test_not_found_not_zero(self):
        s = mod.summarize(fixture([0, None, 1]))
        self.assertEqual(s["bars"][0]["count"], 1)
        self.assertEqual(s["counted"], 2)
        self.assertEqual(len(s["unavailable"]), 1)

    def test_inconsistent_fetch_status_rejected(self):
        data = fixture([1])
        data["records"][0]["fetch_status"] = "not_found"
        with self.assertRaisesRegex(ValueError, "invalid star count"):
            mod.summarize(data)

    def test_duplicate_rejected(self):
        data = fixture([1, 2])
        data["records"][1]["harness_id"] = "0"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            mod.summarize(data)

    def test_offline_render_check_and_drift_detection(self):
        data = fixture([0, 5, 50000, None])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "data").mkdir()
            (root / "data/github-stars.json").write_text(json.dumps(data), encoding="utf-8")
            mod.render(root, check=False)
            mod.render(root, check=True)
            self.assertIn("<svg", (root / mod.SVG_PATH).read_text())
            (root / mod.DOC_PATH).write_text("changed", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "differs"):
                mod.render(root, check=True)

    def test_cohort_is_included_only(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "data").mkdir()
            (root / "data/catalog.psv").write_text(
                "harness_id|repository|project_name\na|https://github.com/x/a|A\nb|https://github.com/x/b|B\n",
                encoding="utf-8")
            (root / "data/signatures.psv").write_text(
                "harness_id|signature\na|included\n", encoding="utf-8")
            self.assertEqual([r["harness_id"] for r in mod.included_rows(root)], ["a"])


if __name__ == "__main__":
    unittest.main()
