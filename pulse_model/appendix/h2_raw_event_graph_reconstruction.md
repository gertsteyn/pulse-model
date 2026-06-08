# Appendix: H2S1 Raw Event-Graph Reconstruction

**Parent hypothesis:** 6.2 Hypothesis H2: The metric is reconstructed from pulse comparisons  
**Status:** H2S1 contract / no-geometry boundary  
**Purpose:** Define a finite raw-record reconstruction slice that starts from clock, signal, and meeting records rather than from an already supplied event manifold or metric.

---

## 1. Purpose

H2 already has an ideal fixed-event theorem: if a smooth event region, embedded clock curves, calibrated clock durations, and proof-grade null directions are supplied, then a sufficiently rich record fixes the Lorentzian metric up to gauge. That theorem is useful but circular if it is treated as a reconstruction from raw records, because its inputs already contain much of the geometric structure.

H2S1 is a narrower strengthening task. It asks what can be recovered from a finite event graph whose observed layer contains only local pulse counts, local clock order, signal incidence, and clock-meeting incidence. The first executable target is a controlled $1+1$ dimensional Minkowski synthetic slice, not the full H2 theorem.

The intended output is a diagnostic reconstruction layer:

- recover clock-event ordering from local records
- merge meeting events without adding coordinates
- build event and signal constraints from raw incidence
- report rank, nullspace, and degeneracy labels
- identify when the record is too sparse or inconsistent
- keep generator-only coordinates out of solver inputs

This appendix does not claim general metric reconstruction from arbitrary sparse pulse records.

---

## 2. Accepted Inputs

H2S1 may use these already accepted Pulse Model ingredients:

- H1 local pulse counters as physical clock records
- calibrated transition frequencies where a synthetic test states them as inputs
- clock-local ordered pulse counts
- signal emission and reception records linked by a signal ID
- clock-meeting records that assert coincidence of local readings
- optional uncertainty and provenance fields for finite-data checks
- the H2 fixed-event theorem only as a downstream consumer after raw promotion succeeds

For the first synthetic slice, H2S1 may also use a generator that internally builds $1+1$ dimensional Minkowski worldlines and null signals. Those generator coordinates are ground truth sidecar data for tests. They are not observed reconstruction inputs.

---

## 3. Prohibited Assumptions

The raw reconstruction task must not start from:

- a smooth event manifold
- a known metric
- known coordinates or coordinate time
- known null cones
- pre-embedded clock worldlines
- proof-grade signal tangent directions
- a global simultaneity convention
- a preferred inertial frame
- generator-only event coordinates in solver input

Any implementation or derivation that consumes one of these as an observed input is outside H2S1. It may be a useful fixed-event H2 calculation, but it is not raw event-graph reconstruction.

---

## 4. Required Files

The H2S1 work owns these files:

- `pulse_model/appendix/h2_raw_event_graph_reconstruction.md`
- `pulse_model/src/pulse_model/raw_record_reconstruction.py`
- `pulse_model/tests/test_raw_record_reconstruction.py`

Roadmap files such as `pulse_model/proof_sequence.md` and `pulse_model/promising_tweaks.md` are not part of the early H2S1 tasks. They are reserved for the final verdict task after its Beads blocker is closed.

---

## 5. Raw-Record Vocabulary

An observed raw record is a finite event graph:

$$
G_{\mathrm{raw}} = (C,E,S,M,P)
$$

where:

- $C$ is the finite set of clock IDs
- $E$ is the finite set of clock-local events
- $S$ is the finite set of signal links
- $M$ is the finite set of meeting records
- $P$ is the finite set of pulse and provenance fields attached to events

The observed layer uses these terms:

- **clock ID:** an opaque local counter identity
- **clock-local event:** one local reading on one clock
- **local sequence index:** the observed order of events on one clock
- **pulse count:** the local counter value at an event
- **emission event:** the clock-local event where a signal is emitted
- **reception event:** the clock-local event where the same signal is received
- **signal ID:** the incidence label linking one emission to one reception
- **meeting ID:** the incidence label saying two or more clock-local events coincide
- **provenance field:** source, generator case, uncertainty, or artifact metadata

The latent layer may introduce these fit variables:

- event representatives after meeting merges
- clock worldline order variables
- signal-incidence variables
- affine clock calibration variables
- gauge variables
- synthetic-slice embedding variables used only after the raw graph has been built

The observed layer must distinguish itself from inferred coordinates, inferred embeddings, metric components, and generator truth.

---

## 6. Minimal Raw Schema

