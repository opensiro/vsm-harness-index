"""Model-era analytics must never masquerade as per-run assessor provenance."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import render_analytics  # noqa: E402
from validate_tldr import load_assessments  # noqa: E402


class AssessedByModelEraTests(unittest.TestCase):
    def test_cutover_date_includes_indeterminate_day(self):
        cases = {
            '2026-10-06': 'before',
            '2026-10-07': 'transition',
            '2026-10-08': 'after',
        }
        for day, expected in cases.items():
            with self.subTest(day=day):
                self.assertEqual(render_analytics.chatgpt_sol_model_era(day), expected)
        with self.assertRaises(ValueError):
            render_analytics.chatgpt_sol_model_era('invalid-date')

    def test_current_snapshot_totals_and_rollout_are_independently_reconciled(self):
        assessments = load_assessments(ROOT / 'assessments')
        counts = render_analytics.model_era_counts(assessments)
        included = sum(counts[k]['included'] for k in render_analytics.MODEL_ERA_KEYS)
        excluded = sum(counts[k]['excluded-no-agentic-vsm'] for k in render_analytics.MODEL_ERA_KEYS)
        proposed = sum(counts[k]['proposed'] for k in render_analytics.MODEL_ERA_KEYS)
        self.assertEqual(included + excluded + proposed, len(assessments))
        self.assertEqual(included, sum(a['status'] == 'included' for a in assessments.values()))
        self.assertEqual(excluded, sum(a['status'] == 'excluded-no-agentic-vsm' for a in assessments.values()))
        self.assertEqual(proposed, sum(a['status'] == 'proposed' for a in assessments.values()))
        self.assertEqual(
            counts['transition']['included'],
            sum(a['status'] == 'included' and a['reviewed_at'] == '2026-10-07' for a in assessments.values()),
        )

    def test_model_era_view_does_not_claim_verified_per_run_identity(self):
        rendered = render_analytics.render_assessed_by_model({})
        self.assertIn('date-inferred', rendered)
        self.assertIn('not verified execution provenance', rendered)
        self.assertIn('GPT-5.6 Sol / GPT-6 Sol (rollout; model uncertain)', rendered)
        self.assertIn('not evidence that both models worked on the same assessment', rendered)
        self.assertIn('not the ordinary Chat tab', rendered)
        self.assertIn('claim that assessments were executed by', rendered)
        self.assertIn('**0**', rendered)

    def test_rendered_output_is_deterministic_and_registered(self):
        path = ROOT / 'analytics' / 'assessed-by-model.md'
        rendered = render_analytics.render_all(ROOT)
        self.assertIn(path, rendered)
        self.assertEqual(rendered[path], path.read_text(encoding='utf-8'))
        self.assertEqual(rendered, render_analytics.render_all(ROOT))


if __name__ == '__main__':
    unittest.main()
