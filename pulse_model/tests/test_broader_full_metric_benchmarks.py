"""Broader full-metric GR benchmarks for the known-physics gate.

These tests extend the first Schwarzschild slices without introducing a
general tensor engine. They check closed-form radial, null, tidal, and
non-Schwarzschild metric results with explicit SI-unit domains.
"""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    SPEED_OF_LIGHT_M_PER_S,
    de_sitter_static_dtaudt,
    schwarzschild_radial_freefall_from_rest_at_infinity_drdtau_m_per_s,
    schwarzschild_radial_freefall_from_rest_at_infinity_dtaudt,
    schwarzschild_radial_null_coordinate_speed_m_per_s,
    schwarzschild_radial_null_light_time_s,
    schwarzschild_radius,
    schwarzschild_tidal_eigenvalues_per_s2,
)

SUN_MASS_KG = 1.988_47e30


def schwarzschild_a(radius_m: float, schwarzschild_radius_m: float) -> float:
    return 1.0 - schwarzschild_radius_m / radius_m


class BroaderFullMetricBenchmarks(unittest.TestCase):
    def test_radial_freefall_from_infinity_has_timelike_normalization(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 12.0 * schwarzschild_radius(SUN_MASS_KG, g, c)
        a = schwarzschild_a(radius_m, schwarzschild_radius(SUN_MASS_KG, g, c))

        dtdtau = schwarzschild_radial_freefall_from_rest_at_infinity_dtaudt(
            SUN_MASS_KG,
            radius_m,
            g,
            c,
        )
        drdtau_m_per_s = schwarzschild_radial_freefall_from_rest_at_infinity_drdtau_m_per_s(
            SUN_MASS_KG,
            radius_m,
            g,
            c,
        )

        metric_norm_m2_per_s2 = -a * c**2 * dtdtau**2 + drdtau_m_per_s**2 / a

        self.assertLess(drdtau_m_per_s, 0.0)
        self.assertAlmostEqual(
            abs(drdtau_m_per_s),
            math.sqrt(2.0 * g * SUN_MASS_KG / radius_m),
            delta=abs(drdtau_m_per_s) * 1e-15,
        )
        self.assertAlmostEqual(metric_norm_m2_per_s2, -c**2, delta=c**2 * 1e-14)

    def test_radial_null_coordinate_speed_has_zero_interval(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 20.0 * schwarzschild_radius(SUN_MASS_KG, g, c)
        a = schwarzschild_a(radius_m, schwarzschild_radius(SUN_MASS_KG, g, c))

        outgoing_speed_m_per_s = schwarzschild_radial_null_coordinate_speed_m_per_s(
            SUN_MASS_KG,
            radius_m,
            True,
            g,
            c,
        )
        incoming_speed_m_per_s = schwarzschild_radial_null_coordinate_speed_m_per_s(
            SUN_MASS_KG,
            radius_m,
            False,
            g,
            c,
        )
        interval_per_dt2_m2_per_s2 = -a * c**2 + outgoing_speed_m_per_s**2 / a

        self.assertGreater(outgoing_speed_m_per_s, 0.0)
        self.assertLess(incoming_speed_m_per_s, 0.0)
        self.assertAlmostEqual(outgoing_speed_m_per_s, c * a, delta=c * 1e-15)
        self.assertAlmostEqual(interval_per_dt2_m2_per_s2, 0.0, delta=c**2 * 1e-14)

    def test_radial_null_light_time_includes_schwarzschild_log_term(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        schwarzschild_radius_m = schwarzschild_radius(SUN_MASS_KG, g, c)
        start_radius_m = 20.0 * schwarzschild_radius_m
        end_radius_m = 60.0 * schwarzschild_radius_m

        light_time_s = schwarzschild_radial_null_light_time_s(
            SUN_MASS_KG,
            start_radius_m,
            end_radius_m,
            g,
            c,
        )
        flat_time_s = (end_radius_m - start_radius_m) / c
        expected_extra_s = (
            schwarzschild_radius_m
            * math.log((end_radius_m - schwarzschild_radius_m) / (start_radius_m - schwarzschild_radius_m))
            / c
        )

        self.assertGreater(light_time_s, flat_time_s)
        self.assertAlmostEqual(light_time_s, flat_time_s + expected_extra_s, delta=light_time_s * 1e-15)
        self.assertAlmostEqual(
            schwarzschild_radial_null_light_time_s(SUN_MASS_KG, end_radius_m, start_radius_m, g, c),
            light_time_s,
            delta=light_time_s * 1e-15,
        )

    def test_schwarzschild_tidal_eigenvalues_match_geodesic_deviation_signs(self) -> None:
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 6_957_000_000.0
        separation_m = 2.0

        radial_per_s2, transverse_1_per_s2, transverse_2_per_s2 = schwarzschild_tidal_eigenvalues_per_s2(
            SUN_MASS_KG,
            radius_m,
            g,
        )

        self.assertGreater(radial_per_s2 * separation_m, 0.0)
        self.assertLess(transverse_1_per_s2 * separation_m, 0.0)
        self.assertAlmostEqual(radial_per_s2, 2.0 * g * SUN_MASS_KG / radius_m**3)
        self.assertAlmostEqual(transverse_1_per_s2, -g * SUN_MASS_KG / radius_m**3)
        self.assertAlmostEqual(radial_per_s2 + transverse_1_per_s2 + transverse_2_per_s2, 0.0)

    def test_de_sitter_static_clock_rate_covers_non_schwarzschild_metric(self) -> None:
        cosmological_constant_per_m2 = 1.1e-52
        radius_m = 1.0e24
        epsilon = cosmological_constant_per_m2 * radius_m**2 / 3.0

        exact_rate = de_sitter_static_dtaudt(cosmological_constant_per_m2, radius_m)
        weak_rate = 1.0 - 0.5 * epsilon

        self.assertAlmostEqual(exact_rate, math.sqrt(1.0 - epsilon))
        self.assertAlmostEqual(exact_rate, weak_rate, delta=epsilon**2)
        self.assertEqual(de_sitter_static_dtaudt(0.0, radius_m), 1.0)

    def test_broader_full_metric_helpers_reject_invalid_domains(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        schwarzschild_radius_m = schwarzschild_radius(SUN_MASS_KG, g, c)

        for radius_m in [schwarzschild_radius_m, 0.5 * schwarzschild_radius_m, 0.0, -1.0]:
            with self.subTest(radius_m=radius_m):
                with self.assertRaises(ValueError):
                    schwarzschild_radial_freefall_from_rest_at_infinity_dtaudt(SUN_MASS_KG, radius_m, g, c)
                with self.assertRaises(ValueError):
                    schwarzschild_radial_null_coordinate_speed_m_per_s(SUN_MASS_KG, radius_m, True, g, c)

        with self.assertRaises(ValueError):
            schwarzschild_radial_null_light_time_s(
                SUN_MASS_KG,
                10.0 * schwarzschild_radius_m,
                schwarzschild_radius_m,
                g,
                c,
            )

        cosmological_constant_per_m2 = 1.1e-52
        horizon_radius_m = math.sqrt(3.0 / cosmological_constant_per_m2)
        with self.assertRaises(ValueError):
            de_sitter_static_dtaudt(cosmological_constant_per_m2, horizon_radius_m)
        with self.assertRaises(ValueError):
            de_sitter_static_dtaudt(-cosmological_constant_per_m2, 1.0)


if __name__ == "__main__":
    unittest.main()
