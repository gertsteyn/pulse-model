---
title: Hypotheses H1-H7
sidebar_label: Hypotheses H1-H7
sidebar_position: 4
---

# Hypotheses H1-H7

This page collects the bridge-program hypotheses, open conjectures, and current best formal statement from the original formalization.

## 6. Pulse Model as a bridge program

The previous section showed that known physics fits the pulse language. This section states the stronger research hypotheses.

---

### 6.1 Hypothesis H1: Time is relational pulse count

Instead of assuming a background parameter $t$, define time operationally by correlations between pulse counters.

For clock $C$ and system observable $O$,

$$
P(O=o \mid N_C=n)
$$

is more fundamental than

$$
P(O=o,t)
$$

This resembles relational-clock approaches to quantum mechanics.

Research task:

> Build a formal conditional-probability model where clock pulse count replaces external time while reproducing the Schrödinger equation in the appropriate limit.

See `appendix/h1_time_is_relational_pulse_count.md` for the conservative single-clock ideal theorem and proof.

---

### 6.2 Hypothesis H2: The metric is reconstructed from pulse comparisons

Assume a network of ideal clocks exchanging signals. Each clock records:

- local pulse count
- emitted signal pulse count
- received signal pulse count
- local acceleration data
- local clock transition type

For a calibrated record with a stated ansatz, nuisance model, and gauge
convention, the metric equivalence class is the object that best explains the
comparisons:

$$
[g_{\mu\nu}] = \arg\min_{[g]} \mathcal{E}[[g];\mathrm{pulse\ records}]
$$

where $\mathcal{E}$ measures mismatch between predicted and observed pulse comparisons.

Program:

> Reconstruct bounded metric-response or metric-equivalence-class information from calibrated pulse-comparison records.

This would make spacetime operational rather than assumed.

Current gate status: H2 is accepted for the ideal fixed-event uniqueness
theorem, partially accepted for restricted finite-data prototype slices, and
conditional for raw-relational event and signal identifiability. It is not
accepted for arbitrary sparse-record metric reconstruction or automatic metric
reconstruction from raw relational pulse records. See
`../evidence/acceptance_reports/h2_metric_reconstruction.md` for the gate decision.

---

### 6.3 Hypothesis H3: Curvature is pulse comparison holonomy

In flat spacetime, pulse comparisons around closed loops are path-independent once acceleration and signal delays are accounted for.

In curved spacetime, transporting clocks and comparing signals around loops can reveal path-dependent differences.

Pulse conjecture:

> Curvature measures non-integrability of pulse comparison.

Mathematically, curvature already measures non-commutativity of covariant transport:

$$
[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma
$$

Pulse version:

> If pulse synchronization is transported around a closed loop, curvature is the residual mismatch.

Research task:

> Formalize clock-synchronization holonomy and derive the Riemann tensor from pulse-network loops.

---

### 6.4 Hypothesis H4: Stress-energy is phase-response density

Known identity:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

Pulse hypothesis:

> Stress-energy is not merely "stuff that curves spacetime"; it is the local phase-response of matter to the pulse-count metric.

This suggests a deeper source-to-geometry map:

$$
\frac{\delta\Theta_{\mathrm{geom}}}{\delta g^{\mu\nu}}+\frac{\delta\Theta_{\mathrm{matter}}}{\delta g^{\mu\nu}}=0
$$

Known GR supplies

$$
\Theta_{\mathrm{geom}}=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int(R-2\Lambda)\sqrt{-g}\,d^4x
$$

The open challenge is to derive this geometric phase functional from pulse consistency.

---

### 6.5 Hypothesis H5: Quantum objects can carry superposed pulse histories

If a clock with internal Hamiltonian $H_C$ is placed in a superposition of two worldlines $\gamma_1$ and $\gamma_2$, then its internal state evolves as

$$
\lvert\chi_i\rangle=\exp\left(-\frac{iH_C\tau_i}{\hbar}\right)\lvert\chi_0\rangle
$$

The combined state can be

$$
\lvert\Psi\rangle=\alpha\lvert\gamma_1\rangle\lvert\chi(\tau_1)\rangle+\beta\lvert\gamma_2\rangle\lvert\chi(\tau_2)\rangle
$$

The path coherence is controlled by the overlap

$$
\mathcal{V}=\left|\langle\chi(\tau_2)\mid\chi(\tau_1)\rangle\right|
$$

For mixed internal state $\rho_C$,

$$
\mathcal{V}(\Delta\tau)=\left|\mathrm{Tr}\left(\rho_C\exp\left(-\frac{iH_C\Delta\tau}{\hbar}\right)\right)\right|
$$

where

$$
\Delta\tau=\tau_1-\tau_2
$$

Pulse interpretation:

> A single quantum object can carry a superposition of different pulse counts. If the internal pulse states become distinguishable, path interference decreases.

This is a precise interface between time dilation and quantum coherence.

---

### 6.6 Hypothesis H6: Classical spacetime emerges when pulse histories decohere

If matter and clocks become entangled with different metric histories, then classical spacetime may emerge as a decohered branch structure.

Possible schematic state:

$$
\lvert\Psi\rangle=\sum_a c_a\lvert g_a\rangle\lvert M_a(g_a)\rangle
$$

Here $M_a(g_a)$ denotes matter phase histories on metric branch $g_a$.

Classical GR corresponds to one branch or a narrow packet of metrics where total phase is stationary.

Research task:

> Model under what conditions superpositions of pulse-count metrics decohere into effective classical geometries.

---

### 6.7 Hypothesis H7: Vacuum energy problem is phase-response, not absolute phase

Vacuum modes may have large absolute phase/action density. But gravity may couple only to a renormalized or relational phase-response.

Known problem:

$$
\rho_{\mathrm{vac}}^{\mathrm{naive}} \gg \rho_\Lambda^{\mathrm{observed}}
$$

Pulse conjecture:

> Absolute uniform vacuum phase may not gravitate directly; only metric-sensitive residual phase-response contributes to curvature.

Current H7 status:

[The H7 appendix](../appendix/h7_vacuum_phase_response.md) accepts only a constrained reformulation. A pure bookkeeping phase has no source if it is not a metric functional, while a uniform covariant vacuum action density coupled through $\sqrt{-g}$ is metric-sensitive and is degenerate with a cosmological-constant term. The conservative gravitational object is the metric variation of the renormalized effective action.

This does not solve the cosmological-constant problem. H7 does not derive $\Lambda$, does not protect the observed value against radiative corrections, and does not predict a dark-energy equation of state.

---

## 15. Open conjectures

### Conjecture 1: Metric-from-pulse-correlations

A Lorentzian metric can be reconstructed from a sufficiently rich set of relational pulse-count and signal-exchange records.

Formal target:

$$
\{N_i,\mathrm{signals}\} \Rightarrow [g_{\mu\nu}]
$$

where $[g_{\mu\nu}]$ is an equivalence class under diffeomorphisms.

### Conjecture 2: Curvature as pulse holonomy

Riemann curvature is equivalent to infinitesimal non-closure of pulse synchronization around loops.

Formal target:

$$
\lim_{\Sigma\to 0} \frac{\Delta N_{\mathrm{loop}}}{\Sigma} \sim R^\rho{}_{\sigma\mu\nu}
$$

with the correct tensor structure.

### Conjecture 3: Stress-energy as phase-response is fundamental

The standard definition of stress-energy is not merely a variational tool. It expresses the physical reason matter sources geometry:

$$
T_{\mu\nu} \propto \frac{\delta \mathrm{matter\ phase}}{\delta \mathrm{pulse-count\ metric}}
$$

### Conjecture 4: Einstein-Hilbert action is geometric pulse-consistency cost

The action

$$
\int R\sqrt{-g}\,d^4x
$$

arises because curvature measures local pulse-comparison inconsistency, and the universe takes stationary total phase over geometry plus matter.

### Conjecture 5: Proper time is a quantum observable only relationally

Proper time should not be promoted to a universal external operator. It appears as a relational observable between clock subsystems and the rest of the system.

### Conjecture 6: Classical spacetime is a decohered pulse-history phase

Spacetime geometry is classical when alternative pulse-count metrics decohere enough that one stationary metric dominates observed correlations.

---

## 18. Current best formal statement

The Pulse Model, in its strongest current form, is:

> Physical systems are quantum phase accumulators. Readable clocks count stable phase beats. Proper time is the path-dependent accumulation parameter for local clocks. The spacetime metric is the universal rule assigning pulse/phase accumulation to path elements. Free motion is stationary phase through that metric. Stress-energy is the response of matter phase to changes in the metric. Classical spacetime is the stationary phase configuration of geometry plus matter. Quantum gravity begins when pulse-count histories and/or the metric itself must be treated in superposition.

Compact symbolic spine:

$$
dN_i = f_i d\tau
$$

$$
d\tau^2 = -\frac{1}{c^2}g_{\mu\nu}dx^\mu dx^\nu
$$

$$
\Theta = \frac{S}{\hbar}
$$

$$
S_{\mathrm{free\ massive}}=-mc^2\int d\tau
$$

$$
T_{\mu\nu} = -\frac{2\hbar}{\sqrt{-g}} \frac{\delta \Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

$$
\delta \left( \Theta_{\mathrm{geom}} + \Theta_{\mathrm{m}} \right) =0
$$

Target open derivation:

$$
\Theta_{\mathrm{geom}} \stackrel{?}{=} \frac{1}{\hbar} \frac{c^3}{16\pi G} \int(R-2\Lambda)\sqrt{-g}\,d^4x
$$

from pulse-count consistency.

---
