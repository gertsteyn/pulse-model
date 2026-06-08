"""Compatibility smoke tests for the review-2 spin_connection import path."""

from __future__ import annotations

import unittest

from pulse_model import SpinHolonomyComparison as PublicSpinHolonomyComparison
from pulse_model import SpinPhaseRecord as PublicSpinPhaseRecord
from pulse_model import spin_half_holonomy_from_rotation_vector as public_spin_half_holonomy
from pulse_model.spin_connection import (
    IDENTITY_SPINOR_HOLONOMY,
    SpinHolonomyComparison,
    SpinPhaseRecord,
    spin_half_holonomy_from_rotation_vector,
)


class SpinConnectionCompatibilityTests(unittest.TestCase):
    def test_review_2_import_path_reexports_canonical_objects(self) -> None:
        self.assertIs(SpinPhaseRecord, PublicSpinPhaseRecord)
        self.assertIs(SpinHolonomyComparison, PublicSpinHolonomyComparison)
        self.assertIs(spin_half_holonomy_from_rotation_vector, public_spin_half_holonomy)

    def test_identity_holonomy_remains_canonical_identity(self) -> None:
        self.assertEqual(spin_half_holonomy_from_rotation_vector((0.0, 0.0, 0.0)), IDENTITY_SPINOR_HOLONOMY)


if __name__ == "__main__":
    unittest.main()
