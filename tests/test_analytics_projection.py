from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import render_analytics  # noqa: E402


class AnalyticsProjectionTests(unittest.TestCase):
    def setUp(self):
        self.vectors = [
            ["A", "A", "C", "—", "A(P)", "?"],
            ["A", "—", "A(P)", "A", "C(P)", "P"],
            ["A", "C", "—", "C(P)", "—", "—"],
        ]

    def test_detailed_counts_reconcile_to_denominator(self):
        counts = render_analytics.state_counts(self.vectors)
        self.assertEqual(len(counts), 6)
        for function_counts in counts:
            self.assertEqual(sum(function_counts.values()), len(self.vectors))

    def test_autonomous_coverage_uses_existing_base_state_semantics(self):
        self.assertEqual(render_analytics.autonomous_coverage(self.vectors[0]), 3)
        self.assertEqual(render_analytics.autonomous_coverage(self.vectors[1]), 3)
        self.assertEqual(render_analytics.autonomous_coverage(self.vectors[2]), 1)
        distribution = render_analytics.coverage_distribution(self.vectors)
        self.assertEqual(distribution[3], 2)
        self.assertEqual(distribution[1], 1)

    def test_cooccurrence_is_symmetric_and_diagonal_reconciles(self):
        predicate = lambda state: state in render_analytics.MATERIAL_STATES
        matrix = render_analytics.cooccurrence_matrix(self.vectors, predicate)
        for left in range(6):
            self.assertEqual(
                matrix[left][left],
                sum(predicate(states[left]) for states in self.vectors),
            )
            for right in range(6):
                self.assertEqual(matrix[left][right], matrix[right][left])

    def test_changed_functions_parser_keeps_s3_star_distinct(self):
        parsed = render_analytics.changed_functions(
            {"changed_functions": "S2, S3*; S5"}
        )
        self.assertEqual(parsed, {"S2", "S3*", "S5"})
        self.assertEqual(render_analytics.changed_functions({"changed_functions": "—"}), set())

    def test_current_repository_aggregates_reconcile(self):
        vectors = [states for _, states in render_analytics.load_included(ROOT)]
        render_analytics.validate_aggregates(vectors)
        rendered_once = render_analytics.render_all(ROOT)
        rendered_twice = render_analytics.render_all(ROOT)
        self.assertEqual(rendered_once, rendered_twice)


if __name__ == "__main__":
    unittest.main()
