"""Executable 05S3 correction-phenomenology checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    SPEED_OF_LIGHT_M_PER_S,
    constant_curvature_sectional_curvatures,
    estimate_pulse_record_curvature,
    finite_loop_parameter,
    gravitational_redshift,
    preferred_projection_parameter,
    project_relative_correction_to_benchmark,
    require_supported_correction_channel,
    spatial_only_plane_weights,
    synthesize_loop_records_from_sectional_curvatures,
)

STANDARD_GRAVITY_M_PER_S2 = 9.806_65


class CorrectionPhenomenologyTests(unittest.TestCase):
    def test_preferred_projection_parameter_keeps_signed_normalization(self) -> None:
        estimate = estimate_pulse_record_curvature(
            synthesize_loop_records_from_sectional_curvatures(
                constant_curvature_sectional_curvatures(0.25),
                area_m2=1.0,
            ),
            plane_weights=spatial_only_plane_weights(),
        )

        parameter = preferred_projection_parameter(estimate)

        self.assertEqual(parameter.unit, "dimensionless")
        self.assertEqual(parameter.residual_unit, "m^-2")
        self.assertAlmostEqual(parameter.scalarization_residual_per_m2, -1.5)
        self.assertAlmostEqual(parameter.reference_scalar_curvature_per_m2, 3.0)
        self.assertAlmostEqual(parameter.signed_lambda, -0.5)
        self.assertAlmostEqual(parameter.relative_size, 0.5)
        self.assertEqual(parameter.sign, -1)
        self.assertEqual(parameter.classification, "preferred-projection-diagnostic")

    def test_finite_loop_parameter_propagates_scale_bound(self) -> None:
        finite_loop_bias = 6.0
        reference_scalar = 3.0
        relative_bound = 0.01
        expected_max_scale = math.sqrt(0.03 / 6.0)

        passing = finite_loop_parameter(
            finite_loop_bias,
            0.5 * expected_max_scale,
            reference_scalar,
            relative_bound,
        )
        failing = finite_loop_parameter(
            finite_loop_bias,
            2.0 * expected_max_scale,
            reference_scalar,
            relative_bound,
        )

        self.assertEqual(passing.bias_unit, "m^-4")
        self.assertEqual(passing.loop_scale_unit, "m")
        self.assertEqual(passing.scalar_correction_unit, "m^-2")
        self.assertAlmostEqual(passing.max_loop_scale_m, expected_max_scale)
        self.assertAlmostEqual(passing.scalar_correction_per_m2, finite_loop_bias * passing.loop_scale_m**2)
        self.assertLess(passing.relative_size, relative_bound)
        self.assertTrue(passing.within_bound)
        self.assertEqual(passing.sign, 1)
        self.assertEqual(passing.classification, "finite-loop-bounded")
        self.assertGreater(failing.relative_size, relative_bound)
        self.assertFalse(failing.within_bound)
        self.assertEqual(failing.classification, "finite-loop-exceeds-bound")

    def test_zero_finite_loop_bias_has_infinite_scale_bound_and_zero_sign(self) -> None:
        parameter = finite_loop_parameter(
            finite_loop_bias_per_m4=0.0,
            loop_scale_m=1.0,
            reference_scalar_curvature_per_m2=3.0,
            relative_bound=0.01,
        )

        self.assertEqual(parameter.scalar_correction_per_m2, 0.0)
        self.assertEqual(parameter.relative_size, 0.0)
        self.assertEqual(parameter.max_loop_scale_m, math.inf)
        self.assertTrue(parameter.within_bound)
        self.assertEqual(parameter.sign, 0)
        self.assertEqual(parameter.classification, "unbiased")

    def test_bounds_are_injected_without_tuning_measured_coefficient(self) -> None:
        strict = finite_loop_parameter(
            finite_loop_bias_per_m4=6.0,
            loop_scale_m=0.05,
            reference_scalar_curvature_per_m2=3.0,
            relative_bound=0.001,
        )
        loose = finite_loop_parameter(
            finite_loop_bias_per_m4=6.0,
            loop_scale_m=0.05,
            reference_scalar_curvature_per_m2=3.0,
            relative_bound=0.01,
        )

        self.assertEqual(strict.finite_loop_bias_per_m4, loose.finite_loop_bias_per_m4)
        self.assertEqual(strict.scalar_correction_per_m2, loose.scalar_correction_per_m2)
        self.assertLess(strict.max_loop_scale_m, loose.max_loop_scale_m)
        self.assertFalse(strict.within_bound)
        self.assertTrue(loose.within_bound)

    def test_unsupported_channels_are_rejected(self) -> None:
        self.assertEqual(
            require_supported_correction_channel("preferred-projection-scalarization"),
            "preferred-projection-scalarization",
        )
        self.assertEqual(
            require_supported_correction_channel("finite-loop-higher-curvature"),
            "finite-loop-higher-curvature",
        )
        for channel in ("squared-loss-promotion", "torsion", "nonlocal-kernel", "h7-vacuum-energy"):
            with self.assertRaises(ValueError):
                require_supported_correction_channel(channel)
        with self.assertRaises(ValueError):
            require_supported_correction_channel("made-up-channel")

    def test_dimension_and_sign_sanity_rejects_bad_numeric_inputs(self) -> None:
        with self.assertRaises(ValueError):
            finite_loop_parameter(
                finite_loop_bias_per_m4=math.nan,
                loop_scale_m=1.0,
                reference_scalar_curvature_per_m2=3.0,
                relative_bound=0.01,
            )
        with self.assertRaises(ValueError):
            finite_loop_parameter(
                finite_loop_bias_per_m4=6.0,
                loop_scale_m=0.0,
                reference_scalar_curvature_per_m2=3.0,
                relative_bound=0.01,
            )
        with self.assertRaises(ValueError):
            finite_loop_parameter(
                finite_loop_bias_per_m4=6.0,
                loop_scale_m=1.0,
                reference_scalar_curvature_per_m2=math.inf,
                relative_bound=0.01,
            )
        with self.assertRaises(ValueError):
            finite_loop_parameter(
                finite_loop_bias_per_m4=6.0,
                loop_scale_m=1.0,
                reference_scalar_curvature_per_m2=3.0,
                relative_bound=-0.01,
            )
        with self.assertRaises(ValueError):
            project_relative_correction_to_benchmark(math.inf, 1.0)

    def test_known_physics_redshift_projection_is_dimensionless_bookkeeping(self) -> None:
        redshift = gravitational_redshift(
            emitter_potential_m2_per_s2=0.0,
            receiver_potential_m2_per_s2=STANDARD_GRAVITY_M_PER_S2,
            speed_of_light_m_per_s=SPEED_OF_LIGHT_M_PER_S,
        )

        projected = project_relative_correction_to_benchmark(-0.5, redshift)

        self.assertLess(redshift, 0.0)
        self.assertGreater(projected, 0.0)
        self.assertAlmostEqual(projected, -0.5 * redshift)
        self.assertAlmostEqual(projected, 0.5 * STANDARD_GRAVITY_M_PER_S2 / SPEED_OF_LIGHT_M_PER_S**2)


if __name__ == "__main__":
    unittest.main()
