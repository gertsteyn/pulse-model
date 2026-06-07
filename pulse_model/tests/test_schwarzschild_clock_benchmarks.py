"""Executable exact-Schwarzschild static clock benchmarks.

All quantities use SI units. These tests cover only static clocks outside a
non-rotating spherical mass in Schwarzschild coordinates; infalling observers,
Kerr spacetime, and general geodesic checks belong to later benchmarks.
"""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    SPEED_OF_LIGHT_M_PER_S,
    schwarzschild_radius,
    schwarzschild_static_dtaudt,
    weak_field_dtaudt,
)

EARTH_MASS_KG = 5.972_2e24
EARTH_EQUATORIAL_RADIUS_M = 6_378_137.0
SUN_MASS_KG = 1.988_47e30
SUN_PHOTOSPHERE_RADIUS_M = 695_700_000.0


class SchwarzschildClockBenchmarks(unittest.TestCase):
    def test_static_clock_rate_matches_exact_formula_for_representative_radii(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2

        cases = [
            (EARTH_MASS_KG, EARTH_EQUATORIAL_RADIUS_M),
            (SUN_MASS_KG, SUN_PHOTOSPHERE_RADIUS_M),
            (SUN_MASS_KG, 10.0 * schwarzschild_radius(SUN_MASS_KG, g, c)),
        ]

        for mass_kg, radius_m in cases:
            with self.subTest(mass_kg=mass_kg, radius_m=radius_m):
                expected = math.sqrt(1.0 - 2.0 * g * mass_kg / (radius_m * c**2))

                self.assertAlmostEqual(
                    schwarzschild_static_dtaudt(mass_kg, radius_m, g, c),
                    expected,
                    delta=abs(expected) * 1e-15,
                )

    def test_weak_field_limit_matches_newtonian_potential_first_order(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        schwarzschild_radius_m = schwarzschild_radius(SUN_MASS_KG, g, c)
        radius_m = 10_000.0 * schwarzschild_radius_m

        exact_rate = schwarzschild_static_dtaudt(SUN_MASS_KG, radius_m, g, c)
        potential_m2_per_s2 = -g * SUN_MASS_KG / radius_m
        weak_field_rate = weak_field_dtaudt(potential_m2_per_s2, 0.0, c)

        epsilon = schwarzschild_radius_m / radius_m
        self.assertLess(weak_field_rate - exact_rate, epsilon**2)
        self.assertAlmostEqual(exact_rate, weak_field_rate, delta=epsilon**2)

    def test_clock_rate_decreases_toward_horizon_without_crossing_domain(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        schwarzschild_radius_m = schwarzschild_radius(SUN_MASS_KG, g, c)

        far_rate = schwarzschild_static_dtaudt(SUN_MASS_KG, 10.0 * schwarzschild_radius_m, g, c)
        close_rate = schwarzschild_static_dtaudt(SUN_MASS_KG, 1.01 * schwarzschild_radius_m, g, c)
        very_close_rate = schwarzschild_static_dtaudt(
            SUN_MASS_KG,
            1.000_001 * schwarzschild_radius_m,
            g,
            c,
        )

        self.assertGreater(far_rate, close_rate)
        self.assertGreater(close_rate, very_close_rate)
        self.assertGreater(very_close_rate, 0.0)
        self.assertAlmostEqual(
            very_close_rate,
            math.sqrt(1.0 - 1.0 / 1.000_001),
            delta=1e-14,
        )

    def test_static_clock_rejects_radii_at_or_inside_schwarzschild_radius(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
        schwarzschild_radius_m = schwarzschild_radius(SUN_MASS_KG, g, c)

        for radius_m in [schwarzschild_radius_m, 0.5 * schwarzschild_radius_m, 0.0, -1.0]:
            with self.subTest(radius_m=radius_m):
                with self.assertRaises(ValueError):
                    schwarzschild_static_dtaudt(SUN_MASS_KG, radius_m, g, c)

    def test_schwarzschild_radius_uses_si_units_and_scales_linearly_with_mass(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        g = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2

        sun_radius_m = schwarzschild_radius(SUN_MASS_KG, g, c)

        self.assertAlmostEqual(sun_radius_m, 2_953.3, delta=0.5)
        self.assertAlmostEqual(
            schwarzschild_radius(2.0 * SUN_MASS_KG, g, c),
            2.0 * sun_radius_m,
            delta=sun_radius_m * 1e-15,
        )


if __name__ == "__main__":
    unittest.main()
