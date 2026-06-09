"""Finite H6P1 pulse-closure response diagnostics.

The helpers in this module implement a small executable analogue of the H6P1
closure-response proposal. They compute closed-loop defects, the intrinsic
covariance-weighted closure functional, and finite response components for
declared metric/control sensitivities. The code deliberately classifies the
result conservatively; it does not promote closure machinery to a new law
without covariance, conservation, coefficient, and baseline ledgers.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, replace
from itertools import combinations
import math

from .calculations import REDUCED_PLANCK_CONSTANT_J_S
from .causal_pulse_response import (
    CoefficientLedger,
    ConservationLedger,
    EnsembleDecomposition,
    EnsembleInvarianceReport,
    PulsePotentialOperator,
    decomposition_distance,
    ensemble_density_matrix,
)


Matrix = tuple[tuple[float, ...], ...]
ComplexMatrix = tuple[tuple[complex, ...], ...]

CLOSURE_RESULT_CLASSIFICATIONS = frozenset(
    {
        "controlled modification",
        "conditional derivation",
        "clean no-go",
        "diagnostic tool",
    }
)
BASELINE_RELATION_LABELS = frozenset(
    {
        "not-compared",
        "same-as-h6s4c-stochastic",
        "same-as-h6s4q-quantum-mediator",
        "distinct-observable",
        "not-applicable",
    }
)


@dataclass(frozen=True)
class ClosureEdgeRecord:
    """One oriented edge phase or pulse record."""

    edge_id: str
    start_id: str
    end_id: str
    value: float

    def __post_init__(self) -> None:
        _require_nonempty_string("edge_id", self.edge_id)
        _require_nonempty_string("start_id", self.start_id)
        _require_nonempty_string("end_id", self.end_id)
        if self.start_id == self.end_id:
            raise ValueError("edge endpoints must differ")
        _require_finite_real("edge value", self.value)


@dataclass(frozen=True)
class ClosureEdgeObservable:
    """Finite Hermitian edge observable used to derive records from a state."""

    edge_id: str
    start_id: str
    end_id: str
    operator: PulsePotentialOperator

    def __post_init__(self) -> None:
        _require_nonempty_string("edge_id", self.edge_id)
        _require_nonempty_string("start_id", self.start_id)
        _require_nonempty_string("end_id", self.end_id)
        if self.start_id == self.end_id:
            raise ValueError("edge observable endpoints must differ")


@dataclass(frozen=True)
class ClosedPulseLoop:
    """Closed loop represented by signed edge-incidence coefficients."""

    loop_id: str
    edge_coefficients: Mapping[str, float] | Sequence[tuple[str, float]]

    def __post_init__(self) -> None:
        _require_nonempty_string("loop_id", self.loop_id)
        coefficients = _validated_coefficients(self.edge_coefficients)
        object.__setattr__(self, "edge_coefficients", coefficients)


@dataclass(frozen=True)
class ClosureDefect:
    """One loop closure defect."""

    loop_id: str
    defect: float

    def __post_init__(self) -> None:
        _require_nonempty_string("loop_id", self.loop_id)
        _require_finite_real("closure defect", self.defect)


@dataclass(frozen=True)
class ClosureCovarianceKernel:
    """Intrinsic closure covariance plus a separate ordinary-noise ledger."""

    intrinsic_matrix: Sequence[Sequence[float]]
    ordinary_instrument_noise_matrix: Sequence[Sequence[float]] | None = None

    def __post_init__(self) -> None:
        intrinsic = _validated_positive_definite_matrix(
            self.intrinsic_matrix,
            "intrinsic closure covariance",
        )
        ordinary = (
            None
            if self.ordinary_instrument_noise_matrix is None
            else _validated_symmetric_nonnegative_matrix(
                self.ordinary_instrument_noise_matrix,
                "ordinary instrument noise covariance",
                len(intrinsic),
            )
        )
        object.__setattr__(self, "intrinsic_matrix", intrinsic)
        object.__setattr__(self, "ordinary_instrument_noise_matrix", ordinary)

    @property
    def dimension(self) -> int:
        return len(self.intrinsic_matrix)


@dataclass(frozen=True)
class ClosureMetricSensitivity:
    """Finite derivative of edge records with respect to one control parameter."""

    parameter: str
    edge_derivatives: Mapping[str, float] | Sequence[tuple[str, float]]

    def __post_init__(self) -> None:
        _require_nonempty_string("parameter", self.parameter)
        derivatives = _validated_coefficients(self.edge_derivatives)
        object.__setattr__(self, "edge_derivatives", derivatives)


@dataclass(frozen=True)
class ClosureResponseComponent:
    """One finite response component, $J_a=-hbar dI/dg_a$."""

    parameter: str
    value: float

    def __post_init__(self) -> None:
        _require_nonempty_string("parameter", self.parameter)
        _require_finite_real("response component", self.value)


@dataclass(frozen=True)
class ClosureFunctionalReport:
    """Computed closure functional using intrinsic covariance only."""

    defects: tuple[ClosureDefect, ...]
    intrinsic_functional: float
    ordinary_instrument_noise_trace: float
    covariance_dimension: int

    def __post_init__(self) -> None:
        if not self.defects:
            raise ValueError("functional report requires at least one defect")
        _require_nonnegative("intrinsic_functional", self.intrinsic_functional)
        _require_nonnegative(
            "ordinary_instrument_noise_trace",
            self.ordinary_instrument_noise_trace,
        )
        _require_positive_int("covariance_dimension", self.covariance_dimension)


@dataclass(frozen=True)
class ClosureGaugeInvarianceReport:
    """Report for pure node-potential relabeling of closed edge records."""

    max_defect_difference: float
    invariant: bool
    reason: str

    def __post_init__(self) -> None:
        _require_nonnegative("max_defect_difference", self.max_defect_difference)
        _require_nonempty_string("reason", self.reason)


@dataclass(frozen=True)
class ClosureBaselineLedger:
    """Baseline comparison ledger for H6P1 promotion discipline."""

    h6s4c_relation: str = "not-compared"
    h6s4q_relation: str = "not-compared"
    fixed_observable_distinct_from_baselines: bool = False

    def __post_init__(self) -> None:
        _require_label("h6s4c_relation", self.h6s4c_relation, BASELINE_RELATION_LABELS)
        _require_label("h6s4q_relation", self.h6s4q_relation, BASELINE_RELATION_LABELS)

    @property
    def h6s4c_compared(self) -> bool:
        return self.h6s4c_relation != "not-compared"

    @property
    def h6s4q_compared(self) -> bool:
        return self.h6s4q_relation != "not-compared"

    @property
    def reduces_to_known_baseline(self) -> bool:
        return (
            self.h6s4c_relation == "same-as-h6s4c-stochastic"
            or self.h6s4q_relation == "same-as-h6s4q-quantum-mediator"
        )

    @property
    def distinct_from_required_baselines(self) -> bool:
        return (
            self.h6s4c_relation == "distinct-observable"
            and self.h6s4q_relation == "distinct-observable"
        )


@dataclass(frozen=True)
class ClosureResponseClassification:
    """Result classification after H6P1 ledgers are applied."""

    classification: str
    candidate_ready: bool
    promotion_blocked: bool
    reasons: tuple[str, ...]
    missing_requirements: tuple[str, ...]
    accepted_as_law: bool = False

    def __post_init__(self) -> None:
        _require_label(
            "classification",
            self.classification,
            CLOSURE_RESULT_CLASSIFICATIONS,
        )
        for reason in self.reasons:
            _require_nonempty_string("classification reason", reason)
        for requirement in self.missing_requirements:
            _require_nonempty_string("missing requirement", requirement)
        if self.accepted_as_law:
            raise ValueError("H6P1 helpers cannot mark a response accepted as law")


@dataclass(frozen=True)
class ClosureResponseReport:
    """Finite closure response report."""

    functional_report: ClosureFunctionalReport | None
    response_components: tuple[ClosureResponseComponent, ...]
    classification: ClosureResponseClassification
    baseline_ledger: ClosureBaselineLedger
    conservation_status: str
    coefficient_provenance: str
    gauge_invariant: bool
    ordinary_noise_separate: bool
    artifact_ledger: tuple[str, ...]
    diagnostic_only: bool
    accepted_as_law: bool = False

    def __post_init__(self) -> None:
        for artifact in self.artifact_ledger:
            _require_nonempty_string("artifact ledger entry", artifact)
        if self.accepted_as_law:
            raise ValueError("H6P1 helpers cannot mark a response accepted as law")


@dataclass(frozen=True)
class ClosureEnsembleComparisonReport:
    """Comparison of closure responses from two ensemble decompositions."""

    first_report: ClosureResponseReport
    second_report: ClosureResponseReport
    ensemble_invariance: EnsembleInvarianceReport
    same_closure_response: bool
    accepted_as_law: bool = False

    def __post_init__(self) -> None:
        if self.accepted_as_law:
            raise ValueError("ensemble comparison cannot accept H6P1 as law")


@dataclass(frozen=True)
class ClosureBaselineComparisonReport:
    """Summary of H6P1 comparison against H6S4-C and H6S4-Q baselines."""

    h6s4c_relation: str
    h6s4q_relation: str
    fixed_observable_distinct_from_baselines: bool
    not_new_physics_claim: bool
    classification: str
    accepted_as_law: bool = False

    def __post_init__(self) -> None:
        _require_label("h6s4c_relation", self.h6s4c_relation, BASELINE_RELATION_LABELS)
        _require_label("h6s4q_relation", self.h6s4q_relation, BASELINE_RELATION_LABELS)
        _require_label(
            "classification",
            self.classification,
            CLOSURE_RESULT_CLASSIFICATIONS,
        )
        if self.accepted_as_law:
            raise ValueError("baseline comparison cannot accept H6P1 as law")


def closure_defect(loop: ClosedPulseLoop, edge_records: Iterable[ClosureEdgeRecord]) -> ClosureDefect:
    """Return the signed edge sum for one closed loop."""

    edge_map = _edge_record_map(edge_records)
    _require_closed_loop_incidence(loop, edge_map)
    defect = math.fsum(
        coefficient * edge_map[edge_id].value
        for edge_id, coefficient in loop.edge_coefficients
    )
    return ClosureDefect(loop.loop_id, defect)


def closure_defects(
    loops: Iterable[ClosedPulseLoop],
    edge_records: Iterable[ClosureEdgeRecord],
) -> tuple[ClosureDefect, ...]:
    """Return closure defects for a finite ordered loop family."""

    loop_tuple = tuple(loops)
    if not loop_tuple:
        raise ValueError("loops must not be empty")
    loop_ids = [loop.loop_id for loop in loop_tuple]
    if len(set(loop_ids)) != len(loop_ids):
        raise ValueError("loop ids must be unique")
    edge_tuple = tuple(edge_records)
    return tuple(closure_defect(loop, edge_tuple) for loop in loop_tuple)


def reverse_closed_loop_orientation(loop: ClosedPulseLoop) -> ClosedPulseLoop:
    """Return the same loop traversed in the opposite orientation."""

    return replace(
        loop,
        edge_coefficients=tuple(
            (edge_id, -coefficient) for edge_id, coefficient in loop.edge_coefficients
        ),
    )


def apply_pure_gauge_relabeling(
    edge_records: Iterable[ClosureEdgeRecord],
    node_offsets: Mapping[str, float],
) -> tuple[ClosureEdgeRecord, ...]:
    """Apply a pure node-potential relabeling to edge records."""

    offsets = dict(node_offsets)
    for node_id, offset in offsets.items():
        _require_nonempty_string("node offset id", node_id)
        _require_finite_real("node offset", offset)
    shifted: list[ClosureEdgeRecord] = []
    for edge in edge_records:
        start_offset = offsets.get(edge.start_id, 0.0)
        end_offset = offsets.get(edge.end_id, 0.0)
        shifted.append(
            replace(edge, value=edge.value + end_offset - start_offset)
        )
    return tuple(shifted)


def check_pure_gauge_invariance(
    loops: Iterable[ClosedPulseLoop],
    edge_records: Iterable[ClosureEdgeRecord],
    node_offsets: Mapping[str, float],
    *,
    tolerance: float = 1.0e-12,
) -> ClosureGaugeInvarianceReport:
    """Check that closed-loop defects are unchanged by pure gauge relabeling."""

    _require_nonnegative("tolerance", tolerance)
    loop_tuple = tuple(loops)
    edge_tuple = tuple(edge_records)
    shifted = apply_pure_gauge_relabeling(edge_tuple, node_offsets)
    before = closure_defects(loop_tuple, edge_tuple)
    after = closure_defects(loop_tuple, shifted)
    max_difference = max(
        (abs(first.defect - second.defect) for first, second in zip(before, after, strict=True)),
        default=0.0,
    )
    invariant = max_difference <= tolerance
    reason = (
        "closed loop defects are invariant under node-potential relabeling"
        if invariant
        else "pure gauge relabeling changed at least one loop defect"
    )
    return ClosureGaugeInvarianceReport(max_difference, invariant, reason)


def closure_functional(
    loops: Iterable[ClosedPulseLoop],
    edge_records: Iterable[ClosureEdgeRecord],
    covariance_kernel: ClosureCovarianceKernel,
) -> ClosureFunctionalReport:
    """Return the quadratic closure functional using intrinsic covariance."""

    loop_tuple = tuple(loops)
    defects = closure_defects(loop_tuple, edge_records)
    if covariance_kernel.dimension != len(defects):
        raise ValueError("covariance dimension must match number of loop defects")
    inverse = _inverse_matrix(covariance_kernel.intrinsic_matrix)
    defect_vector = tuple(defect.defect for defect in defects)
    intrinsic_functional = 0.5 * _quadratic_form(defect_vector, inverse)
    if intrinsic_functional < 0.0 and abs(intrinsic_functional) <= 1.0e-12:
        intrinsic_functional = 0.0
    _require_nonnegative("closure functional", intrinsic_functional)
    ordinary_noise_trace = (
        0.0
        if covariance_kernel.ordinary_instrument_noise_matrix is None
        else math.fsum(
            covariance_kernel.ordinary_instrument_noise_matrix[index][index]
            for index in range(covariance_kernel.dimension)
        )
    )
    return ClosureFunctionalReport(
        defects=defects,
        intrinsic_functional=intrinsic_functional,
        ordinary_instrument_noise_trace=ordinary_noise_trace,
        covariance_dimension=covariance_kernel.dimension,
    )


def finite_closure_response(
    loops: Iterable[ClosedPulseLoop],
    edge_records: Iterable[ClosureEdgeRecord],
    covariance_kernel: ClosureCovarianceKernel | None,
    sensitivities: Iterable[ClosureMetricSensitivity],
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    baseline_ledger: ClosureBaselineLedger,
    *,
    artifact_ledger: Sequence[str],
    gauge_invariant: bool = True,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> ClosureResponseReport:
    """Return the finite analogue of $J_a=-hbar dI/dg_a$.

    The covariance is treated as fixed with respect to the declared finite
    control parameters. If no covariance kernel is supplied, the report is
    still returned, but promotion is blocked and no response is computed.
    """

    loop_tuple = tuple(loops)
    edge_tuple = tuple(edge_records)
    sensitivity_tuple = tuple(sensitivities)
    artifacts = _validated_artifact_ledger(artifact_ledger)
    _require_positive("reduced_planck_constant_j_s", reduced_planck_constant_j_s)
    closure_defects(loop_tuple, edge_tuple)

    functional_report: ClosureFunctionalReport | None = None
    response_components: tuple[ClosureResponseComponent, ...] = ()
    if covariance_kernel is not None:
        functional_report = closure_functional(loop_tuple, edge_tuple, covariance_kernel)
        inverse = _inverse_matrix(covariance_kernel.intrinsic_matrix)
        defect_vector = tuple(defect.defect for defect in functional_report.defects)
        response_components = tuple(
            _response_component(
                loop_tuple,
                sensitivity,
                inverse,
                defect_vector,
                reduced_planck_constant_j_s,
            )
            for sensitivity in sensitivity_tuple
        )

    classification = classify_closure_response(
        covariance_kernel,
        conservation_ledger,
        coefficient_ledger,
        baseline_ledger,
        artifact_ledger=artifacts,
        gauge_invariant=gauge_invariant,
        response_components=response_components,
    )
    ordinary_noise_separate = (
        covariance_kernel is not None
        and covariance_kernel.ordinary_instrument_noise_matrix is not None
    )
    return ClosureResponseReport(
        functional_report=functional_report,
        response_components=response_components,
        classification=classification,
        baseline_ledger=baseline_ledger,
        conservation_status=conservation_ledger.status,
        coefficient_provenance=coefficient_ledger.provenance,
        gauge_invariant=gauge_invariant,
        ordinary_noise_separate=ordinary_noise_separate,
        artifact_ledger=artifacts,
        diagnostic_only=classification.classification == "diagnostic tool"
        or classification.promotion_blocked,
        accepted_as_law=False,
    )


def classify_closure_response(
    covariance_kernel: ClosureCovarianceKernel | None,
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    baseline_ledger: ClosureBaselineLedger,
    *,
    artifact_ledger: Sequence[str],
    gauge_invariant: bool,
    response_components: Sequence[ClosureResponseComponent],
) -> ClosureResponseClassification:
    """Classify the H6P1 closure-response attempt."""

    artifacts = _validated_artifact_ledger(artifact_ledger)
    missing: list[str] = []
    reasons: list[str] = []

    if not gauge_invariant:
        return ClosureResponseClassification(
            classification="clean no-go",
            candidate_ready=False,
            promotion_blocked=True,
            reasons=("no gauge-invariant closure functional survived pure relabeling",),
            missing_requirements=("gauge-invariant closure functional",),
        )

    if covariance_kernel is None:
        missing.append("intrinsic closure covariance kernel")

    if conservation_ledger.status not in {"branchwise-conserved", "expectation-conserved"}:
        missing.append("conservation proof")
    elif not conservation_ledger.accounting_source:
        missing.append("conservation accounting source")

    if coefficient_ledger.provenance == "fit-after-observation rejected":
        reasons.append("fit-after-observation coefficient provenance is rejected")
    elif coefficient_ledger.provenance == "exploratory-only":
        missing.append("non-exploratory coefficient provenance")

    if not baseline_ledger.h6s4c_compared or not baseline_ledger.h6s4q_compared:
        missing.append("H6S4-C and H6S4-Q baseline comparison")

    if not artifacts:
        missing.append("artifact ledger")

    if not response_components:
        reasons.append("no finite response sensitivity produced a response component")
    if (
        baseline_ledger.fixed_observable_distinct_from_baselines
        and not baseline_ledger.distinct_from_required_baselines
    ):
        reasons.append(
            "fixed observable distinction must be distinct from both H6S4-C and H6S4-Q baselines"
        )

    if reasons or missing:
        return ClosureResponseClassification(
            classification="diagnostic tool",
            candidate_ready=False,
            promotion_blocked=True,
            reasons=tuple(reasons + [f"missing {item}" for item in missing]),
            missing_requirements=tuple(missing),
        )

    if (
        baseline_ledger.fixed_observable_distinct_from_baselines
        and baseline_ledger.distinct_from_required_baselines
    ):
        return ClosureResponseClassification(
            classification="controlled modification",
            candidate_ready=True,
            promotion_blocked=False,
            reasons=("complete ledgers and fixed baseline-distinct observable",),
            missing_requirements=(),
        )

    if baseline_ledger.reduces_to_known_baseline:
        return ClosureResponseClassification(
            classification="conditional derivation",
            candidate_ready=True,
            promotion_blocked=False,
            reasons=("closure response reduces to a declared H6S4 baseline structure",),
            missing_requirements=(),
        )

    return ClosureResponseClassification(
        classification="diagnostic tool",
        candidate_ready=True,
        promotion_blocked=False,
        reasons=("closure machinery is defined, but no baseline-distinct observable survives",),
        missing_requirements=(),
    )


def closure_edge_records_from_density(
    density_matrix: Sequence[Sequence[complex]],
    edge_observables: Iterable[ClosureEdgeObservable],
) -> tuple[ClosureEdgeRecord, ...]:
    """Compute edge records from finite density-matrix expectation values."""

    density = _validated_density_matrix(density_matrix, "density_matrix")
    records: list[ClosureEdgeRecord] = []
    for observable in edge_observables:
        if len(density) != observable.operator.dimension:
            raise ValueError("density matrix and edge operator dimensions must match")
        expectation = _trace_product(density, observable.operator.matrix)
        if abs(expectation.imag) > 1.0e-10:
            raise ValueError("edge observable expectation must be real within tolerance")
        records.append(
            ClosureEdgeRecord(
                observable.edge_id,
                observable.start_id,
                observable.end_id,
                expectation.real,
            )
        )
    return tuple(records)


def compare_closure_responses_for_decompositions(
    first_decomposition: EnsembleDecomposition,
    second_decomposition: EnsembleDecomposition,
    edge_observables: Iterable[ClosureEdgeObservable],
    loops: Iterable[ClosedPulseLoop],
    covariance_kernel: ClosureCovarianceKernel | None,
    sensitivities: Iterable[ClosureMetricSensitivity],
    conservation_ledger: ConservationLedger,
    coefficient_ledger: CoefficientLedger,
    baseline_ledger: ClosureBaselineLedger,
    *,
    artifact_ledger: Sequence[str],
    gauge_invariant: bool = True,
    tolerance: float = 1.0e-12,
) -> ClosureEnsembleComparisonReport:
    """Compare closure responses for two decompositions of a density matrix."""

    _require_nonnegative("tolerance", tolerance)
    observable_tuple = tuple(edge_observables)
    loop_tuple = tuple(loops)
    sensitivity_tuple = tuple(sensitivities)
    first_records = closure_edge_records_from_density(
        ensemble_density_matrix(first_decomposition),
        observable_tuple,
    )
    second_records = closure_edge_records_from_density(
        ensemble_density_matrix(second_decomposition),
        observable_tuple,
    )
    first_report = finite_closure_response(
        loop_tuple,
        first_records,
        covariance_kernel,
        sensitivity_tuple,
        conservation_ledger,
        coefficient_ledger,
        baseline_ledger,
        artifact_ledger=artifact_ledger,
        gauge_invariant=gauge_invariant,
    )
    second_report = finite_closure_response(
        loop_tuple,
        second_records,
        covariance_kernel,
        sensitivity_tuple,
        conservation_ledger,
        coefficient_ledger,
        baseline_ledger,
        artifact_ledger=artifact_ledger,
        gauge_invariant=gauge_invariant,
    )
    density_distance = decomposition_distance(first_decomposition, second_decomposition)
    response_difference = closure_response_max_difference(first_report, second_report)
    invariant = density_distance <= tolerance and response_difference <= tolerance
    if density_distance > tolerance:
        reason = "decompositions represent different density matrices"
    elif invariant:
        reason = "same density matrix gives same closure response"
    else:
        reason = "same density matrix gives different closure responses"
    return ClosureEnsembleComparisonReport(
        first_report=first_report,
        second_report=second_report,
        ensemble_invariance=EnsembleInvarianceReport(
            density_matrix_distance=density_distance,
            max_marginal_difference=response_difference,
            invariant=invariant,
            reason=reason,
        ),
        same_closure_response=invariant,
        accepted_as_law=False,
    )


def closure_response_max_difference(
    first_report: ClosureResponseReport,
    second_report: ClosureResponseReport,
) -> float:
    """Return a finite max difference across response components and $I$."""

    differences: list[float] = []
    if first_report.functional_report is not None and second_report.functional_report is not None:
        if len(first_report.functional_report.defects) != len(second_report.functional_report.defects):
            return math.inf
        for first, second in zip(
            first_report.functional_report.defects,
            second_report.functional_report.defects,
            strict=True,
        ):
            if first.loop_id != second.loop_id:
                return math.inf
            differences.append(abs(first.defect - second.defect))
        differences.append(
            abs(
                first_report.functional_report.intrinsic_functional
                - second_report.functional_report.intrinsic_functional
            )
        )
    elif first_report.functional_report is not None or second_report.functional_report is not None:
        return math.inf
    if len(first_report.response_components) != len(second_report.response_components):
        return math.inf
    for first, second in zip(
        first_report.response_components,
        second_report.response_components,
        strict=True,
    ):
        if first.parameter != second.parameter:
            return math.inf
        differences.append(abs(first.value - second.value))
    return max(differences, default=0.0)


def compare_closure_baselines(report: ClosureResponseReport) -> ClosureBaselineComparisonReport:
    """Return the declared H6S4-C/Q baseline comparison summary."""

    return ClosureBaselineComparisonReport(
        h6s4c_relation=report.baseline_ledger.h6s4c_relation,
        h6s4q_relation=report.baseline_ledger.h6s4q_relation,
        fixed_observable_distinct_from_baselines=(
            report.baseline_ledger.fixed_observable_distinct_from_baselines
        ),
        not_new_physics_claim=(
            not report.baseline_ledger.fixed_observable_distinct_from_baselines
            or report.classification.classification != "controlled modification"
        ),
        classification=report.classification.classification,
        accepted_as_law=False,
    )


def _response_component(
    loops: Sequence[ClosedPulseLoop],
    sensitivity: ClosureMetricSensitivity,
    inverse_covariance: Matrix,
    defect_vector: Sequence[float],
    reduced_planck_constant_j_s: float,
) -> ClosureResponseComponent:
    derivatives = dict(sensitivity.edge_derivatives)
    derivative_vector = tuple(
        math.fsum(
            coefficient * derivatives.get(edge_id, 0.0)
            for edge_id, coefficient in loop.edge_coefficients
        )
        for loop in loops
    )
    derivative = _bilinear_form(derivative_vector, inverse_covariance, defect_vector)
    return ClosureResponseComponent(
        sensitivity.parameter,
        -reduced_planck_constant_j_s * derivative,
    )


def _edge_record_map(edge_records: Iterable[ClosureEdgeRecord]) -> dict[str, ClosureEdgeRecord]:
    records: dict[str, ClosureEdgeRecord] = {}
    for edge in edge_records:
        if edge.edge_id in records:
            raise ValueError("edge ids must be unique")
        records[edge.edge_id] = edge
    if not records:
        raise ValueError("edge records must not be empty")
    return records


def _require_closed_loop_incidence(
    loop: ClosedPulseLoop,
    edge_records: Mapping[str, ClosureEdgeRecord],
) -> None:
    node_balances: dict[str, float] = {}
    for edge_id, coefficient in loop.edge_coefficients:
        if edge_id not in edge_records:
            raise ValueError("loop references an unknown edge id")
        edge = edge_records[edge_id]
        node_balances[edge.start_id] = node_balances.get(edge.start_id, 0.0) - coefficient
        node_balances[edge.end_id] = node_balances.get(edge.end_id, 0.0) + coefficient
    for node_id, balance in node_balances.items():
        if not math.isclose(balance, 0.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
            raise ValueError(f"loop edge coefficients must close at node {node_id!r}")


def _validated_coefficients(
    coefficients: Mapping[str, float] | Sequence[tuple[str, float]],
) -> tuple[tuple[str, float], ...]:
    if isinstance(coefficients, Mapping):
        items = tuple(coefficients.items())
    else:
        items = tuple(coefficients)
    if not items:
        raise ValueError("coefficients must not be empty")
    seen: set[str] = set()
    validated: list[tuple[str, float]] = []
    nonzero = False
    for edge_id, coefficient in items:
        _require_nonempty_string("edge coefficient id", edge_id)
        if edge_id in seen:
            raise ValueError("edge coefficient ids must be unique")
        seen.add(edge_id)
        _require_finite_real("edge coefficient", coefficient)
        if coefficient != 0.0:
            nonzero = True
        validated.append((edge_id, float(coefficient)))
    if not nonzero:
        raise ValueError("at least one coefficient must be nonzero")
    return tuple(sorted(validated))


def _validated_artifact_ledger(artifact_ledger: Sequence[str]) -> tuple[str, ...]:
    artifacts = tuple(artifact_ledger)
    for artifact in artifacts:
        _require_nonempty_string("artifact ledger entry", artifact)
    return artifacts


def _validated_matrix(matrix: Sequence[Sequence[float]], name: str) -> Matrix:
    rows = tuple(tuple(float(entry) for entry in row) for row in matrix)
    if not rows:
        raise ValueError(f"{name} must not be empty")
    dimension = len(rows)
    for row in rows:
        if len(row) != dimension:
            raise ValueError(f"{name} must be square")
        for entry in row:
            _require_finite_real(name, entry)
    return rows


def _validated_positive_definite_matrix(matrix: Sequence[Sequence[float]], name: str) -> Matrix:
    rows = _validated_matrix(matrix, name)
    _require_symmetric(rows, name)
    _cholesky_positive_definite(rows, name)
    return rows


def _validated_symmetric_nonnegative_matrix(
    matrix: Sequence[Sequence[float]],
    name: str,
    expected_dimension: int,
) -> Matrix:
    rows = _validated_matrix(matrix, name)
    if len(rows) != expected_dimension:
        raise ValueError(f"{name} dimension must match intrinsic covariance")
    _require_symmetric(rows, name)
    for index in range(len(rows)):
        _require_nonnegative(f"{name} diagonal", rows[index][index])
    _require_positive_semidefinite(
        name,
        tuple(tuple(complex(entry) for entry in row) for row in rows),
    )
    return rows


def _require_symmetric(matrix: Matrix, name: str) -> None:
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            if not math.isclose(matrix[row][col], matrix[col][row], rel_tol=1.0e-12, abs_tol=1.0e-12):
                raise ValueError(f"{name} must be symmetric")


def _cholesky_positive_definite(matrix: Matrix, name: str) -> None:
    dimension = len(matrix)
    lower = [[0.0 for _ in range(dimension)] for _ in range(dimension)]
    for row in range(dimension):
        for col in range(row + 1):
            value = matrix[row][col] - math.fsum(
                lower[row][k] * lower[col][k] for k in range(col)
            )
            if row == col:
                if value <= 1.0e-15:
                    raise ValueError(f"{name} must be positive definite")
                lower[row][col] = math.sqrt(value)
            else:
                lower[row][col] = value / lower[col][col]


def _inverse_matrix(matrix: Matrix) -> Matrix:
    dimension = len(matrix)
    augmented = [
        [float(matrix[row][col]) for col in range(dimension)]
        + [1.0 if row == col else 0.0 for col in range(dimension)]
        for row in range(dimension)
    ]
    for col in range(dimension):
        pivot_row = max(range(col, dimension), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot_row][col]) <= 1.0e-15:
            raise ValueError("matrix is singular")
        if pivot_row != col:
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]
        pivot = augmented[col][col]
        augmented[col] = [entry / pivot for entry in augmented[col]]
        for row in range(dimension):
            if row == col:
                continue
            factor = augmented[row][col]
            if factor:
                augmented[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(augmented[row], augmented[col], strict=True)
                ]
    return tuple(tuple(row[dimension:]) for row in augmented)


def _quadratic_form(vector: Sequence[float], matrix: Matrix) -> float:
    return _bilinear_form(vector, matrix, vector)


def _bilinear_form(first: Sequence[float], matrix: Matrix, second: Sequence[float]) -> float:
    if len(first) != len(matrix) or len(second) != len(matrix):
        raise ValueError("vector and matrix dimensions must match")
    return math.fsum(
        first[row] * matrix[row][col] * second[col]
        for row in range(len(matrix))
        for col in range(len(matrix))
    )


def _validated_density_matrix(
    matrix: Sequence[Sequence[complex]],
    name: str,
) -> ComplexMatrix:
    rows = tuple(tuple(complex(entry) for entry in row) for row in matrix)
    if not rows:
        raise ValueError(f"{name} must not be empty")
    dimension = len(rows)
    for row in rows:
        if len(row) != dimension:
            raise ValueError(f"{name} must be square")
        for value in row:
            _require_finite_complex(f"{name} entry", value)
    for row in range(dimension):
        for col in range(row, dimension):
            if abs(rows[row][col] - rows[col][row].conjugate()) > 1.0e-12:
                raise ValueError(f"{name} must be Hermitian")
    _require_positive_semidefinite(name, rows)
    trace = sum(rows[index][index] for index in range(dimension))
    if abs(trace.imag) > 1.0e-12 or not math.isclose(trace.real, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise ValueError(f"{name} trace must equal 1")
    for index in range(dimension):
        if rows[index][index].real < -1.0e-12:
            raise ValueError(f"{name} diagonal probabilities must be nonnegative")
    return rows


def _require_positive_semidefinite(name: str, matrix: ComplexMatrix) -> None:
    dimension = len(matrix)
    for size in range(1, dimension + 1):
        for indices in combinations(range(dimension), size):
            minor = tuple(tuple(matrix[row][col] for col in indices) for row in indices)
            determinant = _determinant(minor)
            if abs(determinant.imag) > 1.0e-10:
                raise ValueError(f"{name} principal minors must be real")
            if determinant.real < -1.0e-12:
                raise ValueError(f"{name} must be positive semidefinite")


def _determinant(matrix: ComplexMatrix) -> complex:
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


def _trace_product(first: Sequence[Sequence[complex]], second: Sequence[Sequence[complex]]) -> complex:
    if len(first) != len(second):
        raise ValueError("trace product dimensions must match")
    dimension = len(first)
    return sum(
        first[row][col] * second[col][row]
        for row in range(dimension)
        for col in range(dimension)
    )


def _require_label(name: str, value: str, allowed: frozenset[str]) -> None:
    if value not in allowed:
        raise ValueError(f"{name} must be one of {sorted(allowed)}")


def _require_nonempty_string(name: str, value: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a nonempty string")


def _require_finite_real(name: str, value: float) -> None:
    if not isinstance(value, int | float) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite real number")


def _require_finite_complex(name: str, value: complex) -> None:
    if not math.isfinite(value.real) or not math.isfinite(value.imag):
        raise ValueError(f"{name} must be finite")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite_real(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_positive(name: str, value: float) -> None:
    _require_finite_real(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _require_positive_int(name: str, value: int) -> None:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
