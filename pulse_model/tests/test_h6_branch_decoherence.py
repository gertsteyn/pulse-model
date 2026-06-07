import math
import unittest

from pulse_model import (
    branch_distinguishability,
    combined_branch_overlap,
    effective_branch_dominates,
    gaussian_branch_record_overlap,
    two_branch_coherence_magnitude,
    two_branch_decohered,
)


class H6BranchDecoherenceTests(unittest.TestCase):
    def test_combined_overlap_keeps_decoherence_factors_separate(self) -> None:
        overlap = combined_branch_overlap(
            clock_overlap=0.8,
            environmental_overlap=0.5,
            metric_history_overlap=0.25,
            technical_overlap=0.9,
        )

        self.assertAlmostEqual(overlap, 0.8 * 0.5 * 0.25 * 0.9)
        self.assertAlmostEqual(
            branch_distinguishability(
                clock_overlap=0.8,
                environmental_overlap=0.5,
                metric_history_overlap=0.25,
                technical_overlap=0.9,
            ),
            1.0 - overlap,
        )

    def test_ordinary_environmental_and_metric_history_factors_are_not_conflated(self) -> None:
        ordinary_environment_only = combined_branch_overlap(
            clock_overlap=1.0,
            environmental_overlap=0.2,
            metric_history_overlap=1.0,
        )
        metric_history_only = combined_branch_overlap(
            clock_overlap=1.0,
            environmental_overlap=1.0,
            metric_history_overlap=0.2,
        )
        both_channels = combined_branch_overlap(
            clock_overlap=1.0,
            environmental_overlap=0.2,
            metric_history_overlap=0.2,
        )

        self.assertAlmostEqual(ordinary_environment_only, 0.2)
        self.assertAlmostEqual(metric_history_only, 0.2)
        self.assertAlmostEqual(both_channels, 0.04)
        self.assertAlmostEqual(branch_distinguishability(1.0, 0.2, 1.0), 0.8)
        self.assertAlmostEqual(branch_distinguishability(1.0, 1.0, 0.2), 0.8)
        self.assertAlmostEqual(branch_distinguishability(1.0, 0.2, 0.2), 0.96)

    def test_gaussian_branch_record_overlap_is_symmetric_and_decays(self) -> None:
        self.assertEqual(gaussian_branch_record_overlap(0.0), 1.0)
        self.assertAlmostEqual(
            gaussian_branch_record_overlap(2.0, coherence_width=2.0),
            math.exp(-0.5),
        )
        self.assertEqual(
            gaussian_branch_record_overlap(-2.0, coherence_width=2.0),
            gaussian_branch_record_overlap(2.0, coherence_width=2.0),
        )
        self.assertGreater(
            gaussian_branch_record_overlap(1.0),
            gaussian_branch_record_overlap(2.0),
        )

    def test_two_branch_coherence_matches_reduced_density_matrix_off_diagonal(self) -> None:
        self.assertAlmostEqual(two_branch_coherence_magnitude(0.5, 1.0), 0.5)
        self.assertAlmostEqual(two_branch_coherence_magnitude(0.5, 0.02), 0.01)
        self.assertAlmostEqual(
            two_branch_coherence_magnitude(0.9, 0.1),
            math.sqrt(0.9 * 0.1) * 0.1,
        )

    def test_decoherence_threshold_and_dominance_are_distinct(self) -> None:
        self.assertFalse(two_branch_decohered(0.5, 0.1, coherence_threshold=0.01))
        self.assertTrue(two_branch_decohered(0.5, 0.01, coherence_threshold=0.01))

        self.assertTrue(
            effective_branch_dominates(
                branch_probability=0.95,
                total_branch_overlap=0.01,
                probability_threshold=0.9,
                coherence_threshold=0.01,
            )
        )
        self.assertFalse(
            effective_branch_dominates(
                branch_probability=0.5,
                total_branch_overlap=0.01,
                probability_threshold=0.9,
                coherence_threshold=0.01,
            )
        )
        self.assertFalse(
            effective_branch_dominates(
                branch_probability=0.95,
                total_branch_overlap=1.0,
                probability_threshold=0.9,
                coherence_threshold=0.01,
            )
        )

    def test_branch_decoherence_helpers_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            combined_branch_overlap(clock_overlap=-0.1)
        with self.assertRaises(ValueError):
            combined_branch_overlap(clock_overlap=1.1)
        with self.assertRaises(ValueError):
            combined_branch_overlap(clock_overlap=1.0, metric_history_overlap=1.1)
        with self.assertRaises(ValueError):
            gaussian_branch_record_overlap(1.0, coherence_width=0.0)
        with self.assertRaises(ValueError):
            two_branch_coherence_magnitude(-0.1, 1.0)
        with self.assertRaises(ValueError):
            two_branch_coherence_magnitude(0.5, 1.1)
        with self.assertRaises(ValueError):
            two_branch_decohered(0.5, 0.1, coherence_threshold=-0.01)
        with self.assertRaises(ValueError):
            effective_branch_dominates(0.5, 0.1, probability_threshold=1.1)


if __name__ == "__main__":
    unittest.main()
