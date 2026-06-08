---
title: Geometry Action
sidebar_label: Geometry Action Index
sidebar_position: 1
---

# Geometry Action

This branch asks whether pulse or phase consistency can motivate the geometric action used by general relativity, and whether any bounded diagnostic residuals point beyond the conservative model.

## Branch Verdict

The geometry-action branch is a useful conditional and diagnostic scaffold. It does **not** yet derive the Einstein-Hilbert action from arbitrary pulse counts. It also does **not** accept torsion, nonmetricity, independent connection dynamics, finite-loop corrections, or quantum source-response as new physics.

The branch is valuable because it keeps the failure boundary sharp: each diagnostic states what would be needed to become a derivation, prediction, or clean no-go.

## Reading Order

1. [Geometry phase functional from pulse consistency](./phase_functional_from_pulse_consistency.md)
2. [05S pulse-network strengthening](./pulse_network_strengthening.md)
3. [05S2 pulse-record curvature estimator](./pulse_record_curvature_estimator.md)
4. [05S3 correction phenomenology](./correction_phenomenology.md)
5. [05S4 oriented loop phase](./oriented_loop_phase.md)
6. [05S5 spin/full-connection holonomy](./spin_connection_holonomy.md)

## Accepted Outputs

- conditional low-energy geometry-action support under explicit assumptions
- executable pulse-network and curvature-estimator diagnostics
- bounded finite-loop and correction-phenomenology guardrails
- operational oriented-loop phase record contract
- torsion-free spin and polarization holonomy as representation lifts of H3 frame holonomy
- bounded Lorentz-connection residual diagnostic after artifact checks

## Rejected Overclaims

- no arbitrary raw pulse-count derivation of Einstein-Hilbert gravity
- no accepted phase-to-defect coefficient rule
- no accepted physical finite-loop scale
- no accepted torsion or nonmetricity signal
- no independent connection dynamics
- no source-response law for quantum branches

## Code And Tests

- `src/pulse_model/pulse_regge.py`
- `src/pulse_model/pulse_record_curvature.py`
- `src/pulse_model/correction_phenomenology.py`
- `src/pulse_model/oriented_loop_phase.py`
- `src/pulse_model/spin_connection_holonomy.py`
- `tests/test_pulse_regge.py`
- `tests/test_pulse_record_curvature.py`
- `tests/test_correction_phenomenology.py`
- `tests/test_oriented_loop_phase.py`
- `tests/test_spin_connection_holonomy.py`
