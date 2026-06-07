# The Pulse Model

**Version:** 0.2  
**Status:** Working formalization / research program  
**Purpose:** Provide a rigorous shared document for exploring whether a pulse/phase view of time can help bridge conceptual and mathematical gaps between general relativity (GR) and quantum mechanics (QM).

---

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

## 5. Known physics recovered

This section proves that the conservative Pulse Model reproduces standard relativistic and quantum results.

---

### 5.1 Special-relativistic time dilation

In flat spacetime,

$$
ds^2 = -c^2dt^2 + dx^2 + dy^2 + dz^2
$$

For timelike motion,

$$
d\tau^2 = -\frac{ds^2}{c^2}
$$

so

$$
d\tau^2 = dt^2 - \frac{dx^2+dy^2+dz^2}{c^2}
$$

Let

$$
v^2 = \left(\frac{dx}{dt}\right)^2+ \left(\frac{dy}{dt}\right)^2+ \left(\frac{dz}{dt}\right)^2
$$

Then

$$
d\tau = dt\sqrt{1-\frac{v^2}{c^2}}
$$

Pulse count:

$$
dN_i = f_i d\tau = f_i dt\sqrt{1-\frac{v^2}{c^2}}
$$

So a moving clock accumulates fewer pulses per coordinate time $dt$ than a clock at rest in that coordinate frame.

Pulse interpretation:

> Motion tilts the worldline through spacetime. The moving path accumulates less proper-time pulse count per reference-frame time.

---

### 5.2 Gravitational time dilation in Schwarzschild spacetime

Outside a non-rotating spherical mass $M$, the Schwarzschild metric is

$$
ds^2 = -\left(1-\frac{2GM}{rc^2}\right)c^2dt^2 + \left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2 + r^2d\Omega^2
$$

For a static clock at fixed $r,\theta,\phi$,

$$
dr=d\theta=d\phi=0
$$

so

$$
d\tau = dt\sqrt{1-\frac{2GM}{rc^2}}
$$

A lower clock has smaller $r$, so it accumulates fewer pulses per distant coordinate time $dt$.

Pulse count:

$$
dN_i = f_i dt\sqrt{1-\frac{2GM}{rc^2}}
$$

Weak-field approximation:

$$
\Phi(r) = -\frac{GM}{r}
$$

and

$$
1-\frac{2GM}{rc^2} = 1+\frac{2\Phi}{c^2}
$$

For $|\Phi|/c^2 \ll 1$,

$$
\frac{d\tau}{dt} \approx 1+\frac{\Phi}{c^2}
$$

Since $\Phi$ is more negative deeper in gravity, deeper clocks tick slower relative to higher clocks.

Pulse interpretation:

> Gravitational potential changes the pulse-count conversion between local clocks and distant clocks.

---

### 5.3 Weak-field gravity plus velocity

In weak gravity and low velocity, with $\Phi\to 0$ at infinity and retaining only first-order terms in $\Phi/c^2$ and $v^2/c^2$,

$$
\frac{d\tau}{dt} \approx 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}
$$

Therefore

$$
\frac{dN_i}{dt} \approx f_i \left( 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2} \right)
$$

This captures the two satellite-clock effects:

- higher gravitational potential increases pulse accumulation
- higher speed decreases pulse accumulation

Pulse interpretation:

> A worldline collects pulses according to both where it goes in the gravitational pulse landscape and how much spatial motion it has.

---

### 5.4 Newtonian gravity from proper-time action

For a free massive particle,

$$
S=-mc^2\int d\tau
$$

Use the weak-field approximation:

$$
d\tau \approx dt\left(1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}\right)
$$

Then

$$
S \approx -mc^2\int dt\left(1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}\right)
$$

Expand:

$$
S \approx -mc^2\int dt - m\int \Phi\,dt + \int \frac{1}{2}mv^2\,dt
$$

The first term is constant for variations with fixed coordinate-time endpoints, so it does not affect the path. The remaining nonrelativistic action is

$$
S_{\mathrm{NR}} = \int\left(\frac{1}{2}mv^2 - m\Phi\right)dt
$$

This is the Newtonian action with potential energy

$$
U=m\Phi
$$

The Lagrangian is

$$
L=\frac{1}{2}mv^2-m\Phi
$$

Use components $x^i(t)$ and define

$$
v^i=\frac{dx^i}{dt}
$$

and

$$
a^i=\frac{d^2x^i}{dt^2}
$$

Euler-Lagrange gives

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial v^i}\right)-\frac{\partial L}{\partial x^i}=0
$$

Compute the two terms:

$$
\frac{\partial L}{\partial v^i}=mv^i
$$

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial v^i}\right)=ma^i
$$

$$
\frac{\partial L}{\partial x^i}=-m\frac{\partial\Phi}{\partial x^i}
$$

Therefore

$$
ma^i+m\frac{\partial\Phi}{\partial x^i}=0
$$

and

$$
a^i=-\frac{\partial\Phi}{\partial x^i}
$$

Vector form:

$$
\mathbf{a}=-\nabla\Phi
$$

This is Newtonian gravity.

Pulse interpretation:

> Newtonian falling emerges from stationary phase/pulse accumulation in a weak gravitational pulse-count landscape.

---

### 5.5 Gravitational potential energy as rest-phase detuning

Rest energy:

$$
E_0=mc^2
$$

Rest phase rate:

$$
\omega_C=\frac{mc^2}{\hbar}
$$

Weak gravitational time dilation:

$$
\frac{d\tau}{dt}\approx 1+\frac{\Phi}{c^2}
$$

Coordinate-time phase rate:

$$
\Omega=\frac{d\Theta}{dt}=-\frac{mc^2}{\hbar}\frac{d\tau}{dt}
$$

So

$$
\Omega\approx -\frac{mc^2}{\hbar}-\frac{m\Phi}{\hbar}
$$

The gravitational contribution to phase rate is

$$
\Delta\Omega_\Phi=-\frac{m\Phi}{\hbar}
$$

This corresponds to the usual potential energy term $m\Phi$.

Pulse interpretation:

> Gravitational potential energy is rest-energy phase detuned by gravitational time dilation.

This is one of the strongest explanatory compressions of the model.

---

### 5.6 Geodesics from stationary proper time

For a free massive particle,

$$
S=-mc^2\int d\tau
$$

Since $-mc^2$ is constant, extremizing $S$ is equivalent to extremizing proper time:

$$
\delta\int d\tau=0
$$

Use an arbitrary path parameter $\lambda$ and define

$$
u^\mu=\frac{dx^\mu}{d\lambda}
$$

The action may be written as

$$
S=-mc\int\sqrt{-g_{\mu\nu}u^\mu u^\nu}\,d\lambda
$$

where $u^\mu=dx^\mu/d\lambda$. Variation with respect to $x^\mu(\lambda)$ yields the geodesic equation:

$$
\frac{d^2x^\rho}{d\tau^2}+\Gamma^\rho_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau}=0
$$

The connection coefficients are

$$
\Gamma^\rho_{\mu\nu}=\frac{1}{2}g^{\rho\sigma}\left(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu}\right)
$$

Pulse interpretation:

> A freely falling object follows the path where accumulated phase/pulse count is stationary.

This is not a psychological "choice". It is a stationary-action condition.

---

### 5.7 Quantum phase and path integrals

Quantum mechanics assigns a path amplitude proportional to

$$
e^{iS[\gamma]/\hbar}
$$

The total amplitude is a sum over possible paths:

$$
K(B,A) = \int_{\gamma:A\to B} \mathcal{D}\gamma\, e^{iS[\gamma]/\hbar}
$$

In the classical limit, paths far from stationary action cancel by destructive interference. Paths near

$$
\delta S=0
$$

survive constructively.

Pulse interpretation:

> The classical path is the path where neighboring pulse/phase histories stay aligned.

This gives a direct bridge between:

- geodesics in GR
- action in classical mechanics
- phase in QM

---

### 5.8 Atomic transition as readable pulse

For atomic states $\lvert a\rangle$ and $\lvert b\rangle$ with energies $E_a$ and $E_b$,

$$
\Delta E=E_b-E_a
$$

The relative phase evolves as

$$
\Delta\varphi=\frac{\Delta E}{\hbar}\tau
$$

A full cycle occurs when

$$
\Delta\varphi=2\pi
$$

so

$$
f=\frac{\Delta E}{h}
$$

A clock counting this transition accumulates

$$
N=\frac{\Delta\varphi}{2\pi}=\frac{\Delta E}{h}\tau=f\tau
$$

Pulse interpretation:

> An atomic clock is a quantum phase-difference counter.

---

### 5.9 Gravitational redshift

Consider two static observers $A$ and $B$ in a stationary gravitational field, with $A$ emitting and $B$ receiving. For each observer,

$$
d\tau = \sqrt{-g_{00}}\,dt
$$

assuming coordinates with $x^0=ct$ and no spatial motion.

If the same coordinate-time interval $dt$ passes, the pulse counts are

$$
dN_A = f_0 \sqrt{-g_{00}(A)}\,dt
$$