The first H2S1 schema has five observed containers. It intentionally omits coordinates, coordinate time, metric components, and local null directions.

### 6.1 Clocks

Each clock record defines one local pulse counter:

```text
clock_id
clock_species
nominal_frequency_hz
frequency_uncertainty_hz
calibration_status
provenance_id
artifact_flags
```

Required fields are `clock_id`, `nominal_frequency_hz`, and `calibration_status`. A clock may be marked `uncalibrated`; in that case scale and rate ambiguity must be reported rather than silently fixed.

### 6.2 Clock Events

Each clock event is one local counter reading:

```text
event_id
clock_id
local_sequence_index
pulse_count
pulse_count_uncertainty
event_role
provenance_id
artifact_flags
```

The pair `(clock_id, local_sequence_index)` gives only local order on one clock. `pulse_count` is a local counter reading, not coordinate time. `event_role` may be `sample`, `signal_emit`, `signal_receive`, `meeting`, or `mixed`.

For a valid clock chain, local order must be monotone:

$$
i < j \Rightarrow N_i < N_j
$$

unless an explicit wrap or reset artifact is declared. The first H2S1 executable slice rejects wraps rather than modeling them.

### 6.3 Signal Links

Each signal link connects one emission event to one reception event:

```text
signal_id
emitter_clock_id
emit_event_id
emission_pulse_count
receiver_clock_id
receive_event_id
reception_pulse_count
signal_species
link_status
noise_model_id
provenance_id
artifact_flags
```

`emission_pulse_count` and `reception_pulse_count` duplicate the endpoint clock-event pulse counts for validation. A valid record requires exact agreement with the referenced endpoint events unless an uncertainty model explicitly permits a bounded mismatch.

The signal link observes incidence:

$$
s: e_{\mathrm{emit}} \to e_{\mathrm{recv}}
$$

It does not observe a coordinate travel time or a null tangent vector.

### 6.4 Meeting Records

Each meeting record asserts that multiple clock-local events are the same physical event within the stated tolerance:

```text
meeting_id
clock_event_ids
coincidence_uncertainty_s
equality_status
provenance_id
artifact_flags
```

The observed equality constraint is:

$$
e_i \sim_M e_j
$$

for every pair of clock-event IDs listed in the same meeting. This is an incidence assertion only. It does not provide a coordinate position.

### 6.5 Noise, Provenance, And Artifact Fields

Noise and provenance are deliberately small:

```text
noise_model_id
standard_uncertainty
tolerance
provenance_id
generator_case_id
artifact_flags
```

The first executable tests may use deterministic zero-noise records and bounded-tolerance inconsistent records. If nonzero noise is supplied, reconstruction must report residuals against the stated tolerance and may not upgrade a noisy fit into a uniqueness claim.

---

## 7. Latent Variable Ledger

The reconstruction may introduce latent variables only after the observed graph has been validated.

### 7.1 Event Labels

Meeting merges define latent event representatives:

```text
representative_event_id
member_clock_event_ids
component_id
```

These representatives are graph identities, not manifold points.

### 7.2 Clock Worldline Order Variables

For each clock, the local order variable is the sorted list of valid clock-event IDs:

```text
clock_id
ordered_event_ids
order_status
```

This is recoverable from `local_sequence_index` and `pulse_count` consistency. It is not a parametrized worldline embedding.

### 7.3 Signal-Incidence Variables

For each signal, the latent incidence variable is:

```text
signal_id
emit_representative_event_id
receive_representative_event_id
component_id
incidence_status
```

This supports graph constraints and later null constraints. It does not include signal direction or coordinate path data.

### 7.4 Calibration Variables

Clock calibration variables are:

```text
clock_id
frequency_hz
frequency_scale_factor
pulse_origin
calibration_status
```

If these are not supplied, they remain nuisance or gauge variables. The reconstruction must then report `calibration-ambiguity`.

### 7.5 Gauge Variables

The synthetic embedding step may choose:

```text
time_origin
space_origin
boost_parameter
orientation_sign
scale_factor
event_label_permutation
```

These choices are conventions used to compare against generator truth. They are not raw observations.

---

## 8. Observed Versus Inferred Boundary

The observed raw record contains:

- clock IDs
- local sequence indexes
- pulse counts and pulse-count uncertainties
- emission pulse counts
- reception pulse counts
- signal IDs
- meeting IDs
- observed equality constraints at meetings
- optional noise, provenance, and artifact fields

The inferred layer may contain:

- merged event representatives
- connected components
- clock order consistency status
- signal incidence status
- calibration nuisance variables
- gauge choices
- synthetic-slice embedding variables
- rank and nullspace summaries

