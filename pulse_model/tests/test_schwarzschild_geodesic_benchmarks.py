"""Executable curved-metric geodesic benchmarks for Schwarzschild spacetime.

All quantities use SI units. This first slice checks equatorial timelike
circular geodesics outside a non-rotating spherical mass. The coordinate
angular frequency is tested only together with the radial geodesic residual and
the four-velocity normalization, so the benchmark is not just a coordinate
artifact check.
"""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    SPEED_OF_LIGHT_M_PER_S,
    schwarzschild_circular_geodesic_angular_frequency,
    schwarzschild_circular_geodesic_dtaudt,
    schwarzschild_radius,
    weak_field_dtaudt,
)

SUN_MASS_KG = 1.988_47e30


def schwarzschild_a(radius_m: float, schwarzschild_radius_m: float) -> float:
    return 1.0 - schwarzschild_radius_m / radius_m


class SchwarzschildGeodesicBenchmarks(unittest.TestCase):
    def test_circular_geodesic_satisfies_radial_geodesic_equation(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 10.0 * schwarzschild_radius(SUN_MASS_KG, g, c)
        a = schwarzschild_a(radius_m, schwarzschild_radius(SUN_MASS_KG, g, c))

        dtaudt = schwarzschild_circular_geodesic_dtaudt(SUN_MASS_KG, radius_m, g, c)
        dtdtau = 1.0 / dtaudt
        dphidt = schwarzschild_circular_geodesic_angular_frequency(SUN_MASS_KG, radius_m, g, c)
        dphidtau = dphidt * dtdtau

        gamma_r_tt_m_per_s2 = a * g * SUN_MASS_KG / radius_m**2
        gamma_r_phiphi_m = -a * radius_m
        residual_m_per_s2 = (
            gamma_r_tt_m_per_s2 * dtdtau**2
            + gamma_r_phiphi_m * dphidtau**2
        )
        residual_scale_m_per_s2 = (
            abs(gamma_r_tt_m_per_s2 * dtdtau**2)
            + abs(gamma_r_phiphi_m * dphidtau**2)
        )

        self.assertAlmostEqual(residual_m_per_s2, 0.0, delta=residual_scale_m_per_s2 * 1e-14)

    def test_circular_geodesic_four_velocity_has_timelike_normalization(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 12.0 * schwarzschild_radius(SUN_MASS_KG, g, c)
        a = schwarzschild_a(radius_m, schwarzschild_radius(SUN_MASS_KG, g, c))

        dtdtau = 1.0 / schwarzschild_circular_geodesic_dtaudt(SUN_MASS_KG, radius_m, g, c)
        dphidt = schwarzschild_circular_geodesic_angular_frequency(SUN_MASS_KG, radius_m, g, c)
        dphidtau = dphidt * dtdtau

        metric_norm_m2_per_s2 = -a * c**2 * dtdtau**2 + radius_m**2 * dphidtau**2

        self.assertAlmostEqual(metric_norm_m2_per_s2, -c**2, delta=c**2 * 1e-14)

    def test_circular_geodesic_weak_field_limit_matches_newtonian_orbit_rate(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 10_000.0 * schwarzschild_radius(SUN_MASS_KG, g, c)

        exact_dtaudt = schwarzschild_circular_geodesic_dtaudt(SUN_MASS_KG, radius_m, g, c)
        coordinate_orbit_speed_m_per_s = math.sqrt(g * SUN_MASS_KG / radius_m)
        weak_field_rate = weak_field_dtaudt(
            -g * SUN_MASS_KG / radius_m,
            coordinate_orbit_speed_m_per_s,
            c,
        )

        epsilon = g * SUN_MASS_KG / (radius_m * c**2)
        self.assertAlmostEqual(
            exact_dtaudt,
            weak_field_rate,
            delta=2.0 * epsilon**2,
        )
        self.assertAlmostEqual(
            schwarzschild_circular_geodesic_angular_frequency(SUN_MASS_KG, radius_m, g, c),
            math.sqrt(g * SUN_MASS_KG / radius_m**3),
            delta=1e-15,
        )

    def test_circular_geodesic_rate_is_not_static_clock_rate(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        radius_m = 20.0 * schwarzschild_radius(SUN_MASS_KG, g, c)

        circular_geodesic_dtaudt = schwarzschild_circular_geodesic_dtaudt(
            SUN_MASS_KG,
            radius_m,
            g,
            c,
        )
        static_dtaudt = math.sqrt(1.0 - schwarzschild_radius(SUN_MASS_KG, g, c) / radius_m)

        self.assertLess(circular_geodesic_dtaudt, static_dtaudt)

    def test_timelike_circular_geodesic_rejects_radii_at_or_inside_existence_limit(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        minimum_radius_m = 1.5 * schwarzschild_radius(SUN_MASS_KG, g, c)

        for radius_m in [minimum_radius_m, 0.99 * minimum_radius_m, 0.0, -1.0]:
            with self.subTest(radius_m=radius_m):
                with self.assertRaises(ValueError):
                    schwarzschild_circular_geodesic_dtaudt(SUN_MASS_KG, radius_m, g, c)
                with self.assertRaises(ValueError):
                    schwarzschild_circular_geodesic_angular_frequency(
                        SUN_MASS_KG,
                        radius_m,
                        g,
                        c,
                    )


if __name__ == "__main__":
    unittest.main()
