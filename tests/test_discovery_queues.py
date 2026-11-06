from __future__ import annotations

import importlib.util
from contextlib import redirect_stderr, redirect_stdout
from io import BytesIO, StringIO
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


    def test_parse_candidate_rows_preserves_review_ref(self) -> None:
        body = """| # | Project | Canonical repository | Frozen review ref |
| ---: | --- | --- | --- |
| 1 | Alpha | `owner/alpha` | `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` |
"""
        self.assertEqual(
            module.parse_candidate_rows(body),
            [("owner/alpha", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")],
        )

    def test_parse_five_row_controller_with_immutable_ref_header(self) -> None:
        body = """## Frozen source map

| # | Candidate | Canonical repo | Immutable review_ref |
| ---: | --- | --- | --- |
| 1 | Alpha | `owner/alpha` | `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` |
| 2 | Beta | `owner/beta` | `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb` |
"""
        self.assertEqual(
            module.parse_candidate_rows(body),
            [
                ("owner/alpha", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
                ("owner/beta", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"),
            ],
        )

    def test_source_candidate_batch_routes_assessment_control(self) -> None:
        body = "Source candidate batch: #918\nFrozen refs: copied unchanged from #918"
        self.assertEqual(module.source_candidate_batch(body), 918)

    def test_immutable_discovery_owner_links_route_serial_controllers(self) -> None:
        for owner, body in (
            (2896, "Immutable discovery owner [#2896](https://github.com/opensiro/vsm-harness-index/issues/2896)."),
            (2899, "Immutable discovery owner: [#2899](https://github.com/opensiro/vsm-harness-index/issues/2899)."),
        ):
            with self.subTest(owner=owner):
                self.assertEqual(module.source_candidate_batch(body), owner)
                self.assertTrue(module.is_frozen_control_queue(body))

        self.assertIsNone(module.source_candidate_batch("Related sibling intake #2896 is not the owner"))

    def test_completed_immutable_owner_controllers_are_not_active_collisions(self) -> None:
        issues = []
        for number, owner, repository, ref, heading in (
            (2897, 2896, "phuryn/mini-harness", "7ae9fca8221c55bd3c38697a61075357e1a94c26", "Immutable discovery owner"),
            (2900, 2899, "agentjido/jido_harness", "20fe00f7e954b8634b5ca73fc8cb7ee55230de24", "Immutable discovery owner:"),
        ):
            body = (
                f"{heading} [#{owner}](https://github.com/opensiro/vsm-harness-index/issues/{owner}).\n\n"
                "| # | Candidate | Repository | Frozen review_ref |\n"
                "| ---: | --- | --- | --- |\n"
                f"| 1 | Completed | `{repository}` | `{ref}` |\n"
            )
            issues.append({"number": number, "title": "[Assessment batch] Serial five", "body": body})

        api = mock.Mock()
        api.open_issues.return_value = issues
        entries, occupancies, parse_errors = module.active_queue_entries(api, "opensiro/vsm-harness-index")
        self.assertEqual(parse_errors, [])
        self.assertEqual(occupancies, {})
        self.assertEqual([entry.logical_queue_number for entry in entries], [2896, 2899])
        self.assertTrue(all(entry.frozen for entry in entries))
        included = {entry.repository.lower(): entry.repository for entry in entries}
        active, errors, warnings = module.classify_queue_entries(entries, included, {}, included)
        self.assertEqual((active, errors, warnings), ([], [], []))


    def test_assessment_control_is_frozen_by_source_routing(self) -> None:
        body = "Source candidate batch: #918\nFrozen refs: copied unchanged from #918"
        self.assertTrue(module.is_frozen_control_queue(body))

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


    def test_exact_snapshot_duplicate_requires_same_ref_across_queues(self) -> None:
        ref = "cd7ec0ee2031d1723e1d38593d43385778fd5d30"
        entries = [
            module.QueueEntry(918, "[Candidate batch] X", "owner/old", frozen=True, review_ref=ref),
            module.QueueEntry(966, "[Candidate batch] Y", "owner/new", frozen=True, review_ref=ref),
        ]
        self.assertTrue(module.is_exact_snapshot_duplicate(entries))

    def test_exact_snapshot_duplicate_rejects_different_refs(self) -> None:
        entries = [
            module.QueueEntry(
                918,
                "[Candidate batch] X",
                "owner/old",
                frozen=True,
                review_ref="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ),
            module.QueueEntry(
                966,
                "[Candidate batch] Y",
                "owner/new",
                frozen=True,
                review_ref="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
            ),
        ]
        self.assertFalse(module.is_exact_snapshot_duplicate(entries))

    def test_exact_snapshot_duplicate_rejects_missing_ref(self) -> None:
        entries = [
            module.QueueEntry(
                918,
                "[Candidate batch] X",
                "owner/old",
                frozen=True,
                review_ref="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ),
            module.QueueEntry(966, "[Candidate batch] Y", "owner/new", frozen=True),
        ]
        self.assertFalse(module.is_exact_snapshot_duplicate(entries))

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

    def test_title_frozen_controller_keeps_only_unprocessed_rows_active(self) -> None:
        body = """## Frozen candidate map

| # | Project | Canonical repository | Frozen review ref |
| ---: | --- | --- | --- |
| 1 | Done | `owner/done` | `1111111111111111111111111111111111111111` |
| 2 | Pending | `owner/pending` | `2222222222222222222222222222222222222222` |
"""
        api = mock.Mock()
        api.open_issues.return_value = [{
            "number": 2579,
            "title": "[Assessment batch] Done, Pending — frozen #2578",
            "body": body,
        }]
        entries, occupancy, parse_errors = module.active_queue_entries(api, "owner/index")
        active, errors, _warnings = module.classify_queue_entries(
            entries,
            included={"owner/done": "owner/done"},
            proposed={},
            catalog_names={"owner/done": "owner/done"},
        )
        self.assertEqual(parse_errors, [])
        self.assertEqual(occupancy, {})
        self.assertEqual(errors, [])
        self.assertEqual([entry.repository for entry in active], ["owner/pending"])

    def test_unfrozen_title_does_not_hide_canonical_queue_overlap(self) -> None:
        api = mock.Mock()
        api.open_issues.return_value = [{
            "number": 20,
            "title": "[Candidate batch] Active intake",
            "body": "| Project | Repository | Review ref |\n"
                    "| --- | --- | --- |\n"
                    "| Done | `owner/done` | `1111111111111111111111111111111111111111` |\n",
        }]
        entries, _occupancy, _parse_errors = module.active_queue_entries(api, "owner/index")
        active, errors, _warnings = module.classify_queue_entries(
            entries, included={"owner/done": "owner/done"}, proposed={}, catalog_names={}
        )
        self.assertEqual(len(active), 1)
        self.assertIn("#20: owner/done is already canonical status=included", errors)

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
    def test_genuine_duplicate_frozen_repo_id_fails_closed(self) -> None:
        # #2730: two distinct immutable intakes may freeze the same stable repo
        # ID/SHA. Neither is a controller of the other, so this must fail.
        frozen_sha = "fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4"
        issues = [
            {
                "number": number,
                "title": "[Candidate batch] Frozen five",
                "body": (
                    "Batch frozen at 5/5.\n"
                    "| # | Candidate | Repository | Frozen review_ref |\n"
                    "| ---: | --- | --- | --- |\n"
                    f"| 1 | NorthCUA | `{repository}` | `{frozen_sha}` |\n"
                ),
            }
            for number, repository in (
                (2708, "beipo-ai/NorthCUA"),
                (2710, "mirror/NorthCUA"),
            )
        ]
        stderr, stdout = StringIO(), StringIO()
        with (
            mock.patch.object(sys, "argv", ["check_discovery_queues.py"]),
            mock.patch.object(module, "load_assessments", return_value={"included": [], "proposed": []}),
            mock.patch.object(module, "load_catalog", return_value=[]),
            mock.patch.object(module.GitHubAPI, "open_issues", return_value=issues),
            mock.patch.object(module.GitHubAPI, "repository_identities", return_value=[
                (1443075589, "beipo-ai/NorthCUA"),
                (1443075589, "beipo-ai/NorthCUA"),
            ]),
            redirect_stderr(stderr),
            redirect_stdout(stdout),
        ):
            result = module.main()
        self.assertEqual(result, 1)
        self.assertIn("GitHub repository id 1443075589", stderr.getvalue())
        self.assertIn("active batches [2708, 2710]", stderr.getvalue())

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
