"""Executable 05S5 spin-connection holonomy checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    IDENTITY_SPINOR_HOLONOMY,
    SpinHolonomyComparison,
    SpinPhaseRecord,
    conjugate_spinor_holonomy,
    inverse_matrix2c,
    multiply_matrix2c,
    reverse_spinor_holonomy,
    proper_time_flat,
    pulse_count,
    simulate_frame_loop_holonomy,
    spin_half_holonomy_from_rotation_vector,
    spin_half_lift_from_frame_generator,
    spinor_holonomy_distance,
    spinor_holonomy_residual,
    unwrap_spin_phase_rad,
)


class SpinConnectionHolonomyTests(unittest.TestCase):
    def test_flat_identity_holonomy_has_no_residual(self) -> None:
        generator = simulate_frame_loop_holonomy(0.0, 10.0, 1, 2).generator
        spin_lift = spin_half_lift_from_frame_generator(generator)
        comparison = SpinHolonomyComparison(spin_lift, spin_lift, area_m2=2.0)

        self.assertEqual(spin_lift, IDENTITY_SPINOR_HOLONOMY)
        self.assertEqual(comparison.classification, "representation-lift-only")
        self.assertEqual(comparison.residual_norm, 0.0)
        self.assertEqual(comparison.residual_density_per_m2, 0.0)

    def test_small_loop_frame_generator_lifts_to_spin_half_phase(self) -> None:
        angle_rad = 0.25
        generator = simulate_frame_loop_holonomy(0.5, 0.5, 1, 2).generator
        spin_lift = spin_half_lift_from_frame_generator(generator)

        self.assertAlmostEqual(generator[1][2], angle_rad)
        self.assertAlmostEqual(spin_lift[0][0].real, math.cos(angle_rad / 2.0))
        self.assertAlmostEqual(spin_lift[0][0].imag, -math.sin(angle_rad / 2.0))
        self.assertAlmostEqual(spin_lift[1][1].real, math.cos(angle_rad / 2.0))
        self.assertAlmostEqual(spin_lift[1][1].imag, math.sin(angle_rad / 2.0))
        self.assertAlmostEqual(abs(spin_lift[0][0]), 1.0)

    def test_loop_reversal_inverts_spin_holonomy(self) -> None:
        holonomy = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.4))
        reversed_holonomy = spin_half_holonomy_from_rotation_vector((0.0, 0.0, -0.4))

        self.assertLess(spinor_holonomy_distance(reversed_holonomy, reverse_spinor_holonomy(holonomy)), 1.0e-15)
        self.assertLess(
            spinor_holonomy_distance(multiply_matrix2c(holonomy, reversed_holonomy), IDENTITY_SPINOR_HOLONOMY),
            1.0e-15,
        )

    def test_local_frame_relabeling_preserves_residual_norm_by_conjugation(self) -> None:
        expected = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.2))
        residual = spin_half_holonomy_from_rotation_vector((0.03, 0.0, 0.0))
        observed = multiply_matrix2c(residual, expected)
        gauge = spin_half_holonomy_from_rotation_vector((0.0, 0.2, 0.0))

        comparison = SpinHolonomyComparison(observed, expected)
        transformed_comparison = SpinHolonomyComparison(
            conjugate_spinor_holonomy(observed, gauge),
            conjugate_spinor_holonomy(expected, gauge),
        )

        self.assertEqual(comparison.classification, "source-response-missing")
        self.assertAlmostEqual(comparison.residual_norm, transformed_comparison.residual_norm)
        self.assertLess(
            spinor_holonomy_distance(
                transformed_comparison.residual_holonomy,
                conjugate_spinor_holonomy(comparison.residual_holonomy, gauge),
            ),
            1.0e-15,
        )

    def test_spin_double_cover_sign_is_modeled_as_representation_behavior(self) -> None:
        two_pi = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 2.0 * math.pi))
        four_pi = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 4.0 * math.pi))
        alternate_lift = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.0), lift_sign=-1)

        self.assertLess(spinor_holonomy_distance(two_pi, ((-1.0 + 0.0j, 0.0j), (0.0j, -1.0 + 0.0j))), 1.0e-15)
        self.assertLess(spinor_holonomy_distance(four_pi, IDENTITY_SPINOR_HOLONOMY), 1.0e-15)
        self.assertLess(spinor_holonomy_distance(alternate_lift, ((-1.0 + 0.0j, 0.0j), (0.0j, -1.0 + 0.0j))), 1.0e-15)

    def test_scalar_phase_artifact_ledgers_subtract_before_residual_classification(self) -> None:
        record = SpinPhaseRecord(
            observed_phase_rad=10.0,
            levi_civita_phase_rad=3.0,
            spin_preparation_phase_rad=1.0,
            magnetic_phase_rad=2.0,
            berry_phase_rad=1.5,
            detector_phase_rad=0.5,
            instrument_phase_rad=1.25,
            finite_loop_phase_rad=0.75,
            area_m2=4.0,
        )
        residual_record = SpinPhaseRecord(
            observed_phase_rad=10.5,
            levi_civita_phase_rad=3.0,
            spin_preparation_phase_rad=1.0,
            magnetic_phase_rad=2.0,
            berry_phase_rad=1.5,
            detector_phase_rad=0.5,
            instrument_phase_rad=1.25,
            finite_loop_phase_rad=0.75,
            orientation=-1.0,
            area_m2=2.0,
        )

        self.assertAlmostEqual(record.artifact_phase_rad, 7.0)
        self.assertEqual(record.canonical_residual_phase_rad, 0.0)
        self.assertEqual(record.classification, "representation-lift-only")
        self.assertAlmostEqual(residual_record.oriented_residual_phase_rad, -0.5)
        self.assertAlmostEqual(residual_record.residual_density_rad_per_m2, -0.25)
        self.assertEqual(residual_record.classification, "source-response-missing")

    def test_matrix_artifact_holonomy_subtracts_before_residual_classification(self) -> None:
        expected = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.2))
        artifact = spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.1))
        observed = multiply_matrix2c(multiply_matrix2c(artifact, expected), IDENTITY_SPINOR_HOLONOMY)

        residual = spinor_holonomy_residual(observed, expected, artifact)
        comparison = SpinHolonomyComparison(observed, expected, artifact, area_m2=5.0)

        self.assertLess(spinor_holonomy_distance(residual, IDENTITY_SPINOR_HOLONOMY), 1.0e-15)
        self.assertEqual(comparison.classification, "representation-lift-only")
        self.assertLess(comparison.residual_density_per_m2, 1.0e-15)

    def test_torsion_free_spin_lift_does_not_change_scalar_pulse_count(self) -> None:
        scalar_proper_time_s = proper_time_flat(coordinate_time_s=2.0, velocity_m_per_s=0.0)
        scalar_pulses = pulse_count(frequency_hz=10.0, proper_time_s=scalar_proper_time_s)
        generator = simulate_frame_loop_holonomy(curvature_per_m2=0.125, oriented_area_m2=0.5, first_axis=1, second_axis=2).generator
        spin_lift = spin_half_lift_from_frame_generator(generator)
        comparison = SpinHolonomyComparison(spin_lift, spin_lift)

        self.assertEqual(comparison.classification, "representation-lift-only")
        self.assertEqual(pulse_count(frequency_hz=10.0, proper_time_s=scalar_proper_time_s), scalar_pulses)

    def test_rejects_invalid_or_out_of_scope_records(self) -> None:
        with self.assertRaises(ValueError):
            unwrap_spin_phase_rad(math.nan)
        with self.assertRaises(ValueError):
            unwrap_spin_phase_rad(0.0, unwrap_turns=0.5)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            SpinPhaseRecord(observed_phase_rad=math.inf)
        with self.assertRaises(ValueError):
            SpinPhaseRecord(observed_phase_rad=0.0, orientation=0.0)
        with self.assertRaises(ValueError):
            SpinPhaseRecord(observed_phase_rad=0.0, area_m2=0.0)
        with self.assertRaises(ValueError):
            SpinPhaseRecord(observed_phase_rad=0.0).residual_density_rad_per_m2
        with self.assertRaises(ValueError):
            spin_half_holonomy_from_rotation_vector((0.0, math.nan, 0.0))
        with self.assertRaises(ValueError):
            spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.0), lift_sign=0)
        with self.assertRaises(ValueError):
            spin_half_lift_from_frame_generator(
                (
                    (0.0, 0.1, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                )
            )
        with self.assertRaises(ValueError):
            spin_half_lift_from_frame_generator(
                (
                    (0.0, 0.0, 0.0, 0.0),
                    (0.0, 0.0, 0.2, 0.0),
                    (0.0, 0.1, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                )
            )
        with self.assertRaises(ValueError):
            inverse_matrix2c(((0.0j, 0.0j), (0.0j, 0.0j)))
        with self.assertRaises(ValueError):
            SpinHolonomyComparison(((0.0j,), (0.0j,)))  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            SpinHolonomyComparison(IDENTITY_SPINOR_HOLONOMY).residual_density_per_m2


if __name__ == "__main__":
    unittest.main()
