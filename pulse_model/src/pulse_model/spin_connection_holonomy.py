"""Focused 05S5 spin-connection holonomy helpers.

This module implements only the record algebra justified by the 05S5 appendix:
spatial H3 frame-holonomy generators lifted into the spin-half representation,
local-frame conjugation checks, artifact-subtracted scalar spin phases, and
bounded residual classification. It is not a full spinor field or torsion
solver.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .h3_holonomy import Matrix4
from .oriented_loop_phase import TAU_RADIANS

Matrix2C = tuple[tuple[complex, complex], tuple[complex, complex]]
Vector3 = tuple[float, float, float]

IDENTITY_SPINOR_HOLONOMY: Matrix2C = (
    (1.0 + 0.0j, 0.0 + 0.0j),
    (0.0 + 0.0j, 1.0 + 0.0j),
)


@dataclass(frozen=True)
class SpinPhaseRecord:
    """One scalar spin-sensitive phase comparison after ledgers.

    ``levi_civita_phase_rad`` is the H3-predicted representation-lift phase in
    the same branch convention as the observed phase.
    """

    observed_phase_rad: float
    levi_civita_phase_rad: float = 0.0
    spin_preparation_phase_rad: float = 0.0
    magnetic_phase_rad: float = 0.0
    berry_phase_rad: float = 0.0
    detector_phase_rad: float = 0.0
    instrument_phase_rad: float = 0.0
    finite_loop_phase_rad: float = 0.0
    unwrap_turns: int = 0
    orientation: float = 1.0
    area_m2: float | None = None
    source_response_supplied: bool = False
    source_id: str = ""

    def __post_init__(self) -> None:
        _require_finite("observed_phase_rad", self.observed_phase_rad)
        _require_finite("levi_civita_phase_rad", self.levi_civita_phase_rad)
        _require_finite("spin_preparation_phase_rad", self.spin_preparation_phase_rad)
        _require_finite("magnetic_phase_rad", self.magnetic_phase_rad)
        _require_finite("berry_phase_rad", self.berry_phase_rad)
        _require_finite("detector_phase_rad", self.detector_phase_rad)
        _require_finite("instrument_phase_rad", self.instrument_phase_rad)
        _require_finite("finite_loop_phase_rad", self.finite_loop_phase_rad)
        if not isinstance(self.unwrap_turns, int):
            raise ValueError("unwrap_turns must be an integer")
        _require_orientation("orientation", self.orientation)
        if self.area_m2 is not None:
            _require_positive("area_m2", self.area_m2)

    @property
    def unwrapped_observed_phase_rad(self) -> float:
        return self.observed_phase_rad + TAU_RADIANS * self.unwrap_turns

    @property
    def artifact_phase_rad(self) -> float:
        return math.fsum(
            (
                self.spin_preparation_phase_rad,
                self.magnetic_phase_rad,
                self.berry_phase_rad,
                self.detector_phase_rad,
                self.instrument_phase_rad,
                self.finite_loop_phase_rad,
            )
        )

    @property
    def canonical_residual_phase_rad(self) -> float:
        return self.unwrapped_observed_phase_rad - self.levi_civita_phase_rad - self.artifact_phase_rad

    @property
    def oriented_residual_phase_rad(self) -> float:
        return self.orientation * self.canonical_residual_phase_rad

    @property
    def residual_density_rad_per_m2(self) -> float:
        if self.area_m2 is None:
            raise ValueError("area_m2 is required for residual density")
        return self.oriented_residual_phase_rad / self.area_m2

    @property
    def classification(self) -> str:
        if math.isclose(self.canonical_residual_phase_rad, 0.0, rel_tol=1.0e-15, abs_tol=1.0e-15):
            return "representation-lift-only"
        if self.source_response_supplied:
            return "bounded-connection-diagnostic"
        return "source-response-missing"


@dataclass(frozen=True)
class SpinHolonomyComparison:
    """Observed spin holonomy compared with the H3 Levi-Civita spin lift."""

    observed_holonomy: Matrix2C
    levi_civita_holonomy: Matrix2C = IDENTITY_SPINOR_HOLONOMY
    artifact_holonomy: Matrix2C = IDENTITY_SPINOR_HOLONOMY
    area_m2: float | None = None
    source_response_supplied: bool = False
    source_id: str = ""

    def __post_init__(self) -> None:
        _require_matrix2c("observed_holonomy", self.observed_holonomy)
        _require_matrix2c("levi_civita_holonomy", self.levi_civita_holonomy)
        _require_matrix2c("artifact_holonomy", self.artifact_holonomy)
        if self.area_m2 is not None:
            _require_positive("area_m2", self.area_m2)

    @property
    def residual_holonomy(self) -> Matrix2C:
        return spinor_holonomy_residual(
            self.observed_holonomy,
            self.levi_civita_holonomy,
            self.artifact_holonomy,
        )

    @property
    def residual_norm(self) -> float:
        return spinor_holonomy_distance(self.residual_holonomy, IDENTITY_SPINOR_HOLONOMY)

    @property
    def residual_density_per_m2(self) -> float:
        if self.area_m2 is None:
            raise ValueError("area_m2 is required for residual density")
        return self.residual_norm / self.area_m2

    @property
    def classification(self) -> str:
        if math.isclose(self.residual_norm, 0.0, rel_tol=1.0e-15, abs_tol=1.0e-15):
            return "representation-lift-only"
        if self.source_response_supplied:
            return "bounded-connection-diagnostic"
        return "source-response-missing"


def unwrap_spin_phase_rad(principal_phase_rad: float, *, unwrap_turns: int = 0) -> float:
    """Return a scalar spin phase with an explicit integer cycle unwrap."""

    _require_finite("principal_phase_rad", principal_phase_rad)
    if not isinstance(unwrap_turns, int):
        raise ValueError("unwrap_turns must be an integer")
    return principal_phase_rad + TAU_RADIANS * unwrap_turns


def rotation_vector_from_spatial_frame_generator(generator: Matrix4) -> Vector3:
    """Extract the spatial rotation vector from an H3 4x4 generator.

    This helper intentionally accepts only the spatial rotation block used by
    the first executable 05S5 checks. Boost components are rejected instead of
    being silently modeled.
    """

    _require_matrix4("generator", generator)
    for index in range(4):
        if not math.isclose(generator[0][index], 0.0, rel_tol=1.0e-15, abs_tol=1.0e-15):
            raise ValueError("generator must not contain time-row boost components")
        if not math.isclose(generator[index][0], 0.0, rel_tol=1.0e-15, abs_tol=1.0e-15):
            raise ValueError("generator must not contain time-column boost components")
    for row in range(1, 4):
        if not math.isclose(generator[row][row], 0.0, rel_tol=1.0e-15, abs_tol=1.0e-15):
            raise ValueError("spatial generator diagonal entries must be zero")
        for column in range(row + 1, 4):
            if not math.isclose(generator[row][column], -generator[column][row], rel_tol=1.0e-15, abs_tol=1.0e-15):
                raise ValueError("spatial generator block must be antisymmetric")

    return (
        generator[2][3],
        generator[3][1],
        generator[1][2],
    )


def spin_half_lift_from_frame_generator(generator: Matrix4, *, lift_sign: int = 1) -> Matrix2C:
    """Return the spin-half lift of a spatial H3 frame-holonomy generator."""

    return spin_half_holonomy_from_rotation_vector(
        rotation_vector_from_spatial_frame_generator(generator),
        lift_sign=lift_sign,
    )


def spin_half_holonomy_from_rotation_vector(rotation_vector_rad: Vector3, *, lift_sign: int = 1) -> Matrix2C:
    """Return the SU(2) spin-half holonomy for a spatial rotation vector."""

    _require_lift_sign(lift_sign)
    _require_vector3("rotation_vector_rad", rotation_vector_rad)
    x_rad, y_rad, z_rad = rotation_vector_rad
    angle_rad = math.sqrt(x_rad * x_rad + y_rad * y_rad + z_rad * z_rad)
    if angle_rad == 0.0:
        return _scale_matrix2c(IDENTITY_SPINOR_HOLONOMY, complex(lift_sign, 0.0))

    nx = x_rad / angle_rad
    ny = y_rad / angle_rad
    nz = z_rad / angle_rad
    half_angle_rad = 0.5 * angle_rad
    c = math.cos(half_angle_rad)
    s = math.sin(half_angle_rad)
    matrix = (
        (complex(c, -s * nz), complex(-s * ny, -s * nx)),
        (complex(s * ny, -s * nx), complex(c, s * nz)),
    )
    return _scale_matrix2c(matrix, complex(lift_sign, 0.0))


def reverse_spinor_holonomy(holonomy: Matrix2C) -> Matrix2C:
    """Return the inverse holonomy for a reversed loop."""

    return inverse_matrix2c(holonomy)


def spinor_holonomy_residual(
    observed_holonomy: Matrix2C,
    levi_civita_holonomy: Matrix2C,
    artifact_holonomy: Matrix2C = IDENTITY_SPINOR_HOLONOMY,
) -> Matrix2C:
    """Return ``observed * inverse(levi_civita) * inverse(artifact)``.

    With this left-applied artifact convention, an artifact-explained record is
    ``observed = artifact * levi_civita``. The order matters for non-commuting
    spinor holonomies.
    """

    _require_matrix2c("observed_holonomy", observed_holonomy)
    _require_matrix2c("levi_civita_holonomy", levi_civita_holonomy)
    _require_matrix2c("artifact_holonomy", artifact_holonomy)
    return multiply_matrix2c(
        multiply_matrix2c(observed_holonomy, inverse_matrix2c(levi_civita_holonomy)),
        inverse_matrix2c(artifact_holonomy),
    )


def conjugate_spinor_holonomy(holonomy: Matrix2C, gauge_holonomy: Matrix2C) -> Matrix2C:
    """Return a local-frame relabeling by conjugation."""

    _require_matrix2c("holonomy", holonomy)
    _require_matrix2c("gauge_holonomy", gauge_holonomy)
    return multiply_matrix2c(multiply_matrix2c(gauge_holonomy, holonomy), inverse_matrix2c(gauge_holonomy))


def multiply_matrix2c(left: Matrix2C, right: Matrix2C) -> Matrix2C:
    """Multiply two 2x2 complex matrices."""

    _require_matrix2c("left", left)
    _require_matrix2c("right", right)
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def inverse_matrix2c(matrix: Matrix2C) -> Matrix2C:
    """Return the inverse of a nonsingular 2x2 complex matrix."""

    _require_matrix2c("matrix", matrix)
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if abs(determinant) == 0.0:
        raise ValueError("matrix must be nonsingular")
    inv_det = 1.0 / determinant
    return (
        (matrix[1][1] * inv_det, -matrix[0][1] * inv_det),
        (-matrix[1][0] * inv_det, matrix[0][0] * inv_det),
    )


def spinor_holonomy_distance(left: Matrix2C, right: Matrix2C = IDENTITY_SPINOR_HOLONOMY) -> float:
    """Return Frobenius distance between two spinor holonomy matrices."""

    _require_matrix2c("left", left)
    _require_matrix2c("right", right)
    return math.sqrt(
        math.fsum(
            abs(left[row][column] - right[row][column]) ** 2
            for row in range(2)
            for column in range(2)
        )
    )


def _scale_matrix2c(matrix: Matrix2C, scale: complex) -> Matrix2C:
    return (
        (scale * matrix[0][0], scale * matrix[0][1]),
        (scale * matrix[1][0], scale * matrix[1][1]),
    )


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


def _require_lift_sign(lift_sign: int) -> None:
    if lift_sign not in {-1, 1}:
        raise ValueError("lift_sign must be -1 or 1")


def _require_vector3(name: str, vector: Vector3) -> None:
    if len(vector) != 3:
        raise ValueError(f"{name} must have three entries")
    for index, value in enumerate(vector):
        _require_finite(f"{name}[{index}]", value)


def _require_matrix2c(name: str, matrix: Matrix2C) -> None:
    if len(matrix) != 2:
        raise ValueError(f"{name} must have two rows")
    for row_index, row in enumerate(matrix):
        if len(row) != 2:
            raise ValueError(f"{name} rows must have two entries")
        for column_index, value in enumerate(row):
            if not math.isfinite(value.real) or not math.isfinite(value.imag):
                raise ValueError(f"{name}[{row_index}][{column_index}] must be finite")


def _require_matrix4(name: str, matrix: Matrix4) -> None:
    if len(matrix) != 4:
        raise ValueError(f"{name} must have four rows")
    for row_index, row in enumerate(matrix):
        if len(row) != 4:
            raise ValueError(f"{name} rows must have four entries")
        for column_index, value in enumerate(row):
            _require_finite(f"{name}[{row_index}][{column_index}]", value)
