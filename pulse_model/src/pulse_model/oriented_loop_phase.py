"""Focused 05S4 oriented-loop phase helpers.

This module checks only record-level phase algebra justified by the 05S4
appendix: closed-loop phase sums, artifact subtraction, orientation reversal,
additive composition, and conversion into the existing 05S2 curvature estimator
when a phase-to-defect normalization is supplied.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass, replace

from .pulse_record_curvature import CurvatureEstimate, PulseLoopRecord, estimate_pulse_record_curvature
from .pulse_regge import LOCAL_FRAME_PLANES, Plane

TAU_RADIANS = 2.0 * math.pi


@dataclass(frozen=True)
class PhaseComparisonEdge:
    """Signed edge phase increment in a closed loop."""

    start_id: str
    end_id: str
    phase_difference_rad: float

    def __post_init__(self) -> None:
        _require_nonempty_string("start_id", self.start_id)
        _require_nonempty_string("end_id", self.end_id)
        _require_finite("phase_difference_rad", self.phase_difference_rad)


@dataclass(frozen=True)
class OrientedLoopPhaseRecord:
    """One corrected oriented loop phase record.

    ``observed_phase_rad`` is recorded in the canonical loop convention.
    ``orientation`` is applied exactly once to produce the oriented phase.
    """

    plane: Plane
    area_m2: float
    observed_phase_rad: float
    orientation: float = 1.0
    calibration_phase_rad: float = 0.0
    matter_phase_rad: float = 0.0
    rotation_phase_rad: float = 0.0
    instrument_phase_rad: float = 0.0
    finite_loop_phase_rad: float = 0.0
    scalarization_residual_per_m2: float = 0.0
    phase_coupling_rad: float = 1.0
    weight: float = 1.0
    loop_scale_m: float | None = None
    source_id: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "plane", _canonical_plane("plane", self.plane))
        _require_positive("area_m2", self.area_m2)
        _require_finite("observed_phase_rad", self.observed_phase_rad)
        _require_orientation("orientation", self.orientation)
        _require_finite("calibration_phase_rad", self.calibration_phase_rad)
        _require_finite("matter_phase_rad", self.matter_phase_rad)
        _require_finite("rotation_phase_rad", self.rotation_phase_rad)
        _require_finite("instrument_phase_rad", self.instrument_phase_rad)
        _require_finite("finite_loop_phase_rad", self.finite_loop_phase_rad)
        _require_finite("scalarization_residual_per_m2", self.scalarization_residual_per_m2)
        _require_positive("phase_coupling_rad", self.phase_coupling_rad)
        _require_positive("weight", self.weight)
        if self.loop_scale_m is not None:
            _require_positive("loop_scale_m", self.loop_scale_m)

    @property
    def artifact_phase_rad(self) -> float:
        return math.fsum(
            (
                self.calibration_phase_rad,
                self.matter_phase_rad,
                self.rotation_phase_rad,
                self.instrument_phase_rad,
                self.finite_loop_phase_rad,
            )
        )

    @property
    def canonical_phase_rad(self) -> float:
        return self.observed_phase_rad - self.artifact_phase_rad

    @property
    def oriented_phase_rad(self) -> float:
        return self.orientation * self.canonical_phase_rad

    @property
    def oriented_finite_loop_phase_rad(self) -> float:
        return self.orientation * self.finite_loop_phase_rad

    @property
    def sectional_curvature_per_m2(self) -> float:
        return self.oriented_phase_rad / (self.phase_coupling_rad * self.area_m2)

    def to_pulse_loop_record(self) -> PulseLoopRecord:
        """Return an equivalent 05S2 loop-defect record."""

        return PulseLoopRecord(
            plane=self.plane,
            area_m2=self.area_m2,
            defect=self.canonical_phase_rad / self.phase_coupling_rad,
            orientation=self.orientation,
            weight=self.weight,
            loop_scale_m=self.loop_scale_m,
            source_id=self.source_id,
        )


@dataclass(frozen=True)
class OrientedLoopPhaseComposition:
    """Summary of additive oriented-loop phase composition."""

    record_count: int
    linear_sum_rad: float
    composed_phase_rad: float
    squared_loss_rad2: float
    shared_boundary_phase_rad: float
    cross_artifact_phase_rad: float
    finite_loop_overlap_phase_rad: float
    finite_loop_correction_rad: float
    max_abs_scalarization_residual_per_m2: float

    @property
    def additive_error_rad(self) -> float:
        return self.composed_phase_rad - self.linear_sum_rad

    @property
    def is_additive(self) -> bool:
        return math.isclose(self.additive_error_rad, 0.0, rel_tol=1.0e-15, abs_tol=1.0e-15)

    @property
    def classification(self) -> str:
        if not self.is_additive:
            return "nonadditive-phase"
        if self.record_count == 0:
            return "no-records"
        if self.linear_sum_rad == 0.0 and self.squared_loss_rad2 == 0.0:
            return "zero-oriented-phase"
        if self.max_abs_scalarization_residual_per_m2 > 0.0:
            return "oriented-phase-with-scalarization-residual"
        if self.finite_loop_correction_rad != 0.0:
            return "oriented-phase-with-finite-loop-ledger"
        return "additive-oriented-phase"


def closed_phase_sum_rad(
    edges: Iterable[PhaseComparisonEdge],
    *,
    unwrap_turns: int = 0,
) -> float:
    """Return a closed-loop phase sum with an explicit cycle unwrap integer."""

    edge_tuple = tuple(edges)
    if not edge_tuple:
        raise ValueError("edges must contain at least one phase comparison")
    if not isinstance(unwrap_turns, int):
        raise ValueError("unwrap_turns must be an integer")
    for index, edge in enumerate(edge_tuple):
        next_edge = edge_tuple[(index + 1) % len(edge_tuple)]
        if edge.end_id != next_edge.start_id:
            raise ValueError("edges must form a consecutive closed loop")
    return math.fsum(edge.phase_difference_rad for edge in edge_tuple) + TAU_RADIANS * unwrap_turns


def linear_oriented_phase_rad(records: Iterable[OrientedLoopPhaseRecord]) -> float:
    """Return the signed linear oriented phase sum."""

    return math.fsum(record.weight * record.oriented_phase_rad for record in records)


def oriented_phase_squared_loss_rad2(records: Iterable[OrientedLoopPhaseRecord]) -> float:
    """Return the sign-blind squared phase loss."""

    return math.fsum(record.weight * record.canonical_phase_rad * record.canonical_phase_rad for record in records)


def compose_oriented_loop_phases(
    records: Iterable[OrientedLoopPhaseRecord],
    *,
    shared_boundary_phase_rad: float = 0.0,
    cross_artifact_phase_rad: float = 0.0,
    finite_loop_overlap_phase_rad: float = 0.0,
) -> OrientedLoopPhaseComposition:
    """Return the additive composition summary for independent loop records."""

    record_tuple = tuple(records)
    _require_finite("shared_boundary_phase_rad", shared_boundary_phase_rad)
    _require_finite("cross_artifact_phase_rad", cross_artifact_phase_rad)
    _require_finite("finite_loop_overlap_phase_rad", finite_loop_overlap_phase_rad)
    linear_sum = linear_oriented_phase_rad(record_tuple)
    correction_sum = math.fsum(
        (
            shared_boundary_phase_rad,
            cross_artifact_phase_rad,
            finite_loop_overlap_phase_rad,
        )
    )
    return OrientedLoopPhaseComposition(
        record_count=len(record_tuple),
        linear_sum_rad=linear_sum,
        composed_phase_rad=linear_sum + correction_sum,
        squared_loss_rad2=oriented_phase_squared_loss_rad2(record_tuple),
        shared_boundary_phase_rad=shared_boundary_phase_rad,
        cross_artifact_phase_rad=cross_artifact_phase_rad,
        finite_loop_overlap_phase_rad=finite_loop_overlap_phase_rad,
        finite_loop_correction_rad=math.fsum(record.weight * record.oriented_finite_loop_phase_rad for record in record_tuple),
        max_abs_scalarization_residual_per_m2=max(
            (abs(record.scalarization_residual_per_m2) for record in record_tuple),
            default=0.0,
        ),
    )


def reverse_loop_orientation(record: OrientedLoopPhaseRecord) -> OrientedLoopPhaseRecord:
    """Return the same canonical record with reversed traversal orientation."""

    return replace(record, orientation=-record.orientation)


def estimate_oriented_phase_curvature(
    records: Iterable[OrientedLoopPhaseRecord],
    *,
    plane_weights: Mapping[Plane, float] | None = None,
    require_full_coverage: bool = True,
    raise_on_validation: bool = True,
) -> CurvatureEstimate:
    """Estimate curvature from phase-derived defects using the 05S2 estimator."""

    pulse_records = tuple(record.to_pulse_loop_record() for record in records)
    return estimate_pulse_record_curvature(
        pulse_records,
        plane_weights=plane_weights,
        require_full_coverage=require_full_coverage,
        raise_on_validation=raise_on_validation,
    )


def synthesize_oriented_phase_records_from_sectional_curvatures(
    sectional_curvatures_per_m2: Mapping[Plane, float],
    *,
    area_m2: float,
    phase_coupling_rad: float = 1.0,
    finite_loop_phase_rad: float = 0.0,
    scalarization_residual_per_m2: float = 0.0,
    loop_scale_m: float | None = None,
) -> tuple[OrientedLoopPhaseRecord, ...]:
    """Create deterministic phase records from analytic sectional curvatures."""

    _require_positive("area_m2", area_m2)
    _require_positive("phase_coupling_rad", phase_coupling_rad)
    _require_finite("finite_loop_phase_rad", finite_loop_phase_rad)
    _require_finite("scalarization_residual_per_m2", scalarization_residual_per_m2)
    if loop_scale_m is not None:
        _require_positive("loop_scale_m", loop_scale_m)

    records: list[OrientedLoopPhaseRecord] = []
    for plane in LOCAL_FRAME_PLANES:
        value = sectional_curvatures_per_m2.get(plane)
        if value is None:
            continue
        _require_finite(f"sectional_curvatures_per_m2[{plane}]", value)
        corrected_phase = phase_coupling_rad * value * area_m2
        records.append(
            OrientedLoopPhaseRecord(
                plane=plane,
                area_m2=area_m2,
                observed_phase_rad=corrected_phase + finite_loop_phase_rad,
                finite_loop_phase_rad=finite_loop_phase_rad,
                scalarization_residual_per_m2=scalarization_residual_per_m2,
                phase_coupling_rad=phase_coupling_rad,
                loop_scale_m=loop_scale_m,
            )
        )
    return tuple(records)


def _canonical_plane(name: str, plane: Plane) -> Plane:
    if len(plane) != 2:
        raise ValueError(f"{name} plane keys must have two axes")
    first_axis, second_axis = plane
    _require_axis(f"{name} plane first axis", first_axis)
    _require_axis(f"{name} plane second axis", second_axis)
    if first_axis == second_axis:
        raise ValueError(f"{name} plane axes must be distinct")
    return (first_axis, second_axis) if first_axis < second_axis else (second_axis, first_axis)


def _require_axis(name: str, axis: int) -> None:
    if not isinstance(axis, int) or not 0 <= axis <= 3:
        raise ValueError(f"{name} must be a local-frame axis integer from 0 to 3")


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_nonempty_string(name: str, value: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a non-empty string")


def _require_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _require_orientation(name: str, value: float) -> None:
    _require_finite(name, value)
    if value not in {-1.0, 1.0}:
        raise ValueError(f"{name} must be -1.0 or 1.0")


__all__ = [
    "TAU_RADIANS",
    "PhaseComparisonEdge",
    "OrientedLoopPhaseComposition",
    "OrientedLoopPhaseRecord",
    "closed_phase_sum_rad",
    "compose_oriented_loop_phases",
    "estimate_oriented_phase_curvature",
    "linear_oriented_phase_rad",
    "oriented_phase_squared_loss_rad2",
    "reverse_loop_orientation",
    "synthesize_oriented_phase_records_from_sectional_curvatures",
]
