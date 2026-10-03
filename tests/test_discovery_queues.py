from __future__ import annotations

import importlib.util
from io import BytesIO
from pathlib import Path
import sys
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_discovery_queues.py"
SPEC = importlib.util.spec_from_file_location("check_discovery_queues", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class DiscoveryQueueParsingTests(unittest.TestCase):
    def test_normalize_repository_url(self) -> None:
        self.assertEqual(
            module.normalize_repo("https://github.com/openai/openai-agents-js.git/"),
            "openai/openai-agents-js",
        )

    def test_normalize_owner_repo(self) -> None:
        self.assertEqual(module.normalize_repo("`strands-agents/harness-sdk`"), "strands-agents/harness-sdk")

    def test_tracked_queue_title_families(self) -> None:
        for title in (
            "[Candidate batch] Runtime harnesses",
            "[Candidate-batch] Runtime harnesses",
            "[Assessment batch] Runtime harnesses",
            "[Assessment-batch] Runtime harnesses",
            "[Evidence intake] Governance/control candidates",
            "[Evidence-intake] Governance/control candidates",
        ):
            with self.subTest(title=title):
                self.assertTrue(module.is_tracked_queue_title(title))

    def test_non_queue_title_is_ignored(self) -> None:
        for title in (
            "[Related awesome export] Source tracker",
            "[Experiment] Frozen fixture",
            "[Analytics roadmap] Reports",
        ):
            with self.subTest(title=title):
                self.assertFalse(module.is_tracked_queue_title(title))

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


    def test_parse_frozen_review_ref_header(self) -> None:
        body = """| # | Project | Canonical repository | Frozen review ref |
| ---: | --- | --- | --- |
| 1 | Alpha | `owner/alpha` | `1111111111111111111111111111111111111111` |
"""
        self.assertEqual(module.parse_candidate_repositories(body), ["owner/alpha"])

    def test_source_candidate_batch_routes_assessment_control(self) -> None:
        body = "Source candidate batch: #918\nFrozen refs: copied unchanged from #918"
        self.assertEqual(module.source_candidate_batch(body), 918)

    def test_logical_queue_numbers_collapse_source_and_assessment_control(self) -> None:
        entries = [
            module.QueueEntry(918, "[Candidate batch] X", "owner/alpha", frozen=True),
            module.QueueEntry(
                989,
                "[Assessment batch] X",
                "owner/alpha",
                frozen=True,
                source_issue_number=918,
            ),
        ]
        self.assertEqual(module.logical_queue_numbers(entries), [918])

    def test_logical_queue_numbers_preserve_independent_batches(self) -> None:
        entries = [
            module.QueueEntry(918, "[Candidate batch] X", "owner/alpha", frozen=True),
            module.QueueEntry(966, "[Candidate batch] Y", "owner/alpha", frozen=True),
        ]
        self.assertEqual(module.logical_queue_numbers(entries), [918, 966])

    def test_parse_legacy_batch_occupancy(self) -> None:
        self.assertEqual(module.declared_active_occupancy("Batch occupancy: **7/10**"), 7)

    def test_parse_modern_remaining_active_occupancy(self) -> None:
        self.assertEqual(
            module.declared_active_occupancy(
                "**Manual assessment queue. Batch frozen at 10/10. Remaining active candidate occupancy: 9/10.**"
            ),
            9,
        )

    def test_absent_active_occupancy_is_none(self) -> None:
        self.assertIsNone(module.declared_active_occupancy("Batch frozen at 10/10."))

    def test_frozen_batch_is_detected(self) -> None:
        self.assertTrue(module.is_frozen_queue("Candidate intake. Batch complete and frozen at 10/10."))
        self.assertTrue(module.is_frozen_queue("Manual assessment queue. Batch frozen at 10/10."))
        self.assertFalse(module.is_frozen_queue("Candidate intake. Batch occupancy: 7/10."))

    def test_frozen_completed_rows_become_historical(self) -> None:
        entries = [module.QueueEntry(10, "[Candidate batch] X", "owner/done", frozen=True)]
        active, errors, warnings = module.classify_queue_entries(
            entries,
            included={"owner/done": "owner/done"},
            proposed={},
            catalog_names={"owner/done": "owner/done"},
        )
        self.assertEqual(active, [])
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_frozen_unprocessed_rows_remain_active(self) -> None:
        entry = module.QueueEntry(10, "[Candidate batch] X", "owner/pending", frozen=True)
        active, errors, warnings = module.classify_queue_entries(
            [entry], included={}, proposed={}, catalog_names={}
        )
        self.assertEqual(active, [entry])
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_remaining_active_occupancy_uses_filtered_rows(self) -> None:
        entries = [
            module.QueueEntry(12, "[Candidate batch] X", "owner/done", frozen=True),
            module.QueueEntry(12, "[Candidate batch] X", "owner/pending", frozen=True),
        ]
        active, _errors, _warnings = module.classify_queue_entries(
            entries,
            included={"owner/done": "owner/done"},
            proposed={},
            catalog_names={"owner/done": "owner/done"},
        )
        self.assertEqual(module.validate_remaining_occupancies(active, {12: 1}), [])
        self.assertEqual(
            module.validate_remaining_occupancies(active, {12: 2}),
            ["#12: declared remaining active occupancy 2/10 != 1/10 active rows"],
        )

    def test_live_queue_canonical_overlap_still_fails(self) -> None:
        entry = module.QueueEntry(11, "[Candidate batch] X", "owner/already", frozen=False)
        active, errors, _warnings = module.classify_queue_entries(
            [entry],
            included={"owner/already": "owner/already"},
            proposed={},
            catalog_names={"owner/already": "owner/already"},
        )
        self.assertEqual(active, [entry])
        self.assertIn("#11: owner/already is already canonical status=included", errors)
        self.assertIn("#11: owner/already is already present in data/catalog.psv", errors)

    def test_non_candidate_table_is_ignored(self) -> None:
        body = """| Project | Notes |
| --- | --- |
| Alpha | `owner/alpha` |
"""
        self.assertEqual(module.parse_candidate_repositories(body), [])


class DiscoveryQueueGitHubAPITests(unittest.TestCase):
    def test_get_retries_transient_timeout(self) -> None:
        api = module.GitHubAPI("token")
        response = BytesIO(b'{"ok": true}')
        with (
            mock.patch.object(
                module.urllib.request,
                "urlopen",
                side_effect=[TimeoutError("temporary timeout"), response],
            ) as urlopen,
            mock.patch.object(module.time, "sleep") as sleep,
        ):
            self.assertEqual(api.get("/example"), {"ok": True})

        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1)

    def test_repository_identity_404_is_unresolved_not_fatal(self) -> None:
        api = module.GitHubAPI("token")
        not_found = module.urllib.error.HTTPError(
            "https://api.github.com/repos/gone/repo",
            404,
            "Not Found",
            {},
            None,
        )
        with mock.patch.object(module.urllib.request, "urlopen", side_effect=not_found):
            self.assertIsNone(api.repository_identity("gone/repo"))


if __name__ == "__main__":
    unittest.main()
