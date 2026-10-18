"""Issue #55: shallow sharding must preserve and protect canonical corpus discovery."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from assessment_paths import paths, shard, sharded_path  # noqa: E402
from validate_tldr import load_assessments  # noqa: E402
import assessment_preflight as preflight  # noqa: E402


def record(slug: str, repo: str) -> str:
    return f"---\nharness_id: {slug}\nrepository: https://github.com/{repo}\nstatus: proposed\n---\n"


class ShardingTests(unittest.TestCase):
    def test_flat_and_sharded_discovery(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td) / "assessments"
            directory.mkdir()
            (directory / "agent-one.md").write_text(record("agent-one", "org/one"))
            other = sharded_path(directory, "agent-two")
            other.parent.mkdir()
            other.write_text(record("agent-two", "org/two"))
            self.assertEqual(set(load_assessments(directory)), {"agent-one", "agent-two"})
            self.assertEqual(len(paths(directory)), 2)
            self.assertEqual(preflight.resolve_assessment_path(Path(td), "agent-two", "org/two"),
                             ("assessments/ag/agent-two.md", "existing"))
            self.assertEqual(preflight.resolve_assessment_path(Path(td), "agent-three", "org/three"),
                             ("assessments/ag/agent-three.md", "new"))

    def test_duplicate_identity_fails_closed_across_layouts(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td) / "assessments"
            directory.mkdir()
            (directory / "agent-one.md").write_text(record("agent-one", "org/one"))
            copy = sharded_path(directory, "agent-one")
            copy.parent.mkdir()
            copy.write_text(record("agent-one", "org/one"))
            with self.assertRaisesRegex(ValueError, "duplicate"):
                load_assessments(directory)
            with self.assertRaisesRegex(preflight.PreflightError, "duplicate"):
                preflight.resolve_assessment_path(Path(td), "agent-one", "org/one")

    def test_invalid_shard_and_deep_paths_fail_closed(self):
        with tempfile.TemporaryDirectory() as td:
            directory = Path(td)
            wrong = directory / "zz" / "agent-one.md"
            wrong.parent.mkdir()
            wrong.write_text(record("agent-one", "org/one"))
            with self.assertRaisesRegex(ValueError, "shard"):
                paths(directory)
            wrong.unlink()
            deep = directory / "ag" / "nested" / "agent-one.md"
            deep.parent.mkdir(parents=True)
            deep.write_text(record("agent-one", "org/one"))
            with self.assertRaisesRegex(ValueError, "shard"):
                paths(directory)

    def test_live_corpus_uses_shards_only(self):
        repo = Path(__file__).resolve().parents[1]
        directory = repo / "assessments"
        self.assertFalse(list(directory.glob("*.md")), "flat assessment files remain")
        records = paths(directory)
        self.assertGreater(len(records), 0)
        self.assertEqual(len(records), len(load_assessments(directory)))
        for path in records:
            self.assertEqual(path.parent.name, shard(path.stem))

    def test_shard_is_stable(self):
        self.assertEqual(shard("agent-zero"), "ag")
        self.assertEqual(shard("1code"), "1c")


if __name__ == "__main__":
    unittest.main()
