---
title: Validation Ladder
sidebar_label: Validation Ladder
sidebar_position: 5
---

# Validation Ladder

This page collects the problem targets, testable extensions, failure modes, validation ladder, success criteria, failure criteria, and immediate next-action material from the original formalization. Some historical agent-planning language is preserved for no-loss migration and may be superseded by Beads.

## 2. Current gaps in physics targeted by the model

The Pulse Model is not equally relevant to every unsolved problem. It is most relevant where **time, phase, clocks, and gravity** meet.

### 2.1 Problem of time

In ordinary quantum mechanics, time is usually an external parameter:

$$
i\hbar \frac{\partial}{\partial t}\lvert \psi(t) \rangle = H\lvert \psi(t) \rangle
$$

In GR, time is part of the dynamical geometry. Clocks measure proper time along paths through spacetime:

$$
d\tau^2 = -\frac{1}{c^2}g_{\mu\nu}dx^\mu dx^\nu
$$

These two roles of time do not match cleanly. Reviews of quantum time and quantum clocks identify this mismatch as a conceptual barrier to quantum gravity.

Pulse-model response:

> Replace external time with correlations between physical pulse counters.

This points toward relational-clock frameworks, Page-Wootters-style conditional dynamics, and quantum reference frames.

### 2.2 Quantum source of gravity

GR sources curvature using stress-energy:

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}
$$

But quantum matter can be in superposition. If a mass is in a spatial superposition, what is the gravitational field?

Possibilities:

1. gravity remains classical and is sourced by $\langle T_{\mu\nu}\rangle$
2. gravity becomes quantum and enters superposition
3. new collapse/decoherence physics appears
4. the current question is badly posed because spacetime itself is emergent

Pulse-model response:

> A quantum source is a superposition of phase-density histories. The question becomes whether the pulse-count metric also enters superposition.

### 2.3 Semiclassical gravity and measurement

The semiclassical equation

$$
G_{\mu\nu} = \frac{8\pi G}{c^4}\langle T_{\mu\nu}\rangle
$$

is useful, but may fail for superpositions, measurement, and entanglement. The Pulse Model reframes this as:

> Does geometry respond to averaged phase-response, branch-specific phase-response, or something relational between pulse histories?

### 2.4 Black holes and singularities

Black holes expose a clash between:

- GR horizons and singularities
- quantum information
- thermodynamics
- observer-dependent time
- extreme redshift

Pulse-model response:

> A horizon is a boundary where outside pulse comparison with inward-falling histories becomes singular. The information problem becomes a question about how phase/pulse records are preserved, hidden, scrambled, or relationally encoded.

This is not yet a solution, but it gives a language.

### 2.5 Cosmological constant / vacuum energy

Vacuum fields contribute quantum phase/action density. Naively, this should gravitate enormously. Observed dark energy is tiny compared to naive quantum field theory estimates.

Pulse-model response:

> The cosmological constant problem may be a mismatch between absolute vacuum phase density and gravitationally relevant phase-response differences.

This is speculative. It is included because the model treats energy as phase rate, and vacuum energy is therefore naturally inside the seam.

### 2.6 Equivalence principle in quantum-clock regimes

The equivalence principle is extremely well tested for classical falling bodies, including satellite tests such as MICROSCOPE. But quantum clocks and internal energy superpositions create sharper questions:

- Do different internal states couple identically to gravity?
- Does proper time remain universal for all clock species?
- Can a single quantum clock experience a superposition of proper times?
- Does time-dilation-induced decoherence reveal new physics?

Pulse-model response:

> Universality becomes pulse universality: all ideal pulse counters couple to the same metric.

A violation would appear as clock-species-dependent or internal-state-dependent pulse accumulation.

---

## 9. Testable extensions and parameterizations

The model must not merely rename known physics. It should suggest precise tests.

### 9.1 Clock-species universality violation

Standard metric theory predicts

$$
\frac{dN_i}{f_i}=d\tau
$$

for all ideal clock species $i$.

A violation can be parameterized:

$$
\frac{dN_i}{dt} = f_i \left[ 1 + (1+\alpha_i)\frac{\Phi}{c^2} - (1+\beta_i)\frac{v^2}{2c^2} + \cdots \right]
$$

GR predicts

$$
\alpha_i=0,\qquad \beta_i=0
$$

for all ideal clocks.

