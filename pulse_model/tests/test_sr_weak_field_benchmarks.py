"""Executable SR, weak-field, GPS, and Newtonian-action benchmarks.

All quantities use SI units. Fractional clock-rate tests compare ``d tau / dt``
values directly; daily clock offsets are reported in microseconds per day.
The Newtonian-action check uses the weak-field Lagrangian
``L = 1/2 m v^2 - m Phi`` and verifies the Euler-Lagrange result
``a = -grad(Phi)`` by finite differencing a central potential.
"""

from __future__ import annotations

import math
import unittest

from pulse_model import SPEED_OF_LIGHT_M_PER_S, proper_time_flat, weak_field_dtaudt

EARTH_GRAVITATIONAL_PARAMETER_M3_PER_S2 = 3.986_004_418e14
EARTH_EQUATORIAL_RADIUS_M = 6_378_137.0
GPS_NOMINAL_ALTITUDE_M = 20_200_000.0
SECONDS_PER_DAY = 86_400.0


def earth_potential_m2_per_s2(radius_m: float) -> float:
    return -EARTH_GRAVITATIONAL_PARAMETER_M3_PER_S2 / radius_m


def circular_orbit_speed_m_per_s(radius_m: float) -> float:
    return math.sqrt(EARTH_GRAVITATIONAL_PARAMETER_M3_PER_S2 / radius_m)


def finite_difference_gradient(
    potential,
    position_m: float,
    step_m: float,
) -> float:
    return (potential(position_m + step_m) - potential(position_m - step_m)) / (2.0 * step_m)


class SrWeakFieldBenchmarks(unittest.TestCase):
    def test_sr_time_dilation_matches_lorentz_factor(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        coordinate_time_s = 12.5
        velocity_m_per_s = 0.8 * c

        proper_time_s = proper_time_flat(coordinate_time_s, velocity_m_per_s, c)

        self.assertAlmostEqual(proper_time_s, 0.6 * coordinate_time_s, places=12)

    def test_weak_field_potential_and_velocity_terms_have_expected_signs(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        surface_phi = earth_potential_m2_per_s2(EARTH_EQUATORIAL_RADIUS_M)
        higher_phi = earth_potential_m2_per_s2(EARTH_EQUATORIAL_RADIUS_M + 1_000.0)

        surface_static_rate = weak_field_dtaudt(surface_phi, 0.0, c)
        higher_static_rate = weak_field_dtaudt(higher_phi, 0.0, c)
        surface_moving_rate = weak_field_dtaudt(surface_phi, 1_000.0, c)

        self.assertGreater(higher_static_rate, surface_static_rate)
        self.assertLess(surface_moving_rate, surface_static_rate)

    def test_gps_scale_corrections_have_standard_signs_and_magnitude(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        gps_radius_m = EARTH_EQUATORIAL_RADIUS_M + GPS_NOMINAL_ALTITUDE_M
        gps_speed_m_per_s = circular_orbit_speed_m_per_s(gps_radius_m)

        surface_phi = earth_potential_m2_per_s2(EARTH_EQUATORIAL_RADIUS_M)
        gps_phi = earth_potential_m2_per_s2(gps_radius_m)

        gravitational_gain_per_day_us = ((gps_phi - surface_phi) / c**2) * SECONDS_PER_DAY * 1e6
        velocity_loss_per_day_us = (-(gps_speed_m_per_s**2) / (2.0 * c**2)) * SECONDS_PER_DAY * 1e6
        net_rate_delta_per_day_us = (
            weak_field_dtaudt(gps_phi, gps_speed_m_per_s, c)
            - weak_field_dtaudt(surface_phi, 0.0, c)
        ) * SECONDS_PER_DAY * 1e6

        self.assertGreater(gravitational_gain_per_day_us, 0.0)
        self.assertLess(velocity_loss_per_day_us, 0.0)
        self.assertGreater(net_rate_delta_per_day_us, 0.0)
        self.assertAlmostEqual(gravitational_gain_per_day_us, 45.7, delta=0.5)
        self.assertAlmostEqual(velocity_loss_per_day_us, -7.2, delta=0.2)
        self.assertAlmostEqual(net_rate_delta_per_day_us, 38.5, delta=0.7)

    def test_circular_orbit_zero_dilation_altitude_ignoring_ground_rotation(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        zero_dilation_radius_m = 1.5 * EARTH_EQUATORIAL_RADIUS_M
        zero_dilation_altitude_m = zero_dilation_radius_m - EARTH_EQUATORIAL_RADIUS_M

        surface_rate = weak_field_dtaudt(
            earth_potential_m2_per_s2(EARTH_EQUATORIAL_RADIUS_M),
            0.0,
            c,
        )
        orbit_rate = weak_field_dtaudt(
            earth_potential_m2_per_s2(zero_dilation_radius_m),
            circular_orbit_speed_m_per_s(zero_dilation_radius_m),
            c,
        )

        self.assertAlmostEqual(zero_dilation_altitude_m / 1_000.0, 3_189.1, delta=0.1)
        self.assertAlmostEqual(orbit_rate - surface_rate, 0.0, delta=2e-16)

    def test_newtonian_acceleration_follows_minus_gradient_of_potential(self) -> None:
        radius_m = EARTH_EQUATORIAL_RADIUS_M
        finite_difference_step_m = 10.0

        radial_acceleration_m_per_s2 = -finite_difference_gradient(
            earth_potential_m2_per_s2,
            radius_m,
            finite_difference_step_m,
        )
        expected_acceleration_m_per_s2 = -EARTH_GRAVITATIONAL_PARAMETER_M3_PER_S2 / radius_m**2

        self.assertLess(radial_acceleration_m_per_s2, 0.0)
        self.assertAlmostEqual(radial_acceleration_m_per_s2, expected_acceleration_m_per_s2, places=9)
        self.assertAlmostEqual(abs(radial_acceleration_m_per_s2), 9.798, delta=0.001)


if __name__ == "__main__":
    unittest.main()
