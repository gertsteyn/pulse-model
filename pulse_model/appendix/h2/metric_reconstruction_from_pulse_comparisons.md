---
title: H2 Metric Reconstruction From Pulse Comparisons
sidebar_label: Fixed-Event Theorem
sidebar_position: 2
---

# Appendix: Conditional Proof of H2 Metric Reconstruction

**Parent hypothesis:** 6.2 Hypothesis H2: The metric is reconstructed from pulse comparisons  
**Status:** Reviewed conditional proof / ideal fixed-event theorem  
**Purpose:** Prove the ideal dense-data version of H2, state the assumptions needed for the proof, and identify what remains for finite experimental reconstruction.

---

## 0. Review findings

This review checks the appendix as the ideal fixed-event H2 theorem, not as the full finite-data or raw-relational reconstruction theorem.

Findings:

- The fixed-event theorem is internally coherent when its scope is kept narrow: $U$, the incidence map, clock embeddings, and proof-grade signal directions are inputs.
- Null-richness is strong but sufficient for the theorem: sampled projective signal directions must be dense in the null cone of one compatible metric. Compatibility of any second metric then forces the same cone and hence the same conformal metric class.
- Clock-richness is strong but sufficient for the theorem: positive-duration timelike clock segments must occur inside arbitrarily small neighborhoods. Sparse clocks cannot fix an arbitrary conformal factor.
- Event-manifold identification is not proved here. It is an external assumption used only in the diffeomorphism corollary.
- Circularity is avoided only if pulse counts, transition-frequency calibration, and clock universality are treated as operational inputs, not as quantities inferred from the reconstructed metric.
- The raw-relational proof obligation is addressed conditionally in `h2_raw_relational_identifiability.md`.

Review verdict: this appendix can serve as the internally checked ideal fixed-event theorem for H2. It does not yet accept practical H2.

---

## 1. Claim to prove

H2 should not be read as a claim that one can reconstruct a preferred coordinate expression for the metric. Coordinates are gauge. The correct target is the metric equivalence class under diffeomorphisms:

$$
\mathcal{D}_{\mathrm{pulse}} \Rightarrow [g_{\mu\nu}]
$$

where $\mathcal{D}_{\mathrm{pulse}}$ is the full relational record of ideal clocks and exchanged signals.

The ideal fixed-event H2 proof target is:

> Given a sufficiently rich, ideal, dense network of pulse counters and signal exchanges, and given a fixed-event realization consisting of a smooth event region, incidence map, embedded clock segments, and signal tangent directions or infinitesimal signal curves, the pulse record determines a unique Lorentzian metric. Between two smooth realizations, the result is unique up to diffeomorphism once those fixed-event data are identified.

Equivalently, on a fixed-event realization:

> If two Lorentzian metrics explain all proof-grade ideal pulse-count and signal-direction records on the same fixed-event realization, then they are equal. For two different smooth realizations, they are equivalent after the independently supplied event-identifying diffeomorphism.

This is the precise version of the informal statement:

$$
g_{\mu\nu} = \arg\min_g \mathcal{E}[g;\mathrm{pulse\ records}]
$$

The rigorous fixed-event version should instead be:

$$
\hat{[g]} = \arg\min_{[g]} \mathcal{E}([g];\mathcal{D}_{\mathrm{pulse}})
$$

The full relational H2 target remains broader because it must also recover the smooth event representation and proof-grade signal directions from raw relational records.

---

## 2. Why this is plausible

A Lorentzian metric has two operational parts:

1. The null cone structure, which determines which directions light signals can follow.
2. The proper-time scale, which determines how much ideal clock time accumulates along timelike paths.

Signal exchanges can determine the null cone structure. Ideal pulse counters can determine operational durations that any metric realization must match as metric proper times. Together, they should determine the metric.

In geometric language:

- causal and null relations determine the conformal metric class
- timelike clock durations fix the conformal factor
- the remaining ambiguity is coordinate gauge

