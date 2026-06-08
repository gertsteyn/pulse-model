"""Finite-dimensional H6S2 causal pulse-response guardrails.

This module implements the executable contract from the H6S2 appendix. It
keeps the response model finite, deterministic, and deliberately modest: the
helpers classify admissibility conditions, but they do not invent a
pulse-native source-response law.
"""

from __future__ import annotations

from itertools import combinations
import math
from collections.abc import Sequence
from dataclasses import dataclass

from .calculations import SPEED_OF_LIGHT_M_PER_S


Matrix = tuple[tuple[complex, ...], ...]
Vector = tuple[complex, ...]

CAUSAL_DOMAIN_LABELS = frozenset(
    {
        "inside-probe-causal-past",
        "compared-in-shared-future",
        "spacelike-remote-choice",
        "causal-channel-declared",
        "not-declared",
    }
)
CONSERVATION_LABELS = frozenset(
    {
        "branchwise-conserved",
        "expectation-conserved",
        "conservation-requires-environment",
        "not-yet-classified",
        "inconsistent-rejected",
    }
)
COEFFICIENT_PROVENANCE_LABELS = frozenset(
    {
        "derived",
        "calibrated-before-test",
        "fixed-by-known-limit",
        "exploratory-only",
        "fit-after-observation rejected",
    }
)


@dataclass(frozen=True)
class EnsembleComponent:
    """One finite pure-state component in an ensemble decomposition."""

    probability: float
    state_vector: Sequence[complex]
    label: str
    pulse_count: float | None = None

    def __post_init__(self) -> None:
        _require_probability("probability", self.probability)
        _require_nonempty_string("label", self.label)
        vector = _validated_state_vector(self.state_vector)
        object.__setattr__(self, "state_vector", vector)
        if self.pulse_count is not None:
            _require_finite_real("pulse_count", self.pulse_count)

    @property
    def dimension(self) -> int:
        return len(self.state_vector)


