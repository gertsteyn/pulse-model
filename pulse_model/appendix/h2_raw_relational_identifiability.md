# Appendix: H2 Raw Relational Event and Signal Identifiability

**Parent hypothesis:** 6.2 Hypothesis H2: The metric is reconstructed from pulse comparisons  
**Status:** Conditional sufficient-conditions theorem  
**Purpose:** State conditions under which raw relational pulse records admit a smooth fixed-event realization and recover clock embeddings plus proof-grade signal directions or conformal data without assuming the metric being reconstructed.

---

## 1. Scope

The H2 fixed-event theorem assumes:

- a smooth event region $U$
- an incidence map from relational events into $U$
- embedded clock-chain segments
- proof-grade local signal directions or infinitesimal signal curves

This appendix states when those inputs can be justified from raw relational records.

It does not claim that every finite record has a unique smooth realization. Sparse records, noisy records, records with caustics, and records with topology ambiguity can remain underdetermined.

---

## 2. Raw Relational Record

A raw relational record is an event graph:

$$
\mathcal{G} = (E,C,S,M,R)
$$

where:

- $E$ is a finite or dense-limit set of event labels
- $C$ is the set of ordered clock chains
- $S$ is the set of signal links from emission events to reception events
- $M$ is the set of meeting or coincidence identifications
- $R$ is the set of local readings attached to events

The local readings include pulse counts, calibration labels, optional phase records, optional local direction records, and optional acceleration records.

The raw record does not contain coordinates, coordinate time, metric components, or a preferred frame.

---

## 3. Sufficient Conditions

Raw-relational identifiability requires more than graph connectivity. The following conditions are sufficient for the H2 fixed-event inputs.

### 3.1 Manifold-Likeness

The event graph must admit neighborhoods whose incidence and signal-order structure converge to a four-dimensional smooth topology.

Operationally:

- local neighborhoods have stable dimension four in the dense limit
- event neighborhoods separate points
- the limiting topology is Hausdorff and second countable
- overlapping local neighborhoods have smooth transition maps
- clock and signal incidence does not force branching event identities

This condition is not automatic. It is the main raw-relational assumption.

### 3.2 Clock Atlas Richness

Clock chains must be rich enough to act as local probes of timelike structure.

Required:

- ordered clock events converge to smooth one-dimensional embedded curves
- meeting events identify clock intersections consistently
- calibrated pulse counts give monotone local parameters along each clock
- clocks sample every target neighborhood densely enough for the intended theorem
- clock species satisfy the universality assumption after calibration

The clock chains need not define coordinates by themselves. They only need to supply smooth embedded timelike probes and operational durations.

### 3.3 Signal Incidence Richness

Signal links must be rich enough to identify local null structure.

Required:

- emission and reception labels are correct
- signal links are local or decomposable into locally controlled segments
- there is no unresolved multipath ambiguity in the target region
- local signal families approach every projective null direction in the dense limit
- optional phase or direction records are attached to local instrument frames rather than global coordinates

In the strongest case, local direction records directly supply the projective signal directions needed by the fixed-event theorem.

In the weaker dense-link case, infinitesimal signal links recover projective directions as limiting event separations after the manifold structure has been identified.

### 3.4 Causal Regularity

The target region must be causally regular enough that signal incidence separates nearby events.

Sufficient restrictions:

- no closed causal curves in the target region
- no unresolved caustics for the signal links used in reconstruction
- no horizons or boundaries that identify external comparison records ambiguously
- local signal neighborhoods are convex enough that nearby signal links have unique local tangent directions

These restrictions can be weakened later, but they are appropriate for the first raw-identifiability theorem.

### 3.5 Calibration And Nuisance Control

The event graph must include enough calibration and nuisance information to avoid fake geometry.

Required:

- clock frequencies and uncertainties are recorded
- readout delays are bounded or estimated
- environmental shifts are bounded or estimated
- local direction-frame calibrations are bounded or estimated
- acceleration records separate clock transport effects from metric effects when needed
- phase-wrap and signal-label ambiguities are resolved or modeled

Without this control, several non-geometric explanations can fit the same raw record.

---

## 4. Conditional Identifiability Theorem

Consider a sequence of raw relational records:

$$
\mathcal{G}_n = (E_n,C_n,S_n,M_n,R_n)
$$

with increasing clock and signal density and decreasing measurement uncertainty.

Assume:

