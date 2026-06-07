"""Focused 05S3 correction-phenomenology helpers.

This module keeps 05S3 executable checks small and explicit. It propagates
record-derived correction sizes into bounds and benchmark projections; it does
not implement a modified-gravity solver.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .pulse_record_curvature import (
    CurvatureEstimate,
    finite_loop_relative_error,
    max_loop_scale_for_finite_loop_bound,
    scalarization_relative_norm,
)

SUPPORTED_CORRECTION_CHANNELS = (
    "preferred-projection-scalarization",
    "finite-loop-higher-curvature",
)
UNSUPPORTED_CORRECTION_CHANNELS = (
    "squared-loss-promotion",
    "torsion",
    "nonlocal-kernel",
    "lattice-memory",
    "h7-vacuum-energy",
    "cosmology",
)


@dataclass(frozen=True)
class PreferredProjectionParameter:
    """Signed and absolute preferred-projection scalarization size."""

    signed_lambda: float
    relative_size: float
    scalarization_residual_per_m2: float
    reference_scalar_curvature_per_m2: float
    unit: str = "dimensionless"
    residual_unit: str = "m^-2"

    @property
    def sign(self) -> int:
        return _sign(self.signed_lambda)

    @property
    def classification(self) -> str:
        if self.relative_size == 0.0:
            return "unbiased"
        return "preferred-projection-diagnostic"


@dataclass(frozen=True)
class FiniteLoopParameter:
    """Finite-loop correction size and loop-scale bound."""

    finite_loop_bias_per_m4: float
    loop_scale_m: float
    scalar_correction_per_m2: float
    relative_size: float
    max_loop_scale_m: float
    relative_bound: float
    within_bound: bool
    bias_unit: str = "m^-4"
    loop_scale_unit: str = "m"
    scalar_correction_unit: str = "m^-2"

    @property
    def sign(self) -> int:
        return _sign(self.scalar_correction_per_m2)

    @property
    def classification(self) -> str:
        if self.finite_loop_bias_per_m4 == 0.0:
            return "unbiased"
        if self.within_bound:
            return "finite-loop-bounded"
        return "finite-loop-exceeds-bound"


def preferred_projection_parameter(
    estimate: CurvatureEstimate,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> PreferredProjectionParameter:
    """Return the signed 05S3 preferred-projection parameter."""

    _require_positive("curvature_floor_per_m2", curvature_floor_per_m2)
    _require_finite("estimate.scalar_curvature_per_m2", estimate.scalar_curvature_per_m2)
    _require_finite("estimate.scalarization_residual_per_m2", estimate.scalarization_residual_per_m2)
    reference = max(abs(estimate.scalar_curvature_per_m2), curvature_floor_per_m2)
    signed_lambda = estimate.scalarization_residual_per_m2 / reference
    relative_size = scalarization_relative_norm(
        estimate,
        curvature_floor_per_m2=curvature_floor_per_m2,
    )
    return PreferredProjectionParameter(
        signed_lambda=signed_lambda,
        relative_size=relative_size,
        scalarization_residual_per_m2=estimate.scalarization_residual_per_m2,
        reference_scalar_curvature_per_m2=reference,
    )


def finite_loop_parameter(
    finite_loop_bias_per_m4: float,
    loop_scale_m: float,
    reference_scalar_curvature_per_m2: float,
    relative_bound: float,
    *,
    curvature_floor_per_m2: float = 1.0e-30,
) -> FiniteLoopParameter:
    """Return finite-loop correction size and bound status."""

    _require_finite("finite_loop_bias_per_m4", finite_loop_bias_per_m4)
    _require_positive("loop_scale_m", loop_scale_m)
    _require_finite("reference_scalar_curvature_per_m2", reference_scalar_curvature_per_m2)
    _require_nonnegative("relative_bound", relative_bound)
    _require_positive("curvature_floor_per_m2", curvature_floor_per_m2)

    scalar_correction = finite_loop_bias_per_m4 * loop_scale_m * loop_scale_m
    relative_size = finite_loop_relative_error(
        finite_loop_bias_per_m4,
        loop_scale_m,
        reference_scalar_curvature_per_m2,
        curvature_floor_per_m2=curvature_floor_per_m2,
    )
    max_loop_scale = max_loop_scale_for_finite_loop_bound(
        finite_loop_bias_per_m4,
        reference_scalar_curvature_per_m2,
        relative_bound,
        curvature_floor_per_m2=curvature_floor_per_m2,
    )
    return FiniteLoopParameter(
        finite_loop_bias_per_m4=finite_loop_bias_per_m4,
        loop_scale_m=loop_scale_m,
        scalar_correction_per_m2=scalar_correction,
        relative_size=relative_size,
        max_loop_scale_m=max_loop_scale,
        relative_bound=relative_bound,
        within_bound=relative_size <= relative_bound,
    )


def require_supported_correction_channel(channel: str) -> str:
    """Return ``channel`` if 05S3 admits it, otherwise raise ``ValueError``."""

    if channel in SUPPORTED_CORRECTION_CHANNELS:
        return channel
    if channel in UNSUPPORTED_CORRECTION_CHANNELS:
        raise ValueError(f"{channel} is not an admitted 05S3 correction channel")
    raise ValueError(f"unknown 05S3 correction channel: {channel}")


def project_relative_correction_to_benchmark(
    relative_correction: float,
    benchmark_value: float,
) -> float:
    """Project a dimensionless correction onto a known benchmark value.

    This is a bookkeeping helper for falsification checks. It does not assert
    that the correction is a physical source term.
    """

    _require_finite("relative_correction", relative_correction)
    _require_finite("benchmark_value", benchmark_value)
    return relative_correction * benchmark_value


def _sign(value: float) -> int:
    if value > 0.0:
        return 1
    if value < 0.0:
        return -1
    return 0


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
