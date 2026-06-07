"""Executable 05S2 pulse-record curvature estimator checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    LOCAL_FRAME_PLANES,
    PulseLoopRecord,
    classify_scalarization,
    compare_orientation_sensitivity,
    correction_within_relative_bound,
    constant_curvature_sectional_curvatures,
    estimate_pulse_record_curvature,
    estimate_refinement_convergence,
    extract_correction_basis,
    finite_loop_bias_coefficients_per_m4,
    finite_loop_relative_error,
    max_loop_scale_for_finite_loop_bound,
    oriented_linear_defect_functional,
    relative_correction_size,
    scalarization_relative_norm,
    spatial_only_plane_weights,
    squared_defect_loss,
    synthesize_loop_records_from_sectional_curvatures,
    synthesize_refined_loop_record_levels,
    trace_free_tidal_sectional_curvatures,
)


class PulseRecordCurvatureTests(unittest.TestCase):
    def test_flat_zero_records_have_zero_scalar_and_zero_residual(self) -> None:
        records = synthesize_loop_records_from_sectional_curvatures(
            constant_curvature_sectional_curvatures(0.0),
            area_m2=4.0,
            loop_scale_m=2.0,
        )

        estimate = estimate_pulse_record_curvature(records)

        self.assertEqual(estimate.validation_failures, ())
        self.assertEqual(estimate.plane_coverage_fraction, 1.0)
        self.assertEqual(estimate.plane_coverage.missing_planes, ())
        self.assertAlmostEqual(estimate.scalar_curvature_per_m2, 0.0)
        self.assertAlmostEqual(estimate.sampled_scalar_curvature_per_m2, 0.0)
        self.assertAlmostEqual(estimate.scalarization_residual_per_m2, 0.0)
        self.assertTrue(all(value == 0.0 for value in estimate.anisotropic_residuals_per_m2.values()))

    def test_constant_curvature_records_recover_expected_scalar(self) -> None:
        curvature_scale = 0.125
        records = synthesize_loop_records_from_sectional_curvatures(
            constant_curvature_sectional_curvatures(curvature_scale),
            area_m2=0.25,
            loop_scale_m=0.5,
        )

        estimate = estimate_pulse_record_curvature(records)

        self.assertAlmostEqual(estimate.scalar_curvature_per_m2, 12.0 * curvature_scale)
        self.assertAlmostEqual(estimate.sampled_scalar_curvature_per_m2, 12.0 * curvature_scale)
        self.assertAlmostEqual(estimate.scalarization_residual_per_m2, 0.0)
        self.assertTrue(
            all(math.isclose(value, 0.0, abs_tol=1.0e-15) for value in estimate.anisotropic_residuals_per_m2.values())
        )

    def test_trace_free_tidal_records_report_zero_scalar_and_anisotropy(self) -> None:
        tidal_scale = 2.0e-9
        records = synthesize_loop_records_from_sectional_curvatures(
            trace_free_tidal_sectional_curvatures(tidal_scale),
            area_m2=1.0e-4,
            loop_scale_m=1.0e-2,
        )

        estimate = estimate_pulse_record_curvature(records)

        self.assertAlmostEqual(estimate.scalar_curvature_per_m2, 0.0)
        self.assertAlmostEqual(estimate.scalarization_residual_per_m2, 0.0)
        self.assertAlmostEqual(estimate.sectional_curvatures_per_m2[(0, 1)], 2.0 * tidal_scale)
        self.assertAlmostEqual(estimate.anisotropic_residuals_per_m2[(0, 1)], 2.0 * tidal_scale)
        self.assertAlmostEqual(estimate.anisotropic_residuals_per_m2[(2, 3)], 2.0 * tidal_scale)

    def test_biased_plane_weights_produce_reported_scalarization_residual(self) -> None:
        curvature_scale = 0.25
        records = synthesize_loop_records_from_sectional_curvatures(
            constant_curvature_sectional_curvatures(curvature_scale),
            area_m2=9.0e-4,
        )

        estimate = estimate_pulse_record_curvature(records, plane_weights=spatial_only_plane_weights())

        self.assertAlmostEqual(estimate.scalar_curvature_per_m2, 12.0 * curvature_scale)
        self.assertAlmostEqual(estimate.sampled_scalar_curvature_per_m2, 6.0 * curvature_scale)
        self.assertAlmostEqual(estimate.scalarization_residual_per_m2, -6.0 * curvature_scale)
        self.assertEqual(
            classify_scalarization(estimate, residual_floor_per_m2=1.0e-15),
            "preferred-projection-correction",
        )

    def test_constant_curvature_refinement_reports_second_order_convergence(self) -> None:
        curvature_scale = 0.125
        true_scalar = 12.0 * curvature_scale
        levels = synthesize_refined_loop_record_levels(
            constant_curvature_sectional_curvatures(curvature_scale),
            loop_scales_m=(0.4, 0.2, 0.1),
            finite_loop_bias_per_m4=0.5,
        )

        report = estimate_refinement_convergence(
            levels,
            true_scalar_curvature_per_m2=true_scalar,
            error_floor_per_m2=1.0e-18,
        )

        self.assertEqual(report.classification, "convergent")
        self.assertEqual([level.loop_scale_m for level in report.levels], [0.4, 0.2, 0.1])
        self.assertTrue(all(level.estimate.plane_coverage_fraction == 1.0 for level in report.levels))
        self.assertTrue(all(level.scalarization_classification == "unbiased" for level in report.levels))
        self.assertAlmostEqual(report.levels[0].scalar_error_per_m2, 12.0 * 0.5 * 0.4**2)
        self.assertAlmostEqual(report.levels[1].scalar_error_per_m2, 12.0 * 0.5 * 0.2**2)
        self.assertAlmostEqual(report.levels[2].scalar_error_per_m2, 12.0 * 0.5 * 0.1**2)
        self.assertTrue(all(math.isclose(slope, 2.0, abs_tol=1.0e-12) for slope in report.adjacent_slopes))

    def test_flat_refinement_reports_exact_within_floor(self) -> None:
        levels = synthesize_refined_loop_record_levels(
            constant_curvature_sectional_curvatures(0.0),
            loop_scales_m=(1.0, 0.5, 0.25),
        )

        report = estimate_refinement_convergence(
            levels,
            true_scalar_curvature_per_m2=0.0,
            error_floor_per_m2=1.0e-30,
        )

        self.assertEqual(report.classification, "exact-within-floor")
        self.assertEqual(report.max_abs_scalar_error_per_m2, 0.0)
        self.assertEqual(report.max_abs_scalarization_residual_per_m2, 0.0)
        self.assertTrue(all(math.isinf(slope) for slope in report.adjacent_slopes))

    def test_empty_refinement_report_has_clean_no_levels_classification(self) -> None:
        report = estimate_refinement_convergence((), true_scalar_curvature_per_m2=0.0)

        self.assertEqual(report.levels, ())
        self.assertEqual(report.adjacent_slopes, ())
        self.assertEqual(report.scalar_error_classification, "no-levels")
        self.assertEqual(report.scalarization_classification, "no-levels")
        self.assertEqual(report.classification, "no-levels")

    def test_refinement_reports_biased_sampling_as_correction(self) -> None:
        curvature_scale = 0.25
        levels = synthesize_refined_loop_record_levels(
            constant_curvature_sectional_curvatures(curvature_scale),
            loop_scales_m=(0.2, 0.1),
        )

        report = estimate_refinement_convergence(
            levels,
            true_scalar_curvature_per_m2=12.0 * curvature_scale,
            plane_weights=spatial_only_plane_weights(),
        )

        self.assertEqual(report.scalar_error_classification, "exact-within-floor")
        self.assertEqual(report.scalarization_classification, "preferred-projection-correction")
        self.assertEqual(report.classification, "exact-within-floor-with-preferred-projection-correction")
        self.assertTrue(
            all(level.scalarization_classification == "preferred-projection-correction" for level in report.levels)
        )
        self.assertTrue(all(level.estimate.scalarization_residual_per_m2 < 0.0 for level in report.levels))
        self.assertAlmostEqual(report.max_abs_scalarization_residual_per_m2, 6.0 * curvature_scale)

    def test_validation_reports_missing_planes_and_rejects_bad_records(self) -> None:
        partial_records = (
            PulseLoopRecord(plane=(0, 1), area_m2=1.0, defect=0.25),
            PulseLoopRecord(plane=(1, 2), area_m2=1.0, defect=0.25),
        )

        reported = estimate_pulse_record_curvature(partial_records, raise_on_validation=False)

        self.assertFalse(reported.is_valid)
        self.assertIn("missing local two-plane coverage", reported.validation_failures[0])
        self.assertEqual(reported.plane_coverage.represented_planes, ((0, 1), (1, 2)))
        with self.assertRaises(ValueError):
            estimate_pulse_record_curvature(partial_records)
        with self.assertRaises(ValueError):
            estimate_pulse_record_curvature(())
        with self.assertRaises(ValueError):
            PulseLoopRecord(plane=(0, 0), area_m2=1.0, defect=0.0)
        with self.assertRaises(ValueError):
            PulseLoopRecord(plane=(0, 1), area_m2=0.0, defect=0.0)
        with self.assertRaises(ValueError):
            PulseLoopRecord(plane=(0, 1), area_m2=1.0, defect=math.nan)
        with self.assertRaises(ValueError):
            PulseLoopRecord(plane=(0, 1), area_m2=1.0, defect=0.0, orientation=0.0)
        with self.assertRaises(ValueError):
            estimate_pulse_record_curvature(
                synthesize_loop_records_from_sectional_curvatures(
                    constant_curvature_sectional_curvatures(0.0),
                    area_m2=1.0,
                ),
                plane_weights={(0, 1): -1.0},
            )

    def test_reversed_plane_order_is_canonicalized(self) -> None:
        record = PulseLoopRecord(plane=(2, 0), area_m2=2.0, defect=-0.5)

        self.assertEqual(record.plane, (0, 2))
        self.assertIn(record.plane, LOCAL_FRAME_PLANES)
        self.assertAlmostEqual(record.sectional_curvature_per_m2, -0.25)

    def test_oriented_linear_defect_keeps_sign_while_squared_loss_does_not(self) -> None:
        record = PulseLoopRecord(plane=(1, 2), area_m2=4.0, defect=0.125, weight=2.0)
        reversed_record = PulseLoopRecord(plane=(1, 2), area_m2=4.0, defect=0.125, orientation=-1.0, weight=2.0)

        self.assertAlmostEqual(oriented_linear_defect_functional((record,)), 0.25)
        self.assertAlmostEqual(oriented_linear_defect_functional((reversed_record,)), -0.25)
        self.assertAlmostEqual(squared_defect_loss((record,)), squared_defect_loss((reversed_record,)))

        check = compare_orientation_sensitivity(record)

        self.assertTrue(check.linear_changes_sign)
        self.assertTrue(check.squared_loss_loses_orientation)
        self.assertAlmostEqual(check.linear_forward, -check.linear_reversed)
        self.assertAlmostEqual(check.squared_forward, check.squared_reversed)

    def test_defect_is_canonical_signed_value_and_orientation_applies_once(self) -> None:
        canonical_negative = PulseLoopRecord(plane=(0, 1), area_m2=2.0, defect=-0.5)
        reversed_loop = PulseLoopRecord(plane=(0, 1), area_m2=2.0, defect=-0.5, orientation=-1.0)

        self.assertAlmostEqual(canonical_negative.sectional_curvature_per_m2, -0.25)
        self.assertAlmostEqual(reversed_loop.sectional_curvature_per_m2, 0.25)
        self.assertAlmostEqual(oriented_linear_defect_functional((canonical_negative,)), -0.5)
        self.assertAlmostEqual(oriented_linear_defect_functional((reversed_loop,)), 0.5)

    def test_correction_basis_extracts_scalarization_and_finite_loop_terms(self) -> None:
        curvature_scale = 0.25
        levels = synthesize_refined_loop_record_levels(
            constant_curvature_sectional_curvatures(curvature_scale),
            loop_scales_m=(0.4, 0.2, 0.1),
            finite_loop_bias_per_m4=0.5,
        )
        report = estimate_refinement_convergence(
            levels,
            true_scalar_curvature_per_m2=12.0 * curvature_scale,
            error_floor_per_m2=1.0e-18,
        )
        biased_estimate = estimate_pulse_record_curvature(
            synthesize_loop_records_from_sectional_curvatures(
                constant_curvature_sectional_curvatures(curvature_scale),
                area_m2=1.0e-4,
            ),
            plane_weights=spatial_only_plane_weights(),
        )

        coefficients = finite_loop_bias_coefficients_per_m4(report)
        correction = extract_correction_basis(biased_estimate, refinement_report=report)

        self.assertEqual(coefficients, correction.finite_loop_bias_coefficients_per_m4)
        self.assertTrue(all(math.isclose(value, 6.0, abs_tol=1.0e-12) for value in coefficients))
        self.assertAlmostEqual(correction.finite_loop_bias_mean_per_m4, 6.0)
        self.assertAlmostEqual(correction.scalarization_residual_per_m2, -6.0 * curvature_scale)
        self.assertAlmostEqual(correction.scalarization_relative_norm, 0.5)
        self.assertAlmostEqual(scalarization_relative_norm(biased_estimate), 0.5)
        self.assertEqual(
            correction.retained_terms,
            ("preferred-projection-scalarization", "finite-loop-higher-curvature"),
        )
        self.assertEqual(correction.unsupported_terms, ("torsion", "nonlocal-kernel", "lattice-memory"))

    def test_correction_basis_does_not_keep_unsupported_terms_for_clean_estimate(self) -> None:
        estimate = estimate_pulse_record_curvature(
            synthesize_loop_records_from_sectional_curvatures(
                constant_curvature_sectional_curvatures(0.0),
                area_m2=1.0,
            )
        )

        correction = extract_correction_basis(estimate)

        self.assertEqual(correction.retained_terms, ())
        self.assertIsNone(correction.finite_loop_bias_mean_per_m4)
        self.assertEqual(correction.unsupported_terms, ("torsion", "nonlocal-kernel", "lattice-memory"))

    def test_scalarization_correction_bound_rejects_large_preferred_projection(self) -> None:
        curvature_scale = 0.25
        estimate = estimate_pulse_record_curvature(
            synthesize_loop_records_from_sectional_curvatures(
                constant_curvature_sectional_curvatures(curvature_scale),
                area_m2=1.0,
            ),
            plane_weights=spatial_only_plane_weights(),
        )

        self.assertAlmostEqual(
            relative_correction_size(
                estimate.scalarization_residual_per_m2,
                estimate.scalar_curvature_per_m2,
            ),
            0.5,
        )
        self.assertFalse(
            correction_within_relative_bound(
                estimate.scalarization_residual_per_m2,
                estimate.scalar_curvature_per_m2,
                relative_bound=0.01,
            )
        )

    def test_finite_loop_bound_sets_maximum_loop_scale(self) -> None:
        finite_loop_bias = 6.0
        reference_scalar = 3.0
        relative_bound = 0.01

        max_scale = max_loop_scale_for_finite_loop_bound(
            finite_loop_bias,
            reference_scalar,
            relative_bound,
        )

        self.assertAlmostEqual(max_scale, math.sqrt(0.03 / 6.0))
        self.assertLess(
            finite_loop_relative_error(finite_loop_bias, 0.5 * max_scale, reference_scalar),
            relative_bound,
        )
        self.assertGreater(
            finite_loop_relative_error(finite_loop_bias, 2.0 * max_scale, reference_scalar),
            relative_bound,
        )
        self.assertEqual(max_loop_scale_for_finite_loop_bound(0.0, reference_scalar, relative_bound), math.inf)

    def test_finite_loop_bound_rejects_nonfinite_reference_scalar(self) -> None:
        for reference_scalar in (math.nan, math.inf, -math.inf):
            with self.assertRaises(ValueError):
                max_loop_scale_for_finite_loop_bound(
                    finite_loop_bias_per_m4=6.0,
                    reference_scalar_curvature_per_m2=reference_scalar,
                    relative_bound=0.01,
                )


if __name__ == "__main__":
    unittest.main()
