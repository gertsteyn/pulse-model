---
title: Formal Model
sidebar_label: Formal Model
sidebar_position: 1
---

# Formal Model

This is the focused reference entry point for the Pulse Model formalization. It preserves the core statement from the original monolithic formalization and links to the split reference pages.

## Reference Pages

- [Definitions and axioms](./definitions_and_axioms.md)
- [Known-physics recovery](./known_physics_recovery.md)
- [Hypotheses H1-H7](./hypotheses_h1_h7.md)
- [Validation ladder](./validation_ladder.md)
- [Workstreams and API](./workstreams_and_api.md)
- [References](./references.md)

The compatibility full-source page remains at [The formal Pulse Model](../pulse_model_formalization.md).

## Abstract

The Pulse Model proposes that physical time should be treated operationally as **accumulated local pulse count**, where a pulse is not a universal cosmic tick, but a countable unit of local quantum phase evolution. Atomic transitions are the cleanest readable example of such pulses. In established physics, an ideal clock measures **proper time** along its worldline, while quantum amplitudes accumulate **phase** equal to action divided by Planck's constant:

$$
\Theta = \frac{S}{\hbar}
$$

For a free massive particle,

$$
S = -mc^2 \int d\tau
$$

so its quantum phase is directly proportional to accumulated proper time:

$$
\Theta = -\frac{mc^2}{\hbar}\tau
$$

This gives the core bridge:

worldline → proper time → pulse count → quantum phase

The model does not start by replacing GR or QM. It begins by reframing their common seam: **proper time in GR is phase accumulation in QM**. The research question is whether spacetime geometry can be understood as the consistency structure governing comparisons between local phase/pulse accumulators.

The model has two layers:

1. **Conservative layer:** a re-expression of known physics in pulse/phase language. This reproduces special-relativistic time dilation, gravitational time dilation, Newtonian gravity as a weak-field limit, geodesic motion, gravitational redshift, and quantum gravitational phase shifts.
2. **Speculative layer:** a research program that asks whether the metric, stress-energy coupling, and quantum gravity can be derived from relational pulse-count consistency rather than assumed as background structure.

A central identity for the research program is that stress-energy can be written as the response of matter action, and therefore matter phase, to changes in the metric:

$$
T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta S_{\mathrm{m}}}{\delta g^{\mu\nu}} = -\frac{2\hbar}{\sqrt{-g}} \frac{\delta \Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

In pulse language:

> Stress-energy is the sensitivity of matter phase accumulation to the pulse-count metric.

This creates a concrete seam to investigate:

matter phase response ↔ spacetime geometry

---

## 0. Reading guide

This document uses three labels:

| Label | Meaning |
|---|---|
| **Known** | Standard GR/QM result, rephrased in pulse language. |
| **Hypothesis** | Pulse Model claim not yet derived from established theory. |
| **Program** | Concrete workstream for agents to formalize, simulate, test, or falsify the model. |

The document is written so that Codex agents can split the work into independent modules:

- symbolic derivations
- numerical simulations
- clock-network metric reconstruction
- quantum clock/interferometer modeling
- equivalence-principle violation searches
- literature mapping
- speculative action-principle development

---

## 1. Core hypothesis

### 1.1 Informal statement

The Pulse Model begins with this operational statement:

> Time is not a universal background flow. Time is the accumulated local count of physical phase/pulse evolution along a worldline.

The most concrete pulse is an atomic transition. A clock based on an atomic transition counts cycles of a frequency

$$
f_0 = \frac{\Delta E}{h}
$$

where $\Delta E$ is the energy difference between two quantum states.

If the atom follows a worldline $\gamma$, the number of local transition cycles accumulated along that worldline is

$$
N[\gamma] = \int_\gamma f_0\,d\tau
$$

where $d\tau$ is proper time.

This is the basic pulse-count equation.

### 1.2 Deeper phase statement

A readable clock pulse is only one kind of quantum phase. More generally, a quantum path has phase

$$
\Theta[\gamma] = \frac{S[\gamma]}{\hbar}
$$

For a free massive object,

$$
S[\gamma] = -mc^2 \int_\gamma d\tau
$$

so

$$
\Theta[\gamma] = -\omega_C \tau[\gamma]
$$

where

$$
\omega_C = \frac{mc^2}{\hbar}
$$

is the Compton angular frequency.

This does **not** mean ordinary matter exposes a practical clock at the Compton frequency. It means that the action phase of massive matter is tied to proper time at a very deep level.

### 1.3 Working slogan

> Matter is phase accumulation. Atomic clocks are readable phase beats. Gravity is the geometry that controls how phase/pulse counts compare between paths.

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

