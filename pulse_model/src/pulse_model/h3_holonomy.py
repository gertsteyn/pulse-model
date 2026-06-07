"""Small H3 loop-holonomy and tidal residual simulations."""

from __future__ import annotations

import math
from collections.abc import Iterable
from dataclasses import dataclass

from .calculations import (
    GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    schwarzschild_tidal_eigenvalues_per_s2,
)

Matrix4 = tuple[tuple[float, float, float, float], ...]


@dataclass(frozen=True)
class FrameLoopSimulation:
    """First-slice local frame-closure simulation."""

    generator: Matrix4
    curvature_per_m2: float
    oriented_area_m2: float
    first_axis: int
    second_axis: int
    scalar_projection_s: float


def corrected_loop_residual_s(
    raw_residual_s: float,
    artifact_corrections_s: Iterable[float],
) -> float:
    """Return raw loop timing residual after independently modeled artifacts."""

    _require_finite("raw_residual_s", raw_residual_s)
    corrections = list(artifact_corrections_s)
    for index, correction_s in enumerate(corrections):
        _require_finite(f"artifact_corrections_s[{index}]", correction_s)

    return raw_residual_s - math.fsum(corrections)


def simulate_frame_loop_holonomy(
    curvature_per_m2: float,
    oriented_area_m2: float,
    first_axis: int,
    second_axis: int,
    scalar_sensitivity_s: float = 0.0,
) -> FrameLoopSimulation:
    """Simulate the leading small-loop frame closure.

    The generator entry is ``curvature_per_m2 * oriented_area_m2`` in the
    requested spatial local-frame plane. This is a local benchmark of the H3
    relation ``K ~ R A``; it is not a general Lorentz transport solver.
    """

    _require_finite("curvature_per_m2", curvature_per_m2)
    _require_finite("oriented_area_m2", oriented_area_m2)
    _require_spatial_axis("first_axis", first_axis)
    _require_spatial_axis("second_axis", second_axis)
    _require_finite("scalar_sensitivity_s", scalar_sensitivity_s)
    if first_axis == second_axis:
        raise ValueError("first_axis and second_axis must be distinct")

    generator_value = curvature_per_m2 * oriented_area_m2
    generator_rows = [[0.0 for _ in range(4)] for _ in range(4)]
    generator_rows[first_axis][second_axis] = generator_value
    generator_rows[second_axis][first_axis] = -generator_value
    generator: Matrix4 = (
        (generator_rows[0][0], generator_rows[0][1], generator_rows[0][2], generator_rows[0][3]),
        (generator_rows[1][0], generator_rows[1][1], generator_rows[1][2], generator_rows[1][3]),
        (generator_rows[2][0], generator_rows[2][1], generator_rows[2][2], generator_rows[2][3]),
        (generator_rows[3][0], generator_rows[3][1], generator_rows[3][2], generator_rows[3][3]),
    )

    return FrameLoopSimulation(
        generator=generator,
        curvature_per_m2=curvature_per_m2,
        oriented_area_m2=oriented_area_m2,
        first_axis=first_axis,
        second_axis=second_axis,
        scalar_projection_s=scalar_sensitivity_s * generator_value,
    )


def schwarzschild_tidal_ranging_residual_m(
    mass_kg: float,
    radius_m: float,
    separation_m: float,
    elapsed_proper_time_s: float,
    axis: str = "radial",
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
) -> float:
    """Return short-time Schwarzschild geodesic-deviation displacement."""

    _require_finite("separation_m", separation_m)
    _require_nonnegative("elapsed_proper_time_s", elapsed_proper_time_s)

    radial_per_s2, transverse_1_per_s2, transverse_2_per_s2 = schwarzschild_tidal_eigenvalues_per_s2(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
    )

    if axis == "radial":
        eigenvalue_per_s2 = radial_per_s2
    elif axis in {"transverse", "transverse_1", "theta"}:
        eigenvalue_per_s2 = transverse_1_per_s2
    elif axis in {"transverse_2", "phi"}:
        eigenvalue_per_s2 = transverse_2_per_s2
    else:
        raise ValueError("axis must be radial, transverse, transverse_1, transverse_2, theta, or phi")

    return 0.5 * eigenvalue_per_s2 * separation_m * elapsed_proper_time_s**2


def max_abs_matrix_entry(matrix: Matrix4) -> float:
    """Return the largest absolute matrix entry."""

    _require_matrix4(matrix)
    return max(abs(value) for row in matrix for value in row)


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_spatial_axis(name: str, axis: int) -> None:
    if not isinstance(axis, int) or not 1 <= axis <= 3:
        raise ValueError(f"{name} must be a spatial axis integer from 1 to 3")


def _require_matrix4(matrix: Matrix4) -> None:
    if len(matrix) != 4:
        raise ValueError("matrix must have four rows")
    for row_index, row in enumerate(matrix):
        if len(row) != 4:
            raise ValueError("matrix rows must have four entries")
        for column_index, value in enumerate(row):
            _require_finite(f"matrix[{row_index}][{column_index}]", value)