$$
dN_B = f_0 \sqrt{-g_{00}(B)}\,dt
$$

For a light signal, the coordinate cycle rate is conserved in a stationary spacetime. The received frequency compared against the receiver's local clock is therefore:

$$
\frac{\nu_B}{\nu_A} = \frac{\sqrt{-g_{00}(A)}}{\sqrt{-g_{00}(B)}}
$$

Weak-field:

$$
g_{00}\approx -\left(1+\frac{2\Phi}{c^2}\right)
$$

so

$$
\frac{\Delta \nu}{\nu_A} \approx \frac{\Phi_A-\Phi_B}{c^2}
$$

where $\Delta\nu=\nu_B-\nu_A$. If $B$ is higher than $A$, then $\Phi_B>\Phi_A$ and the received frequency is lower than the emitted frequency.

Pulse interpretation:

> Redshift is a mismatch between pulse counters at different gravitational potentials.

---

### 5.10 Gravitationally induced quantum interference: COW phase

The Colella-Overhauser-Werner neutron interferometry experiment observed a gravitationally induced quantum phase shift. The Pulse Model reproduces the phase shift directly.

For a nonrelativistic particle in uniform gravity,

$$
L = \frac{1}{2}mv^2 - mgz
$$

The phase along a path is

$$
\Theta = \frac{1}{\hbar}\int L\,dt
$$

Consider two horizontal path segments of length $L_h$, separated by height $H$, with speed $v$. The signed phase depends on which path is taken as the reference and on loop orientation; the benchmark magnitude is convention-independent. The area is

$$
A = H L_h
$$

The potential energy difference is

$$
\Delta U = mgH
$$

The time across the horizontal segment is

$$
T=\frac{L_h}{v}
$$

The phase difference from the potential term is

$$
\Delta\Theta = -\frac{1}{\hbar}\Delta U\,T = -\frac{mgH}{\hbar}\frac{L_h}{v}
$$

So

$$
|\Delta\Theta| = \frac{mgA}{\hbar v}
$$

Pulse interpretation:

> Gravity shifts the relative phase/pulse accumulation of matter waves along different height paths.

This is not only a clock effect. It is a quantum phase effect.

---

### 5.11 Equivalence principle as pulse universality

Weak equivalence principle:

> Freely falling test bodies follow the same trajectories independent of composition.

Pulse version:

> All ideal matter-wave phase accumulators see the same pulse-count metric.

From the Newtonian weak-field derivation:

$$
L=\frac{1}{2}mv^2-m\Phi
$$

The equation of motion is

$$
m\mathbf{a}=-m\nabla\Phi
$$

so mass cancels:

$$
\mathbf{a}=-\nabla\Phi
$$

Pulse interpretation:

> Different masses carry different phase density, but the same metric gradient. The phase scale changes; the stationary path does not.

---

### 5.12 Stress-energy as matter phase-response

In GR, matter stress-energy is defined by variation of the matter action:

$$
T_{\mu\nu} = -\frac{2}{\sqrt{-g}} \frac{\delta S_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

Since

$$
S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}
$$

we get

$$
T_{\mu\nu} = -\frac{2\hbar}{\sqrt{-g}} \frac{\delta \Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

This is a crucial bridge.

Pulse interpretation:

> Stress-energy is the sensitivity of matter phase accumulation to changes in the pulse-count metric.

This reframes "matter tells spacetime how to curve":

> Matter phase-response tells the pulse-count metric how it must adjust.

This does not yet derive Einstein's field equations, but it identifies the exact mathematical seam where matter phase and geometry interact.

---

### 5.13 Einstein equation as stationary phase balance

The Einstein-Hilbert action is

$$
S_{\mathrm{EH}}=\frac{c^3}{16\pi G}\int(R-2\Lambda)\sqrt{-g}\,d^4x
$$

Total action:

$$
S_{\mathrm{total}}=S_{\mathrm{EH}}+S_{\mathrm{m}}
$$

The classical field equation follows from

$$
\delta S_{\mathrm{total}}=0
$$

Variation with respect to $g^{\mu\nu}$ gives

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}
$$

In phase form:

$$
\Theta_{\mathrm{total}}=\frac{S_{\mathrm{EH}}+S_{\mathrm{m}}}{\hbar}
$$

and

$$
\delta\Theta_{\mathrm{total}}=0
$$

Pulse interpretation:

> Classical spacetime is the stationary phase configuration of geometry plus matter.

This is already how semiclassical path-integral reasoning points toward GR: in a path integral over geometries,

