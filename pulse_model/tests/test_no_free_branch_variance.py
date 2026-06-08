"""Executable H6S3 no-free-branch-variance checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    CausalDomain,
    CoefficientLedger,
    ConservationLedger,
    DensityMatrixResponseSetup,
    EnsembleComponent,
    EnsembleDecomposition,
    PointerRecord,
    PulsePotentialOperator,
    ResponseDistribution,
    ResponsePoint,
    branch_variance_from_response,
    check_ensemble_invariance,
    classify_branch_variance_route,
    compare_branch_variance_across_decompositions,
    density_matrix_expectation_response,
    ensemble_density_matrix,
    guardrail_response_kernel,
    invalid_ensemble_branch_response,
    pointer_record_branch_response,
    response_marginal_max_difference,
)


class NoFreeBranchVarianceTests(unittest.TestCase):
    def _z_decomposition(self, *, pulse_counts: tuple[float, float] = (9.0, 11.0)) -> EnsembleDecomposition:
        return EnsembleDecomposition(
            (
                EnsembleComponent(0.5, (1.0, 0.0), "0", pulse_counts[0]),
                EnsembleComponent(0.5, (0.0, 1.0), "1", pulse_counts[1]),
            ),
            name="E_Z",
        )

    def _x_decomposition(self, *, pulse_counts: tuple[float, float] = (10.0, 10.0)) -> EnsembleDecomposition:
        scale = 1.0 / math.sqrt(2.0)
        return EnsembleDecomposition(
            (
                EnsembleComponent(0.5, (scale, scale), "+", pulse_counts[0]),
                EnsembleComponent(0.5, (scale, -scale), "-", pulse_counts[1]),
            ),
            name="E_X",
        )

    def _potential_operator(self) -> PulsePotentialOperator:
        return PulsePotentialOperator(((0.0, 0.0), (0.0, 2.0)), label="Phi")

    def _density_response(self, decomposition: EnsembleDecomposition) -> ResponseDistribution:
        return density_matrix_expectation_response(
            DensityMatrixResponseSetup(
                ensemble_density_matrix(decomposition),
                self._potential_operator(),
                clock_frequency_hz=2.0,
                duration_s=5.0,
                speed_of_light_m_per_s=10.0,
            )
        )

    def test_density_only_response_has_same_marginal_and_no_free_branch_variance(self) -> None:
        z_decomposition = self._z_decomposition()
        x_decomposition = self._x_decomposition()
        z_response = self._density_response(z_decomposition)
        x_response = self._density_response(x_decomposition)

        report = compare_branch_variance_across_decompositions(
            z_decomposition,
            x_decomposition,
            z_response,
            x_response,
            route_classification=classify_branch_variance_route("density-only-baseline"),
        )

        self.assertTrue(check_ensemble_invariance(z_decomposition, x_decomposition, z_response, x_response).invariant)
        self.assertAlmostEqual(response_marginal_max_difference(z_response, x_response), 0.0)
        self.assertTrue(report.same_density)
        self.assertTrue(report.same_probe_marginal)
        self.assertFalse(report.branch_variance_changes)
        self.assertFalse(report.diagnostic_failure)
        self.assertFalse(report.route_classification.physical_branch_variance_allowed)
        self.assertFalse(report.accepted_as_law)

    def test_arbitrary_branch_counts_can_change_variance_across_decompositions(self) -> None:
        z_decomposition = self._z_decomposition(pulse_counts=(9.0, 11.0))
        x_decomposition = self._x_decomposition(pulse_counts=(10.0, 10.0))
        z_response = invalid_ensemble_branch_response(z_decomposition)
        x_response = invalid_ensemble_branch_response(x_decomposition)

        report = compare_branch_variance_across_decompositions(
            z_decomposition,
            x_decomposition,
            z_response,
            x_response,
        )

        self.assertTrue(report.same_density)
        self.assertAlmostEqual(branch_variance_from_response(z_response), 1.0)
        self.assertAlmostEqual(branch_variance_from_response(x_response), 0.0)
        self.assertTrue(report.branch_variance_changes)
        self.assertTrue(report.diagnostic_failure)

    def test_decomposition_dependent_variance_is_rejected_without_records(self) -> None:
        z_decomposition = self._z_decomposition(pulse_counts=(8.0, 12.0))
        x_decomposition = self._x_decomposition(pulse_counts=(10.0, 10.0))
        report = compare_branch_variance_across_decompositions(
            z_decomposition,
            x_decomposition,
            invalid_ensemble_branch_response(z_decomposition),
            invalid_ensemble_branch_response(x_decomposition),
            route_classification=classify_branch_variance_route("unsupported-decomposition"),
        )

        self.assertTrue(report.same_density)
        self.assertTrue(report.branch_variance_changes)
        self.assertTrue(report.diagnostic_failure)
        self.assertFalse(report.route_classification.physical_branch_variance_allowed)
        self.assertEqual(report.route_classification.missing_requirements, ("physical branch-support route",))
        self.assertFalse(report.accepted_as_law)

    def test_pointer_record_variance_requires_local_record_or_shared_future(self) -> None:
        with self.assertRaises(ValueError):
            pointer_record_branch_response(
                PointerRecord(
                    pointer_basis=("0", "1"),
                    probabilities=(0.5, 0.5),
                    pulse_counts=(9.0, 11.0),
                    local_record_exists=False,
                    causal_status="inside-probe-causal-past",
                )
            )

        shared_future = pointer_record_branch_response(
            PointerRecord(
                pointer_basis=("0", "1"),
                probabilities=(0.5, 0.5),
                pulse_counts=(9.0, 11.0),
                local_record_exists=True,
                causal_status="compared-in-shared-future",
            )
        )
        route = classify_branch_variance_route(
            "pointer-record-or-collapse-record",
            local_record_declared=True,
            causal_support_declared=True,
            conservation_ledger_declared=True,
            branch_matching_declared=True,
            artifact_ledger_declared=True,
        )

        self.assertAlmostEqual(branch_variance_from_response(shared_future), 1.0)
        self.assertTrue(route.physical_branch_variance_allowed)
        self.assertTrue(route.diagnostic_only)
        self.assertFalse(route.accepted_as_law)

    def test_stochastic_classical_route_is_only_allowed_with_declared_noise_law_and_ledgers(self) -> None:
        missing_law = classify_branch_variance_route(
            "stochastic-classical-pulse-geometry",
            coefficient_provenance_declared=True,
            regulator_provenance_declared=True,
            conservation_ledger_declared=True,
            no_signaling_guardrail_declared=True,
            artifact_ledger_declared=True,
        )
        missing_regulator = classify_branch_variance_route(
            "stochastic-classical-pulse-geometry",
            stochastic_law_declared=True,
            coefficient_provenance_declared=True,
            conservation_ledger_declared=True,
            no_signaling_guardrail_declared=True,
            artifact_ledger_declared=True,
        )
        complete = classify_branch_variance_route(
            "stochastic-classical-pulse-geometry",
            stochastic_law_declared=True,
            coefficient_provenance_declared=True,
            regulator_provenance_declared=True,
            conservation_ledger_declared=True,
            no_signaling_guardrail_declared=True,
            artifact_ledger_declared=True,
        )

        self.assertFalse(missing_law.physical_branch_variance_allowed)
        self.assertIn("objective causal noise law", missing_law.missing_requirements)
        self.assertFalse(missing_regulator.physical_branch_variance_allowed)
        self.assertIn("regulator provenance", missing_regulator.missing_requirements)
        self.assertTrue(complete.physical_branch_variance_allowed)
        self.assertTrue(complete.diagnostic_only)
        self.assertFalse(complete.accepted_as_law)

    def test_quantum_geometry_route_is_only_a_scoped_comparator_without_a_law(self) -> None:
        missing_sector = classify_branch_variance_route(
            "non-classical-geometry-or-mediator",
            conservation_ledger_declared=True,
            coupling_assumptions_declared=True,
            coefficient_provenance_declared=True,
            artifact_ledger_declared=True,
            recovery_limit_declared=True,
        )
        missing_coupling = classify_branch_variance_route(
            "non-classical-geometry-or-mediator",
            non_classical_sector_declared=True,
            conservation_ledger_declared=True,
            coefficient_provenance_declared=True,
            artifact_ledger_declared=True,
            recovery_limit_declared=True,
        )
        scoped_comparator = classify_branch_variance_route(
            "non-classical-geometry-or-mediator",
            non_classical_sector_declared=True,
            coupling_assumptions_declared=True,
            conservation_ledger_declared=True,
            coefficient_provenance_declared=True,
            artifact_ledger_declared=True,
            recovery_limit_declared=True,
        )

        self.assertFalse(missing_sector.physical_branch_variance_allowed)
        self.assertIn("non-classical sector", missing_sector.missing_requirements)
        self.assertFalse(missing_coupling.physical_branch_variance_allowed)
        self.assertIn("coupling assumptions", missing_coupling.missing_requirements)
        self.assertTrue(scoped_comparator.physical_branch_variance_allowed)
        self.assertIn("comparator", scoped_comparator.reason)
        self.assertTrue(scoped_comparator.diagnostic_only)
        self.assertFalse(scoped_comparator.accepted_as_law)

    def test_ordinary_instrument_noise_is_not_counted_as_branch_response_variance(self) -> None:
        z_decomposition = self._z_decomposition()
        x_decomposition = self._x_decomposition()
        ordinary_noise = ResponseDistribution(
            (
                ResponsePoint(9.0, 0.25),
                ResponsePoint(10.0, 0.5),
                ResponsePoint(11.0, 0.25),
            ),
            family="ordinary-instrument-noise",
        )

        report = compare_branch_variance_across_decompositions(
            z_decomposition,
            x_decomposition,
            ordinary_noise,
            ordinary_noise,
            route_classification=classify_branch_variance_route("density-only-baseline"),
        )

        self.assertGreater(branch_variance_from_response(ordinary_noise), 0.0)
        self.assertTrue(report.same_density)
        self.assertTrue(report.same_probe_marginal)
        self.assertFalse(report.branch_variance_changes)
        self.assertFalse(report.diagnostic_failure)
        self.assertFalse(report.route_classification.physical_branch_variance_allowed)

    def test_fit_after_observation_coefficients_do_not_promote_variance_to_prediction(self) -> None:
        route = classify_branch_variance_route(
            "stochastic-classical-pulse-geometry",
            stochastic_law_declared=True,
            regulator_provenance_declared=True,
            conservation_ledger_declared=True,
            no_signaling_guardrail_declared=True,
            artifact_ledger_declared=True,
            coefficient_provenance_declared=False,
        )
        guardrail = guardrail_response_kernel(
            ResponseDistribution((ResponsePoint(10.0, 1.0),), family="candidate-stochastic-response"),
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("expectation-conserved", accounting_source="density operator source"),
            CoefficientLedger("fit-after-observation rejected"),
            gauge_or_branch_matching_declared=True,
            artifact_ledger=("finite H6S3 diagnostic",),
            regulator_provenance="none",
        )

        self.assertFalse(route.physical_branch_variance_allowed)
        self.assertIn("coefficient provenance", route.missing_requirements)
        self.assertFalse(route.accepted_as_law)
        self.assertFalse(guardrail.allowed)
        self.assertTrue(any("fit-after-observation" in reason for reason in guardrail.reasons))


if __name__ == "__main__":
    unittest.main()