@dataclass(frozen=True)
class EnsembleDecomposition:
    """Finite ensemble decomposition of one local density operator."""

    components: Sequence[EnsembleComponent]
    name: str = "ensemble"

    def __post_init__(self) -> None:
        _require_nonempty_string("name", self.name)
        components = tuple(self.components)
        if not components:
            raise ValueError("components must not be empty")
        dimension = components[0].dimension
        labels: set[str] = set()
        for component in components:
            if component.dimension != dimension:
                raise ValueError("all ensemble components must have the same dimension")
            if component.label in labels:
                raise ValueError("ensemble component labels must be unique")
            labels.add(component.label)
        total_probability = math.fsum(component.probability for component in components)
        if not math.isclose(total_probability, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
            raise ValueError("ensemble probabilities must sum to 1")
        object.__setattr__(self, "components", components)

    @property
    def dimension(self) -> int:
        return self.components[0].dimension


@dataclass(frozen=True)
class PulsePotentialOperator:
    """Finite Hermitian operator used in an expectation response."""

    matrix: Sequence[Sequence[complex]]
    label: str = "potential"

    def __post_init__(self) -> None:
        _require_nonempty_string("label", self.label)
        matrix = _validated_square_matrix(self.matrix, "matrix")
        _require_hermitian("matrix", matrix)
        object.__setattr__(self, "matrix", matrix)

    @property
    def dimension(self) -> int:
        return len(self.matrix)


@dataclass(frozen=True)
class DensityMatrixResponseSetup:
    """Inputs for the density-operator expectation response."""

    density_matrix: Sequence[Sequence[complex]]
    potential_operator: PulsePotentialOperator
    clock_frequency_hz: float
    duration_s: float
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S

    def __post_init__(self) -> None:
        density_matrix = _validated_density_matrix(self.density_matrix, "density_matrix")
        if len(density_matrix) != self.potential_operator.dimension:
            raise ValueError("density matrix and potential operator dimensions must match")
        _require_nonnegative("clock_frequency_hz", self.clock_frequency_hz)
        _require_nonnegative("duration_s", self.duration_s)
        _require_positive("speed_of_light_m_per_s", self.speed_of_light_m_per_s)
        object.__setattr__(self, "density_matrix", density_matrix)


@dataclass(frozen=True)
class ResponsePoint:
    """One point in a finite probe pulse-count distribution."""

    pulse_count: float
    probability: float

    def __post_init__(self) -> None:
        _require_finite_real("pulse_count", self.pulse_count)
        _require_nonnegative("probability", self.probability)


@dataclass(frozen=True)
class ResponseDistribution:
    """Normalized finite probe pulse-count distribution."""

    points: Sequence[ResponsePoint]
    family: str = "response"
    accepted_as_law: bool = False
    diagnostic_only: bool = True

    def __post_init__(self) -> None:
        _require_nonempty_string("family", self.family)
        points = tuple(self.points)
        if not points:
            raise ValueError("response distribution must not be empty")
        total_probability = math.fsum(point.probability for point in points)
        if not math.isclose(total_probability, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
            raise ValueError("response distribution probabilities must sum to 1")
        object.__setattr__(self, "points", points)


@dataclass(frozen=True)
class PointerRecord:
    """Local pointer-record data for branch-conditioned response."""

    pointer_basis: Sequence[str]
    probabilities: Sequence[float]
    pulse_counts: Sequence[float]
    local_record_exists: bool
    causal_status: str
    channel_description: str = ""

    def __post_init__(self) -> None:
        basis = tuple(self.pointer_basis)
        probabilities = tuple(self.probabilities)
        pulse_counts = tuple(self.pulse_counts)
        if not basis:
            raise ValueError("pointer basis must be declared")
        if len(set(basis)) != len(basis):
            raise ValueError("pointer basis labels must be unique")
        if len(probabilities) != len(basis) or len(pulse_counts) != len(basis):
            raise ValueError("pointer basis, probabilities, and pulse counts must have matching lengths")
        for label in basis:
            _require_nonempty_string("pointer_basis label", label)
        for probability in probabilities:
            _require_probability("pointer probability", probability)
        total_probability = math.fsum(probabilities)
        if not math.isclose(total_probability, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
            raise ValueError("pointer probabilities must sum to 1")
        for pulse_count in pulse_counts:
            _require_finite_real("pointer pulse count", pulse_count)
        _require_label("causal_status", self.causal_status, CAUSAL_DOMAIN_LABELS)
        object.__setattr__(self, "pointer_basis", basis)
        object.__setattr__(self, "probabilities", probabilities)
        object.__setattr__(self, "pulse_counts", pulse_counts)


@dataclass(frozen=True)
class CausalDomain:
    """Declared causal-domain status for a candidate response."""

    status: str
    record_exists: bool = False
    ledgers_declared: bool = False
    channel_description: str = ""

    def __post_init__(self) -> None:
        _require_label("status", self.status, CAUSAL_DOMAIN_LABELS)
        if self.channel_description:
            _require_nonempty_string("channel_description", self.channel_description)


@dataclass(frozen=True)
class ConservationLedger:
    """Conservation account supplied by a response family."""

    status: str
    accounting_source: str = ""
    discontinuous_branch_update: bool = False
    environment_or_collapse_sector: str = ""

    def __post_init__(self) -> None:
        _require_label("status", self.status, CONSERVATION_LABELS)
        if self.accounting_source:
            _require_nonempty_string("accounting_source", self.accounting_source)
        if self.environment_or_collapse_sector:
            _require_nonempty_string(
                "environment_or_collapse_sector",
                self.environment_or_collapse_sector,
            )


@dataclass(frozen=True)
class CoefficientLedger:
    """Coefficient provenance supplied by a response family."""

    provenance: str
    coefficient_name: str = ""
    regulator_provenance: str = ""

    def __post_init__(self) -> None:
        _require_label("provenance", self.provenance, COEFFICIENT_PROVENANCE_LABELS)
        if self.coefficient_name:
            _require_nonempty_string("coefficient_name", self.coefficient_name)
        if self.regulator_provenance:
            _require_nonempty_string("regulator_provenance", self.regulator_provenance)


@dataclass(frozen=True)
class EnsembleInvarianceReport:
    """Comparison of two decompositions and their probe marginals."""

    density_matrix_distance: float
    max_marginal_difference: float
    invariant: bool
    reason: str


@dataclass(frozen=True)
class ResponseKernelReport:
    """Admissibility report for a candidate response distribution."""

    response_distribution: ResponseDistribution
    allowed: bool
    reasons: tuple[str, ...]
    causal_status: str
    conservation_status: str
    coefficient_provenance: str
    gauge_or_branch_matching_declared: bool
    artifact_ledger: tuple[str, ...]
    regulator_provenance: str
    conservation_accounting_source: str
    discontinuous_branch_update: bool


def ensemble_density_matrix(decomposition: EnsembleDecomposition) -> Matrix:
    """Return the density matrix represented by a finite ensemble."""

    dimension = decomposition.dimension
    density = [[0.0 + 0.0j for _ in range(dimension)] for _ in range(dimension)]
    for component in decomposition.components:
        for row in range(dimension):
            for col in range(dimension):
                density[row][col] += (
                    component.probability
                    * component.state_vector[row]
                    * component.state_vector[col].conjugate()
                )
    matrix = tuple(tuple(row) for row in density)
    return _validated_density_matrix(matrix, "ensemble density matrix")


def decomposition_distance(
    first: EnsembleDecomposition,
    second: EnsembleDecomposition,
) -> float:
    """Return the maximum absolute matrix-entry difference between ensembles."""

    first_density = ensemble_density_matrix(first)
    second_density = ensemble_density_matrix(second)
    _require_same_dimension(first_density, second_density)
    return _matrix_max_abs_difference(first_density, second_density)


def density_matrix_expectation_response(setup: DensityMatrixResponseSetup) -> ResponseDistribution:
    """Return the one-point density-operator expectation response."""

    expectation = _trace_product(setup.density_matrix, setup.potential_operator.matrix)
    if abs(expectation.imag) > 1.0e-10:
        raise ValueError("density-operator expectation must be real within tolerance")
    pulse_count = setup.clock_frequency_hz * setup.duration_s * (
        1.0 + expectation.real / setup.speed_of_light_m_per_s**2
    )
    _require_finite_real("expectation pulse count", pulse_count)
    return ResponseDistribution(
        (ResponsePoint(pulse_count, 1.0),),
        family="density-operator-expectation-response",
        accepted_as_law=False,
        diagnostic_only=False,
    )


def expectation_response_from_density(setup: DensityMatrixResponseSetup) -> ResponseDistribution:
    """Alias for the density-operator expectation response."""

    return density_matrix_expectation_response(setup)


def invalid_ensemble_branch_response(decomposition: EnsembleDecomposition) -> ResponseDistribution:
    """Return the rejected diagnostic response attached to ensemble branches."""

    points: list[ResponsePoint] = []
    for component in decomposition.components:
        if component.pulse_count is None:
            raise ValueError("invalid ensemble branch response requires component pulse_count values")
        points.append(ResponsePoint(component.pulse_count, component.probability))
    return ResponseDistribution(
        tuple(points),
        family="invalid-ensemble-dependent-branch-response",
        accepted_as_law=False,
        diagnostic_only=True,
    )


def pointer_record_branch_response(pointer_record: PointerRecord) -> ResponseDistribution:
    """Return a branch response only when a local pointer record is admissible."""

    if not pointer_record.local_record_exists:
        raise ValueError("pointer-record branch response requires a local record")
    if pointer_record.causal_status == "causal-channel-declared" and not pointer_record.channel_description:
        raise ValueError("causal-channel-declared pointer response requires a modeled channel")
    if pointer_record.causal_status not in {
        "inside-probe-causal-past",
        "compared-in-shared-future",
        "causal-channel-declared",
    }:
        raise ValueError("pointer-record branch response requires an allowed causal status")
    points = tuple(
        ResponsePoint(pulse_count, probability)
        for pulse_count, probability in zip(
            pointer_record.pulse_counts,
            pointer_record.probabilities,
            strict=True,
        )
    )
    return ResponseDistribution(
        points,
        family="pointer-record-branch-response",
        accepted_as_law=False,
        diagnostic_only=True,
    )


def check_ensemble_invariance(
    first_decomposition: EnsembleDecomposition,
    second_decomposition: EnsembleDecomposition,
    first_response: ResponseDistribution,
    second_response: ResponseDistribution,
    *,
    density_tolerance: float = 1.0e-12,
    response_tolerance: float = 1.0e-12,
) -> EnsembleInvarianceReport:
    """Check whether equal-density decompositions give the same probe marginal."""

    _require_nonnegative("density_tolerance", density_tolerance)
    _require_nonnegative("response_tolerance", response_tolerance)
    density_distance = decomposition_distance(first_decomposition, second_decomposition)
    marginal_difference = response_marginal_max_difference(
        first_response,
        second_response,
        pulse_count_tolerance=response_tolerance,
    )
    invariant = density_distance <= density_tolerance and marginal_difference <= response_tolerance
    if density_distance > density_tolerance:
        reason = "decompositions represent different density matrices"
    elif invariant:
        reason = "same density matrix gives same probe marginal"
    else:
        reason = "same density matrix gives different probe marginals"
    return EnsembleInvarianceReport(
        density_matrix_distance=density_distance,
        max_marginal_difference=marginal_difference,
        invariant=invariant,
        reason=reason,
    )


def check_causal_domain(
    causal_domain: CausalDomain,
    *,
    probe_marginal_changes: bool = False,
) -> tuple[bool, str]:
    """Return whether the causal-domain declaration is admissible."""

    status = causal_domain.status
    if status == "inside-probe-causal-past":
        if causal_domain.record_exists and causal_domain.ledgers_declared:
            return True, "inside-probe-causal-past accepted with declared record and ledgers"
        return False, "inside-probe-causal-past requires declared record and ledgers"
    if status == "compared-in-shared-future":
        if causal_domain.record_exists and causal_domain.ledgers_declared:
            return True, "compared-in-shared-future accepted for later correlation analysis"
        return False, "compared-in-shared-future requires declared record and ledgers"
    if status == "spacelike-remote-choice":
        if probe_marginal_changes:
            return False, "spacelike-remote-choice rejected because probe marginal changes"
        return True, "spacelike-remote-choice leaves probe marginal invariant at this gate"
    if status == "causal-channel-declared":
        if causal_domain.channel_description:
            return True, "causal-channel-declared accepted with modeled channel"
        return False, "causal-channel-declared requires a modeled channel"
    return False, "not-declared causal domain is blocked"


def classify_conservation_ledger(ledger: ConservationLedger) -> str:
    """Return the normalized H6S2 conservation label."""

    return ledger.status


def classify_coefficient_ledger(ledger: CoefficientLedger) -> str:
    """Return the normalized H6S2 coefficient provenance label."""

    return ledger.provenance


def guardrail_response_kernel(
    response_distribution: ResponseDistribution,
    causal_domain: CausalDomain,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    *,
    gauge_or_branch_matching_declared: bool,
    artifact_ledger: Sequence[str],
    regulator_provenance: str,
    probe_marginal_changes: bool = False,
) -> ResponseKernelReport:
    """Apply the H6S2 admissibility guardrails to a candidate response."""

    artifacts = tuple(artifact_ledger)
    for artifact in artifacts:
        _require_nonempty_string("artifact ledger entry", artifact)
    if regulator_provenance:
        _require_nonempty_string("regulator_provenance", regulator_provenance)

    reasons: list[str] = []
    causal_allowed, causal_reason = check_causal_domain(
        causal_domain,
        probe_marginal_changes=probe_marginal_changes,
    )
    if not causal_allowed:
        reasons.append(causal_reason)

    if conservation_ledger.status == "not-yet-classified":
        reasons.append("missing conservation status")
    elif conservation_ledger.status == "inconsistent-rejected":
        reasons.append("conservation ledger is inconsistent-rejected")
    elif not conservation_ledger.accounting_source:
        reasons.append("conservation accounting source is missing")

    if coefficient_ledger.provenance == "fit-after-observation rejected":
        reasons.append("fit-after-observation coefficient provenance is rejected")

    if not gauge_or_branch_matching_declared:
        reasons.append("gauge or branch matching declaration is missing")
    if not artifacts:
        reasons.append("artifact ledger is missing")
    if not regulator_provenance:
        reasons.append("regulator provenance is missing")

    return ResponseKernelReport(
        response_distribution=response_distribution,
        allowed=not reasons,
        reasons=tuple(reasons),
        causal_status=causal_domain.status,
        conservation_status=conservation_ledger.status,
        coefficient_provenance=coefficient_ledger.provenance,
        gauge_or_branch_matching_declared=gauge_or_branch_matching_declared,
        artifact_ledger=artifacts,
        regulator_provenance=regulator_provenance,
        conservation_accounting_source=conservation_ledger.accounting_source,
        discontinuous_branch_update=conservation_ledger.discontinuous_branch_update,
    )


def response_marginal_max_difference(
    first_response: ResponseDistribution,
    second_response: ResponseDistribution,
    *,
    pulse_count_tolerance: float = 1.0e-12,
) -> float:
    """Return the maximum probability difference for matching pulse support."""

    _require_nonnegative("pulse_count_tolerance", pulse_count_tolerance)
    first = _coalesced_points(first_response.points, pulse_count_tolerance)
    second = _coalesced_points(second_response.points, pulse_count_tolerance)
    if len(first) != len(second):
        return math.inf
    max_difference = 0.0
    for first_point, second_point in zip(first, second, strict=True):
        if not math.isclose(
            first_point.pulse_count,
            second_point.pulse_count,
            rel_tol=0.0,
            abs_tol=pulse_count_tolerance,
        ):
            return math.inf
        max_difference = max(max_difference, abs(first_point.probability - second_point.probability))
    return max_difference


def _validated_state_vector(vector: Sequence[complex]) -> Vector:
    values = tuple(complex(value) for value in vector)
    if not values:
        raise ValueError("state vector must not be empty")
    norm = 0.0
    for value in values:
        _require_finite_complex("state vector entry", value)
        norm += abs(value) ** 2
    if not math.isclose(norm, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise ValueError("state vector must be normalized")
    return values


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


def _validated_density_matrix(matrix: Sequence[Sequence[complex]], name: str) -> Matrix:
    rows = _validated_square_matrix(matrix, name)
    _require_hermitian(name, rows)
    _require_positive_semidefinite(name, rows)
    trace = _trace(rows)
    if abs(trace.imag) > 1.0e-12:
        raise ValueError(f"{name} trace must be real")
    if not math.isclose(trace.real, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise ValueError(f"{name} trace must be 1")
    return rows


def _require_hermitian(name: str, matrix: Matrix) -> None:
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if abs(matrix[row][col] - matrix[col][row].conjugate()) > 1.0e-12:
                raise ValueError(f"{name} must be Hermitian")


def _require_positive_semidefinite(name: str, matrix: Matrix) -> None:
    dimension = len(matrix)
    for size in range(1, dimension + 1):
        for indices in combinations(range(dimension), size):
            minor = tuple(tuple(matrix[row][col] for col in indices) for row in indices)
            determinant = _determinant(minor)
            if abs(determinant.imag) > 1.0e-10:
                raise ValueError(f"{name} principal minors must be real")
            if determinant.real < -1.0e-12:
                raise ValueError(f"{name} must be positive semidefinite")


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


def _require_same_dimension(first: Matrix, second: Matrix) -> None:
    if len(first) != len(second):
        raise ValueError("matrices must have the same dimension")


def _matrix_max_abs_difference(first: Matrix, second: Matrix) -> float:
    max_difference = 0.0
    for row in range(len(first)):
        for col in range(len(first)):
            max_difference = max(max_difference, abs(first[row][col] - second[row][col]))
    return max_difference


def _coalesced_points(
    points: Sequence[ResponsePoint],
    pulse_count_tolerance: float,
) -> tuple[ResponsePoint, ...]:
    sorted_points = sorted((point for point in points if point.probability > 0.0), key=lambda point: point.pulse_count)
    if not sorted_points:
        return ()

    merged: list[ResponsePoint] = []
    current_probability = sorted_points[0].probability
    current_weighted_count = sorted_points[0].pulse_count * sorted_points[0].probability
    current_reference = sorted_points[0].pulse_count

    for point in sorted_points[1:]:
        if math.isclose(point.pulse_count, current_reference, rel_tol=0.0, abs_tol=pulse_count_tolerance):
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


def _require_positive(name: str, value: float) -> None:
    _require_finite_real(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _require_probability(name: str, value: float) -> None:
    _require_nonnegative(name, value)
    if value > 1.0:
        raise ValueError(f"{name} must be at most 1")