$$
Z=\int\mathcal{D}g\,\mathcal{D}\psi\,\exp\left(\frac{i}{\hbar}\left[S_{\mathrm{EH}}[g]+S_{\mathrm{m}}[g,\psi]\right]\right)
$$

classical geometry appears where the total phase is stationary.

The Pulse Model's speculative goal is to interpret or derive $S_{\mathrm{EH}}$ as the geometric phase-accounting cost required for consistent pulse comparisons.

---

### 5.14 Why scalar "clock speed" is not enough

A naive Pulse Model may say:

> Gravity is just a scalar field that changes local clock rate.

That is insufficient.

A scalar pulse-rate field can explain:

- gravitational time dilation
- Newtonian acceleration in weak fields
- part of gravitational redshift

But full GR requires a tensor metric $g_{\mu\nu}$. Reasons:

1. **Spatial curvature matters.** Light bending in GR depends on both temporal and spatial parts of the metric.
2. **Frame dragging requires off-diagonal metric components** such as $g_{0i}$.
3. **Gravitational waves are tensor perturbations**, not scalar pulse-rate ripples.
4. **Tidal curvature is direction-dependent.**
5. **Massless fields have $d\tau=0$** but still have phase and are affected by geometry.

Therefore the correct upgrade is:

> Gravity is not a scalar pulse-rate field. It is a tensorial pulse-count metric.

The model must use

$$
g_{\mu\nu}
$$

not merely a scalar clock-speed function.

---

### 5.15 Known-physics derivation audit

On June 7, 2026, the conservative derivations in section 5 were reviewed for dimensional consistency, signs, assumptions, and scope.

Conventions used by the audit:

- metric signature $(-,+,+,+)$
- coordinates with $x^0=ct$ when used
- Newtonian potential $\Phi=-GM/r$, with $\Phi\to0$ at infinity
- weak-field formulas keep terms through first order in $\Phi/c^2$ and $v^2/c^2$
- stress-energy is varied with respect to the inverse metric $g^{\mu\nu}$

| Benchmark | Audit result |
|---|---|
| SR time dilation | Dimensionally consistent. The sign gives fewer pulses for a moving clock in an inertial frame. |
| Schwarzschild time dilation | Consistent with $\Phi=-GM/r$ and the weak-field limit $d\tau/dt\approx1+\Phi/c^2$. |
| Weak-field gravity plus velocity | Correct to first order. Higher $\Phi$ increases pulse accumulation; higher $v$ decreases it. |
| Newtonian action | The rest-energy term is safely dropped for fixed coordinate-time endpoints, and Euler-Lagrange gives $\mathbf{a}=-\nabla\Phi$. |
| Geodesics | Stationary proper time gives the standard geodesic equation under the stated metric convention. |
| Redshift | The receiver/emitter convention is now explicit: $\Delta\nu/\nu_A\approx(\Phi_A-\Phi_B)/c^2$. |
| COW phase | The magnitude $mgA/(\hbar v)$ is dimensionless and standard; the sign is orientation-dependent. |
| Stress-energy | The phase-response identity follows directly from $S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}$ under the inverse-metric variation convention. |

No blocking correction remains in the written conservative derivations. The known-physics gate is still not accepted until the formulas are backed by executable benchmark checks.

---

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
`h2_acceptance_report.md` for the gate decision.

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

[The H7 appendix](./appendix/h7_vacuum_phase_response.md) accepts only a constrained reformulation. A pure bookkeeping phase has no source if it is not a metric functional, while a uniform covariant vacuum action density coupled through $\sqrt{-g}$ is metric-sensitive and is degenerate with a cosmological-constant term. The conservative gravitational object is the metric variation of the renormalized effective action.

This does not solve the cosmological-constant problem. H7 does not derive $\Lambda$, does not protect the observed value against radiative corrections, and does not predict a dark-energy equation of state.

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

## 8. Important insights produced by the model

### 8.1 Gravity as phase refraction

In optics, rays bend when phase velocity varies across space. In gravity, matter-wave phase accumulation varies across spacetime.

Weak-field matter phase rate:

$$
\frac{d\Theta}{dt}\approx -\frac{mc^2}{\hbar}-\frac{m\Phi}{\hbar}+\frac{mv^2}{2\hbar}
$$

Spatial variation in $\Phi$ changes phase accumulation. Stationary phase paths bend.

Pulse interpretation:

> Falling is matter-wave phase refraction through a non-uniform pulse-count metric.

---

### 8.2 Inertia as phase rigidity

Large mass means large rest phase rate:

$$
\omega_C = \frac{mc^2}{\hbar}
$$

A massive object's action changes rapidly for non-stationary path deviations. Nearby alternatives dephase strongly and cancel.

