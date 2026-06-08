---
title: H2 Metric Reconstruction
sidebar_label: H2 Index
sidebar_position: 1
---

# H2 Metric Reconstruction

H2 asks whether relational pulse counts and signal exchanges can determine the Lorentzian metric, up to diffeomorphism.

## Current Verdict

H2 is accepted for the ideal fixed-event uniqueness theorem and partially accepted for restricted finite-data prototype slices. H2S1 adds a raw event-graph reconstruction diagnostic. H2 is not accepted for arbitrary sparse-record metric reconstruction.

The acceptance report is [H2 metric reconstruction acceptance](../../evidence/acceptance_reports/h2_metric_reconstruction.md).

## Reading Order

1. [Metric reconstruction from pulse comparisons](./metric_reconstruction_from_pulse_comparisons.md)
2. [Finite pulse-record schema](./finite_pulse_record_schema.md)
3. [Finite-data stability and gauge](./finite_data_stability_and_gauge.md)
4. [Raw relational identifiability](./raw_relational_identifiability.md)
5. [Raw event-graph reconstruction](./raw_event_graph_reconstruction.md)

## Accepted Outputs

- ideal fixed-event uniqueness under stated smooth-event, clock, signal, and richness assumptions
- finite schema for practical pulse and signal records
- restricted finite-data prototype estimators and stability conditions
- raw event-graph reconstruction diagnostic for a controlled slice

## Rejected Overclaims

- no general reconstruction from arbitrary sparse finite records
- no automatic derivation of the smooth event manifold from arbitrary raw data
- no full metric-field solver without ansatz, gauge, calibration, and nuisance models

## Code And Tests

- `src/pulse_model/h2_reconstruction.py`
- `src/pulse_model/raw_record_reconstruction.py`
- `tests/test_h2_reconstruction.py`
- `tests/test_raw_record_reconstruction.py`
