---
title: H2 Acceptance Report
sidebar_label: H2 Acceptance
sidebar_position: 5
---

# H2 Acceptance Report

**Issue:** `sci-dug.3`  
**Date:** June 7, 2026  
**Gate:** `02 H2 metric reconstruction from pulse comparisons`

## Verdict

H2 is **accepted at the ideal fixed-event level** and **partially accepted at the finite-data prototype level**.

Accepted:

- ideal fixed-event uniqueness of the Lorentzian metric under the reviewed assumptions
- separation of metric uniqueness from event-manifold identification
- finite pulse-record schema for practical records
- first executable finite-data slices for Minkowski, weak-static, stationary direction timing, Shapiro-style spatial delay, and weak-wave differential arm timing, with the Shapiro and weak-wave slices treated as calibrated response benchmarks rather than full raw-record schema implementations
- finite-data gauge and stability conditions for restricted ansatz fits, with first-slice uncertainty propagation demonstrated in code
- sufficient raw-relational conditions for promoting event graphs to fixed-event inputs

Not accepted:

- general reconstruction of an arbitrary metric from sparse finite records
- automatic raw-relational derivation of the smooth event manifold, clock embeddings, or proof-grade signal directions for arbitrary records
- practical metric reconstruction without a stated ansatz, gauge convention, calibration model, and nuisance model

## Artifacts

Proof and schema:

- [H2 fixed-event theorem](./appendix/h2_metric_reconstruction_from_pulse_comparisons.md)
- [H2 finite pulse-record schema](./appendix/h2_finite_pulse_record_schema.md)
- [H2 finite-data stability and gauge conditions](./appendix/h2_finite_data_stability_and_gauge.md)
- [H2 raw relational identifiability](./appendix/h2_raw_relational_identifiability.md)
- [Proof sequence](./proof_sequence.md)

Code:

- `src/pulse_model/h2_reconstruction.py`

Executable checks:

- `tests/test_h2_reconstruction.py`

## Accepted Ideal Result

The ideal H2 theorem proves the following bounded statement:

> Given a fixed smooth event region, incidence map, embedded clock segments, proof-grade signal directions or infinitesimal signal curves, dense null-rich signal data, clock-rich timelike samples, calibrated universal clocks, and a compatible Lorentzian metric, no second compatible Lorentzian metric exists on that fixed-event realization.

The proof strategy is:

- signal directions determine the null cone
- null cones determine the conformal metric class
- calibrated pulse-derived timelike durations fix the conformal factor
- coordinate freedom remains as diffeomorphism gauge

This is enough to make $[g_{\mu\nu}]$ the right ideal H2 target.

The raw-relational appendix states sufficient conditions under which event graphs can supply the fixed-event inputs. It is not a proof that arbitrary raw pulse records automatically produce the event manifold or signal tangent directions.

## Accepted Finite Prototype Result

The finite-data work is accepted only as a restricted prototype.

Implemented slices:

| Slice | Accepted result | Gauge or ansatz |
|---|---|---|
| Minkowski static clocks | Equal pulse-derived clock rates recover the flat static-clock slice | Reference-clock time-scale gauge |
| Weak static field | Clock ratios recover potential differences | Reference clock fixes additive potential convention |
| Stationary direction timing | Counter-propagating signal times recover a signed timing asymmetry | Observable asymmetry, not unique coordinate $g_{0i}$ |
| Spatial delay | Shapiro-style benchmark records recover a $\gamma$ proxy | Calibrated endpoint geometry and mass model supplied as interpretation metadata |
| Weak wave | Differential arm timing benchmark records recover injected $h_+$ | Fixed arm geometry, polarization basis, and long-wavelength approximation supplied as interpretation metadata |

The prototype demonstrates that selected pulse/signal-style records and calibrated response benchmarks can recover selected metric-response parameters with explicit tolerances and uncertainty propagation. It does not yet reconstruct a general metric field or implement the full finite schema for every slice.

## Stability And Gauge Decision

Finite H2 stability is accepted only under the conditions in the stability appendix:

- the metric or response ansatz is stated
- gauge choices are stated
- nuisance variables are fixed, bounded, or jointly estimated
- the residual and covariance model are stated
- the gauge-fixed Jacobian or equivalent sensitivity calculation is full rank for the claimed parameters
- uncertainty propagation is reported
- known degeneracies are named

The current executable prototype satisfies the first-slice gauge conventions and closed-form uncertainty propagation checks. It does not yet satisfy the full Jacobian/covariance stability program for arbitrary finite networks, all nuisance parameters, or full metric-field reconstruction.

## Remaining Assumptions

H2 still depends on:

- clock universality after calibration
- signal propagation by the relevant null structure
- correct signal-link labels
- controlled environmental clock shifts
- enough clock and signal richness for the claimed ansatz
- explicit gauge fixing
- correct nuisance modeling
- finite-data sensitivity above numerical and measurement noise floors
- raw-relational event and signal identifiability conditions for claims beyond fixed-event reconstruction

## H3 Start Decision

H3 can safely start, with a boundary.

H3 may use the ideal fixed-event H2 result as a metric equivalence-class input:

$$
[g_{\mu\nu}]
$$

It may also use the finite prototype outputs as toy or ansatz-level reconstructed metric-response data.

H3 must not assume that H2 has already solved raw-relational event-manifold identification or arbitrary sparse finite-data metric reconstruction. The first H3 task should define a loop observable against a fixed-event or explicitly gauge-fixed reconstructed metric object, then state which parts depend on later H2 strengthening.

## Gate Decision

The `02 H2 metric reconstruction from pulse comparisons` gate is:

- **accepted** for the ideal fixed-event uniqueness theorem
- **partially accepted** for finite-data reconstruction prototypes under stated ansatz and gauge conditions, with full finite-data stability still conditional
- **conditional** for raw-relational identifiability under the sufficient conditions in the appendix
- **not accepted** for arbitrary sparse-record metric reconstruction

This is sufficient to unblock the first H3 loop-observable work, provided H3 keeps the fixed-event and gauge boundaries explicit.