The inferred layer still does not become an observed smooth event manifold. Coordinates and embeddings, when introduced by later tasks, are diagnostic fit variables used to test whether the finite raw graph admits the intended $1+1$ dimensional realization.

---

## 9. Synthetic $1+1$ Dimensional Generator

The first controlled arena is flat $1+1$ dimensional Minkowski spacetime. It is a generator for finite raw records, not an observed reconstruction input.

### 9.1 Generator Coordinates

The generator may use internal inertial coordinates $(t,x)$ with $c=1$ and metric:

$$
ds^2 = -dt^2 + dx^2
$$

For an inertial clock $A$, choose internal parameters:

```text
clock_id
frequency_hz
pulse_origin
t_origin
x_origin
velocity
proper_time_start
proper_time_stop
sample_pulse_counts
```

with $|v_A| < 1$. The generator uses:

$$
\gamma_A = (1-v_A^2)^{-1/2}
$$

$$
t_A(\tau_A) = t_{0,A} + \gamma_A \tau_A
$$

$$
x_A(\tau_A) = x_{0,A} + \gamma_A v_A \tau_A
$$

and pulse count:

$$
N_A(\tau_A) = N_{0,A} + f_A \tau_A
$$

These coordinates and proper times are generator-only truth.

### 9.2 Generated Clock Events

For every sampled pulse count $N_A$, the generator computes:

$$
\tau_A = (N_A - N_{0,A}) / f_A
$$

It then creates a raw clock event with:

```text
event_id
clock_id
local_sequence_index
pulse_count
pulse_count_uncertainty
event_role
provenance_id
artifact_flags
```

The hidden sidecar may store:

```text
truth_event_id
event_id
t
x
proper_time
worldline_parameters
```

The solver must not consume the hidden sidecar.

### 9.3 Generated Meeting Events

For clocks $A$ and $B$, a meeting exists when their generator worldlines intersect within the selected proper-time ranges:

$$
t_A(\tau_A) = t_B(\tau_B)
$$

$$
x_A(\tau_A) = x_B(\tau_B)
$$

If the corresponding pulse counts are sampled, or if the case requests an exact meeting sample, the generator emits:

```text
meeting_id
clock_event_ids
coincidence_uncertainty_s
equality_status
provenance_id
artifact_flags
```

The observed record only states equality of clock-local events. It does not state the internal $(t,x)$ intersection.

### 9.4 Generated Signal Records

For a signal emitted from clock $A$ at pulse count $N_e$, the generator computes the emission event:

$$
(t_e,x_e) = (t_A(\tau_e),x_A(\tau_e))
$$

It finds a future reception event on clock $B$ by solving:

$$
t_B(\tau_r) - t_e = |x_B(\tau_r) - x_e|
$$

If a valid future solution exists in the sampled range, the generator emits a signal link:

```text
signal_id
emitter_clock_id
emit_event_id
emission_pulse_count
receiver_clock_id
receive_event_id
reception_pulse_count
signal_species
link_status
noise_model_id
provenance_id
artifact_flags
```

The null equation is generator truth. The observed signal record contains only emission and reception incidence plus pulse counts.

### 9.5 Observable And Withheld Quantities

Observable raw records:

- clock IDs
- clock-local sequence indexes
- pulse counts
- calibration fields explicitly included in clock records
- meeting IDs and equality groups
- signal IDs and endpoint event IDs
- optional uncertainty, provenance, and artifact flags

Generator-only ground truth:

- internal coordinates $(t,x)$
- proper times $\tau_A$ except as converted to pulse counts through supplied calibration
- velocities and worldline origins
- null-equation solutions
- event embeddings
- true Poincare transform between equivalent sidecars

Withheld from reconstruction:

- coordinate event tables
- coordinate travel times
- signal tangent directions
- metric components
- precomputed clock embeddings
- generator case labels that reveal the expected degeneracy

The tests may inspect the sidecar only after reconstruction, and only to check gauge-aware agreement or deliberate underdetermination.

### 9.6 Implemented Generator Cases

The first executable generator includes these focused cases:

- `single_inertial_clock`: one valid clock chain; useful for order recovery but underdetermined for geometry
- `separated_inertial_clocks`: two nonmeeting inertial clocks with reciprocal signals; useful for null-link constraints and calibrated static ranging
- `crossing_inertial_clocks`: two clock chains with one exact meeting event; useful for event-representative alignment and for confirming that a single meeting is still geometrically underdetermined
- `flat_three_clock_network`: three calibrated static clocks with reciprocal reference-clock links and one non-reference signal; useful for a better-conditioned synthetic rank test
- `sparse_underdetermined`: a weakly linked record that must report underdetermination instead of failure
- `inconsistent_record`: a deliberately impossible pulse order, meeting, or signal endpoint used to test rejection

