"""Executable H6S4-Q finite quantum-mediator boundary checks."""

from __future__ import annotations

import math
import unittest

from pulse_model import (
    BranchCarrierDeclaration,
    CausalDomain,
    CoefficientLedger,
    ConservationLedger,
    CouplingDeclaration,
    EnsembleComponent,
    EnsembleDecomposition,
    LocalStochasticPulseSetup,
    MediatorDeclaration,
    NoiseCouplingLedger,
    PulsePotentialOperator,
    QuantumPulseMediatorSetup,
    QuantumPulseReadout,
    QuantumRegulatorLedger,
    RecoveryDeclaration,
    RegulatorLedger,
    StochasticLawDeclaration,
    compare_quantum_mediator_baselines,
    compare_quantum_mediator_responses_for_decompositions,
    quantum_pulse_geometry_response,
    response_marginal_max_difference,
    stochastic_pulse_geometry_response,
)


class QuantumPulseGeometryTests(unittest.TestCase):
    def _identity(self, dimension: int) -> tuple[tuple[complex, ...], ...]:
        return tuple(
            tuple(1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(dimension))
            for row in range(dimension)
        )

    def _permutation_unitary(self, transform) -> tuple[tuple[complex, ...], ...]:
        dimension = 8
        rows = [[0.0 + 0.0j for _ in range(dimension)] for _ in range(dimension)]
        for source in range(2):
            for mediator in range(2):
                for probe in range(2):
                    out_source, out_mediator, out_probe = transform(source, mediator, probe)
                    in_index = (source * 2 + mediator) * 2 + probe
                    out_index = (out_source * 2 + out_mediator) * 2 + out_probe
                    rows[out_index][in_index] = 1.0 + 0.0j
        return tuple(tuple(row) for row in rows)

    def _source_to_mediator_unitary(self) -> tuple[tuple[complex, ...], ...]:
        return self._permutation_unitary(
            lambda source, mediator, probe: (source, mediator ^ source, probe)
        )

    def _mediator_to_probe_unitary(self) -> tuple[tuple[complex, ...], ...]:
        return self._permutation_unitary(
            lambda source, mediator, probe: (source, mediator, probe ^ mediator)
        )

    def _z_decomposition(self) -> EnsembleDecomposition:
        return EnsembleDecomposition(
            (
                EnsembleComponent(0.5, (1.0, 0.0), "0", 10.0),
                EnsembleComponent(0.5, (0.0, 1.0), "1", 11.0),
            ),
            name="E_Z",
        )

    def _x_decomposition(self) -> EnsembleDecomposition:
        scale = 1.0 / math.sqrt(2.0)
        return EnsembleDecomposition(
            (
                EnsembleComponent(0.5, (scale, scale), "+", 10.5),
                EnsembleComponent(0.5, (scale, -scale), "-", 10.5),
            ),
            name="E_X",
        )

    def _setup(
        self,
        *,
        mediator: MediatorDeclaration | None = None,
        source_state=((0.5, 0.0), (0.0, 0.5)),
        source_mediator_unitary=None,
        mediator_probe_unitary=None,
    ) -> QuantumPulseMediatorSetup:
        return QuantumPulseMediatorSetup(
            source_state=source_state,
            mediator=mediator or MediatorDeclaration(2),
            mediator_state=((1.0, 0.0), (0.0, 0.0)),
            probe_clock_state=((1.0, 0.0), (0.0, 0.0)),
            source_mediator_coupling=CouplingDeclaration(
                "source-mediator",
                "source-mediator",
                source_mediator_unitary or self._source_to_mediator_unitary(),
                "g_sm",
            ),
            mediator_probe_coupling=CouplingDeclaration(
                "mediator-probe",
                "mediator-probe",
                mediator_probe_unitary or self._mediator_to_probe_unitary(),
                "g_mc",
            ),
            readout=QuantumPulseReadout(
                (-1.0, 1.0),
                (-1.0, 1.0),
                (-1.0, 1.0),
                pulse_count_values=(10.0, 11.0),
                timing_values_s=(1.0, 2.0),
                source_labels=("s0", "s1"),
                mediator_labels=("m0", "m1"),
                probe_labels=("c0", "c1"),
            ),
        )

    def _report(
        self,
        *,
        setup: QuantumPulseMediatorSetup | None = None,
        branch_carrier: BranchCarrierDeclaration | None = None,
        conservation_ledger: ConservationLedger | None = None,
        coefficient_ledger: CoefficientLedger | None = None,
        recovery: RecoveryDeclaration | None = None,
        standard_quantum_mediator_equivalent: bool = True,
        fixed_observable_distinct_from_known_baselines: bool = False,
    ):
        return quantum_pulse_geometry_response(
            setup or self._setup(),
            branch_carrier or BranchCarrierDeclaration(),
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            conservation_ledger
            or ConservationLedger("branchwise-conserved", accounting_source="closed finite unitary"),
            coefficient_ledger
            or CoefficientLedger("fixed-by-known-limit", coefficient_name="known mediator coupling"),
            QuantumRegulatorLedger(),
            recovery or RecoveryDeclaration(),
            artifact_ledger=("ordinary noise separated", "postselection absent"),
            standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
            fixed_observable_distinct_from_known_baselines=(
                fixed_observable_distinct_from_known_baselines
            ),
        )

    def _h6s4c_response(self):
        setup = LocalStochasticPulseSetup(
            ((0.5, 0.0), (0.0, 0.5)),
            PulsePotentialOperator(((0.0, 0.0), (0.0, 0.1)), label="Phi"),
            clock_frequency_hz=10.0,
            duration_s=1.0,
            speed_of_light_m_per_s=1.0,
        )
        return stochastic_pulse_geometry_response(
            setup,
            StochasticLawDeclaration(),
            NoiseCouplingLedger(),
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("branchwise-conserved", accounting_source="static finite source"),
            CoefficientLedger("fixed-by-known-limit", coefficient_name="weak-field redshift"),
            RegulatorLedger(),
            artifact_ledger=("ordinary instrument noise separated",),
        )

    def test_equivalent_ensemble_decompositions_do_not_change_local_probe_marginal(self) -> None:
        comparison = compare_quantum_mediator_responses_for_decompositions(
            self._z_decomposition(),
            self._x_decomposition(),
            self._setup(),
            BranchCarrierDeclaration(),
            CausalDomain("inside-probe-causal-past", record_exists=True, ledgers_declared=True),
            ConservationLedger("branchwise-conserved", accounting_source="closed finite unitary"),
            CoefficientLedger("fixed-by-known-limit", coefficient_name="known mediator coupling"),
            QuantumRegulatorLedger(),
            RecoveryDeclaration(),
            artifact_ledger=("ordinary noise separated",),
        )

        self.assertTrue(comparison.ensemble_invariance.invariant)
        self.assertTrue(comparison.same_probe_marginal)
        self.assertTrue(comparison.spacelike_remote_basis_safe)
        self.assertAlmostEqual(
            response_marginal_max_difference(
                comparison.first_report.probe_marginal,
                comparison.second_report.probe_marginal,
            ),
            0.0,
        )
        self.assertFalse(comparison.accepted_as_law)

    def test_mediator_can_generate_correlations_without_pointer_branch_label(self) -> None:
        correlated = self._report()
        uncorrelated = self._report(
            setup=self._setup(
                source_mediator_unitary=self._identity(8),
                mediator_probe_unitary=self._identity(8),
            )
        )

        self.assertGreater(correlated.source_probe_covariance, 0.0)
        self.assertGreater(correlated.mediator_probe_covariance, 0.0)
        self.assertEqual(correlated.branch_carrier, "quantum-correlations")
        self.assertAlmostEqual(uncorrelated.source_probe_covariance, 0.0)
        self.assertAlmostEqual(uncorrelated.mediator_probe_covariance, 0.0)
        self.assertFalse(correlated.accepted_as_law)

    def test_density_only_and_h6s4c_baselines_are_reproduced_as_controls(self) -> None:
        report = self._report()
        h6s4c = self._h6s4c_response()
        baseline = compare_quantum_mediator_baselines(
            report,
            density_only_response=h6s4c.density_only_distribution,
            h6s4c_response=h6s4c.response_distribution,
        )

        self.assertAlmostEqual(report.pulse_count_mean, h6s4c.density_only_mean_pulse_count)
        self.assertAlmostEqual(baseline.density_only_mean_difference_pulses, 0.0)
        self.assertAlmostEqual(baseline.h6s4c_mean_difference_pulses, 0.0)
        self.assertAlmostEqual(
            response_marginal_max_difference(report.probe_marginal, h6s4c.response_distribution),
            0.0,
        )
        self.assertTrue(baseline.not_new_prediction)

    def test_missing_mediator_sector_blocks_route(self) -> None:
        report = self._report(
            setup=self._setup(mediator=MediatorDeclaration(2, sector_type="not-declared"))
        )

        self.assertEqual(report.classification.status, "blocked")
        self.assertFalse(report.classification.candidate_ready)
        self.assertIn("mediator sector", report.classification.missing_requirements)

    def test_missing_conservation_ledger_blocks_promotion(self) -> None:
        report = self._report(conservation_ledger=ConservationLedger("not-yet-classified"))

        self.assertEqual(report.classification.status, "blocked")
        self.assertFalse(report.classification.candidate_ready)
        self.assertIn("conservation ledger", report.classification.missing_requirements)
        self.assertFalse(report.accepted_as_law)

    def test_missing_coefficient_provenance_blocks_promotion(self) -> None:
        report = self._report(
            coefficient_ledger=CoefficientLedger("exploratory-only", coefficient_name="free pulse coupling")
        )

        self.assertEqual(report.classification.status, "blocked")
        self.assertFalse(report.classification.candidate_ready)
        self.assertIn(
            "non-exploratory coefficient provenance",
            report.classification.missing_requirements,
        )

    def test_missing_recovery_limit_blocks_law_status(self) -> None:
        report = self._report(
            recovery=RecoveryDeclaration(classical_weak_field_limit_declared=False)
        )

        self.assertEqual(report.classification.status, "blocked")
        self.assertFalse(report.classification.candidate_ready)
        self.assertIn(
            "classical weak-field recovery limit",
            report.classification.missing_requirements,
        )

    def test_arbitrary_ensemble_branch_carrier_is_blocked(self) -> None:
        report = self._report(
            branch_carrier=BranchCarrierDeclaration(
                "arbitrary-ensemble-labels",
                "externally chosen branch labels",
            )
        )

        self.assertEqual(report.classification.status, "blocked")
        self.assertIn(
            "physical branch-information carrier",
            report.classification.missing_requirements,
        )
        self.assertTrue(any("arbitrary ensemble labels" in reason for reason in report.classification.reasons))

    def test_accepted_as_law_remains_false_with_complete_ledgers(self) -> None:
        report = self._report()
        baseline = compare_quantum_mediator_baselines(
            report,
            density_only_response=self._h6s4c_response().density_only_distribution,
            h6s4c_response=self._h6s4c_response().response_distribution,
        )

        self.assertTrue(report.classification.candidate_ready)
        self.assertFalse(report.accepted_as_law)
        self.assertFalse(report.classification.accepted_as_law)
        self.assertFalse(baseline.accepted_as_law)

    def test_final_classification_is_not_new_prediction_without_fixed_difference(self) -> None:
        report = self._report(standard_quantum_mediator_equivalent=False)
        baseline = compare_quantum_mediator_baselines(
            report,
            density_only_response=self._h6s4c_response().density_only_distribution,
            h6s4c_response=self._h6s4c_response().response_distribution,
            standard_quantum_mediator_equivalent=False,
        )

        self.assertEqual(report.classification.status, "diagnostic-only")
        self.assertFalse(report.classification.fixed_observable_distinct_from_known_baselines)
        self.assertTrue(baseline.not_new_prediction)
        self.assertNotEqual(report.classification.status, "controlled-modification-candidate")

    def test_standard_quantum_mediator_equivalence_is_conditional_not_new_physics(self) -> None:
        report = self._report(standard_quantum_mediator_equivalent=True)
        baseline = compare_quantum_mediator_baselines(
            report,
            density_only_response=self._h6s4c_response().density_only_distribution,
            h6s4c_response=self._h6s4c_response().response_distribution,
            standard_quantum_mediator_equivalent=True,
        )

        self.assertEqual(report.classification.status, "conditional-derivation-candidate")
        self.assertTrue(report.classification.standard_quantum_mediator_equivalent)
        self.assertTrue(baseline.not_new_prediction)
        self.assertTrue(any("standard quantum mediator equivalence" in reason for reason in baseline.reasons))
        self.assertFalse(report.accepted_as_law)


if __name__ == "__main__":
    unittest.main()