Pulse interpretation:

> Inertia is phase rigidity: larger mass makes the stationary path sharper.

### 8.3 Weight as constraint off the natural pulse path

In GR, free fall is inertial. Standing on Earth is accelerated because the ground prevents geodesic motion.

Pulse interpretation:

> Weight is the felt result of being forced away from the natural stationary pulse-count path.

### 8.4 Tides as pulse-gradient curvature

A uniform gravitational field can be transformed away locally by free fall. Tides remain because the gravitational gradient changes over space.

Pulse interpretation:

> Tidal gravity is curvature in the pulse-count metric: neighboring worldlines accumulate pulses differently in a way no local frame can remove.

### 8.5 Redshift as pulse-ratio mismatch

A photon emitted by a lower clock and received by a higher clock is compared against different local pulse counters.

Pulse interpretation:

> Redshift is not the photon "getting tired"; it is the receiver comparing the signal against a different local pulse rate.

### 8.6 Black hole horizon as pulse-comparison boundary

For a distant observer, clocks near a horizon appear infinitely redshifted. For the infalling observer, proper time remains finite.

Pulse interpretation:

> A horizon is a boundary where external pulse comparison degenerates, while local pulse accumulation remains finite along infalling paths.

This is useful but incomplete; inside the horizon the causal structure changes, so "slow time" language is not sufficient.

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

## 11. Codex agent workstreams

Each workstream should produce code, derivations, tests, and a short report.

### Agent A: Symbolic GR recovery

**Goal:** Verify that the Pulse Model reproduces standard relativistic clock and motion equations.

**Tasks:**

1. Implement symbolic proper-time functional.
2. Derive SR time dilation from Minkowski metric.
3. Derive Schwarzschild gravitational time dilation.
4. Derive weak-field combined expression:

   
$$
\frac{d\tau}{dt} \approx 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}
$$

5. Derive Newtonian action from relativistic action.
6. Derive Euler-Lagrange equations and recover:

   
$$
\mathbf{a}=-\nabla\Phi
$$

**Deliverables:**

- `derivations/sr_time_dilation.md`
- `derivations/weak_field_limit.md`
- `src/pulse_model/relativity.py`
- unit tests checking dimensional consistency and known numeric cases

**Acceptance criteria:**

- GPS-scale correction signs are correct.
- Circular orbit zero-dilation altitude calculation is reproduced.
- Symbolic derivations match standard formulas.

---

### Agent B: Quantum phase and interferometry

**Goal:** Build simulations of phase accumulation along alternative paths.

**Tasks:**

1. Implement path phase:

   
$$
\Theta = S/\hbar
$$

2. Simulate two-path phase difference in uniform gravity.
3. Reproduce COW phase:

   
$$
\Delta\Theta = \frac{mgA}{\hbar v}
$$

4. Simulate atom interferometer phases with laser pulses.
5. Compare phase view with proper-time view.

**Deliverables:**

- `src/pulse_model/phase.py`
- `notebooks/cow_phase.ipynb`
- `notebooks/atom_interferometer_phase.ipynb`
- numerical plots of phase versus area, mass, velocity, and gravity

**Acceptance criteria:**

- COW scaling matches literature.
- Phase is dimensionless.
- Classical stationary path emerges numerically from phase cancellation.

---

### Agent C: Quantum clock superposition simulator

**Goal:** Model a clock in a superposition of proper times.

**Tasks:**

1. Represent internal clock Hamiltonian $H_C$.
2. Evolve internal states along two worldlines:

   
$$
\lvert \chi_i \rangle=e^{-iH_C\tau_i/\hbar}\lvert \chi_0 \rangle
$$

3. Compute visibility:

   
$$
\mathcal{V} = \left| \mathrm{Tr} \left( \rho_C e^{-iH_C\Delta\tau/\hbar} \right) \right|
$$

4. Simulate pure two-level clocks.
5. Simulate thermal internal states.
6. Add gravitational height difference:

   
$$
\Delta\tau \approx \frac{gH}{c^2}T
$$

**Deliverables:**

- `src/pulse_model/quantum_clock.py`
- `notebooks/proper_time_superposition.ipynb`
- parameter sweeps for $H,T,\Delta E$

**Acceptance criteria:**

- Visibility equals 1 when $\Delta\tau=0$.
- Visibility oscillates for pure two-level states.
- Visibility decays for broad energy distributions.

---

### Agent D: Pulse universality tests

**Goal:** Parameterize and constrain deviations from metric universality.

**Tasks:**