This is the key proof strategy.

---

## 3. Required assumptions

The proof needs explicit assumptions. Without them, H2 is too strong.

### 3.1 Geometric assumptions

Work in a spacetime region $U$ satisfying:

- $U$ is a connected smooth four-dimensional manifold region.
- $U$ carries a smooth Lorentzian metric $g_{\mu\nu}$ with signature $(-,+,+,+)$.
- $U$ is time-orientable.
- The observed signal paths are governed by the same null structure as $g_{\mu\nu}$.
- Recorded signal directions can be assigned unambiguously to the events where they are emitted or received.

For a first proof, a convex normal neighborhood is sufficient because it avoids caustic and topology ambiguity in the signal data. This is stronger than the fixed-event uniqueness proof itself needs, but it is a clean domain for relating raw signal records to local tangent directions. Later proofs can relax this.

### 3.2 Clock assumptions

Each clock is ideal after calibration. The operational duration is:

$$
dT_A = \frac{dN_A}{f_A}
$$

where $A$ labels the clock and $f_A$ is its known local transition frequency.

A compatible metric must reproduce this operational duration as metric proper time along the clock worldline:

$$
dT_A=d\tau_g
$$

This assumes:

- no clock-species violation
- known transition frequencies
- controlled environmental shifts
- count records with arbitrarily small measurement error in the ideal limit

The transition frequency $f_A$ is an operational calibration input. The theorem does not derive it from $g_{\mu\nu}$.

Nonideal clocks can be added later as nuisance models, but the core theorem should start with ideal clocks.

### 3.3 Signal assumptions

Signals used for reconstruction satisfy:

- signal emission and reception events are recorded by local pulse counts
- signal propagation follows null curves of the metric
- signal labels identify which emission event corresponds to which reception event
- local emitted and received frequencies or phases can be recorded when redshift information is needed

Finite-data reconstruction can start with event matching and null propagation. The ideal proof-grade theorem additionally requires local signal tangent directions, either directly recorded or recovered from dense infinitesimal signal families. Signal phase and redshift can then strengthen finite-data reconstruction.

Those local signal directions must not be inferred by first reconstructing the metric. They are part of the fixed-event data, or they must be obtained from a separate raw-relational limit theorem.

### 3.4 Network richness assumptions

The network must be sufficiently rich. For the fixed-event uniqueness theorem, the required richness is:

- sampled projective signal directions are dense in every local null cone of one compatible metric
- positive-duration timelike clock segments occur inside arbitrarily small neighborhoods
- calibrated clocks obey a universal operational duration scale

For the broader relational problem, additional richness is needed:

- clock worldlines pass through a dense enough set of events in $U$
- signal exchanges supply enough incidence data to identify event neighborhoods
- meeting events or two-way signaling provide relational event identification

Sparse clock networks reconstruct only a finite approximation or a restricted metric ansatz.

---

## 4. Proof-level data model

The primitive data should be relational, not coordinate-based. This section is the proof-level data model. The finite-data schema is defined in `h2_finite_pulse_record_schema.md`.

For each clock $A$:

- clock identifier $A$
- transition type $i_A$
- calibrated transition frequency $f_A$
- ordered local pulse counts $N_A(k)$
- local acceleration record $a_A(k)$ when available
- emitted signal records
- received signal records
- clock-meeting records with other clocks

For each signal $s$:

- emitting clock $A$
- emission pulse count $N_A(e_s)$
- receiving clock $B$
- reception pulse count $N_B(r_s)$
- signal identifier linking emission to reception
- optional emitted phase
- optional received phase
- local emission and reception direction, or enough neighboring infinitesimal signal links to recover it, for proof-grade records

The raw data are not coordinates. They are event incidences, clock orderings, pulse intervals, and signal links.

---

## 5. Observable primitives

The proof should reduce all records to four operational primitives.

### 5.1 Timelike pulse duration

For two events $p$ and $q$ on clock $A$:

$$
\Delta T_A(p,q) = \frac{N_A(q)-N_A(p)}{f_A}
$$

This is the measured operational duration along that clock segment. A compatible metric must reproduce it as the segment's proper time.

### 5.2 Null signal relation

For a signal emitted at $p$ and received at $q$, the record asserts that $p$ and $q$ are connected by a future-directed null signal path.

For the proof-grade ideal theorem, the record must also determine local signal tangent directions. This can happen either because directions are recorded directly by local frames, or because the dense infinitesimal signal family determines the tangent directions in the limit.

In a candidate metric, the signal curve $y_s$ must satisfy:

$$
g_{\mu\nu}(y_s)\dot y_s^\mu \dot y_s^\nu = 0
$$

and, for freely propagating light in the geometric-optics limit, $y_s$ should also be a null geodesic.

### 5.3 Frequency comparison

If emitted and received signal phases are recorded, the candidate metric predicts a frequency ratio:

$$
\frac{\nu_{\mathrm{recv}}}{\nu_{\mathrm{emit}}} = \frac{(k_\mu u^\mu)_{\mathrm{recv}}}{(k_\mu u^\mu)_{\mathrm{emit}}}
$$

where $u^\mu$ is the clock four-velocity and $k^\mu$ is the signal wave vector.

This observable helps constrain redshift and the relative motion of clocks.

### 5.4 Local acceleration

A non-geodesic clock has proper acceleration:

$$
a^\mu = u^\nu\nabla_\nu u^\mu
$$

Acceleration records help separate actual metric structure from thrust, support forces, and clock-network motion. They are especially useful in finite-data reconstruction.

---

## 6. Reconstruction map

There are two reconstruction problems.

The proof below uses the **fixed-event problem**. In that problem, the smooth event region $U$, embedded clock segments $\gamma_A$, and signal tangent directions $k_s$ are already fixed. A candidate metric $g$ predicts the proof-critical records:

$$
\mathcal{P}_{\mathrm{proof}}(g) = \{\tau_g[\gamma_A],g(k_s,k_s)\}
$$

Redshift predictions $z_g$ and proper-acceleration predictions $a_g$ are auxiliary terms for practical reconstruction. They are not used in the theorem.

The fixed-event reconstruction problem minimizes over smooth metrics on the already fixed region and embeddings:

$$
\hat g = \arg\min_g \mathcal{E}(g;\mathcal{D}_{\mathrm{pulse}})
$$

The full relational reconstruction problem is broader. It must also infer the smooth event representation, clock embeddings $X_A$, and signal curves or directions $Y_s$. Only then can it minimize over metric equivalence classes:

$$
\hat{[g]} = \arg\min_{[g],X,Y,\chi} \mathcal{E}(\mathcal{P}([g],X,Y),\mathcal{D}_{\mathrm{pulse}},\chi)
$$

Here $\mathcal{P}([g],X,Y)$ denotes the full-record prediction map: it predicts clock operational-duration matches, signal nullness, event incidences, and any auxiliary redshift or acceleration records for the chosen metric class and embeddings.

The nuisance variables $\chi$ collect clock calibration uncertainties, environmental shifts, finite timing errors, and incomplete signal-path information.

For the fixed-event ideal theorem, take the zero-noise, dense-data limit, remove $\chi$, and hold $U$, $\gamma_A$, and $k_s$ fixed.

The residual should include:

$$
\mathcal{E} = w_\tau\mathcal{E}_\tau + w_{\mathrm{null}}\mathcal{E}_{\mathrm{null}} + w_z\mathcal{E}_z + w_a\mathcal{E}_a + w_{\mathrm{smooth}}\mathcal{E}_{\mathrm{smooth}}
$$

where:

- $\mathcal{E}_\tau$ compares predicted metric proper times with observed operational durations
- $\mathcal{E}_{\mathrm{null}}$ enforces signal nullness and event linkage
- $\mathcal{E}_z$ compares predicted and observed redshifts
- $\mathcal{E}_a$ compares predicted and observed proper accelerations
- $\mathcal{E}_{\mathrm{smooth}}$ regularizes finite-data fits toward smooth metrics

