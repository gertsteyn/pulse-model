"""Executable H6S4-C stochastic pulse-geometry boundary checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    CausalDomain,
    CoefficientLedger,
    ConservationLedger,
    EnsembleComponent,
    EnsembleDecomposition,
    LocalStochasticPulseSetup,
    NoiseCouplingLedger,
    PointerRecord,
    PulsePotentialOperator,
    RegulatorLedger,
    StochasticLawDeclaration,
    branch_variance_from_response,
    compare_stochastic_baselines,
    compare_stochastic_responses_for_decompositions,
    invalid_ensemble_branch_response,
    pointer_record_branch_response,
    response_marginal_max_difference,
    stochastic_excess_variance,
    stochastic_pulse_geometry_response,
)


class StochasticPulseGeometryTests(unittest.TestCase):
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

    def _setup(self, *, ordinary_noise: float = 0.0) -> LocalStochasticPulseSetup:
        return LocalStochasticPulseSetup(
            ((0.5, 0.0), (0.0, 0.5)),
            self._potential_operator(),
            clock_frequency_hz=2.0,
            duration_s=5.0,
            ordinary_instrument_noise_variance_pulses2=ordinary_noise,
            speed_of_light_m_per_s=10.0,
        )

    def _complete_report(
        self,
        *,
        ordinary_noise: float = 0.0,
        causal_domain: CausalDomain | None = None,
        conservation_ledger: ConservationLedger | None = None,
        coefficient_ledger: CoefficientLedger | None = None,
        coupling_ledger: NoiseCouplingLedger | None = None,
        regulator_ledger: RegulatorLedger | None = None,
    ):
        return stochastic_pulse_geometry_response(
            self._setup(ordinary_noise=ordinary_noise),
            StochasticLawDeclaration(),
            coupling_ledger or NoiseCouplingLedger(),
            causal_domain
            or CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            conservation_ledger
            or ConservationLedger("branchwise-conserved", accounting_source="static finite source"),
            coefficient_ledger
            or CoefficientLedger("fixed-by-known-limit", coefficient_name="weak-field redshift"),
            regulator_ledger or RegulatorLedger(),
            artifact_ledger=("ordinary instrument noise separated",),
        )

    def _complete_decomposition_comparison(
        self,
        *,
        causal_domain: CausalDomain | None = None,
        coupling_ledger: NoiseCouplingLedger | None = None,
    ):
        return compare_stochastic_responses_for_decompositions(
            self._z_decomposition(),
            self._x_decomposition(),
            self._potential_operator(),
            2.0,
            5.0,
            StochasticLawDeclaration(),
            coupling_ledger or NoiseCouplingLedger(),
            causal_domain
            or CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("branchwise-conserved", accounting_source="static finite source"),
            CoefficientLedger("fixed-by-known-limit", coefficient_name="weak-field redshift"),
            RegulatorLedger(),
            artifact_ledger=("ordinary instrument noise separated",),
            speed_of_light_m_per_s=10.0,
        )

    def test_equivalent_z_and_x_decompositions_give_same_stochastic_response(self) -> None:
        comparison = self._complete_decomposition_comparison()

        self.assertTrue(comparison.ensemble_invariance.invariant)
        self.assertTrue(comparison.same_stochastic_response)
        self.assertTrue(comparison.spacelike_remote_basis_safe)
        self.assertAlmostEqual(
            response_marginal_max_difference(
                comparison.first_report.response_distribution,
                comparison.second_report.response_distribution,
            ),
            0.0,
        )
        self.assertFalse(comparison.no_free_branch_variance_report.diagnostic_failure)

    def test_ordinary_instrument_noise_remains_separate_from_geometry_noise(self) -> None:
        report = self._complete_report(ordinary_noise=4.0)

        self.assertAlmostEqual(report.excess_pulse_count_variance_pulses2, 0.01)
        self.assertAlmostEqual(report.ordinary_instrument_noise_variance_pulses2, 4.0)
        self.assertAlmostEqual(report.observed_variance_pulses2, 4.01)
        self.assertAlmostEqual(stochastic_excess_variance(report), 0.01)

    def test_missing_coefficient_provenance_blocks_candidate_status(self) -> None:
        report = self._complete_report(
            coefficient_ledger=CoefficientLedger("exploratory-only", coefficient_name="free amplitude")
        )

        self.assertEqual(report.classification.status, "blocked")
        self.assertFalse(report.classification.candidate_ready)
        self.assertIn(
            "non-exploratory coefficient provenance",
            report.classification.missing_requirements,
        )
        self.assertFalse(report.accepted_as_law)

    def test_missing_conservation_ledger_blocks_candidate_status(self) -> None:
        report = self._complete_report(
            conservation_ledger=ConservationLedger("not-yet-classified")
        )

        self.assertEqual(report.classification.status, "blocked")
        self.assertFalse(report.classification.candidate_ready)
        self.assertIn("conservation ledger", report.classification.missing_requirements)

    def test_spacelike_remote_basis_change_cannot_change_probe_marginal(self) -> None:
        comparison = self._complete_decomposition_comparison(
            causal_domain=CausalDomain("spacelike-remote-choice")
        )

        self.assertTrue(comparison.same_stochastic_response)
        self.assertTrue(comparison.spacelike_remote_basis_safe)
        self.assertAlmostEqual(comparison.ensemble_invariance.max_marginal_difference, 0.0)
        self.assertFalse(comparison.first_report.accepted_as_law)
        self.assertFalse(comparison.second_report.accepted_as_law)

    def test_candidate_produces_fixed_excess_variance_and_is_not_law(self) -> None:
        report = self._complete_report()

        self.assertEqual(report.classification.status, "controlled-modification-candidate")
        self.assertTrue(report.classification.candidate_ready)
        self.assertAlmostEqual(report.excess_pulse_count_variance_pulses2, 0.01)
        self.assertGreater(report.timing_jitter_variance_s2, 0.0)
        self.assertFalse(report.accepted_as_law)
        self.assertFalse(report.classification.accepted_as_law)

    def test_accepted_as_law_remains_false_with_complete_ledgers(self) -> None:
        report = self._complete_report()
        baseline = compare_stochastic_baselines(
            report,
            no_free_branch_variance_report=self._complete_decomposition_comparison().no_free_branch_variance_report,
        )

        self.assertTrue(report.classification.candidate_ready)
        self.assertFalse(report.accepted_as_law)
        self.assertFalse(baseline.accepted_as_law)

    def test_invalid_ensemble_branch_response_remains_rejected_baseline(self) -> None:
        comparison = self._complete_decomposition_comparison()
        invalid = invalid_ensemble_branch_response(self._z_decomposition(pulse_counts=(9.0, 11.0)))
        baseline = compare_stochastic_baselines(
            comparison.first_report,
            invalid_ensemble_response=invalid,
            no_free_branch_variance_report=comparison.no_free_branch_variance_report,
        )

        self.assertAlmostEqual(branch_variance_from_response(invalid), 1.0)
        self.assertTrue(baseline.invalid_ensemble_rejected)
        self.assertEqual(baseline.route_failure_classification, "controlled-modification-candidate")
        self.assertFalse(baseline.accepted_as_law)

    def test_pointer_record_variance_is_only_baseline_comparator(self) -> None:
        comparison = self._complete_decomposition_comparison()
        pointer = pointer_record_branch_response(
            PointerRecord(
                pointer_basis=("0", "1"),
                probabilities=(0.5, 0.5),
                pulse_counts=(9.0, 11.0),
                local_record_exists=True,
                causal_status="inside-probe-causal-past",
            )
        )
        baseline = compare_stochastic_baselines(
            comparison.first_report,
            pointer_record_response=pointer,
            no_free_branch_variance_report=comparison.no_free_branch_variance_report,
        )

        self.assertAlmostEqual(branch_variance_from_response(pointer), 1.0)
        self.assertTrue(pointer.diagnostic_only)
        self.assertFalse(pointer.accepted_as_law)
        self.assertTrue(baseline.pointer_record_is_comparator_only)
        self.assertFalse(baseline.accepted_as_law)


if __name__ == "__main__":
    unittest.main()
