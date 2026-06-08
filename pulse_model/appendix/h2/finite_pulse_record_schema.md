---
title: H2 Finite Pulse-Record Schema
sidebar_label: Finite Record Schema
sidebar_position: 3
---

# Appendix: Finite Pulse-Record Schema for H2

**Parent hypothesis:** 6.2 Hypothesis H2: The metric is reconstructed from pulse comparisons  
**Status:** Schema / implementation contract  
**Purpose:** Define the finite-data record that H2 reconstruction algorithms consume and synthetic generators produce, without treating coordinates as observables.

---

## 1. Boundary

This appendix is the source of truth for finite pulse and signal records. It sits between the ideal fixed-event theorem and the executable reconstruction prototypes.

The schema must support:

- synthetic generation from known metrics
- reconstruction residuals against candidate metric classes
- calibration and nuisance modeling
- gauge freedom, including coordinate freedom
- sparse, noisy, finite records

It must not store coordinate positions, coordinate times, metric components, or a preferred frame as observed data. Those quantities can appear only as latent variables inside a generator, reconstruction fit, or hidden truth sidecar used for tests.

The finite record is therefore:

$$
\mathcal{D}_{\mathrm{finite}} = (\mathcal{O}, \mathcal{C}, \mathcal{N}, \mathcal{M})
$$

where $\mathcal{O}$ is the observed relational record, $\mathcal{C}$ is calibration information, $\mathcal{N}$ is the nuisance model, and $\mathcal{M}$ is metadata about units, uncertainties, and record provenance.

---

## 2. Core Principle

The observed record contains only operational statements:

- clock $A$ registered pulse count $N$ at event $e$
- signal $s$ was emitted at event $e$ and received at event $r$
- clocks $A$ and $B$ met at a shared event
- a local instrument measured phase, frequency ratio, direction, or acceleration at an event

The reconstruction may introduce latent coordinates $x_e^\mu$, clock embeddings $X_A$, signal curves $Y_s$, tetrads, and metric parameters. These are fit variables, not observations.

Two reconstructions related by a diffeomorphism and corresponding relabeling of latent coordinates represent the same physical answer.

---

## 3. Event Graph

The observed record is an event graph, not a coordinate table.

Graph nodes:

- clock events, meaning local readings on a named clock
- meeting events, meaning equivalence classes of local clock events asserted to coincide
- signal emission and reception endpoints, referenced through clock events

Graph edges:

- clock-order edges between events on the same clock
- clock-segment edges selected for duration residuals
- signal-link edges from emission event to reception event
- meeting-incidence edges joining local clock events to a shared event
- optional phase, direction, and acceleration attachments at graph nodes

The graph may be sparse and disconnected in early examples. A reconstruction model may assign latent event representatives to graph nodes, but those representatives are not part of the observed graph.

---

## 4. Record Containers

The finite record has eight top-level containers.

### 4.1 Clocks

Each clock entry defines an operational counter and its calibration model:

```text
clock_id
clock_species
transition_id
nominal_frequency_hz
frequency_uncertainty_hz
calibration_model_id
environment_model_id
readout_noise_model_id
```

The nominal transition frequency is an input calibration. It is not derived from the reconstructed metric.

### 4.2 Clock Events

Each clock event is a pulse-counter reading on one clock:

```text
event_id
clock_id
local_sequence_index
pulse_count
pulse_count_uncertainty
readout_phase_cycles
readout_phase_uncertainty_cycles
event_role
```

The `local_sequence_index` gives only ordering along a clock. It is not a coordinate time. The `event_role` may mark entries such as `sample`, `signal_emit`, `signal_receive`, or `meeting`.

### 4.3 Clock Segments

Clock segments identify adjacent or selected intervals on a single clock:

```text
segment_id
clock_id
start_event_id
end_event_id
segment_kind
```

The observed operational duration for a segment is computed from pulse counts and calibration:

$$
\Delta T_A(e_i,e_j) = \frac{N_A(e_j)-N_A(e_i)}{f_A}
$$

In finite data, $f_A$ can be replaced by the calibrated effective frequency supplied by the calibration model.

### 4.4 Signal Links

Each signal link records an emitted signal and the corresponding reception:

```text
signal_id
emitter_clock_id
emit_event_id
receiver_clock_id
receive_event_id
signal_species
link_label
path_class_hint
```

The link asserts incidence and propagation by the chosen signal species. It does not assert a coordinate travel time. The optional `path_class_hint` may distinguish direct, reflected, multipath, or unresolved links.

### 4.5 Phase And Frequency Records

Signal phase or frequency information is stored locally at emission or reception:

```text
phase_record_id
signal_id
event_id
clock_id
phase_cycles
phase_uncertainty_cycles
frequency_hz
frequency_uncertainty_hz
phase_wrap_model_id
```

Frequency comparisons are derived from paired local records when available. A phase value may be ambiguous by integer wraps; that ambiguity belongs in the nuisance model.

### 4.6 Direction Records

Direction records describe a signal direction measured by local apparatus:

```text
direction_record_id
signal_id
event_id
clock_id
local_frame_id
direction_components
direction_uncertainty
direction_kind
```

The direction is expressed in a local instrument frame attached to a clock or station. That local frame is part of calibration or a latent fit object. The direction components are not global coordinates.

Direction records are optional for practical reconstruction but proof-grade ideal records require either local signal directions or dense infinitesimal signal families from which they can be recovered.

### 4.7 Acceleration Records

Acceleration records describe local non-gravitational acceleration measured by an onboard instrument:

```text
acceleration_record_id
event_id
clock_id
local_frame_id
acceleration_m_per_s2
acceleration_uncertainty_m_per_s2
bias_model_id
```

Acceleration helps separate support forces, thrust, and station motion from metric structure. It is not itself curvature.

### 4.8 Meeting Records

Meeting records identify events shared by multiple clocks:

```text
meeting_id
event_id
clock_event_ids
coincidence_uncertainty_s
```

A meeting is an incidence assertion. It says multiple local records refer to the same physical event within uncertainty.

---

## 5. Observables

The observed layer contains only quantities that can be read from clocks, signal instruments, local direction sensors, local accelerometers, and incidence labels.

Primary observables:

- pulse counts and pulse-count differences
- clock-event order along each clock
- signal emission and reception incidence
- signal labels matching emission to reception
- local phase and frequency readings
- local signal directions in calibrated instrument frames
- local acceleration readings in calibrated instrument frames
- clock-meeting coincidences

Derived operational observables:

- pulse-derived segment duration $\Delta T_A$
- two-clock frequency ratio
- signal phase difference modulo phase-wrap ambiguity
- round-trip or loop timing residuals computed from pulse counts

Non-observables:

- coordinate event locations $x_e^\mu$
- coordinate times $t_e$
- metric components $g_{\mu\nu}(x)$
- proper time as a prior geometric quantity
- global simultaneity slices
- gravitational potential values $\Phi(x)$ as direct readings
- curvature tensors as direct readings

These non-observables may be inferred by a reconstruction model, but they must not be part of the raw record.

---

## 6. Latent And Gauge Variables

Reconstruction introduces latent variables to explain the observed record.

### 6.1 Latent Variables

Common latent variables include:

- event representatives $x_e^\mu$ in a chosen chart
- clock embeddings $X_A(\lambda)$
- signal curves or tangent directions $Y_s$
- candidate metric parameters $\theta_g$
- local tetrads or instrument-frame orientations $E_A$
- clock frequency corrections $\delta f_A$
- clock phase offsets and readout delays
- signal path choices for multipath records
- environmental shifts such as temperature, magnetic, or pressure shifts

The tuple $(x_e^\mu, X_A, Y_s, E_A, \theta_g)$ is a reconstruction aid. It is not unique.

### 6.2 Gauge Freedoms

Gauge freedoms include:

- arbitrary coordinate relabeling of event representatives
- Poincare freedom in flat-spacetime synthetic tests
- additive potential convention in weak static tests
- clock pulse-origin offsets
- local instrument-frame orientation conventions
- phase-wrap integer choices
- parameter degeneracies in an underconstrained metric ansatz

Gauge fixing is allowed for computation, but any accepted result must state which convention was chosen and which recovered quantities are gauge-invariant or convention-dependent.

