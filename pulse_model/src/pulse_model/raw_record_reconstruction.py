"""Raw event-graph reconstruction helpers for the H2S1 synthetic slice.

The implementation is intentionally narrow. It validates raw clock, signal,
and meeting records; recovers local order and meeting representatives; and
solves the first static 1+1D reciprocal-signal embedding diagnostic. Synthetic
truth coordinates live only in generator sidecars and are never consumed by the
reconstruction functions.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True)
class RawClock:
    """Observed clock-counter calibration record."""

    clock_id: str
    nominal_frequency_hz: float
    frequency_uncertainty_hz: float = 0.0
    clock_species: str = "ideal"
    calibration_status: str = "calibrated"
    provenance_id: str = "synthetic"
    artifact_flags: tuple[str, ...] = ()


@dataclass(frozen=True)
class RawClockEvent:
    """Observed clock-local pulse reading."""

    event_id: str
    clock_id: str
    local_sequence_index: int
    pulse_count: float
    pulse_count_uncertainty: float = 0.0
    event_role: str = "sample"
    provenance_id: str = "synthetic"
    artifact_flags: tuple[str, ...] = ()


@dataclass(frozen=True)
class RawSignalLink:
    """Observed signal incidence between two clock-local events."""

    signal_id: str
    emitter_clock_id: str
    emit_event_id: str
    emission_pulse_count: float
    receiver_clock_id: str
    receive_event_id: str
    reception_pulse_count: float
    signal_species: str = "light"
    link_status: str = "direct"
    noise_model_id: str = "zero"
    provenance_id: str = "synthetic"
    artifact_flags: tuple[str, ...] = ()


@dataclass(frozen=True)
class RawMeeting:
    """Observed equality of multiple clock-local events."""

    meeting_id: str
    clock_event_ids: tuple[str, ...]
    coincidence_uncertainty_s: float = 0.0
    equality_status: str = "exact"
    provenance_id: str = "synthetic"
    artifact_flags: tuple[str, ...] = ()


@dataclass(frozen=True)
class RawEventRecord:
    """Finite observed raw event graph."""

    clocks: tuple[RawClock, ...]
    events: tuple[RawClockEvent, ...]
    signals: tuple[RawSignalLink, ...] = ()
    meetings: tuple[RawMeeting, ...] = ()


@dataclass(frozen=True)
class TruthEvent:
    """Generator-only event coordinate sidecar."""

    event_id: str
    t: float
    x: float
    proper_time: float


@dataclass(frozen=True)
class SyntheticRawCase:
    """Synthetic raw record plus hidden truth used only by tests."""

    raw_record: RawEventRecord
    truth_events: tuple[TruthEvent, ...]
    generator_case_id: str


@dataclass(frozen=True)
class MeetingMerge:
    """Merged event representatives after meeting equality constraints."""

    representative_by_event_id: Mapping[str, str]
    members_by_representative: Mapping[str, tuple[str, ...]]


@dataclass(frozen=True)
class PartialOrder:
    """Recovered graph order after local clock and signal edges."""

    edges: tuple[tuple[str, str], ...]
    topological_order: tuple[str, ...]
    component_count: int


@dataclass(frozen=True)
class EventCoordinate:
    """Gauge-fixed synthetic fit coordinate for one observed event."""

    event_id: str
    t: float
    x: float


@dataclass(frozen=True)
class NullSignalResidual:
    """Future/null residual for one observed light signal."""

    signal_id: str
    delta_t: float
    delta_x: float
    residual: float
    is_future_directed: bool
    is_satisfied: bool


@dataclass(frozen=True)
class MatrixRankReport:
    """Linear rank and nullspace report for the static signal equations."""

    variable_names: tuple[str, ...]
    residual_names: tuple[str, ...]
    variable_count: int
    residual_count: int
    rank: int
    nullity: int
    singular_values: tuple[float, ...]
    tolerance: float
    gauge_mode_count: int
    non_gauge_nullity: int
    nullspace_basis: tuple[tuple[float, ...], ...]
    degeneracy_labels: tuple[str, ...]
    residual_norm: float
    max_abs_residual: float


@dataclass(frozen=True)
class RawReconstruction:
    """Full H2S1 first-slice reconstruction diagnostic."""

    ordered_event_ids_by_clock: Mapping[str, tuple[str, ...]]
    meeting_merge: MeetingMerge
    partial_order: PartialOrder
    event_coordinates: tuple[EventCoordinate, ...]
    null_signal_residuals: tuple[NullSignalResidual, ...]
    rank_report: MatrixRankReport
    degeneracy_labels: tuple[str, ...]
    consumed_observed_fields: tuple[str, ...]


def synthesize_static_reciprocal_signal_case(
    distance: float = 1.0,
    frequency_hz: float = 1.0,
    clock_ids: tuple[str, str] = ("A", "B"),
) -> SyntheticRawCase:
    """Return a two-clock static light-ranging case with hidden truth sidecar."""

    _require_positive("distance", distance)
    _require_positive("frequency_hz", frequency_hz)
    if len(clock_ids) != 2 or len(set(clock_ids)) != 2:
        raise ValueError("clock_ids must contain two distinct IDs")

    reference_id, probe_id = clock_ids
    clocks = (
        RawClock(reference_id, frequency_hz),
        RawClock(probe_id, frequency_hz),
    )
    events = (
        RawClockEvent(f"{reference_id}:emit", reference_id, 0, 0.0, event_role="signal_emit"),
        RawClockEvent(
            f"{reference_id}:receive",
            reference_id,
            1,
            2.0 * distance * frequency_hz,
            event_role="signal_receive",
        ),
        RawClockEvent(
            f"{probe_id}:turn",
            probe_id,
            0,
            distance * frequency_hz,
            event_role="mixed",
        ),
    )
    signals = (
        RawSignalLink(
            "s-out",
            reference_id,
            f"{reference_id}:emit",
            0.0,
            probe_id,
            f"{probe_id}:turn",
            distance * frequency_hz,
        ),
        RawSignalLink(
            "s-back",
            probe_id,
            f"{probe_id}:turn",
            distance * frequency_hz,
            reference_id,
            f"{reference_id}:receive",
            2.0 * distance * frequency_hz,
        ),
    )
    truth = (
        TruthEvent(f"{reference_id}:emit", 0.0, 0.0, 0.0),
        TruthEvent(f"{reference_id}:receive", 2.0 * distance, 0.0, 2.0 * distance),
        TruthEvent(f"{probe_id}:turn", distance, distance, distance),
    )

    return SyntheticRawCase(
        raw_record=RawEventRecord(clocks=clocks, events=events, signals=signals),
        truth_events=truth,
        generator_case_id="separated_inertial_clocks",
    )


def synthesize_meeting_case(frequency_hz: float = 1.0) -> SyntheticRawCase:
    """Return a two-clock meeting case for event-identity tests."""

    _require_positive("frequency_hz", frequency_hz)
    clocks = (RawClock("A", frequency_hz), RawClock("B", frequency_hz))
    events = (
        RawClockEvent("A:before", "A", 0, 0.0),
        RawClockEvent("A:meet", "A", 1, frequency_hz, event_role="meeting"),
        RawClockEvent("A:after", "A", 2, 2.0 * frequency_hz),
        RawClockEvent("B:meet", "B", 0, 0.0, event_role="meeting"),
        RawClockEvent("B:after", "B", 1, frequency_hz),
    )
    meetings = (RawMeeting("m0", ("A:meet", "B:meet")),)
    truth = (
        TruthEvent("A:before", -1.0, 0.0, 0.0),
        TruthEvent("A:meet", 0.0, 0.0, 1.0),
        TruthEvent("A:after", 1.0, 0.0, 2.0),
        TruthEvent("B:meet", 0.0, 0.0, 0.0),
        TruthEvent("B:after", 1.0, 0.0, 1.0),
    )
    return SyntheticRawCase(
        raw_record=RawEventRecord(clocks=clocks, events=events, meetings=meetings),
        truth_events=truth,
        generator_case_id="crossing_inertial_clocks",
    )


def synthesize_single_clock_case(frequency_hz: float = 1.0) -> SyntheticRawCase:
    """Return one calibrated clock chain with no geometric constraints."""

    _require_positive("frequency_hz", frequency_hz)
    clocks = (RawClock("A", frequency_hz),)
    events = (
        RawClockEvent("A:0", "A", 0, 0.0),
        RawClockEvent("A:1", "A", 1, frequency_hz),
    )
    truth = (
        TruthEvent("A:0", 0.0, 0.0, 0.0),
        TruthEvent("A:1", 1.0, 0.0, 1.0),
    )
    return SyntheticRawCase(
        raw_record=RawEventRecord(clocks=clocks, events=events),
        truth_events=truth,
        generator_case_id="single_inertial_clock",
    )


def synthesize_flat_three_clock_network(frequency_hz: float = 1.0) -> SyntheticRawCase:
    """Return a three-clock static network with reference and non-reference links."""

    _require_positive("frequency_hz", frequency_hz)
    clocks = (
        RawClock("A", frequency_hz),
        RawClock("B", frequency_hz),
        RawClock("C", frequency_hz),
    )
    events = (
        RawClockEvent("A:emit", "A", 0, 0.0, event_role="signal_emit"),
        RawClockEvent("A:receive_b", "A", 1, 2.0 * frequency_hz, event_role="signal_receive"),
        RawClockEvent("A:receive_c", "A", 2, 4.0 * frequency_hz, event_role="signal_receive"),
        RawClockEvent("B:turn", "B", 0, frequency_hz, event_role="mixed"),
        RawClockEvent("C:turn", "C", 0, 2.0 * frequency_hz, event_role="mixed"),
    )
    signals = (
        RawSignalLink("s-ab", "A", "A:emit", 0.0, "B", "B:turn", frequency_hz),
        RawSignalLink("s-ba", "B", "B:turn", frequency_hz, "A", "A:receive_b", 2.0 * frequency_hz),
        RawSignalLink("s-ac", "A", "A:emit", 0.0, "C", "C:turn", 2.0 * frequency_hz),
        RawSignalLink("s-ca", "C", "C:turn", 2.0 * frequency_hz, "A", "A:receive_c", 4.0 * frequency_hz),
        RawSignalLink("s-bc", "B", "B:turn", frequency_hz, "C", "C:turn", 2.0 * frequency_hz),
    )
    truth = (
        TruthEvent("A:emit", 0.0, 0.0, 0.0),
        TruthEvent("A:receive_b", 2.0, 0.0, 2.0),
        TruthEvent("A:receive_c", 4.0, 0.0, 4.0),
        TruthEvent("B:turn", 1.0, 1.0, 1.0),
        TruthEvent("C:turn", 2.0, 2.0, 2.0),
    )
    return SyntheticRawCase(
        raw_record=RawEventRecord(clocks=clocks, events=events, signals=signals),
        truth_events=truth,
        generator_case_id="flat_three_clock_network",
    )


def synthesize_sparse_underdetermined_case(frequency_hz: float = 1.0) -> SyntheticRawCase:
    """Return a weakly linked two-clock case that must stay rank-deficient."""

    case = synthesize_static_reciprocal_signal_case(distance=1.0, frequency_hz=frequency_hz)
    return SyntheticRawCase(
        raw_record=RawEventRecord(
            clocks=case.raw_record.clocks,
            events=case.raw_record.events,
            signals=case.raw_record.signals[:1],
        ),
        truth_events=case.truth_events,
        generator_case_id="sparse_underdetermined",
    )


def synthesize_inconsistent_record(frequency_hz: float = 1.0) -> SyntheticRawCase:
    """Return a deliberately invalid raw record for rejection tests."""

    _require_positive("frequency_hz", frequency_hz)
    clocks = (RawClock("A", frequency_hz),)
    events = (
        RawClockEvent("A:0", "A", 0, frequency_hz),
        RawClockEvent("A:1", "A", 1, 0.0),
    )
    return SyntheticRawCase(
        raw_record=RawEventRecord(clocks=clocks, events=events),
        truth_events=(),
        generator_case_id="inconsistent_record",
    )


def recover_event_order(record: RawEventRecord) -> Mapping[str, tuple[str, ...]]:
    """Validate and return clock-local event order."""

    clocks_by_id = _clock_map(record)
    events_by_clock: dict[str, list[RawClockEvent]] = {clock_id: [] for clock_id in clocks_by_id}
    seen_events: set[str] = set()
    for event in record.events:
        if event.event_id in seen_events:
            raise ValueError(f"duplicate event_id: {event.event_id}")
        seen_events.add(event.event_id)
        if event.clock_id not in clocks_by_id:
            raise ValueError(f"event {event.event_id} references unknown clock_id")
        _require_finite(f"pulse_count[{event.event_id}]", event.pulse_count)
        _require_nonnegative(
            f"pulse_count_uncertainty[{event.event_id}]",
            event.pulse_count_uncertainty,
        )
        events_by_clock[event.clock_id].append(event)

    ordered: dict[str, tuple[str, ...]] = {}
    for clock_id, events in events_by_clock.items():
        sequence_indexes: set[int] = set()
        sorted_events = sorted(events, key=lambda item: item.local_sequence_index)
        last_pulse: float | None = None
        for event in sorted_events:
            if event.local_sequence_index in sequence_indexes:
                raise ValueError(f"duplicate local_sequence_index on clock {clock_id}")
            sequence_indexes.add(event.local_sequence_index)
            if last_pulse is not None and event.pulse_count <= last_pulse:
                raise ValueError(f"nonmonotone pulse_count on clock {clock_id}")
            last_pulse = event.pulse_count
        ordered[clock_id] = tuple(event.event_id for event in sorted_events)
    return ordered


def merge_meeting_events(record: RawEventRecord) -> MeetingMerge:
    """Merge raw meeting equality groups with union-find."""

    event_by_id = _event_map(record)
    parent = {event_id: event_id for event_id in event_by_id}

    def find(event_id: str) -> str:
        while parent[event_id] != event_id:
            parent[event_id] = parent[parent[event_id]]
            event_id = parent[event_id]
        return event_id

    def union(left: str, right: str) -> None:
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    seen_meetings: set[str] = set()
    for meeting in record.meetings:
        if meeting.meeting_id in seen_meetings:
            raise ValueError(f"duplicate meeting_id: {meeting.meeting_id}")
        seen_meetings.add(meeting.meeting_id)
        if len(meeting.clock_event_ids) < 2:
            raise ValueError(f"meeting {meeting.meeting_id} must list at least two events")
        _require_nonnegative(
            f"coincidence_uncertainty_s[{meeting.meeting_id}]",
            meeting.coincidence_uncertainty_s,
        )
        clocks_in_meeting: set[str] = set()
        for event_id in meeting.clock_event_ids:
            if event_id not in event_by_id:
                raise ValueError(f"meeting {meeting.meeting_id} references unknown event_id")
            clock_id = event_by_id[event_id].clock_id
            if clock_id in clocks_in_meeting:
                raise ValueError("meeting-conflict: one clock contributes multiple events")
            clocks_in_meeting.add(clock_id)
        first = meeting.clock_event_ids[0]
        for event_id in meeting.clock_event_ids[1:]:
            union(first, event_id)

    members: dict[str, list[str]] = {}
    for event_id in event_by_id:
        root = find(event_id)
        members.setdefault(root, []).append(event_id)

    representatives = {event_id: find(event_id) for event_id in event_by_id}
    return MeetingMerge(
        representative_by_event_id=representatives,
        members_by_representative={
            representative: tuple(sorted(member_ids))
            for representative, member_ids in members.items()
        },
    )


def reconstruct_raw_event_graph(
    record: RawEventRecord,
    reference_clock_id: str | None = None,
    tolerance: float = 1.0e-9,
) -> RawReconstruction:
    """Return the first H2S1 raw event-graph reconstruction diagnostic."""

    _require_positive("tolerance", tolerance)
    clocks_by_id = _clock_map(record)
    if not clocks_by_id:
        raise ValueError("record must contain at least one clock")
    reference_id = reference_clock_id or record.clocks[0].clock_id
    if reference_id not in clocks_by_id:
        raise ValueError("reference_clock_id is not present in record")

    ordered = recover_event_order(record)
    merge = merge_meeting_events(record)
    partial_order = _partial_order(record, ordered, merge)
    variable_names, equations = _static_signal_equations(record, reference_id, tolerance)
    rank_report, solution = _rank_report_from_equations(variable_names, equations, tolerance)
    has_determined_fit = rank_report.nullity == 0 and "noisy-inconsistency" not in rank_report.degeneracy_labels
    coordinates = _fit_static_coordinates(record, reference_id, solution) if has_determined_fit else {}
    residuals = _null_signal_residuals(record, coordinates, tolerance) if has_determined_fit else ()

    labels = {"valid", *rank_report.degeneracy_labels}
    if len(record.clocks) < 2:
        labels.add("insufficient-clocks")
    if len(record.clocks) >= 2:
        labels.add("mirror-boost-ambiguity")
    if partial_order.component_count > 1:
        labels.add("disconnected-component")
    if record.signals and not _has_reciprocal_signal(record):
        labels.add("missing-reciprocal-signals")
    if any(clock.calibration_status != "calibrated" for clock in record.clocks):
        labels.add("calibration-ambiguity")
    if any(not residual.is_satisfied for residual in residuals):
        labels.add("noisy-inconsistency")

    return RawReconstruction(
        ordered_event_ids_by_clock=ordered,
        meeting_merge=merge,
        partial_order=partial_order,
        event_coordinates=tuple(coordinates.values()),
        null_signal_residuals=residuals,
        rank_report=rank_report,
        degeneracy_labels=tuple(sorted(labels)),
        consumed_observed_fields=(
            "clock_id",
            "nominal_frequency_hz",
            "calibration_status",
            "event_id",
            "local_sequence_index",
            "pulse_count",
            "signal_id",
            "emit_event_id",
            "receive_event_id",
            "meeting_id",
            "clock_event_ids",
        ),
    )


def _static_signal_equations(
    record: RawEventRecord,
    reference_clock_id: str,
    tolerance: float,
) -> tuple[tuple[str, ...], tuple[tuple[str, tuple[float, ...], float], ...]]:
    clocks = [clock.clock_id for clock in record.clocks if clock.clock_id != reference_clock_id]
    variable_names = tuple(
        name
        for clock_id in clocks
        for name in (f"{clock_id}.beta", f"{clock_id}.distance")
    )
    variable_index = {name: index for index, name in enumerate(variable_names)}
    variable_count = 2 * len(clocks)
    clock_by_id = _clock_map(record)
    event_by_id = _event_map(record)

    equations: list[tuple[str, tuple[float, ...], float]] = []
    non_reference_signals: list[tuple[RawSignalLink, RawClockEvent, RawClockEvent]] = []
    for signal in record.signals:
        emit = event_by_id[signal.emit_event_id]
        receive = event_by_id[signal.receive_event_id]
        if signal.emitter_clock_id == reference_clock_id and signal.receiver_clock_id in clocks:
            clock_id = signal.receiver_clock_id
            row = [0.0] * variable_count
            row[variable_index[f"{clock_id}.beta"]] = 1.0
            row[variable_index[f"{clock_id}.distance"]] = -1.0
            rhs = _event_tau(emit, clock_by_id[reference_clock_id]) - _event_tau(
                receive,
                clock_by_id[clock_id],
            )
            equations.append((signal.signal_id, tuple(row), rhs))
        elif signal.receiver_clock_id == reference_clock_id and signal.emitter_clock_id in clocks:
            clock_id = signal.emitter_clock_id
            row = [0.0] * variable_count
            row[variable_index[f"{clock_id}.beta"]] = 1.0
            row[variable_index[f"{clock_id}.distance"]] = 1.0
            rhs = _event_tau(receive, clock_by_id[reference_clock_id]) - _event_tau(
                emit,
                clock_by_id[clock_id],
            )
            equations.append((signal.signal_id, tuple(row), rhs))
        elif signal.emitter_clock_id in clocks and signal.receiver_clock_id in clocks:
            non_reference_signals.append((signal, emit, receive))

    for meeting in record.meetings:
        ref_events = [
            event_by_id[event_id]
            for event_id in meeting.clock_event_ids
            if event_by_id[event_id].clock_id == reference_clock_id
        ]
        if not ref_events:
            continue
        ref_tau = _event_tau(ref_events[0], clock_by_id[reference_clock_id])
        for event_id in meeting.clock_event_ids:
            event = event_by_id[event_id]
            if event.clock_id == reference_clock_id or event.clock_id not in clocks:
                continue
            beta_row = [0.0] * variable_count
            beta_row[variable_index[f"{event.clock_id}.beta"]] = 1.0
            equations.append(
                (
                    f"{meeting.meeting_id}:{event.clock_id}:beta",
                    tuple(beta_row),
                    ref_tau - _event_tau(event, clock_by_id[event.clock_id]),
                )
            )

    if non_reference_signals:
        base_report, base_solution = _rank_report_from_equations(
            variable_names,
            tuple(equations),
            tolerance,
        )
        for signal, emit, receive in non_reference_signals:
            emitter_id = signal.emitter_clock_id
            receiver_id = signal.receiver_clock_id
            branch = _non_reference_signal_branch(
                emitter_id,
                receiver_id,
                variable_names,
                base_report,
                base_solution,
                tolerance,
            )
            if branch is None:
                continue
            row = [0.0] * variable_count
            row[variable_index[f"{receiver_id}.beta"]] = 1.0
            row[variable_index[f"{receiver_id}.distance"]] = -branch
            row[variable_index[f"{emitter_id}.beta"]] -= 1.0
            row[variable_index[f"{emitter_id}.distance"]] += branch
            rhs = _event_tau(emit, clock_by_id[emitter_id]) - _event_tau(
                receive,
                clock_by_id[receiver_id],
            )
            equations.append((signal.signal_id, tuple(row), rhs))

    return variable_names, tuple(equations)


def _non_reference_signal_branch(
    emitter_id: str,
    receiver_id: str,
    variable_names: tuple[str, ...],
    rank_report: MatrixRankReport,
    solution: Mapping[str, float],
    tolerance: float,
) -> float | None:
    if "noisy-inconsistency" in rank_report.degeneracy_labels:
        return None
    emitter_distance = _fixed_solution_value(
        f"{emitter_id}.distance",
        variable_names,
        rank_report.nullspace_basis,
        solution,
        tolerance,
    )
    receiver_distance = _fixed_solution_value(
        f"{receiver_id}.distance",
        variable_names,
        rank_report.nullspace_basis,
        solution,
        tolerance,
    )
    if emitter_distance is None or receiver_distance is None:
        return None
    separation = receiver_distance - emitter_distance
    if abs(separation) <= tolerance:
        return None
    return 1.0 if separation > 0.0 else -1.0


def _fixed_solution_value(
    variable_name: str,
    variable_names: tuple[str, ...],
    nullspace_basis: tuple[tuple[float, ...], ...],
    solution: Mapping[str, float],
    tolerance: float,
) -> float | None:
    if variable_name not in solution:
        return None
    variable_index = {name: index for index, name in enumerate(variable_names)}
    index = variable_index.get(variable_name)
    if index is None:
        return None
    if any(abs(vector[index]) > tolerance for vector in nullspace_basis):
        return None
    return solution[variable_name]


def _rank_report_from_equations(
    variable_names: tuple[str, ...],
    equations: tuple[tuple[str, tuple[float, ...], float], ...],
    tolerance: float,
) -> tuple[MatrixRankReport, Mapping[str, float]]:
    residual_names = tuple(name for name, _, _ in equations)
    matrix = [list(row) for _, row, _ in equations]
    rhs = [value for _, _, value in equations]
    variable_count = len(variable_names)

    rref, pivot_columns = _rref(matrix, tolerance)
    rank = len(pivot_columns)
    nullity = max(0, variable_count - rank)
    nullspace = _nullspace_from_rref(rref, pivot_columns, variable_count, tolerance)
    if matrix:
        solution, inconsistent = _particular_solution(matrix, rhs, tolerance)
    else:
        solution = tuple(0.0 for _ in variable_names)
        inconsistent = False
    residual_vector = _matrix_vector_residual(matrix, solution, rhs)
    residual_norm = math.sqrt(sum(value * value for value in residual_vector))
    max_abs_residual = max((abs(value) for value in residual_vector), default=0.0)

    labels: set[str] = set()
    if variable_count == 0:
        labels.add("insufficient-clocks")
    if nullity > 0:
        labels.add("rank-deficient")
    if inconsistent or max_abs_residual > tolerance:
        labels.add("noisy-inconsistency")

    return (
        MatrixRankReport(
            variable_names=variable_names,
            residual_names=residual_names,
            variable_count=variable_count,
            residual_count=len(equations),
            rank=rank,
            nullity=nullity,
            singular_values=_singular_values(matrix, tolerance),
            tolerance=tolerance,
            gauge_mode_count=0,
            non_gauge_nullity=nullity,
            nullspace_basis=nullspace,
            degeneracy_labels=tuple(sorted(labels)),
            residual_norm=residual_norm,
            max_abs_residual=max_abs_residual,
        ),
        {name: solution[index] for index, name in enumerate(variable_names)},
    )


def _fit_static_coordinates(
    record: RawEventRecord,
    reference_clock_id: str,
    solution: Mapping[str, float],
) -> dict[str, EventCoordinate]:
    clock_by_id = _clock_map(record)
    coordinates: dict[str, EventCoordinate] = {}
    for event in record.events:
        tau = _event_tau(event, clock_by_id[event.clock_id])
        if event.clock_id == reference_clock_id:
            coordinates[event.event_id] = EventCoordinate(event.event_id, tau, 0.0)
            continue
        beta = solution.get(f"{event.clock_id}.beta")
        distance = solution.get(f"{event.clock_id}.distance")
        if beta is None or distance is None:
            continue
        coordinates[event.event_id] = EventCoordinate(event.event_id, beta + tau, distance)
    return coordinates


def _null_signal_residuals(
    record: RawEventRecord,
    coordinates: Mapping[str, EventCoordinate],
    tolerance: float,
) -> tuple[NullSignalResidual, ...]:
    residuals: list[NullSignalResidual] = []
    for signal in record.signals:
        emit = coordinates.get(signal.emit_event_id)
        receive = coordinates.get(signal.receive_event_id)
        if emit is None or receive is None:
            continue
        delta_t = receive.t - emit.t
        delta_x = receive.x - emit.x
        residual = delta_t * delta_t - delta_x * delta_x
        residuals.append(
            NullSignalResidual(
                signal_id=signal.signal_id,
                delta_t=delta_t,
                delta_x=delta_x,
                residual=residual,
                is_future_directed=delta_t > 0.0,
                is_satisfied=delta_t > 0.0 and abs(residual) <= tolerance,
            )
        )
    return tuple(residuals)


def _partial_order(
    record: RawEventRecord,
    ordered: Mapping[str, tuple[str, ...]],
    merge: MeetingMerge,
) -> PartialOrder:
    edges: list[tuple[str, str]] = []
    for event_ids in ordered.values():
        for left, right in zip(event_ids, event_ids[1:], strict=False):
            left_rep = merge.representative_by_event_id[left]
            right_rep = merge.representative_by_event_id[right]
            if left_rep == right_rep:
                raise ValueError("event-order-conflict: meeting merge collapses local order")
            edges.append((left_rep, right_rep))
    for signal in record.signals:
        left_rep = merge.representative_by_event_id[signal.emit_event_id]
        right_rep = merge.representative_by_event_id[signal.receive_event_id]
        if left_rep == right_rep:
            raise ValueError("event-order-conflict: signal endpoint representatives coincide")
        edges.append((left_rep, right_rep))

    representatives = tuple(sorted(set(merge.representative_by_event_id.values())))
    topological_order = _topological_order(representatives, edges)
    return PartialOrder(
        edges=tuple(edges),
        topological_order=topological_order,
        component_count=_component_count(representatives, edges),
    )


def _topological_order(
    representatives: Sequence[str],
    edges: Sequence[tuple[str, str]],
) -> tuple[str, ...]:
    incoming = {representative: 0 for representative in representatives}
    outgoing: dict[str, list[str]] = {representative: [] for representative in representatives}
    for left, right in edges:
        outgoing.setdefault(left, []).append(right)
        incoming[right] = incoming.get(right, 0) + 1
        incoming.setdefault(left, incoming.get(left, 0))

    ready = sorted(item for item, count in incoming.items() if count == 0)
    order: list[str] = []
    while ready:
        current = ready.pop(0)
        order.append(current)
        for target in outgoing.get(current, ()):
            incoming[target] -= 1
            if incoming[target] == 0:
                ready.append(target)
                ready.sort()
    if len(order) != len(incoming):
        raise ValueError("event-order-conflict: partial order contains a cycle")
    return tuple(order)


def _component_count(
    representatives: Sequence[str],
    edges: Sequence[tuple[str, str]],
) -> int:
    if not representatives:
        return 0
    adjacency: dict[str, set[str]] = {representative: set() for representative in representatives}
    for left, right in edges:
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)
    seen: set[str] = set()
    count = 0
    for representative in representatives:
        if representative in seen:
            continue
        count += 1
        stack = [representative]
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            stack.extend(sorted(adjacency.get(current, ())))
    return count


def _has_reciprocal_signal(record: RawEventRecord) -> bool:
    pairs = {(signal.emitter_clock_id, signal.receiver_clock_id) for signal in record.signals}
    return any((right, left) in pairs for left, right in pairs)


def _clock_map(record: RawEventRecord) -> Mapping[str, RawClock]:
    clocks: dict[str, RawClock] = {}
    for clock in record.clocks:
        if not clock.clock_id:
            raise ValueError("clock_id must not be empty")
        if clock.clock_id in clocks:
            raise ValueError(f"duplicate clock_id: {clock.clock_id}")
        if not clock.calibration_status:
            raise ValueError(f"calibration_status[{clock.clock_id}] must not be empty")
        _require_positive(f"nominal_frequency_hz[{clock.clock_id}]", clock.nominal_frequency_hz)
        _require_nonnegative(
            f"frequency_uncertainty_hz[{clock.clock_id}]",
            clock.frequency_uncertainty_hz,
        )
        clocks[clock.clock_id] = clock
    return clocks


def _event_map(record: RawEventRecord) -> Mapping[str, RawClockEvent]:
    recover_event_order(record)
    events = {event.event_id: event for event in record.events}
    signal_ids: set[str] = set()
    for signal in record.signals:
        if not signal.signal_id:
            raise ValueError("signal_id must not be empty")
        if signal.signal_id in signal_ids:
            raise ValueError(f"duplicate signal_id: {signal.signal_id}")
        signal_ids.add(signal.signal_id)
        if signal.emit_event_id not in events or signal.receive_event_id not in events:
            raise ValueError(f"signal {signal.signal_id} references unknown event_id")
        emit = events[signal.emit_event_id]
        receive = events[signal.receive_event_id]
        if emit.clock_id != signal.emitter_clock_id:
            raise ValueError(f"signal {signal.signal_id} emitter_clock_id mismatch")
        if receive.clock_id != signal.receiver_clock_id:
            raise ValueError(f"signal {signal.signal_id} receiver_clock_id mismatch")
        if not math.isclose(emit.pulse_count, signal.emission_pulse_count, rel_tol=0.0, abs_tol=1.0e-12):
            raise ValueError(f"signal {signal.signal_id} emission_pulse_count mismatch")
        if not math.isclose(receive.pulse_count, signal.reception_pulse_count, rel_tol=0.0, abs_tol=1.0e-12):
            raise ValueError(f"signal {signal.signal_id} reception_pulse_count mismatch")
    return events


def _event_tau(event: RawClockEvent, clock: RawClock) -> float:
    return event.pulse_count / clock.nominal_frequency_hz


def _rref(
    matrix: Sequence[Sequence[float]],
    tolerance: float,
) -> tuple[tuple[tuple[float, ...], ...], tuple[int, ...]]:
    rows = [list(row) for row in matrix]
    if not rows:
        return (), ()
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        best_row = max(
            range(pivot_row, row_count),
            key=lambda candidate: abs(rows[candidate][column]),
        )
        if abs(rows[best_row][column]) <= tolerance:
            continue
        rows[pivot_row], rows[best_row] = rows[best_row], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot for value in rows[pivot_row]]
        for row_index in range(row_count):
            if row_index == pivot_row:
                continue
            factor = rows[row_index][column]
            if abs(factor) <= tolerance:
                continue
            rows[row_index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(rows[row_index], rows[pivot_row], strict=True)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    cleaned = tuple(tuple(0.0 if abs(value) <= tolerance else value for value in row) for row in rows)
    return cleaned, tuple(pivot_columns)


def _nullspace_from_rref(
    rref: Sequence[Sequence[float]],
    pivot_columns: Sequence[int],
    variable_count: int,
    tolerance: float,
) -> tuple[tuple[float, ...], ...]:
    pivot_set = set(pivot_columns)
    free_columns = [column for column in range(variable_count) if column not in pivot_set]
    basis: list[tuple[float, ...]] = []
    for free_column in free_columns:
        vector = [0.0] * variable_count
        vector[free_column] = 1.0
        for row_index, pivot_column in enumerate(pivot_columns):
            value = -rref[row_index][free_column]
            vector[pivot_column] = 0.0 if abs(value) <= tolerance else value
        basis.append(tuple(vector))
    return tuple(basis)


def _particular_solution(
    matrix: Sequence[Sequence[float]],
    rhs: Sequence[float],
    tolerance: float,
) -> tuple[tuple[float, ...], bool]:
    if not matrix:
        return (), False
    augmented = [list(row) + [value] for row, value in zip(matrix, rhs, strict=True)]
    rref, pivot_columns = _rref(augmented, tolerance)
    variable_count = len(matrix[0])
    inconsistent = False
    solution = [0.0] * variable_count
    for row in rref:
        coeffs = row[:variable_count]
        value = row[variable_count]
        if all(abs(item) <= tolerance for item in coeffs) and abs(value) > tolerance:
            inconsistent = True
    for row_index, pivot_column in enumerate(pivot_columns):
        if pivot_column < variable_count:
            solution[pivot_column] = rref[row_index][variable_count]
    return tuple(solution), inconsistent


def _matrix_vector_residual(
    matrix: Sequence[Sequence[float]],
    vector: Sequence[float],
    rhs: Sequence[float],
) -> tuple[float, ...]:
    return tuple(
        sum(coefficient * vector[index] for index, coefficient in enumerate(row)) - rhs_value
        for row, rhs_value in zip(matrix, rhs, strict=True)
    )


def _singular_values(matrix: Sequence[Sequence[float]], tolerance: float) -> tuple[float, ...]:
    if not matrix or not matrix[0]:
        return ()
    column_count = len(matrix[0])
    gram = [[0.0 for _ in range(column_count)] for _ in range(column_count)]
    for row in matrix:
        for left in range(column_count):
            for right in range(column_count):
                gram[left][right] += row[left] * row[right]
    eigenvalues = _jacobi_eigenvalues(gram, tolerance)
    return tuple(math.sqrt(max(value, 0.0)) for value in sorted(eigenvalues, reverse=True))


def _jacobi_eigenvalues(matrix: Sequence[Sequence[float]], tolerance: float) -> tuple[float, ...]:
    values = [list(row) for row in matrix]
    size = len(values)
    if size == 1:
        return (values[0][0],)
    for _ in range(max(1, 50 * size * size)):
        pivot_left = 0
        pivot_right = 1
        max_offdiag = 0.0
        for left in range(size):
            for right in range(left + 1, size):
                if abs(values[left][right]) > max_offdiag:
                    max_offdiag = abs(values[left][right])
                    pivot_left = left
                    pivot_right = right
        if max_offdiag <= tolerance:
            break
        app = values[pivot_left][pivot_left]
        aqq = values[pivot_right][pivot_right]
        apq = values[pivot_left][pivot_right]
        angle = 0.5 * math.atan2(2.0 * apq, aqq - app)
        cosine = math.cos(angle)
        sine = math.sin(angle)
        for index in range(size):
            if index == pivot_left or index == pivot_right:
                continue
            aip = values[index][pivot_left]
            aiq = values[index][pivot_right]
            values[index][pivot_left] = cosine * aip - sine * aiq
            values[pivot_left][index] = values[index][pivot_left]
            values[index][pivot_right] = sine * aip + cosine * aiq
            values[pivot_right][index] = values[index][pivot_right]
        values[pivot_left][pivot_left] = (
            cosine * cosine * app
            - 2.0 * sine * cosine * apq
            + sine * sine * aqq
        )
        values[pivot_right][pivot_right] = (
            sine * sine * app
            + 2.0 * sine * cosine * apq
            + cosine * cosine * aqq
        )
        values[pivot_left][pivot_right] = 0.0
        values[pivot_right][pivot_left] = 0.0
    return tuple(values[index][index] for index in range(size))


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")