The ideal proof should not depend on the arbitrary weights. The weights are for practical reconstruction.

---

## 7. Formal proof

This section proves the ideal local form of H2. It is a conditional proof: if the pulse record is ideal, dense, calibrated, and rich enough to define local light cones and timelike clock scales, then the metric is determined.

The core theorem is a fixed-event-manifold theorem: once the relational event structure has been represented as a smooth region $U$, the pulse record determines the metric on $U$. The diffeomorphism statement is then a corollary, and it depends on a separate event-manifold identification result.

This proof does not prove that a sparse experimental network uniquely reconstructs an arbitrary metric. Sparse and noisy reconstruction is an inverse problem handled later by algorithms and stability estimates.

### 7.1 Definitions

An **ideal pulse record** $\mathcal{D}_{\mathrm{pulse}}$ consists of:

- a relational event set $E$
- ordered clock-event chains $C_A \subset E$
- signal links $s:p_s\to q_s$ between emission and reception events
- pulse counts $N_A(p)$ along each clock chain
- calibrated transition frequencies $f_A$
- clock-meeting identifications
- optional acceleration and phase records

For clock events $p,q$ on clock $A$, define the operational duration:

$$
\Delta T_A(p,q)=\frac{N_A(q)-N_A(p)}{f_A}
$$

This is a physical reading: count difference divided by calibrated transition frequency. It is not yet a metric proper time.

**Clock universality** means that all ideal calibrated clock species reduce to the same operational duration scale. If two ideal clocks traverse the same physical infinitesimal segment, then:

$$
\frac{dN_A}{f_A}=\frac{dN_B}{f_B}
$$

If this fails, H2 fails in its single-metric form.

The record is **fixed-event realized** when there are:

- a smooth region $U$
- an incidence-preserving map from $E$ into $U$
- embedded clock-chain segments $\gamma_A[p,q]$ in $U$
- recorded signal tangent directions or infinitesimal signal curves in $TU$

These objects are inputs to the fixed-event theorem. Deriving them from raw relational records is a separate reconstruction problem.

A Lorentzian metric $g$ is **compatible** with this fixed-event realization when each clock segment is timelike for $g$ and each clock interval satisfies:

$$
\Delta T_A(p,q) = \int_{\gamma_A[p,q]} d\tau_g
$$

and each recorded signal direction $k_s$ satisfies:

$$
g_{\mu\nu}k_s^\mu k_s^\nu = 0
$$

If the record stores infinitesimal signal curves instead of directions, $k_s$ is the corresponding tangent direction.

The record is **null-rich relative to $g$** when, for every event $p$ and every nonzero $g$-null vector $v\in T_pU$, the recorded signal directions contain a sequence converging to the projective direction of $v$ in any local smooth trivialization.

The record is **clock-rich** when, for every event $p$ and every neighborhood $V$ of $p$, there is a sampled timelike clock segment with positive operational duration contained entirely in $V$.

The record is **event-manifold identifiable** when two smooth realizations of the same relational event set determine a smooth incidence-preserving diffeomorphism between their realized regions.

Event-manifold identifiability is not used in the fixed-event theorem. It is only used later to restate the result up to diffeomorphism.

These richness assumptions are strong. They are the price of a clean uniqueness theorem.

### 7.2 Fixed-event theorem

Let $U$ be a connected smooth region carrying a fixed-event ideal pulse record $\mathcal{D}_{\mathrm{pulse}}$.

Let $g$ be a compatible smooth Lorentzian metric on $U$ with signature $(-,+,+,+)$. Let $h$ be another smooth Lorentzian metric on $U$ with the same signature. Suppose:

- $h$ is also compatible with $\mathcal{D}_{\mathrm{pulse}}$
- clock universality holds
- $\mathcal{D}_{\mathrm{pulse}}$ is null-rich relative to $g$
- $\mathcal{D}_{\mathrm{pulse}}$ is clock-rich

