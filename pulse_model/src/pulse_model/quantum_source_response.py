"""Focused H6S1 quantum source-response discriminator helpers.

The helpers implement only the weak-field two-branch source/probe arena
defined in the H6S1 appendix. They compare expectation-sourced and
branch-mixture pulse-count records, and provide guardrail checks for
no-signaling and conservation classifications.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

from .calculations import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    SPEED_OF_LIGHT_M_PER_S,
    clock_visibility,
    two_level_clock_visibility,
)


@dataclass(frozen=True)
class TwoBranchWeakFieldSetup:
    """Minimal two-branch source and stationary probe-clock setup."""

    probability_a: float
    source_position_a_m: float
    source_position_b_m: float
    probe_position_m: float
    coordinate_duration_s: float
    clock_frequency_hz: float
    source_mass_kg: float
    relative_phase_rad: float = 0.0
    branch_overlap: float = 0.0
    softening_radius_m: float = 0.0
    branch_label_a: str = "a"
    branch_label_b: str = "b"
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S

    def __post_init__(self) -> None:
        _require_probability("probability_a", self.probability_a)
        _require_finite("source_position_a_m", self.source_position_a_m)
        _require_finite("source_position_b_m", self.source_position_b_m)
        _require_finite("probe_position_m", self.probe_position_m)
        _require_nonnegative("coordinate_duration_s", self.coordinate_duration_s)
        _require_nonnegative("clock_frequency_hz", self.clock_frequency_hz)
        _require_nonnegative("source_mass_kg", self.source_mass_kg)
        _require_finite("relative_phase_rad", self.relative_phase_rad)
        _require_probability("branch_overlap", self.branch_overlap)
        _require_nonnegative("softening_radius_m", self.softening_radius_m)
        _require_nonempty_string("branch_label_a", self.branch_label_a)
        _require_nonempty_string("branch_label_b", self.branch_label_b)
        if self.branch_label_a == self.branch_label_b:
            raise ValueError("branch labels must be distinct")
        _require_positive(
            "gravitational_constant_m3_per_kg_s2",
            self.gravitational_constant_m3_per_kg_s2,
        )
        _require_positive("speed_of_light_m_per_s", self.speed_of_light_m_per_s)

        for name, source_position in (
            ("source_position_a_m", self.source_position_a_m),
            ("source_position_b_m", self.source_position_b_m),
        ):
            if self.softening_radius_m == 0.0 and source_position == self.probe_position_m:
                raise ValueError(f"{name} must not coincide with probe_position_m without softening")

        for potential in (
            softened_newtonian_potential(
                self.source_mass_kg,
                self.source_position_a_m,
                self.probe_position_m,
                self.softening_radius_m,
                self.gravitational_constant_m3_per_kg_s2,
            ),
            softened_newtonian_potential(
                self.source_mass_kg,
                self.source_position_b_m,
                self.probe_position_m,
                self.softening_radius_m,
                self.gravitational_constant_m3_per_kg_s2,
            ),
        ):
            weak_field_probe_proper_time_s(
                self.coordinate_duration_s,
                potential,
                self.speed_of_light_m_per_s,
            )

    @property
    def probability_b(self) -> float:
        return 1.0 - self.probability_a


@dataclass(frozen=True)
class BranchProbeResponse:
    """One branch-conditioned probe-clock response."""

    branch_label: str
    probability: float
    source_position_m: float
    potential_m2_per_s2: float
    proper_time_s: float
    pulse_count: float


@dataclass(frozen=True)
class SourceResponseSummary:
    """Computed H6S1 discriminator channels for one setup."""

    branch_a: BranchProbeResponse
    branch_b: BranchProbeResponse
    expectation_potential_m2_per_s2: float
    expectation_proper_time_s: float
    expectation_pulse_count: float
    branch_mixture_mean_pulse_count: float
    branch_mixture_variance_pulses2: float
    instrumental_noise_variance_pulses2: float
    observed_variance_pulses2: float
    branch_separation_pulses: float
    branch_separation_score: float
    source_probe_covariance_pulses: float
    source_probe_correlation: float


@dataclass(frozen=True)
class PulseDistributionPoint:
    """One point in a finite probe pulse-count marginal distribution."""

    pulse_count: float
    probability: float

    def __post_init__(self) -> None:
        _require_finite("pulse_count", self.pulse_count)
        _require_nonnegative("probability", self.probability)


@dataclass(frozen=True)
class NoSignalingGuardrail:
    """Comparison of two probe marginals under remote basis choices."""

    rule_name: str
    max_marginal_difference: float
    tolerance: float
    causal_channel_declared: bool = False

    def __post_init__(self) -> None:
        _require_nonempty_string("rule_name", self.rule_name)
        _require_nonnegative_or_inf("max_marginal_difference", self.max_marginal_difference)
        _require_nonnegative("tolerance", self.tolerance)

    @property
    def classification(self) -> str:
        if self.max_marginal_difference <= self.tolerance:
            return "no-signaling-passed"
        if self.causal_channel_declared:
            return "causal-channel-required"
        return "rejected-remote-basis-signaling"

    @property
    def rejected(self) -> bool:
        return self.classification == "rejected-remote-basis-signaling"


def softened_newtonian_potential(
    source_mass_kg: float,
    source_position_m: float,
    probe_position_m: float,
    softening_radius_m: float = 0.0,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
) -> float:
    """Return ``-G M / sqrt(distance^2 + softening^2)`` at the probe."""

    _require_nonnegative("source_mass_kg", source_mass_kg)
    _require_finite("source_position_m", source_position_m)
    _require_finite("probe_position_m", probe_position_m)
    _require_nonnegative("softening_radius_m", softening_radius_m)
    _require_positive(
        "gravitational_constant_m3_per_kg_s2",
        gravitational_constant_m3_per_kg_s2,
    )

    distance_m = probe_position_m - source_position_m
    radius_m = math.hypot(distance_m, softening_radius_m)
    if radius_m == 0.0:
        raise ValueError("source and probe positions must not coincide without softening")
    return -gravitational_constant_m3_per_kg_s2 * source_mass_kg / radius_m


def weak_field_probe_proper_time_s(
    coordinate_duration_s: float,
    potential_m2_per_s2: float,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return stationary probe proper time in the weak-field toy arena."""

    _require_nonnegative("coordinate_duration_s", coordinate_duration_s)
    _require_finite("potential_m2_per_s2", potential_m2_per_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    rate = 1.0 + potential_m2_per_s2 / speed_of_light_m_per_s**2
    if rate < 0.0:
        raise ValueError("weak-field rate must not make probe proper time negative")
    return coordinate_duration_s * rate


def branch_probe_response(setup: TwoBranchWeakFieldSetup, branch_label: str) -> BranchProbeResponse:
    """Return the branch-conditioned weak-field probe response."""

    if branch_label == setup.branch_label_a:
        probability = setup.probability_a
        source_position_m = setup.source_position_a_m
    elif branch_label == setup.branch_label_b:
        probability = setup.probability_b
        source_position_m = setup.source_position_b_m
    else:
        raise ValueError("branch_label must match one setup branch label")

    potential = softened_newtonian_potential(
        setup.source_mass_kg,
        source_position_m,
        setup.probe_position_m,
        setup.softening_radius_m,
        setup.gravitational_constant_m3_per_kg_s2,
    )
    proper_time = weak_field_probe_proper_time_s(
        setup.coordinate_duration_s,
        potential,
        setup.speed_of_light_m_per_s,
    )
    return BranchProbeResponse(
        branch_label=branch_label,
        probability=probability,
        source_position_m=source_position_m,
        potential_m2_per_s2=potential,
        proper_time_s=proper_time,
        pulse_count=setup.clock_frequency_hz * proper_time,
    )


def source_response_discriminator(
    setup: TwoBranchWeakFieldSetup,
    instrumental_noise_stddev_pulses: float = 0.0,
) -> SourceResponseSummary:
    """Return expectation-sourced and branch-mixture discriminator channels."""

    _require_nonnegative("instrumental_noise_stddev_pulses", instrumental_noise_stddev_pulses)

    branch_a = branch_probe_response(setup, setup.branch_label_a)
    branch_b = branch_probe_response(setup, setup.branch_label_b)
    expectation_potential = (
        setup.probability_a * branch_a.potential_m2_per_s2
        + setup.probability_b * branch_b.potential_m2_per_s2
    )
    expectation_proper_time = weak_field_probe_proper_time_s(
        setup.coordinate_duration_s,
        expectation_potential,
        setup.speed_of_light_m_per_s,
    )
    expectation_pulse_count = setup.clock_frequency_hz * expectation_proper_time
    mixture_mean = setup.probability_a * branch_a.pulse_count + setup.probability_b * branch_b.pulse_count
    branch_separation = branch_a.pulse_count - branch_b.pulse_count
    probability_product = setup.probability_a * setup.probability_b
    branch_variance = probability_product * branch_separation * branch_separation
    instrumental_variance = instrumental_noise_stddev_pulses * instrumental_noise_stddev_pulses
    observed_variance = branch_variance + instrumental_variance
    if instrumental_noise_stddev_pulses == 0.0:
        branch_separation_score = math.inf if branch_separation != 0.0 else 0.0
    else:
        branch_separation_score = abs(branch_separation) / instrumental_noise_stddev_pulses

    covariance = probability_product * branch_separation
    correlation_denominator = math.sqrt(probability_product * observed_variance)
    source_probe_correlation = 0.0
    if correlation_denominator > 0.0:
        source_probe_correlation = covariance / correlation_denominator

    return SourceResponseSummary(
        branch_a=branch_a,
        branch_b=branch_b,
        expectation_potential_m2_per_s2=expectation_potential,
        expectation_proper_time_s=expectation_proper_time,
        expectation_pulse_count=expectation_pulse_count,
        branch_mixture_mean_pulse_count=mixture_mean,
        branch_mixture_variance_pulses2=branch_variance,
        instrumental_noise_variance_pulses2=instrumental_variance,
        observed_variance_pulses2=observed_variance,
        branch_separation_pulses=branch_separation,
        branch_separation_score=branch_separation_score,
        source_probe_covariance_pulses=covariance,
        source_probe_correlation=source_probe_correlation,
    )


def branch_proper_time_difference_s(setup: TwoBranchWeakFieldSetup) -> float:
    """Return ``tau_a - tau_b`` for the two branch-conditioned probe times."""

    branch_a = branch_probe_response(setup, setup.branch_label_a)
    branch_b = branch_probe_response(setup, setup.branch_label_b)
    return branch_a.proper_time_s - branch_b.proper_time_s


def branch_visibility(
    setup: TwoBranchWeakFieldSetup,
    energy_levels_j: Iterable[float],
    probabilities: Iterable[float],
) -> float:
    """Return the internal-clock visibility from branch proper-time difference."""

    return clock_visibility(
        branch_proper_time_difference_s(setup),
        energy_levels_j,
        probabilities,
    )


def two_level_branch_visibility(
    setup: TwoBranchWeakFieldSetup,
    transition_frequency_hz: float,
    excited_state_probability: float = 0.5,
) -> float:
    """Return two-level internal-clock visibility for the branch difference."""

    return two_level_clock_visibility(
        branch_proper_time_difference_s(setup),
        transition_frequency_hz,
        excited_state_probability,
    )


def expectation_sourced_distribution(setup: TwoBranchWeakFieldSetup) -> tuple[PulseDistributionPoint, ...]:
    """Return the one-point expectation-sourced probe marginal."""

    summary = source_response_discriminator(setup)
    return (PulseDistributionPoint(summary.expectation_pulse_count, 1.0),)


def branch_mixture_distribution(setup: TwoBranchWeakFieldSetup) -> tuple[PulseDistributionPoint, ...]:
    """Return the two-point branch-mixture probe marginal."""

    summary = source_response_discriminator(setup)
    return (
        PulseDistributionPoint(summary.branch_a.pulse_count, setup.probability_a),
        PulseDistributionPoint(summary.branch_b.pulse_count, setup.probability_b),
    )


def invalid_remote_basis_toy_distribution(
    setup: TwoBranchWeakFieldSetup,
    remote_basis: str,
) -> tuple[PulseDistributionPoint, ...]:
    """Return the intentionally invalid toy marginal for no-signaling checks."""

    summary = source_response_discriminator(setup)
    if remote_basis == "Z":
        probabilities = (setup.probability_a, setup.probability_b)
    elif remote_basis == "X":
        probabilities = (0.5, 0.5)
    else:
        raise ValueError("remote_basis must be 'Z' or 'X'")
    return (
        PulseDistributionPoint(summary.branch_a.pulse_count, probabilities[0]),
        PulseDistributionPoint(summary.branch_b.pulse_count, probabilities[1]),
    )


def pulse_marginal_max_difference(
    first_distribution: Sequence[PulseDistributionPoint],
    second_distribution: Sequence[PulseDistributionPoint],
    *,
    pulse_count_tolerance: float = 1.0e-12,
) -> float:
    """Return the maximum probability difference for matching pulse support."""

    _require_nonnegative("pulse_count_tolerance", pulse_count_tolerance)
    first = _coalesce_distribution(
        _require_distribution("first_distribution", first_distribution),
        pulse_count_tolerance,
    )
    second = _coalesce_distribution(
        _require_distribution("second_distribution", second_distribution),
        pulse_count_tolerance,
    )
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


def no_signaling_guardrail(
    rule_name: str,
    baseline_distribution: Sequence[PulseDistributionPoint],
    changed_basis_distribution: Sequence[PulseDistributionPoint],
    *,
    causal_channel_declared: bool = False,
    tolerance: float = 1.0e-12,
) -> NoSignalingGuardrail:
    """Classify whether a remote basis change altered the probe marginal."""

    return NoSignalingGuardrail(
        rule_name=rule_name,
        max_marginal_difference=pulse_marginal_max_difference(
            baseline_distribution,
            changed_basis_distribution,
            pulse_count_tolerance=tolerance,
        ),
        tolerance=tolerance,
        causal_channel_declared=causal_channel_declared,
    )


def classify_conservation_status(model_family: str) -> str:
    """Return the H6S1 conservation label for a model family."""

    normalized = model_family.strip().lower().replace("_", "-")
    mapping = {
        "expectation-sourced": "expectation-conserved",
        "expectation-sourced-semiclassical": "expectation-conserved",
        "branch-specific": "branchwise-conserved",
        "branch-specific-metric": "branchwise-conserved",
        "collapse-selection": "conservation-requires-environment",
        "collapse-decoherence": "conservation-requires-environment",
        "pulse-native": "not-yet-classified",
        "pulse-native-kernel": "not-yet-classified",
        "invalid-toy": "inconsistent-rejected",
        "intentionally-invalid-toy": "inconsistent-rejected",
    }
    try:
        return mapping[normalized]
    except KeyError as exc:
        raise ValueError(f"unknown H6S1 model family: {model_family}") from exc


def _require_distribution(
    name: str,
    distribution: Sequence[PulseDistributionPoint],
) -> tuple[PulseDistributionPoint, ...]:
    if not distribution:
        raise ValueError(f"{name} must not be empty")
    points = tuple(distribution)
    total_probability = math.fsum(point.probability for point in points)
    if not math.isclose(total_probability, 1.0, rel_tol=1.0e-12, abs_tol=1.0e-12):
        raise ValueError(f"{name} probabilities must sum to 1")
    return points


def _coalesce_distribution(
    distribution: Sequence[PulseDistributionPoint],
    pulse_count_tolerance: float,
) -> tuple[PulseDistributionPoint, ...]:
    """Merge finite-distribution points with indistinguishable pulse counts."""

    if not distribution:
        return ()

    sorted_points = sorted(
        (point for point in distribution if point.probability > 0.0),
        key=lambda point: point.pulse_count,
    )
    if not sorted_points:
        return ()
    merged: list[PulseDistributionPoint] = []
    current_probability = sorted_points[0].probability
    current_weighted_pulse_count = sorted_points[0].pulse_count * sorted_points[0].probability
    current_reference_pulse_count = sorted_points[0].pulse_count

    for point in sorted_points[1:]:
        if math.isclose(
            point.pulse_count,
            current_reference_pulse_count,
            rel_tol=0.0,
            abs_tol=pulse_count_tolerance,
        ):
            current_probability += point.probability
            current_weighted_pulse_count += point.pulse_count * point.probability
            if current_probability > 0.0:
                current_reference_pulse_count = current_weighted_pulse_count / current_probability
        else:
            merged.append(_merged_distribution_point(current_weighted_pulse_count, current_probability))
            current_probability = point.probability
            current_weighted_pulse_count = point.pulse_count * point.probability
            current_reference_pulse_count = point.pulse_count

    merged.append(_merged_distribution_point(current_weighted_pulse_count, current_probability))
    return tuple(merged)


def _merged_distribution_point(
    weighted_pulse_count: float,
    probability: float,
) -> PulseDistributionPoint:
    if probability == 0.0:
        return PulseDistributionPoint(0.0, 0.0)
    return PulseDistributionPoint(weighted_pulse_count / probability, probability)


def _require_nonempty_string(name: str, value: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a nonempty string")


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_nonnegative_or_inf(name: str, value: float) -> None:
    if math.isnan(value):
        raise ValueError(f"{name} must not be NaN")
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _require_probability(name: str, value: float) -> None:
    _require_nonnegative(name, value)
    if value > 1.0:
        raise ValueError(f"{name} must be at most 1")
