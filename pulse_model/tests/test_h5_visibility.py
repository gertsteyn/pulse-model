import math
import unittest

from pulse_model import (
    REDUCED_PLANCK_CONSTANT_J_S,
    clock_visibility,
    clock_visibility_series,
    gaussian_energy_spread_visibility,
    gaussian_energy_spread_visibility_series,
    height_delta_tau_s,
    two_level_clock_visibility,
    two_level_clock_visibility_series,
    velocity_delta_tau_s,
    weak_field_delta_tau_s,
)


class H5ClockVisibilityTests(unittest.TestCase):
    def test_visibility_is_one_at_zero_proper_time_difference(self) -> None:
        self.assertEqual(
            clock_visibility(
                delta_tau_s=0.0,
                energy_levels_j=[0.0, 1.0, 2.0],
                probabilities=[0.2, 0.3, 0.5],
            ),
            1.0,
        )

    def test_equal_two_level_clock_oscillates_and_revives(self) -> None:
        self.assertEqual(two_level_clock_visibility(0.0, 0.5), 1.0)
        self.assertAlmostEqual(two_level_clock_visibility(1.0, 0.5), 0.0)
        self.assertAlmostEqual(two_level_clock_visibility(2.0, 0.5), 1.0)

    def test_energy_eigenstate_keeps_full_visibility(self) -> None:
        self.assertAlmostEqual(
            two_level_clock_visibility(
                delta_tau_s=123.0,
                transition_frequency_hz=9.0,
                excited_state_probability=1.0,
            ),
            1.0,
        )

    def test_mixed_discrete_clock_dephases_without_full_two_level_revival(self) -> None:
        hbar = REDUCED_PLANCK_CONSTANT_J_S
        visibility = clock_visibility(
            delta_tau_s=1.0,
            energy_levels_j=[0.0, math.pi * hbar, 0.5 * math.pi * hbar],
            probabilities=[1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0],
            reduced_planck_constant_j_s=hbar,
        )

        self.assertGreater(visibility, 0.0)
        self.assertLess(visibility, 1.0)

    def test_visibility_series_matches_pointwise_values(self) -> None:
        delta_tau_values_s = [0.0, 0.25, 0.5, 1.0]

        self.assertEqual(
            two_level_clock_visibility_series(delta_tau_values_s, 0.5),
            [
                two_level_clock_visibility(delta_tau_s, 0.5)
                for delta_tau_s in delta_tau_values_s
            ],
        )
        self.assertEqual(
            clock_visibility_series(
                delta_tau_values_s,
                [0.0, math.pi * REDUCED_PLANCK_CONSTANT_J_S],
                [0.5, 0.5],
            ),
            [
                clock_visibility(
                    delta_tau_s,
                    [0.0, math.pi * REDUCED_PLANCK_CONSTANT_J_S],
                    [0.5, 0.5],
                )
                for delta_tau_s in delta_tau_values_s
            ],
        )

    def test_gaussian_energy_spread_visibility_decays_with_delta_tau(self) -> None:
        hbar = REDUCED_PLANCK_CONSTANT_J_S
        energy_stddev_j = hbar

        self.assertEqual(gaussian_energy_spread_visibility(0.0, energy_stddev_j), 1.0)
        self.assertAlmostEqual(
            gaussian_energy_spread_visibility(1.0, energy_stddev_j),
            math.exp(-0.5),
        )
        self.assertGreater(
            gaussian_energy_spread_visibility(0.5, energy_stddev_j),
            gaussian_energy_spread_visibility(1.0, energy_stddev_j),
        )
        self.assertEqual(
            gaussian_energy_spread_visibility(-1.0, energy_stddev_j),
            gaussian_energy_spread_visibility(1.0, energy_stddev_j),
        )

    def test_gaussian_visibility_series_matches_pointwise_values(self) -> None:
        values = [-1.0, 0.0, 1.0]

        self.assertEqual(
            gaussian_energy_spread_visibility_series(
                values,
                REDUCED_PLANCK_CONSTANT_J_S,
            ),
            [
                gaussian_energy_spread_visibility(
                    delta_tau_s,
                    REDUCED_PLANCK_CONSTANT_J_S,
                )
                for delta_tau_s in values
            ],
        )

    def test_height_delta_tau_matches_uniform_field_approximation(self) -> None:
        delta_tau_s = height_delta_tau_s(
            coordinate_time_s=5.0,
            height_difference_m=3.0,
            gravity_m_per_s2=2.0,
            speed_of_light_m_per_s=100.0,
        )

        self.assertAlmostEqual(delta_tau_s, 2.0 * 3.0 * 5.0 / 100.0**2)
        self.assertAlmostEqual(
            height_delta_tau_s(5.0, -3.0, 2.0, 100.0),
            -delta_tau_s,
        )

    def test_velocity_delta_tau_matches_low_velocity_approximation(self) -> None:
        delta_tau_s = velocity_delta_tau_s(
            coordinate_time_s=5.0,
            branch_1_velocity_m_per_s=6.0,
            branch_2_velocity_m_per_s=2.0,
            speed_of_light_m_per_s=100.0,
        )

        expected = -5.0 * (6.0**2 - 2.0**2) / (2.0 * 100.0**2)
        self.assertAlmostEqual(delta_tau_s, expected)

    def test_weak_field_delta_tau_combines_potential_and_velocity_terms(self) -> None:
        delta_tau_s = weak_field_delta_tau_s(
            coordinate_time_s=5.0,
            branch_1_potential_m2_per_s2=200.0,
            branch_2_potential_m2_per_s2=50.0,
            branch_1_velocity_m_per_s=6.0,
            branch_2_velocity_m_per_s=2.0,
            speed_of_light_m_per_s=100.0,
        )

        expected = 5.0 * (
            (200.0 - 50.0) / 100.0**2
            - (6.0**2 - 2.0**2) / (2.0 * 100.0**2)
        )
        self.assertAlmostEqual(delta_tau_s, expected)

    def test_delta_tau_helpers_feed_visibility_simulator(self) -> None:
        delta_tau_s = height_delta_tau_s(
            coordinate_time_s=2.0,
            height_difference_m=5.0,
            gravity_m_per_s2=10.0,
            speed_of_light_m_per_s=100.0,
        )

        self.assertAlmostEqual(delta_tau_s, 0.01)
        self.assertAlmostEqual(
            two_level_clock_visibility(delta_tau_s, transition_frequency_hz=25.0),
            math.sqrt(0.5),
        )

    def test_visibility_helpers_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            two_level_clock_visibility(1.0, -1.0)
        with self.assertRaises(ValueError):
            two_level_clock_visibility(1.0, 1.0, excited_state_probability=1.1)
        with self.assertRaises(ValueError):
            gaussian_energy_spread_visibility(1.0, -1.0)
        with self.assertRaises(ValueError):
            clock_visibility_series([0.0], [0.0, 1.0], [1.0])

    def test_delta_tau_helpers_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            height_delta_tau_s(-1.0, 1.0)
        with self.assertRaises(ValueError):
            velocity_delta_tau_s(1.0, 2.0, 0.0, 1.0)
        with self.assertRaises(ValueError):
            weak_field_delta_tau_s(1.0, 0.0, 0.0, speed_of_light_m_per_s=0.0)


if __name__ == "__main__":
    unittest.main()
