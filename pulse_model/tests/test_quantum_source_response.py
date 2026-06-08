"""Executable H6S1 quantum source-response discriminator checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    REDUCED_PLANCK_CONSTANT_J_S,
    PulseDistributionPoint,
    TwoBranchWeakFieldSetup,
    branch_mixture_distribution,
    branch_probe_response,
    branch_visibility,
    classify_conservation_status,
    expectation_sourced_distribution,
    invalid_remote_basis_toy_distribution,
    no_signaling_guardrail,
    pulse_marginal_max_difference,
    softened_newtonian_potential,
    source_response_discriminator,
    two_level_branch_visibility,
)


class QuantumSourceResponseTests(unittest.TestCase):
    def _setup(self, *, probability_a: float = 0.25) -> TwoBranchWeakFieldSetup:
        return TwoBranchWeakFieldSetup(
            probability_a=probability_a,
            source_position_a_m=2.0,
            source_position_b_m=-4.0,
            probe_position_m=0.0,
            coordinate_duration_s=10.0,
            clock_frequency_hz=5.0,
            source_mass_kg=2.0,
            gravitational_constant_m3_per_kg_s2=1.0,
            speed_of_light_m_per_s=10.0,
        )

    def test_valid_two_branch_input_constructs_branch_records(self) -> None:
        setup = self._setup()

        self.assertAlmostEqual(setup.probability_b, 0.75)
        self.assertEqual(setup.branch_label_a, "a")
        self.assertEqual(setup.branch_label_b, "b")

        branch_a = branch_probe_response(setup, "a")
        branch_b = branch_probe_response(setup, "b")

        self.assertAlmostEqual(branch_a.potential_m2_per_s2, -1.0)
        self.assertAlmostEqual(branch_b.potential_m2_per_s2, -0.5)
        self.assertLess(branch_a.pulse_count, branch_b.pulse_count)

    def test_softened_newtonian_potential_regularizes_coincident_probe(self) -> None:
        self.assertAlmostEqual(
            softened_newtonian_potential(
                source_mass_kg=2.0,
                source_position_m=3.0,
                probe_position_m=0.0,
                gravitational_constant_m3_per_kg_s2=1.0,
            ),
            -2.0 / 3.0,
        )
        self.assertAlmostEqual(
            softened_newtonian_potential(
                source_mass_kg=2.0,
                source_position_m=0.0,
                probe_position_m=0.0,
                softening_radius_m=4.0,
                gravitational_constant_m3_per_kg_s2=1.0,
            ),
            -0.5,
        )
        with self.assertRaises(ValueError):
            softened_newtonian_potential(2.0, 0.0, 0.0, gravitational_constant_m3_per_kg_s2=1.0)

    def test_expectation_sourced_mean_matches_branch_mixture_mean(self) -> None:
        summary = source_response_discriminator(self._setup())

        self.assertAlmostEqual(summary.expectation_potential_m2_per_s2, -0.625)
        self.assertAlmostEqual(summary.expectation_proper_time_s, 9.9375)
        self.assertAlmostEqual(summary.expectation_pulse_count, 49.6875)
        self.assertAlmostEqual(summary.branch_mixture_mean_pulse_count, 49.6875)
        self.assertAlmostEqual(
            summary.branch_mixture_mean_pulse_count,
            summary.expectation_pulse_count,
        )

    def test_branch_mixture_has_same_mean_but_different_variance(self) -> None:
        summary = source_response_discriminator(self._setup())
        expectation_distribution = expectation_sourced_distribution(self._setup())
        branch_distribution = branch_mixture_distribution(self._setup())

        self.assertAlmostEqual(expectation_distribution[0].pulse_count, summary.branch_mixture_mean_pulse_count)
        self.assertAlmostEqual(summary.branch_mixture_variance_pulses2, 0.25 * 0.75 * 0.25**2)
        self.assertGreater(summary.branch_mixture_variance_pulses2, 0.0)
        self.assertEqual(len(branch_distribution), 2)
        self.assertNotEqual(branch_distribution[0].pulse_count, branch_distribution[1].pulse_count)

    def test_branch_conditioned_shifts_are_explicit(self) -> None:
        summary = source_response_discriminator(self._setup(probability_a=0.5))

        self.assertAlmostEqual(summary.branch_a.pulse_count, 49.5)
        self.assertAlmostEqual(summary.branch_b.pulse_count, 49.75)
        self.assertAlmostEqual(summary.branch_separation_pulses, -0.25)
        self.assertEqual(summary.branch_separation_score, math.inf)

    def test_source_probe_correlation_is_branch_perfect_without_added_noise(self) -> None:
        summary = source_response_discriminator(self._setup(probability_a=0.3))

        self.assertAlmostEqual(abs(summary.source_probe_correlation), 1.0)
        self.assertLess(summary.source_probe_correlation, 0.0)
        self.assertAlmostEqual(summary.source_probe_covariance_pulses, 0.3 * 0.7 * -0.25)

    def test_instrumental_noise_adds_to_variance_and_reduces_correlation(self) -> None:
        noiseless = source_response_discriminator(self._setup(probability_a=0.5))
        noisy = source_response_discriminator(
            self._setup(probability_a=0.5),
            instrumental_noise_stddev_pulses=3.0,
        )

        self.assertAlmostEqual(
            noisy.observed_variance_pulses2,
            noiseless.branch_mixture_variance_pulses2 + 9.0,
        )
        self.assertAlmostEqual(noisy.instrumental_noise_variance_pulses2, 9.0)
        self.assertAlmostEqual(noisy.branch_separation_score, 0.25 / 3.0)
        self.assertLess(abs(noisy.source_probe_correlation), abs(noiseless.source_probe_correlation))

    def test_branch_visibility_uses_only_probe_proper_time_difference(self) -> None:
        setup = TwoBranchWeakFieldSetup(
            probability_a=0.5,
            source_position_a_m=1.0,
            source_position_b_m=2.0,
            probe_position_m=0.0,
            coordinate_duration_s=100.0,
            clock_frequency_hz=1.0,
            source_mass_kg=1.0,
            gravitational_constant_m3_per_kg_s2=1.0,
            speed_of_light_m_per_s=10.0,
        )
        energy_gap_j = 2.0 * math.pi * REDUCED_PLANCK_CONSTANT_J_S

        self.assertAlmostEqual(two_level_branch_visibility(setup, 1.0), 0.0, places=15)
        self.assertAlmostEqual(
            branch_visibility(setup, [0.0, energy_gap_j], [0.5, 0.5]),
            0.0,
            places=15,
        )

    def test_no_signaling_guardrail_rejects_invalid_remote_basis_toy_rule(self) -> None:
        setup = self._setup(probability_a=0.8)
        z_distribution = invalid_remote_basis_toy_distribution(setup, "Z")
        x_distribution = invalid_remote_basis_toy_distribution(setup, "X")

        rejected = no_signaling_guardrail(
            "invalid-remote-basis-toy",
            z_distribution,
            x_distribution,
        )
        passed = no_signaling_guardrail(
            "branch-mixture-bookkeeping",
            branch_mixture_distribution(setup),
            branch_mixture_distribution(setup),
        )

        self.assertEqual(rejected.classification, "rejected-remote-basis-signaling")
        self.assertTrue(rejected.rejected)
        self.assertAlmostEqual(rejected.max_marginal_difference, 0.3)
        self.assertEqual(passed.classification, "no-signaling-passed")
        self.assertFalse(passed.rejected)

    def test_marginal_difference_rejects_changed_support_without_causal_channel(self) -> None:
        first = (PulseDistributionPoint(1.0, 1.0),)
        second = (PulseDistributionPoint(2.0, 1.0),)
        guardrail = no_signaling_guardrail("support-changing-rule", first, second)

        self.assertEqual(pulse_marginal_max_difference(first, second), math.inf)
        self.assertEqual(guardrail.classification, "rejected-remote-basis-signaling")

    def test_conservation_classifier_keeps_model_families_separate(self) -> None:
        self.assertEqual(
            classify_conservation_status("expectation-sourced"),
            "expectation-conserved",
        )
        self.assertEqual(
            classify_conservation_status("branch-specific"),
            "branchwise-conserved",
        )
        self.assertEqual(
            classify_conservation_status("collapse-selection"),
            "conservation-requires-environment",
        )
        self.assertEqual(
            classify_conservation_status("pulse-native"),
            "not-yet-classified",
        )
        self.assertEqual(
            classify_conservation_status("invalid-toy"),
            "inconsistent-rejected",
        )

    def test_invalid_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self._setup(probability_a=-0.1)
        with self.assertRaises(ValueError):
            self._setup(probability_a=1.1)
        with self.assertRaises(ValueError):
            TwoBranchWeakFieldSetup(
                probability_a=0.5,
                source_position_a_m=math.nan,
                source_position_b_m=2.0,
                probe_position_m=0.0,
                coordinate_duration_s=1.0,
                clock_frequency_hz=1.0,
                source_mass_kg=1.0,
            )
        with self.assertRaises(ValueError):
            TwoBranchWeakFieldSetup(
                probability_a=0.5,
                source_position_a_m=0.0,
                source_position_b_m=2.0,
                probe_position_m=0.0,
                coordinate_duration_s=1.0,
                clock_frequency_hz=1.0,
                source_mass_kg=1.0,
            )
        with self.assertRaises(ValueError):
            TwoBranchWeakFieldSetup(
                probability_a=0.5,
                source_position_a_m=1.0,
                source_position_b_m=2.0,
                probe_position_m=0.0,
                coordinate_duration_s=1.0,
                clock_frequency_hz=1.0,
                source_mass_kg=-1.0,
            )
        with self.assertRaises(ValueError):
            TwoBranchWeakFieldSetup(
                probability_a=0.5,
                source_position_a_m=1.0,
                source_position_b_m=2.0,
                probe_position_m=0.0,
                coordinate_duration_s=1.0,
                clock_frequency_hz=1.0,
                source_mass_kg=1.0,
                branch_label_a="a",
                branch_label_b="a",
            )
        with self.assertRaises(ValueError):
            source_response_discriminator(self._setup(), instrumental_noise_stddev_pulses=-1.0)
        with self.assertRaises(ValueError):
            invalid_remote_basis_toy_distribution(self._setup(), "Y")
        with self.assertRaises(ValueError):
            classify_conservation_status("unknown")


if __name__ == "__main__":
    unittest.main()
