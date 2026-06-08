---
title: H2 Finite-Data Stability And Gauge
sidebar_label: Stability And Gauge
sidebar_position: 4
---

# Appendix: H2 Finite-Data Stability and Gauge Conditions

**Parent hypothesis:** 6.2 Hypothesis H2: The metric is reconstructed from pulse comparisons  
**Status:** Stability and gauge appendix  
**Purpose:** State when finite pulse-record perturbations produce controlled uncertainty in a reconstructed metric class, and identify when gauge freedom or degeneracy prevents such a claim.

---

## 1. Scope

The ideal H2 theorem proves fixed-event uniqueness under dense proof-grade assumptions. The finite-data problem is weaker. A sparse noisy record cannot reconstruct an arbitrary Lorentzian metric without additional choices.

This appendix covers the practical finite-data setting used by the H2 schema and prototypes:

- a finite observed pulse/signal record
- a restricted metric or signal-response ansatz
- explicit calibration and nuisance variables
- a chosen gauge convention
- weighted residuals with stated uncertainties

The result is conditional. Finite H2 is stable only after gauge modes and nuisance degeneracies have been separated from the metric parameters being claimed.

---

## 2. Parameterized Reconstruction Problem

Let the observed finite record be represented by a vector of operational observations:

$$
y \in \mathbb{R}^m
$$

The entries of $y$ are pulse-derived durations, frequency ratios, phase residuals, direction residuals, acceleration readings, and incidence residuals from `h2_finite_pulse_record_schema.md`.

Choose a restricted reconstruction model:

$$
\theta \in \Theta
$$

where $\theta$ contains the metric-class parameters that are actually being estimated. Examples include:

- static clock-rate ratios
- weak-static potential differences
- a stationary direction-timing asymmetry
- a Shapiro-delay parameter such as $\gamma$
- a weak-wave strain component such as $h_+$

Let nuisance and calibration variables be:

$$
\chi \in X
$$

The finite prediction map is:

$$
F(\theta,\chi) = y_{\mathrm{pred}}
$$

The weighted residual is:

$$
r(\theta,\chi) = C_y^{-1/2}(y-F(\theta,\chi))
$$

where $C_y$ is the observation covariance matrix. A diagonal covariance is acceptable for the first prototype only when the independence assumption is stated.

---

## 3. Metric Norm

There is no single finite-data metric norm until a reconstruction target has been chosen. The norm must match the ansatz.

For a finite parameter estimate, use a weighted parameter norm:

$$
\|\delta\theta\|_W^2 = \delta\theta^\mu W_{\mu\nu}\delta\theta^\nu
$$

where $W$ is positive definite on the non-gauge parameter subspace.

For local metric-field estimates, a stronger norm may be used after gauge fixing:

$$
\|\delta g\|_{U,k} = \max_{0\le j\le k}\sup_{p\in U} |\nabla^j\delta g(p)|
$$

This stronger norm is only meaningful after choosing:

- a region $U$
- a background or candidate connection for comparing tensor fields
- a gauge condition
- a smoothness class
- boundary or regularity conditions

For the current H2 prototypes, the accepted norm is the finite parameter norm. Claims about arbitrary metric-field stability are not yet justified.

---

## 4. Gauge Fixing

A finite reconstruction must state its gauge convention before reporting stability.

Required gauge choices by slice:

- Minkowski static-clock slice: choose a reference clock as the time-scale gauge.
- Weak-static slice: choose a reference clock or boundary convention for the additive potential.
- Stationary direction-timing slice: report direction-time asymmetry as the observable; do not claim a unique coordinate component $g_{0i}$ without an ansatz.
- Shapiro-delay slice: state the calibrated endpoint geometry and mass model used to interpret delay as a spatial-metric or $\gamma$ constraint.
- Weak-wave slice: choose arm geometry, polarization basis, and long-wavelength approximation before reporting $h_+$.

Gauge freedom that remains after these choices is not an error. It is part of the equivalence class. A report should distinguish:

- gauge-fixed parameters
- gauge-invariant observables
- convention-dependent parameters
- underdetermined parameters

---

## 5. Noise Assumptions

The finite-data stability claim assumes:

- observation errors are small relative to the linearization scale
- observation covariance $C_y$ is known or bounded
- clock calibration uncertainties are included in $C_y$ or in $\chi$
- nuisance parameters have bounded prior ranges or are estimated jointly
- signal-link labels are correct, or mislabeling is modeled explicitly
- phase-wrap integers are resolved or included as discrete nuisance variables
- the reconstruction remains inside the domain where the ansatz is valid

If these assumptions fail, small-looking residuals can hide a wrong metric interpretation.

---

## 6. Local Stability Proposition

Assume:

- a gauge has been fixed
- $\theta_0$ and $\chi_0$ are the true model and nuisance parameters
- the observed record is $y=F(\theta_0,\chi_0)+\epsilon$
- $F$ is continuously differentiable near $(\theta_0,\chi_0)$
- nuisance variables are fixed, bounded, or jointly estimated with priors
- the Jacobian with respect to non-gauge metric parameters has full column rank

Let:

$$
J_\theta = C_y^{-1/2}\frac{\partial F}{\partial\theta}
$$