Then:

$$
g=h
$$

Therefore, once the event manifold, clock embeddings, and proof-grade signal directions are fixed, no second compatible Lorentzian metric exists.

### 7.3 Fixed-event proof overview

The proof has five steps.

1. Pulse counts determine operational durations.
2. Signal directions force the second metric to vanish on the first metric's null cone.
3. Vanishing on the same null cone forces conformal equivalence.
4. Clock durations fix the conformal factor.
5. Therefore the two fixed-event metrics are equal.

Each step is proven below.

### 7.4 Lemma 1: Pulse counts determine operational duration

For an ideal calibrated clock $A$, the pulse record determines the operational duration of any sampled segment of that clock:

$$
\Delta T_A(p,q) = \frac{N_A(q)-N_A(p)}{f_A}
$$

**Proof.**

The pulse record gives $N_A(p)$ and $N_A(q)$. Calibration gives $f_A$. Since $f_A$ is known and nonzero, the ratio:

$$
\Delta T_A(p,q) = \frac{N_A(q)-N_A(p)}{f_A}
$$

is directly determined. This uses only pulse count and clock calibration. It does not assume a prior metric reconstruction. QED.

### 7.5 Lemma 2: Signal data constrain the null cone

Let $g$ and $h$ be compatible with the same fixed-event signal record. If the record is null-rich relative to $g$, then every $g$-null vector is also $h$-null:

$$
g_p(v,v)=0 \Rightarrow h_p(v,v)=0
$$

**Proof.**

By compatibility, every recorded signal direction is null for $h$.

Let $v\in T_pU$ be nonzero and $g$-null:

$$
g_p(v,v)=0
$$

By null-richness relative to $g$, there is a sequence of recorded signal directions converging to the projective direction of $v$ in a local smooth trivialization. Each direction in the sequence is $h$-null. Since $h$ is smooth, the function:

$$
w\mapsto h(w,w)
$$

is continuous on tangent vectors. Therefore the limit direction $v$ is also $h$-null:

$$
h_p(v,v)=0
$$

QED.

### 7.6 Lemma 3: Null-cone vanishing implies conformal metrics

Let $g_p$ and $h_p$ be Lorentzian inner products on a four-dimensional tangent space $T_pU$, both with signature $(-,+,+,+)$. If every $g_p$-null vector is also $h_p$-null, then:

$$
h_p = \Omega(p)^2 g_p
$$

for some positive scalar $\Omega(p)$.

**Proof.**

Choose a $g_p$-orthonormal basis, so:

$$
g_p(v,v) = -(v^0)^2 + (v^1)^2 + (v^2)^2 + (v^3)^2
$$

Write the components of $h_p$ in this basis as $H_{\mu\nu}$.

Every $g_p$-null vector of the form:

$$
v=(1,n^1,n^2,n^3)
$$

with:

$$
(n^1)^2+(n^2)^2+(n^3)^2=1
$$

is also $h_p$-null by hypothesis. Therefore:

$$
H_{00}+2H_{0i}n^i+H_{ij}n^i n^j=0
$$

for every unit spatial vector $n$.

Replacing $n$ by $-n$ and subtracting gives:

$$
4H_{0i}n^i=0
$$

for every unit $n$, so:

$$
H_{0i}=0
$$

The remaining condition is:

$$
H_{00}+H_{ij}n^i n^j=0
$$

for every unit $n$. Thus the quadratic form $H_{ij}n^i n^j$ is constant on the unit sphere. By the polarization identity, this implies:

$$
H_{ij}=\alpha\delta_{ij}
$$

for some scalar $\alpha$. Then:

$$
H_{00}=-\alpha
$$

So:

$$
h_p(v,v)=\alpha\left(-(v^0)^2+(v^1)^2+(v^2)^2+(v^3)^2\right)
$$

and therefore:

$$
h_p=\alpha g_p
$$

