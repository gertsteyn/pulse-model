"""Deterministic H6S4-Q finite quantum-mediator helpers.

The API evaluates a declared finite source/mediator/probe setup. It returns
exact joint records, local probe marginals, and simple correlation diagnostics.
It does not sample, choose ensemble branch labels, or promote the route to an
accepted law.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, replace
from itertools import combinations
import math

from .causal_pulse_response import (
    CausalDomain,
    CoefficientLedger,
    ConservationLedger,
    EnsembleDecomposition,
    EnsembleInvarianceReport,
    ResponseDistribution,
    ResponsePoint,
    check_causal_domain,
    check_ensemble_invariance,
    ensemble_density_matrix,
    response_marginal_max_difference,
)


Matrix = tuple[tuple[complex, ...], ...]

MEDIATOR_SECTOR_LABELS = frozenset(
    {
        "finite-quantum-mediator",
        "non-classical-geometry",
        "known-framework-stand-in",
        "not-declared",
    }
)
BRANCH_CARRIER_LABELS = frozenset(
    {
        "quantum-correlations",
        "local-record",
        "causal-channel",
        "shared-future-comparison",
        "arbitrary-ensemble-labels",
        "not-declared",
    }
)
QUANTUM_REGULATOR_LABELS = frozenset(
    {
        "none-required",
        "finite-truncation",
        "finite-operator",
        "known-framework-cutoff",
        "exploratory-only",
        "not-declared",
        "fit-after-observation rejected",
    }
)
QUANTUM_MEDIATOR_STATUS_LABELS = frozenset(
    {
        "controlled-modification-candidate",
        "conditional-derivation-candidate",
        "diagnostic-only",
        "blocked",
        "clean-no-go-candidate",
    }
)
COUPLING_ACTS_ON_LABELS = frozenset({"source-mediator", "mediator-probe"})


@dataclass(frozen=True)
class MediatorDeclaration:
    """Declared finite mediator or non-classical geometry sector."""

    dimension: int
    sector_type: str = "finite-quantum-mediator"
    state_space_label: str = "finite mediator"
    basis_status: str = "declared finite comparator basis"

    def __post_init__(self) -> None:
        _require_positive_int("mediator dimension", self.dimension)
        _require_label("sector_type", self.sector_type, MEDIATOR_SECTOR_LABELS)
        _require_nonempty_string("state_space_label", self.state_space_label)
        _require_nonempty_string("basis_status", self.basis_status)


@dataclass(frozen=True)
class CouplingDeclaration:
    """Declared finite full-system unitary for one coupling stage."""

    name: str
    acts_on: str
    unitary_matrix: Sequence[Sequence[complex]]
    coefficient_name: str
    coefficient_value: float | None = None

    def __post_init__(self) -> None:
        _require_nonempty_string("coupling name", self.name)
        _require_label("acts_on", self.acts_on, COUPLING_ACTS_ON_LABELS)
        matrix = _validated_square_matrix(self.unitary_matrix, "unitary_matrix")
        _require_nonempty_string("coefficient_name", self.coefficient_name)
        if self.coefficient_value is not None:
            _require_finite_real("coefficient_value", self.coefficient_value)
        object.__setattr__(self, "unitary_matrix", matrix)

    @property
    def dimension(self) -> int:
        return len(self.unitary_matrix)


@dataclass(frozen=True)
class BranchCarrierDeclaration:
    """How H6S4-Q carries branch information without arbitrary labels."""

    carrier: str = "quantum-correlations"
    description: str = "declared source-mediator-probe quantum correlations"

    def __post_init__(self) -> None:
        _require_label("branch carrier", self.carrier, BRANCH_CARRIER_LABELS)
        _require_nonempty_string("branch carrier description", self.description)


@dataclass(frozen=True)
class QuantumRegulatorLedger:
    """Regulator or truncation provenance for H6S4-Q."""

    provenance: str = "finite-truncation"
    description: str = "finite source/mediator/probe Hilbert-space truncation"

    def __post_init__(self) -> None:
        _require_label("regulator provenance", self.provenance, QUANTUM_REGULATOR_LABELS)
        _require_nonempty_string("regulator description", self.description)


@dataclass(frozen=True)
class RecoveryDeclaration:
    """Declared recovery of the accepted weak-field baseline."""

    classical_weak_field_limit_declared: bool = True
    density_only_limit_declared: bool = True
    framework: str = "standard finite quantum mediator weak-field limit"

    def __post_init__(self) -> None:
        _require_nonempty_string("recovery framework", self.framework)


@dataclass(frozen=True)
class QuantumPulseReadout:
    """Finite source, mediator, probe, pulse-count, and timing readout maps."""

    source_values: Sequence[float]
    mediator_values: Sequence[float]
    probe_values: Sequence[float]
    pulse_count_values: Sequence[float] | None = None
    timing_values_s: Sequence[float] | None = None
    source_labels: Sequence[str] = ()
    mediator_labels: Sequence[str] = ()
    probe_labels: Sequence[str] = ()

    def __post_init__(self) -> None:
        source_values = _validated_real_tuple("source readout value", self.source_values)
        mediator_values = _validated_real_tuple("mediator readout value", self.mediator_values)
        probe_values = _validated_real_tuple("probe readout value", self.probe_values)
        pulse_count_values = (
            probe_values
            if self.pulse_count_values is None
            else _validated_real_tuple("pulse-count readout value", self.pulse_count_values)
        )
        timing_values_s = (
            None
            if self.timing_values_s is None
            else _validated_real_tuple("timing readout value", self.timing_values_s)
        )
        object.__setattr__(self, "source_values", source_values)
        object.__setattr__(self, "mediator_values", mediator_values)
        object.__setattr__(self, "probe_values", probe_values)
        object.__setattr__(self, "pulse_count_values", pulse_count_values)
        object.__setattr__(self, "timing_values_s", timing_values_s)
        object.__setattr__(
            self,
            "source_labels",
            _validated_labels(self.source_labels, len(source_values), "s"),
        )
        object.__setattr__(
            self,
            "mediator_labels",
            _validated_labels(self.mediator_labels, len(mediator_values), "m"),
        )
        object.__setattr__(
            self,
            "probe_labels",
            _validated_labels(self.probe_labels, len(probe_values), "c"),
        )


@dataclass(frozen=True)
class QuantumPulseMediatorSetup:
    """Finite H6S4-Q source/mediator/probe candidate setup."""

    source_state: Sequence[Sequence[complex]]
    mediator: MediatorDeclaration
    mediator_state: Sequence[Sequence[complex]]
    probe_clock_state: Sequence[Sequence[complex]]
    source_mediator_coupling: CouplingDeclaration
    mediator_probe_coupling: CouplingDeclaration
    readout: QuantumPulseReadout

    def __post_init__(self) -> None:
        source_state = _validated_density_matrix(self.source_state, "source_state")
        mediator_state = _validated_density_matrix(self.mediator_state, "mediator_state")
        probe_state = _validated_density_matrix(self.probe_clock_state, "probe_clock_state")
        source_dimension = len(source_state)
        mediator_dimension = len(mediator_state)
        probe_dimension = len(probe_state)
        if mediator_dimension != self.mediator.dimension:
            raise ValueError("mediator declaration dimension must match mediator_state")
        if self.source_mediator_coupling.acts_on != "source-mediator":
            raise ValueError("source_mediator_coupling must act on source-mediator")
        if self.mediator_probe_coupling.acts_on != "mediator-probe":
            raise ValueError("mediator_probe_coupling must act on mediator-probe")
        full_dimension = source_dimension * mediator_dimension * probe_dimension
        _require_full_unitary_dimension(
            self.source_mediator_coupling,
            full_dimension,
            "source_mediator_coupling",
        )
        _require_full_unitary_dimension(
            self.mediator_probe_coupling,
            full_dimension,
            "mediator_probe_coupling",
        )
        _require_readout_length(self.readout.source_values, source_dimension, "source readout")
        _require_readout_length(self.readout.mediator_values, mediator_dimension, "mediator readout")
        _require_readout_length(self.readout.probe_values, probe_dimension, "probe readout")
        _require_readout_length(self.readout.pulse_count_values, probe_dimension, "pulse-count readout")
        if self.readout.timing_values_s is not None:
            _require_readout_length(self.readout.timing_values_s, probe_dimension, "timing readout")
        object.__setattr__(self, "source_state", source_state)
        object.__setattr__(self, "mediator_state", mediator_state)
        object.__setattr__(self, "probe_clock_state", probe_state)

    @property
    def source_dimension(self) -> int:
        return len(self.source_state)

    @property
    def mediator_dimension(self) -> int:
        return len(self.mediator_state)

    @property
    def probe_dimension(self) -> int:
        return len(self.probe_clock_state)

    @property
    def full_dimension(self) -> int:
        return self.source_dimension * self.mediator_dimension * self.probe_dimension


@dataclass(frozen=True)
class JointRecordPoint:
    """One finite source/mediator/probe record point."""

    source_label: str
    mediator_label: str
    probe_label: str
    source_value: float
    mediator_value: float
    probe_value: float
    pulse_count: float
    probability: float

    def __post_init__(self) -> None:
        _require_nonempty_string("source_label", self.source_label)
        _require_nonempty_string("mediator_label", self.mediator_label)
        _require_nonempty_string("probe_label", self.probe_label)
        _require_finite_real("source_value", self.source_value)
        _require_finite_real("mediator_value", self.mediator_value)
        _require_finite_real("probe_value", self.probe_value)
        _require_finite_real("pulse_count", self.pulse_count)
        _require_probability("probability", self.probability)


@dataclass(frozen=True)
class MarginalRecordPoint:
    """One finite marginal record point."""

    label: str
    value: float
    probability: float

    def __post_init__(self) -> None:
        _require_nonempty_string("label", self.label)
        _require_finite_real("value", self.value)
        _require_probability("probability", self.probability)


@dataclass(frozen=True)
class ConditionalProbeShift:
    """Probe shift conditioned on a declared mediator record."""

    mediator_label: str
    mediator_probability: float
    conditional_probe_mean: float
    unconditional_probe_mean: float
    shift: float

    def __post_init__(self) -> None:
        _require_nonempty_string("mediator_label", self.mediator_label)
        _require_probability("mediator_probability", self.mediator_probability)
        _require_finite_real("conditional_probe_mean", self.conditional_probe_mean)
        _require_finite_real("unconditional_probe_mean", self.unconditional_probe_mean)
        _require_finite_real("shift", self.shift)


@dataclass(frozen=True)
class QuantumMediatorRouteClassification:
    """Route status after H6S4-Q ledgers are applied."""

    status: str
    candidate_ready: bool
    diagnostic_only: bool
    accepted_as_law: bool
    fixed_observable_distinct_from_known_baselines: bool
    standard_quantum_mediator_equivalent: bool
    reasons: tuple[str, ...]
    missing_requirements: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_label("status", self.status, QUANTUM_MEDIATOR_STATUS_LABELS)
        for reason in self.reasons:
            _require_nonempty_string("classification reason", reason)
        for requirement in self.missing_requirements:
            _require_nonempty_string("missing requirement", requirement)
        if self.accepted_as_law:
            raise ValueError("H6S4-Q API cannot mark the route accepted as law before final verdict")


@dataclass(frozen=True)
class QuantumPulseGeometryReport:
    """Deterministic finite response report for H6S4-Q."""

    final_state: Matrix
    joint_distribution: tuple[JointRecordPoint, ...]
    source_marginal: tuple[MarginalRecordPoint, ...]
    mediator_marginal: tuple[MarginalRecordPoint, ...]
    probe_marginal: ResponseDistribution
    classification: QuantumMediatorRouteClassification
    source_probe_covariance: float
    mediator_source_covariance: float
    mediator_probe_covariance: float
    pulse_count_mean: float
    pulse_count_variance: float
    conditional_probe_shifts: tuple[ConditionalProbeShift, ...]
    witness_value: float | None
    initial_probe_visibility: float | None
    final_probe_visibility: float | None
    visibility_difference: float | None
    timing_mean_s: float | None
    source_timing_covariance: float | None
    branch_carrier: str
    causal_status: str
    conservation_status: str
    coefficient_provenance: str
    regulator_provenance: str
    recovery_framework: str
    artifact_ledger: tuple[str, ...]
    diagnostic_only: bool
    accepted_as_law: bool


@dataclass(frozen=True)
class QuantumMediatorEnsembleComparisonReport:
    """Remote-basis/decomposition invariance report for H6S4-Q."""

    first_report: QuantumPulseGeometryReport
    second_report: QuantumPulseGeometryReport
    ensemble_invariance: EnsembleInvarianceReport
    same_probe_marginal: bool
    spacelike_remote_basis_safe: bool
    accepted_as_law: bool


@dataclass(frozen=True)
class QuantumMediatorBaselineComparisonReport:
    """Baseline comparator report for the H6S4-Q route."""

    route_classification: str
    density_only_mean_difference_pulses: float | None
    h6s4c_mean_difference_pulses: float | None
    fixed_background_marginal_difference: float | None
    standard_quantum_mediator_equivalent: bool
    fixed_candidate_difference: bool
    not_new_prediction: bool
    reasons: tuple[str, ...]
    accepted_as_law: bool

    def __post_init__(self) -> None:
        _require_label("route_classification", self.route_classification, QUANTUM_MEDIATOR_STATUS_LABELS)
        for reason in self.reasons:
            _require_nonempty_string("baseline reason", reason)
        if self.accepted_as_law:
            raise ValueError("baseline report cannot accept H6S4-Q as law before final verdict")


def quantum_pulse_geometry_response(
    setup: QuantumPulseMediatorSetup,
    branch_carrier: BranchCarrierDeclaration,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    regulator_ledger: QuantumRegulatorLedger,
    recovery: RecoveryDeclaration,
    *,
    artifact_ledger: Sequence[str],
    entanglement_witness_matrix: Sequence[Sequence[complex]] | None = None,
    fixed_observable_distinct_from_known_baselines: bool = False,
    standard_quantum_mediator_equivalent: bool = True,
) -> QuantumPulseGeometryReport:
    """Return the deterministic H6S4-Q finite mediator response report."""

    artifacts = _validated_artifact_ledger(artifact_ledger)
    classification = classify_quantum_mediator_candidate(
        setup.mediator,
        branch_carrier,
        causal_domain,
        conservation_ledger,
        coefficient_ledger,
        regulator_ledger,
        recovery,
        artifact_ledger=artifacts,
        fixed_observable_distinct_from_known_baselines=fixed_observable_distinct_from_known_baselines,
        standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
    )

    initial_state = _kronecker_product(
        _kronecker_product(setup.source_state, setup.mediator_state),
        setup.probe_clock_state,
    )
    after_source_mediator = _unitary_evolve(
        setup.source_mediator_coupling.unitary_matrix,
        initial_state,
    )
    final_state = _unitary_evolve(
        setup.mediator_probe_coupling.unitary_matrix,
        after_source_mediator,
    )
    _require_density_trace_one(final_state, "final_state")

    joint_distribution = _joint_record_distribution(setup, final_state)
    source_marginal = _source_marginal(setup, joint_distribution)
    mediator_marginal = _mediator_marginal(setup, joint_distribution)
    probe_marginal = _probe_response_distribution(setup, joint_distribution)

    source_mean = _marginal_mean(source_marginal)
    mediator_mean = _marginal_mean(mediator_marginal)
    probe_readout_mean = _probe_readout_mean(joint_distribution)
    source_probe_covariance = _joint_covariance(
        joint_distribution,
        first="source",
        first_mean=source_mean,
        second="probe",
        second_mean=probe_readout_mean,
    )
    mediator_source_covariance = _joint_covariance(
        joint_distribution,
        first="source",
        first_mean=source_mean,
        second="mediator",
        second_mean=mediator_mean,
    )
    mediator_probe_covariance = _joint_covariance(
        joint_distribution,
        first="mediator",
        first_mean=mediator_mean,
        second="probe",
        second_mean=probe_readout_mean,
    )
    pulse_count_mean, pulse_count_variance = _pulse_count_moments(joint_distribution)
    conditional_probe_shifts = _conditional_probe_shifts(
        setup,
        joint_distribution,
        unconditional_probe_mean=probe_readout_mean,
    )
    witness_value = (
        None
        if entanglement_witness_matrix is None
        else _witness_value(entanglement_witness_matrix, final_state)
    )
    probe_final_state = _partial_trace_probe(
        final_state,
        setup.source_dimension,
        setup.mediator_dimension,
        setup.probe_dimension,
    )
    initial_visibility = _probe_visibility(setup.probe_clock_state)
    final_visibility = _probe_visibility(probe_final_state)
    visibility_difference = (
        None
        if initial_visibility is None or final_visibility is None
        else final_visibility - initial_visibility
    )
    timing_mean_s, source_timing_covariance = _timing_observables(
        setup,
        joint_distribution,
        source_mean=source_mean,
    )

    return QuantumPulseGeometryReport(
        final_state=final_state,
        joint_distribution=joint_distribution,
        source_marginal=source_marginal,
        mediator_marginal=mediator_marginal,
        probe_marginal=probe_marginal,
        classification=classification,
        source_probe_covariance=source_probe_covariance,
        mediator_source_covariance=mediator_source_covariance,
        mediator_probe_covariance=mediator_probe_covariance,
        pulse_count_mean=pulse_count_mean,
        pulse_count_variance=pulse_count_variance,
        conditional_probe_shifts=conditional_probe_shifts,
        witness_value=witness_value,
        initial_probe_visibility=initial_visibility,
        final_probe_visibility=final_visibility,
        visibility_difference=visibility_difference,
        timing_mean_s=timing_mean_s,
        source_timing_covariance=source_timing_covariance,
        branch_carrier=branch_carrier.carrier,
        causal_status=causal_domain.status,
        conservation_status=conservation_ledger.status,
        coefficient_provenance=coefficient_ledger.provenance,
        regulator_provenance=regulator_ledger.provenance,
        recovery_framework=recovery.framework,
        artifact_ledger=artifacts,
        diagnostic_only=classification.diagnostic_only,
        accepted_as_law=False,
    )


def classify_quantum_mediator_candidate(
    mediator: MediatorDeclaration,
    branch_carrier: BranchCarrierDeclaration,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    regulator_ledger: QuantumRegulatorLedger,
    recovery: RecoveryDeclaration,
    *,
    artifact_ledger: Sequence[str],
    fixed_observable_distinct_from_known_baselines: bool = False,
    standard_quantum_mediator_equivalent: bool = True,
) -> QuantumMediatorRouteClassification:
    """Classify whether the finite H6S4-Q route has complete ledgers."""

    artifacts = _validated_artifact_ledger(artifact_ledger)
    missing: list[str] = []
    reasons: list[str] = []

    if mediator.sector_type == "not-declared":
        missing.append("mediator sector")
    if branch_carrier.carrier in {"not-declared", "arbitrary-ensemble-labels"}:
        missing.append("physical branch-information carrier")
        reasons.append("arbitrary ensemble labels are not admissible branch-information carriers")

    causal_allowed, causal_reason = check_causal_domain(causal_domain)
    if not causal_allowed:
        missing.append("causal support")
        reasons.append(causal_reason)

    if conservation_ledger.status == "not-yet-classified":
        missing.append("conservation ledger")
    elif conservation_ledger.status == "inconsistent-rejected":
        reasons.append("conservation ledger is inconsistent-rejected")
    elif not conservation_ledger.accounting_source:
        missing.append("conservation accounting source")
    if (
        conservation_ledger.status == "conservation-requires-environment"
        and not conservation_ledger.environment_or_collapse_sector
    ):
        missing.append("environment or mediator conservation sector")

    if coefficient_ledger.provenance == "fit-after-observation rejected":
        reasons.append("fit-after-observation coefficient provenance is rejected")
    elif coefficient_ledger.provenance == "exploratory-only":
        missing.append("non-exploratory coefficient provenance")

    if regulator_ledger.provenance in {"not-declared", "fit-after-observation rejected"}:
        missing.append("regulator provenance")
    elif regulator_ledger.provenance == "exploratory-only":
        missing.append("non-exploratory regulator provenance")

    if not recovery.classical_weak_field_limit_declared:
        missing.append("classical weak-field recovery limit")
    if not recovery.density_only_limit_declared:
        missing.append("density-only recovery limit")
    if not artifacts:
        missing.append("artifact ledger")

    if reasons or missing:
        all_reasons = tuple(reasons + [f"missing {item}" for item in missing])
        return QuantumMediatorRouteClassification(
            status="blocked",
            candidate_ready=False,
            diagnostic_only=True,
            accepted_as_law=False,
            fixed_observable_distinct_from_known_baselines=False,
            standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
            reasons=all_reasons,
            missing_requirements=tuple(missing),
        )

    if fixed_observable_distinct_from_known_baselines and not standard_quantum_mediator_equivalent:
        status = "controlled-modification-candidate"
        reason = "complete ledgers and fixed observable distinct from known baselines"
    elif standard_quantum_mediator_equivalent:
        status = "conditional-derivation-candidate"
        reason = "finite route is equivalent to a known quantum mediator framework"
    else:
        status = "diagnostic-only"
        reason = "finite route is a comparator without a fixed baseline-distinct observable"

    return QuantumMediatorRouteClassification(
        status=status,
        candidate_ready=True,
        diagnostic_only=status == "diagnostic-only",
        accepted_as_law=False,
        fixed_observable_distinct_from_known_baselines=(
            fixed_observable_distinct_from_known_baselines
        ),
        standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
        reasons=(reason, "final H6S4-Q verdict still controls law status"),
        missing_requirements=(),
    )


def compare_quantum_mediator_responses_for_decompositions(
    first_decomposition: EnsembleDecomposition,
    second_decomposition: EnsembleDecomposition,
    template_setup: QuantumPulseMediatorSetup,
    branch_carrier: BranchCarrierDeclaration,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    regulator_ledger: QuantumRegulatorLedger,
    recovery: RecoveryDeclaration,
    *,
    artifact_ledger: Sequence[str],
    fixed_observable_distinct_from_known_baselines: bool = False,
    standard_quantum_mediator_equivalent: bool = True,
) -> QuantumMediatorEnsembleComparisonReport:
    """Compare H6S4-Q probe marginals for two ensemble descriptions."""

    first_setup = replace(template_setup, source_state=ensemble_density_matrix(first_decomposition))
    second_setup = replace(template_setup, source_state=ensemble_density_matrix(second_decomposition))
    first_report = quantum_pulse_geometry_response(
        first_setup,
        branch_carrier,
        causal_domain,
        conservation_ledger,
        coefficient_ledger,
        regulator_ledger,
        recovery,
        artifact_ledger=artifact_ledger,
        fixed_observable_distinct_from_known_baselines=fixed_observable_distinct_from_known_baselines,
        standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
    )
    second_report = quantum_pulse_geometry_response(
        second_setup,
        branch_carrier,
        causal_domain,
        conservation_ledger,
        coefficient_ledger,
        regulator_ledger,
        recovery,
        artifact_ledger=artifact_ledger,
        fixed_observable_distinct_from_known_baselines=fixed_observable_distinct_from_known_baselines,
        standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
    )
    invariance = check_ensemble_invariance(
        first_decomposition,
        second_decomposition,
        first_report.probe_marginal,
        second_report.probe_marginal,
    )
    same_probe_marginal = (
        response_marginal_max_difference(first_report.probe_marginal, second_report.probe_marginal)
        <= 1.0e-12
    )
    return QuantumMediatorEnsembleComparisonReport(
        first_report=first_report,
        second_report=second_report,
        ensemble_invariance=invariance,
        same_probe_marginal=same_probe_marginal,
        spacelike_remote_basis_safe=same_probe_marginal and invariance.invariant,
        accepted_as_law=False,
    )


def compare_quantum_mediator_baselines(
    report: QuantumPulseGeometryReport,
    *,
    density_only_response: ResponseDistribution | None = None,
    h6s4c_response: ResponseDistribution | None = None,
    fixed_background_response: ResponseDistribution | None = None,
    standard_quantum_mediator_equivalent: bool = True,
) -> QuantumMediatorBaselineComparisonReport:
    """Compare the H6S4-Q report against declared baseline marginals."""

    report_mean = _response_mean(report.probe_marginal)
    density_difference = (
        None
        if density_only_response is None
        else abs(report_mean - _response_mean(density_only_response))
    )
    h6s4c_difference = (
        None
        if h6s4c_response is None
        else abs(report_mean - _response_mean(h6s4c_response))
    )
    fixed_background_difference = (
        None
        if fixed_background_response is None
        else response_marginal_max_difference(report.probe_marginal, fixed_background_response)
    )
    fixed_candidate_difference = (
        report.classification.fixed_observable_distinct_from_known_baselines
        and not standard_quantum_mediator_equivalent
    )
    reasons = list(report.classification.reasons)
    if density_only_response is None:
        reasons.append("density-only baseline response not supplied")
    if h6s4c_response is None:
        reasons.append("H6S4-C baseline response not supplied")
    if standard_quantum_mediator_equivalent:
        reasons.append("standard quantum mediator equivalence blocks new-physics promotion")
    if not fixed_candidate_difference:
        reasons.append("no fixed observable distinct from known baselines")

    return QuantumMediatorBaselineComparisonReport(
        route_classification=report.classification.status,
        density_only_mean_difference_pulses=density_difference,
        h6s4c_mean_difference_pulses=h6s4c_difference,
        fixed_background_marginal_difference=fixed_background_difference,
        standard_quantum_mediator_equivalent=standard_quantum_mediator_equivalent,
        fixed_candidate_difference=fixed_candidate_difference,
        not_new_prediction=not fixed_candidate_difference,
        reasons=tuple(reasons),
        accepted_as_law=False,
    )


def _unitary_evolve(unitary: Matrix, density_matrix: Matrix) -> Matrix:
    return _matrix_multiply(
        _matrix_multiply(unitary, density_matrix),
        _conjugate_transpose(unitary),
    )


def _joint_record_distribution(
    setup: QuantumPulseMediatorSetup,
    final_state: Matrix,
) -> tuple[JointRecordPoint, ...]:
    points: list[JointRecordPoint] = []
    for source_index in range(setup.source_dimension):
        for mediator_index in range(setup.mediator_dimension):
            for probe_index in range(setup.probe_dimension):
                index = _joint_index(
                    source_index,
                    mediator_index,
                    probe_index,
                    setup.mediator_dimension,
                    setup.probe_dimension,
                )
                probability = _probability_from_diagonal(final_state[index][index])
                if probability <= 0.0:
                    continue
                points.append(
                    JointRecordPoint(
                        source_label=setup.readout.source_labels[source_index],
                        mediator_label=setup.readout.mediator_labels[mediator_index],
                        probe_label=setup.readout.probe_labels[probe_index],
                        source_value=setup.readout.source_values[source_index],
                        mediator_value=setup.readout.mediator_values[mediator_index],
                        probe_value=setup.readout.probe_values[probe_index],
                        pulse_count=setup.readout.pulse_count_values[probe_index],
                        probability=probability,
                    )
                )
    total_probability = math.fsum(point.probability for point in points)
    if not math.isclose(total_probability, 1.0, rel_tol=1.0e-10, abs_tol=1.0e-10):
        raise ValueError("joint record probabilities must sum to 1")
    return tuple(points)


def _source_marginal(
    setup: QuantumPulseMediatorSetup,
    joint_distribution: Sequence[JointRecordPoint],
) -> tuple[MarginalRecordPoint, ...]:
    return tuple(
        MarginalRecordPoint(
            setup.readout.source_labels[index],
            setup.readout.source_values[index],
            math.fsum(point.probability for point in joint_distribution if point.source_label == setup.readout.source_labels[index]),
        )
        for index in range(setup.source_dimension)
    )


def _mediator_marginal(
    setup: QuantumPulseMediatorSetup,
    joint_distribution: Sequence[JointRecordPoint],
) -> tuple[MarginalRecordPoint, ...]:
    return tuple(
        MarginalRecordPoint(
            setup.readout.mediator_labels[index],
            setup.readout.mediator_values[index],
            math.fsum(
                point.probability
                for point in joint_distribution
                if point.mediator_label == setup.readout.mediator_labels[index]
            ),
        )
        for index in range(setup.mediator_dimension)
    )


def _probe_response_distribution(
    setup: QuantumPulseMediatorSetup,
    joint_distribution: Sequence[JointRecordPoint],
) -> ResponseDistribution:
    points = []
    for index in range(setup.probe_dimension):
        label = setup.readout.probe_labels[index]
        probability = math.fsum(
            point.probability for point in joint_distribution if point.probe_label == label
        )
        points.append(ResponsePoint(setup.readout.pulse_count_values[index], probability))
    return ResponseDistribution(
        _coalesced_response_points(points),
        family="quantum-mediator-probe-marginal",
        accepted_as_law=False,
        diagnostic_only=True,
    )


def _marginal_mean(points: Sequence[MarginalRecordPoint]) -> float:
    return math.fsum(point.value * point.probability for point in points)


def _probe_readout_mean(joint_distribution: Sequence[JointRecordPoint]) -> float:
    return math.fsum(point.probe_value * point.probability for point in joint_distribution)


def _response_mean(response: ResponseDistribution) -> float:
    return math.fsum(point.pulse_count * point.probability for point in response.points)


def _joint_covariance(
    joint_distribution: Sequence[JointRecordPoint],
    *,
    first: str,
    first_mean: float,
    second: str,
    second_mean: float,
) -> float:
    return math.fsum(
        (_record_value(point, first) - first_mean)
        * (_record_value(point, second) - second_mean)
        * point.probability
        for point in joint_distribution
    )


def _record_value(point: JointRecordPoint, name: str) -> float:
    if name == "source":
        return point.source_value
    if name == "mediator":
        return point.mediator_value
    if name == "probe":
        return point.probe_value
    raise ValueError("unknown record value")


def _pulse_count_moments(joint_distribution: Sequence[JointRecordPoint]) -> tuple[float, float]:
    mean = math.fsum(point.pulse_count * point.probability for point in joint_distribution)
    variance = math.fsum(
        (point.pulse_count - mean) ** 2 * point.probability
        for point in joint_distribution
    )
    if variance < 0.0 and abs(variance) <= 1.0e-12:
        variance = 0.0
    _require_nonnegative("pulse-count variance", variance)
    return mean, variance


def _conditional_probe_shifts(
    setup: QuantumPulseMediatorSetup,
    joint_distribution: Sequence[JointRecordPoint],
    *,
    unconditional_probe_mean: float,
) -> tuple[ConditionalProbeShift, ...]:
    shifts: list[ConditionalProbeShift] = []
    for mediator_label in setup.readout.mediator_labels:
        mediator_probability = math.fsum(
            point.probability for point in joint_distribution if point.mediator_label == mediator_label
        )
        if mediator_probability <= 0.0:
            continue
        conditional_mean = math.fsum(
            point.probe_value * point.probability
            for point in joint_distribution
            if point.mediator_label == mediator_label
        ) / mediator_probability
        shifts.append(
            ConditionalProbeShift(
                mediator_label,
                mediator_probability,
                conditional_mean,
                unconditional_probe_mean,
                conditional_mean - unconditional_probe_mean,
            )
        )
    return tuple(shifts)


def _witness_value(witness_matrix: Sequence[Sequence[complex]], final_state: Matrix) -> float:
    witness = _validated_square_matrix(witness_matrix, "entanglement_witness_matrix")
    _require_same_dimension(witness, final_state)
    _require_hermitian("entanglement_witness_matrix", witness)
    value = _trace_product(witness, final_state)
    if abs(value.imag) > 1.0e-10:
        raise ValueError("entanglement witness value must be real within tolerance")
    _require_finite_real("entanglement witness value", value.real)
    return value.real


def _partial_trace_probe(
    full_state: Matrix,
    source_dimension: int,
    mediator_dimension: int,
    probe_dimension: int,
) -> Matrix:
    rows: list[list[complex]] = [
        [0.0 + 0.0j for _ in range(probe_dimension)]
        for _ in range(probe_dimension)
    ]
    for source_index in range(source_dimension):
        for mediator_index in range(mediator_dimension):
            for probe_row in range(probe_dimension):
                row_index = _joint_index(
                    source_index,
                    mediator_index,
                    probe_row,
                    mediator_dimension,
                    probe_dimension,
                )
                for probe_col in range(probe_dimension):
                    col_index = _joint_index(
                        source_index,
                        mediator_index,
                        probe_col,
                        mediator_dimension,
                        probe_dimension,
                    )
                    rows[probe_row][probe_col] += full_state[row_index][col_index]
    return tuple(tuple(row) for row in rows)


def _probe_visibility(probe_state: Matrix) -> float | None:
    if len(probe_state) < 2:
        return None
    visibility = 2.0 * abs(probe_state[0][1])
    _require_nonnegative("probe visibility", visibility)
    return visibility


def _timing_observables(
    setup: QuantumPulseMediatorSetup,
    joint_distribution: Sequence[JointRecordPoint],
    *,
    source_mean: float,
) -> tuple[float | None, float | None]:
    if setup.readout.timing_values_s is None:
        return None, None
    timing_by_label = {
        label: setup.readout.timing_values_s[index]
        for index, label in enumerate(setup.readout.probe_labels)
    }
    mean = math.fsum(
        timing_by_label[point.probe_label] * point.probability
        for point in joint_distribution
    )
    covariance = math.fsum(
        (point.source_value - source_mean)
        * (timing_by_label[point.probe_label] - mean)
        * point.probability
        for point in joint_distribution
    )
    return mean, covariance


def _joint_index(
    source_index: int,
    mediator_index: int,
    probe_index: int,
    mediator_dimension: int,
    probe_dimension: int,
) -> int:
    return (source_index * mediator_dimension + mediator_index) * probe_dimension + probe_index


def _validated_density_matrix(matrix: Sequence[Sequence[complex]], name: str) -> Matrix:
    rows = _validated_square_matrix(matrix, name)
    _require_hermitian(name, rows)
    _require_positive_semidefinite(name, rows)
    _require_density_trace_one(rows, name)
    return rows


def _validated_square_matrix(matrix: Sequence[Sequence[complex]], name: str) -> Matrix:
    rows = tuple(tuple(complex(value) for value in row) for row in matrix)
    if not rows:
        raise ValueError(f"{name} must not be empty")
    dimension = len(rows)
    for row in rows:
        if len(row) != dimension:
            raise ValueError(f"{name} must be square")
        for value in row:
            _require_finite_complex(f"{name} entry", value)
    return rows


def _require_density_trace_one(matrix: Matrix, name: str) -> None:
    trace = _trace(matrix)
    if abs(trace.imag) > 1.0e-10:
        raise ValueError(f"{name} trace must be real")
    if not math.isclose(trace.real, 1.0, rel_tol=1.0e-10, abs_tol=1.0e-10):
        raise ValueError(f"{name} trace must be 1")


def _require_hermitian(name: str, matrix: Matrix) -> None:
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if abs(matrix[row][col] - matrix[col][row].conjugate()) > 1.0e-10:
                raise ValueError(f"{name} must be Hermitian")


def _require_positive_semidefinite(name: str, matrix: Matrix) -> None:
    dimension = len(matrix)
    for size in range(1, dimension + 1):
        for indices in combinations(range(dimension), size):
            minor = tuple(tuple(matrix[row][col] for col in indices) for row in indices)
            determinant = _determinant(minor)
            if abs(determinant.imag) > 1.0e-10:
                raise ValueError(f"{name} principal minors must be real")
            if determinant.real < -1.0e-10:
                raise ValueError(f"{name} must be positive semidefinite")


def _require_full_unitary_dimension(
    coupling: CouplingDeclaration,
    full_dimension: int,
    name: str,
) -> None:
    if coupling.dimension != full_dimension:
        raise ValueError(f"{name} dimension must match source*mediator*probe dimension")
    _require_unitary(name, coupling.unitary_matrix)


def _require_unitary(name: str, matrix: Matrix) -> None:
    identity = _identity_matrix(len(matrix))
    product = _matrix_multiply(_conjugate_transpose(matrix), matrix)
    if _matrix_max_abs_difference(product, identity) > 1.0e-10:
        raise ValueError(f"{name} must be unitary")


def _matrix_multiply(first: Matrix, second: Matrix) -> Matrix:
    _require_same_dimension(first, second)
    dimension = len(first)
    rows: list[list[complex]] = []
    for row in range(dimension):
        entries: list[complex] = []
        for col in range(dimension):
            entries.append(
                sum(first[row][inner] * second[inner][col] for inner in range(dimension))
            )
        rows.append(entries)
    return tuple(tuple(row) for row in rows)


def _conjugate_transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[col][row].conjugate() for col in range(len(matrix)))
        for row in range(len(matrix))
    )


def _identity_matrix(dimension: int) -> Matrix:
    return tuple(
        tuple(1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(dimension))
        for row in range(dimension)
    )


def _kronecker_product(first: Matrix, second: Matrix) -> Matrix:
    rows: list[list[complex]] = []
    for first_row in first:
        for second_row in second:
            row: list[complex] = []
            for first_value in first_row:
                for second_value in second_row:
                    row.append(first_value * second_value)
            rows.append(row)
    return tuple(tuple(row) for row in rows)


def _trace(matrix: Matrix) -> complex:
    return sum(matrix[index][index] for index in range(len(matrix)))


def _trace_product(first: Matrix, second: Matrix) -> complex:
    _require_same_dimension(first, second)
    total = 0.0 + 0.0j
    dimension = len(first)
    for row in range(dimension):
        for col in range(dimension):
            total += first[row][col] * second[col][row]
    return total


def _determinant(matrix: Matrix) -> complex:
    dimension = len(matrix)
    work = [list(row) for row in matrix]
    determinant = 1.0 + 0.0j
    for pivot_index in range(dimension):
        pivot_row = max(
            range(pivot_index, dimension),
            key=lambda row: abs(work[row][pivot_index]),
        )
        pivot = work[pivot_row][pivot_index]
        if abs(pivot) <= 1.0e-15:
            return 0.0 + 0.0j
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            determinant *= -1.0
        determinant *= pivot
        for row in range(pivot_index + 1, dimension):
            factor = work[row][pivot_index] / pivot
            for col in range(pivot_index + 1, dimension):
                work[row][col] -= factor * work[pivot_index][col]
    return determinant


def _matrix_max_abs_difference(first: Matrix, second: Matrix) -> float:
    _require_same_dimension(first, second)
    max_difference = 0.0
    for row in range(len(first)):
        for col in range(len(first)):
            max_difference = max(max_difference, abs(first[row][col] - second[row][col]))
    return max_difference


def _require_same_dimension(first: Matrix, second: Matrix) -> None:
    if len(first) != len(second):
        raise ValueError("matrices must have the same dimension")


def _coalesced_response_points(points: Sequence[ResponsePoint]) -> tuple[ResponsePoint, ...]:
    sorted_points = sorted((point for point in points if point.probability > 0.0), key=lambda point: point.pulse_count)
    if not sorted_points:
        raise ValueError("response distribution must not be empty")
    merged: list[ResponsePoint] = []
    current_probability = sorted_points[0].probability
    current_weighted_count = sorted_points[0].pulse_count * sorted_points[0].probability
    current_reference = sorted_points[0].pulse_count
    for point in sorted_points[1:]:
        if math.isclose(point.pulse_count, current_reference, rel_tol=0.0, abs_tol=1.0e-12):
            current_probability += point.probability
            current_weighted_count += point.pulse_count * point.probability
            current_reference = current_weighted_count / current_probability
        else:
            merged.append(ResponsePoint(current_weighted_count / current_probability, current_probability))
            current_probability = point.probability
            current_weighted_count = point.pulse_count * point.probability
            current_reference = point.pulse_count
    merged.append(ResponsePoint(current_weighted_count / current_probability, current_probability))
    return tuple(merged)


def _probability_from_diagonal(value: complex) -> float:
    if abs(value.imag) > 1.0e-10:
        raise ValueError("record probability must be real")
    probability = value.real
    if probability < 0.0 and abs(probability) <= 1.0e-10:
        return 0.0
    _require_probability("record probability", probability)
    return probability


def _validated_real_tuple(name: str, values: Sequence[float]) -> tuple[float, ...]:
    result = tuple(float(value) for value in values)
    if not result:
        raise ValueError(f"{name}s must not be empty")
    for value in result:
        _require_finite_real(name, value)
    return result


def _validated_labels(
    labels: Sequence[str],
    expected_length: int,
    prefix: str,
) -> tuple[str, ...]:
    if not labels:
        return tuple(f"{prefix}{index}" for index in range(expected_length))
    result = tuple(labels)
    if len(result) != expected_length:
        raise ValueError("readout label count must match readout values")
    if len(set(result)) != len(result):
        raise ValueError("readout labels must be unique")
    for label in result:
        _require_nonempty_string("readout label", label)
    return result


def _require_readout_length(values: Sequence[float], expected_length: int, name: str) -> None:
    if len(values) != expected_length:
        raise ValueError(f"{name} length must match sector dimension")


def _validated_artifact_ledger(artifact_ledger: Sequence[str]) -> tuple[str, ...]:
    artifacts = tuple(artifact_ledger)
    for artifact in artifacts:
        _require_nonempty_string("artifact ledger entry", artifact)
    return artifacts


def _require_label(name: str, value: str, allowed: frozenset[str]) -> None:
    _require_nonempty_string(name, value)
    if value not in allowed:
        allowed_values = ", ".join(sorted(allowed))
        raise ValueError(f"{name} must be one of: {allowed_values}")


def _require_nonempty_string(name: str, value: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a nonempty string")


def _require_finite_complex(name: str, value: complex) -> None:
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError(f"{name} must be finite")


def _require_finite_real(name: str, value: float) -> None:
    if not isinstance(value, int | float) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite real number")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite_real(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_probability(name: str, value: float) -> None:
    _require_nonnegative(name, value)
    if value > 1.0:
        raise ValueError(f"{name} must be at most 1")


def _require_positive_int(name: str, value: int) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