The generator case label is sidecar metadata for tests. Reconstruction receives only `RawEventRecord`.

### 9.7 Generator Gauge Freedoms

The same observed raw graph can have many equivalent sidecars. The generator contract therefore treats these as gauge:

- translation in $t$
- translation in $x$
- Lorentz boost
- spatial reflection
- clock pulse-origin shift
- global scale if calibration is not fixed
- clock, event, signal, and meeting relabeling

A reconstruction check may compare to generator truth only after applying a stated gauge convention or using gauge-invariant residuals.

---

## 10. Event Ordering And Clock Embedding Constraints

This section defines what can be recovered before null-signal equations are used as metric constraints.

### 10.1 Per-Clock Event Order

For each clock $A$, collect all events with `clock_id = A`. The primary order key is `local_sequence_index`; `pulse_count` is an independent monotonicity check.

Algorithm:

1. group clock events by `clock_id`
2. sort each group by `local_sequence_index`
3. reject duplicate sequence indexes unless an artifact flag declares an unusable record
4. require pulse counts to be strictly increasing in sorted order
5. emit the ordered event list and adjacent order edges

The accepted local order relation is:

$$
e_i \prec_A e_j
$$

when clock $A$ records $e_i$ before $e_j$. This relation is local to one clock and does not define global simultaneity.

### 10.2 Meeting Merge Algorithm

Meeting records define an equivalence relation on clock-local events. The implementation target is a union-find merge:

1. initialize every clock event as its own representative
2. for each meeting record, union every listed `clock_event_id`
3. reject a meeting if any listed event ID is missing
4. reject a meeting if equality forces a local event-order cycle on one clock
5. store the representative and member event IDs

The meeting relation is:

$$
e_i \sim_M e_j
$$

This is an equality of event identity only. It is not equality of clock pulse counts, proper times, or coordinates.

### 10.3 Partial Order Across Records

After meeting merges, build a directed graph over event representatives.

Edges:

- local clock order edges from $e_i \prec_A e_j$
- signal incidence edges from emission representative to reception representative

The signal edge asserts causal direction:

$$
e_{\mathrm{emit}} \prec_S e_{\mathrm{recv}}
$$

At this stage it does not assert a null interval length. The graph must be acyclic inside each connected component. A cycle means the record has `event-order-conflict` unless an explicit artifact model removes one edge.

The partial-order output is:

```text
representative_event_ids
order_edges
signal_edges
topological_order
component_id
order_status
```

Disconnected components keep separate topological orders and must be reported as `disconnected-component`.

### 10.4 Affine Clock Parameters

Each clock may be assigned an affine local parameter:

$$
\lambda_A(e) = \alpha_A N_A(e) + \beta_A
$$

where $N_A(e)$ is the observed pulse count. If the clock frequency is calibrated, then:

$$
\alpha_A = 1/f_A
$$

If calibration is absent, $\alpha_A>0$ remains a calibration variable. The offset $\beta_A$ is a local origin gauge unless a synchronization or reset record fixes it.

Meetings do not imply:

$$
\lambda_A(e_i) = \lambda_B(e_j)
$$

unless the raw record explicitly contains a synchronization rule. A meeting says only that two local readings are the same event. This prevents calibration smuggling.

### 10.5 Synthetic $1+1$ Dimensional Clock Embedding Target

For the synthetic inertial slice, an embedding fit may introduce event-plane variables only after the raw graph has been validated. A clock worldline is represented as:

$$
X_A(\lambda_A) = P_A + U_A \lambda_A
$$

where $P_A$ and $U_A$ are latent $1+1$ dimensional vectors. With calibrated proper-time units, the inertial tangent must satisfy:

$$
\eta(U_A,U_A) = -1
$$

Meeting records impose coordinate equality of the latent embeddings:

$$
X_A(\lambda_A(e_i)) = X_B(\lambda_B(e_j))
$$

for events merged by the same meeting representative.

The Poincare gauge may be fixed for comparison by choosing one reference meeting as the origin and one calibrated reference clock as the rest clock. This is a convention for solving the synthetic system, not an observed fact.

### 10.6 Embedding Identifiability Boundary

Meeting and local-order data alone usually do not determine a unique synthetic embedding. The correct outputs are:

- `single_inertial_clock`: order and affine parameter are recoverable; geometry is underdetermined
- `separated_inertial_clocks`: without meetings, relative offset and boost remain underdetermined until signal constraints are added
- `one_meeting_pair`: event identity is aligned at one point; relative boost and separation history remain gauge or underdetermined
- `connected_meeting_network`: shared event representatives can be embedded up to Poincare gauge if enough nonconflicting meetings constrain the component
- `weakly_connected_network`: partial order exists, but non-gauge embedding variables remain in the nullspace
- `disconnected_network`: no cross-component embedding claim is allowed

This is the honest H2S1.4 conclusion: the raw event graph can recover order, event identity, and affine clock parameters, but metric-bearing separation structure requires the null-signal constraints and rank analysis in the next task.

---

## 11. Null-Signal Constraints And Rank Tests

Null-signal constraints are added only after raw schema validation, meeting merges, partial-order construction, and latent synthetic variables have been declared.

### 11.1 Null Residual From A Signal Record

For each signal link $s$, let $e_s$ be the representative emission event and $r_s$ be the representative reception event. In the synthetic $1+1$ dimensional fit, introduce latent coordinates:

$$
X(e) = (t_e,x_e)
$$

The signal record contributes the future-directed constraint:

$$
t_{r_s} - t_{e_s} > 0
$$

and the null residual:

$$
q_s = (t_{r_s} - t_{e_s})^2 - (x_{r_s} - x_{e_s})^2
$$

A perfect flat synthetic record has:

$$
q_s = 0
$$

The reconstruction receives only the signal endpoint IDs and pulse counts. The coordinates in $q_s$ are latent variables introduced by the fit.

### 11.2 Clock-Embedding Residuals

When using inertial clock-line variables, every event $e$ on clock $A$ has:

$$
X(e) = P_A + U_A \lambda_A(e)
$$

with:

$$
\lambda_A(e) = \alpha_A N_A(e) + \beta_A
$$

The calibrated inertial norm residual is:

$$
h_A = \eta(U_A,U_A) + 1
$$

Meeting records impose:

$$
m_{ij} = X(e_i) - X(e_j)
$$

for events merged by the same representative. The first implementation may use event-coordinate variables or clock-line variables, but it must report which variable set was used.

### 11.3 Gauge-Fixing Convention For Rank

Rank is meaningful only after gauge has been fixed or removed. The first synthetic convention is:

- analyze one connected component at a time
- choose one reference representative event and set $t=0$, $x=0$
- choose one calibrated reference clock in that component
- set the reference clock at rest in the fit gauge
- set the reference clock pulse-origin convention through $\beta_{\mathrm{ref}}=0$
- if no calibrated clock exists, set one scale convention and report `calibration-ambiguity`
- choose one orientation convention when possible, but report `mirror-boost-ambiguity` if the record does not fix orientation

Equivalently, an implementation may project known translation, boost, and scale gauge directions out of the Jacobian instead of adding explicit gauge-fixing rows. The rank report must state which route was used.

### 11.4 Linearized Constraint System

Collect all residuals into:

$$
R(z) = (q_s,m_{ij},h_A,g_k)
$$

where $z$ is the vector of latent fit variables and $g_k$ are gauge-fixing residuals if explicit gauge rows are used.

At a candidate solution $z_0$, compute the linearized system:

$$
J \delta z = -R(z_0)
$$

with:

$$
J_{ab} = \partial R_a / \partial z_b
$$

For a null-signal residual using event-coordinate variables, the nonzero derivatives are:

$$
\partial q_s / \partial t_{e_s} = -2(t_{r_s}-t_{e_s})
$$

$$
\partial q_s / \partial t_{r_s} = 2(t_{r_s}-t_{e_s})
$$

$$
\partial q_s / \partial x_{e_s} = 2(x_{r_s}-x_{e_s})
$$

$$
\partial q_s / \partial x_{r_s} = -2(x_{r_s}-x_{e_s})
$$

Clock-line variables use the same residuals with the chain rule through $X_A(\lambda_A)$.

The first executable static diagnostic uses a narrower signed $1+1$ dimensional clock-line slice. It fixes one calibrated reference clock at $x=0$ and gives each non-reference clock a fitted offset $\beta_A$ and signed distance $x_A$.

Reference-clock signal rows are always linear in this slice. Non-reference signal rows are added only when the reference-clock and meeting rows already fix both endpoint distances enough to select the signed orientation branch. If that branch is not fixed, the record remains an underdetermined or mirror/orientation-ambiguous diagnostic instead of being forced into a false inconsistency.

