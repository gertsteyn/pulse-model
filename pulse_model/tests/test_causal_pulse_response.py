"""Executable H6S2 causal pulse-response guardrail checks."""

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
    check_causal_domain,
    check_ensemble_invariance,
    decomposition_distance,
    density_matrix_expectation_response,
    ensemble_density_matrix,
    guardrail_response_kernel,
    invalid_ensemble_branch_response,
    pointer_record_branch_response,
    response_marginal_max_difference,
)


class CausalPulseResponseTests(unittest.TestCase):
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

    def _expectation_response(self, decomposition: EnsembleDecomposition) -> ResponseDistribution:
        return density_matrix_expectation_response(
            DensityMatrixResponseSetup(
                ensemble_density_matrix(decomposition),
                self._potential_operator(),
                clock_frequency_hz=2.0,
                duration_s=5.0,
                speed_of_light_m_per_s=10.0,
            )
        )

    def test_expectation_response_is_decomposition_invariant(self) -> None:
        z_decomposition = self._z_decomposition()
        x_decomposition = self._x_decomposition()

        z_response = self._expectation_response(z_decomposition)
        x_response = self._expectation_response(x_decomposition)
        report = check_ensemble_invariance(
            z_decomposition,
            x_decomposition,
            z_response,
            x_response,
        )

        self.assertLess(decomposition_distance(z_decomposition, x_decomposition), 1.0e-12)
        self.assertTrue(report.invariant)
        self.assertAlmostEqual(response_marginal_max_difference(z_response, x_response), 0.0)
        self.assertAlmostEqual(z_response.points[0].pulse_count, 10.1)

    def test_invalid_branch_response_detects_decomposition_dependence(self) -> None:
        z_decomposition = self._z_decomposition(pulse_counts=(9.0, 11.0))
        x_decomposition = self._x_decomposition(pulse_counts=(10.0, 10.0))
        z_response = invalid_ensemble_branch_response(z_decomposition)
        x_response = invalid_ensemble_branch_response(x_decomposition)

        report = check_ensemble_invariance(
            z_decomposition,
            x_decomposition,
            z_response,
            x_response,
        )
        guardrail = guardrail_response_kernel(
            z_response,
            CausalDomain("spacelike-remote-choice", ledgers_declared=True),
            ConservationLedger("branchwise-conserved", accounting_source="branch toy ledger"),
            CoefficientLedger("derived"),
            gauge_or_branch_matching_declared=True,
            artifact_ledger=("invalid ensemble diagnostic",),
            regulator_provenance="none",
            probe_marginal_changes=True,
        )

        self.assertFalse(report.invariant)
        self.assertEqual(report.max_marginal_difference, math.inf)
        self.assertTrue(z_response.diagnostic_only)
        self.assertFalse(z_response.accepted_as_law)
        self.assertFalse(guardrail.allowed)
        self.assertTrue(any("spacelike-remote-choice" in reason for reason in guardrail.reasons))

    def test_pointer_record_response_requires_causal_record(self) -> None:
        inside_record = PointerRecord(
            pointer_basis=("0", "1"),
            probabilities=(0.5, 0.5),
            pulse_counts=(9.0, 11.0),
            local_record_exists=True,
            causal_status="inside-probe-causal-past",
        )
        shared_future_record = PointerRecord(
            pointer_basis=("0", "1"),
            probabilities=(0.5, 0.5),
            pulse_counts=(9.0, 11.0),
            local_record_exists=True,
            causal_status="compared-in-shared-future",
        )
        modeled_channel_record = PointerRecord(
            pointer_basis=("0", "1"),
            probabilities=(0.5, 0.5),
            pulse_counts=(9.0, 11.0),
            local_record_exists=True,
            causal_status="causal-channel-declared",
            channel_description="modeled classical record channel",
        )

        self.assertEqual(len(pointer_record_branch_response(inside_record).points), 2)
        self.assertEqual(len(pointer_record_branch_response(shared_future_record).points), 2)
        self.assertEqual(len(pointer_record_branch_response(modeled_channel_record).points), 2)

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
        with self.assertRaises(ValueError):
            pointer_record_branch_response(
                PointerRecord(
                    pointer_basis=("0", "1"),
                    probabilities=(0.5, 0.5),
                    pulse_counts=(9.0, 11.0),
                    local_record_exists=True,
                    causal_status="spacelike-remote-choice",
                )
            )
        with self.assertRaises(ValueError):
            pointer_record_branch_response(
                PointerRecord(
                    pointer_basis=("0", "1"),
                    probabilities=(0.5, 0.5),
                    pulse_counts=(9.0, 11.0),
                    local_record_exists=True,
                    causal_status="causal-channel-declared",
                )
            )

    def test_same_density_matrix_same_probe_marginal(self) -> None:
        z_decomposition = self._z_decomposition()
        x_decomposition = self._x_decomposition()
        z_response = self._expectation_response(z_decomposition)
        x_response = self._expectation_response(x_decomposition)

        self.assertLess(decomposition_distance(z_decomposition, x_decomposition), 1.0e-12)
        self.assertEqual(response_marginal_max_difference(z_response, x_response), 0.0)
        self.assertTrue(
            check_ensemble_invariance(
                z_decomposition,
                x_decomposition,
                z_response,
                x_response,
            ).invariant
        )

    def test_candidate_kernel_missing_conservation_is_blocked(self) -> None:
        response = ResponseDistribution((ResponsePoint(10.0, 1.0),), family="candidate")
        report = guardrail_response_kernel(
            response,
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("not-yet-classified"),
            CoefficientLedger("derived"),
            gauge_or_branch_matching_declared=True,
            artifact_ledger=("finite two-state diagnostic",),
            regulator_provenance="none",
        )

        self.assertFalse(report.allowed)
        self.assertIn("missing conservation status", report.reasons)

    def test_no_fitted_coefficient_or_fit_after_observation(self) -> None:
        response = ResponseDistribution((ResponsePoint(10.0, 1.0),), family="candidate")
        report = guardrail_response_kernel(
            response,
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("expectation-conserved", accounting_source="density operator source"),
            CoefficientLedger("fit-after-observation rejected"),
            gauge_or_branch_matching_declared=True,
            artifact_ledger=("finite two-state diagnostic",),
            regulator_provenance="none",
        )

        self.assertFalse(report.allowed)
        self.assertTrue(any("fit-after-observation" in reason for reason in report.reasons))
        with self.assertRaises(ValueError):
            CoefficientLedger("fit-after-observation")

    def test_not_declared_and_unmodeled_causal_channel_are_blocked(self) -> None:
        self.assertEqual(
            check_causal_domain(CausalDomain("not-declared")),
            (False, "not-declared causal domain is blocked"),
        )
        self.assertFalse(check_causal_domain(CausalDomain("causal-channel-declared"))[0])
        self.assertTrue(
            check_causal_domain(
                CausalDomain(
                    "causal-channel-declared",
                    channel_description="modeled classical communication channel",
                )
            )[0]
        )

    def test_missing_gauge_artifact_or_regulator_leaves_candidate_blocked(self) -> None:
        response = ResponseDistribution((ResponsePoint(10.0, 1.0),), family="candidate")
        report = guardrail_response_kernel(
            response,
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("expectation-conserved", accounting_source="density operator source"),
            CoefficientLedger("derived"),
            gauge_or_branch_matching_declared=False,
            artifact_ledger=(),
            regulator_provenance="",
        )

        self.assertFalse(report.allowed)
        self.assertIn("gauge or branch matching declaration is missing", report.reasons)
        self.assertIn("artifact ledger is missing", report.reasons)
        self.assertIn("regulator provenance is missing", report.reasons)

    def test_probability_normalization_dimension_and_non_finite_inputs_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            EnsembleDecomposition(
                (
                    EnsembleComponent(0.6, (1.0, 0.0), "0"),
                    EnsembleComponent(0.6, (0.0, 1.0), "1"),
                )
            )
        with self.assertRaises(ValueError):
            EnsembleDecomposition(
                (
                    EnsembleComponent(0.5, (1.0, 0.0), "0"),
                    EnsembleComponent(0.5, (1.0, 0.0, 0.0), "wide"),
                )
            )
        with self.assertRaises(ValueError):
            EnsembleComponent(0.5, (math.nan, 0.0), "nan")
        with self.assertRaises(ValueError):
            ResponseDistribution((ResponsePoint(1.0, 0.4),))
        with self.assertRaises(ValueError):
            PulsePotentialOperator(((1.0, math.nan), (0.0, 1.0)))
        with self.assertRaises(ValueError):
            DensityMatrixResponseSetup(
                ((0.5, 0.0), (0.0, 0.5)),
                PulsePotentialOperator(((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))),
                clock_frequency_hz=1.0,
                duration_s=1.0,
            )
        with self.assertRaises(ValueError):
            DensityMatrixResponseSetup(
                ((1.2, 0.0), (0.0, -0.2)),
                PulsePotentialOperator(((1.0, 0.0), (0.0, 1.0))),
                clock_frequency_hz=1.0,
                duration_s=1.0,
            )


if __name__ == "__main__":
    unittest.main()