- the manifold-likeness condition holds
- clock atlas richness holds
- signal incidence richness holds
- causal regularity holds
- calibration and nuisance variables converge or remain bounded

Then there exists a smooth four-dimensional event region $U$ and incidence maps:

$$
\iota_n:E_n\to U
$$

such that, in the dense limit:

- meeting records converge to shared events in $U$
- clock chains converge to embedded clock curves
- pulse-count differences converge to operational durations along those curves
- local signal direction records or infinitesimal signal families converge to projective null-direction data
- any second smooth realization satisfying the same limiting incidence, clock, and signal-direction structure is related by an incidence-preserving diffeomorphism

Therefore the raw relational record supplies the fixed-event inputs needed by the H2 ideal theorem, up to diffeomorphism.

This theorem is conditional. The assumptions do the work. The theorem says what must be checked before raw records are promoted to a fixed-event realization.

---

## 5. Why The Diffeomorphism Is The Right Ambiguity

Event labels are arbitrary. If two smooth realizations preserve:

- event incidence
- clock order
- clock meetings
- pulse-count durations
- signal-link incidence
- limiting signal directions or conformal data

then the only remaining smooth ambiguity is relabeling the event region by a diffeomorphism.

The physical object is not a coordinate map:

$$
x^\mu(e)
$$

The physical target is the event structure and metric class:

$$
[g_{\mu\nu}]
$$

after the fixed-event H2 theorem is applied.

---

## 6. Recovering Signal Directions

There are two acceptable routes.

### 6.1 Direct Local Direction Records

If local apparatus records emission or reception direction in a calibrated local frame, then the raw record supplies projective signal directions after frame calibration.

The direction is local. It is not a global coordinate vector.

### 6.2 Dense Infinitesimal Signal Families

If direct direction records are absent, dense infinitesimal signal links can recover directions after the event manifold has been identified.

In a recovered local chart, take signal endpoints $p_n$ and $q_n$ with:

$$
\iota(q_n)\to \iota(p_n)
$$

The projective tangent direction is the limit of the endpoint separation direction:

$$
[k] = \lim_{n\to\infty} [\iota(q_n)-\iota(p_n)]
$$

This limit must be independent of chart choice up to the usual tangent-vector transformation. If it is not, the record has not supplied proof-grade signal direction data.

### 6.3 Conformal Data Route

A stronger dense signal record may determine the local causal cone directly from which events are connected by infinitesimal signals.

In that case the raw record supplies conformal metric data rather than individual tangent samples. The conformal factor still requires calibrated timelike clock durations.

---

## 7. Gauge Freedoms

Raw-relational identifiability must not remove genuine gauge freedom.

Gauge freedoms include:

- event-label renaming
- smooth diffeomorphism of the recovered event region
- clock pulse-origin offsets
- smooth reparameterization of clock chains compatible with pulse counts
- local frame rotations or boosts in direction-record instrumentation
- signal phase-wrap choices
- additive potential convention in weak-static finite fits
- ansatz parameter degeneracies in sparse reconstructions

A raw-identifiability claim succeeds only after separating these gauge freedoms from physical structure.

---

## 8. Failure Modes

Raw-relational event and signal identifiability can fail in precise ways:

- Sparse clock networks do not determine a smooth event region.
- Sparse signal links do not determine local null cones.
- Caustics or multipath signals make endpoint links ambiguous.
- Topology ambiguity lets different event regions explain the same incidence graph.
- Horizons or boundaries can make external comparison records incomplete.
- Clock nonuniversality prevents a single metric scale.
- Unmodeled clock drift mimics $g_{00}$ variation.
- Unmodeled signal delay mimics spatial curvature.
- Unmodeled acceleration or support forces mimic geometric effects.
- Phase-wrap ambiguity changes inferred frequency or path residuals.
- Local direction frames without calibration do not define projective tangent data.

These failures do not refute fixed-event H2. They block promotion of raw records into the fixed-event theorem.

---

## 9. Relation To H2 Acceptance

This appendix strengthens the H2 story by naming sufficient raw-relational conditions. It does not change the H2 gate decision by itself.

H2 remains:

- accepted for ideal fixed-event metric uniqueness
- partially accepted for restricted finite-data prototype slices
- conditional for raw-relational event and signal identifiability

Future practical work should turn the sufficient conditions above into explicit algorithms and tests for finite event graphs.
