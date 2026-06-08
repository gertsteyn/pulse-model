---
title: Known-Physics Recovery
sidebar_label: Known-Physics Recovery
sidebar_position: 3
---

# Known-Physics Recovery

This page preserves the known-physics recovery section from the original formalization. It should be read with the evidence report at [Known-physics validation](../evidence/known_physics_validation.md).

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