1. Implement deviation model:

   
$$
\frac{dN_i}{dt} = f_i \left[ 1 + (1+\alpha_i)\frac{\Phi}{c^2} - (1+\beta_i)\frac{v^2}{2c^2} \right]
$$

2. Collect public clock comparison data.
3. Fit bounds on $\alpha_i,\beta_i$.
4. Compare with existing local position invariance and Lorentz-violation frameworks.

**Deliverables:**

- `src/pulse_model/universality.py`
- `data/clock_tests/`
- `reports/pulse_universality_bounds.md`

**Acceptance criteria:**

- Existing null results imply $\alpha_i,\beta_i$ consistent with zero.
- Code can forecast sensitivity of future clocks.

---

### Agent E: Pulse-network metric reconstruction

**Goal:** Infer metric components from synthetic clock/signal data.

**Tasks:**

1. Generate synthetic clock records in known spacetime.
2. Define pulse-record data structure:

   ```text
   clock_id
   event_id
   local_pulse_count
   emitted_signal_id
   received_signal_id
   signal_phase
   local_acceleration
   ```

3. Fit $g_{00}$ in weak static fields.
4. Fit full weak-field metric:

   
$$
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}
$$

5. Add loop holonomy analysis.

**Deliverables:**

- `src/pulse_model/network.py`
- `src/pulse_model/reconstruct_metric.py`
- `notebooks/metric_reconstruction.ipynb`

**Acceptance criteria:**

- Recover known gravitational potential from clock ratios.
- Recover synthetic gravitational wave perturbation from clock network residuals.
- Provide uncertainty estimates.

---

### Agent F: Stress-energy as phase-response

**Goal:** Formalize the identity

