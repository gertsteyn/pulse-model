---
title: H1 Time Is Relational Pulse Count
sidebar_label: H1 Time
sidebar_position: 2
---

# Appendix: Hypothesis H1 - Time Is Relational Pulse Count

**Parent hypothesis:** 6.1 Hypothesis H1: Time is relational pulse count  
**Status:** Accepted with limits for the conservative single-clock, single-time theorem  
**Purpose:** Prove the bounded claim that ordinary single-time predictions can be rewritten as conditional predictions against an ideal physical pulse counter, while keeping stronger relational-time claims out of scope.

## Purpose

Hypothesis H1 states that time should not enter the fundamental description as an external background parameter. Temporal statements should instead be expressed as correlations between physical pulse counters and system observables.

The main formalization states this as:

$$
P(O=o \mid N_C=n)
$$

rather than:

$$
P(O=o,t)
$$

This appendix defines the proof target, proves the conservative single-clock ideal theorem, and separates that theorem from the stronger open research claims.

## What A Proof Must Establish

H1 is not proved by saying that clocks measure time. That would leave external time intact and only describe how an instrument reports it.

The stronger claim is:

> Every single-time observable prediction can be reformulated as a conditional relation between a physical clock's pulse count and the rest of the system, with ordinary time-parametrized physics recovered when the chosen clock is ideal.

A conservative proof should establish equivalence with single-time Born predictions and relativistic clock behavior in the appropriate limit. A stronger proof would show that external time is a redundant gauge-like parameter rather than a primitive physical input.

## Target Theorem

For a clock $C$ and a system observable $O$, first define the relational probability for a finite clock readout event $A_C$:

$$
P_{\mathrm{rel}}(O=o \mid A_C)=\frac{\mathrm{Tr}_{CS}[(E_C(A_C)\otimes E_O(o))\rho_{CS}]}{\mathrm{Tr}_{CS}[(E_C(A_C)\otimes I_S)\rho_{CS}]}
$$

Here $E_C(A_C)$ is the clock readout effect, $E_O(o)$ is the system observable effect, and $\rho_{CS}$ is the joint clock-system state.

For a discrete pulse counter, $A_C$ may be the event $N_C=n$. For a continuous ideal clock, $A_C$ must be a finite readout window $W_n$ around the calibrated clock reading $\tau_n=n/f_C$, or else a conditional-density limit. A continuous point reading is not an ordinary finite-probability event.

The proof target is:

$$
\left|P_{\mathrm{rel}}(O=o \mid W_n)-P_{\mathrm{std}}(O=o;t=n/f_C)\right|\leq\epsilon_C(O,o,n)
$$

where $f_C$ is the clock's calibrated local pulse frequency and $\epsilon_C(O,o,n)$ vanishes in the ideal-clock limit.

Equivalently, for a sufficiently ideal clock, conditioning on pulse count $n$ must recover the same predictions as ordinary evolution at:

$$
\tau_C = n/f_C
$$

The proof must then show that $\tau_C$ is not a new universal time. It is only the calibrated proper-time variable associated with clock $C$.

## Minimal Formal Ingredients

A proof needs these objects.

1. A clock Hilbert space $\mathcal{H}_C$.
2. A system Hilbert space $\mathcal{H}_S$.
3. A physical joint state $\rho_{CS}$ or $|\Psi\rangle$.
4. A clock pulse-count readout POVM or spectral measure $E_C(A_C)$ over readout events. In the discrete case:

$$
\sum_n E_C(n)=I_C
$$

In the continuous ideal-clock model, finite windows replace point events:

$$
E_C(W_n)=\int_{W_n}d\tau |\tau\rangle_C\langle\tau|_C
$$

5. A system observable POVM $E_O(o)$ satisfying:

$$
\sum_o E_O(o)=I_S
$$

6. A clock calibration rule:

$$
n = f_C \tau_C
$$

7. A rule for physical admissibility that does not depend on an observable external time.

When a conditional system state is needed, the proof must also specify a measurement operator or instrument for the clock readout. A POVM effect fixes probabilities, but it does not by itself uniquely fix the post-readout system state.

For the ideal Page-Wootters-style construction, the admissibility rule can be a stationary constraint:

$$
H_{\mathrm{tot}}|\Psi\rangle=0
$$

with:

$$
H_{\mathrm{tot}}=H_C+H_S
$$

Interactions and curved-spacetime corrections can be added later. The proof below begins with the noninteracting ideal-clock case.

## Conservative H1 Theorem

This section proves the conservative single-clock version of H1.

It proves that an idealized pulse counter can replace the external time parameter in single-time ordinary quantum predictions, in the precise sense that conditioning on the clock's pulse count gives the same Born probabilities as standard Schrödinger evolution in the sharp-readout limit.

It does not prove the stronger quantum-gravity claim that spacetime geometry itself emerges from pulse comparisons. That stronger claim belongs to H2 and later hypotheses.

### Assumptions

Assume an ideal clock-system split:

$$
\mathcal{H}_{CS}=\mathcal{H}_C\otimes\mathcal{H}_S
$$

The clock has generalized readout states $|\tau\rangle_C$ satisfying:

$$
\langle\tau|\tau'\rangle=\delta(\tau-\tau')
$$

and:

$$
\int d\tau |\tau\rangle_C\langle\tau|_C=I_C
$$

The clock Hamiltonian generates translations of the clock readout:

$$
e^{-iH_C a/\hbar}|\tau\rangle_C=|\tau+a\rangle_C
$$

Equivalently, for any joint history state $|\Phi\rangle$:

$$
{}_C\langle\tau|H_C|\Phi\rangle=-i\hbar\frac{\partial}{\partial\tau}{}_C\langle\tau|\Phi\rangle
$$

This is a mathematical idealization. A clock with a perfectly translation-covariant readout over the full real line requires an ideal generator and is not a claim that real clocks have exact sharp time states or an exactly unbounded physical energy spectrum. Real clocks are treated as finite-resolution approximations to this model.

The system has Hamiltonian $H_S$. In the first proof there is no clock-system interaction:

$$
H_{\mathrm{tot}}=H_C+H_S
$$

