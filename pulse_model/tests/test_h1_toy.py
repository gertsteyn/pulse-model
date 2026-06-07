import math
import unittest

from pulse_model import PulseConditionedTwoLevelModel


class PulseConditionedTwoLevelModelTests(unittest.TestCase):
    def test_sharp_window_matches_standard_born_prediction(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=10.0,
            rabi_angular_frequency_rad_per_s=math.pi,
        )

        pulse_count = 5.0
        proper_time_s = pulse_count / 10.0

        self.assertAlmostEqual(
            model.sharp_window_excited_probability(pulse_count),
            model.standard_excited_probability(proper_time_s),
        )

    def test_sharp_window_uses_calibrated_pulse_count(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=8.0,
            rabi_angular_frequency_rad_per_s=2.0 * math.pi,
        )

        self.assertEqual(model.proper_time_at_pulse_count_s(4.0), 0.5)
        self.assertAlmostEqual(model.sharp_window_excited_probability(4.0), 1.0)

    def test_finite_window_averages_nearby_standard_predictions(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=10.0,
            rabi_angular_frequency_rad_per_s=2.0 * math.pi,
        )

        averaged = model.finite_window_excited_probability(
            center_pulse_count=10.0,
            window_width_pulses=5.0,
        )

        self.assertAlmostEqual(averaged, 0.5 - 1.0 / math.pi)
        self.assertGreater(averaged, model.sharp_window_excited_probability(10.0))

    def test_finite_window_converges_to_sharp_window(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=100.0,
            rabi_angular_frequency_rad_per_s=3.0,
        )

        sharp = model.sharp_window_excited_probability(42.0)
        finite = model.finite_window_excited_probability(
            center_pulse_count=42.0,
            window_width_pulses=1.0e-6,
        )

        self.assertAlmostEqual(finite, sharp, places=12)

    def test_leading_resolution_correction_matches_small_uniform_window(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=100.0,
            rabi_angular_frequency_rad_per_s=4.0,
        )

        exact = model.finite_window_excited_probability(
            center_pulse_count=25.0,
            window_width_pulses=0.1,
        )
        leading = model.leading_uniform_window_resolution_probability(
            center_pulse_count=25.0,
            window_width_pulses=0.1,
        )

        self.assertAlmostEqual(leading, exact, delta=1.0e-8)

    def test_resolution_correction_scales_with_variance(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=50.0,
            rabi_angular_frequency_rad_per_s=2.5,
        )

        small = model.leading_resolution_correction(
            center_pulse_count=5.0,
            resolution_stddev_pulses=0.2,
        )
        large = model.leading_resolution_correction(
            center_pulse_count=5.0,
            resolution_stddev_pulses=0.4,
        )

        self.assertAlmostEqual(large, 4.0 * small)

    def test_full_period_window_averages_to_one_half(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=10.0,
            rabi_angular_frequency_rad_per_s=2.0 * math.pi,
        )

        self.assertAlmostEqual(
            model.finite_window_excited_probability(
                center_pulse_count=5.0,
                window_width_pulses=10.0,
            ),
            0.5,
        )

    def test_finite_window_rejects_windows_crossing_counter_origin(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=10.0,
            rabi_angular_frequency_rad_per_s=2.0 * math.pi,
        )

        with self.assertRaises(ValueError):
            model.finite_window_excited_probability(
                center_pulse_count=1.0,
                window_width_pulses=3.0,
            )

    def test_leading_uniform_window_rejects_large_phase_width(self) -> None:
        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=1.0,
            rabi_angular_frequency_rad_per_s=10.0,
        )

        with self.assertRaises(ValueError):
            model.leading_uniform_window_resolution_probability(
                center_pulse_count=10.0,
                window_width_pulses=1.0,
            )

    def test_validation_rejects_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            PulseConditionedTwoLevelModel(
                clock_frequency_hz=0.0,
                rabi_angular_frequency_rad_per_s=1.0,
            )
        with self.assertRaises(ValueError):
            PulseConditionedTwoLevelModel(
                clock_frequency_hz=1.0,
                rabi_angular_frequency_rad_per_s=-1.0,
            )

        model = PulseConditionedTwoLevelModel(
            clock_frequency_hz=1.0,
            rabi_angular_frequency_rad_per_s=1.0,
        )

        with self.assertRaises(ValueError):
            model.sharp_window_excited_probability(-1.0)
        with self.assertRaises(ValueError):
            model.finite_window_excited_probability(1.0, -1.0)
        with self.assertRaises(ValueError):
            model.leading_resolution_correction(1.0, -1.0)
        with self.assertRaises(ValueError):
            model.leading_uniform_window_resolution_probability(1.0, -1.0)


if __name__ == "__main__":
    unittest.main()