For a signal from the reference clock $R$ to clock $A$, the row is:

$$
\beta_A - x_A = \tau_R(e_s) - \tau_A(r_s)
$$

For a signal from clock $A$ to the reference clock $R$, the row is:

$$
\beta_A + x_A = \tau_R(r_s) - \tau_A(e_s)
$$

For a signal from non-reference clock $A$ to non-reference clock $B$ when $x_B>x_A$ in the chosen orientation convention, the row is:

$$
\beta_B - x_B - \beta_A + x_A = \tau_A(e_s) - \tau_B(r_s)
$$

When the reference rows fix $x_B<x_A$, the opposite branch is:

$$
\beta_B + x_B - \beta_A - x_A = \tau_A(e_s) - \tau_B(r_s)
$$

A meeting with a reference-clock event contributes only the affine offset row needed to align that event in the chosen gauge. It does not add a hidden distance row for the other clock. Without signal rows, a one-meeting pair remains rank-deficient.

The nonlinear null residuals are reported only for a linearly consistent static fit with no remaining nullspace. Rank-deficient records report rank and degeneracy labels without using an arbitrary particular solution to manufacture a null-residual verdict.

### 11.5 Rank And Nullspace Report

Every executable reconstruction must return:

```text
variable_count
residual_count
rank
nullity
singular_values
tolerance
gauge_mode_count
non_gauge_nullity
degeneracy_labels
residual_norm
max_abs_residual
```

The non-gauge nullity is:

$$
d_{\mathrm{nonGauge}} = n_{\mathrm{variables}} - r - d_{\mathrm{gauge}}
$$

where $r$ is the numerical rank after the stated tolerance convention. If $d_{\mathrm{nonGauge}}>0$, the result is underdetermined even if the residual norm is zero.

### 11.6 Required Degeneracy Labels

The rank report must attach these labels when applicable:

- `insufficient-clocks`: fewer than the claimed embedding dimension requires, or no reference clock exists
- `missing-meetings`: clocks cannot be event-aligned where a future embedding claim explicitly requires alignment
- `missing-reciprocal-signals`: at least one directed clock pair is one-way where the relative separation or clock offset needs a two-way check
- `disconnected-component`: rank is reported per component and no cross-component geometry is claimed
- `calibration-ambiguity`: clock rate or global scale is chosen by convention rather than observed calibration
- `mirror-boost-ambiguity`: orientation or boost remains after the stated gauge convention
- `rank-deficient`: a non-gauge nullspace remains
- `noisy-inconsistency`: the residual norm exceeds the stated tolerance

These are diagnostic outputs, not implementation failures. The implementation-level `valid` label means the raw schema and graph validation succeeded; it can appear together with degeneracy labels such as `rank-deficient` or `calibration-ambiguity`.

### 11.7 Well-Conditioned Synthetic Slice

In the well-conditioned $1+1$ dimensional synthetic slice, a valid result may recover:

- per-clock event order
- meeting-event representatives
- component-level partial order
- calibrated affine clock parameters
- a flat inertial clock embedding up to the stated Poincare, scale, and reflection gauge
- future-directed null-signal satisfaction for determined static fits
- full rank after gauge removal for the claimed variables

It still does not recover:

- a general Lorentzian metric
- a smooth event manifold outside the finite synthetic graph
- arbitrary null cones
- curvature
- a unique coordinate frame
- generator coordinates as observables

If the record is sparse, disconnected, weakly calibrated, or one-way only, the correct result is a rank or degeneracy diagnostic rather than a reconstruction theorem.

---

## 12. Adversarial Circularity And Artifact Review

This review checks the H2S1 result as implemented by `raw_record_reconstruction.py` and `test_raw_record_reconstruction.py`. It is intentionally severe.

