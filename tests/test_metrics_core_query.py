import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_metrics.py"


class CoreMetricsQueryTests(unittest.TestCase):
    def test_core_query_matches_generated_metrics_and_is_write_free(self):
        metrics_path = ROOT / "data" / "metrics.json"
        markdown_path = ROOT / "METRICS.md"
        before_metrics = metrics_path.read_text(encoding="utf-8")
        before_markdown = markdown_path.read_text(encoding="utf-8")

        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--source-root",
                str(ROOT),
                "--stdout-core-json",
            ],
            check=True,
            text=True,
            capture_output=True,
        )
        core = json.loads(completed.stdout)
        generated = json.loads(before_metrics)

        self.assertEqual(
            core["included_assessments"],
            generated["corpus"]["included_assessments"],
        )
        self.assertEqual(
            core["catalog_entries"],
            generated["corpus"]["catalog_entries"],
        )
        self.assertEqual(before_metrics, metrics_path.read_text(encoding="utf-8"))
        self.assertEqual(before_markdown, markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
