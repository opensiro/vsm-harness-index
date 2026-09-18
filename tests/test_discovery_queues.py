from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_discovery_queues.py"
SPEC = importlib.util.spec_from_file_location("check_discovery_queues", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class DiscoveryQueueParsingTests(unittest.TestCase):
    def test_normalize_repository_url(self) -> None:
        self.assertEqual(
            module.normalize_repo("https://github.com/openai/openai-agents-js.git/"),
            "openai/openai-agents-js",
        )

    def test_normalize_owner_repo(self) -> None:
        self.assertEqual(module.normalize_repo("`strands-agents/harness-sdk`"), "strands-agents/harness-sdk")

    def test_parse_current_candidate_table(self) -> None:
        body = """## Candidates pinned for intake

| Project | Canonical repository | Review ref | Role / why in scope |
| --- | --- | --- | --- |
| Alpha | `owner/alpha` | `1111111111111111111111111111111111111111` | runtime |
| Beta | `https://github.com/owner/beta` | `2222222222222222222222222222222222222222` | runtime |
"""
        self.assertEqual(module.parse_candidate_repositories(body), ["owner/alpha", "owner/beta"])

    def test_parse_repository_header_variant(self) -> None:
        body = """| Project | Repository | Review ref |
| --- | --- | --- |
| Alpha | `owner/alpha` | `1111111111111111111111111111111111111111` |
"""
        self.assertEqual(module.parse_candidate_repositories(body), ["owner/alpha"])

    def test_non_candidate_table_is_ignored(self) -> None:
        body = """| Project | Notes |
| --- | --- |
| Alpha | `owner/alpha` |
"""
        self.assertEqual(module.parse_candidate_repositories(body), [])


if __name__ == "__main__":
    unittest.main()