Because $h_p$ and $g_p$ have the same signature convention $(-,+,+,+)$, $\alpha$ is positive. Write $\alpha=\Omega(p)^2$. QED.

Applying this pointwise to the smooth metrics $g$ and $h$ gives:

$$
h=\Omega^2 g
$$

with smooth positive $\Omega$.

### 7.7 Lemma 4: Clock durations fix the conformal factor

Let $h=\Omega^2 g$ on a connected region $U$, with $\Omega>0$ smooth. If a clock-rich pulse record assigns the same operational duration to all sampled timelike clock segments for both metrics, then:

$$
\Omega=1
$$

throughout $U$.

**Proof.**

For any timelike curve segment $\gamma$, conformal rescaling changes the line element by:

$$
d\tau_h = \Omega d\tau_g
$$

Both metrics are compatible with the same operational pulse record, so each sampled clock segment has the same operational duration:

$$
\Delta T_\gamma = \int_\gamma d\tau_h = \int_\gamma d\tau_g
$$

Substituting $d\tau_h=\Omega d\tau_g$ gives:

$$
\int_\gamma \Omega d\tau_g = \int_\gamma d\tau_g
$$

so:

$$
\int_\gamma (\Omega-1)d\tau_g = 0
$$

Assume for contradiction that $\Omega(p_0)\neq 1$ at some point $p_0$. Since $\Omega$ is continuous, there is a neighborhood $V$ of $p_0$ where $\Omega-1$ has a definite nonzero sign.

By clock-richness, there are arbitrarily short sampled timelike clock segments contained in $V$. For any such segment:

$$
\int_\gamma (\Omega-1)d\tau_g
$$

has that same nonzero sign and cannot vanish. This contradicts the equality of pulse-derived durations.

Therefore $\Omega(p)=1$ for every $p$ in $U$. QED.

### 7.8 Proof of the fixed-event theorem

Let $g$ and $h$ be two compatible smooth Lorentzian metrics on the same fixed event region $U$.

By Lemma 2, every $g$-null vector is $h$-null.

By Lemma 3, there is a smooth positive function $\Omega$ such that:

$$
h=\Omega^2 g
$$

By Lemma 1, pulse counts determine operational durations along the sampled clocks.

By Lemma 4, equality of those pulse-derived durations on a clock-rich record forces:

$$
\Omega=1
$$

Therefore:

$$
h=g
$$

So the fixed-event metric is uniquely determined by the ideal pulse record. QED.

### 7.9 Diffeomorphism corollary

Suppose the same ideal pulse record has two spacetime realizations:

$$
(U,g)
$$

and:

$$
(\tilde U,\tilde g)
$$

Assume a separate event-manifold identification result supplies an incidence-preserving diffeomorphism:

$$
\phi:U\to\tilde U
$$

that maps the clock segments, signal directions, pulse records, and meeting events of the first realization to the corresponding objects of the second realization.

Then pull back the second metric:

$$
h=\phi^*\tilde g
$$

Assume this pullback preserves the fixed-event theorem hypotheses on $U$: $h$ is compatible with the pulled-back pulse record, clock universality holds, the record is clock-rich, and the signal directions are null-rich relative to $g$.

The fixed-event theorem then applies to $g$ and $h$ on $U$, so:

$$
g=h
$$

Therefore:

$$
g=\phi^*\tilde g
$$

So, once event-manifold identification is supplied independently, the ideal pulse record determines the metric equivalence class $[g_{\mu\nu}]$.

### 7.10 Corollary: Uniqueness of the zero-residual reconstruction

On a fixed event manifold in the ideal dense-data limit, suppose the residual functional satisfies:

$$
\mathcal{E}(g;\mathcal{D}_{\mathrm{pulse}})=0
$$

exactly when $g$ realizes all pulse durations and signal links in $\mathcal{D}_{\mathrm{pulse}}$.

Then the zero-residual minimizer is unique:

$$
\hat g=g
$$