For the proof below, assume $\mathcal{H}_S$ is finite-dimensional. Then $H_S$ and all observable effects $E_O(o)$ are bounded. Infinite-dimensional systems require corresponding boundedness and domain assumptions before the same limit and error-bound steps are valid.

Physical joint histories satisfy the stationary constraint:

$$
H_{\mathrm{tot}}|\Psi\rangle=0
$$

The clock has stable pulse frequency $f_C$, so the clock's pulse count and local clock reading are related by:

$$
n=f_C\tau_C
$$

The ideal proof treats $\tau_C$ as continuous. A discrete pulse counter is recovered by sampling at:

$$
\tau_n=n/f_C
$$

### Theorem Statement

Let $\rho_S(0)$ be the system state at clock reading $0$. Define:

$$
U_S(\tau)=\exp(-iH_S\tau/\hbar)
$$

and:

$$
\rho_S(\tau)=U_S(\tau)\rho_S(0)U_S(\tau)^\dagger
$$

For a finite continuous clock readout, let $W_n$ be the readout window:

$$
W_n=[\tau_n-\Delta\tau/2,\tau_n+\Delta\tau/2]
$$

centered at:

$$
\tau_n=n/f_C
$$

with width $\Delta\tau$. In the ideal clock model:

$$
E_C(W_n)=\int_{W_n}d\tau |\tau\rangle_C\langle\tau|_C
$$

Then the finite-window relational probability approaches the standard Born prediction:

$$
\lim_{\Delta\tau\to0}P_{\mathrm{rel}}(O=o \mid C\in W_n)=\mathrm{Tr}_S[E_O(o)U_S(n/f_C)\rho_S(0)U_S(n/f_C)^\dagger]
$$

This is exactly the ordinary prediction:

$$
P_{\mathrm{std}}(O=o;t=n/f_C)
$$

after the external parameter $t$ is replaced by the clock's calibrated pulse count.

For a discrete counter obtained by sampling this ideal continuous clock, the same statement holds at the sampled readout $n$ with:

$$
U_S(n)=\exp(-iH_S n/(\hbar f_C))
$$

A standalone discrete-clock proof would use a discrete history state and a shift generator on the clock readout lattice. This appendix proves the sampled ideal-clock version.

### Proof

First prove the statement for a pure initial system state $|\psi_0\rangle_S$. The mixed-state result follows by linearity.

Let $|\Psi\rangle$ be a physical joint history satisfying:

$$
H_{\mathrm{tot}}|\Psi\rangle=0
$$

Define the conditional system vector at clock reading $\tau$ by projection onto the clock readout:

$$
|\psi(\tau)\rangle_S={}_C\langle\tau|\Psi\rangle
$$

Strictly, an ideal clock over an infinite readout range gives generalized states. One may either work in a rigged-Hilbert-space sense or restrict the clock to a large finite interval and then take conditional probabilities. The conditional ratios below are independent of the overall history normalization.

Project the stationary constraint onto a clock reading:

$$
{}_C\langle\tau|(H_C+H_S)|\Psi\rangle=0
$$

Using the clock-generator assumption:

$$
{}_C\langle\tau|H_C|\Psi\rangle=-i\hbar\frac{\partial}{\partial\tau}|\psi(\tau)\rangle_S
$$

Therefore the constraint becomes:

$$
-i\hbar\frac{\partial}{\partial\tau}|\psi(\tau)\rangle_S+H_S|\psi(\tau)\rangle_S=0
$$

Rearranging gives:

$$
i\hbar\frac{\partial}{\partial\tau}|\psi(\tau)\rangle_S=H_S|\psi(\tau)\rangle_S
$$

This is the Schrödinger equation, but $\tau$ is the physical clock readout label, not an external time parameter.

Given the boundary condition:

$$
|\psi(0)\rangle_S=|\psi_0\rangle_S
$$

the unique solution is:

$$
|\psi(\tau)\rangle_S=U_S(\tau)|\psi_0\rangle_S
$$

Equivalently, the corresponding history can be represented as:

$$
|\Psi\rangle=\int d\tau |\tau\rangle_C U_S(\tau)|\psi_0\rangle_S
$$

Now condition on a finite clock readout window $W_n$. The clock effect is:

$$
E_C(W_n)=\int_{W_n}d\tau |\tau\rangle_C\langle\tau|_C
$$

The unnormalized conditional system state is:

$$
\tilde{\rho}_S(W_n)=\int_{W_n}d\tau |\psi(\tau)\rangle_S\langle\psi(\tau)|_S
$$

If $|\psi_0\rangle_S$ is normalized, unitarity gives:

$$
\langle\psi(\tau)|\psi(\tau)\rangle=1
$$

so the window normalization is:

$$
Z(W_n)=\int_{W_n}d\tau=\Delta\tau
$$

and the normalized conditional state is:

$$
\rho_S(W_n)=\frac{1}{\Delta\tau}\int_{W_n}d\tau |\psi(\tau)\rangle_S\langle\psi(\tau)|_S
$$

For an observable effect $E_O(o)$, the finite-window relational Born probability is:

$$
P_{\mathrm{rel}}(O=o \mid C\in W_n)=\mathrm{Tr}_S[E_O(o)\rho_S(W_n)]
$$

Substitute the solution:

$$
P_{\mathrm{rel}}(O=o \mid C\in W_n)=\frac{1}{\Delta\tau}\int_{W_n}d\tau \mathrm{Tr}_S[E_O(o)U_S(\tau)\rho_S(0)U_S(\tau)^\dagger]
$$

Define:

$$
F_{O,o}(\tau)=\mathrm{Tr}_S[E_O(o)U_S(\tau)\rho_S(0)U_S(\tau)^\dagger]
$$

Under the finite-dimensional assumption above, $F_{O,o}$ is differentiable with bounded derivative on every finite readout window.

If $F_{O,o}$ is continuous at:

$$
\tau_n=n/f_C
$$

then:

$$
\lim_{\Delta\tau\to0}P_{\mathrm{rel}}(O=o \mid C\in W_n)=F_{O,o}(\tau_n)
$$

Therefore:

$$
\lim_{\Delta\tau\to0}P_{\mathrm{rel}}(O=o \mid C\in W_n)=\mathrm{Tr}_S[E_O(o)U_S(n/f_C)\rho_S(0)U_S(n/f_C)^\dagger]
$$

This is the same expression standard quantum mechanics writes as the Born probability at time $t=n/f_C$.

When the appendix writes $P_{\mathrm{rel}}(O=o \mid N_C=n)$ for a continuous ideal clock, that is only shorthand for this sharp-window limit or for the corresponding conditional probability density. The precise continuous statement uses $W_n$.

Thus, under the ideal-clock assumptions, external time can be replaced by relational conditioning on pulse count for single-time Born predictions without changing the observable prediction in the sharp-readout limit.

The finite-window error can be bounded. If:

$$
M_{O,o,n}=\sup_{\tau\in W_n}\left|\frac{dF_{O,o}}{d\tau}(\tau)\right|
$$

then:

$$
\left|P_{\mathrm{rel}}(O=o \mid C\in W_n)-F_{O,o}(\tau_n)\right|\leq M_{O,o,n}\Delta\tau/2
$$

Thus the theorem's correction can be taken as:

$$
\epsilon_C(O,o,n)=M_{O,o,n}\Delta\tau/2
$$

for this finite-window ideal-clock model. The derivative bound exists under the finite-dimensional assumption stated above.

### Pulse-Count Schrödinger Equation

Because:

$$
\tau=n/f_C
$$

the derivative transforms as:

$$
\frac{\partial}{\partial\tau}=f_C\frac{\partial}{\partial n}
$$

The recovered Schrödinger equation becomes:

$$
i\hbar f_C\frac{\partial}{\partial n}|\psi(n)\rangle_S=H_S|\psi(n)\rangle_S
$$

For a discrete counter, one pulse advances the conditional state by:

$$
|\psi_{n+1}\rangle_S=\exp(-iH_S/(\hbar f_C))|\psi_n\rangle_S
$$

The continuous pulse-count equation is the high-resolution limit of this exact discrete update.

### Mixed-State Extension

Let:

$$
\rho_S(0)=\sum_k p_k|\psi_k\rangle\langle\psi_k|
$$

For each component, define:

$$
|\Psi_k\rangle=\int d\tau |\tau\rangle_C U_S(\tau)|\psi_k\rangle_S
$$

and the mixed history:

$$
\rho_{CS}=\sum_k p_k|\Psi_k\rangle\langle\Psi_k|
$$

Each $|\Psi_k\rangle$ satisfies the stationary constraint in the same generalized sense as the pure-state proof, so the mixed history satisfies the constraint componentwise.

For a finite clock window $W_n$, conditioning gives:

$$
\rho_S(W_n)=\frac{1}{\Delta\tau}\int_{W_n}d\tau U_S(\tau)\rho_S(0)U_S(\tau)^\dagger
$$

Taking the sharp-window limit gives:

$$
\rho_S(n)=U_S(n/f_C)\rho_S(0)U_S(n/f_C)^\dagger
$$

and therefore, in that sharp-window limit:

$$
\lim_{\Delta\tau\to0}P_{\mathrm{rel}}(O=o \mid C\in W_n)=\mathrm{Tr}_S[E_O(o)\rho_S(n)]
$$

So the theorem holds for arbitrary density matrices on the finite-dimensional system Hilbert space assumed above.

### Clock-Choice Corollary

Now compare two ideal co-located clocks $C$ and $D$ with frequencies $f_C$ and $f_D$.

Their pulse counts satisfy:

$$
n_C=f_C\tau
$$

and:

$$
n_D=f_D\tau
$$

If their central readouts satisfy:

$$
n_C/f_C=n_D/f_D
$$

then both central readings refer to the same local proper-time reading $\tau$.

For continuous readouts, exact finite-window equality requires matched proper-time windows. Let:

$$
W=[\tau-\Delta\tau/2,\tau+\Delta\tau/2]
$$

and let each clock's readout event correspond to that same window $W$ after calibration. Then both clocks define the same conditional state:

$$
\rho_S^C(W)=\rho_S^D(W)=\frac{1}{\Delta\tau}\int_W d\tau' U_S(\tau')\rho_S(0)U_S(\tau')^\dagger
$$

and hence:

$$
P(O=o \mid C\in W)=P(O=o \mid D\in W)
$$

For discrete readouts or unmatched finite bins, equality is exact only when the calibrated proper-time windows match. Otherwise the two clocks differ by the finite-resolution errors of their respective bins, and the equality is recovered in the sharp-readout limit.

No clock species is preferred. Different ideal pulse counters are merely different calibrations of the same local proper-time correlation once their readouts are compared as proper-time windows.

### Relativistic Consistency Corollary

For a clock following worldline $\gamma_C$, pulse count is:

$$
N_C[\gamma_C]=\int_{\gamma_C} f_C d\tau_C
$$

with:

$$
d\tau_C=\frac{1}{c}\sqrt{-g_{\mu\nu}dx^\mu dx^\nu}
$$

The quantity $d\tau_C$ is invariant under coordinate transformations. Therefore $N_C[\gamma_C]$ is an operational scalar for an ideal clock with fixed local frequency $f_C$.

If two identical clocks depart from event $A$, follow worldlines $\gamma_1$ and $\gamma_2$, and reunite at event $B$, then:

$$
\Delta N_C=f_C(\tau[\gamma_1]-\tau[\gamma_2])
$$

This is the standard relativistic clock-comparison result. H1 therefore preserves special-relativistic and general-relativistic proper-time behavior in the ideal-clock limit.

### Simple Resolution-Smearing Model

Real clocks do not project sharply onto one value of $\tau$. The following is a simple classical readout-smearing model, not a general finite-clock theorem. It captures finite resolution only; it does not include coherent clock-system measurement effects, entanglement generated by the readout, clock backreaction, or clock Hamiltonian imperfections.

The executable toy model treats the pulse counter as a nonnegative readout. Its uniform finite windows therefore must satisfy:

$$
n-\Delta n/2\ge 0
$$

The analytic ideal-clock expressions may instead be recentered or restricted to any interval where the readout kernel has support inside the modeled clock domain.

Model a finite clock readout $n$ by a response kernel $K_n(\tau)$ centered at:

$$
\tau_n=n/f_C
$$

For the uniform ideal history used above, this model gives the clock-resolution average:

$$
\rho_S^{K}(n)=\frac{\int d\tau K_n(\tau)\rho_S(\tau)}{\int d\tau K_n(\tau)}
$$

Assume the kernel is normalized, symmetric, and has variance $\sigma_\tau^2$. Expanding around $\tau_n$ gives:

$$
\rho_S^{K}(n)=\rho_S(\tau_n)+\frac{\sigma_\tau^2}{2}\frac{\partial^2\rho_S}{\partial\tau^2}(\tau_n)+\mathcal{O}(\sigma_\tau^4/T_S^4)
$$

Here $T_S$ is the shortest system timescale on which $\rho_S(\tau)$ changes appreciably. The fourth-order remainder assumes a symmetric scaled kernel with finite fourth moment.

Since:

$$
\frac{\partial\rho_S}{\partial\tau}=-\frac{i}{\hbar}[H_S,\rho_S]
$$

the second derivative is:

$$
\frac{\partial^2\rho_S}{\partial\tau^2}=-\frac{1}{\hbar^2}[H_S,[H_S,\rho_S]]
$$

Therefore:

$$
\rho_S^{K}(n)=\rho_S(\tau_n)-\frac{\sigma_\tau^2}{2\hbar^2}[H_S,[H_S,\rho_S(\tau_n)]]+\mathcal{O}(\sigma_\tau^4/T_S^4)
$$

For any observable effect $E_O(o)$:

$$
P_K(O=o \mid N_C=n)=\mathrm{Tr}_S[E_O(o)\rho_S^{K}(n)]
$$

and:

$$
\lim_{\sigma_\tau\to 0}P_K(O=o \mid N_C=n)=P_{\mathrm{rel}}(O=o \mid N_C=n)
$$

The pulse-count resolution is:

$$
\sigma_\tau=\sigma_n/f_C
$$

so high-frequency, low-noise clocks recover the ideal theorem within this smearing model. The leading correction is energy-basis smearing from clock readout uncertainty.

For the executable two-level toy model in `src/pulse_model/h1_toy.py`, the measured probability is:

$$
P_1(\tau)=\sin^2(\omega\tau/2)
$$

The leading resolution correction is therefore:

$$
\Delta P_{\mathrm{res}}=\frac{\sigma_\tau^2\omega^2}{4}\cos(\omega\tau_n)
$$

For a uniform finite readout window of width $\Delta\tau$, the variance is:

$$
\sigma_\tau^2=\Delta\tau^2/12
$$

so:

$$
P_1^{K}(n)\approx P_1(\tau_n)+\frac{\Delta\tau^2\omega^2}{48}\cos(\omega\tau_n)
$$

The numerical test checks this expansion against the exact uniform-window average. The regime of validity is:

$$
\omega\Delta\tau\ll 1
$$

Equivalently, in pulse-count units:

$$
\omega\Delta n/f_C\ll 1
$$

The executable leading approximation enforces the conservative guard $\omega\Delta n/f_C\le 1$. Wider uniform windows should use the exact finite-window average rather than the leading correction formula.

### Other Finite-Clock Corrections

The resolution term above is universal enough to test in the single-clock toy model because it only requires a readout kernel. The other finite-clock effects require extra physical models. The honest first-order targets are:

| Correction | Leading target | Status in this appendix |
|---|---|---|
| Resolution | $\Delta P_{\mathrm{res}}=(\sigma_\tau^2/2)F''(\tau_n)$ | Derived and tested for the two-level toy model. |
| Frequency drift | $\Delta P_{\mathrm{drift}}\approx F'(\tau_n)\delta\tau_{\mathrm{drift}}$ | Target stated; needs a drift model for $f_C(\tau)$. |
| Clock decoherence | An added clock-channel term in the conditioned state | Open; requires a clock instrument or master equation. |
| Backreaction | First-order interaction correction from $H_{\mathrm{int}}$ | Open; requires a clock-system interaction Hamiltonian. |
| Gravitational uncertainty | $\Delta P_{\mathrm{grav}}\approx F'(\tau_n)\delta\tau_{\mathrm{grav}}$ plus smearing from variance | Target stated in weak-field form; needs a metric or potential uncertainty model. |

For slow frequency drift, write the actual clock frequency as:

$$
f_C(\tau)=f_0(1+\eta(\tau))
$$

The recorded pulse count is:

$$
n=f_0\int_0^\tau(1+\eta(s))ds
$$

If the data are analyzed using the nominal calibration $f_0$, then:

$$
\tau_{\mathrm{nom}}=n/f_0=\tau+\int_0^\tau\eta(s)ds
$$

To first order, the actual system proper time at nominal readout $\tau_{\mathrm{nom}}$ is shifted by:

$$
\delta\tau_{\mathrm{drift}}\approx-\int_0^{\tau_{\mathrm{nom}}}\eta(s)ds
$$

and any single-time probability $F(\tau)$ shifts by:

$$
\Delta P_{\mathrm{drift}}\approx F'(\tau_{\mathrm{nom}})\delta\tau_{\mathrm{drift}}
$$

For weak-field gravitational uncertainty, the clock-rate approximation is:

$$
d\tau\approx dt(1+\Phi/c^2-v^2/(2c^2))
$$

so uncertainty in the potential contributes:

$$
\delta\tau_{\mathrm{grav}}\approx\int \delta\Phi(t)dt/c^2
$$

This enters the same first-order bias formula and, if random, also produces a resolution-like variance term. A full correction requires specifying the probability law for $\delta\Phi$ and the clock path.

### What This Proof Establishes

The proof establishes:

- single-time Born predictions can be written as $P(O=o \mid N_C=n)$ in the discrete case or as a sharp-window limit in the continuous case
- the Schrödinger equation is recovered as conditional evolution with respect to clock pulse count
- standard single-time Born probabilities are recovered exactly in the ideal sharp-readout limit
- different ideal clock species agree after calibration
- relativistic proper-time clock comparisons are preserved
- simple finite readout resolution gives controlled corrections that vanish in the ideal limit
- drift and gravitational uncertainty have first-order bias targets, while decoherence and backreaction are explicitly left model-dependent

### Review Status

Status: accepted-with-limits for the conservative single-clock theorem.

The review accepts the theorem as a correct idealized recovery of single-time Born predictions under the assumptions stated above:

- the clock and system factorize as $\mathcal{H}_C\otimes\mathcal{H}_S$
- the clock is an ideal translation-covariant readout or a sampled approximation to one
- the total history satisfies $H_{\mathrm{tot}}|\Psi\rangle=0$ with $H_{\mathrm{tot}}=H_C+H_S$
- clock-system interactions, backreaction, drift, decoherence, and gravitational uncertainty are neglected
- the system Hilbert space is finite-dimensional, or corresponding domain and boundedness assumptions are supplied
- conditioning uses a finite clock event with nonzero denominator, not a zero-probability continuous point event
- clock-species comparisons use calibrated, matched proper-time windows

No required edits block use of this theorem as the H1 single-time starting point. The appendix already handles the main review risks: finite-window conditioning, discrete sampling as a sampled ideal-clock limit, clock calibration, relativistic proper-time behavior, and the distinction between the conservative theorem and stronger relational-time claims.

The executable toy model for the single-time slice is implemented in `src/pulse_model/h1_toy.py` and tested in `tests/test_h1_toy.py`. It checks the sharp-window recovery, finite-window average, and leading resolution correction for a two-level finite-dimensional system.

The H1 acceptance report below records exactly what level of H1 is accepted and what remains open.

### What This Proof Does Not Establish

The proof does not establish:

- that physically realizable clocks can be perfectly ideal
- that all interacting clock-system models reduce to this simple theorem
- that multi-time correlations or sequential measurement histories have been proved rather than targeted
- that Heisenberg-picture correlation functions have been proved rather than targeted
- that coherent clock readout effects, entanglement, and backreaction are negligible in real clocks
- that the metric can be reconstructed from pulse records
- that the Einstein-Hilbert action follows from pulse consistency
- that quantum gravity has been solved
- that external coordinate time is unnecessary in every practical calculation

The exact result is narrow and precise:

> In ordinary quantum mechanics with an idealized single clock, single-time Born predictions can be rewritten as conditional predictions indexed by that clock's calibrated pulse count.

That is the conservative proof of H1 established here.

## Sequential And Multi-Time Extension Target

The single-time theorem above is not enough for the full H1 gate. Ordinary quantum theory also predicts sequential measurement probabilities and multi-time correlation functions. Those are not determined by POVM effects alone. They require instruments because each readout changes, records, or at least conditions the later state.

This section states the formal target. It is not a completed proof.

### Required Instruments

A sequential H1 theorem must specify:

1. Clock readout instruments $\mathcal{R}_k(W_k)$ for each clock window $W_k$. These instruments must create durable records of clock readouts and must state their backreaction on the clock.
2. System instruments $\mathcal{J}_{a_k}^{(k)}$ for each measured system outcome $a_k$. Each $\mathcal{J}_{a_k}^{(k)}$ is a completely positive trace-nonincreasing map, and $\sum_{a_k}\mathcal{J}_{a_k}^{(k)}$ is trace preserving.
3. A record space or classical memory that stores the ordered outcomes and clock readouts.
4. A rule for conditioning on the whole record, with nonzero probability for the selected clock-readout sequence.
5. A calibration rule for each clock window:

$$
\tau_k=n_k/f_C
$$

The clock windows must be ordered and sufficiently separated:

$$
\tau_1<\tau_2<\cdots<\tau_m
$$

and:

$$
\tau_{k+1}-\tau_k
$$

must be large compared with the readout resolution unless the theorem explicitly handles overlapping clock events.

### Standard Sequential Target

Let:

$$
\mathcal{U}_{\Delta\tau}(\rho)=U_S(\Delta\tau)\rho U_S(\Delta\tau)^\dagger
$$

where:

$$
U_S(\Delta\tau)=\exp(-iH_S\Delta\tau/\hbar)
$$

For a sequence of ideal clock readings:

$$
\tau_k=n_k/f_C
$$

define:

$$
\Delta\tau_1=\tau_1
$$

and for $k>1$:

$$
\Delta\tau_k=\tau_k-\tau_{k-1}
$$

The standard sequential probability for outcomes $a_1,\ldots,a_m$ is:

$$
P_{\mathrm{std}}(a_1,\ldots,a_m;\tau_1,\ldots,\tau_m)=\mathrm{Tr}_S[\mathcal{J}_{a_m}^{(m)}\circ\mathcal{U}_{\Delta\tau_m}\circ\cdots\circ\mathcal{J}_{a_1}^{(1)}\circ\mathcal{U}_{\Delta\tau_1}(\rho_S(0))]
$$

Let the ordered clock-record event be:

$$
\mathcal{Q}_{\mathbf{W}}=(q_1\in W_1,\ldots,q_m\in W_m)_{\mathrm{rec}}
$$

where $q_k$ is the $k$th stored clock readout produced by the clock readout instruments $\mathcal{R}_1(W_1),\ldots,\mathcal{R}_m(W_m)$. This is a condition on the ordered record, not a simultaneous projection onto one clock value.

The relational H1 target is:

$$
\lim_{\Delta W_1,\ldots,\Delta W_m\to0}P_{\mathrm{rel}}(a_1,\ldots,a_m \mid \mathcal{Q}_{\mathbf{W}};\mathcal{R}_1,\ldots,\mathcal{R}_m)=P_{\mathrm{std}}(a_1,\ldots,a_m;\tau_1,\ldots,\tau_m)
$$

with:

$$
\tau_k=n_k/f_C
$$

Here $\Delta W_1,\ldots,\Delta W_m\to0$ means that every clock readout window shrinks in calibrated proper-time width while preserving the ordered record sequence.

This target must reduce to the single-time theorem when $m=1$. If one of the $\mathcal{J}_{a_k}^{(k)}$ is replaced by a no-op trace-preserving instrument, the corresponding marginal must agree with the standard prediction with that unobserved step removed.

### Multi-Time Correlation Target

Heisenberg-picture correlation functions are not automatically probabilities. Their operational meaning depends on the chosen ordering or measurement protocol. For a time-ordered noninvasive correlation target, define:

$$
A_k(\tau_k)=U_S(\tau_k)^\dagger A_k U_S(\tau_k)
$$

Then the target correlator is:

$$
C_{\mathrm{std}}(A_m,\ldots,A_1;\tau_m,\ldots,\tau_1)=\mathrm{Tr}_S[A_m(\tau_m)\cdots A_1(\tau_1)\rho_S(0)]
$$

The relational target is:

$$
\lim_{\Delta W_1,\ldots,\Delta W_m\to0}C_{\mathrm{rel}}(A_m,\ldots,A_1 \mid \mathcal{Q}_{\mathbf{W}};\mathcal{R}_1,\ldots,\mathcal{R}_m)=C_{\mathrm{std}}(A_m,\ldots,A_1;\tau_m,\ldots,\tau_1)
$$

This target is acceptable only after the ordering convention and clock-readout protocol are specified. Different measurement instruments can represent different physical experiments even when they share the same single-time POVM effects.

### Assumptions For The Sequential Target

The conservative sequential target assumes:

- the same ideal clock-system split as the single-time theorem
- finite-dimensional system Hilbert space, or equivalent domain assumptions
- no clock-system interaction except the explicitly modeled readout instruments
- calibrated monotonic clock readouts
- clock windows whose finite-width corrections are controlled by the finite-clock terms above
- ordered records that cannot be confused or overwritten
- system instruments that are the same instruments used in the standard comparison theory
- no hidden observable external time in the final conditional probabilities

### What Counts As Recovery

Sequential H1 recovery means:

- every finite sequence of specified standard instruments has a relational clock-conditioned probability with the same sharp-window limit
- the finite-window corrections vanish as all clock resolutions vanish
- marginalizing over unobserved outcomes agrees with the corresponding standard marginal
- the $m=1$ case reproduces the conservative single-time theorem
- clock species changes only reparametrize calibrated windows when the proper-time windows match
- multi-time correlators are recovered only for a stated ordering and readout protocol

This would still be conservative recovery. It would show that external time can be removed from a larger class of ordinary quantum predictions, but it would not by itself prove that clock choice is fully gauge-like or that spacetime geometry emerges from pulse records.

## H1 Acceptance Report

**Issue:** `sci-6q1.4`  
**Date:** June 7, 2026  
**Gate:** `01 H1 relational pulse time`

### Verdict

H1 is **accepted-with-limits at the conservative single-clock level**.

The accepted result is:

> Single-time ordinary quantum predictions for a finite-dimensional noninteracting system can be rewritten as conditional predictions indexed by a calibrated ideal pulse counter. In the sharp-readout limit, the relational probability matches the standard Born prediction at $\tau=n/f_C$.

This is enough to use H1 as a conservative starting point for later pulse-record and clock-network work. It is not a proof of the stronger claim that external time is fully gauge-like, that all sequential predictions have been reconstructed, or that spacetime geometry emerges from pulse records.

### Accepted Artifacts

Written derivations and formal targets:

- This appendix, especially the conservative H1 theorem, clock-choice corollary, relativistic consistency corollary, simple resolution-smearing model, and sequential/multi-time extension target.
- `pulse_model/roadmap.md`, Step 1, which records H1's current proof status and downstream boundary.

Executable artifacts:

- `src/pulse_model/h1_toy.py` implements a two-level pulse-conditioned model.
- `tests/test_h1_toy.py` checks sharp-window Born recovery, calibrated pulse-count indexing, finite-window averaging, leading resolution correction, convergence to sharp readout, domain and approximation guards, and validation errors.

Verification commands:

```bash
PYTHONPATH=src .venv/bin/python -m unittest tests.test_h1_toy
```

Targeted H1 verification result in this run: 10 tests passed under Python 3.14.

```bash
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests
```

Latest full-suite verification result in this run: 38 tests passed under Python 3.14.

The Docusaurus build also passed:

```bash
npm run build
```

### Status By Requirement

| Requirement | Status | Evidence |
|---|---|---|
| Single-time theorem reviewed for assumptions and domain issues | Accepted with limits | Review status above; assumptions are finite-dimensional system, ideal clock, stationary history, no clock-system interaction. |
| Finite readout windows handled explicitly | Accepted for symmetric readout kernels | Sharp-window theorem and resolution-smearing derivation. |
| Discrete pulse sampling handled explicitly | Accepted as sampled ideal-clock version | The theorem states $U(n)=\exp(-iH_S n/(\hbar f_C))$ for sampled pulse count. |
| Clock calibration explicit | Accepted | Calibration rule $\tau=n/f_C$ is used throughout the theorem and toy model. |
| Clock species agreement after calibration | Accepted for ideal matched proper-time windows | Clock-choice corollary. |
| Relativistic proper-time behavior preserved | Accepted in the ideal-clock limit | Relativistic consistency corollary. |
| Finite-clock corrections derived and tested | Partially accepted | Resolution correction is derived and tested; drift and gravitational uncertainty have first-order targets; decoherence and backreaction remain model-dependent. |
| Sequential and multi-time predictions | Target stated, not proved | Sequential/multi-time section defines instruments, assumptions, theorem target, and recovery criteria. |

### Remaining Open Claims

The following claims are not accepted as established H1 results:

- physically realizable clocks can be perfectly ideal
- arbitrary interacting clock-system models reduce to the simple single-clock theorem
- sequential measurement histories are recovered in full generality
- Heisenberg-picture correlators are recovered without specifying an ordering and readout protocol
- clock choice is fully gauge-like in the sense needed for strong relational time
- coherent clock readout effects, entanglement, decoherence, backreaction, and gravitational uncertainty are negligible in real clocks
- pulse counts reconstruct the metric, curvature, stress-energy coupling, or geometry action

### Gate Decision

The `01 H1 relational pulse time` gate is complete for the current proof-sequence purpose:

- accepted as a conservative single-clock, single-time equivalence result
- executable for a two-level finite-dimensional toy model, including finite-window and leading resolution-correction checks
- extended with a formal sequential/multi-time target, but not a proof of that stronger target

Downstream work may cite H1 as an accepted-with-limits conservative foundation. It must not cite H1 as a solved problem of time, a derivation of spacetime, or a proof that all external time has been eliminated from every practical calculation.

## Roadmap Step 1: Define Pulse Count Operationally

The first step is to make $N_C$ an observable readout, not a hidden parameter.

For an ideal clock transition with frequency $f_C$, the pulse count along the clock worldline is:

$$
N_C[\gamma]=\int_\gamma f_C d\tau
$$

In a quantum model, the clock readout must be represented by effects $E_C(n)$.

For a discrete counter:

$$
n\in\mathbb{Z}
$$

For a high-frequency or continuum approximation, one may use a calibrated variable:

$$
\tau_C=n/f_C
$$

The proof must specify the conditions under which $n$ can be treated as monotonic, readable, and stable over the experiment.

Required clock-quality assumptions:

- the readout is monotonic over the interval being modeled
- the transition frequency is stable enough that drift is below the target error
- the readout resolution is small compared with the system timescale
- clock-system backreaction is negligible at first order
- the clock has enough coherence to support the conditional description

These are not merely engineering details. They determine the correction term $\epsilon_C$.

## Roadmap Step 2: Replace External Time With Conditional Probability

The second step is to define the conservative single-time predictions as conditional probabilities, then extend the same strategy to richer temporal observables as a later task.

The relational probability is:

$$
P_{\mathrm{rel}}(O=o \mid A_C)=\frac{P(O=o,A_C)}{P(A_C)}
$$

In quantum form:

$$
P_{\mathrm{rel}}(O=o \mid A_C)=\frac{\mathrm{Tr}_{CS}[(E_C(A_C)\otimes E_O(o))\rho_{CS}]}{\mathrm{Tr}_{CS}[(E_C(A_C)\otimes I_S)\rho_{CS}]}
$$

This formula contains no observable external $t$. It uses only:

- a joint physical state
- a clock readout
- a system readout
- a conditionalization rule

The denominator must be nonzero:

$$
\mathrm{Tr}_{CS}[(E_C(A_C)\otimes I_S)\rho_{CS}]>0
$$

This condition means the clock readout event $A_C$ is physically realized within the modeled ensemble.

## Roadmap Step 3: Construct The Ideal Relational State

The third step is to show that a stationary joint state can encode ordinary system evolution.

Use an ideal clock basis $|\tau\rangle$ satisfying a covariance condition:

$$
e^{-iH_C a/\hbar}|\tau\rangle=|\tau+a\rangle
$$

An ideal relational history state can be written schematically as:

$$
|\Psi\rangle=\int d\tau |\tau\rangle_C |\psi(\tau)\rangle_S
$$

This is not a claim that all $\tau$ values occur in an external time. It is a compact representation of correlations between clock readings and system states.

The state must satisfy:

$$
(H_C+H_S)|\Psi\rangle=0
$$

Projecting this constraint onto the clock reading $|\tau\rangle_C$ should yield:

$$
i\hbar \frac{\partial}{\partial \tau}|\psi(\tau)\rangle_S=H_S|\psi(\tau)\rangle_S
$$

This is the key recovery result. The Schrödinger equation appears as the equation governing conditional system states indexed by clock readings.

## Roadmap Step 4: Convert Proper Time To Pulse Count

H1 specifically uses pulse count, not an abstract continuous clock variable. Therefore the proof must translate:

$$
\tau_C=n/f_C
$$

Substitution into the Schrödinger equation gives:

$$
i\hbar f_C \frac{\partial}{\partial n}|\psi(n)\rangle_S=H_S|\psi(n)\rangle_S
$$

For truly discrete pulses, the exact ideal update over one pulse is:

$$
|\psi_{n+1}\rangle_S=\exp(-iH_S/(\hbar f_C))|\psi_n\rangle_S
$$

The differential Schrödinger equation is recovered when the system changes slowly over one clock pulse:

$$
\|H_S\|/(\hbar f_C)\ll 1
$$

This step prevents the proof from silently replacing pulse count with an assumed continuum.

## Roadmap Step 5: Recover Standard Observable Predictions

The next step is to show that conditional states reproduce ordinary Born-rule predictions.

Define a clock readout operator $M_C(n)$ such that:

$$
E_C(n)=M_C(n)^\dagger M_C(n)
$$

For that readout instrument, define the conditional system state in the discrete case:

$$
\rho_S(n)=\frac{\mathrm{Tr}_C[(M_C(n)\otimes I_S)\rho_{CS}(M_C(n)^\dagger\otimes I_S)]}{\mathrm{Tr}_{CS}[(E_C(n)\otimes I_S)\rho_{CS}]}
$$

Then:

$$
P_{\mathrm{rel}}(O=o \mid N_C=n)=\mathrm{Tr}_S[E_O(o)\rho_S(n)]
$$

In the ideal limit, this must match:

$$
\rho_S(n)=U(n)\rho_S(0)U(n)^\dagger
$$

where:

$$
U(n)=\exp(-iH_S n/(\hbar f_C))
$$

For the conservative single-time theorem, this is the target recovery of ordinary time evolution as pulse-count-indexed conditional evolution.

## Roadmap Step 6: Show That Clock Choice Is A Calibration, Not A Preferred Time

H1 rejects a universal pulse. Different ideal clocks may have different local transition frequencies.

For clocks $C$ and $D$:

$$
n_C=f_C\tau
$$

$$
n_D=f_D\tau
$$

If both clocks are ideal, co-located, and calibrated against the same local proper time interval, then:

$$
n_C/f_C=n_D/f_D
$$

The proof must show that replacing $C$ with $D$ only reparametrizes the same conditional predictions when their readout events describe the same calibrated proper-time window:

$$
P(O=o \mid C\in W)=P(O=o \mid D\in W)
$$

In the sharp-readout limit this reduces to matching central readings:

$$
n_C/f_C=n_D/f_D
$$

This establishes that no particular clock species defines fundamental time.

## Roadmap Step 7: Recover Relativistic Proper-Time Behavior

The clock variable must be local and path-dependent.

For a clock following worldline $\gamma_C$:

$$
N_C[\gamma_C]=\int_{\gamma_C} f_C d\tau_C
$$

with:

$$
d\tau_C=\frac{1}{c}\sqrt{-g_{\mu\nu}dx^\mu dx^\nu}
$$

The proof must show that if two clocks separate and reunite, the conditional predictions depend on their accumulated proper times, not on coordinate time:

$$
\Delta N_C=f_C(\tau_1-\tau_2)
$$

This connects H1 to standard special-relativistic and general-relativistic clock comparisons.

## Roadmap Step 8: Prove Coordinate Invariance

A valid proof cannot depend on a coordinate label $t$.

Under a coordinate change:

$$
x^\mu\rightarrow x'^\mu(x)
$$

the predicted conditional probabilities must remain unchanged:

$$
P_{\mathrm{rel}}(O=o \mid A_C)\rightarrow P_{\mathrm{rel}}(O=o \mid A_C)
$$

This works only if the clock reading is tied to proper-time pulse accumulation or to a fully operational signal-exchange protocol.

This step is essential because otherwise H1 would merely rename coordinate time.

## Roadmap Step 9: Bound Finite-Clock Corrections

Real clocks are not ideal. A serious proof must quantify how imperfect clocks modify conditional dynamics.

Let the total correction be:

$$
\epsilon_C=\epsilon_{\mathrm{res}}+\epsilon_{\mathrm{drift}}+\epsilon_{\mathrm{back}}+\epsilon_{\mathrm{decoh}}+\epsilon_{\mathrm{grav}}
$$

where the terms represent readout resolution, frequency drift, backreaction, clock decoherence, and gravitational uncertainty.

The proof must show:

$$
\lim_{\epsilon_C\to 0}P_{\mathrm{rel}}(O=o \mid W_n)=P_{\mathrm{std}}(O=o;t=n/f_C)
$$

It should also derive the leading nonzero correction. This is important because finite-clock corrections may become the first place where H1 makes measurable predictions beyond a reinterpretation of known physics.

## Roadmap Step 10: Separate Conservative Equivalence From New Physics

The proof should be split into two layers.

### Layer A: Conservative Equivalence

Show that relational pulse-count conditioning reproduces:

- Born-rule probabilities
- Schrödinger evolution
- Heisenberg-picture correlation functions
- special-relativistic time dilation
- gravitational time dilation
- standard clock comparison experiments

This layer establishes that H1 is compatible with known physics.

The theorem above proves the first conservative single-time slice. The remaining items in this layer are broader validation tasks.

### Layer B: Fundamental Relational Time

Show that the external parameter can be removed from the fundamental formulation.

This requires one of the following:

- a Hamiltonian-constraint formulation where physical states are stationary
- a path-integral formulation where only relational boundary data are observable
- a quantum-reference-frame formulation where clock choice is a gauge-like choice

This layer is where H1 becomes more than a change of language.

## Roadmap Step 11: Connect To The Rest Of The Pulse Model

H1 is the clock-level foundation. It must remain compatible with the later hypotheses.

Connection to H2:

$$
\{N_i,\mathrm{signals}\}\Rightarrow[g_{\mu\nu}]
$$

Clock pulse counts are the raw relational data from which the metric may be reconstructed.

Connection to H3:

$$
\Delta N_{\mathrm{loop}}\neq 0
$$

Closed-loop pulse mismatches should encode curvature or synchronization holonomy.

Connection to H5:

$$
|\Psi\rangle=\alpha|\gamma_1\rangle|\chi(\tau_1)\rangle+\beta|\gamma_2\rangle|\chi(\tau_2)\rangle
$$

If quantum systems can carry superposed pulse histories, then H1 must support conditional probabilities over quantum clock states, not only classical clock counters.

## Roadmap Step 12: State Failure Conditions Clearly

H1 should be considered false, incomplete, or merely linguistic if any of these occur:

- ordinary Schrödinger evolution cannot be recovered in the ideal-clock limit
- the proof requires an observable external time after conditionalization
- one clock species becomes physically preferred without predicting Lorentz violation
- finite-clock corrections contradict existing clock experiments
- coordinate transformations change the predicted conditional probabilities
- massless fields cannot be described through action or field phase
- multiple ideal clocks give inconsistent predictions after calibration to matched proper-time windows
- the model cannot distinguish clock imperfections from fundamental temporal structure

## Minimal First Derivation Proven Here

The first complete derivation is deliberately narrow.

Use:

- one ideal clock
- one finite-dimensional quantum system
- no clock-system interaction
- flat spacetime
- a stationary total state satisfying $H_{\mathrm{tot}}|\Psi\rangle=0$
- pulse count $n=f_C\tau_C$

It proves:

$$
\lim_{\Delta\tau\to0}P_{\mathrm{rel}}(O=o \mid C\in W_n)=\mathrm{Tr}_S[E_O(o)U(n)\rho_S(0)U(n)^\dagger]
$$

with:

$$
U(n)=\exp(-iH_S n/(\hbar f_C))
$$

This is the minimal successful proof of H1 at the conservative level.

## Summary

The conservative proof of H1 shows that single-time temporal predictions can be formulated using conditional probabilities between physical pulse counters and system observables. The central mathematical move is:

$$ 
P(O=o,t)\rightarrow P(O=o \mid N_C=n)
$$

For a continuous ideal clock, the precise right side is $P(O=o \mid C\in W_n)$ followed by a sharp-window limit. The notation $P(O=o \mid N_C=n)$ is exact only for a discrete pulse readout, or as shorthand after this limiting procedure has been specified.

The central recovery theorem is:

$$
i\hbar f_C \frac{\partial}{\partial n}|\psi(n)\rangle=H_S|\psi(n)\rangle
$$

The central conceptual requirement is that $n$ is not a universal tick. It is a local, physical, calibrated pulse count. Ordinary time appears only as the idealized parameter reconstructed from relational pulse data:

$$
\tau_C=n/f_C
$$

Under the idealized single-clock assumptions proved above, H1 is a precise bridge between ordinary single-time quantum predictions, relativistic proper time, and the Pulse Model's deeper claim that spacetime should be described through relational pulse comparisons.
