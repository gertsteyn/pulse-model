import unittest


def _dot3(left: tuple[float, float, float], right: tuple[float, float, float]) -> float:
    return sum(a * b for a, b in zip(left, right, strict=True))


def _cross3(left: tuple[float, float, float], right: tuple[float, float, float]) -> tuple[float, float, float]:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


class H4StressEnergyPhaseResponseTests(unittest.TestCase):
    def test_phase_response_identity_preserves_inverse_metric_sign(self) -> None:
        reduced_planck_constant = 3.0
        sqrt_minus_g = 2.0
        delta_theta_delta_inverse_metric = -5.0

        stress_energy_component = (
            -2.0
            * reduced_planck_constant
            / sqrt_minus_g
            * delta_theta_delta_inverse_metric
        )

        self.assertEqual(stress_energy_component, 15.0)

    def test_homogeneous_scalar_pressure_is_not_mass_density(self) -> None:
        phi_dot = 4.0
        potential = 3.0

        energy_density = 0.5 * phi_dot**2 + potential
        pressure = 0.5 * phi_dot**2 - potential

        self.assertEqual(energy_density, 11.0)
        self.assertEqual(pressure, 5.0)
        self.assertNotEqual(pressure, energy_density)

    def test_scalar_gradient_contributes_anisotropic_spatial_stress(self) -> None:
        phi_dot = 3.0
        spatial_gradient = (2.0, 0.0, 0.0)
        potential = 5.0
        gradient_squared = _dot3(spatial_gradient, spatial_gradient)
        isotropic_part = 0.5 * phi_dot**2 - 0.5 * gradient_squared - potential

        stress_xx = spatial_gradient[0] ** 2 + isotropic_part
        stress_yy = spatial_gradient[1] ** 2 + isotropic_part
        stress_zz = spatial_gradient[2] ** 2 + isotropic_part
        pressure = (stress_xx + stress_yy + stress_zz) / 3.0
        expected_pressure = 0.5 * phi_dot**2 - gradient_squared / 6.0 - potential

        self.assertAlmostEqual(stress_xx, 1.5)
        self.assertAlmostEqual(stress_yy, -2.5)
        self.assertAlmostEqual(stress_zz, -2.5)
        self.assertAlmostEqual(pressure, expected_pressure)

    def test_electromagnetic_stress_has_tension_along_field_direction(self) -> None:
        electric = (3.0, 0.0, 0.0)
        magnetic = (0.0, 0.0, 0.0)
        field_energy = _dot3(electric, electric) + _dot3(magnetic, magnetic)

        energy_density = 0.5 * field_energy
        stress_xx = -electric[0] ** 2 - magnetic[0] ** 2 + 0.5 * field_energy
        stress_yy = -electric[1] ** 2 - magnetic[1] ** 2 + 0.5 * field_energy
        stress_zz = -electric[2] ** 2 - magnetic[2] ** 2 + 0.5 * field_energy
        pressure = (stress_xx + stress_yy + stress_zz) / 3.0

        self.assertEqual(energy_density, 4.5)
        self.assertEqual(stress_xx, -4.5)
        self.assertEqual(stress_yy, 4.5)
        self.assertEqual(stress_zz, 4.5)
        self.assertEqual(pressure, energy_density / 3.0)

    def test_electromagnetic_momentum_density_is_poynting_vector(self) -> None:
        electric = (1.0, 0.0, 0.0)
        magnetic = (0.0, 2.0, 0.0)

        self.assertEqual(_cross3(electric, magnetic), (0.0, 0.0, 2.0))

    def test_point_particle_components_include_momentum_flux(self) -> None:
        delta_density = 2.0
        energy = 13.0
        momentum = (3.0, 4.0, 0.0)

        local_energy_density = energy * delta_density
        momentum_density_x = momentum[0] * delta_density
        spatial_stress_xx = momentum[0] * momentum[0] / energy * delta_density
        spatial_stress_xy = momentum[0] * momentum[1] / energy * delta_density

        self.assertEqual(local_energy_density, 26.0)
        self.assertEqual(momentum_density_x, 6.0)
        self.assertAlmostEqual(spatial_stress_xx, 18.0 / 13.0)
        self.assertAlmostEqual(spatial_stress_xy, 24.0 / 13.0)


if __name__ == "__main__":
    unittest.main()
