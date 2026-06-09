"""Executable H6P1 pulse-closure response boundary checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    ClosedPulseLoop,
    ClosureBaselineLedger,
    ClosureCovarianceKernel,
    ClosureEdgeObservable,
    ClosureEdgeRecord,
    ClosureMetricSensitivity,
    CoefficientLedger,
    ConservationLedger,
    EnsembleComponent,
    EnsembleDecomposition,
    PulsePotentialOperator,
    check_pure_gauge_invariance,
    closure_defect,
    closure_edge_records_from_density,
    closure_functional,
    closure_response_max_difference,
    compare_closure_baselines,
    compare_closure_responses_for_decompositions,
    finite_closure_response,
    reverse_closed_loop_orientation,
)


class PulseClosureResponseTests(unittest.TestCase):
    def _triangle_loop(self) -> ClosedPulseLoop:
        return ClosedPulseLoop("L_abc", {"ab": 1.0, "bc": 1.0, "ca": 1.0})

    def _triangle_edges(self) -> tuple[ClosureEdgeRecord, ...]:
        return (
            ClosureEdgeRecord("ab", "a", "b", 0.4),
            ClosureEdgeRecord("bc", "b", "c", -0.1),
            ClosureEdgeRecord("ca", "c", "a", 0.2),
        )

    def _kernel(self) -> ClosureCovarianceKernel:
        return ClosureCovarianceKernel(((2.0,),))

    def _sensitivity(self) -> tuple[ClosureMetricSensitivity, ...]:
        return (ClosureMetricSensitivity("g00", {"ab": 0.5, "bc": 0.0, "ca": 0.0}),)

    def _conservation(self) -> ConservationLedger:
        return ConservationLedger("expectation-conserved", accounting_source="finite closure ledger")

    def _coefficient(self) -> CoefficientLedger:
        return CoefficientLedger("derived", coefficient_name="closure-gradient")

    def _baseline(
        self,
        *,
        h6s4c_relation: str = "same-as-h6s4c-stochastic",
        h6s4q_relation: str = "same-as-h6s4q-quantum-mediator",
        distinct: bool = False,
    ) -> ClosureBaselineLedger:
        return ClosureBaselineLedger(
            h6s4c_relation,
            h6s4q_relation,
            fixed_observable_distinct_from_baselines=distinct,
        )

    def _complete_response(
        self,
        *,
        covariance: ClosureCovarianceKernel | None = None,
        conservation: ConservationLedger | None = None,
        coefficient: CoefficientLedger | None = None,
        baseline: ClosureBaselineLedger | None = None,
        gauge_invariant: bool = True,
    ):
        return finite_closure_response(
            (self._triangle_loop(),),
            self._triangle_edges(),
            self._kernel() if covariance is None else covariance,
            self._sensitivity(),
            conservation or self._conservation(),
            coefficient or self._coefficient(),
            baseline or self._baseline(),
            artifact_ledger=("ordinary instrument noise separated",),
            gauge_invariant=gauge_invariant,
        )

    def test_loop_orientation_reversal_changes_sign_of_defect(self) -> None:
        loop = self._triangle_loop()
        defect = closure_defect(loop, self._triangle_edges())
        reversed_defect = closure_defect(reverse_closed_loop_orientation(loop), self._triangle_edges())

        self.assertAlmostEqual(defect.defect, 0.5)
        self.assertAlmostEqual(reversed_defect.defect, -defect.defect)

    def test_closure_functional_is_orientation_even(self) -> None:
        loop = self._triangle_loop()
        forward = closure_functional((loop,), self._triangle_edges(), self._kernel())
        reversed_report = closure_functional(
            (reverse_closed_loop_orientation(loop),),
            self._triangle_edges(),
            self._kernel(),
        )

        self.assertAlmostEqual(forward.intrinsic_functional, 0.0625)
        self.assertAlmostEqual(reversed_report.intrinsic_functional, forward.intrinsic_functional)

    def test_independent_loop_contributions_add(self) -> None:
        first_loop = self._triangle_loop()
        first_edges = self._triangle_edges()
        second_loop = ClosedPulseLoop("L_def", {"de": 1.0, "ef": 1.0, "fd": 1.0})
        second_edges = (
            ClosureEdgeRecord("de", "d", "e", 0.1),
            ClosureEdgeRecord("ef", "e", "f", 0.2),
            ClosureEdgeRecord("fd", "f", "d", -0.7),
        )

        first = closure_functional((first_loop,), first_edges, ClosureCovarianceKernel(((2.0,),)))
        second = closure_functional((second_loop,), second_edges, ClosureCovarianceKernel(((4.0,),)))
        combined = closure_functional(
            (first_loop, second_loop),
            first_edges + second_edges,
            ClosureCovarianceKernel(((2.0, 0.0), (0.0, 4.0))),
        )

        self.assertAlmostEqual(combined.intrinsic_functional, first.intrinsic_functional + second.intrinsic_functional)

    def test_pure_gauge_relabeling_does_not_change_closed_observables(self) -> None:
        report = check_pure_gauge_invariance(
            (self._triangle_loop(),),
            self._triangle_edges(),
            {"a": 3.0, "b": -2.0, "c": 0.75},
        )

        self.assertTrue(report.invariant)
        self.assertAlmostEqual(report.max_defect_difference, 0.0)

    def test_equivalent_ensemble_decompositions_give_same_closure_response(self) -> None:
        z_decomposition = EnsembleDecomposition(
            (
                EnsembleComponent(0.5, (1.0, 0.0), "0"),
                EnsembleComponent(0.5, (0.0, 1.0), "1"),
            ),
            name="E_Z",
        )
        scale = 1.0 / math.sqrt(2.0)
        x_decomposition = EnsembleDecomposition(
            (
                EnsembleComponent(0.5, (scale, scale), "+"),
                EnsembleComponent(0.5, (scale, -scale), "-"),
            ),
            name="E_X",
        )
        observables = (
            ClosureEdgeObservable(
                "ab",
                "a",
                "b",
                PulsePotentialOperator(((0.2, 0.0), (0.0, 0.8)), label="O_ab"),
            ),
            ClosureEdgeObservable(
                "bc",
                "b",
                "c",
                PulsePotentialOperator(((-0.1, 0.0), (0.0, 0.3)), label="O_bc"),
            ),
            ClosureEdgeObservable(
                "ca",
                "c",
                "a",
                PulsePotentialOperator(((0.0, 0.0), (0.0, 0.2)), label="O_ca"),
            ),
        )

        comparison = compare_closure_responses_for_decompositions(
            z_decomposition,
            x_decomposition,
            observables,
            (self._triangle_loop(),),
            self._kernel(),
            self._sensitivity(),
            self._conservation(),
            self._coefficient(),
            self._baseline(),
            artifact_ledger=("ordinary instrument noise separated",),
        )

        self.assertTrue(comparison.ensemble_invariance.invariant)
        self.assertTrue(comparison.same_closure_response)
        self.assertAlmostEqual(comparison.ensemble_invariance.max_marginal_difference, 0.0)
        self.assertFalse(comparison.accepted_as_law)

    def test_missing_covariance_kernel_blocks_promotion(self) -> None:
        report = finite_closure_response(
            (self._triangle_loop(),),
            self._triangle_edges(),
            None,
            self._sensitivity(),
            self._conservation(),
            self._coefficient(),
            self._baseline(),
            artifact_ledger=("ordinary instrument noise separated",),
        )

        self.assertIsNone(report.functional_report)
        self.assertTrue(report.classification.promotion_blocked)
        self.assertIn("intrinsic closure covariance kernel", report.classification.missing_requirements)
        self.assertEqual(report.classification.classification, "diagnostic tool")

    def test_missing_conservation_proof_blocks_promotion(self) -> None:
        report = self._complete_response(conservation=ConservationLedger("not-yet-classified"))

        self.assertTrue(report.classification.promotion_blocked)
        self.assertIn("conservation proof", report.classification.missing_requirements)
        self.assertEqual(report.classification.classification, "diagnostic tool")

    def test_arbitrary_fitted_coefficients_are_rejected(self) -> None:
        report = self._complete_response(
            coefficient=CoefficientLedger(
                "fit-after-observation rejected",
                coefficient_name="free closure amplitude",
            )
        )

        self.assertTrue(report.classification.promotion_blocked)
        self.assertIn(
            "fit-after-observation coefficient provenance is rejected",
            report.classification.reasons,
        )
        self.assertFalse(report.classification.accepted_as_law)

    def test_ordinary_instrument_noise_is_separate_from_intrinsic_covariance(self) -> None:
        intrinsic_only = closure_functional(
            (self._triangle_loop(),),
            self._triangle_edges(),
            self._kernel(),
        )
        with_ordinary_noise = ClosureCovarianceKernel(
            ((2.0,),),
            ordinary_instrument_noise_matrix=((5.0,),),
        )
        noisy = closure_functional((self._triangle_loop(),), self._triangle_edges(), with_ordinary_noise)
        report = self._complete_response(covariance=with_ordinary_noise)

        self.assertAlmostEqual(noisy.intrinsic_functional, intrinsic_only.intrinsic_functional)
        self.assertAlmostEqual(noisy.ordinary_instrument_noise_trace, 5.0)
        self.assertTrue(report.ordinary_noise_separate)

    def test_h6s4_baseline_equivalence_forces_conditional_derivation_not_new_physics(self) -> None:
        report = self._complete_response()
        baseline = compare_closure_baselines(report)

        self.assertEqual(report.classification.classification, "conditional derivation")
        self.assertTrue(baseline.not_new_physics_claim)
        self.assertEqual(baseline.h6s4c_relation, "same-as-h6s4c-stochastic")
        self.assertEqual(baseline.h6s4q_relation, "same-as-h6s4q-quantum-mediator")

    def test_controlled_modification_requires_fixed_baseline_distinct_observable(self) -> None:
        report = self._complete_response(
            baseline=self._baseline(
                h6s4c_relation="distinct-observable",
                h6s4q_relation="distinct-observable",
                distinct=True,
            )
        )

        self.assertEqual(report.classification.classification, "controlled modification")
        self.assertTrue(report.classification.candidate_ready)
        self.assertFalse(report.accepted_as_law)

    def test_inconsistent_baseline_distinction_cannot_promote(self) -> None:
        report = self._complete_response(
            baseline=self._baseline(
                h6s4c_relation="same-as-h6s4c-stochastic",
                h6s4q_relation="distinct-observable",
                distinct=True,
            )
        )

        self.assertEqual(report.classification.classification, "diagnostic tool")
        self.assertTrue(report.classification.promotion_blocked)
        self.assertIn(
            "fixed observable distinction must be distinct from both H6S4-C and H6S4-Q baselines",
            report.classification.reasons,
        )

    def test_clean_no_go_when_invariant_closure_functional_fails(self) -> None:
        report = self._complete_response(gauge_invariant=False)

        self.assertEqual(report.classification.classification, "clean no-go")
        self.assertTrue(report.classification.promotion_blocked)
        self.assertIn("gauge-invariant closure functional", report.classification.missing_requirements)

    def test_diagnostic_tool_when_closure_machinery_has_no_baseline_distinction(self) -> None:
        report = self._complete_response(
            baseline=self._baseline(
                h6s4c_relation="not-applicable",
                h6s4q_relation="not-applicable",
                distinct=False,
            )
        )

        self.assertEqual(report.classification.classification, "diagnostic tool")
        self.assertTrue(report.classification.candidate_ready)
        self.assertFalse(report.classification.promotion_blocked)

    def test_rejects_invalid_covariance_blocks(self) -> None:
        with self.assertRaises(ValueError):
            ClosureCovarianceKernel(((1.0, 1.0), (1.0, 1.0)))
        with self.assertRaises(ValueError):
            ClosureCovarianceKernel(((1.0,),), ordinary_instrument_noise_matrix=((1.0, 0.0), (0.0, 1.0)))
        with self.assertRaises(ValueError):
            ClosureCovarianceKernel(
                ((1.0, 0.0), (0.0, 1.0)),
                ordinary_instrument_noise_matrix=((1.0, 2.0), (2.0, 1.0)),
            )

    def test_rejects_loop_coefficients_that_do_not_close_at_nodes(self) -> None:
        open_loop = ClosedPulseLoop("open", {"ab": 1.0})

        with self.assertRaises(ValueError):
            closure_functional((open_loop,), self._triangle_edges(), self._kernel())

    def test_missing_covariance_does_not_bypass_loop_closure_validation(self) -> None:
        open_loop = ClosedPulseLoop("open", {"ab": 1.0})

        with self.assertRaises(ValueError):
            finite_closure_response(
                (open_loop,),
                self._triangle_edges(),
                None,
                self._sensitivity(),
                self._conservation(),
                self._coefficient(),
                self._baseline(),
                artifact_ledger=("ordinary instrument noise separated",),
            )

    def test_direct_density_matrix_must_be_positive_semidefinite(self) -> None:
        observable = ClosureEdgeObservable(
            "ab",
            "a",
            "b",
            PulsePotentialOperator(((1.0, 0.0), (0.0, 2.0)), label="O_ab"),
        )

        with self.assertRaises(ValueError):
            closure_edge_records_from_density(((0.5, 1.0), (1.0, 0.5)), (observable,))

    def test_response_difference_includes_closure_defect_sign(self) -> None:
        forward = finite_closure_response(
            (self._triangle_loop(),),
            self._triangle_edges(),
            self._kernel(),
            (),
            self._conservation(),
            self._coefficient(),
            self._baseline(),
            artifact_ledger=("ordinary instrument noise separated",),
        )
        reversed_defect = finite_closure_response(
            (reverse_closed_loop_orientation(self._triangle_loop()),),
            self._triangle_edges(),
            self._kernel(),
            (),
            self._conservation(),
            self._coefficient(),
            self._baseline(),
            artifact_ledger=("ordinary instrument noise separated",),
        )

        self.assertAlmostEqual(closure_response_max_difference(forward, reversed_defect), 1.0)


if __name__ == "__main__":
    unittest.main()
