"""Executable phase, redshift, and COW benchmarks.

The tests use SI units and compare dimensionless phase outputs against the
standard weak-field formulas documented in the formalization.
"""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    REDUCED_PLANCK_CONSTANT_J_S,
    SPEED_OF_LIGHT_M_PER_S,
    cow_phase_shift,
    free_massive_phase,
    gravitational_redshift,
    weak_field_dtaudt,
)

NEUTRON_MASS_KG = 1.674_927_498_04e-27
STANDARD_GRAVITY_M_PER_S2 = 9.806_65


class PhaseRedshiftCowBenchmarks(unittest.TestCase):
    def test_gravitational_redshift_for_one_meter_height_has_standard_sign(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        height_m = 1.0
        lower_potential_m2_per_s2 = 0.0
        upper_potential_m2_per_s2 = STANDARD_GRAVITY_M_PER_S2 * height_m

        fractional_shift = gravitational_redshift(
            lower_potential_m2_per_s2,
            upper_potential_m2_per_s2,
            c,
        )

        expected = -STANDARD_GRAVITY_M_PER_S2 * height_m / c**2
        self.assertLess(fractional_shift, 0.0)
        self.assertAlmostEqual(fractional_shift, expected, delta=abs(expected) * 1e-12)
        self.assertAlmostEqual(fractional_shift, -1.091e-16, delta=1e-19)

    def test_rest_phase_detuning_matches_weak_field_potential_energy_term(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        hbar = REDUCED_PLANCK_CONSTANT_J_S
        potential_m2_per_s2 = -6.25e7
        coordinate_time_s = 1.0e-6

        flat_phase = free_massive_phase(NEUTRON_MASS_KG, coordinate_time_s, c, hbar)
        weak_field_phase = free_massive_phase(
            NEUTRON_MASS_KG,
            coordinate_time_s * weak_field_dtaudt(potential_m2_per_s2, 0.0, c),
            c,
            hbar,
        )

        detuning_phase = weak_field_phase - flat_phase
        expected = -NEUTRON_MASS_KG * potential_m2_per_s2 * coordinate_time_s / hbar

        self.assertGreater(detuning_phase, 0.0)
        self.assertTrue(math.isfinite(detuning_phase))
        self.assertAlmostEqual(detuning_phase, expected, delta=abs(expected) * 5e-7)

    def test_free_massive_phase_is_dimensionless_and_scales_linearly(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        hbar = REDUCED_PLANCK_CONSTANT_J_S
        proper_time_s = 1.0e-9

        base_phase = free_massive_phase(NEUTRON_MASS_KG, proper_time_s, c, hbar)
        double_mass_phase = free_massive_phase(2.0 * NEUTRON_MASS_KG, proper_time_s, c, hbar)
        double_time_phase = free_massive_phase(NEUTRON_MASS_KG, 2.0 * proper_time_s, c, hbar)

        expected = -(NEUTRON_MASS_KG * c**2 / hbar) * proper_time_s
        self.assertLess(base_phase, 0.0)
        self.assertTrue(math.isfinite(base_phase))
        self.assertAlmostEqual(base_phase, expected, delta=abs(expected) * 1e-15)
        self.assertAlmostEqual(double_mass_phase, 2.0 * base_phase, delta=abs(base_phase) * 1e-15)
        self.assertAlmostEqual(double_time_phase, 2.0 * base_phase, delta=abs(base_phase) * 1e-15)

    def test_cow_phase_representative_neutron_case_is_dimensionless(self) -> None:
        hbar = REDUCED_PLANCK_CONSTANT_J_S
        area_m2 = 1.0e-4
        velocity_m_per_s = 2_200.0

        phase = cow_phase_shift(
            NEUTRON_MASS_KG,
            STANDARD_GRAVITY_M_PER_S2,
            area_m2,
            velocity_m_per_s,
            hbar,
        )

        expected = NEUTRON_MASS_KG * STANDARD_GRAVITY_M_PER_S2 * area_m2 / (hbar * velocity_m_per_s)
        self.assertGreater(phase, 0.0)
        self.assertTrue(math.isfinite(phase))
        self.assertAlmostEqual(phase, expected, delta=abs(expected) * 1e-15)
        self.assertAlmostEqual(phase, 7.08, delta=0.02)

    def test_cow_phase_scaling_with_mass_gravity_area_and_velocity(self) -> None:
        hbar = REDUCED_PLANCK_CONSTANT_J_S
        base = cow_phase_shift(NEUTRON_MASS_KG, STANDARD_GRAVITY_M_PER_S2, 2.0e-4, 1_800.0, hbar)

        self.assertAlmostEqual(
            cow_phase_shift(2.0 * NEUTRON_MASS_KG, STANDARD_GRAVITY_M_PER_S2, 2.0e-4, 1_800.0, hbar),
            2.0 * base,
            delta=abs(base) * 1e-15,
        )
        self.assertAlmostEqual(
            cow_phase_shift(NEUTRON_MASS_KG, 2.0 * STANDARD_GRAVITY_M_PER_S2, 2.0e-4, 1_800.0, hbar),
            2.0 * base,
            delta=abs(base) * 1e-15,
        )
        self.assertAlmostEqual(
            cow_phase_shift(NEUTRON_MASS_KG, STANDARD_GRAVITY_M_PER_S2, 4.0e-4, 1_800.0, hbar),
            2.0 * base,
            delta=abs(base) * 1e-15,
        )
        self.assertAlmostEqual(
            cow_phase_shift(NEUTRON_MASS_KG, STANDARD_GRAVITY_M_PER_S2, 2.0e-4, 3_600.0, hbar),
            0.5 * base,
            delta=abs(base) * 1e-15,
        )


if __name__ == "__main__":
    unittest.main()
