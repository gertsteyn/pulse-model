"""Focused H6S3 no-free-branch-variance helpers.

The helpers reuse the finite H6S2 response-distribution API. They compute
ordinary finite moments, compare branch-variance diagnostics across equivalent
decompositions, and classify the route a claimed branch variance belongs to.
They do not promote any route to a new prediction or accepted law.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .causal_pulse_response import (
    EnsembleDecomposition,
    ResponseDistribution,
    decomposition_distance,
    response_marginal_max_difference,
)


BRANCH_VARIANCE_ROUTE_LABELS = frozenset(
    {
        "density-only-baseline",
        "pointer-record-or-collapse-record",
        "stochastic-classical-pulse-geometry",
        "non-classical-geometry-or-mediator",
        "unsupported-decomposition",
    }
)


@dataclass(frozen=True)
class ResponseMoments:
    """Mean and variance of a finite probe pulse-count distribution."""

    mean: float
    variance: float
    family: str


@dataclass(frozen=True)
class BranchVarianceRouteClassification:
    """Diagnostic route classification for a claimed branch variance."""

    route: str
    physical_branch_variance_allowed: bool
    diagnostic_only: bool
    accepted_as_law: bool
    reason: str
    missing_requirements: tuple[str, ...]


@dataclass(frozen=True)
class NoFreeBranchVarianceReport:
    """Comparison report for H6S3 finite branch-variance diagnostics."""

    density_matrix_distance: float
    max_marginal_difference: float
    first_response_mean: float
    second_response_mean: float
    first_branch_variance: float
    second_branch_variance: float
    branch_variance_difference: float
    same_density: bool
    same_probe_marginal: bool
    branch_variance_changes: bool
    diagnostic_failure: bool
    route_classification: BranchVarianceRouteClassification
    diagnostic_only: bool
    accepted_as_law: bool
    reason: str


def response_moments(response: ResponseDistribution) -> ResponseMoments:
    """Return finite mean and variance for a normalized response distribution."""

    _validate_response_distribution(response)
    mean = math.fsum(point.pulse_count * point.probability for point in response.points)
    variance = math.fsum(
        point.probability * (point.pulse_count - mean) ** 2
        for point in response.points
    )
    _require_finite_real("response mean", mean)
    _require_nonnegative("response variance", variance)
    return ResponseMoments(mean=mean, variance=variance, family=response.family)


def response_mean(response: ResponseDistribution) -> float:
    """Return the finite mean pulse count for a response distribution."""

    return response_moments(response).mean


def response_variance(response: ResponseDistribution) -> float:
    """Return the finite variance for a response distribution."""

    return response_moments(response).variance


def branch_variance_from_response(response: ResponseDistribution) -> float:
    """Return the branch-variance diagnostic carried by a finite response."""

    return response_moments(response).variance


def classify_branch_variance_route(
    route: str,
    *,
    local_record_declared: bool = False,
    causal_support_declared: bool = False,
    stochastic_law_declared: bool = False,
    non_classical_sector_declared: bool = False,
    conservation_ledger_declared: bool = False,
    coefficient_provenance_declared: bool = False,
    regulator_provenance_declared: bool = False,
    no_signaling_guardrail_declared: bool = False,
    branch_matching_declared: bool = False,
    coupling_assumptions_declared: bool = False,
    artifact_ledger_declared: bool = False,
    recovery_limit_declared: bool = False,
) -> BranchVarianceRouteClassification:
    """Classify which H6S3 route supports a claimed branch variance."""

    _require_label("route", route, BRANCH_VARIANCE_ROUTE_LABELS)

    if route == "density-only-baseline":
        return BranchVarianceRouteClassification(
            route=route,
            physical_branch_variance_allowed=False,
            diagnostic_only=True,
            accepted_as_law=False,
            reason="density-only baseline has an invariant marginal and no free branch variance",
            missing_requirements=(),
        )

    if route == "pointer-record-or-collapse-record":
        missing = _missing_requirements(
            (
                ("local record", local_record_declared),
                ("causal support", causal_support_declared),
                ("conservation ledger", conservation_ledger_declared),
                ("branch matching", branch_matching_declared),
                ("artifact ledger", artifact_ledger_declared),
            )
        )
        return BranchVarianceRouteClassification(
            route=route,
            physical_branch_variance_allowed=not missing,
            diagnostic_only=True,
            accepted_as_law=False,
            reason=(
                "record-conditioned branch variance is diagnostic and ledger-dependent"
                if not missing
                else "pointer or collapse route is missing required records, matching, or ledgers"
            ),
            missing_requirements=missing,
        )

    if route == "stochastic-classical-pulse-geometry":
        missing = _missing_requirements(
            (
                ("objective causal noise law", stochastic_law_declared),
                ("coefficient provenance", coefficient_provenance_declared),
                ("regulator provenance", regulator_provenance_declared),
                ("conservation ledger", conservation_ledger_declared),
                ("no-signaling guardrail", no_signaling_guardrail_declared),
                ("artifact ledger", artifact_ledger_declared),
            )
        )
        return BranchVarianceRouteClassification(
            route=route,
            physical_branch_variance_allowed=not missing,
            diagnostic_only=True,
            accepted_as_law=False,
            reason=(
                "stochastic classical variance is diagnostic until the law is validated"
                if not missing
                else "stochastic classical route is missing law, provenance, guardrail, or ledger support"
            ),
            missing_requirements=missing,
        )

    if route == "non-classical-geometry-or-mediator":
        missing = _missing_requirements(
            (
                ("non-classical sector", non_classical_sector_declared),
                ("coupling assumptions", coupling_assumptions_declared),
                ("conservation ledger", conservation_ledger_declared),
                ("coefficient provenance", coefficient_provenance_declared),
                ("artifact ledger", artifact_ledger_declared),
                ("recovery limit", recovery_limit_declared),
            )
        )
        return BranchVarianceRouteClassification(
            route=route,
            physical_branch_variance_allowed=not missing,
            diagnostic_only=True,
            accepted_as_law=False,
            reason=(
                "non-classical route is a scoped diagnostic comparator until a law is supplied"
                if not missing
                else "non-classical route is missing sector, coupling, ledger, or recovery support"
            ),
            missing_requirements=missing,
        )

    return BranchVarianceRouteClassification(
        route=route,
        physical_branch_variance_allowed=False,
        diagnostic_only=True,
        accepted_as_law=False,
        reason="unsupported decomposition labels do not make branch variance physical",
        missing_requirements=("physical branch-support route",),
    )


def compare_branch_variance_across_decompositions(
    first_decomposition: EnsembleDecomposition,
    second_decomposition: EnsembleDecomposition,
    first_response: ResponseDistribution,
    second_response: ResponseDistribution,
    *,
    route_classification: BranchVarianceRouteClassification | None = None,
    density_tolerance: float = 1.0e-12,
    response_tolerance: float = 1.0e-12,
    variance_tolerance: float = 1.0e-12,
) -> NoFreeBranchVarianceReport:
    """Compare finite branch variance across two ensemble descriptions."""

    _require_nonnegative("density_tolerance", density_tolerance)
    _require_nonnegative("response_tolerance", response_tolerance)
    _require_nonnegative("variance_tolerance", variance_tolerance)

    route = route_classification or classify_branch_variance_route("unsupported-decomposition")
    first_moments = response_moments(first_response)
    second_moments = response_moments(second_response)
    density_distance = decomposition_distance(first_decomposition, second_decomposition)
    marginal_difference = response_marginal_max_difference(
        first_response,
        second_response,
        pulse_count_tolerance=response_tolerance,
    )
    variance_difference = abs(first_moments.variance - second_moments.variance)

    same_density = density_distance <= density_tolerance
    same_probe_marginal = marginal_difference <= response_tolerance
    branch_variance_changes = variance_difference > variance_tolerance
    diagnostic_failure = (
        same_density
        and (branch_variance_changes or not same_probe_marginal)
        and not route.physical_branch_variance_allowed
    )

    if not same_density:
        reason = "decompositions represent different density matrices"
    elif route.physical_branch_variance_allowed:
        reason = "branch variance is route-conditioned and remains diagnostic, not an accepted law"
    elif branch_variance_changes:
        reason = "same density with decomposition-dependent branch variance is rejected without a route"
    elif not same_probe_marginal:
        reason = "same density with changed probe marginal fails H6S2 admissibility"
    else:
        reason = "same density gives invariant probe marginal and no free branch variance"

    return NoFreeBranchVarianceReport(
        density_matrix_distance=density_distance,
        max_marginal_difference=marginal_difference,
        first_response_mean=first_moments.mean,
        second_response_mean=second_moments.mean,
        first_branch_variance=first_moments.variance,
        second_branch_variance=second_moments.variance,
        branch_variance_difference=variance_difference,
        same_density=same_density,
        same_probe_marginal=same_probe_marginal,
        branch_variance_changes=branch_variance_changes,
        diagnostic_failure=diagnostic_failure,
        route_classification=route,
        diagnostic_only=True,
        accepted_as_law=False,
        reason=reason,
    )


def _validate_response_distribution(response: ResponseDistribution) -> None:
    _require_nonempty_string("response family", response.family)
    points = tuple(response.points)
    if not points:
        raise ValueError("response distribution must not be empty")
    total_probability = 0.0
    for point in points:
        _require_finite_real("response pulse_count", point.pulse_count)
        _require_nonnegative("response probability", point.probability)
        total_probability += point.probability
    if not math.isclose(total_probability, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise ValueError("response distribution probabilities must sum to 1")


def _missing_requirements(requirements: tuple[tuple[str, bool], ...]) -> tuple[str, ...]:
    return tuple(name for name, declared in requirements if not declared)


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