**Proof.**

If two different fixed-event metrics had zero residual, they would both realize the same ideal pulse record. By the theorem, they would be equal. QED.

### 7.11 What has been proven

The proof establishes this precise H2 statement:

> In an ideal dense pulse-clock and proof-grade signal-direction network, calibrated pulse durations fix the timelike scale. If the signal direction records densely sample the null cone of a compatible metric, then no second compatible Lorentzian metric exists. The result is up to diffeomorphism once event-manifold identification is supplied.

More precisely, the proof establishes metric uniqueness on a fixed event manifold. The up-to-diffeomorphism statement follows only when an independent event-manifold identification result is available.

This is the reviewed H2 ideal-level result. It is strong enough to justify using a reconstructed metric object as the target of finite-data H2 work, but it is not strong enough to start H3 as if practical metric reconstruction were already accepted.

The proof does not yet establish:

- uniqueness for sparse finite networks
- stability under measurement noise
- reconstruction without clock calibration
- reconstruction when clock species violate universality
- reconstruction in regions with severe caustics, topology ambiguity, horizons, or closed timelike curves
- an algorithm that is numerically well-conditioned
- derivation of the smooth event manifold from the relational event set alone
- recovery of the incidence map, embedded clock curves, and signal tangent directions from raw relational records

Those are separate finite-data and physical-realizability problems.

---

## 8. Practical proof route by increasing difficulty

### Level 1: Minkowski reconstruction

Start with inertial and accelerated clocks in flat spacetime.

Show that pulse intervals and light signals recover:

$$
g_{\mu\nu} = \eta_{\mu\nu}
$$

up to Poincare transformations and arbitrary coordinate relabeling.

Acceptance condition:

> The reconstruction distinguishes inertial time dilation from acceleration history without inventing curvature.

### Level 2: Weak static field

Use a weak-field metric:

$$
g_{00} \approx -\left(1+\frac{2\Phi}{c^2}\right)
$$

Clock comparisons at different potentials should recover $\Phi$ up to an additive constant fixed by boundary convention.

Acceptance condition:

> Redshift and pulse-count ratios recover the known Newtonian potential difference.

### Level 3: Stationary field with frame dragging

Include off-diagonal components:

$$
g_{0i} \neq 0
$$

Use counter-propagating signal loops and Sagnac-type comparisons.

Acceptance condition:

> Direction-dependent signal timing recovers the gravitomagnetic part of the weak-field metric.

### Level 4: Spatial curvature and lensing

Use null signal paths plus clock baselines to recover spatial metric information, not just $g_{00}$.

Acceptance condition:

> The reconstruction recovers light-bending or Shapiro-delay data requiring spatial curvature.

### Level 5: Time-dependent perturbations

Fit weak gravitational-wave perturbations:

$$
g_{\mu\nu} = \eta_{\mu\nu}+h_{\mu\nu}
$$

Acceptance condition:

> Network pulse residuals recover injected $h_{\mu\nu}$ modes up to gauge.

### Level 6: General local theorem

Prove the ideal dense-data uniqueness theorem for a smooth Lorentzian region.

Acceptance condition:

> On a fixed event region, any two compatible metrics producing the same complete proof-grade ideal pulse record are equal. Across two smooth realizations, they are diffeomorphic after an independently supplied event-identifying map.

---

## 9. Avoiding circularity

The circularity risk is:

1. Define pulse count using proper time.
2. Define proper time using the metric.
3. Define the metric using pulse count.

The proof must avoid this by separating physical readings from geometric reconstruction.

Operational input:

$$
\Delta N
$$

Calibration input:

$$
f
$$

Derived operational duration:

$$
\Delta T_{\mathrm{op}} = \Delta N/f
$$

Reconstructed object:

$$
[g_{\mu\nu}]
$$

The metric is then the object whose timelike lengths reproduce $\Delta T_{\mathrm{op}}$ and whose null curves reproduce the signal records. Proper time is not assumed as a prior geometric quantity in the reconstruction; the operational duration is inferred from calibrated pulse counts first, and a compatible metric must match it.

