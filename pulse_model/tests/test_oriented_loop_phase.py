"""Executable 05S4 oriented-loop phase checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    PhaseComparisonEdge,
    OrientedLoopPhaseRecord,
    REDUCED_PLANCK_CONSTANT_J_S,
    TAU_RADIANS,
    closed_phase_sum_rad,
    compose_oriented_loop_phases,
    constant_curvature_sectional_curvatures,
    cow_phase_shift,
    estimate_oriented_phase_curvature,
    linear_oriented_phase_rad,
    oriented_phase_squared_loss_rad2,
    reverse_loop_orientation,
    spatial_only_plane_weights,
    synthesize_oriented_phase_records_from_sectional_curvatures,
)

NEUTRON_MASS_KG = 1.674_927_498_04e-27
STANDARD_GRAVITY_M_PER_S2 = 9.806_65


class OrientedLoopPhaseTests(unittest.TestCase):
    def test_closed_phase_sum_cancels_clock_zero_offsets(self) -> None:
        offsets = {"a": 1.25, "b": -0.75, "c": 2.5}
        edges = (
            PhaseComparisonEdge("a", "b", offsets["b"] - offsets["a"]),
            PhaseComparisonEdge("b", "c", offsets["c"] - offsets["b"]),
            PhaseComparisonEdge("c", "a", offsets["a"] - offsets["c"]),
        )

        self.assertAlmostEqual(closed_phase_sum_rad(edges), 0.0)
        self.assertAlmostEqual(closed_phase_sum_rad(edges, unwrap_turns=1), TAU_RADIANS)

    def test_flat_zero_phase_records_have_zero_composition_and_curvature(self) -> None:
        records = synthesize_oriented_phase_records_from_sectional_curvatures(
            constant_curvature_sectional_curvatures(0.0),
            area_m2=0.25,
            phase_coupling_rad=2.0,
            loop_scale_m=0.5,
        )

        composition = compose_oriented_loop_phases(records)
        estimate = estimate_oriented_phase_curvature(records)

        self.assertEqual(composition.classification, "zero-oriented-phase")
        self.assertEqual(composition.linear_sum_rad, 0.0)
        self.assertEqual(composition.squared_loss_rad2, 0.0)
        self.assertEqual(estimate.scalar_curvature_per_m2, 0.0)
        self.assertEqual(estimate.scalarization_residual_per_m2, 0.0)

    def test_constant_curvature_phase_records_recover_existing_scalar_estimator(self) -> None:
        curvature_scale = 0.125
        records = synthesize_oriented_phase_records_from_sectional_curvatures(
            constant_curvature_sectional_curvatures(curvature_scale),
            area_m2=0.5,
            phase_coupling_rad=3.0,
        )

        estimate = estimate_oriented_phase_curvature(records)

        self.assertAlmostEqual(estimate.scalar_curvature_per_m2, 12.0 * curvature_scale)
        self.assertAlmostEqual(estimate.sampled_scalar_curvature_per_m2, 12.0 * curvature_scale)
        self.assertAlmostEqual(estimate.scalarization_residual_per_m2, 0.0)

    def test_loop_reversal_changes_linear_phase_but_not_squared_loss(self) -> None:
        record = OrientedLoopPhaseRecord(plane=(1, 2), area_m2=4.0, observed_phase_rad=0.25, weight=2.0)
        reversed_record = reverse_loop_orientation(record)

        self.assertAlmostEqual(linear_oriented_phase_rad((record,)), 0.5)
        self.assertAlmostEqual(linear_oriented_phase_rad((reversed_record,)), -0.5)
        self.assertAlmostEqual(
            oriented_phase_squared_loss_rad2((record,)),
            oriented_phase_squared_loss_rad2((reversed_record,)),
        )

    def test_independent_loop_composition_is_additive_and_reports_cross_terms(self) -> None:
        records = (
            OrientedLoopPhaseRecord(plane=(0, 1), area_m2=1.0, observed_phase_rad=0.2),
            OrientedLoopPhaseRecord(plane=(1, 2), area_m2=1.0, observed_phase_rad=-0.05),
        )

        additive = compose_oriented_loop_phases(records)
        nonadditive = compose_oriented_loop_phases(records, shared_boundary_phase_rad=1.0e-3)

        self.assertTrue(additive.is_additive)
        self.assertAlmostEqual(additive.composed_phase_rad, 0.15)
        self.assertEqual(additive.classification, "additive-oriented-phase")
        self.assertFalse(nonadditive.is_additive)
        self.assertEqual(nonadditive.classification, "nonadditive-phase")
        self.assertAlmostEqual(nonadditive.additive_error_rad, 1.0e-3)

    def test_artifact_ledgers_subtract_and_report_finite_loop_correction(self) -> None:
        record = OrientedLoopPhaseRecord(
            plane=(1, 3),
            area_m2=2.0,
            observed_phase_rad=10.0,
            orientation=-1.0,
            calibration_phase_rad=1.0,
            matter_phase_rad=2.0,
            rotation_phase_rad=0.5,
            instrument_phase_rad=0.25,
            finite_loop_phase_rad=0.75,
        )

        composition = compose_oriented_loop_phases((record,))

        self.assertAlmostEqual(record.artifact_phase_rad, 4.5)
        self.assertAlmostEqual(record.canonical_phase_rad, 5.5)
        self.assertAlmostEqual(record.oriented_phase_rad, -5.5)
        self.assertAlmostEqual(composition.finite_loop_correction_rad, -0.75)
        self.assertEqual(composition.classification, "oriented-phase-with-finite-loop-ledger")

    def test_scalarization_residual_is_exposed_for_biased_plane_coverage(self) -> None:
        curvature_scale = 0.25
        records = synthesize_oriented_phase_records_from_sectional_curvatures(
            constant_curvature_sectional_curvatures(curvature_scale),
            area_m2=1.0e-4,
            scalarization_residual_per_m2=-6.0 * curvature_scale,
        )

        composition = compose_oriented_loop_phases(records)
        estimate = estimate_oriented_phase_curvature(records, plane_weights=spatial_only_plane_weights())

        self.assertEqual(composition.classification, "oriented-phase-with-scalarization-residual")
        self.assertAlmostEqual(composition.max_abs_scalarization_residual_per_m2, 6.0 * curvature_scale)
        self.assertAlmostEqual(estimate.scalar_curvature_per_m2, 12.0 * curvature_scale)
        self.assertAlmostEqual(estimate.sampled_scalar_curvature_per_m2, 6.0 * curvature_scale)
        self.assertAlmostEqual(estimate.scalarization_residual_per_m2, -6.0 * curvature_scale)

    def test_cow_matter_phase_and_rotation_phase_are_ledgers_not_geometry(self) -> None:
        cow_phase_rad = cow_phase_shift(
            NEUTRON_MASS_KG,
            STANDARD_GRAVITY_M_PER_S2,
            area_m2=1.0e-4,
            velocity_m_per_s=2_200.0,
            reduced_planck_constant_j_s=REDUCED_PLANCK_CONSTANT_J_S,
        )
        rotation_phase_rad = 0.125
        record = OrientedLoopPhaseRecord(
            plane=(1, 2),
            area_m2=1.0,
            observed_phase_rad=cow_phase_rad + rotation_phase_rad,
            matter_phase_rad=cow_phase_rad,
            rotation_phase_rad=rotation_phase_rad,
        )

        composition = compose_oriented_loop_phases((record,))

        self.assertAlmostEqual(record.canonical_phase_rad, 0.0)
        self.assertEqual(composition.classification, "zero-oriented-phase")
        self.assertAlmostEqual(composition.linear_sum_rad, 0.0)

    def test_rejects_nonfinite_or_physically_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            PhaseComparisonEdge("", "b", 0.0)
        with self.assertRaises(ValueError):
            PhaseComparisonEdge("a", "b", math.nan)
        with self.assertRaises(ValueError):
            closed_phase_sum_rad(
                (
                    PhaseComparisonEdge("a", "b", 0.1),
                    PhaseComparisonEdge("c", "a", -0.1),
                )
            )
        with self.assertRaises(ValueError):
            closed_phase_sum_rad((PhaseComparisonEdge("a", "a", 0.0),), unwrap_turns=0.5)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            OrientedLoopPhaseRecord(plane=(0, 1), area_m2=0.0, observed_phase_rad=0.0)
        with self.assertRaises(ValueError):
            OrientedLoopPhaseRecord(plane=(0, 1), area_m2=1.0, observed_phase_rad=math.inf)
        with self.assertRaises(ValueError):
            OrientedLoopPhaseRecord(plane=(0, 1), area_m2=1.0, observed_phase_rad=0.0, orientation=0.0)
        with self.assertRaises(ValueError):
            OrientedLoopPhaseRecord(plane=(0, 0), area_m2=1.0, observed_phase_rad=0.0)
        with self.assertRaises(ValueError):
            OrientedLoopPhaseRecord(plane=(0, 1), area_m2=1.0, observed_phase_rad=0.0, phase_coupling_rad=0.0)


if __name__ == "__main__":
    unittest.main()
