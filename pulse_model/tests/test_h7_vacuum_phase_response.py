import math
import unittest

from pulse_model import (
    cosmological_constant_from_energy_density_per_m2,
    cosmological_constant_from_hubble_fraction_per_m2,
    cpl_dark_energy_density_ratio,
    critical_density_energy_j_per_m3,
    dark_energy_density_j_per_m3,
    hubble_parameter_per_s,
    vacuum_energy_hierarchy_ratio,
)


class H7VacuumPhaseResponseTests(unittest.TestCase):
    def test_planck_like_dark_energy_scale_is_tiny_but_nonzero(self) -> None:
        hubble_km_per_s_mpc = 67.4
        dark_energy_fraction = 0.685

        hubble_per_s = hubble_parameter_per_s(hubble_km_per_s_mpc)
        critical_density = critical_density_energy_j_per_m3(hubble_km_per_s_mpc)
        dark_energy_density = dark_energy_density_j_per_m3(
            hubble_km_per_s_mpc,
            dark_energy_fraction,
        )
        cosmological_constant = cosmological_constant_from_hubble_fraction_per_m2(
            hubble_km_per_s_mpc,
            dark_energy_fraction,
        )

        self.assertAlmostEqual(
            hubble_per_s,
            2.184_285_241_085_502_3e-18,
            delta=2.184_285_241_085_502_3e-30,
        )
        self.assertAlmostEqual(
            critical_density,
            7.668_947_767_821_908e-10,
            delta=7.668_947_767_821_908e-22,
        )
        self.assertAlmostEqual(
            dark_energy_density,
            5.253_229_220_958_007e-10,
            delta=5.253_229_220_958_007e-22,
        )
        self.assertAlmostEqual(
            cosmological_constant,
            1.090_910_502_838_092_9e-52,
            delta=1.090_910_502_838_092_9e-64,
        )
        self.assertAlmostEqual(
            cosmological_constant,
            cosmological_constant_from_energy_density_per_m2(dark_energy_density),
            delta=cosmological_constant * 1e-12,
        )

    def test_vacuum_hierarchy_ratio_is_only_a_scale_comparison(self) -> None:
        observed_density = dark_energy_density_j_per_m3(67.4, 0.685)

        self.assertEqual(vacuum_energy_hierarchy_ratio(0.0, observed_density), 0.0)
        self.assertAlmostEqual(
            vacuum_energy_hierarchy_ratio(1.0, observed_density),
            1.0 / observed_density,
        )

    def test_cpl_density_ratio_reduces_to_constant_lambda_case(self) -> None:
        self.assertEqual(cpl_dark_energy_density_ratio(1.0), 1.0)
        self.assertEqual(cpl_dark_energy_density_ratio(0.5, w0=-1.0, wa=0.0), 1.0)
        self.assertEqual(cpl_dark_energy_density_ratio(2.0, w0=-1.0, wa=0.0), 1.0)

    def test_cpl_density_ratio_matches_w0_wa_formula(self) -> None:
        scale_factor = 0.75
        w0 = -0.8
        wa = -0.4
        expected = scale_factor ** (-3.0 * (1.0 + w0 + wa)) * math.exp(
            3.0 * wa * (scale_factor - 1.0)
        )

        self.assertAlmostEqual(
            cpl_dark_energy_density_ratio(scale_factor, w0=w0, wa=wa),
            expected,
        )

    def test_h7_cosmology_helpers_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            hubble_parameter_per_s(0.0)
        with self.assertRaises(ValueError):
            critical_density_energy_j_per_m3(-1.0)
        with self.assertRaises(ValueError):
            dark_energy_density_j_per_m3(67.4, -0.1)
        with self.assertRaises(ValueError):
            cosmological_constant_from_energy_density_per_m2(-1.0)
        with self.assertRaises(ValueError):
            vacuum_energy_hierarchy_ratio(1.0, 0.0)
        with self.assertRaises(ValueError):
            cpl_dark_energy_density_ratio(0.0)
        with self.assertRaises(ValueError):
            cpl_dark_energy_density_ratio(1.0, w0=math.inf)


if __name__ == "__main__":
    unittest.main()
