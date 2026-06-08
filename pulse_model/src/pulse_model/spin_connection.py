"""Compatibility re-exports for the review-2 spin-connection path.

The canonical 05S5 implementation lives in ``spin_connection_holonomy``.
This module keeps the shorter review-2 import path discoverable without
duplicating logic.
"""

from .spin_connection_holonomy import (
    IDENTITY_SPINOR_HOLONOMY,
    SpinHolonomyComparison,
    SpinPhaseRecord,
    conjugate_spinor_holonomy,
    inverse_matrix2c,
    multiply_matrix2c,
    reverse_spinor_holonomy,
    rotation_vector_from_spatial_frame_generator,
    spin_half_holonomy_from_rotation_vector,
    spin_half_lift_from_frame_generator,
    spinor_holonomy_distance,
    spinor_holonomy_residual,
    unwrap_spin_phase_rad,
)

__all__ = [
    "IDENTITY_SPINOR_HOLONOMY",
    "SpinHolonomyComparison",
    "SpinPhaseRecord",
    "conjugate_spinor_holonomy",
    "inverse_matrix2c",
    "multiply_matrix2c",
    "reverse_spinor_holonomy",
    "rotation_vector_from_spatial_frame_generator",
    "spin_half_holonomy_from_rotation_vector",
    "spin_half_lift_from_frame_generator",
    "spinor_holonomy_distance",
    "spinor_holonomy_residual",
    "unwrap_spin_phase_rad",
]
