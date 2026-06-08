"""Deterministic H6S4-C stochastic pulse-geometry candidate helpers.

The API evaluates the finite weak-field candidate from the H6S4-C appendix.
It treats the local potential operator as declared in its spectral basis and
returns the exact finite probe pulse-count distribution. It does not sample,
fit coefficients, or use arbitrary ensemble branch labels.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass

from .calculations import SPEED_OF_LIGHT_M_PER_S
from .causal_pulse_response import (
    CausalDomain,
    CoefficientLedger,
    ConservationLedger,
    DensityMatrixResponseSetup,
    EnsembleDecomposition,
    EnsembleInvarianceReport,
    PulsePotentialOperator,
    ResponseDistribution,
    ResponsePoint,
    check_causal_domain,
    check_ensemble_invariance,
    density_matrix_expectation_response,
    ensemble_density_matrix,
)
from .no_free_branch_variance import (
    NoFreeBranchVarianceReport,
    classify_branch_variance_route,
    compare_branch_variance_across_decompositions,
)


COUPLING_TARGET_LABELS = frozenset(
    {
        "potential-operator-variance",
        "stress-energy-noise-kernel",
        "phase-density",
        "pulse-records",
        "curvature-records",
        "not-declared",
    }
)
REGULATOR_PROVENANCE_LABELS = frozenset(
    {
        "none-required",
        "finite-operator",
        "finite-size-source",
        "h6s1-softening-declared",
        "calibrated-before-test",
        "exploratory-only",
        "not-declared",
        "fit-after-observation rejected",
    }
)
STOCHASTIC_CANDIDATE_STATUS_LABELS = frozenset(
    {
        "controlled-modification-candidate",
        "diagnostic-only",
        "blocked",
        "clean-no-go-candidate",
    }
)


@dataclass(frozen=True)
class StochasticLawDeclaration:
    """Declared finite stochastic law before external comparison."""

    law_name: str = "finite-spectral-potential-noise"
    stochastic_variable: str = "spectral-potential-fluctuation"
    pre_code_result_class: str = "controlled-modification-candidate"
    gr_recovery_declared: bool = True
    qm_recovery_declared: bool = True

    def __post_init__(self) -> None:
        _require_nonempty_string("law_name", self.law_name)
        _require_nonempty_string("stochastic_variable", self.stochastic_variable)
        _require_label(
            "pre_code_result_class",
            self.pre_code_result_class,
            STOCHASTIC_CANDIDATE_STATUS_LABELS,
        )


@dataclass(frozen=True)
class NoiseCouplingLedger:
    """Noise process and coupling target for H6S4-C."""

    coupling_target: str = "potential-operator-variance"
    causal_noise_declared: bool = True
    no_signaling_guardrail_declared: bool = True
    description: str = "finite local potential spectral noise"

    def __post_init__(self) -> None:
        _require_label("coupling_target", self.coupling_target, COUPLING_TARGET_LABELS)
        _require_nonempty_string("description", self.description)


@dataclass(frozen=True)
class RegulatorLedger:
    """Regulator provenance for the stochastic candidate."""

    provenance: str = "finite-operator"
    description: str = "finite local potential operator"

    def __post_init__(self) -> None:
        _require_label("regulator provenance", self.provenance, REGULATOR_PROVENANCE_LABELS)
        _require_nonempty_string("regulator description", self.description)


@dataclass(frozen=True)
class LocalStochasticPulseSetup:
    """Finite local setup for the stochastic pulse-potential response."""

    density_matrix: Sequence[Sequence[complex]]
    potential_operator: PulsePotentialOperator
    clock_frequency_hz: float
    duration_s: float
    ordinary_instrument_noise_variance_pulses2: float = 0.0
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S

    def __post_init__(self) -> None:
        validated = DensityMatrixResponseSetup(
            self.density_matrix,
            self.potential_operator,
            self.clock_frequency_hz,
            self.duration_s,
            self.speed_of_light_m_per_s,
        )
        _require_nonnegative(
            "ordinary_instrument_noise_variance_pulses2",
            self.ordinary_instrument_noise_variance_pulses2,
        )
        object.__setattr__(self, "density_matrix", validated.density_matrix)


@dataclass(frozen=True)
class StochasticCandidateClassification:
    """Candidate status after H6S4-C ledgers are applied."""

    status: str
    candidate_ready: bool
    diagnostic_only: bool
    accepted_as_law: bool
    reasons: tuple[str, ...]
    missing_requirements: tuple[str, ...]

    def __post_init__(self) -> None:
        _require_label("status", self.status, STOCHASTIC_CANDIDATE_STATUS_LABELS)
        for reason in self.reasons:
            _require_nonempty_string("classification reason", reason)
        for requirement in self.missing_requirements:
            _require_nonempty_string("missing requirement", requirement)
        if self.accepted_as_law:
            raise ValueError("H6S4-C API cannot mark the candidate accepted as law before final verdict")


@dataclass(frozen=True)
class StochasticPulseGeometryReport:
    """Deterministic finite response report for H6S4-C."""

    response_distribution: ResponseDistribution
    density_only_distribution: ResponseDistribution
    classification: StochasticCandidateClassification
    mean_pulse_count: float
    density_only_mean_pulse_count: float
    potential_mean_m2_per_s2: float
    potential_variance_m4_per_s4: float
    excess_pulse_count_variance_pulses2: float
    timing_jitter_variance_s2: float
    ordinary_instrument_noise_variance_pulses2: float
    observed_variance_pulses2: float
    law_name: str
    coupling_target: str
    coefficient_provenance: str
    conservation_status: str
    regulator_provenance: str
    causal_status: str
    artifact_ledger: tuple[str, ...]
    diagnostic_only: bool
    accepted_as_law: bool


@dataclass(frozen=True)
class StochasticEnsembleComparisonReport:
    """Remote-basis/decomposition invariance report for H6S4-C."""

    first_report: StochasticPulseGeometryReport
    second_report: StochasticPulseGeometryReport
    ensemble_invariance: EnsembleInvarianceReport
    no_free_branch_variance_report: NoFreeBranchVarianceReport
    same_stochastic_response: bool
    spacelike_remote_basis_safe: bool
    accepted_as_law: bool


@dataclass(frozen=True)
class StochasticBaselineComparisonReport:
    """Baseline comparator report for the H6S4-C route."""

    route_failure_classification: str
    density_only_mean_difference_pulses: float
    density_only_variance_pulses2: float
    stochastic_excess_variance_pulses2: float
    invalid_ensemble_variance_pulses2: float | None
    invalid_ensemble_rejected: bool
    pointer_record_variance_pulses2: float | None
    pointer_record_is_comparator_only: bool
    ordinary_instrument_noise_variance_pulses2: float
    ordinary_noise_separate: bool
    h6s3_no_free_report_reason: str
    reasons: tuple[str, ...]
    accepted_as_law: bool

    def __post_init__(self) -> None:
        _require_label(
            "route_failure_classification",
            self.route_failure_classification,
            STOCHASTIC_CANDIDATE_STATUS_LABELS,
        )
        for reason in self.reasons:
            _require_nonempty_string("baseline reason", reason)
        if self.accepted_as_law:
            raise ValueError("baseline report cannot accept H6S4-C as law before final verdict")


def stochastic_pulse_geometry_response(
    setup: LocalStochasticPulseSetup,
    law: StochasticLawDeclaration,
    coupling_ledger: NoiseCouplingLedger,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    regulator_ledger: RegulatorLedger,
    *,
    artifact_ledger: Sequence[str],
) -> StochasticPulseGeometryReport:
    """Return the deterministic H6S4-C stochastic response report."""

    artifacts = _validated_artifact_ledger(artifact_ledger)
    potential_values = _diagonal_potential_values(setup.potential_operator)
    probabilities = _spectral_probabilities(setup.density_matrix)
    points = _response_points_from_potential_values(setup, potential_values, probabilities)
    response = ResponseDistribution(
        _coalesced_points(points),
        family="stochastic-classical-pulse-geometry",
        accepted_as_law=False,
        diagnostic_only=True,
    )
    density_only = density_matrix_expectation_response(
        DensityMatrixResponseSetup(
            setup.density_matrix,
            setup.potential_operator,
            setup.clock_frequency_hz,
            setup.duration_s,
            setup.speed_of_light_m_per_s,
        )
    )
    potential_mean = math.fsum(
        probability * potential_value
        for potential_value, probability in zip(potential_values, probabilities, strict=True)
    )
    potential_second_moment = math.fsum(
        probability * potential_value**2
        for potential_value, probability in zip(potential_values, probabilities, strict=True)
    )
    potential_variance = potential_second_moment - potential_mean**2
    if potential_variance < 0.0 and abs(potential_variance) <= 1.0e-12:
        potential_variance = 0.0
    _require_nonnegative("potential variance", potential_variance)

    response_mean, response_variance = _response_moments(response)
    density_only_mean, _ = _response_moments(density_only)
    excess_variance = (
        (setup.clock_frequency_hz * setup.duration_s / setup.speed_of_light_m_per_s**2) ** 2
        * potential_variance
    )
    timing_jitter_variance = (
        (setup.duration_s / setup.speed_of_light_m_per_s**2) ** 2
        * potential_variance
    )
    observed_variance = response_variance + setup.ordinary_instrument_noise_variance_pulses2
    classification = classify_stochastic_candidate(
        law,
        coupling_ledger,
        causal_domain,
        conservation_ledger,
        coefficient_ledger,
        regulator_ledger,
        artifact_ledger=artifacts,
    )

    return StochasticPulseGeometryReport(
        response_distribution=response,
        density_only_distribution=density_only,
        classification=classification,
        mean_pulse_count=response_mean,
        density_only_mean_pulse_count=density_only_mean,
        potential_mean_m2_per_s2=potential_mean,
        potential_variance_m4_per_s4=potential_variance,
        excess_pulse_count_variance_pulses2=excess_variance,
        timing_jitter_variance_s2=timing_jitter_variance,
        ordinary_instrument_noise_variance_pulses2=setup.ordinary_instrument_noise_variance_pulses2,
        observed_variance_pulses2=observed_variance,
        law_name=law.law_name,
        coupling_target=coupling_ledger.coupling_target,
        coefficient_provenance=coefficient_ledger.provenance,
        conservation_status=conservation_ledger.status,
        regulator_provenance=regulator_ledger.provenance,
        causal_status=causal_domain.status,
        artifact_ledger=artifacts,
        diagnostic_only=classification.diagnostic_only,
        accepted_as_law=False,
    )


def classify_stochastic_candidate(
    law: StochasticLawDeclaration,
    coupling_ledger: NoiseCouplingLedger,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    regulator_ledger: RegulatorLedger,
    *,
    artifact_ledger: Sequence[str],
) -> StochasticCandidateClassification:
    """Classify whether the finite stochastic candidate has complete ledgers."""

    artifacts = _validated_artifact_ledger(artifact_ledger)
    missing: list[str] = []
    reasons: list[str] = []

    if not law.stochastic_variable:
        missing.append("stochastic variable")
    if law.pre_code_result_class == "clean-no-go-candidate":
        reasons.append("law declaration is already a clean-no-go candidate")
    if not law.gr_recovery_declared:
        missing.append("GR recovery limit")
    if not law.qm_recovery_declared:
        missing.append("QM recovery limit")

    if coupling_ledger.coupling_target != "potential-operator-variance":
        missing.append("potential-operator variance coupling target")
    if not coupling_ledger.causal_noise_declared:
        missing.append("causal noise declaration")
    if not coupling_ledger.no_signaling_guardrail_declared:
        missing.append("no-signaling guardrail")

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
        conservation_ledger.discontinuous_branch_update
        and not conservation_ledger.environment_or_collapse_sector
    ):
        missing.append("environment or reservoir for discontinuous update")

    if coefficient_ledger.provenance == "fit-after-observation rejected":
        reasons.append("fit-after-observation coefficient provenance is rejected")
    elif coefficient_ledger.provenance == "exploratory-only":
        missing.append("non-exploratory coefficient provenance")

    if regulator_ledger.provenance in {"not-declared", "fit-after-observation rejected"}:
        missing.append("regulator provenance")
    elif regulator_ledger.provenance == "exploratory-only":
        missing.append("non-exploratory regulator provenance")

    if not artifacts:
        missing.append("artifact ledger")

    if reasons or missing:
        all_reasons = tuple(reasons + [f"missing {item}" for item in missing])
        return StochasticCandidateClassification(
            status="blocked",
            candidate_ready=False,
            diagnostic_only=True,
            accepted_as_law=False,
            reasons=all_reasons,
            missing_requirements=tuple(missing),
        )

    return StochasticCandidateClassification(
        status=law.pre_code_result_class,
        candidate_ready=True,
        diagnostic_only=False,
        accepted_as_law=False,
        reasons=("complete ledgers for pre-code candidate; final verdict still controls law status",),
        missing_requirements=(),
    )


def stochastic_excess_variance(report: StochasticPulseGeometryReport) -> float:
    """Return the fixed excess pulse-count variance from the report."""

    _require_nonnegative(
        "excess_pulse_count_variance_pulses2",
        report.excess_pulse_count_variance_pulses2,
    )
    return report.excess_pulse_count_variance_pulses2


def compare_stochastic_responses_for_decompositions(
    first_decomposition: EnsembleDecomposition,
    second_decomposition: EnsembleDecomposition,
    potential_operator: PulsePotentialOperator,
    clock_frequency_hz: float,
    duration_s: float,
    law: StochasticLawDeclaration,
    coupling_ledger: NoiseCouplingLedger,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    regulator_ledger: RegulatorLedger,
    *,
    artifact_ledger: Sequence[str],
    ordinary_instrument_noise_variance_pulses2: float = 0.0,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> StochasticEnsembleComparisonReport:
    """Compare H6S4-C responses for two ensemble descriptions of a state."""

    first_report = stochastic_pulse_geometry_response(
        LocalStochasticPulseSetup(
            ensemble_density_matrix(first_decomposition),
            potential_operator,
            clock_frequency_hz,
            duration_s,
            ordinary_instrument_noise_variance_pulses2,
            speed_of_light_m_per_s,
        ),
        law,
        coupling_ledger,
        causal_domain,
        conservation_ledger,
        coefficient_ledger,
        regulator_ledger,
        artifact_ledger=artifact_ledger,
    )
    second_report = stochastic_pulse_geometry_response(
        LocalStochasticPulseSetup(
            ensemble_density_matrix(second_decomposition),
            potential_operator,
            clock_frequency_hz,
            duration_s,
            ordinary_instrument_noise_variance_pulses2,
            speed_of_light_m_per_s,
        ),
        law,
        coupling_ledger,
        causal_domain,
        conservation_ledger,
        coefficient_ledger,
        regulator_ledger,
        artifact_ledger=artifact_ledger,
    )
    ensemble_invariance = check_ensemble_invariance(
        first_decomposition,
        second_decomposition,
        first_report.response_distribution,
        second_report.response_distribution,
    )
    no_free_report = compare_branch_variance_across_decompositions(
        first_decomposition,
        second_decomposition,
        first_report.response_distribution,
        second_report.response_distribution,
        route_classification=classify_branch_variance_route(
            "stochastic-classical-pulse-geometry",
            stochastic_law_declared=bool(law.stochastic_variable),
            coefficient_provenance_declared=coefficient_ledger.provenance
            not in {"exploratory-only", "fit-after-observation rejected"},
            regulator_provenance_declared=regulator_ledger.provenance
            not in {"not-declared", "exploratory-only", "fit-after-observation rejected"},
            conservation_ledger_declared=conservation_ledger.status
            not in {"not-yet-classified", "inconsistent-rejected"},
            no_signaling_guardrail_declared=coupling_ledger.no_signaling_guardrail_declared,
            artifact_ledger_declared=bool(tuple(artifact_ledger)),
        ),
    )
    same_response = ensemble_invariance.invariant and not no_free_report.branch_variance_changes
    return StochasticEnsembleComparisonReport(
        first_report=first_report,
        second_report=second_report,
        ensemble_invariance=ensemble_invariance,
        no_free_branch_variance_report=no_free_report,
        same_stochastic_response=same_response,
        spacelike_remote_basis_safe=same_response and not no_free_report.diagnostic_failure,
        accepted_as_law=False,
    )


def compare_stochastic_baselines(
    report: StochasticPulseGeometryReport,
    *,
    invalid_ensemble_response: ResponseDistribution | None = None,
    pointer_record_response: ResponseDistribution | None = None,
    no_free_branch_variance_report: NoFreeBranchVarianceReport | None = None,
) -> StochasticBaselineComparisonReport:
    """Compare the H6S4-C candidate against required baseline families."""

    density_mean, density_variance = _response_moments(report.density_only_distribution)
    density_mean_difference = abs(report.mean_pulse_count - density_mean)
    invalid_variance = (
        _response_moments(invalid_ensemble_response)[1]
        if invalid_ensemble_response is not None
        else None
    )
    pointer_variance = (
        _response_moments(pointer_record_response)[1]
        if pointer_record_response is not None
        else None
    )
    invalid_rejected = (
        invalid_ensemble_response is None
        or (
            invalid_ensemble_response.family == "invalid-ensemble-dependent-branch-response"
            and invalid_ensemble_response.diagnostic_only
            and not invalid_ensemble_response.accepted_as_law
        )
    )
    pointer_comparator_only = (
        pointer_record_response is None
        or (
            pointer_record_response.family == "pointer-record-branch-response"
            and pointer_record_response.diagnostic_only
            and not pointer_record_response.accepted_as_law
        )
    )
    no_free_reason = (
        no_free_branch_variance_report.reason
        if no_free_branch_variance_report is not None
        else "H6S3 no-free branch variance report not supplied"
    )
    reasons = list(report.classification.reasons)
    if not invalid_rejected:
        reasons.append("invalid ensemble branch response was not rejected")
    if not pointer_comparator_only:
        reasons.append("pointer-record response was promoted beyond comparator status")
    if no_free_branch_variance_report is None:
        reasons.append("missing H6S3 no-free branch variance comparison")
    elif no_free_branch_variance_report.diagnostic_failure:
        reasons.append(no_free_branch_variance_report.reason)

    route_classification = _route_failure_classification(
        report,
        invalid_rejected=invalid_rejected,
        pointer_comparator_only=pointer_comparator_only,
        no_free_branch_variance_report=no_free_branch_variance_report,
    )

    return StochasticBaselineComparisonReport(
        route_failure_classification=route_classification,
        density_only_mean_difference_pulses=density_mean_difference,
        density_only_variance_pulses2=density_variance,
        stochastic_excess_variance_pulses2=report.excess_pulse_count_variance_pulses2,
        invalid_ensemble_variance_pulses2=invalid_variance,
        invalid_ensemble_rejected=invalid_rejected,
        pointer_record_variance_pulses2=pointer_variance,
        pointer_record_is_comparator_only=pointer_comparator_only,
        ordinary_instrument_noise_variance_pulses2=report.ordinary_instrument_noise_variance_pulses2,
        ordinary_noise_separate=True,
        h6s3_no_free_report_reason=no_free_reason,
        reasons=tuple(reasons),
        accepted_as_law=False,
    )


def _route_failure_classification(
    report: StochasticPulseGeometryReport,
    *,
    invalid_rejected: bool,
    pointer_comparator_only: bool,
    no_free_branch_variance_report: NoFreeBranchVarianceReport | None,
) -> str:
    if report.classification.status == "blocked":
        return "blocked"
    if not invalid_rejected or not pointer_comparator_only:
        return "blocked"
    if no_free_branch_variance_report is None:
        return "diagnostic-only"
    if no_free_branch_variance_report.diagnostic_failure:
        return "clean-no-go-candidate"
    if report.excess_pulse_count_variance_pulses2 > 0.0:
        return report.classification.status
    return "diagnostic-only"


def _diagonal_potential_values(operator: PulsePotentialOperator) -> tuple[float, ...]:
    matrix = operator.matrix
    values: list[float] = []
    for row, entries in enumerate(matrix):
        for col, entry in enumerate(entries):
            if row == col:
                if abs(entry.imag) > 1.0e-12:
                    raise ValueError("potential spectral values must be real")
                _require_finite_real("potential spectral value", entry.real)
                values.append(entry.real)
            elif abs(entry) > 1.0e-12:
                raise ValueError("potential_operator must be diagonal in the declared spectral basis")
    return tuple(values)


def _spectral_probabilities(density_matrix: Sequence[Sequence[complex]]) -> tuple[float, ...]:
    probabilities: list[float] = []
    for index, row in enumerate(density_matrix):
        probability = row[index]
        if abs(probability.imag) > 1.0e-12:
            raise ValueError("density spectral probabilities must be real")
        _require_nonnegative("density spectral probability", probability.real)
        probabilities.append(probability.real)
    total_probability = math.fsum(probabilities)
    if not math.isclose(total_probability, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise ValueError("density spectral probabilities must sum to 1")
    return tuple(probabilities)


def _response_points_from_potential_values(
    setup: LocalStochasticPulseSetup,
    potential_values: Sequence[float],
    probabilities: Sequence[float],
) -> tuple[ResponsePoint, ...]:
    points: list[ResponsePoint] = []
    for potential_value, probability in zip(potential_values, probabilities, strict=True):
        pulse_count = setup.clock_frequency_hz * setup.duration_s * (
            1.0 + potential_value / setup.speed_of_light_m_per_s**2
        )
        _require_nonnegative("stochastic pulse count", pulse_count)
        if probability > 0.0:
            points.append(ResponsePoint(pulse_count, probability))
    if not points:
        raise ValueError("stochastic response distribution must not be empty")
    return tuple(points)


def _response_moments(response: ResponseDistribution) -> tuple[float, float]:
    mean = math.fsum(point.pulse_count * point.probability for point in response.points)
    variance = math.fsum(
        point.probability * (point.pulse_count - mean) ** 2
        for point in response.points
    )
    _require_finite_real("response mean", mean)
    _require_nonnegative("response variance", variance)
    return mean, variance


def _coalesced_points(points: Sequence[ResponsePoint]) -> tuple[ResponsePoint, ...]:
    sorted_points = sorted(points, key=lambda point: point.pulse_count)
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


def _require_finite_real(name: str, value: float) -> None:
    if not isinstance(value, int | float) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite real number")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite_real(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")