---

## 10. What remains beyond this proof

The theorem above proves the ideal local form of H2 under strong assumptions. The following work is still required to turn that conditional theorem into a broader reconstruction program.

### 10.1 Formal data theorem

Define minimal conditions under which $\mathcal{D}_{\mathrm{pulse}}$ has a dense-limit event-manifold interpretation, rather than treating event-manifold identification as an external input. This includes recovering the incidence map, embedded clock curves, and signal tangent directions or infinitesimal signal curves from raw relational records.

Sufficient raw-relational conditions are stated in `h2_raw_relational_identifiability.md`.

### 10.2 Conformal theorem

We proved the local proof-grade signal-direction version. A stronger version should prove when finite or causal-order signal data determine the conformal metric class.

### 10.3 Scale theorem

We proved the dense clock-rich version. A stronger version should specify minimal clock sampling needed to determine the conformal factor.

### 10.4 Gauge theorem

The diffeomorphism corollary depends on an external event-manifold identification result. A stronger version should derive that diffeomorphism freedom directly from the relational event structure.

### 10.5 Stability theorem

For noisy finite records, prove that small record perturbations produce controlled uncertainty in the reconstructed metric class under a specified metric norm.

The first finite-data stability and gauge conditions are stated in `h2_finite_data_stability_and_gauge.md`.

### 10.6 Constructive algorithm

Provide an algorithm that recovers known synthetic metrics:

- Minkowski spacetime
- weak static potential
- stationary metric with $g_{0i}$
- weak gravitational wave perturbation

The algorithm is not the proof, but it tests the proof's assumptions and exposes hidden degeneracies.

---

## 11. Failure modes

H2 can fail in several precise ways.

### 11.1 Insufficient network richness

Sparse clocks and signals may underdetermine the metric. This is not a failure of the hypothesis unless no plausible dense limit works.

### 11.2 Clock nonuniversality

If different ideal clock species imply different proper-time scales:

$$
\frac{dN_i}{f_i} \neq \frac{dN_j}{f_j}
$$

then there is no single universal metric for all pulse counters.

### 11.3 Nonmetric signal behavior

If signal propagation cannot be represented by null curves of any Lorentzian metric, H2 fails or must be generalized.

### 11.4 Nonmetric clock transport

If clock comparisons require torsion, nonmetricity, species-dependent couplings, or path rules not captured by $g_{\mu\nu}$, then H2 must be weakened.

### 11.5 Topological ambiguity

Signal records in regions with caustics, horizons, closed timelike curves, or nontrivial topology may not identify events uniquely without extra assumptions.

---

## 12. Relation to H3

H2 reconstructs the metric from local pulse and signal consistency.

H3 then asks whether curvature appears as loop non-integrability of those comparisons.

The logical order should be:

1. H2: recover $[g_{\mu\nu}]$.
2. Use $[g_{\mu\nu}]$ to define the Levi-Civita connection.
3. H3: show loop pulse-comparison residuals recover curvature.

So H3 should not be used as an assumption in the H2 proof. It should become a consequence or diagnostic after H2 succeeds.

---

## 13. Recommended future strengthening

The finite pulse-record schema is defined in `h2_finite_pulse_record_schema.md`, and the first executable reconstruction prototypes now exist in `src/pulse_model/h2_reconstruction.py`.

The next H2 strengthening work should:

- turn the calibrated Shapiro and weak-wave response benchmarks into full finite-schema observed records with separate truth sidecars
- add explicit residual, covariance, and Jacobian-rank checks for the claimed finite parameters
- test raw-relational event and signal identifiability conditions on finite event graphs
- broaden the sparse-network degeneracy analysis before claiming arbitrary metric-field reconstruction

Future implementation should stay explicit about which fields are observables and which coordinates, embeddings, metric parameters, and gauge choices are latent reconstruction variables.