after removing gauge directions and nuisance directions that are not separately identifiable.

If the smallest singular value of $J_\theta$ is:

$$
s_{\min} > 0
$$

then the weighted least-squares estimate is locally stable. To first order:

$$
\|\delta\theta\|_2 \le \frac{\|C_y^{-1/2}\epsilon\|_2}{s_{\min}} + O(\|\epsilon\|_2^2)
$$

Equivalently, the parameter covariance is approximately:

$$
C_\theta \approx (J_\theta^\top J_\theta)^{-1}
$$

when the residual model is locally linear and the noise covariance is correct.

This is the finite-data stability claim. It does not say the record determines all components of $g_{\mu\nu}$; it says the chosen non-gauge parameters are stable if the gauge-fixed Jacobian is well conditioned.

---

## 7. Prototype Uncertainty Formulas

The current executable H2 prototype has explicit first-slice uncertainty propagation.

### 7.1 Static Clock Ratio

For a clock-rate ratio:

$$
R_A = \Delta T_A / \Delta T_{\mathrm{ref}}
$$

the weak-static potential difference in the reference-clock gauge is:

$$
\Delta\Phi_A = c^2(R_A-1)
$$

and:

$$
\sigma_{\Delta\Phi_A} = c^2\sigma_{R_A}
$$

This shows why small height-scale potential differences are numerically delicate in a naive double-precision pulse-count prototype.

### 7.2 Direction-Timing Asymmetry

For counter-propagating loop times $T_+$ and $T_-$:

$$
A = \frac{T_+ - T_-}{2}
$$

If both timing measurements have uncertainty $\sigma_T$, then:

$$
\sigma_A = \sigma_T/\sqrt{2}
$$

The observable $A$ is stable when the loop protocol and synchronization convention are fixed. Interpreting $A$ as a unique $g_{0i}$ component needs an additional stationary-metric ansatz.

### 7.3 Shapiro-Delay Gamma

For a calibrated Shapiro geometry:

$$
\Delta t_{\mathrm{Shapiro}} = (1+\gamma)\frac{GM}{c^3}\log\left(\frac{r_e+r_r+R}{r_e+r_r-R}\right)
$$

The recovered $\gamma$ uncertainty is:

$$
\sigma_\gamma = \sigma_t \left[\frac{GM}{c^3}\log\left(\frac{r_e+r_r+R}{r_e+r_r-R}\right)\right]^{-1}
$$

This is a spatial-metric constraint only under the calibrated endpoint and mass assumptions.

### 7.4 Weak-Wave Differential Arm Timing

For a long-wavelength plus-polarized wave and orthogonal equal arms:

$$
h_+ = \frac{T_x-T_y}{L/c}
$$

If both arm timings have uncertainty $\sigma_T$, then:

$$
\sigma_{h_+} = \frac{\sqrt{2}\sigma_T}{L/c}
$$

This estimate is stable only after fixing arm length calibration, polarization basis, and long-wavelength approximation.

---

## 8. Known Degeneracies

Finite H2 work must report these degeneracies when relevant:

- Diffeomorphism freedom: coordinate components of $g_{\mu\nu}$ are not observables.
- Time-scale gauge: static clock ratios need a reference clock or equivalent convention.
- Additive potential convention: weak-static $\Phi$ is recovered only up to a constant.
- Clock calibration versus $g_{00}$: frequency offsets can mimic gravitational clock-rate shifts.
- Velocity versus potential: moving clocks can mimic static potential differences unless acceleration and kinematic data constrain them.
- Signal delay versus spatial metric: instrument delay, plasma delay, or multipath can mimic Shapiro-like excess time.
- Synchronization convention versus $g_{0i}$: direction asymmetry is observable, but coordinate $g_{0i}$ requires an ansatz.
- Arm calibration versus wave strain: differential arm timing can mimic weak $h_+$ if arm length or timing calibration drifts.
- Sparse network degeneracy: finite clocks and links generally constrain only a low-dimensional ansatz.
- Caustics and topology: multiple signal paths can break simple event and tangent identification.

These are not optional caveats. They define the boundary between a finite-data result and an overclaim.

---

## 9. Acceptance Conditions For Stable Finite H2 Results

A finite H2 reconstruction result can be called stable only when:

- the observed record follows the finite schema
- the metric or response ansatz is stated
- gauge choices are stated
- nuisance variables are fixed, bounded, or jointly estimated
- the residual and covariance model are stated
- the gauge-fixed Jacobian or equivalent sensitivity calculation is full rank for the claimed parameters
- uncertainty propagation is reported
- known degeneracies are named
- synthetic truth is kept separate from observed records

If any item is missing, the result may still be a useful demonstration, but it should not be used as practical H2 acceptance evidence.

---

## 10. Consequence For H2

The H2 practical program is partially supported by the current finite prototypes: they demonstrate that selected pulse and signal records can recover selected metric-response parameters under clear gauge conventions.

Accordingly, the current H2 gate is partial rather than fully practical: the acceptance report identifies the accepted first-slice parameters, names gauge and ansatz dependencies, and leaves arbitrary sparse-data reconstruction, the full Jacobian and covariance program, and raw-relational promotion as explicit future strengthening work.