Research tasks:

- collect clock-comparison bounds on $\alpha_i,\beta_i$
- map to Standard-Model Extension coefficients where applicable
- identify which transitions maximize sensitivity

### 9.2 Internal-state-dependent free fall

If internal energy contributes differently to gravitational coupling, then atoms in different internal states may fall differently.

Parameterization:

$$
m_g^{(a)} = m_i^{(a)}(1+\epsilon_a)
$$

Transition-dependent signal:

$$
\Delta\epsilon_{ab}=\epsilon_a-\epsilon_b
$$

GR predicts

$$
\Delta\epsilon_{ab}=0
$$

Pulse interpretation:

> Internal pulse energy must gravitate universally.

### 9.3 Proper-time superposition visibility

For a clock in a spatial superposition with proper-time difference $\Delta\tau$, visibility is

$$
\mathcal{V}(\Delta\tau) = \left| \mathrm{Tr} \left( \rho_C e^{-iH_C\Delta\tau/\hbar} \right) \right|
$$

Research task:

- simulate $\mathcal{V}$ for realistic atomic clocks
- include gravitational height differences
- include velocity time dilation
- compare with proposed clock-interferometry experiments

### 9.4 Metric superposition witness

If two masses become entangled only through gravity, that suggests gravity has non-classical mediation properties.

Pulse-model framing:

> Can two pulse histories become entangled through a shared pulse-count metric?

Research task:

- translate Bose-Marletto-Vedral-style and related gravitational-entanglement proposals into pulse-history language
- identify what observable is actually a pulse/phase comparison

### 9.5 Clock-network curvature reconstruction

Use a network of clocks to reconstruct curvature from pulse ratios and signal timing.

Inputs:

$$
\{N_i^{\mathrm{emit}},N_j^{\mathrm{recv}},\mathrm{signal\ phase},\mathrm{local\ acceleration}\}
$$

Output:

$$
\hat g_{\mu\nu}(x)
$$

Research tasks:

- implement a synthetic clock network in Minkowski spacetime
- add weak gravitational potential
- reconstruct $g_{00}$
- add rotating source and attempt reconstruct $g_{0i}$
- add gravitational wave perturbation $h_{\mu\nu}$

---

## 10. Failure modes and constraints

### 10.1 No hidden preferred frame

The model must not smuggle in a universal pulse or preferred foliation unless it explicitly predicts Lorentz violation.

Constraint:

$$
\mathrm{Local\ Lorentz\ invariance\ must\ be\ recovered.}
$$

### 10.2 Coordinate invariance

Pulse counts along closed worldline comparisons are observable. Coordinates are not.

The model must be diffeomorphism-invariant:

$$
x^\mu \rightarrow x'^\mu(x)
$$

must not change physical predictions.

### 10.3 Massless fields

Photons have

$$
d\tau=0
$$

along null paths. A model based only on proper-time pulses cannot describe light.

Fix:

> Use proper-time pulse counts for clocks, but use action/phase for general quantum fields.

For light, phase is not $mc^2\tau/\hbar$. It is field phase governed by null propagation and electromagnetic action.

### 10.4 Scalar clock-rate field is insufficient

As noted above, full gravity is tensorial.

The model must reproduce:

- light bending
- perihelion precession
- frame dragging
- gravitational waves
- black hole metrics
- cosmological metrics

This requires $g_{\mu\nu}$, not only a scalar pulse-rate function.

### 10.5 Clock imperfections are not fundamental time

Real clocks suffer shifts:

- temperature
- electromagnetic fields
- acceleration sensitivity
- collisions
- finite linewidth
- environmental decoherence

The model must distinguish:

$$
\mathrm{ideal\ pulse\ count} f_i d\tau
$$

from device-specific perturbations.

### 10.6 Circularity risk

If we define pulses using proper time and define proper time using the metric, then use pulses to define the metric, circularity can occur.

Research requirement:

> Develop an operational reconstruction method where the metric is inferred from relational pulse data without assuming the metric as prior input.

### 10.7 Conservation laws

GR implies

$$
\nabla_\mu T^{\mu\nu}=0
$$

via diffeomorphism invariance and the Bianchi identity.

Pulse-model action principles must preserve this.

### 10.8 Quantum measurement

The model does not yet solve measurement/collapse. If it adds collapse, it must specify:

- what collapses
- in which basis
- whether energy is conserved
- whether Lorentz invariance survives
- whether faster-than-light signaling is avoided

---

## 14. Validation ladder

The model should advance only by passing increasingly strict levels.

### Level 0: Dimensional consistency

Every equation must have correct units.

### Level 1: Special relativity

Reproduce:

$$
d\tau=dt\sqrt{1-v^2/c^2}
$$

### Level 2: Weak-field GR

Reproduce:

$$
\frac{d\tau}{dt} \approx 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}
$$

and

$$
\mathbf{a}=-\nabla\Phi
$$

### Level 3: Quantum phase

Reproduce:

$$
\Theta=S/\hbar
$$

and the COW phase shift.

### Level 4: Full metric GR

Handle:

- Schwarzschild
- Kerr
- FLRW
- gravitational waves
- geodesic deviation

### Level 5: Quantum clocks

Model:

- proper-time superpositions
- clock-interferometer visibility
- gravitational time-dilation-induced entanglement/decoherence

### Level 6: Source-to-metric coupling

Recover:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}
$$

or produce a controlled modification with testable predictions.

### Level 7: New physics

Predict deviations not already ruled out.

Examples:

- clock-species-dependent redshift
- internal-state-dependent free fall
- anomalous decoherence in quantum clock superpositions
- metric reconstruction residuals not explained by GR
- modified vacuum phase-response

---

## 16. What would count as success?

The Pulse Model becomes scientifically serious if it can do at least one of these:

1. **Derive a known result more naturally.**  
   Example: derive Einstein-Hilbert action from pulse-holonomy consistency.

2. **Unify two known formalisms.**  
   Example: show Page-Wootters relational time and GR proper time share a common pulse-count structure.

3. **Produce a new calculation tool.**  
   Example: a clock-network metric reconstruction method useful for relativistic geodesy or gravitational-wave detection.

4. **Generate a testable deviation.**  
   Example: a small clock-species-dependent redshift parameter not already excluded.

5. **Clarify quantum gravity experiments.**  
   Example: express gravitational entanglement proposals as pulse-history phase comparisons and identify what is actually being measured.

---

## 17. What would count as failure?

The model fails or must be heavily revised if:

1. It requires a universal preferred clock without predicting observed Lorentz invariance.
2. It cannot handle photons or massless fields.
3. It reproduces only $g_{00}$ but not full $g_{\mu\nu}$.
4. It cannot recover the Einstein equation or a viable alternative.
5. It predicts clock-species deviations already ruled out.
6. It cannot preserve energy-momentum conservation.
7. It produces coordinate-dependent observables.
8. It is only a vocabulary shift and yields no new derivations, tools, or tests.

---

## 20. Immediate next actions

For the formal proof order, dependency gates, progress status vocabulary, and current queue, use `roadmap.md` as the source of truth.

The current next work is no longer the original agent-order sketch. H1 through H7 and the known-physics recovery ladder now have accepted-with-limits artifacts, so downstream work should start from the proof ledger rather than this early planning list.

At the current gate, H7 should be used only in its accepted constrained sense: it separates absolute bookkeeping phase from covariant renormalized response, but it does not derive $\Lambda$, solve vacuum-energy naturalness, or predict dark-energy evolution. New downstream work should follow `roadmap.md`, preserving the caveats attached to 05, 05S, H6, and H7.

---

## 21. Short version for agents

```text
We model physical time as local pulse/phase accumulation.

Known equations:
  dN_i = f_i dτ
  dτ² = -(1/c²) g_μν dx^μ dx^ν
  Θ = S/ħ
  S_free = -mc² ∫ dτ
  T_μν = -(2ℏ/√-g) δΘ_matter/δg^μν

Recover:
  SR time dilation
  gravitational redshift
  weak-field Newtonian gravity
  geodesics
  quantum phase shifts
  clock-interferometer visibility
  Einstein equation from total phase stationarity

Main hypothesis:
  Spacetime metric is the consistency structure for comparing local quantum pulse histories.

Main open derivation:
  Derive or motivate Θ_geometry = (c³/16πGℏ)∫(R-2Λ)√-g d⁴x from pulse-comparison consistency.

Do not:
  introduce universal clock
  assume scalar clock-speed field is enough
  ignore massless fields
  make coordinate-dependent predictions
  bypass known experimental constraints
```