---

## 7. Calibration Variables

Calibration variables convert raw local readings into operational comparisons.

Required calibration variables:

- transition frequency and uncertainty for each clock species
- clock-specific fractional frequency offset
- readout latency and uncertainty
- phase readout scale and phase-wrap convention
- local direction-frame alignment and uncertainty
- acceleration bias, scale, and uncertainty
- signal species and propagation model

For an idealized first prototype, most calibration variables may be fixed at nominal values with zero or small uncertainty. The schema still names them so later finite-data work can relax that idealization without changing the record shape.

---

## 8. Nuisance Parameters

Nuisance parameters represent finite-data imperfections rather than new metric structure.

Core nuisance classes:

- count quantization and readout jitter
- finite clock linewidth and drift
- environmental clock shifts
- unknown instrument delays
- missing or mislabeled signal links
- phase-wrap ambiguity
- direction-measurement misalignment
- acceleration bias and sensor noise
- unresolved multipath signal propagation
- finite sampling of clock worldlines
- finite sampling of null directions

The reconstruction may estimate nuisance parameters jointly with metric parameters. It must report when a metric feature is degenerate with a nuisance parameter.

---

## 9. Reconstruction Residuals

A candidate reconstruction predicts observable records from latent embeddings, a metric class, calibration variables, and nuisance variables.

### 9.1 Clock Segment Residual

For a clock segment from $e_i$ to $e_j$, the observed duration is:

$$
\Delta T_A^{\mathrm{obs}} = \frac{N_A(e_j)-N_A(e_i)}{f_A^{\mathrm{eff}}}
$$

The candidate metric predicts:

$$
\Delta \tau_A^{\mathrm{pred}} = \int_{X_A(e_i)}^{X_A(e_j)} d\tau_g
$$

The residual is:

$$
r_\tau = \frac{\Delta T_A^{\mathrm{obs}}-\Delta \tau_A^{\mathrm{pred}}}{\sigma_\tau}
$$

where $\sigma_\tau$ includes count, calibration, and readout uncertainty.

### 9.2 Signal Link Residual

For signal $s$ from event $e$ to event $r$, the candidate must supply a signal curve or tangent data $Y_s$ connecting the latent event representatives. The null residual is:

$$
r_{\mathrm{null}} = \frac{g_{\mu\nu}(Y_s)\dot Y_s^\mu \dot Y_s^\nu}{\sigma_{\mathrm{null}}}
$$

Endpoint incidence is a separate residual:

$$
r_{\mathrm{end}} = \frac{d_{\mathrm{end}}}{\sigma_{\mathrm{end}}}
$$

Here $d_{\mathrm{end}}$ is the endpoint mismatch measured in the chosen latent chart or model coordinates after gauge fixing. It is not an observed coordinate distance.

### 9.3 Frequency And Phase Residual

For paired emission and reception frequency records, the metric predicts:

$$
\rho_g = \frac{(k_\mu u^\mu)_{\mathrm{recv}}}{(k_\mu u^\mu)_{\mathrm{emit}}}
$$

The observed ratio is computed from local frequency readings:

$$
\rho_{\mathrm{obs}} = \frac{\nu_{\mathrm{recv}}}{\nu_{\mathrm{emit}}}
$$

The residual is:

$$
r_\nu = \frac{\rho_{\mathrm{obs}}-\rho_g}{\sigma_\rho}
$$

Phase residuals must include integer wrap nuisance variables when phase is recorded modulo cycles.

### 9.4 Direction Residual

A candidate signal tangent can be projected into the local calibrated instrument frame. The direction residual compares that projected direction with the observed local direction:

$$
r_{\mathrm{dir}} = \frac{\delta\theta_{\mathrm{dir}}}{\sigma_{\mathrm{dir}}}
$$

Here $\delta\theta_{\mathrm{dir}}$ is the angular mismatch in the local instrument frame. This residual depends on local frame calibration and should not be interpreted as a global coordinate-direction comparison.

### 9.5 Acceleration Residual

The candidate predicts proper acceleration along a clock worldline:

$$
a^\mu = u^\nu\nabla_\nu u^\mu
$$