| Check | Risk | H2S1 control | Classification |
| --- | --- | --- | --- |
| Hidden event-manifold input | The solver might start from event coordinates while claiming raw reconstruction. | The observed `RawEventRecord` stores clock IDs, local event IDs, pulse counts, signal endpoints, and meetings. Synthetic coordinates are only in `SyntheticRawCase.truth_events`, and reconstruction accepts `RawEventRecord`. | diagnostic tool |
| Hidden coordinate leakage from synthetic data | Generator truth could be consumed by the fit. | The non-leakage test tampers with truth sidecar coordinates and gets the same reconstruction. Consumed fields exclude `t`, `x`, and `truth_event_id`. | diagnostic tool |
| Null-cone circularity | Null constraints could assume the full null cone before reconstruction. | The solver uses only endpoint incidence and pulse-derived affine parameters. The null residual is a synthetic $1+1$ dimensional fit residual, not a supplied cone field. | conditional derivation |
| Calibration smuggling | Meeting records could be treated as equality of clock times. | The appendix and code treat meetings as event identity only. Clock rate and origin are separate affine variables or supplied calibration. | diagnostic tool |
| Label-order artifacts | Event labels could determine ordering instead of observed local order. | Ordering is recovered from `local_sequence_index` and checked against monotone `pulse_count`; duplicate or nonmonotone records are rejected. | diagnostic tool |
| Insufficient graph richness | Sparse records might be overclaimed as reconstructions. | One-way or sparse records return rank deficiency and `missing-reciprocal-signals` or `disconnected-component` labels. | clean no-go |
| Gauge fixing mistaken as observable structure | The chosen reference clock, origin, and orientation could be presented as physical. | The embedding is explicitly gauge-fixed. Output coordinates are fit diagnostics, while labels and rank report expose remaining nullspace. | diagnostic tool |
| Noisy inconsistency | Inconsistent records could be fitted by convention. | Signal pulse mismatches, meeting conflicts, order cycles, and nonzero residuals beyond tolerance are rejected or labeled `noisy-inconsistency`. | clean no-go |
| Overextension from $1+1$ dimensional flat tests to general Lorentzian H2 | A successful static synthetic case could be overstated as general metric reconstruction. | The appendix states that the slice does not recover a general Lorentzian metric, smooth event manifold, arbitrary null cones, or curvature. | blocked |

### 12.1 Surviving Claims

The surviving claims are narrow:

- **Raw schema validation:** diagnostic tool. The code checks that clock, event, signal, and meeting records are internally well formed.
- **Event-order recovery:** diagnostic tool. Local order is recoverable from local sequence and pulse monotonicity, not from event labels.
- **Meeting merge:** diagnostic tool. Meeting records recover event representatives, not clock-time equality or coordinates.
- **Static reciprocal signal embedding:** conditional derivation. In the calibrated static $1+1$ dimensional slice, reciprocal light links recover a gauge-fixed clock offset and separation for the stated variables.
- **Rank and nullspace report:** diagnostic tool. The report identifies whether the finite constraint system is full rank after the stated gauge convention.
- **Sparse record outcome:** clean no-go. One-way, disconnected, or weakly calibrated records do not support a reconstruction claim.

No H2S1 result here is a new prediction or controlled modification. The useful output is a diagnostic reduction of H2 circularity for a controlled finite synthetic problem.

---

## 13. Final Verdict

**Project-rule classification:** diagnostic tool.

H2S1 reduces a real circularity in H2 by replacing some fixed-event assumptions with an executable raw event-graph diagnostic. It does not prove general metric reconstruction from arbitrary raw pulse records.

### 13.1 Accepted Inputs

The accepted H2S1 input layer is:

- clock IDs
- local ordered pulse counts
- calibrated clock frequencies when explicitly supplied
- emission pulse counts
- reception pulse counts
- signal IDs linking one emission event to one reception event
- meeting IDs and meeting equality groups
- optional uncertainty, provenance, and artifact flags

The synthetic generator may hold internal $1+1$ dimensional Minkowski coordinates, but those coordinates are ground-truth sidecar data only.

### 13.2 Recovered Structure

The completed H2S1 slice recovers or reports:

- per-clock event order
- meeting-event representatives
- component-level partial order from local clock order and signal incidence
- affine clock parameters up to calibration and origin gauge
- a gauge-fixed static $1+1$ dimensional reciprocal-signal embedding for the implemented synthetic slice
- future-directed null-signal residual satisfaction for determined static fits in that slice
- rank, nullspace, residual, and degeneracy diagnostics for sparse or weak records

### 13.3 Unresolved Degeneracies

The following remain unresolved or intentionally reported as degeneracies:

- disconnected components
- insufficient clocks
- missing meetings where event alignment is required
- missing reciprocal signals where separation or offset needs a two-way check
- calibration ambiguity
- mirror, boost, and orientation gauge
- non-gauge rank deficiency in sparse records
- noisy inconsistency beyond stated tolerance

### 13.4 Rejected Overclaims

H2S1 rejects these claims:

- arbitrary sparse raw records determine a Lorentzian metric
- the synthetic coordinate sidecar is an observed event manifold
- meeting records imply equality of clock times
- the implemented static $1+1$ dimensional slice reconstructs general curvature
- null-signal endpoint incidence supplies a full null cone
- gauge-fixed coordinates are observables
- H2S1 supplies new external physics or a controlled modification of GR