$$
T_{\mu\nu} = -\frac{2\hbar}{\sqrt{-g}} \frac{\delta \Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

for common fields.

**Tasks:**

1. Derive $T_{\mu\nu}$ for scalar field action.
2. Derive $T_{\mu\nu}$ for electromagnetic field action.
3. Derive point-particle stress-energy from worldline action.
4. Express each result in phase-response language.
5. Identify which components correspond to energy density, momentum flux, pressure, and stress.

**Deliverables:**

- `appendix/h4_stress_energy_as_phase_response.md`
- `tests/test_h4_stress_energy_phase_response.py`
- optional symbolic checks only if later work needs machine-checked variation algebra

**Acceptance criteria:**

- Standard stress-energy tensors are recovered.
- Units and signs are consistent.
- The phase-response interpretation handles pressure, not just mass density.

---

### Agent G: Geometry phase functional

**Goal:** Explore whether the Einstein-Hilbert action can be interpreted or derived as a pulse-consistency cost.

**Tasks:**

1. Start from standard:

   
$$
S_{\mathrm{EH}} = \frac{c^3}{16\pi G} \int(R-2\Lambda)\sqrt{-g}\,d^4x
$$

2. Express as phase:

   
$$
\Theta_{\mathrm{EH}}=S_{\mathrm{EH}}/\hbar
$$

3. Study dimensions in Planck units.
4. Investigate curvature as loop pulse-comparison holonomy.
5. Attempt derivation of $R\sqrt{-g}$ from local holonomy density.
6. Compare with Regge calculus and causal set discretizations.

**Deliverables:**

- `research/geometric_phase_cost.md`
- `notebooks/regge_pulse_cost.ipynb`
- candidate discrete action

**Acceptance criteria:**

- Reproduce Einstein-Hilbert action in continuum limit or clearly identify failure.
- Preserve diffeomorphism invariance or explain replacement symmetry.
- Avoid introducing preferred frame.

---

### Agent H: Quantum source / metric superposition

**Goal:** Model the relation between superposed matter phase histories and geometry.

**Tasks:**

1. Model matter source state:

   
$$
\lvert \psi \rangle=\alpha\lvert L \rangle+\beta\lvert R \rangle
$$

2. Compare three models:

   - semiclassical metric sourced by $\langle T_{\mu\nu}\rangle$
   - branch metric $\alpha\lvert g_L \rangle\lvert L \rangle+\beta\lvert g_R \rangle\lvert R \rangle$
   - collapse/decoherence model

3. Track pulse histories of probe clocks.
4. Predict entanglement/decoherence signatures.

**Deliverables:**

- `src/pulse_model/metric_superposition.py`
- `reports/superposed_source_models.md`

**Acceptance criteria:**

- Distinguish predictions between models.
- Identify experiments that can falsify each class.
- Keep assumptions explicit.

---

### Agent I: Black hole pulse model

**Goal:** Translate black hole clock behavior and horizon structure into pulse-history language.

**Tasks:**

1. Compute proper time for infalling observer in Schwarzschild spacetime.
2. Compute redshift for signals emitted near horizon.
3. Track pulse counts for static, orbiting, and infalling clocks.
4. Analyze horizon as breakdown of external pulse comparison.
5. Explore phase records and information flow.

**Deliverables:**

- `notebooks/black_hole_pulse_counts.ipynb`
- `reports/horizon_pulse_comparison.md`

**Acceptance criteria:**

- Correctly distinguish local finite proper time from distant infinite redshift.
- Avoid saying "time stops" as an absolute statement.
- Handle null geodesics and massless phase separately.

---

### Agent J: Literature and benchmark map

**Goal:** Keep the research grounded.

**Tasks:**

1. Build a bibliography of:
   - quantum clocks
   - problem of time
   - atom interferometry
   - gravitational redshift
   - quantum reference frames
   - semiclassical gravity
   - equivalence principle tests
   - clock networks
2. Map each paper to Pulse Model concepts.
3. Identify known no-go theorems and constraints.
4. Maintain a benchmark list of equations and experiments the model must reproduce.

**Deliverables:**

- `references/pulse_model_bibliography.bib`
- `reports/literature_map.md`
- `tests/benchmarks.md`

**Acceptance criteria:**

- Every speculative claim is tagged and sourced.
- Benchmarks are converted into executable tests where possible.

---

## 12. Suggested repository structure

```text
pulse-model/
  README.md
  docs/
    pulse_model_formalization.md
    assumptions.md
    glossary.md
  appendix/
    h1_time_is_relational_pulse_count.md
    h2_metric_reconstruction_from_pulse_comparisons.md
    h3_pulse_comparison_holonomy.md
    h4_stress_energy_as_phase_response.md
  src/
    pulse_model/
      __init__.py
      constants.py
      relativity.py
      phase.py
      quantum_clock.py
      universality.py
      network.py
      reconstruct_metric.py
      metric_superposition.py
  tests/
    test_h4_stress_energy_phase_response.py
  notebooks/
    cow_phase.ipynb
    atom_interferometer_phase.ipynb
    proper_time_superposition.ipynb
    metric_reconstruction.ipynb
    black_hole_pulse_counts.ipynb
  data/
    clock_tests/
    experiments/
  reports/
    pulse_universality_bounds.md
    superposed_source_models.md
    horizon_pulse_comparison.md
    literature_map.md
  tests/
    test_units.py
    test_sr.py
    test_weak_field.py
    test_phase.py
    test_clock_visibility.py
    benchmarks.md
  references/
    pulse_model_bibliography.bib
```

---

## 13. Minimal computational API

The first implementation should expose these pure functions.

```python
def proper_time_flat(dt: float, v: float, c: float) -> float:
    """Return proper time for inertial motion in flat spacetime."""
    ...

def weak_field_dtaudt(phi: float, v: float, c: float) -> float:
    """Return dτ/dt in weak gravity and low velocity."""
    ...

def pulse_count(frequency: float, proper_time: float) -> float:
    """Return accumulated pulse count."""
    ...

def free_massive_phase(mass: float, proper_time: float, c: float, hbar: float) -> float:
    """Return free massive action phase."""
    ...

def gravitational_redshift(phi_emit: float, phi_recv: float, c: float) -> float:
    """Return weak-field fractional frequency shift."""
    ...

def cow_phase_shift(mass: float, gravity: float, area: float, velocity: float, hbar: float) -> float:
    """Return COW gravitational phase shift."""
    ...

def clock_visibility(delta_tau: float, energy_levels: list[float], probabilities: list[float], hbar: float) -> float:
    """Return internal-clock path visibility."""
    ...
```

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

## 19. References and starting sources

These are not exhaustive. They are starting anchors for agents.

### Core action/phase bridge

- Feynman Lectures, Vol. II, Ch. 19, "The Principle of Least Action": https://www.feynmanlectures.caltech.edu/II_19.html
- Path integral formulation overview: https://en.wikipedia.org/wiki/Path_integral_formulation

### GR and Einstein field equations

- MIT OCW, "Einstein's Field Equations": https://ocw.mit.edu/courses/8-033-relativity-fall-2006/02415213222b845bbec6e734c64d1718_fieldeqs.pdf
- MIT OCW 8.962, Lecture 12, "The Einstein Field Equation": https://ocw.mit.edu/courses/8-962-general-relativity-spring-2020/resources/lecture-12-the-einstein-field-equation/
- Stanford Gravity Probe B, "Einstein's Spacetime": https://einstein.stanford.edu/SPACETIME/spacetime2.html

### Atomic clocks and gravitational time dilation

- NIST/JILA, "JILA Atomic Clocks Measure Einstein's General Relativity at Millimeter Scale": https://www.nist.gov/news-events/news/2022/02/jila-atomic-clocks-measure-einsteins-general-relativity-millimeter-scale
- NIST educational page, "Einstein's General Relativity and Your Age": https://www.nist.gov/education/resources-for-parents%2C-teachers-and-students/einsteins-general-relativity-and-your-age

### Gravitational quantum phase

- Colella, Overhauser, Werner, "Observation of Gravitationally Induced Quantum Interference", Physical Review Letters 34, 1472 (1975): https://link.aps.org/doi/10.1103/PhysRevLett.34.1472
- Pound and Rebka, "Apparent Weight of Photons", Physical Review Letters 4, 337 (1960): https://fisica.unipv.it/percorsi/pdf/rebka_1960.pdf

### Quantum clocks and problem of time

- Altaie, Hodgson, Beige, "Time and Quantum Clocks: a review of recent developments", Frontiers in Physics / arXiv:2203.12564: https://arxiv.org/abs/2203.12564
- Gambini, Porto, Pullin, "A relational solution to the problem of time in quantum mechanics and quantum gravity induced by a fundamental mechanism for quantum decoherence", arXiv:gr-qc/0402118: https://arxiv.org/abs/gr-qc/0402118
- Gryb, Thébault, "The role of time in relational quantum theories", arXiv:1110.2429: https://arxiv.org/abs/1110.2429

### Quantum clocks, time dilation, and entanglement

- Pikovski, Zych, Costa, Brukner, "Universal decoherence due to gravitational time dilation", Nature Physics 11, 668-672 (2015): https://ucrisportal.univie.ac.at/de/publications/universal-decoherence-due-to-gravitational-time-dilation/
- Castro-Ruiz, Giacomini, Brukner, "Entanglement of quantum clocks through gravity", PNAS 114, E2303-E2309 (2017): https://pmc.ncbi.nlm.nih.gov/articles/PMC5373405/
- Meltzer et al., "Atomic clock interferometry using optical tweezers", Physical Review A 110, 032602 (2024): https://ui.adsabs.harvard.edu/abs/2024PhRvA.110c2602M/abstract
- Giacomini, "Spacetime Quantum Reference Frames and superpositions of proper times", Quantum 5, 508 (2021): https://quantum-journal.org/papers/q-2021-07-22-508/

### Equivalence principle tests

- Touboul et al., "MICROSCOPE mission: final results of the test of the Equivalence Principle", arXiv:2209.15487: https://arxiv.org/abs/2209.15487
- Touboul et al., "Result of the MICROSCOPE Weak Equivalence Principle test", arXiv:2209.15488: https://arxiv.org/abs/2209.15488

### Emerging quantum-clock / curved-spacetime proposals

- "Probing curved spacetime with a distributed atomic processor", arXiv:2502.12954: https://arxiv.org/html/2502.12954v1
- Gündoğan, Barzel, Rätzel, "Gravitational time dilation in quantum clock interferometry with entangled multi-photon states and quantum memories", arXiv:2601.02470: https://arxiv.org/abs/2601.02470
- Balsells, "Geometry and proper time of a relativistic quantum clock", arXiv:2410.08156: https://arxiv.org/abs/2410.08156

### Cosmology / dark sector context

- CERN, "Dark matter": https://home.cern/science/physics/dark-matter/
- Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", arXiv:1807.06209: https://arxiv.org/abs/1807.06209
- DESI / Lawrence Berkeley National Laboratory, "New DESI Results Strengthen Hints That Dark Energy May Evolve": https://newscenter.lbl.gov/2025/03/19/new-desi-results-strengthen-hints-that-dark-energy-may-evolve/
- Khalife et al., "Review of Hubble tension solutions with new SH0ES and SPT-3G data", arXiv:2312.09814: https://arxiv.org/html/2312.09814v2

---

## 20. Immediate next actions

For the formal proof order, dependency gates, progress status vocabulary, and current queue, use `proof_sequence.md` as the source of truth.

The current next work is no longer the original agent-order sketch. H1 through H7 and the known-physics recovery ladder now have accepted-with-limits artifacts, so downstream work should start from the proof ledger rather than this early planning list.

At the current gate, H7 should be used only in its accepted constrained sense: it separates absolute bookkeeping phase from covariant renormalized response, but it does not derive $\Lambda$, solve vacuum-energy naturalness, or predict dark-energy evolution. New downstream work should follow `proof_sequence.md`, preserving the caveats attached to 05, 05S, H6, and H7.

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