After projection into the local instrument frame, the residual compares predicted and observed acceleration:

$$
r_a = \frac{a_{\mathrm{obs}}-a_{\mathrm{pred}}}{\sigma_a}
$$

This term helps prevent a reconstruction from explaining station thrust or support forces as metric curvature.

### 9.6 Incidence Residual

Meeting records and signal endpoint records impose event-identification constraints. The residual should penalize candidate embeddings that split an asserted shared event or merge unrelated events.

This is a relational constraint. It should be expressed in the latent model only after a gauge convention has been chosen.

### 9.7 Smoothness And Model Residual

Finite records do not determine an arbitrary smooth metric. A reconstruction may add a smoothness, ansatz, or regularization term:

$$
\mathcal{E}_{\mathrm{model}} = \lambda_{\mathrm{model}} R_{\mathrm{model}}
$$

This term is not an observable. It must be reported as a modeling assumption.

### 9.8 Total Residual

A practical reconstruction can combine residuals as:

$$
\mathcal{E} = \sum r_\tau^2 + \sum r_{\mathrm{null}}^2 + \sum r_{\mathrm{end}}^2 + \sum r_\nu^2 + \sum r_{\mathrm{dir}}^2 + \sum r_a^2 + \mathcal{E}_{\mathrm{model}}
$$

Weights and covariance matrices should come from the uncertainty model. If arbitrary weights are used in an early prototype, the report must state that the result is a demonstration rather than a stable estimator.

---

## 10. Synthetic Generation Requirements

A synthetic generator may use coordinates and a known metric internally, but those truth variables must be separated from the observed record.

Generation steps:

1. Choose a truth metric family and parameter values.
2. Choose clock worldlines or station histories in a chart.
3. Choose clock species, calibrations, and environmental models.
4. Sample clock events and integrate truth proper time.
5. Convert proper-time intervals into pulse counts with calibration and noise.
6. Generate signal emissions and receptions by solving the truth signal propagation problem.
7. Record only event IDs, clock IDs, pulse counts, signal links, local phases, local directions, accelerations, and uncertainties.
8. Add finite-data imperfections from the nuisance model.
9. Store truth coordinates and metric parameters only in a hidden test sidecar.

The public synthetic record must remain invariant in meaning under coordinate relabeling of the truth chart.

---

## 11. First Prototype Slice

The first finite-data reconstruction prototype should use the smallest useful subset of this schema.

For Minkowski reconstruction:

- clocks
- clock events
- clock segments
- signal links
- optional acceleration records for non-inertial clocks
- calibration records with fixed nominal frequencies

Expected result: recover the flat metric class up to Poincare and coordinate gauge, without creating curvature from accelerated clocks.

For weak static reconstruction:

- all Minkowski fields
- at least two clocks with stable frequency calibration
- clock segment comparisons across different gravitational potentials
- signal links or meeting records sufficient to constrain which clocks are being compared
- optional frequency records for redshift checks

Expected result: recover potential differences or $g_{00}$ differences up to the additive potential convention.

The prototype may use a restricted metric ansatz. It must state the ansatz because sparse finite records do not reconstruct a general metric.

---

## 12. Acceptance Conditions For Records

A finite record is valid for H2 reconstruction work when:

- every observed numeric field has units and uncertainty
- every signal reception references a matching emission
- every event ID is scoped by relational incidence, not by coordinate values
- clock pulse origins and local sequence orderings are explicit
- calibration variables needed to convert pulse counts into durations are present
- nuisance variables are named even when fixed to ideal values
- latent coordinate fields are absent from the observed record
- synthetic truth data, if present, is stored separately from the observed record
- residuals can be computed from the record plus a candidate reconstruction model

Records that fail these conditions may still be useful for informal examples, but they should not be used as H2 acceptance evidence.

---

## 13. Relation To Adjacent H2 Tasks

This schema unblocks the first reconstruction prototype. The prototype should implement only the subset it needs, but it should preserve the same boundary between observables, latent variables, calibration, and nuisance parameters.

The raw-relational event-identifiability theorem can also use this schema as its finite starting point. That theorem must explain when event incidence and dense signal-link data justify the fixed-event assumptions used by the ideal H2 proof.
