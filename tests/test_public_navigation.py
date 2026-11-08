"""Guard human navigation and generated links to canonical assessment evidence."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
RECORD_RE = re.compile(
    r'<a id="([^"]+)"></a>\[[^\]]+\]'
    r'\((assessments/[^)]+\.md)\) '
    r'\(\[source\]\((https://github\.com/[^)]+)\)\)'
)


class PublicNavigationTests(unittest.TestCase):
    def test_readme_browse_paths_and_examples(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        human = text.split("## I'm human\n", 1)[1].split("\n## I'm AI", 1)[0]
        for marker in (
            "https://opensiro.com/vsm-index.html",
            "https://opensiro.com/harness-monitor.html",
            "https://opensiro.com/harness-server.html",
            "[TLDR.md](TLDR.md)",
            "[RANKINGS.md](RANKINGS.md)",
            "[FULL_A.md](FULL_A.md)",
            "[Sources and attribution](SOURCES.md)",
            "[Henterprise](assessments/he/henterprise.md)",
            "[Onion Harness](assessments/on/onion-harness.md)",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, human)

    def test_generated_views_link_included_canonical_evidence_and_source(self):
        metrics = json.loads((ROOT / "data/metrics.json").read_text(encoding="utf-8"))
        included = metrics["corpus"]["included_assessments"]
        full_a = metrics["corpus"]["full_a_assessments"]
        ids_by_view = {}
        for view, count in (("TLDR.md", included), ("RANKINGS.md", included), ("FULL_A.md", full_a)):
            content = (ROOT / view).read_text(encoding="utf-8")
            matches = RECORD_RE.findall(content)
            with self.subTest(view=view):
                self.assertEqual(len(matches), count)
                ids = [harness_id for harness_id, _, _ in matches]
                self.assertEqual(len(ids), len(set(ids)))
                for harness_id, path, upstream in matches:
                    self.assertEqual(
                        path,
                        f"assessments/{harness_id[:2]}/{harness_id}.md",
                    )
                    self.assertTrue((ROOT / path).is_file(), path)
                    self.assertTrue(upstream.startswith("https://github.com/"))
                ids_by_view[view] = set(ids)
        self.assertEqual(ids_by_view["TLDR.md"], ids_by_view["RANKINGS.md"])
        self.assertLessEqual(ids_by_view["FULL_A.md"], ids_by_view["TLDR.md"])


if __name__ == "__main__":
    unittest.main()
