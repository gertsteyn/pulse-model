"""Finite-record H2 reconstruction prototypes.

This module intentionally implements narrow first slices: static clock records
in Minkowski or weak-static fields, direction-dependent timing records, and
calibrated Shapiro-delay and weak-wave response benchmarks. Coordinates, truth
potentials, endpoint geometry, and arm geometry are used only by synthetic
generators or as interpretation metadata; they are not full raw observed
finite-schema records for every slice.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping

from .calculations import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    SPEED_OF_LIGHT_M_PER_S,
    pulse_count,
    weak_field_dtaudt,
)


@dataclass(frozen=True)
class ClockCalibration:
    """Operational clock calibration for one pulse counter."""

    clock_id: str
    nominal_frequency_hz: float
    frequency_uncertainty_hz: float = 0.0
    clock_species: str = "ideal"
    transition_id: str = "nominal"


@dataclass(frozen=True)
class ClockEvent:
    """A local pulse-counter reading, not a coordinate event."""

    event_id: str
    clock_id: str
    local_sequence_index: int
    pulse_count: float
    pulse_count_uncertainty: float = 0.0
    event_role: str = "sample"


@dataclass(frozen=True)
class ClockSegment:
    """A selected interval on one clock."""

    segment_id: str
    clock_id: str
    start_event_id: str
    end_event_id: str
    segment_kind: str = "static_comparison"


@dataclass(frozen=True)
class SignalLink:
    """A relational signal link between clock events."""

    signal_id: str
    emitter_clock_id: str
    emit_event_id: str
    receiver_clock_id: str
    receive_event_id: str
    signal_species: str = "light"
    path_class_hint: str = "comparison_link"


@dataclass(frozen=True)
class PulseRecord:
    """Finite observed H2 record for the first reconstruction prototype."""

    clocks: tuple[ClockCalibration, ...]
    events: tuple[ClockEvent, ...]
    segments: tuple[ClockSegment, ...]
    signal_links: tuple[SignalLink, ...] = ()

    def clock(self, clock_id: str) -> ClockCalibration:
        for clock in self.clocks:
            if clock.clock_id == clock_id:
                return clock
        raise KeyError(f"unknown clock_id: {clock_id}")

    def event(self, event_id: str) -> ClockEvent:
        for event in self.events:
            if event.event_id == event_id:
                return event
        raise KeyError(f"unknown event_id: {event_id}")


@dataclass(frozen=True)
class DurationObservation:
    """Pulse-derived duration for one clock segment."""

    segment_id: str
    clock_id: str
    duration_s: float
    uncertainty_s: float


@dataclass(frozen=True)
class ClockRateRatio:
    """Clock duration ratio relative to a chosen reference clock."""

    clock_id: str
    reference_clock_id: str
    duration_ratio: float
    uncertainty: float


@dataclass(frozen=True)
class FlatMetricReconstruction:
    """Flat-metric first-slice result in a reference-clock gauge."""

    reference_clock_id: str
    rate_ratios: tuple[ClockRateRatio, ...]
    max_fractional_rate_deviation: float
    tolerance_fraction: float
    is_flat_within_tolerance: bool
    metric_label: str = "eta_mu_nu up to Poincare and coordinate gauge"


@dataclass(frozen=True)
class PotentialDifferenceEstimate:
    """Weak-static potential difference recovered from a clock-rate ratio."""

    clock_id: str
    reference_clock_id: str
    duration_ratio: float
    potential_difference_m2_per_s2: float
    uncertainty_m2_per_s2: float


@dataclass(frozen=True)
class DirectionalTimingRecord:
    """Counter-propagating signal-loop timing record for a stationary metric slice."""

    loop_id: str
    clockwise_duration_s: float
    counterclockwise_duration_s: float
    duration_uncertainty_s: float = 0.0


@dataclass(frozen=True)
class DirectionalTimingEstimate:
    """Recovered direction-dependent timing asymmetry."""

    loop_id: str
    time_asymmetry_s: float
    uncertainty_s: float


@dataclass(frozen=True)
class ShapiroDelayRecord:
    """Calibrated Shapiro-delay response benchmark.

    Endpoint geometry and mass are interpretation metadata for this first slice,
    not raw observed fields from the finite pulse-record schema.
    """

    signal_id: str
    central_mass_kg: float
    emitter_radius_m: float
    receiver_radius_m: float
    coordinate_separation_m: float
    observed_light_time_s: float
    duration_uncertainty_s: float = 0.0


@dataclass(frozen=True)
class ShapiroDelayEstimate:
    """Recovered spatial-curvature delay and PPN gamma proxy."""

    signal_id: str
    delay_s: float
    gamma: float
    gamma_uncertainty: float


@dataclass(frozen=True)
class GravitationalWaveArmRecord:
    """Calibrated differential arm timing response benchmark.

    Arm geometry is interpretation metadata for this first slice, not a full raw
    observed pulse-record schema implementation.
    """

    record_id: str
    arm_length_m: float
    x_arm_duration_s: float
    y_arm_duration_s: float
    duration_uncertainty_s: float = 0.0


@dataclass(frozen=True)
class GravitationalWaveStrainEstimate:
    """Recovered long-wavelength plus-polarized strain."""

    record_id: str
    h_plus: float
    uncertainty: float


def synthesize_minkowski_pulse_signal_record(
    clock_ids: tuple[str, ...],
    coordinate_duration_s: float,
    frequency_hz: float,
    pulse_count_uncertainty: float = 0.0,
) -> PulseRecord:
    """Return a finite record for static ideal clocks in Minkowski spacetime.

    The coordinate duration is a generator-side truth variable. It is converted
    into pulse counts and is not stored in the observed ``PulseRecord``.
    """

    if not clock_ids:
        raise ValueError("clock_ids must not be empty")

    return synthesize_weak_static_pulse_signal_record(
        {clock_id: 0.0 for clock_id in clock_ids},
        coordinate_duration_s,
        frequency_hz,
        pulse_count_uncertainty,
    )


def synthesize_weak_static_pulse_signal_record(
    clock_potentials_m2_per_s2: Mapping[str, float],
    coordinate_duration_s: float,
    frequency_hz: float,
    pulse_count_uncertainty: float = 0.0,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> PulseRecord:
    """Return a finite static-clock record generated from weak-field rates.

    The input potentials and coordinate duration are hidden truth data used only
    to synthesize pulse counts. The returned record keeps only observables and
    relational signal links.
    """

    if not clock_potentials_m2_per_s2:
        raise ValueError("clock_potentials_m2_per_s2 must not be empty")
    _require_positive("coordinate_duration_s", coordinate_duration_s)
    _require_positive("frequency_hz", frequency_hz)
    _require_nonnegative("pulse_count_uncertainty", pulse_count_uncertainty)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    clocks: list[ClockCalibration] = []
    events: list[ClockEvent] = []
    segments: list[ClockSegment] = []

    for clock_index, (clock_id, potential_m2_per_s2) in enumerate(clock_potentials_m2_per_s2.items()):
        if not clock_id:
            raise ValueError("clock_id must not be empty")
        _require_finite(f"potential_m2_per_s2[{clock_id}]", potential_m2_per_s2)

        rate = weak_field_dtaudt(potential_m2_per_s2, 0.0, speed_of_light_m_per_s)
        if rate <= 0.0:
            raise ValueError(f"weak-field clock rate for {clock_id} must be positive")

        start_event_id = f"{clock_id}:start"
        end_event_id = f"{clock_id}:end"
        proper_duration_s = coordinate_duration_s * rate

        clocks.append(ClockCalibration(clock_id=clock_id, nominal_frequency_hz=frequency_hz))
        events.extend(
            [
                ClockEvent(
                    event_id=start_event_id,
                    clock_id=clock_id,
                    local_sequence_index=0,
                    pulse_count=0.0,
                    pulse_count_uncertainty=pulse_count_uncertainty,
                    event_role="signal_emit" if clock_index == 0 else "signal_receive",
                ),
                ClockEvent(
                    event_id=end_event_id,
                    clock_id=clock_id,
                    local_sequence_index=1,
                    pulse_count=pulse_count(frequency_hz, proper_duration_s),
                    pulse_count_uncertainty=pulse_count_uncertainty,
                    event_role="signal_emit" if clock_index == 0 else "signal_receive",
                ),
            ]
        )
        segments.append(
            ClockSegment(
                segment_id=f"{clock_id}:segment",
                clock_id=clock_id,
                start_event_id=start_event_id,
                end_event_id=end_event_id,
            )
        )

    reference_clock_id = next(iter(clock_potentials_m2_per_s2))
    signal_links = _comparison_signal_links(reference_clock_id, tuple(clock_potentials_m2_per_s2))

    return PulseRecord(
        clocks=tuple(clocks),
        events=tuple(events),
        segments=tuple(segments),
        signal_links=signal_links,
    )


def pulse_segment_duration(record: PulseRecord, segment_id: str) -> DurationObservation:
    """Return pulse-derived duration and uncertainty for a segment."""

    segment = _segment(record, segment_id)
    clock = record.clock(segment.clock_id)
    start = record.event(segment.start_event_id)
    end = record.event(segment.end_event_id)

    if start.clock_id != segment.clock_id or end.clock_id != segment.clock_id:
        raise ValueError("segment endpoints must belong to the segment clock")
    if end.local_sequence_index <= start.local_sequence_index:
        raise ValueError("segment end must come after segment start")

    count_delta = end.pulse_count - start.pulse_count
    if count_delta <= 0.0:
        raise ValueError("segment pulse_count delta must be positive")

    frequency_hz = clock.nominal_frequency_hz
    _require_positive("nominal_frequency_hz", frequency_hz)

    duration_s = count_delta / frequency_hz
    count_uncertainty = math.hypot(start.pulse_count_uncertainty, end.pulse_count_uncertainty)
    count_duration_uncertainty_s = count_uncertainty / frequency_hz
    frequency_duration_uncertainty_s = 0.0
    if clock.frequency_uncertainty_hz > 0.0:
        frequency_duration_uncertainty_s = (
            duration_s * clock.frequency_uncertainty_hz / frequency_hz
        )

    return DurationObservation(
        segment_id=segment.segment_id,
        clock_id=segment.clock_id,
        duration_s=duration_s,
        uncertainty_s=math.hypot(count_duration_uncertainty_s, frequency_duration_uncertainty_s),
    )


def reconstruct_flat_metric(
    record: PulseRecord,
    reference_clock_id: str,
    tolerance_fraction: float = 1e-12,
) -> FlatMetricReconstruction:
    """Test whether static-clock ratios recover the Minkowski flat slice.

    The reference clock fixes the time-scale gauge. This first slice recovers
    equality of static clock rates, not a general metric from arbitrary sparse
    data.
    """

    _require_nonnegative("tolerance_fraction", tolerance_fraction)
    ratios = clock_rate_ratios(record, reference_clock_id)
    max_deviation = max((abs(ratio.duration_ratio - 1.0) for ratio in ratios), default=0.0)

    return FlatMetricReconstruction(
        reference_clock_id=reference_clock_id,
        rate_ratios=ratios,
        max_fractional_rate_deviation=max_deviation,
        tolerance_fraction=tolerance_fraction,
        is_flat_within_tolerance=max_deviation <= tolerance_fraction,
    )


def reconstruct_weak_static_potential_differences(
    record: PulseRecord,
    reference_clock_id: str,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> tuple[PotentialDifferenceEstimate, ...]:
    """Recover weak-static potential differences from clock-rate ratios.

    The reference clock sets the additive potential convention. For the first
    static weak-field slice, ``Delta Phi = c^2 (duration_ratio - 1)``.
    """

    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)
    c_squared = speed_of_light_m_per_s**2

    estimates = []
    for ratio in clock_rate_ratios(record, reference_clock_id):
        estimates.append(
            PotentialDifferenceEstimate(
                clock_id=ratio.clock_id,
                reference_clock_id=reference_clock_id,
                duration_ratio=ratio.duration_ratio,
                potential_difference_m2_per_s2=c_squared * (ratio.duration_ratio - 1.0),
                uncertainty_m2_per_s2=c_squared * ratio.uncertainty,
            )
        )

    return tuple(estimates)


def synthesize_directional_timing_record(
    loop_id: str,
    base_light_time_s: float,
    time_asymmetry_s: float,
    duration_uncertainty_s: float = 0.0,
) -> DirectionalTimingRecord:
    """Return a counter-propagating loop record with a signed asymmetry.

    This is the finite-record handle for stationary off-diagonal metric effects:
    direction-dependent timing is observable even when the absolute coordinate
    representation of $g_{0i}$ is gauge-dependent.
    """

    if not loop_id:
        raise ValueError("loop_id must not be empty")
    _require_positive("base_light_time_s", base_light_time_s)
    _require_finite("time_asymmetry_s", time_asymmetry_s)
    _require_nonnegative("duration_uncertainty_s", duration_uncertainty_s)

    clockwise = base_light_time_s + time_asymmetry_s
    counterclockwise = base_light_time_s - time_asymmetry_s
    _require_positive("clockwise_duration_s", clockwise)
    _require_positive("counterclockwise_duration_s", counterclockwise)

    return DirectionalTimingRecord(
        loop_id=loop_id,
        clockwise_duration_s=clockwise,
        counterclockwise_duration_s=counterclockwise,
        duration_uncertainty_s=duration_uncertainty_s,
    )


def recover_directional_time_asymmetry(
    record: DirectionalTimingRecord,
) -> DirectionalTimingEstimate:
    """Recover the signed half-difference of counter-propagating signal times."""

    _require_positive("clockwise_duration_s", record.clockwise_duration_s)
    _require_positive("counterclockwise_duration_s", record.counterclockwise_duration_s)
    _require_nonnegative("duration_uncertainty_s", record.duration_uncertainty_s)

    return DirectionalTimingEstimate(
        loop_id=record.loop_id,
        time_asymmetry_s=0.5 * (record.clockwise_duration_s - record.counterclockwise_duration_s),
        uncertainty_s=record.duration_uncertainty_s / math.sqrt(2.0),
    )


def shapiro_delay_s(
    central_mass_kg: float,
    emitter_radius_m: float,
    receiver_radius_m: float,
    coordinate_separation_m: float,
    gamma: float = 1.0,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return the weak-field Shapiro delay for a calibrated two-endpoint path."""

    log_factor = _shapiro_log_factor(emitter_radius_m, receiver_radius_m, coordinate_separation_m)
    _require_nonnegative("central_mass_kg", central_mass_kg)
    _require_finite("gamma", gamma)
    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    return (
        (1.0 + gamma)
        * gravitational_constant_m3_per_kg_s2
        * central_mass_kg
        * log_factor
        / speed_of_light_m_per_s**3
    )


