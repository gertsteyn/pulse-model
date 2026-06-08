---
title: H5 Superposed Pulse Histories
sidebar_label: H5 Superposed Histories
sidebar_position: 6
---

# Appendix: H5 Superposed Pulse Histories

**Parent hypothesis:** 6.5 Hypothesis H5: Quantum objects can carry superposed pulse histories  
**Status:** Accepted with limits for conservative quantum-clock visibility and weak-field proper-time inputs  
**Purpose:** Map established quantum-clock, proper-time-superposition, time-dilation decoherence, and clock-interferometry results into conservative Pulse Model benchmark targets.

---

## 1. Scope

H5 asks whether a quantum object can carry a superposition of different proper-time or pulse-count histories, and whether the model reproduces the standard clock-interferometer visibility formulas.

This appendix records the literature map, simulator formulas, proper-time inputs, and H5 summary report. It does not claim that gravitationally induced visibility loss has already been observed in a single delocalized clock, and it does not treat ordinary matter-wave phase shifts as sufficient evidence for operational proper-time superposition.

The conservative H5 target is:

> Given two interferometer branches with proper times $\tau_1$ and $\tau_2$, an internal clock state evolves differently on the two branches. The path visibility is the modulus of the overlap of those branch-conditioned clock states.

## 2. Literature Map

