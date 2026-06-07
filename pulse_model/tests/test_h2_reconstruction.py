"""Executable first-slice H2 metric reconstruction checks.

The prototype uses the reference clock as the time-scale gauge. It verifies
static-clock rate equality for Minkowski records and weak-static potential
differences from clock ratios, directional timing asymmetry, calibrated
Shapiro-delay gamma recovery, and calibrated weak-wave arm timing recovery. It
does not claim arbitrary sparse records determine a general metric.
"""

from __future__ import annotations

import unittest

from pulse_model import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    SPEED_OF_LIGHT_M_PER_S,
    clock_rate_ratios,
    pulse_segment_duration,
    recover_directional_time_asymmetry,
    recover_gravitational_wave_h_plus,
    recover_shapiro_gamma,
    reconstruct_flat_metric,
    reconstruct_weak_static_potential_differences,
    synthesize_directional_timing_record,
    synthesize_gravitational_wave_arm_record,
    synthesize_minkowski_pulse_signal_record,
    synthesize_shapiro_delay_record,
    synthesize_weak_static_pulse_signal_record,
)

STANDARD_GRAVITY_M_PER_S2 = 9.806_65


class H2ReconstructionTests(unittest.TestCase):
    def test_minkowski_record_reconstructs_flat_static_clock_slice(self) -> None:
        record = synthesize_minkowski_pulse_signal_record(
            ("reference", "probe_a", "probe_b"),
            coordinate_duration_s=10.0,
            frequency_hz=10_000_000.0,
        )

        reconstruction = reconstruct_flat_metric(record, "reference", tolerance_fraction=1e-15)

        self.assertTrue(reconstruction.is_flat_within_tolerance)
        self.assertEqual(
            reconstruction.metric_label,
            "eta_mu_nu up to Poincare and coordinate gauge",
        )
        self.assertEqual(len(record.signal_links), 4)
        self.assertEqual(reconstruction.max_fractional_rate_deviation, 0.0)
        self.assertTrue(all(ratio.duration_ratio == 1.0 for ratio in reconstruction.rate_ratios))

    def test_minkowski_rate_ratios_are_independent_of_duration_gauge(self) -> None:
        short_record = synthesize_minkowski_pulse_signal_record(
            ("reference", "probe"),
            coordinate_duration_s=1.0,
            frequency_hz=1_000.0,
        )
        long_record = synthesize_minkowski_pulse_signal_record(
            ("reference", "probe"),
            coordinate_duration_s=37.0,
            frequency_hz=1_000.0,
        )

        short_ratios = clock_rate_ratios(short_record, "reference")
        long_ratios = clock_rate_ratios(long_record, "reference")

        self.assertEqual(
            [ratio.duration_ratio for ratio in short_ratios],
            [ratio.duration_ratio for ratio in long_ratios],
        )

    def test_weak_static_record_recovers_potential_differences_from_clock_ratios(self) -> None:
        lower_potential = -6.25e7
        upper_potential = 2.5e7
        record = synthesize_weak_static_pulse_signal_record(
            {
                "reference": 0.0,
                "lower": lower_potential,
                "upper": upper_potential,
            },
            coordinate_duration_s=1_000.0,
            frequency_hz=9_192_631_770.0,
        )

        estimates = {
            estimate.clock_id: estimate
            for estimate in reconstruct_weak_static_potential_differences(record, "reference")
        }

        self.assertAlmostEqual(
            estimates["lower"].potential_difference_m2_per_s2,
            lower_potential,
            delta=abs(lower_potential) * 1e-6,
        )
        self.assertAlmostEqual(
            estimates["upper"].potential_difference_m2_per_s2,
            upper_potential,
            delta=abs(upper_potential) * 1e-6,
        )
        self.assertEqual(estimates["reference"].potential_difference_m2_per_s2, 0.0)

    def test_weak_static_uncertainty_is_reported_from_pulse_count_noise(self) -> None:
        record = synthesize_weak_static_pulse_signal_record(
            {
                "reference": 0.0,
                "probe": -STANDARD_GRAVITY_M_PER_S2,
            },
            coordinate_duration_s=10.0,
            frequency_hz=10_000.0,
            pulse_count_uncertainty=0.25,
        )

        estimates = reconstruct_weak_static_potential_differences(record, "reference")
        ratios = clock_rate_ratios(record, "reference")
        probe_estimate = next(estimate for estimate in estimates if estimate.clock_id == "probe")
        reference_estimate = next(
            estimate for estimate in estimates if estimate.clock_id == "reference"
        )
        reference_ratio = next(ratio for ratio in ratios if ratio.clock_id == "reference")
        reference_segment = pulse_segment_duration(record, "reference:segment")

        self.assertGreater(probe_estimate.uncertainty_m2_per_s2, 0.0)
        self.assertEqual(reference_ratio.uncertainty, 0.0)
        self.assertEqual(reference_estimate.uncertainty_m2_per_s2, 0.0)
        self.assertGreater(reference_segment.uncertainty_s, 0.0)
        self.assertAlmostEqual(
            probe_estimate.potential_difference_m2_per_s2,
            -STANDARD_GRAVITY_M_PER_S2,
            delta=probe_estimate.uncertainty_m2_per_s2,
        )

    def test_validation_rejects_empty_or_unphysical_synthetic_inputs(self) -> None:
        with self.assertRaises(ValueError):
            synthesize_minkowski_pulse_signal_record((), 1.0, 1.0)
        with self.assertRaises(ValueError):
            synthesize_minkowski_pulse_signal_record(("clock",), 0.0, 1.0)
        with self.assertRaises(ValueError):
            synthesize_minkowski_pulse_signal_record(("clock",), 1.0, -1.0)
        with self.assertRaises(ValueError):
            synthesize_weak_static_pulse_signal_record(
                {"clock": -2.0 * SPEED_OF_LIGHT_M_PER_S**2},
                1.0,
                1.0,
            )

    def test_direction_dependent_timing_recovers_stationary_asymmetry(self) -> None:
        record = synthesize_directional_timing_record(
            loop_id="loop",
            base_light_time_s=2.0e-6,
            time_asymmetry_s=3.5e-9,
            duration_uncertainty_s=2.0e-12,
        )

        estimate = recover_directional_time_asymmetry(record)

        self.assertAlmostEqual(estimate.time_asymmetry_s, 3.5e-9, delta=1e-21)
        self.assertGreater(estimate.uncertainty_s, 0.0)
        self.assertGreater(record.clockwise_duration_s, record.counterclockwise_duration_s)

    def test_shapiro_delay_record_recovers_injected_spatial_gamma(self) -> None:
        solar_mass_kg = 1.988_47e30
        astronomical_unit_m = 149_597_870_700.0
        record = synthesize_shapiro_delay_record(
            signal_id="solar-grazing-link",
            central_mass_kg=solar_mass_kg,
            emitter_radius_m=astronomical_unit_m,
            receiver_radius_m=1.4 * astronomical_unit_m,
            coordinate_separation_m=2.2 * astronomical_unit_m,
            gamma=1.0,
            duration_uncertainty_s=1e-10,
        )

        estimate = recover_shapiro_gamma(record)

        self.assertGreater(estimate.delay_s, 0.0)
        self.assertAlmostEqual(estimate.gamma, 1.0, delta=1e-8)
        self.assertGreater(estimate.gamma_uncertainty, 0.0)

    def test_gravitational_wave_arm_record_recovers_injected_h_plus_mode(self) -> None:
        record = synthesize_gravitational_wave_arm_record(
            record_id="gw-plus",
            arm_length_m=4_000.0,
            h_plus=2.0e-12,
            duration_uncertainty_s=1e-20,
        )

        estimate = recover_gravitational_wave_h_plus(record)

        self.assertAlmostEqual(estimate.h_plus, 2.0e-12, delta=1e-15)
        self.assertGreater(estimate.uncertainty, 0.0)
        self.assertGreater(record.x_arm_duration_s, record.y_arm_duration_s)

    def test_extended_record_validation_rejects_invalid_domains(self) -> None:
        solar_mass_kg = 1.988_47e30

        with self.assertRaises(ValueError):
            synthesize_directional_timing_record("loop", 1.0, 2.0)
        with self.assertRaises(ValueError):
            synthesize_shapiro_delay_record(
                "bad",
                solar_mass_kg,
                emitter_radius_m=10.0,
                receiver_radius_m=10.0,
                coordinate_separation_m=20.0,
            )
        with self.assertRaises(ValueError):
            synthesize_gravitational_wave_arm_record("bad", 0.0, 1e-21)

    def test_shapiro_delay_matches_standard_formula_scale(self) -> None:
        solar_mass_kg = 1.988_47e30
        astronomical_unit_m = 149_597_870_700.0
        record = synthesize_shapiro_delay_record(
            signal_id="scale",
            central_mass_kg=solar_mass_kg,
            emitter_radius_m=astronomical_unit_m,
            receiver_radius_m=astronomical_unit_m,
            coordinate_separation_m=1.5 * astronomical_unit_m,
            gamma=1.0,
        )
        estimate = recover_shapiro_gamma(record)

        characteristic_time_s = (
            GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
            * solar_mass_kg
            / SPEED_OF_LIGHT_M_PER_S**3
        )

        self.assertGreater(estimate.delay_s, characteristic_time_s)


if __name__ == "__main__":
    unittest.main()
