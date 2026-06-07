import math
import unittest

from pulse_model import (
    REDUCED_PLANCK_CONSTANT_J_S,
    SPEED_OF_LIGHT_M_PER_S,
    clock_visibility,
    cow_phase_shift,
    free_massive_phase,
    gravitational_redshift,
    proper_time_flat,
    pulse_count,
    weak_field_dtaudt,
)


class CalculationTests(unittest.TestCase):
    def test_proper_time_flat_matches_sr_time_dilation(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S

        self.assertEqual(proper_time_flat(10.0, 0.0, c), 10.0)
        self.assertAlmostEqual(proper_time_flat(10.0, 0.6 * c, c), 8.0)
        self.assertEqual(proper_time_flat(10.0, c, c), 0.0)

    def test_weak_field_dtaudt_combines_potential_and_velocity_terms(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S
        phi = -6.25e7
        velocity = 3_900.0

        expected = 1.0 + phi / c**2 - velocity**2 / (2.0 * c**2)
        self.assertAlmostEqual(weak_field_dtaudt(phi, velocity, c), expected)

    def test_pulse_count_uses_hertz_times_seconds(self) -> None:
        self.assertEqual(pulse_count(9_192_631_770.0, 2.0), 18_385_263_540.0)

    def test_free_massive_phase_is_dimensionless_and_negative(self) -> None:
        phase = free_massive_phase(2.0, 3.0, 5.0, 10.0)

        self.assertEqual(phase, -15.0)

    def test_gravitational_redshift_uses_receiver_minus_emitter_frequency(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S

        self.assertEqual(gravitational_redshift(0.0, 0.0, c), 0.0)
        self.assertLess(gravitational_redshift(-10.0, 0.0, c), 0.0)

    def test_cow_phase_shift_scales_with_mass_area_gravity_and_inverse_velocity(self) -> None:
        base = cow_phase_shift(2.0, 3.0, 5.0, 7.0, 11.0)

        self.assertAlmostEqual(base, 30.0 / 77.0)
        self.assertAlmostEqual(cow_phase_shift(4.0, 3.0, 5.0, 7.0, 11.0), 2.0 * base)
        self.assertAlmostEqual(cow_phase_shift(2.0, 3.0, 5.0, 14.0, 11.0), 0.5 * base)

    def test_clock_visibility_handles_zero_and_destructive_two_level_cases(self) -> None:
        hbar = REDUCED_PLANCK_CONSTANT_J_S

        self.assertEqual(clock_visibility(0.0, [0.0, 2.0], [0.5, 0.5], hbar), 1.0)
        self.assertAlmostEqual(clock_visibility(1.0, [0.0, math.pi * hbar], [0.5, 0.5], hbar), 0.0)

    def test_validation_rejects_unphysical_inputs(self) -> None:
        c = SPEED_OF_LIGHT_M_PER_S

        with self.assertRaises(ValueError):
            proper_time_flat(1.0, 1.1 * c, c)
        with self.assertRaises(ValueError):
            pulse_count(-1.0, 1.0)
        with self.assertRaises(ValueError):
            cow_phase_shift(1.0, 9.8, 1.0, 0.0)
        with self.assertRaises(ValueError):
            clock_visibility(1.0, [0.0, 1.0], [0.25, 0.25])


if __name__ == "__main__":
    unittest.main()
