---
title: Definitions And Axioms
sidebar_label: Definitions And Axioms
sidebar_position: 2
---

# Definitions And Axioms

This page collects the formal definitions, principles, and core mathematical objects from the original Pulse Model formalization.

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

## 3. Definitions and notation

### 3.1 Spacetime

Let $M$ be a differentiable four-dimensional manifold with metric $g_{\mu\nu}$. Use signature

$$
(-,+,+,+)
$$

Coordinates are written $x^\mu$, with $x^0 = ct$ when convenient.

### 3.2 Worldline

A timelike worldline is a map

$$
\gamma:\lambda \mapsto x^\mu(\lambda)
$$

from a parameter $\lambda$ to spacetime events.

### 3.3 Proper time

For a timelike worldline,

$$
d\tau = \frac{1}{c} \sqrt{-g_{\mu\nu}dx^\mu dx^\nu}
$$

and

$$
\tau[\gamma,g] = \int_\gamma d\tau
$$

### 3.4 Pulse

A pulse is a countable local cycle of a physical system. In the conservative model, the cleanest pulse is a quantum transition phase cycle.

For transition energy $\Delta E$,

$$
\omega_0 = \frac{\Delta E}{\hbar}
$$

and

$$
f_0 = \frac{\omega_0}{2\pi} = \frac{\Delta E}{h}
$$

### 3.5 Pulse count

For an ideal clock transition $i$,

$$
N_i[\gamma,g] = \frac{1}{2\pi}\int_\gamma \omega_i\,d\tau = \int_\gamma f_i\,d\tau
$$

For a stable clock with constant local frequency $f_i$,

$$
N_i = f_i \tau
$$

### 3.6 Quantum phase

For a path $\gamma$,

$$
\Theta[\gamma] = \frac{S[\gamma]}{\hbar}
$$

where $S$ is the action.

For a free massive particle,

$$
S[\gamma] = -mc^2 \tau[\gamma]
$$

so

$$
\Theta[\gamma] = -\frac{mc^2}{\hbar}\tau[\gamma]
$$

### 3.7 Pulse-count metric

The metric is the rule that assigns proper-time intervals to path elements. In pulse language:

> The metric is the local rule that determines how many ideal pulses a path segment can accumulate.

For an ideal clock $i$,

$$
dN_i = f_i d\tau
$$

so

$$
dN_i^2 = f_i^2 d\tau^2 = -\frac{f_i^2}{c^2}g_{\mu\nu}dx^\mu dx^\nu
$$

Since $f_i$ is clock-specific, the universal object is not $dN_i$ but $d\tau$, or equivalently the metric.

### 3.8 Event comparison

Two clocks can meaningfully compare pulse counts only when their worldlines intersect or when they exchange signals with a known protocol.

If two clocks start at event $A$, follow worldlines $\gamma_1,\gamma_2$, and reunite at event $B$, then the pulse difference is

$$
\Delta N_i = f_i\left(\tau[\gamma_1]-\tau[\gamma_2]\right)
$$

This difference is physically observable and coordinate-independent.

---

## 4. Axioms and principles

### P1. Local phase accumulation

Every physical system evolves by accumulating quantum phase.

For a path or history $h$,

$$
\Theta[h]=\frac{S[h]}{\hbar}
$$

This is standard quantum mechanics in action form.

### P2. Ideal pulse counters measure proper time

For an ideal localized clock following timelike worldline $\gamma$,

$$
N_i[\gamma]=\int_\gamma f_i\,d\tau
$$

This is standard relativistic clock behavior.

### P3. Pulse universality

All ideal pulse counters couple to the same spacetime metric:

$$
dN_i/f_i = dN_j/f_j = d\tau
$$

for all ideal clock types $i,j$.

This is the pulse-language form of local position invariance and metric universality.

### P4. Classical paths are stationary phase paths

In the classical limit, paths whose action varies rapidly cancel by destructive interference. The observed classical path satisfies

$$
\delta S = 0
$$

or equivalently

$$
\delta \Theta = 0
$$

This is the action-phase bridge.

### P5. Gravity is pulse-count geometry

Gravity is not treated as a force field acting inside time. It is the metric structure that determines pulse/phase accumulation along paths.

Conservative version:

$$
g_{\mu\nu} \mathrm{determines} d\tau
$$

Speculative version:

$$
g_{\mu\nu} \mathrm{emerges\ from\ consistency\ constraints\ among\ quantum\ pulse\ histories}
$$

### P6. Stress-energy is phase-response

Because matter phase is $\Theta_{\mathrm{m}}=S_{\mathrm{m}}/\hbar$, the stress-energy tensor is the metric response of matter phase:

$$
T_{\mu\nu} = -\frac{2\hbar}{\sqrt{-g}} \frac{\delta \Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

This is mathematically equivalent to the standard definition of stress-energy, but the interpretation is pulse-model-specific.

### P7. No universal pulse

The model rejects a global cosmic tick.

There are only local pulse counters and relational comparisons.

---

## 7. Core mathematical object

The Pulse Model can be expressed using three functionals.

### 7.1 Proper-time functional

$$
\tau[\gamma,g] = \int_\gamma \frac{1}{c} \sqrt{-g_{\mu\nu}dx^\mu dx^\nu}
$$

This is GR's clock functional.

### 7.2 Pulse functional

For clock species $i$,

$$
N_i[\gamma,g] = \int_\gamma f_i(\xi)\,d\tau
$$

where $\xi$ denotes internal/environmental variables. For an ideal clock, $f_i$ is constant.

### 7.3 Phase functional

For matter history $h$,

$$
\Theta[h,g] = \frac{1}{\hbar}S[h,g]
$$

For localized free massive worldline:

$$
\Theta[\gamma,g] = -\frac{mc^2}{\hbar}\tau[\gamma,g]
$$

For fields:

$$
\Theta[\psi,g] = \frac{1}{\hbar} \int \mathcal{L}(\psi,\nabla\psi,g) \sqrt{-g}\,d^4x
$$

### 7.4 Total phase

$$
\Theta_{\mathrm{total}}[g,\psi]=\Theta_{\mathrm{geom}}[g]+\Theta_{\mathrm{matter}}[g,\psi]
$$

Classical equations:

$$
\delta\Theta_{\mathrm{total}}=0
$$

Quantum theory:

$$
Z=\int\mathcal{D}g\,\mathcal{D}\psi\,\exp\left(i\Theta_{\mathrm{total}}[g,\psi]\right)
$$

The Pulse Model's central program is to explain the origin and meaning of $\Theta_{\mathrm{geom}}$ from pulse-count consistency.

---

