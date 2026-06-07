"""Executable H3 loop-holonomy and tidal-residual simulations."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    corrected_loop_residual_s,
    max_abs_matrix_entry,
    schwarzschild_tidal_eigenvalues_per_s2,
    schwarzschild_tidal_ranging_residual_m,
    simulate_frame_loop_holonomy,
)

SUN_MASS_KG = 1.988_47e30


class H3HolonomyTests(unittest.TestCase):
    def test_corrected_flat_loop_residual_removes_modeled_artifacts(self) -> None:
        raw_residual_s = 4.0e-12
        modeled_artifacts_s = [1.5e-12, 2.5e-12]

        self.assertEqual(corrected_loop_residual_s(raw_residual_s, modeled_artifacts_s), 0.0)

    def test_flat_frame_loop_has_zero_generator(self) -> None:
        simulation = simulate_frame_loop_holonomy(
            curvature_per_m2=0.0,
            oriented_area_m2=250.0,
            first_axis=1,
            second_axis=2,
        )

        self.assertEqual(max_abs_matrix_entry(simulation.generator), 0.0)
        self.assertEqual(simulation.scalar_projection_s, 0.0)

    def test_curved_frame_loop_scales_with_curvature_area_and_orientation(self) -> None:
        curvature_per_m2 = 2.0e-18
        oriented_area_m2 = 5.0e6
        scalar_sensitivity_s = 3.0e-3

        simulation = simulate_frame_loop_holonomy(
            curvature_per_m2,
            oriented_area_m2,
            first_axis=1,
            second_axis=2,
            scalar_sensitivity_s=scalar_sensitivity_s,
        )
        reversed_simulation = simulate_frame_loop_holonomy(
            curvature_per_m2,
            -oriented_area_m2,
            first_axis=1,
            second_axis=2,
            scalar_sensitivity_s=scalar_sensitivity_s,
        )

        expected_generator = curvature_per_m2 * oriented_area_m2
        self.assertAlmostEqual(simulation.generator[1][2], expected_generator)
        self.assertAlmostEqual(simulation.generator[2][1], -expected_generator)
        self.assertAlmostEqual(simulation.scalar_projection_s, scalar_sensitivity_s * expected_generator)
        self.assertAlmostEqual(reversed_simulation.generator[1][2], -simulation.generator[1][2])
        self.assertAlmostEqual(
            simulate_frame_loop_holonomy(curvature_per_m2, 2.0 * oriented_area_m2, 1, 2).generator[1][2],
            2.0 * simulation.generator[1][2],
        )

    def test_schwarzschild_tidal_ranging_matches_geodesic_deviation(self) -> None:
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 6.957e9
        separation_m = 2.0
        elapsed_s = 0.25
        radial_per_s2, transverse_per_s2, _ = schwarzschild_tidal_eigenvalues_per_s2(
            SUN_MASS_KG,
            radius_m,
            g,
        )

        radial_residual_m = schwarzschild_tidal_ranging_residual_m(
            SUN_MASS_KG,
            radius_m,
            separation_m,
            elapsed_s,
            "radial",
            g,
        )
        transverse_residual_m = schwarzschild_tidal_ranging_residual_m(
            SUN_MASS_KG,
            radius_m,
            separation_m,
            elapsed_s,
            "transverse",
            g,
        )

        self.assertGreater(radial_residual_m, 0.0)
        self.assertLess(transverse_residual_m, 0.0)
        self.assertAlmostEqual(radial_residual_m, 0.5 * radial_per_s2 * separation_m * elapsed_s**2)
        self.assertAlmostEqual(transverse_residual_m, 0.5 * transverse_per_s2 * separation_m * elapsed_s**2)

    def test_tidal_ranging_has_expected_quadratic_time_and_linear_separation_scaling(self) -> None:
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 6.957e9
        base = schwarzschild_tidal_ranging_residual_m(SUN_MASS_KG, radius_m, 2.0, 0.25, "radial", g)

        self.assertAlmostEqual(
            schwarzschild_tidal_ranging_residual_m(SUN_MASS_KG, radius_m, 4.0, 0.25, "radial", g),
            2.0 * base,
        )
        self.assertAlmostEqual(
            schwarzschild_tidal_ranging_residual_m(SUN_MASS_KG, radius_m, 2.0, 0.5, "radial", g),
            4.0 * base,
        )

    def test_h3_helpers_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            simulate_frame_loop_holonomy(math.inf, 1.0, 1, 2)
        with self.assertRaises(ValueError):
            simulate_frame_loop_holonomy(1.0, 1.0, 2, 2)
        with self.assertRaises(ValueError):
            simulate_frame_loop_holonomy(1.0, 1.0, -1, 2)
        with self.assertRaises(ValueError):
            simulate_frame_loop_holonomy(1.0, 1.0, 0, 1)
        with self.assertRaises(ValueError):
            simulate_frame_loop_holonomy(1.0, 1.0, 1, 0)
        with self.assertRaises(ValueError):
            corrected_loop_residual_s(0.0, [math.nan])
        with self.assertRaises(ValueError):
            schwarzschild_tidal_ranging_residual_m(SUN_MASS_KG, 1.0, 1.0, -1.0)
        with self.assertRaises(ValueError):
            schwarzschild_tidal_ranging_residual_m(SUN_MASS_KG, 1.0, 1.0, 1.0, "bad-axis")


if __name__ == "__main__":
    unittest.main()