### 13.5 Allowed Downstream Uses

Downstream work may use H2S1 as:

- a raw-record schema and validation contract
- a meeting-merge and event-order recovery diagnostic
- a finite graph rank and degeneracy report
- a non-leakage test pattern for synthetic generators
- a guardrail before promoting raw records into fixed-event H2 assumptions
- a starting point for richer finite-schema Jacobian and covariance work

### 13.6 Prohibited Downstream Uses

Downstream work must not use H2S1 as:

- proof that H2 is solved for arbitrary finite records
- proof of a smooth event manifold
- proof of a general Lorentzian metric
- proof of curvature or Einstein-Hilbert dynamics
- a replacement for H2 fixed-event richness assumptions
- a source of new predictions

### 13.7 Remaining Assumptions

The diagnostic still assumes:

- calibrated frequencies where the embedding scale is claimed
- correct signal IDs and meeting IDs
- monotone clock-local pulse order
- a controlled flat $1+1$ dimensional synthetic arena for the executable embedding slice
- a stated gauge convention for coordinate comparison
- residual tolerances appropriate to the record's uncertainty model

### 13.8 Verification Commands

The completed implementation was checked with:

```bash
uv run python -m unittest tests.test_raw_record_reconstruction
uv run python -m unittest tests.test_h2_reconstruction
uv run python -m unittest discover -s tests
uv run python -m compileall src tests/test_raw_record_reconstruction.py
```

---

## 14. Gauge Freedoms

H2S1 must preserve genuine gauge freedom instead of mistaking it for recovered physics.

Gauge freedoms include:

- clock ID and event label relabeling
- signal ID relabeling
- meeting ID relabeling
- local pulse-origin offsets
- affine clock calibration where calibration is not supplied
- event representative choices after meeting merges
- $1+1$ dimensional translation, boost, and reflection in synthetic embeddings
- global time and length scale where calibration does not fix it
- ordering choices inside disconnected components

The reconstruction result should report gauge-fixed choices separately from invariant or observable structure.

---

## 15. Failure And Degeneracy Labels

Every finite result must report applicable labels from this list:

- `valid`: the raw schema and graph validation succeeded; this can coexist with degeneracy labels
- `invalid-record`: a required record field is missing or contradictory
- `duplicate-signal`: a signal ID maps to more than one emission or reception
- `meeting-conflict`: meeting records force incompatible event identities
- `event-order-conflict`: pulse counts or sequence indexes violate local order
- `disconnected-component`: a component is not linked to the rest of the graph
- `insufficient-clocks`: too few clock chains exist for the claimed embedding
- `missing-meetings`: clock chains lack coincidence records needed to align them
- `missing-reciprocal-signals`: at least one signal pair is one-way where two-way constraints are required
- `calibration-ambiguity`: clock-rate or scale freedom remains unresolved
- `mirror-boost-ambiguity`: the synthetic embedding is recoverable only up to orientation and boost
- `rank-deficient`: the linearized constraint system has a non-gauge nullspace
- `noisy-inconsistency`: residuals exceed stated tolerance or uncertainty
- `hidden-geometry-leak`: solver inputs contain coordinates, null directions, or metric data

A failure label is not necessarily a physics failure. Often it is the correct conclusion that the raw record is underdetermined.

---

## 16. Result Labels

The final H2S1 verdict must use exactly one project-rule classification:

- known-physics reformulation
- diagnostic tool
- conditional derivation
- new prediction
- controlled modification
- clean no-go

Intermediate claims may also be marked:

- `artifact`
- `blocked`
- `underdetermined`
- `validated-synthetic-slice`

Those intermediate labels do not replace the final project-rule classification.

---

## 17. Ordered Task Sequence

The H2S1 work proceeds in this order:

1. Define raw reconstruction scope, appendix contract, and no-geometry boundary.
2. Define raw pulse, signal, and meeting-event schema.
3. Specify the $1+1$ dimensional Minkowski synthetic generator from raw records.
4. Derive event ordering and clock embedding constraints.
5. Derive null-signal constraints, rank tests, and degeneracy labels.
6. Implement raw record reconstruction helpers and focused tests.
7. Run adversarial circularity and artifact review.
8. Write the final raw H2 strengthening verdict and update roadmap files only after the coordinated roadmap blocker is closed.

The sequence is intentionally conservative. Later steps may add detail to this appendix, but they must keep the no-geometry boundary intact.
