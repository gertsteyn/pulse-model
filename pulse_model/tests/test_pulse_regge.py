"""Executable 05S pulse-Regge prototype checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    LOCAL_FRAME_PLANES,
    BoundaryHinge,
    ReggeCell,
    ReggeHinge,
    basis_bivector,
    boundary_hinge_sum_m2,
    constant_curvature_hinges,
    linear_hinge_sum_m2,
    lower_first_lorentz_index,
    oriented_volume_sum_m4,
    project_hinge_defect,
    quadrature_scalar_curvature_from_planes,
    raise_first_lorentz_index,
    regge_curvature_integral_m2,
    scalar_curvature_from_sectional_planes,
    scalarization_residual_from_planes,
    volume_sum_m4,
    zero_matrix4,
)


class PulseReggeTests(unittest.TestCase):
    def test_flat_zero_defect_has_zero_hinge_and_curvature_sum(self) -> None:
        hinge = ReggeHinge(area_m2=4.0, defect=project_hinge_defect(zero_matrix4(), basis_bivector(1, 2)))

        self.assertEqual(hinge.defect, 0.0)
        self.assertEqual(linear_hinge_sum_m2([hinge]), 0.0)
        self.assertEqual(regge_curvature_integral_m2([hinge]), 0.0)

    def test_project_hinge_defect_recovers_rotation_and_orientation_sign(self) -> None:
        generator = basis_bivector(1, 2, 0.125)
        normal = basis_bivector(1, 2)
        reversed_normal = basis_bivector(1, 2, -1.0)

        self.assertAlmostEqual(project_hinge_defect(generator, normal), 0.125)
        self.assertAlmostEqual(project_hinge_defect(generator, reversed_normal), -0.125)
        self.assertAlmostEqual(project_hinge_defect(basis_bivector(1, 2, -0.125), normal), -0.125)

    def test_project_hinge_defect_accepts_time_space_boost_plane(self) -> None:
        rapidity = 0.02
        generator_lower = basis_bivector(0, 1, rapidity)
        generator_mixed = raise_first_lorentz_index(generator_lower)

        self.assertAlmostEqual(generator_mixed[0][1], -rapidity)
        self.assertAlmostEqual(generator_mixed[1][0], -rapidity)
        self.assertAlmostEqual(
            project_hinge_defect(lower_first_lorentz_index(generator_mixed), basis_bivector(0, 1)),
            rapidity,
        )

    def test_scalarization_quadrature_detects_anisotropic_plane_weights(self) -> None:
        curvature_scale = 0.125
        constant_curvature_planes = {
            plane: curvature_scale if plane[0] != 0 else -curvature_scale for plane in LOCAL_FRAME_PLANES
        }
        full_weights = {plane: 1.0 for plane in LOCAL_FRAME_PLANES}
        spatial_only_weights = {
            (0, 1): 0.0,
            (0, 2): 0.0,
            (0, 3): 0.0,
            (1, 2): 1.0,
            (1, 3): 1.0,
            (2, 3): 1.0,
        }

        expected_scalar_curvature = 12.0 * curvature_scale
        self.assertAlmostEqual(
            scalar_curvature_from_sectional_planes(constant_curvature_planes),
            expected_scalar_curvature,
        )
        self.assertAlmostEqual(
            quadrature_scalar_curvature_from_planes(constant_curvature_planes, full_weights),
            expected_scalar_curvature,
        )
        self.assertAlmostEqual(scalarization_residual_from_planes(constant_curvature_planes, full_weights), 0.0)
        self.assertAlmostEqual(
            scalarization_residual_from_planes(constant_curvature_planes, spatial_only_weights),
            -6.0 * curvature_scale,
        )

    def test_constant_curvature_refinement_preserves_regge_curvature_integral(self) -> None:
        scalar_curvature_per_m2 = 3.0e-12
        volume_m4 = 2.5e20
        expected_integral_m2 = scalar_curvature_per_m2 * volume_m4

        coarse = constant_curvature_hinges(scalar_curvature_per_m2, volume_m4, refinement_cells=1)
        refined = constant_curvature_hinges(scalar_curvature_per_m2, volume_m4, refinement_cells=16)

        self.assertAlmostEqual(regge_curvature_integral_m2(coarse), expected_integral_m2)
        self.assertAlmostEqual(regge_curvature_integral_m2(refined), expected_integral_m2)
        self.assertAlmostEqual(refined[0].area_m2, coarse[0].area_m2 / 4.0)
        self.assertAlmostEqual(refined[0].defect, coarse[0].defect / 4.0)

    def test_linear_defect_sum_scales_with_area_defect_and_orientation(self) -> None:
        base = [ReggeHinge(area_m2=10.0, defect=0.2)]
        doubled_area = [ReggeHinge(area_m2=20.0, defect=0.2)]
        doubled_defect = [ReggeHinge(area_m2=10.0, defect=0.4)]
        reversed_orientation = [ReggeHinge(area_m2=10.0, defect=0.2, orientation=-1.0)]

        self.assertAlmostEqual(linear_hinge_sum_m2(doubled_area), 2.0 * linear_hinge_sum_m2(base))
        self.assertAlmostEqual(linear_hinge_sum_m2(doubled_defect), 2.0 * linear_hinge_sum_m2(base))
        self.assertAlmostEqual(linear_hinge_sum_m2(reversed_orientation), -linear_hinge_sum_m2(base))

    def test_boundary_hinge_sum_tracks_orientation_sign(self) -> None:
        boundary = [BoundaryHinge(area_m2=6.0, exterior_angle=0.25)]
        reversed_boundary = [BoundaryHinge(area_m2=6.0, exterior_angle=0.25, orientation=-1.0)]

        self.assertAlmostEqual(boundary_hinge_sum_m2(boundary), 1.5)
        self.assertAlmostEqual(boundary_hinge_sum_m2(reversed_boundary), -1.5)

    def test_volume_sum_keeps_positive_cell_volumes(self) -> None:
        self.assertAlmostEqual(volume_sum_m4([1.0, 2.5, 3.5]), 7.0)

    def test_oriented_volume_sum_tracks_cell_orientation(self) -> None:
        cells = [ReggeCell(volume_m4=3.0), ReggeCell(volume_m4=1.25, orientation=-1.0)]

        self.assertAlmostEqual(oriented_volume_sum_m4(cells), 1.75)

    def test_pulse_regge_helpers_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            ReggeHinge(area_m2=0.0, defect=1.0)
        with self.assertRaises(ValueError):
            ReggeHinge(area_m2=1.0, defect=math.nan)
        with self.assertRaises(ValueError):
            ReggeHinge(area_m2=1.0, defect=1.0, orientation=0.5)
        with self.assertRaises(ValueError):
            ReggeCell(volume_m4=1.0, orientation=0.5)
        with self.assertRaises(ValueError):
            BoundaryHinge(area_m2=-1.0, exterior_angle=1.0)
        with self.assertRaises(ValueError):
            basis_bivector(1, 1)
        with self.assertRaises(ValueError):
            basis_bivector(-1, 2)
        with self.assertRaises(ValueError):
            project_hinge_defect(
                (
                    (1.0, 0.0, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                    (0.0, 0.0, 0.0, 0.0),
                ),
                zero_matrix4(),
            )
        with self.assertRaises(ValueError):
            constant_curvature_hinges(1.0, 1.0, 0)
        with self.assertRaises(ValueError):
            volume_sum_m4([1.0, 0.0])
        with self.assertRaises(ValueError):
            scalar_curvature_from_sectional_planes({(0, 0): 1.0})
        with self.assertRaises(ValueError):
            quadrature_scalar_curvature_from_planes({(0, 1): 1.0}, {(0, 4): 1.0})


if __name__ == "__main__":
    unittest.main()