| Topic | Literature anchor | Benchmark imported into H5 | Boundary for Pulse Model claims |
|---|---|---|---|
| Quantum clocks and time | [Altaie, Hodgson, Beige review](https://arxiv.org/abs/2203.12564) | Treat clocks as physical quantum systems, not external parameters. | A review does not supply a unique H5 dynamics; H5 must specify Hamiltonian, state, and readout. |
| Proper-time visibility witness | [Zych, Costa, Pikovski, Brukner 2011](https://www.nature.com/articles/ncomms1498) | Visibility loss is governed by clock-state overlap, not only by path phase. | Phase shifts alone can often be rephrased as effective-potential phases; H5 must use an operational clock degree of freedom. |
| Time-dilation decoherence | [Pikovski, Zych, Costa, Brukner 2015](https://www.nature.com/articles/nphys3366) | Internal energy spread entangles with center-of-mass position through differential proper time. | This is a model of distinguishability, not a demonstrated universal collapse mechanism; competing decoherence channels and conceptual critiques must be tracked. |
| Decoherence caveats | [Bonder, Okon, Sudarsky comment](https://arxiv.org/abs/1507.05320), [Carlesso and Bassi competing-decoherence analysis](https://arxiv.org/abs/1602.01979) | Keep frame, subsystem, isolation, and environmental-decoherence assumptions explicit. | H5 must not overstate gravitational time dilation as the dominant practical decoherence source without a parameter check. |
| Quantum-clock redshift interferometry | [Roura 2020](https://arxiv.org/abs/1810.06744) | Light-pulse and clock-state protocols need careful closure and sensitivity analysis. | Some atom interferometers are insensitive to uniform-field redshift unless the protocol is designed to be clock-sensitive. |
| Static optical-clock redshift benchmarks | [Chou, Hume, Rosenband, Wineland 2010](https://doi.org/10.1126/science.1192720), [Bothwell et al. 2022](https://www.nature.com/articles/s41586-021-04349-7) | Use measured clock-rate scales to set realistic $\Delta\tau$ and phase targets. | Localized clock comparisons are not the same as delocalized clock-interferometer visibility loss. |
| Clock-interferometer proposals | [Meltzer and Sagi 2024](https://arxiv.org/abs/2402.14412) | Optical-tweezer clock interferometry gives a concrete candidate architecture with linear sensitivity to gravitational time dilation. | Proposed sensitivity is not a completed H5 observation. |
| Long-coherence atom interferometry | [Overstreet et al. 2024](https://www.nature.com/articles/s41567-024-02518-9) | Long spatial-superposition times make proper-time effects less hopeless experimentally. | Long coherence alone does not make the atom an operational clock; internal clock-state coherence is required. |

## 3. Benchmark Visibility Formulas

Consider two branches $\gamma_1$ and $\gamma_2$ with proper times $\tau_1$ and $\tau_2$. Let the internal clock Hamiltonian be $H_C$ and the initial internal state be $\rho_C$.

The branch-conditioned clock evolution is:

$$
\rho_C^{(i)}=e^{-iH_C\tau_i/\hbar}\rho_C e^{iH_C\tau_i/\hbar}
$$

The proper-time difference is:

$$
\Delta\tau=\tau_1-\tau_2
$$

For a pure clock state $|\chi_0\rangle$, the path visibility benchmark is:

$$
\mathcal{V}(\Delta\tau)=|\langle\chi_0|e^{-iH_C\Delta\tau/\hbar}|\chi_0\rangle|
$$

For a mixed or energy-incoherent clock state, the benchmark is:

$$
\mathcal{V}(\Delta\tau)=|\mathrm{Tr}(\rho_C e^{-iH_C\Delta\tau/\hbar})|
$$

If $\rho_C$ is diagonal in the clock energy basis with probabilities $p_j$ and energies $E_j$, this becomes:

$$
\mathcal{V}(\Delta\tau)=\left|\sum_j p_j e^{-iE_j\Delta\tau/\hbar}\right|
$$

This is the formula already represented by `clock_visibility` in `src/pulse_model/calculations.py`.

### 3.1 Two-Level Clock

For a two-level clock with energies $0$ and $\Delta E$, and equal probabilities:

$$
\mathcal{V}_{2}(\Delta\tau)=\left|\cos(\Delta E\Delta\tau/(2\hbar))\right|
$$

Equivalently, if $\Delta E=h f_0$:

$$
\mathcal{V}_{2}(\Delta\tau)=|\cos(\pi f_0\Delta\tau)|
$$

Full visibility loss in this idealized two-level benchmark first occurs when:

$$
f_0\Delta\tau=1/2
$$

For optical clock frequencies near $10^{14}$ to $10^{15}\ \mathrm{Hz}$, that requires $\Delta\tau$ near $10^{-15}$ to $10^{-16}\ \mathrm{s}$. Earth-lab proper-time differences over millimetre and centimetre separations are much smaller per second, so realistic proposals usually aim for phase sensitivity, longer hold times, larger separations, entangled resources, or repeated measurements rather than literal full contrast loss in one shot.

### 3.2 Broad Energy Distribution

For an internal state with mean energy $\bar{E}$ and rms energy spread $\sigma_E$, a narrow-time expansion gives:

$$
\mathcal{V}(\Delta\tau)\approx\exp(-\sigma_E^2\Delta\tau^2/(2\hbar^2))
$$

This is a benchmark envelope, not a new collapse postulate. It is the characteristic function of the internal energy distribution.

### 3.3 Interferometer Fringes

For a balanced two-path interferometer with controllable phase $\phi$, the output probabilities have the form:

$$
P_\pm=\frac{1}{2}(1\pm\mathcal{V}\cos(\phi+\phi_0))
$$

Here $\phi_0$ includes ordinary branch action phases and the phase of the clock-state overlap. H5 must keep $\mathcal{V}$ separate from ordinary phase shifts because phase shifts can be reproduced by effective potentials even when no operational clock degree of freedom records proper time.

## 4. Proper-Time Inputs

The weak-field, low-velocity proper-time rate used in the existing codebase is:

$$
\frac{d\tau}{dt}\approx1+\Phi/c^2-v^2/(2c^2)
$$

For two branches, the leading difference is:

$$
\Delta\tau\approx\int dt\left((\Phi_1-\Phi_2)/c^2-(v_1^2-v_2^2)/(2c^2)\right)
$$

Near Earth's surface, with height difference $\Delta z$ and equal velocities:

$$
\Delta\tau\approx g\Delta z T/c^2
$$

The corresponding pulse-count difference for a clock species with pulse frequency $f_C$ is:

$$
\Delta N_C=f_C\Delta\tau
$$

So H5 can use either proper-time difference or calibrated pulse-count difference. The physical visibility is unchanged by this reparametrization as long as $f_C$ is a calibration of the same internal Hamiltonian and the same local proper time.

The simulator helper sign convention is `delta_tau_s = tau_1 - tau_2`. The implemented constant-rate helpers are:

- `weak_field_delta_tau_s`, for two branches with fixed weak-field potentials and fixed speed magnitudes over the same coordinate-time interval
- `height_delta_tau_s`, the near-Earth shortcut with signed height difference $\Delta z=z_1-z_2$
- `velocity_delta_tau_s`, the low-velocity special-relativistic contribution from unequal branch speeds

Their domain is deliberately narrow. They assume a common weak-field coordinate time $T$, constant branch parameters over that interval, $|\Phi|/c^2 \ll 1$, $v^2/c^2 \ll 1$, and $|g\Delta z|/c^2 \ll 1$ for the height shortcut. Time-dependent paths should be represented later by summing or integrating short segments, not by hiding a full interferometer model inside these scalar helpers.

## 5. Experimental Scale Map

The scale near Earth's surface is:

$$
g/c^2\approx1.09\times10^{-16}\ \mathrm{m}^{-1}
$$

Therefore:

| Separation and hold time | Approximate $\Delta\tau$ | Optical phase scale for $f_0=4.3\times10^{14}\ \mathrm{Hz}$ |
|---|---|---|
| $\Delta z=1\ \mathrm{mm}$, $T=1\ \mathrm{s}$ | $1.1\times10^{-19}\ \mathrm{s}$ | $3.0\times10^{-4}\ \mathrm{rad}$ |
| $\Delta z=1\ \mathrm{cm}$, $T=1\ \mathrm{s}$ | $1.1\times10^{-18}\ \mathrm{s}$ | $3.0\times10^{-3}\ \mathrm{rad}$ |
| $\Delta z=10\ \mathrm{cm}$, $T=1\ \mathrm{s}$ | $1.1\times10^{-17}\ \mathrm{s}$ | $3.0\times10^{-2}\ \mathrm{rad}$ |
| $\Delta z=1\ \mathrm{cm}$, $T=10\ \mathrm{s}$ | $1.1\times10^{-17}\ \mathrm{s}$ | $3.0\times10^{-2}\ \mathrm{rad}$ |

Relevant benchmark regimes:

- Static optical clocks have already measured gravitational redshift at centimetre and millimetre scales, but those are localized clock comparisons.
- Matter-wave and atom interferometers routinely measure gravitational or inertial phase shifts, but an H5 clock test needs an internal state that actually carries timing information along the branches.
- Proposed optical clock interferometers target linear sensitivity to gravitational time dilation by combining spatial splitting with coherent clock-state control.
- Long-coherence lattice interferometry demonstrates that long spatial superposition times are becoming realistic, but H5 must still account for clock-state coherence, branch closure, vibrations, wavefront aberrations, trap shifts, blackbody shifts, collisions, spontaneous emission, and ordinary technical dephasing.

## 6. Claims H5 Must Not Overstate

H5 must not claim:

- that ordinary COW or atom-interferometer phase shifts alone prove operational proper-time superposition
- that localized optical-clock redshift experiments are already delocalized clock-interferometer visibility tests
- that gravitational time-dilation decoherence has been observed as the dominant decoherence channel in matter-wave experiments
- that proper time must be promoted to a new quantum operator
- that a visibility-loss formula proves spacetime itself is in quantum superposition
- that environmental decoherence can be ignored when comparing with experiments
- that pulse-count language changes the standard benchmark formula without adding a new measurable assumption

The accepted conservative statement should be:

> If a quantum system has internal clock degrees of freedom and its center of mass follows two branches with different proper times, then ordinary quantum mechanics plus relativistic proper time predicts branch-clock entanglement. The path visibility is the overlap of the two internal clock states.

## 7. Visibility Simulator

The first simulator stays small and explicit. It does not attempt a full atom-interferometer laser-pulse model. That belongs to a later task after the visibility benchmark is stable.

Implemented helpers in `src/pulse_model/calculations.py`:

- `clock_visibility` evaluates the discrete-energy mixed-state benchmark.
- `clock_visibility_series` evaluates that benchmark on a $\Delta\tau$ grid.
- `two_level_clock_visibility` evaluates the two-level clock benchmark with transition frequency $f_0$ and excited-state probability.
- `two_level_clock_visibility_series` evaluates the two-level benchmark on a $\Delta\tau$ grid.
- `gaussian_energy_spread_visibility` evaluates the broad-energy Gaussian envelope.
- `gaussian_energy_spread_visibility_series` evaluates the Gaussian envelope on a $\Delta\tau$ grid.
- `weak_field_delta_tau_s` evaluates the constant-rate weak-field branch difference $\Delta\tau=\tau_1-\tau_2$.
- `height_delta_tau_s` evaluates the uniform-field height shortcut $\Delta\tau\approx g\Delta zT/c^2$.
- `velocity_delta_tau_s` evaluates the low-velocity contribution $\Delta\tau\approx -T(v_1^2-v_2^2)/(2c^2)$.

The discrete-energy simulator implements:

$$
\mathcal{V}(\Delta\tau)=\left|\sum_j p_j e^{-iE_j\Delta\tau/\hbar}\right|
$$

The two-level helper implements:

$$
\mathcal{V}_{2}(\Delta\tau)=\left|(1-p_e)+p_e e^{-i2\pi f_0\Delta\tau}\right|
$$

For $p_e=1/2$, this reduces to:

$$
\mathcal{V}_{2}(\Delta\tau)=|\cos(\pi f_0\Delta\tau)|
$$

The Gaussian broad-energy helper implements:

$$
\mathcal{V}_{\mathrm{G}}(\Delta\tau)=\exp(-\sigma_E^2\Delta\tau^2/(2\hbar^2))
$$

The tests in `tests/test_h5_visibility.py` check:

- visibility is $1$ at zero proper-time difference
- equal two-level clocks oscillate and revive
- energy eigenstates keep full visibility
- mixed discrete clocks dephase
- Gaussian broad-energy envelopes decay with $|\Delta\tau|$
- series helpers match pointwise evaluations
- invalid probabilities, frequencies, and energy spreads are rejected
- height differences reproduce $\Delta\tau\approx g\Delta zT/c^2$
- velocity differences reproduce $\Delta\tau\approx -T(v_1^2-v_2^2)/(2c^2)$
- combined weak-field potential and velocity terms reproduce the branch formula
- generated $\Delta\tau$ values feed the two-level visibility simulator
- negative coordinate times, nonpositive light speeds, and superluminal branch speeds are rejected

The proper-time helpers implement the constant-rate weak-field input:

$$
\Delta\tau\approx T\left((\Phi_1-\Phi_2)/c^2-(v_1^2-v_2^2)/(2c^2)\right)
$$

Environmental contrast loss should remain a separate multiplier:

$$
\mathcal{V}_{\mathrm{obs}}=\mathcal{V}_{\mathrm{clock}}\mathcal{V}_{\mathrm{env}}\mathcal{V}_{\mathrm{tech}}
$$

## 8. Literature-Map Decision

The 06.1 literature map, 06.2 visibility simulator, and 06.3 proper-time helpers support H5 as a conservative, testable clock-interferometry program.

Accepted benchmark for downstream implementation:

$$
\mathcal{V}(\Delta\tau)=|\mathrm{Tr}(\rho_C e^{-iH_C\Delta\tau/\hbar})|
$$

Current H5 status:

- literature map drafted
- benchmark visibility formulas identified
- experimental scales identified
- overclaim boundaries stated
- visibility simulator implemented and tested
- weak-field, height, and velocity $\Delta\tau$ helpers implemented and tested
- H5 summary report accepted with limits

## 9. H5 Summary Report

### Verdict

H5 is **accepted with limits** as a conservative quantum-clock and clock-interferometry calculation.

The accepted result is:

- a two-branch quantum system can be represented with branch-conditioned internal clock states when the branch proper times are specified
- the path visibility is the internal clock-state overlap
- pure two-level clocks, mixed discrete clocks, and broad-energy clock states reproduce the standard visibility benchmarks
- weak-field height differences and low-velocity branch-speed differences can feed the same $\Delta\tau$ visibility simulator
- ordinary environmental and technical contrast loss remains separate from proper-time-induced distinguishability

The accepted result is not:

- a proof that matter-wave phase shifts alone demonstrate operational proper-time superposition
- a claim that gravitational time dilation is the dominant decoherence channel in current matter-wave experiments
- a full atom-interferometer pulse-sequence model
- a theory of quantum metric branches or metric superposition
- a derivation of the geometry-action coupling

### Evidence

| H5 item | Artifact or section | Gate covered |
|---|---|---|
| Literature map and overclaim boundaries | Sections 2, 5, and 6 | Experimental and interpretive scope |
| Visibility formula | Sections 3 and 7 | Clock-overlap visibility equation |
| Proper-time inputs | Sections 4 and 7 | Height, velocity, and combined weak-field delta-tau helpers |
| Executable simulator | `src/pulse_model/calculations.py` | Discrete clocks, two-level clocks, Gaussian envelopes, and delta-tau helpers |
| Regression tests | `tests/test_h5_visibility.py` | Visibility limits, dephasing, Gaussian decay, height/velocity formulas, validation |

Representative simulator outputs from the implemented tests and helpers:

| Scenario | Helper path | Output |
|---|---|---|
| Two-level clock, frequency 0.5 Hz, delta tau 0 s | `two_level_clock_visibility` | 1 |
| Two-level clock, frequency 0.5 Hz, delta tau 1 s | `two_level_clock_visibility` | approximately 0 |
| Two-level clock, frequency 0.5 Hz, delta tau 2 s | `two_level_clock_visibility` | 1 |
| Gaussian envelope, energy spread hbar, delta tau 1 s | `gaussian_energy_spread_visibility` | 0.6065306597 |
| Height example, T 2 s, height difference 5 m, g 10 m/s^2, c 100 m/s | `height_delta_tau_s` | delta tau 0.01 s |
| Same height example with frequency 25 Hz | `height_delta_tau_s` then `two_level_clock_visibility` | visibility about 0.7071067812 |
| Velocity example, T 5 s, speeds 6 m/s and 2 m/s, c 100 m/s | `velocity_delta_tau_s` | delta tau -0.008 s |
| Combined weak-field example from tests | `weak_field_delta_tau_s` | delta tau 0.067 s |

These small numerical examples are not proposed laboratory parameters. They are regression-scale values chosen to make the formulas and signs visible.

### Experiment Mapping

| Experimental class | What H5 can use | What H5 must not claim |
|---|---|---|
| Static optical-clock redshift tests | Calibrate realistic $\Delta\tau$ and pulse-count scales for height differences. | They are localized clock comparisons, not delocalized clock-interferometer visibility tests. |
| Quantum-clock redshift interferometry proposals | Supply protocol targets where internal clock states and branch closure are designed to reveal proper-time sensitivity. | A generic atom interferometer is not automatically redshift-sensitive in the H5 sense. |
| Optical-tweezer or long-coherence clock-interferometer proposals | Give candidate architectures for long hold times, controlled separations, and coherent internal clock readout. | Proposed sensitivity is not the same as an observed H5 visibility-loss signal. |
| COW and ordinary atom-interferometer phase tests | Provide conservative phase and gravitational benchmark scales. | Ordinary phase shifts alone do not prove operational proper-time superposition. |
| Time-dilation decoherence models | Supply the overlap formula and distinguishability logic for internal energy spread. | They do not remove the need to model ordinary environmental decoherence and technical contrast loss. |

### Decoherence Separation

H5 accepts proper-time-induced distinguishability only as the clock-state overlap:

$$
\mathcal{V}_{\mathrm{clock}}=|\mathrm{Tr}(\rho_C e^{-iH_C\Delta\tau/\hbar})|
$$

Observed interferometer contrast should be modeled as:

$$
\mathcal{V}_{\mathrm{obs}}=\mathcal{V}_{\mathrm{clock}}\mathcal{V}_{\mathrm{env}}\mathcal{V}_{\mathrm{tech}}
$$

This separation is required. A low measured contrast is not automatically evidence for H5 proper-time distinguishability, and a high measured contrast does not falsify H5 unless the clock-state coherence, path closure, and expected $\Delta\tau$ sensitivity are all in the tested regime.

### What H5 Provides To H6

H5 gives H6 a bounded branch-distinguishability input:

- each branch may carry a proper-time or pulse-count history
- an internal clock Hamiltonian and initial state define the clock overlap between branches
- the branch-clock overlap gives a conservative matter-side distinguishability measure
- environmental and technical contrast factors must remain separate nuisance or model factors

For H6, this means a metric-branch state model can use H5-style overlaps as one source of branch distinguishability. H5 does not itself define metric quantum states, branch-specific gravitational fields, collapse dynamics, semiclassical sourcing, or energy/no-signaling consistency. Those remain H6 and geometry-action obligations.

### Remaining Boundaries

The accepted H5 slice remains deliberately narrow:

- branch paths are externally specified rather than derived from a full light-pulse interferometer model
- weak-field $\Delta\tau$ helpers assume constant branch parameters over a common coordinate-time interval
- broad-energy Gaussian visibility is an ideal envelope, not an environmental master equation
- realistic experiment comparison still needs branch closure, laser phases, clock-state preparation/readout, systematic shifts, and noise budgets
- speculative metric-superposition claims must wait for H6 and source-to-metric coupling work