def synthesize_shapiro_delay_record(
    signal_id: str,
    central_mass_kg: float,
    emitter_radius_m: float,
    receiver_radius_m: float,
    coordinate_separation_m: float,
    gamma: float = 1.0,
    duration_uncertainty_s: float = 0.0,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> ShapiroDelayRecord:
    """Return a calibrated response record with injected Shapiro delay."""

    if not signal_id:
        raise ValueError("signal_id must not be empty")
    _require_nonnegative("duration_uncertainty_s", duration_uncertainty_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)
    _shapiro_log_factor(emitter_radius_m, receiver_radius_m, coordinate_separation_m)

    observed_light_time_s = (
        coordinate_separation_m / speed_of_light_m_per_s
        + shapiro_delay_s(
            central_mass_kg,
            emitter_radius_m,
            receiver_radius_m,
            coordinate_separation_m,
            gamma,
            speed_of_light_m_per_s=speed_of_light_m_per_s,
        )
    )

    return ShapiroDelayRecord(
        signal_id=signal_id,
        central_mass_kg=central_mass_kg,
        emitter_radius_m=emitter_radius_m,
        receiver_radius_m=receiver_radius_m,
        coordinate_separation_m=coordinate_separation_m,
        observed_light_time_s=observed_light_time_s,
        duration_uncertainty_s=duration_uncertainty_s,
    )


def recover_shapiro_gamma(
    record: ShapiroDelayRecord,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> ShapiroDelayEstimate:
    """Recover the PPN gamma proxy from a calibrated Shapiro-delay record."""

    log_factor = _shapiro_log_factor(
        record.emitter_radius_m,
        record.receiver_radius_m,
        record.coordinate_separation_m,
    )
    _require_nonnegative("central_mass_kg", record.central_mass_kg)
    _require_positive("observed_light_time_s", record.observed_light_time_s)
    _require_nonnegative("duration_uncertainty_s", record.duration_uncertainty_s)
    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    flat_light_time_s = record.coordinate_separation_m / speed_of_light_m_per_s
    delay_s = record.observed_light_time_s - flat_light_time_s
    scale = (
        gravitational_constant_m3_per_kg_s2
        * record.central_mass_kg
        * log_factor
        / speed_of_light_m_per_s**3
    )
    _require_positive("shapiro_scale", scale)

    return ShapiroDelayEstimate(
        signal_id=record.signal_id,
        delay_s=delay_s,
        gamma=delay_s / scale - 1.0,
        gamma_uncertainty=record.duration_uncertainty_s / scale,
    )


def synthesize_gravitational_wave_arm_record(
    record_id: str,
    arm_length_m: float,
    h_plus: float,
    duration_uncertainty_s: float = 0.0,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> GravitationalWaveArmRecord:
    """Return a calibrated long-wavelength differential arm timing benchmark."""

    if not record_id:
        raise ValueError("record_id must not be empty")
    _require_positive("arm_length_m", arm_length_m)
    _require_finite("h_plus", h_plus)
    _require_nonnegative("duration_uncertainty_s", duration_uncertainty_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    flat_duration_s = arm_length_m / speed_of_light_m_per_s
    return GravitationalWaveArmRecord(
        record_id=record_id,
        arm_length_m=arm_length_m,
        x_arm_duration_s=flat_duration_s * (1.0 + 0.5 * h_plus),
        y_arm_duration_s=flat_duration_s * (1.0 - 0.5 * h_plus),
        duration_uncertainty_s=duration_uncertainty_s,
    )


def recover_gravitational_wave_h_plus(
    record: GravitationalWaveArmRecord,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> GravitationalWaveStrainEstimate:
    """Recover the plus-polarized strain from differential arm timing."""

    _require_positive("arm_length_m", record.arm_length_m)
    _require_positive("x_arm_duration_s", record.x_arm_duration_s)
    _require_positive("y_arm_duration_s", record.y_arm_duration_s)
    _require_nonnegative("duration_uncertainty_s", record.duration_uncertainty_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    flat_duration_s = record.arm_length_m / speed_of_light_m_per_s
    duration_difference_s = record.x_arm_duration_s - record.y_arm_duration_s

    return GravitationalWaveStrainEstimate(
        record_id=record.record_id,
        h_plus=duration_difference_s / flat_duration_s,
        uncertainty=math.sqrt(2.0) * record.duration_uncertainty_s / flat_duration_s,
    )


def clock_rate_ratios(record: PulseRecord, reference_clock_id: str) -> tuple[ClockRateRatio, ...]:
    """Return one duration ratio per clock relative to ``reference_clock_id``."""

    observations = _single_segment_observations_by_clock(record)
    if reference_clock_id not in observations:
        raise ValueError("reference_clock_id must have exactly one segment")

    reference = observations[reference_clock_id]
    if reference.duration_s <= 0.0:
        raise ValueError("reference duration must be positive")

    ratios = []
    for clock_id in sorted(observations):
        observation = observations[clock_id]
        if clock_id == reference_clock_id:
            ratio = 1.0
            uncertainty = 0.0
        else:
            ratio = observation.duration_s / reference.duration_s
            uncertainty = _ratio_uncertainty(
                ratio,
                observation.duration_s,
                observation.uncertainty_s,
                reference.duration_s,
                reference.uncertainty_s,
            )
        ratios.append(
            ClockRateRatio(
                clock_id=clock_id,
                reference_clock_id=reference_clock_id,
                duration_ratio=ratio,
                uncertainty=uncertainty,
            )
        )

    return tuple(ratios)


def _comparison_signal_links(
    reference_clock_id: str,
    clock_ids: tuple[str, ...],
) -> tuple[SignalLink, ...]:
    links = []
    for clock_id in clock_ids:
        if clock_id == reference_clock_id:
            continue
        for endpoint in ["start", "end"]:
            links.append(
                SignalLink(
                    signal_id=f"{reference_clock_id}->{clock_id}:{endpoint}",
                    emitter_clock_id=reference_clock_id,
                    emit_event_id=f"{reference_clock_id}:{endpoint}",
                    receiver_clock_id=clock_id,
                    receive_event_id=f"{clock_id}:{endpoint}",
                )
            )
    return tuple(links)


def _single_segment_observations_by_clock(record: PulseRecord) -> dict[str, DurationObservation]:
    observations: dict[str, DurationObservation] = {}
    for segment in record.segments:
        if segment.clock_id in observations:
            raise ValueError("prototype expects at most one selected segment per clock")
        observations[segment.clock_id] = pulse_segment_duration(record, segment.segment_id)

    for clock in record.clocks:
        if clock.clock_id not in observations:
            raise ValueError(f"clock has no selected segment: {clock.clock_id}")

    return observations


def _segment(record: PulseRecord, segment_id: str) -> ClockSegment:
    for segment in record.segments:
        if segment.segment_id == segment_id:
            return segment
    raise KeyError(f"unknown segment_id: {segment_id}")


def _ratio_uncertainty(
    ratio: float,
    duration_s: float,
    duration_uncertainty_s: float,
    reference_duration_s: float,
    reference_uncertainty_s: float,
) -> float:
    terms = []
    if duration_uncertainty_s > 0.0:
        terms.append(duration_uncertainty_s / duration_s)
    if reference_uncertainty_s > 0.0:
        terms.append(reference_uncertainty_s / reference_duration_s)
    return abs(ratio) * math.sqrt(math.fsum(term * term for term in terms))


def _shapiro_log_factor(
    emitter_radius_m: float,
    receiver_radius_m: float,
    coordinate_separation_m: float,
) -> float:
    _require_positive("emitter_radius_m", emitter_radius_m)
    _require_positive("receiver_radius_m", receiver_radius_m)
    _require_positive("coordinate_separation_m", coordinate_separation_m)

    denominator = emitter_radius_m + receiver_radius_m - coordinate_separation_m
    if denominator <= 0.0:
        raise ValueError("coordinate_separation_m must be less than emitter_radius_m + receiver_radius_m")

    log_argument = (emitter_radius_m + receiver_radius_m + coordinate_separation_m) / denominator
    if log_argument <= 1.0:
        raise ValueError("Shapiro log argument must be greater than 1")
    return math.log(log_argument)


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")
