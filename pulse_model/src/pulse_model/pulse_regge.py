"""Small algebraic pulse-Regge checks for 05S.

This module is intentionally not a general Regge-calculus or GR engine. It
only encodes the local linear-defect identities needed by the 05S appendix.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from dataclasses import dataclass

Matrix4 = tuple[tuple[float, float, float, float], ...]
Plane = tuple[int, int]
LORENTZ_SIGNATURE = (-1.0, 1.0, 1.0, 1.0)
LOCAL_FRAME_PLANES: tuple[Plane, ...] = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)


@dataclass(frozen=True)
class ReggeHinge:
    """Interior hinge contribution ``orientation * area * defect``."""

    area_m2: float
    defect: float
    orientation: float = 1.0

    def __post_init__(self) -> None:
        _require_positive("area_m2", self.area_m2)
        _require_finite("defect", self.defect)
        _require_orientation("orientation", self.orientation)


@dataclass(frozen=True)
class BoundaryHinge:
    """Boundary hinge contribution ``orientation * area * exterior_angle``."""

    area_m2: float
    exterior_angle: float
    orientation: float = 1.0

    def __post_init__(self) -> None:
        _require_positive("area_m2", self.area_m2)
        _require_finite("exterior_angle", self.exterior_angle)
        _require_orientation("orientation", self.orientation)


@dataclass(frozen=True)
class ReggeCell:
    """Cell-volume contribution ``orientation * volume``."""

    volume_m4: float
    orientation: float = 1.0

    def __post_init__(self) -> None:
        _require_positive("volume_m4", self.volume_m4)
        _require_orientation("orientation", self.orientation)


def basis_bivector(first_axis: int, second_axis: int, scale: float = 1.0) -> Matrix4:
    """Return an antisymmetric local-frame bivector in the requested plane."""

    _require_axis("first_axis", first_axis)
    _require_axis("second_axis", second_axis)
    _require_finite("scale", scale)
    if first_axis == second_axis:
        raise ValueError("first_axis and second_axis must be distinct")

    rows = [[0.0 for _ in range(4)] for _ in range(4)]
    rows[first_axis][second_axis] = scale
    rows[second_axis][first_axis] = -scale
    return _matrix4_from_rows(rows)


def lower_first_lorentz_index(generator_mixed: Matrix4) -> Matrix4:
    """Lower the first index of a mixed local Lorentz generator."""

    _require_matrix4("generator_mixed", generator_mixed)
    rows = [
        [LORENTZ_SIGNATURE[row] * generator_mixed[row][column] for column in range(4)]
        for row in range(4)
    ]
    generator_lower = _matrix4_from_rows(rows)
    _require_antisymmetric_matrix4("generator_lower", generator_lower)
    return generator_lower


def raise_first_lorentz_index(generator_lower: Matrix4) -> Matrix4:
    """Raise the first index of a lowered local Lorentz generator."""

    _require_antisymmetric_matrix4("generator_lower", generator_lower)
    rows = [
        [LORENTZ_SIGNATURE[row] * generator_lower[row][column] for column in range(4)]
        for row in range(4)
    ]
    return _matrix4_from_rows(rows)


def zero_matrix4() -> Matrix4:
    """Return a zero local-frame generator."""

    return (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    )


def project_hinge_defect(generator_lower: Matrix4, normal_bivector: Matrix4) -> float:
    """Project a lowered Lorentz generator onto an oriented hinge normal.

    ``generator_lower`` has lower indices. ``normal_bivector`` carries the
    contravariant components used in the contraction. The result is the
    rotation angle or boost rapidity in the stated convention:
    ``0.5 * B^ab K_ab``.
    """

    _require_antisymmetric_matrix4("generator_lower", generator_lower)
    _require_antisymmetric_matrix4("normal_bivector", normal_bivector)
    return 0.5 * math.fsum(
        normal_bivector[row][column] * generator_lower[row][column]
        for row in range(4)
        for column in range(4)
    )


def linear_hinge_sum_m2(hinges: Iterable[ReggeHinge]) -> float:
    """Return the oriented linear Regge sum ``sum s_h A_h epsilon_h``."""

    return math.fsum(hinge.orientation * hinge.area_m2 * hinge.defect for hinge in hinges)


def regge_curvature_integral_m2(hinges: Iterable[ReggeHinge]) -> float:
    """Return the scalar-curvature integral represented by interior hinges."""

    return 2.0 * linear_hinge_sum_m2(hinges)


def boundary_hinge_sum_m2(boundary_hinges: Iterable[BoundaryHinge]) -> float:
    """Return the oriented discrete boundary sum ``sum s_b A_b psi_b``."""

    return math.fsum(
        boundary_hinge.orientation * boundary_hinge.area_m2 * boundary_hinge.exterior_angle
        for boundary_hinge in boundary_hinges
    )


def volume_sum_m4(cell_volumes_m4: Iterable[float]) -> float:
    """Return the positive four-volume sum for a cell-volume list."""

    volumes = list(cell_volumes_m4)
    for index, volume_m4 in enumerate(volumes):
        _require_positive(f"cell_volumes_m4[{index}]", volume_m4)
    return math.fsum(volumes)


def oriented_volume_sum_m4(cells: Iterable[ReggeCell]) -> float:
    """Return the oriented volume sum ``sum s_sigma V_sigma``."""

    return math.fsum(cell.orientation * cell.volume_m4 for cell in cells)


def scalar_curvature_from_sectional_planes(sectional_curvatures: Mapping[Plane, float]) -> float:
    """Return ``R`` from diagonal sectional curvature components.

    Entries are lower-index components ``R_abab`` in a local orthonormal frame.
    Missing planes are treated as zero, making biased quadrature tests small
    and explicit.
    """

    curvatures = _canonical_plane_map("sectional_curvatures", sectional_curvatures)
    return 2.0 * math.fsum(
        _plane_metric_sign(plane) * curvatures.get(plane, 0.0) for plane in LOCAL_FRAME_PLANES
    )


def quadrature_scalar_curvature_from_planes(
    sectional_curvatures: Mapping[Plane, float],
    plane_weights: Mapping[Plane, float],
) -> float:
    """Return the scalar curvature sampled by weighted local two-planes."""

    curvatures = _canonical_plane_map("sectional_curvatures", sectional_curvatures)
    weights = _canonical_plane_map("plane_weights", plane_weights)
    return 2.0 * math.fsum(
        weights.get(plane, 0.0) * _plane_metric_sign(plane) * curvatures.get(plane, 0.0)
        for plane in LOCAL_FRAME_PLANES
    )


def scalarization_residual_from_planes(
    sectional_curvatures: Mapping[Plane, float],
    plane_weights: Mapping[Plane, float],
) -> float:
    """Return the preferred-projection residual from biased plane weights."""

    return quadrature_scalar_curvature_from_planes(
        sectional_curvatures,
        plane_weights,
    ) - scalar_curvature_from_sectional_planes(sectional_curvatures)


def constant_curvature_hinges(
    scalar_curvature_per_m2: float,
    volume_m4: float,
    refinement_cells: int,
) -> tuple[ReggeHinge, ...]:
    """Return a symbolic constant-curvature hinge refinement.

    The construction enforces the Regge scaling relation
    ``2 * sum A_h epsilon_h = R * V`` while making each hinge area scale like
    the square of the cell length and each defect scale like curvature times
    area. It is a convergence check, not a mesh generator.
    """

    _require_finite("scalar_curvature_per_m2", scalar_curvature_per_m2)
    _require_positive("volume_m4", volume_m4)
    if not isinstance(refinement_cells, int) or refinement_cells <= 0:
        raise ValueError("refinement_cells must be a positive integer")

    cell_volume_m4 = volume_m4 / refinement_cells
    hinge_area_m2 = math.sqrt(cell_volume_m4)
    target_linear_sum_m2 = 0.5 * scalar_curvature_per_m2 * volume_m4
    defect = target_linear_sum_m2 / (refinement_cells * hinge_area_m2)
    return tuple(ReggeHinge(hinge_area_m2, defect) for _ in range(refinement_cells))


def _matrix4_from_rows(rows: list[list[float]]) -> Matrix4:
    return (
        (rows[0][0], rows[0][1], rows[0][2], rows[0][3]),
        (rows[1][0], rows[1][1], rows[1][2], rows[1][3]),
        (rows[2][0], rows[2][1], rows[2][2], rows[2][3]),
        (rows[3][0], rows[3][1], rows[3][2], rows[3][3]),
    )


def _canonical_plane_map(name: str, values: Mapping[Plane, float]) -> dict[Plane, float]:
    canonical: dict[Plane, float] = {}
    for plane, value in values.items():
        canonical_plane = _canonical_plane(name, plane)
        _require_finite(f"{name}[{canonical_plane}]", value)
        canonical[canonical_plane] = value
    return canonical


def _canonical_plane(name: str, plane: Plane) -> Plane:
    if len(plane) != 2:
        raise ValueError(f"{name} plane keys must have two axes")
    first_axis, second_axis = plane
    _require_axis(f"{name} plane first axis", first_axis)
    _require_axis(f"{name} plane second axis", second_axis)
    if first_axis == second_axis:
        raise ValueError(f"{name} plane axes must be distinct")
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


def _require_orientation(name: str, value: float) -> None:
    _require_finite(name, value)
    if value not in {-1.0, 1.0}:
        raise ValueError(f"{name} must be -1.0 or 1.0")


def _require_matrix4(name: str, matrix: Matrix4) -> None:
    if len(matrix) != 4:
        raise ValueError(f"{name} must have four rows")
    for row_index, row in enumerate(matrix):
        if len(row) != 4:
            raise ValueError(f"{name} rows must have four entries")
        for column_index, value in enumerate(row):
            _require_finite(f"{name}[{row_index}][{column_index}]", value)


def _require_antisymmetric_matrix4(name: str, matrix: Matrix4) -> None:
    _require_matrix4(name, matrix)
    for row in range(4):
        if matrix[row][row] != 0.0:
            raise ValueError(f"{name} diagonal entries must be zero")
        for column in range(row + 1, 4):
            if not math.isclose(matrix[row][column], -matrix[column][row], abs_tol=1.0e-15):
                raise ValueError(f"{name} must be antisymmetric")
