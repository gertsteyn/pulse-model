"""Pulse-record curvature estimator for 05S2.

This module is a deliberately narrow estimator layer. It converts corrected
small-loop pulse defects into local sectional-curvature samples, then reports
scalar curvature and scalarization diagnostics. It does not use the target
Einstein-Hilbert action as an input.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, replace

from .pulse_regge import (
    LOCAL_FRAME_PLANES,
    LORENTZ_SIGNATURE,
    Plane,
    quadrature_scalar_curvature_from_planes,
    scalar_curvature_from_sectional_planes,
    scalarization_residual_from_planes,
)


@dataclass(frozen=True)
class PulseLoopRecord:
    """Corrected loop-defect record for one local two-plane.

    ``defect`` is signed in the canonical local-plane convention.
    ``orientation`` records the loop traversal sign and is applied once.
    """

    plane: Plane
    area_m2: float
    defect: float
    orientation: float = 1.0
    weight: float = 1.0
    loop_scale_m: float | None = None
    source_id: str = ""

    def __post_init__(self) -> None:
        canonical_plane = _canonical_plane("plane", self.plane)
        object.__setattr__(self, "plane", canonical_plane)
        _require_positive("area_m2", self.area_m2)
        _require_finite("defect", self.defect)
        _require_orientation("orientation", self.orientation)
        _require_positive("weight", self.weight)
        if self.loop_scale_m is not None:
            _require_positive("loop_scale_m", self.loop_scale_m)

    @property
    def sectional_curvature_per_m2(self) -> float:
        """Return the lower-index sectional curvature sample."""

        return self.orientation * self.defect / self.area_m2


@dataclass(frozen=True)
class PlaneCoverage:
    """Coverage diagnostics for the six local Lorentz two-planes."""

    represented_planes: tuple[Plane, ...]
    missing_planes: tuple[Plane, ...]
    record_counts: Mapping[Plane, int]

    @property
    def fraction(self) -> float:
        return len(self.represented_planes) / len(LOCAL_FRAME_PLANES)

    @property
    def is_complete(self) -> bool:
        return not self.missing_planes


@dataclass(frozen=True)
class CurvatureEstimate:
    """Local curvature estimate and scalarization diagnostics."""

    sectional_curvatures_per_m2: Mapping[Plane, float]
    scalar_curvature_per_m2: float
    sampled_scalar_curvature_per_m2: float
    scalarization_residual_per_m2: float
    anisotropic_residuals_per_m2: Mapping[Plane, float]
    plane_coverage: PlaneCoverage
    validation_failures: tuple[str, ...] = ()

    @property
    def plane_coverage_fraction(self) -> float:
        return self.plane_coverage.fraction

    @property
    def is_valid(self) -> bool:
        return not self.validation_failures


@dataclass(frozen=True)
class RefinementLevelEstimate:
    """Curvature-estimator diagnostics at one loop-resolution level."""

    loop_scale_m: float
    estimate: CurvatureEstimate
    true_scalar_curvature_per_m2: float
    scalar_error_per_m2: float
    abs_scalar_error_per_m2: float
    relative_scalar_error: float
    scalarization_classification: str


@dataclass(frozen=True)
class RefinementConvergenceReport:
    """Refinement convergence summary for one benchmark family."""

    levels: tuple[RefinementLevelEstimate, ...]
    adjacent_slopes: tuple[float, ...]
    error_floor_per_m2: float

    @property
    def max_abs_scalar_error_per_m2(self) -> float:
        return max((level.abs_scalar_error_per_m2 for level in self.levels), default=0.0)

    @property
    def max_abs_scalarization_residual_per_m2(self) -> float:
        return max((abs(level.estimate.scalarization_residual_per_m2) for level in self.levels), default=0.0)

    @property
    def scalar_error_classification(self) -> str:
        if not self.levels:
            return "no-levels"
        if self.max_abs_scalar_error_per_m2 <= self.error_floor_per_m2:
            return "exact-within-floor"
        finite_slopes = [slope for slope in self.adjacent_slopes if math.isfinite(slope)]
        if finite_slopes and min(finite_slopes) > 0.0:
            return "convergent"
        return "nonconvergent"

    @property
    def scalarization_classification(self) -> str:
        level_classifications = {level.scalarization_classification for level in self.levels}
        if "coverage-failure" in level_classifications:
            return "coverage-failure"
        if "preferred-projection-correction" in level_classifications:
            return "preferred-projection-correction"
        if level_classifications == {"unbiased"}:
            return "unbiased"
        return "no-levels"

    @property
    def classification(self) -> str:
        scalar_error = self.scalar_error_classification
        scalarization = self.scalarization_classification
        if scalar_error == "no-levels" and scalarization == "no-levels":
            return "no-levels"
        if scalarization == "unbiased":
            return scalar_error
        return f"{scalar_error}-with-{scalarization}"


@dataclass(frozen=True)
class OrientationSensitivityCheck:
    """Compare oriented linear defect with sign-blind squared loss."""

    linear_forward: float
    linear_reversed: float
    squared_forward: float
    squared_reversed: float

    @property
    def linear_changes_sign(self) -> bool:
        return math.isclose(self.linear_forward, -self.linear_reversed, rel_tol=1.0e-15, abs_tol=1.0e-15)

    @property
    def squared_loss_loses_orientation(self) -> bool:
        return math.isclose(self.squared_forward, self.squared_reversed, rel_tol=1.0e-15, abs_tol=1.0e-15)


@dataclass(frozen=True)
class CorrectionBasisEstimate:
    """Controlled correction terms indicated by 05S2 estimator failures."""

    scalarization_residual_per_m2: float
    scalarization_relative_norm: float
    finite_loop_bias_coefficients_per_m4: tuple[float, ...]
    retained_terms: tuple[str, ...]
    unsupported_terms: tuple[str, ...]

    @property
    def finite_loop_bias_mean_per_m4(self) -> float | None:
        if not self.finite_loop_bias_coefficients_per_m4:
            return None
        return math.fsum(self.finite_loop_bias_coefficients_per_m4) / len(self.finite_loop_bias_coefficients_per_m4)


def estimate_pulse_record_curvature(
    records: Iterable[PulseLoopRecord],
    *,
    plane_weights: Mapping[Plane, float] | None = None,
    require_full_coverage: bool = True,
    raise_on_validation: bool = True,
) -> CurvatureEstimate:
    """Estimate local scalar curvature from corrected pulse-loop records."""

    record_list = tuple(records)
    coverage = plane_coverage(record_list)
    failures = _validation_failures(record_list, coverage, require_full_coverage)
    if failures and raise_on_validation:
        raise ValueError("; ".join(failures))

    sectional_curvatures = _weighted_sectional_curvatures(record_list)
    scalar_curvature = scalar_curvature_from_sectional_planes(sectional_curvatures)
    weights = _canonical_plane_weights(plane_weights) if plane_weights is not None else _full_plane_weights()
    sampled_scalar_curvature = quadrature_scalar_curvature_from_planes(sectional_curvatures, weights)
    scalarization_residual = scalarization_residual_from_planes(sectional_curvatures, weights)

    return CurvatureEstimate(
        sectional_curvatures_per_m2=sectional_curvatures,
        scalar_curvature_per_m2=scalar_curvature,
        sampled_scalar_curvature_per_m2=sampled_scalar_curvature,
        scalarization_residual_per_m2=scalarization_residual,
        anisotropic_residuals_per_m2=anisotropic_residuals(sectional_curvatures, scalar_curvature),
        plane_coverage=coverage,
        validation_failures=failures,
    )


def extract_correction_basis(
    estimate: CurvatureEstimate,
    *,
    refinement_report: RefinementConvergenceReport | None = None,
    residual_floor_per_m2: float = 1.0e-30,
    curvature_floor_per_m2: float = 1.0e-30,
) -> CorrectionBasisEstimate:
    """Return the minimal correction basis indicated by current diagnostics."""

    _require_positive("residual_floor_per_m2", residual_floor_per_m2)
    retained_terms: list[str] = []
    scalar_norm = scalarization_relative_norm(estimate, curvature_floor_per_m2=curvature_floor_per_m2)
    if abs(estimate.scalarization_residual_per_m2) > residual_floor_per_m2:
        retained_terms.append("preferred-projection-scalarization")

    finite_loop_coefficients: tuple[float, ...] = ()
    if refinement_report is not None:
        finite_loop_coefficients = finite_loop_bias_coefficients_per_m4(
            refinement_report,
            error_floor_per_m2=refinement_report.error_floor_per_m2,
        )
        if finite_loop_coefficients:
            retained_terms.append("finite-loop-higher-curvature")

    return CorrectionBasisEstimate(
        scalarization_residual_per_m2=estimate.scalarization_residual_per_m2,
        scalarization_relative_norm=scalar_norm,
        finite_loop_bias_coefficients_per_m4=finite_loop_coefficients,
        retained_terms=tuple(retained_terms),
        unsupported_terms=("torsion", "nonlocal-kernel", "lattice-memory"),
    )


def scalarization_relative_norm(
    estimate: CurvatureEstimate,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> float:
    """Return scalarization residual size relative to the scalar estimate."""

    _require_positive("curvature_floor_per_m2", curvature_floor_per_m2)
    return abs(estimate.scalarization_residual_per_m2) / max(
        abs(estimate.scalar_curvature_per_m2),
        curvature_floor_per_m2,
    )


def finite_loop_bias_coefficients_per_m4(
    report: RefinementConvergenceReport,
    *,
    error_floor_per_m2: float | None = None,
) -> tuple[float, ...]:
    """Return scalar finite-loop bias coefficients ``e_R / ell**2``."""

    floor = report.error_floor_per_m2 if error_floor_per_m2 is None else error_floor_per_m2
    _require_positive("error_floor_per_m2", floor)
    coefficients: list[float] = []
    for level in report.levels:
        if level.abs_scalar_error_per_m2 <= floor:
            continue
        coefficients.append(level.scalar_error_per_m2 / (level.loop_scale_m * level.loop_scale_m))
    return tuple(coefficients)


def relative_correction_size(
    correction_per_m2: float,
    reference_scalar_curvature_per_m2: float,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> float:
    """Return correction size relative to a reference scalar curvature."""

    _require_finite("correction_per_m2", correction_per_m2)
    _require_finite("reference_scalar_curvature_per_m2", reference_scalar_curvature_per_m2)
    _require_positive("curvature_floor_per_m2", curvature_floor_per_m2)
    return abs(correction_per_m2) / max(abs(reference_scalar_curvature_per_m2), curvature_floor_per_m2)


def correction_within_relative_bound(
    correction_per_m2: float,
    reference_scalar_curvature_per_m2: float,
    relative_bound: float,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> bool:
    """Return whether a scalar correction passes a stated relative bound."""

    _require_nonnegative("relative_bound", relative_bound)
    return (
        relative_correction_size(
            correction_per_m2,
            reference_scalar_curvature_per_m2,
            curvature_floor_per_m2=curvature_floor_per_m2,
        )
        <= relative_bound
    )


def finite_loop_relative_error(
    finite_loop_bias_per_m4: float,
    loop_scale_m: float,
    reference_scalar_curvature_per_m2: float,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> float:
    """Return relative scalar error from ``B_R ell**2``."""

    _require_finite("finite_loop_bias_per_m4", finite_loop_bias_per_m4)
    _require_positive("loop_scale_m", loop_scale_m)
    scalar_correction = finite_loop_bias_per_m4 * loop_scale_m * loop_scale_m
    return relative_correction_size(
        scalar_correction,
        reference_scalar_curvature_per_m2,
        curvature_floor_per_m2=curvature_floor_per_m2,
    )


def max_loop_scale_for_finite_loop_bound(
    finite_loop_bias_per_m4: float,
    reference_scalar_curvature_per_m2: float,
    relative_bound: float,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> float:
    """Return largest loop scale that keeps ``B_R ell**2`` within a bound."""

    _require_finite("finite_loop_bias_per_m4", finite_loop_bias_per_m4)
    _require_finite("reference_scalar_curvature_per_m2", reference_scalar_curvature_per_m2)
    _require_nonnegative("relative_bound", relative_bound)
    _require_positive("curvature_floor_per_m2", curvature_floor_per_m2)
    if finite_loop_bias_per_m4 == 0.0:
        return math.inf
    reference = max(abs(reference_scalar_curvature_per_m2), curvature_floor_per_m2)
    return math.sqrt(relative_bound * reference / abs(finite_loop_bias_per_m4))


def oriented_linear_defect_functional(records: Iterable[PulseLoopRecord]) -> float:
    """Return the signed linear defect functional for orientation checks."""

    return math.fsum(record.weight * record.orientation * record.defect for record in records)


def squared_defect_loss(records: Iterable[PulseLoopRecord]) -> float:
    """Return the sign-blind squared defect loss used by estimator fitting."""

    return math.fsum(record.weight * record.defect * record.defect for record in records)


def compare_orientation_sensitivity(record: PulseLoopRecord) -> OrientationSensitivityCheck:
    """Compare one record with its orientation reversal."""

    reversed_record = replace(record, orientation=-record.orientation)
    return OrientationSensitivityCheck(
        linear_forward=oriented_linear_defect_functional((record,)),
        linear_reversed=oriented_linear_defect_functional((reversed_record,)),
        squared_forward=squared_defect_loss((record,)),
        squared_reversed=squared_defect_loss((reversed_record,)),
    )


def estimate_refinement_convergence(
    refinement_levels: Iterable[Iterable[PulseLoopRecord]],
    *,
    true_scalar_curvature_per_m2: float,
    plane_weights: Mapping[Plane, float] | None = None,
    error_floor_per_m2: float = 1.0e-30,
    residual_floor_per_m2: float = 1.0e-30,
) -> RefinementConvergenceReport:
    """Estimate convergence diagnostics across loop-refinement levels."""

    _require_finite("true_scalar_curvature_per_m2", true_scalar_curvature_per_m2)
    _require_positive("error_floor_per_m2", error_floor_per_m2)
    _require_positive("residual_floor_per_m2", residual_floor_per_m2)

    levels: list[RefinementLevelEstimate] = []
    for records in refinement_levels:
        record_tuple = tuple(records)
        loop_scale = _representative_loop_scale_m(record_tuple)
        estimate = estimate_pulse_record_curvature(record_tuple, plane_weights=plane_weights)
        scalar_error = estimate.scalar_curvature_per_m2 - true_scalar_curvature_per_m2
        abs_scalar_error = abs(scalar_error)
        relative_error = abs_scalar_error / max(abs(true_scalar_curvature_per_m2), error_floor_per_m2)
        levels.append(
            RefinementLevelEstimate(
                loop_scale_m=loop_scale,
                estimate=estimate,
                true_scalar_curvature_per_m2=true_scalar_curvature_per_m2,
                scalar_error_per_m2=scalar_error,
                abs_scalar_error_per_m2=abs_scalar_error,
                relative_scalar_error=relative_error,
                scalarization_classification=classify_scalarization(
                    estimate,
                    residual_floor_per_m2=residual_floor_per_m2,
                ),
            )
        )

    sorted_levels = tuple(sorted(levels, key=lambda level: level.loop_scale_m, reverse=True))
    return RefinementConvergenceReport(
        levels=sorted_levels,
        adjacent_slopes=_adjacent_convergence_slopes(sorted_levels, error_floor_per_m2),
        error_floor_per_m2=error_floor_per_m2,
    )


def classify_scalarization(
    estimate: CurvatureEstimate,
    *,
    residual_floor_per_m2: float = 1.0e-30,
) -> str:
    """Classify whether scalarization is usable, corrected, or failed."""

    _require_positive("residual_floor_per_m2", residual_floor_per_m2)
    if not estimate.plane_coverage.is_complete:
        return "coverage-failure"
    if abs(estimate.scalarization_residual_per_m2) <= residual_floor_per_m2:
        return "unbiased"
    return "preferred-projection-correction"


def plane_coverage(records: Iterable[PulseLoopRecord]) -> PlaneCoverage:
    """Return represented and missing local two-plane diagnostics."""

    counts = Counter(record.plane for record in records)
    represented = tuple(plane for plane in LOCAL_FRAME_PLANES if counts[plane] > 0)
    missing = tuple(plane for plane in LOCAL_FRAME_PLANES if counts[plane] == 0)
    return PlaneCoverage(represented, missing, {plane: counts[plane] for plane in LOCAL_FRAME_PLANES})


def anisotropic_residuals(
    sectional_curvatures: Mapping[Plane, float],
    scalar_curvature_per_m2: float,
) -> dict[Plane, float]:
    """Return deviations from the constant-curvature scalarization pattern."""

    curvatures = {_canonical_plane("sectional_curvatures", plane): value for plane, value in sectional_curvatures.items()}
    isotropic_scale = scalar_curvature_per_m2 / 12.0
    return {
        plane: curvatures.get(plane, 0.0) - _plane_metric_sign(plane) * isotropic_scale
        for plane in LOCAL_FRAME_PLANES
    }


def constant_curvature_sectional_curvatures(curvature_scale_per_m2: float) -> dict[Plane, float]:
    """Return lower-index sectional curvatures for four-dimensional constant curvature."""

    _require_finite("curvature_scale_per_m2", curvature_scale_per_m2)
    return {plane: _plane_metric_sign(plane) * curvature_scale_per_m2 for plane in LOCAL_FRAME_PLANES}


def trace_free_tidal_sectional_curvatures(tidal_scale_per_m2: float) -> dict[Plane, float]:
    """Return a simple vacuum-like weak-field tidal sectional pattern.

    The pattern has nonzero local tidal components but zero scalar curvature.
    It matches the common Schwarzschild-tidal sign structure up to the chosen
    orientation convention.
    """

    _require_finite("tidal_scale_per_m2", tidal_scale_per_m2)
    q = tidal_scale_per_m2
    return {
        (0, 1): 2.0 * q,
        (0, 2): -q,
        (0, 3): -q,
        (1, 2): -q,
        (1, 3): -q,
        (2, 3): 2.0 * q,
    }


def synthesize_loop_records_from_sectional_curvatures(
    sectional_curvatures: Mapping[Plane, float],
    *,
    area_m2: float,
    weight: float = 1.0,
    loop_scale_m: float | None = None,
) -> tuple[PulseLoopRecord, ...]:
    """Create synthetic corrected loop records from analytic sectional data."""

    _require_positive("area_m2", area_m2)
    _require_positive("weight", weight)
    if loop_scale_m is not None:
        _require_positive("loop_scale_m", loop_scale_m)

    records: list[PulseLoopRecord] = []
    for plane in LOCAL_FRAME_PLANES:
        value = sectional_curvatures.get(plane)
        if value is None:
            continue
        _require_finite(f"sectional_curvatures[{plane}]", value)
        records.append(
            PulseLoopRecord(
                plane=plane,
                area_m2=area_m2,
                defect=value * area_m2,
                weight=weight,
                loop_scale_m=loop_scale_m,
            )
        )
    return tuple(records)


def synthesize_refined_loop_record_levels(
    sectional_curvatures: Mapping[Plane, float],
    *,
    loop_scales_m: Iterable[float],
    finite_loop_bias_per_m4: float = 0.0,
) -> tuple[tuple[PulseLoopRecord, ...], ...]:
    """Create deterministic synthetic refinement levels.

    ``finite_loop_bias_per_m4`` adds a constant-curvature-shaped bias
    proportional to ``loop_scale_m ** 2``. This gives controlled synthetic
    convergence without fitting to a target action.
    """

    _require_finite("finite_loop_bias_per_m4", finite_loop_bias_per_m4)
    levels: list[tuple[PulseLoopRecord, ...]] = []
    for loop_scale_m in loop_scales_m:
        _require_positive("loop_scale_m", loop_scale_m)
        area_m2 = loop_scale_m * loop_scale_m
        biased_curvatures = {
            plane: value + _plane_metric_sign(plane) * finite_loop_bias_per_m4 * area_m2
            for plane, value in sectional_curvatures.items()
        }
        levels.append(
            synthesize_loop_records_from_sectional_curvatures(
                biased_curvatures,
                area_m2=area_m2,
                loop_scale_m=loop_scale_m,
            )
        )
    return tuple(levels)


def spatial_only_plane_weights() -> dict[Plane, float]:
    """Return weights that deliberately keep only spatial two-planes."""

    return {plane: 0.0 if 0 in plane else 1.0 for plane in LOCAL_FRAME_PLANES}


def _weighted_sectional_curvatures(records: tuple[PulseLoopRecord, ...]) -> dict[Plane, float]:
    weighted_sums: defaultdict[Plane, float] = defaultdict(float)
    weights: defaultdict[Plane, float] = defaultdict(float)
    for record in records:
        weighted_sums[record.plane] += record.weight * record.sectional_curvature_per_m2
        weights[record.plane] += record.weight
    return {plane: weighted_sums[plane] / weights[plane] for plane in LOCAL_FRAME_PLANES if weights[plane] > 0.0}


def _validation_failures(
    records: tuple[PulseLoopRecord, ...],
    coverage: PlaneCoverage,
    require_full_coverage: bool,
) -> tuple[str, ...]:
    failures: list[str] = []
    if not records:
        failures.append("at least one pulse-loop record is required")
    if require_full_coverage and coverage.missing_planes:
        failures.append(f"missing local two-plane coverage: {coverage.missing_planes}")
    return tuple(failures)


def _full_plane_weights() -> dict[Plane, float]:
    return {plane: 1.0 for plane in LOCAL_FRAME_PLANES}


def _canonical_plane_weights(weights: Mapping[Plane, float]) -> dict[Plane, float]:
    canonical: dict[Plane, float] = {}
    for plane, value in weights.items():
        canonical_plane = _canonical_plane("plane_weights", plane)
        _require_nonnegative(f"plane_weights[{canonical_plane}]", value)
        canonical[canonical_plane] = value
    return canonical


def _representative_loop_scale_m(records: tuple[PulseLoopRecord, ...]) -> float:
    if not records:
        raise ValueError("at least one pulse-loop record is required")
    scales = [record.loop_scale_m for record in records if record.loop_scale_m is not None]
    if len(scales) != len(records):
        raise ValueError("all records in a refinement level must have loop_scale_m")
    if all(scale == scales[0] for scale in scales):
        return scales[0]
    return math.fsum(scales) / len(scales)


def _adjacent_convergence_slopes(
    levels: tuple[RefinementLevelEstimate, ...],
    error_floor_per_m2: float,
) -> tuple[float, ...]:
    slopes: list[float] = []
    for coarse, fine in zip(levels, levels[1:], strict=False):
        if fine.loop_scale_m >= coarse.loop_scale_m:
            raise ValueError("refinement levels must have strictly decreasing loop scales")
        coarse_error = coarse.abs_scalar_error_per_m2
        fine_error = fine.abs_scalar_error_per_m2
        if coarse_error <= error_floor_per_m2 and fine_error <= error_floor_per_m2:
            slopes.append(math.inf)
            continue
        if fine_error <= error_floor_per_m2:
            slopes.append(math.inf)
            continue
        if coarse_error <= error_floor_per_m2:
            slopes.append(-math.inf)
            continue
        slopes.append(math.log(coarse_error / fine_error) / math.log(coarse.loop_scale_m / fine.loop_scale_m))
    return tuple(slopes)


def _canonical_plane(name: str, plane: Plane) -> Plane:
    if len(plane) != 2:
        raise ValueError(f"{name} must have two axes")
    first_axis, second_axis = plane
    _require_axis(f"{name} first axis", first_axis)
    _require_axis(f"{name} second axis", second_axis)
    if first_axis == second_axis:
        raise ValueError(f"{name} axes must be distinct")
    return (first_axis, second_axis) if first_axis < second_axis else (second_axis, first_axis)


def _plane_metric_sign(plane: Plane) -> float:
    first_axis, second_axis = plane
    return LORENTZ_SIGNATURE[first_axis] * LORENTZ_SIGNATURE[second_axis]


def _require_axis(name: str, axis: int) -> None:
    if not isinstance(axis, int) or not 0 <= axis <= 3:
        raise ValueError(f"{name} must be a local-frame axis integer from 0 to 3")


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


def _require_orientation(name: str, value: float) -> None:
    _require_finite(name, value)
    if value not in {-1.0, 1.0}:
        raise ValueError(f"{name} must be -1.0 or 1.0")
