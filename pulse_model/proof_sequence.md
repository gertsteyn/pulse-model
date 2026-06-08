# Pulse Model Proof Sequence

**Canonical page:** This compatibility path is preserved for older links. The canonical reader-facing roadmap is now [Roadmap](./roadmap.md).

**Purpose:** Define the natural order for proving, testing, or falsifying the Pulse Model.
**Scope:** This document tracks conceptual progress and acceptance gates. Durable task status belongs in Beads issues, not in this file.
**Parent:** [Formal Model](./formal_model/index.md)

---

## 1. Destination

The Pulse Model should end in one of three clear states.

1. **Strong success:** pulse-count consistency derives or strongly motivates spacetime geometry and dynamics, ideally including the Einstein-Hilbert phase functional:

$$
\Theta_{\mathrm{geom}} = \frac{1}{\hbar}\frac{c^3}{16\pi G}\int(R-2\Lambda)\sqrt{-g}\,d^4x
$$

2. **Useful conservative success:** pulse language produces reliable derivations, simulations, reconstruction tools, or clearer experimental descriptions while remaining equivalent to known GR/QM.
3. **Clean failure:** the model is shown to be only a vocabulary shift, or it fails at a specific gate such as metric reconstruction, curvature, conservation, or experimental constraints.

The working goal is therefore:

> Turn local pulse/phase accumulation into either a derivation engine, a prediction engine, or a precisely bounded failed hypothesis.

The current frontier options are tracked in [Frontier Strategy](./frontier_strategy.md). Those paths are not accepted proof steps. They are candidate modifications or sharpenings that could become future Beads epics if they pass the novelty gate.

---

## 2. Status Vocabulary

Use these status labels consistently.

| Status | Meaning |
|---|---|
| Not started | No dedicated proof, simulation, or appendix exists. |
| Drafted | A written proof target or derivation exists, but it has not been stress-tested. |
| Internally checked | Assumptions, units, signs, and logical dependencies have been reviewed against known physics. |
| Executable | A symbolic or numerical implementation exists and reproduces benchmark cases. |
| Accepted | The result passes its acceptance gates and can be used as an input to later hypotheses. |
| Blocked | A missing earlier result or contradiction prevents honest progress. |
| Failed | The hypothesis fails under its stated assumptions or contradicts known constraints. |

Beads issues should hold assigned work, dependencies, blockers, and completion state. This document should only summarize the proof ladder and current conceptual status.

---

## 3. Dependency Spine

The central proof order is:

```text
H1 -> H2 -> H3 -> H4 -> Geometry phase functional -> H5 -> H6 -> H7
```

Short form:

1. Prove pulse count can replace external time in ordinary predictions.
2. Prove pulse and signal comparisons reconstruct the metric.
3. Prove loop comparison residuals recover curvature.
4. Prove matter phase-response recovers stress-energy for standard matter.
5. Derive or motivate the geometric phase functional.
6. Extend pulse histories into quantum superposition.
7. Explain classical spacetime as decohered pulse-history structure.
8. Only then address vacuum energy and cosmology-level phase-response claims.

Later speculative claims should not be treated as established inputs for earlier gates.

---

## 4. Progress Ledger

| Step | Hypothesis or gate | Current status | Current artifact | Next proof move |
|---|---|---|---|---|
| 0 | Known-physics recovery ladder | Accepted with limits for the conservative executable first slice, exact and representative full-metric GR benchmarks, and reviewed H4 stress-energy phase-response evidence | `formal_model/known_physics_recovery.md`; `evidence/known_physics_validation.md`; `appendix/h4_stress_energy_as_phase_response.md`; Python tests under `tests/` | Use the accepted known-physics benchmarks and H4 matter-side source evidence downstream, but keep geometry-action recovery as a separate prerequisite for stronger claims. |
| 1 | H1: time is relational pulse count | Accepted with limits for conservative single-clock recovery | `appendix/h1_time_is_relational_pulse_count.md`, `src/pulse_model/h1_toy.py` | Use H1 as a bounded input to H2 and H5; do not treat stronger relational-time claims as proved. |
| 2 | H2: metric from pulse comparisons | Accepted for ideal fixed-event theorem; partially accepted for finite-data prototype slices; H2S1 adds a raw event-graph diagnostic tool; raw-relational identifiability remains conditional | `evidence/acceptance_reports/h2_metric_reconstruction.md`, `appendix/h2/metric_reconstruction_from_pulse_comparisons.md`, `appendix/h2/finite_pulse_record_schema.md`, `appendix/h2/finite_data_stability_and_gauge.md`, `appendix/h2/raw_relational_identifiability.md`, `appendix/h2/raw_event_graph_reconstruction.md`, `src/pulse_model/h2_reconstruction.py`, `src/pulse_model/raw_record_reconstruction.py`, `tests/test_h2_reconstruction.py`, `tests/test_raw_record_reconstruction.py` | Use H2 and H2S1 as bounded inputs to H3 and raw-record guardrails while treating arbitrary sparse-record reconstruction as open. |
| 3 | H3: curvature as pulse comparison holonomy | Accepted with limits for the first fixed-event or gauge-fixed curvature-holonomy slice | `appendix/h3_pulse_comparison_holonomy.md`, `src/pulse_model/h3_holonomy.py`, `tests/test_h3_holonomy.py` | Use H3 as a bounded curvature-holonomy input to geometry-action work, without treating it as a derivation of the geometric action. |
| 4 | H4: stress-energy as phase-response density | Accepted with limits for scalar-field, electromagnetic, and point-particle matter; covariant conservation derived on shell from diffeomorphism invariance; lightweight sign/convention checks executable | `appendix/h4_stress_energy_as_phase_response.md`, `tests/test_h4_stress_energy_phase_response.py` | Use H4 as a reviewed matter-side source input for the geometry-action gate, without treating it as a derivation of the geometric action. |
| 5 | Geometry phase functional | Accepted with limits; 05S strengthens it to a stronger conditional pulse-network derivation; 05S2 adds an executable pulse-record curvature estimator and bounded correction diagnostics, with final verdict useful constrained modification rather than novel raw-pulse derivation; 05S3 adds a correction-phenomenology novelty gate, with final verdict useful bounded diagnostic only; 05S4 adds an operational oriented-loop phase diagnostic, with final verdict useful bounded oriented-phase diagnostic rather than novel geometry-phase bridge; 05S5 adds conservative spin-connection recovery and a bounded connection-holonomy diagnostic, with final verdict useful bounded torsion/connection diagnostic rather than novel connection-phase response | `appendix/geometry_action/phase_functional_from_pulse_consistency.md`; `appendix/geometry_action/pulse_network_strengthening.md`; `appendix/geometry_action/pulse_record_curvature_estimator.md`; `appendix/geometry_action/correction_phenomenology.md`; `appendix/geometry_action/oriented_loop_phase.md`; `appendix/geometry_action/spin_connection_holonomy.md`; `src/pulse_model/pulse_regge.py`; `src/pulse_model/pulse_record_curvature.py`; `src/pulse_model/correction_phenomenology.py`; `src/pulse_model/oriented_loop_phase.py`; `src/pulse_model/spin_connection_holonomy.py`; `tests/test_pulse_regge.py`; `tests/test_pulse_record_curvature.py`; `tests/test_correction_phenomenology.py`; `tests/test_oriented_loop_phase.py`; `tests/test_spin_connection_holonomy.py` | Use 05/05S as conditional low-energy geometry-action input only when assumptions are explicit; use 05S2 for estimator, refinement, scalarization, and correction checks; use 05S3 as a bounded diagnostic and novelty guard for correction claims; use 05S4 as the operational phase-readout contract and artifact filter for oriented-loop claims; use 05S5 as the spin/full-connection artifact filter, representation-lift theorem, and bounded connection-residual diagnostic; do not treat Einstein-Hilbert gravity, the phase-to-defect coefficient, source-response, torsion, nonmetricity, independent connection dynamics, or new external deviations as derived from arbitrary pulse counts alone. |
| 6 | H5: superposed pulse histories | Accepted with limits for conservative quantum-clock visibility, weak-field proper-time inputs, and experiment mapping | `appendix/h5_superposed_pulse_histories.md`, `src/pulse_model/calculations.py`, `tests/test_h5_visibility.py` | Use H5 as a bounded branch-distinguishability input to H6 once geometry-action and source-to-metric prerequisites are ready. |
| 7 | H6: classical spacetime from decohered pulse histories | Accepted with limits for reduced branch-decoherence bookkeeping and model comparison; H6S1 adds an executable weak-field quantum source-response diagnostic tool; H6S2 adds an ensemble-decomposition-invariance admissibility filter with a clean no-go subtheorem; full classical-spacetime emergence and a real source-response law remain blocked | `appendix/h6/decohered_pulse_histories_classical_spacetime.md`, `appendix/h6/quantum_source_response_discriminator.md`, `appendix/h6/causal_pulse_response_kernel.md`, `src/pulse_model/calculations.py`, `src/pulse_model/quantum_source_response.py`, `src/pulse_model/causal_pulse_response.py`, `tests/test_h6_branch_decoherence.py`, `tests/test_quantum_source_response.py`, `tests/test_causal_pulse_response.py` | Use H6 only as a bounded branch-distinguishability, source-to-metric comparison, and source-response diagnostic framework; H6S2 means branch-conditioned variance is admissible only with local pointer records, a causal selection rule, or shared-future comparison. Stronger emergence still needs energy/no-signaling accounting, branch-selection dynamics, a causal source-response law, and macroscopic GR recovery. |
| 8 | H7: vacuum energy as phase-response | Constrained reformulation accepted with limits for renormalized metric-sensitive phase-response bookkeeping; no cosmological-constant solution or testable H7 deviation accepted | `appendix/h7_vacuum_phase_response.md`, `src/pulse_model/calculations.py`, `tests/test_h7_vacuum_phase_response.py` | Use H7 only as a conservative renormalized effective-action vocabulary and overclaim guardrail; stronger work needs a symmetry, dynamical residual, protected scale, or testable $w(a)$ prediction. |

---

## 5. Step 0: Known-Physics Recovery Gate

### Question

Does the conservative pulse language reproduce established GR/QM before adding speculative claims?

### Why It Matters

If the model cannot reproduce known results with correct signs, units, and limiting behavior, none of the speculative hypotheses should be advanced.

### Acceptance Gates

The model must reproduce:

- special-relativistic time dilation
- Schwarzschild gravitational time dilation
- weak-field combined expression:

$$
\frac{d\tau}{dt} \approx 1+\frac{\Phi}{c^2}-\frac{v^2}{2c^2}
$$

- Newtonian gravity from the proper-time action:

$$
\mathbf{a}=-\nabla\Phi
$$

- geodesic motion from stationary proper time
- gravitational redshift
- COW gravitational phase shift
- stress-energy definition as action variation

### Progress Rule

This gate is accepted only when the derivations are both written and backed by symbolic or numerical tests for representative cases.

---

## 6. Step 1: H1, Time Is Relational Pulse Count

### Question

Can ordinary single-time quantum predictions be reformulated as conditional predictions against a physical pulse counter?

### Current State

The conservative single-clock theorem in `appendix/h1_time_is_relational_pulse_count.md` is accepted-with-limits for the ideal single-time slice.

It proves, under ideal assumptions:

$$
\lim_{\Delta\tau\to0}P_{\mathrm{rel}}(O=o \mid C\in W_n)=\mathrm{Tr}_S[E_O(o)U(n)\rho_S(0)U(n)^\dagger]
$$

with:

$$
U(n)=\exp(-iH_S n/(\hbar f_C))
$$

and pulse-count Schrödinger form:

$$
i\hbar f_C \frac{\partial}{\partial n}|\psi(n)\rangle = H_S|\psi(n)\rangle
$$

The executable check in `src/pulse_model/h1_toy.py` implements a two-level finite-dimensional system conditioned on calibrated pulse count. Its tests in `tests/test_h1_toy.py` verify that the sharp-window probability matches the standard Born prediction at $\tau=n/f_C$, that a finite readout window returns the uniform average over nearby proper-time predictions, that the leading resolution correction matches the small-window expansion, and that finite windows and approximations reject inputs outside their stated domains.

The appendix now also states the formal target for sequential measurement probabilities and multi-time correlators. That target requires explicit clock readout instruments, system instruments, ordered records, and a stated correlation-ordering convention.

The H1 acceptance report in the appendix records the gate decision: H1 is accepted as a conservative single-clock, single-time equivalence result with executable finite-window and leading resolution-correction checks. This does not accept the stronger relational-time claim. The accepted slice is limited to a finite-dimensional noninteracting system conditioned on an ideal clock readout or a sampled ideal pulse counter, with matched calibrated proper-time windows for clock-species comparisons. The appendix gives first-order targets for drift and gravitational uncertainty, and explicitly leaves decoherence and backreaction model-dependent until a clock instrument or interaction Hamiltonian is specified. Sequential and multi-time predictions have a formal target, not a completed proof.

### Acceptance Gates

H1 is accepted at the conservative level when:

- the single-time theorem has been reviewed for assumptions and domain issues
- finite readout windows and discrete pulse sampling are handled explicitly
- different ideal clock species are shown to agree after calibration
- relativistic proper-time behavior is preserved
- a finite-clock correction model is derived and checked in a toy example

H1 is accepted at the stronger relational level only when:

- sequential or multi-time measurement predictions are reconstructed
- clock choice can be treated as a reference-frame or gauge-like choice
- no observable external time remains in the final physical predictions

---

## 7. Step 2: H2, Metric From Pulse Comparisons

### Question

Can relational pulse counts and signal exchanges determine the Lorentzian metric, up to diffeomorphism?

### Current State

The H2 gate decision is recorded in `evidence/acceptance_reports/h2_metric_reconstruction.md`: H2 is accepted for the ideal fixed-event uniqueness theorem, partially accepted for restricted finite-data prototype slices, and conditional for raw-relational identifiability under stated sufficient conditions. It is not accepted for arbitrary sparse-record metric reconstruction.

The conditional fixed-event theorem in `appendix/h2/metric_reconstruction_from_pulse_comparisons.md` has been reviewed as an internally checked ideal theorem.

Its scope is deliberately narrow: it proves metric uniqueness only after a smooth event region, incidence map, embedded clock segments, and proof-grade signal directions or infinitesimal signal curves are supplied. `appendix/h2/raw_relational_identifiability.md` states sufficient conditions under which raw event graphs can supply those fixed-event inputs.

The finite record schema in `appendix/h2/finite_pulse_record_schema.md` defines the practical data contract for observables, latent and gauge variables, calibration variables, nuisance parameters, reconstruction residuals, and synthetic generation.

The stability and gauge conditions in `appendix/h2/finite_data_stability_and_gauge.md` define the finite parameter norm, gauge conventions, noise assumptions, local Jacobian-rank stability condition, first-slice uncertainty formulas, and known degeneracies.

The first executable prototype in `src/pulse_model/h2_reconstruction.py` implements static-clock synthetic records and estimators for:

- Minkowski clock-rate equality in a reference-clock gauge
- weak-static potential differences from pulse-derived clock ratios
- pulse-count uncertainty propagation into potential-difference uncertainty
- stationary direction-dependent timing asymmetry as the finite-record handle for $g_{0i}$ effects
- Shapiro-style calibrated response-benchmark recovery as a spatial-metric constraint
- long-wavelength calibrated differential arm timing recovery for an injected weak $h_+$ mode

Its tests in `tests/test_h2_reconstruction.py` verify the finite-record boundary, signal-link presence, gauge independence of clock-rate ratios under coordinate-duration rescaling, flat-slice recovery, weak-static recovery at the documented first-slice tolerance, direction-dependent loop timing, calibrated Shapiro-delay gamma recovery, and injected weak-wave strain recovery. The Shapiro and weak-wave helpers are response benchmarks with interpretation metadata, not full schema-compliant raw observed records. This is not yet a reconstruction of arbitrary sparse metric data or a full Jacobian/covariance stability result.

The H2S1 appendix adds the first executable raw event-graph reconstruction diagnostic. It defines the no-geometry boundary, raw clock/signal/meeting schema, $1+1$ dimensional Minkowski generator contract, event-order and meeting-merge algorithms, null-signal residuals, rank/nullspace reporting, and an adversarial circularity review. The helper module `src/pulse_model/raw_record_reconstruction.py` validates raw records, recovers local order and meeting representatives, solves the static reciprocal-signal embedding slice, and reports sparse-record degeneracies. Its tests in `tests/test_raw_record_reconstruction.py` verify validation, event ordering, meeting merges, gauge-fixed embedding, null residuals, rank/nullspace reporting, underdetermined one-way records, inconsistent record rejection, and no leakage of generator-only coordinates. The final H2S1 verdict is **diagnostic tool**: it reduces H2 circularity for a controlled finite graph slice, but it does not prove a smooth event manifold, a general Lorentzian metric, arbitrary null cones, curvature, or new physics from arbitrary raw records.

Its ideal proof strategy is:

- signal directions determine the null cone
- null cones determine the conformal metric class
- calibrated timelike pulse durations fix the conformal factor
- coordinate freedom remains as diffeomorphism gauge

### Acceptance Gates

H2 is accepted at the ideal level when:

- the fixed-event theorem is reviewed and internally checked
- event-manifold identification assumptions are isolated from metric uniqueness
- clock-richness and null-richness assumptions are stated minimally
- circularity is avoided by distinguishing pulse-derived operational duration from metric proper time

The current finite-data prototype slice is accepted when:

- synthetic Minkowski records recover the static flat-clock slice in a stated gauge
- weak static records recover potential differences up to the expected convention
- stationary records recover the signed direction-timing asymmetry observable
- calibrated Shapiro-style benchmark records recover a $\gamma$ proxy with endpoint geometry and mass model stated as interpretation metadata
- calibrated weak-wave differential arm benchmarks recover injected $h_+$ under fixed arm geometry, polarization basis, and long-wavelength approximation
- finite noise produces reported uncertainty for the claimed first-slice parameters rather than arbitrary metric drift

---

## 8. Step 3: H3, Curvature As Pulse Comparison Holonomy

### Question

Do closed-loop pulse or synchronization mismatches recover curvature?

### Proof Target

Define an operational loop observable $\Delta N_{\mathrm{loop}}$ or equivalent synchronization residual such that its infinitesimal limit has the tensor content of curvature:

$$
\lim_{\Sigma\to0}\frac{\Delta N_{\mathrm{loop}}}{\Sigma}\sim R^\rho{}_{\sigma\mu\nu}
$$

### Acceptance Gates

H3 is accepted when:

- the loop observable is coordinate-invariant
- acceleration and signal-delay artifacts are separated from curvature
- flat spacetime gives zero residual after protocol corrections
- a known curved metric gives the expected Riemann tensor or geodesic-deviation signal
- the result does not assume the curvature conclusion in the synchronization rule

H3 depends on H2 because metric reconstruction supplies the object whose connection and curvature are being tested.

---

## 9. Step 4: H4, Stress-Energy As Phase-Response

### Question

Does the phase-response identity recover standard stress-energy for common matter systems?

### Proof Target

Starting from:

$$
S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}
$$

recover:

$$
T_{\mu\nu} = -\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

for:

- scalar fields
- electromagnetic fields
- point particles
- fluids or effective matter models, if needed later

### Acceptance Gates

H4 is accepted when:

- standard stress-energy tensors are recovered with correct signs
- energy density, momentum flux, pressure, and stress are all interpreted in phase-response terms
- conservation follows from diffeomorphism invariance:

$$
\nabla_\mu T^{\mu\nu}=0
$$

- the proof does not reduce stress-energy to mass density alone

H4 can proceed partly in parallel with H2 and H3, but it becomes load-bearing before the geometry-action step.

---

## 10. Step 5: Geometry Phase Functional

### Question

Can the geometric part of the action be derived from pulse-count consistency rather than assumed?

### Target

Derive, motivate, or falsify:

$$
\Theta_{\mathrm{geom}} \stackrel{?}{=} \frac{1}{\hbar}\frac{c^3}{16\pi G}\int(R-2\Lambda)\sqrt{-g}\,d^4x
$$

from pulse comparison, curvature holonomy, or relational consistency principles.

### Acceptance Gates

This step succeeds only if it:

- explains why curvature scalar $R$ is the correct local geometric phase density, or clearly identifies the missing assumption
- preserves diffeomorphism invariance
- yields Einstein's equation when combined with H4:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}
$$

- recovers the correct Newtonian limit
- avoids a preferred foliation or universal clock
- handles boundary terms or states why they are outside the current proof

This is the central speculative gate. Failure here does not necessarily kill the conservative model, but it blocks the strongest claim.

### Current State

Step 5 is accepted with limits and strengthened conditionally by 05S, with 05S2 now adding executable estimator and correction diagnostics. The original geometry-action appendix records the 05.5 conservative decision: the Einstein-Hilbert plus cosmological-constant phase may be used as the leading smooth low-energy candidate when H2 metric reconstruction, H3 curvature holonomy, H4 conserved matter phase-response, locality, scalarization, metric-only response, second-order dynamics, and boundary assumptions are carried forward explicitly.

The 05S appendix turns the main missing assumptions into an admissible pulse-network route. It defines pulse-cell complexes, maps corrected H3 frame holonomies to non-null Lorentzian hinge defects, gives restricted sufficient conditions for locality, scalarization, and replacement invariance, adds a small pulse-Regge prototype, and classifies higher-curvature, torsion, anisotropic, nonlocal, finite-loop, and lattice-memory corrections.

This is a stronger conditional derivation, not a fundamental derivation from arbitrary raw pulse data. Downstream work must still carry the 05S admissibility, locality, scalarization, refinement, boundary, and correction assumptions explicitly.

The 05S2 appendix upgrades the practical status of this gate without removing those caveats. It defines a pulse-record curvature-estimator contract, implements local sectional and scalar curvature estimation, checks deterministic refinement convergence, exposes preferred-plane scalarization residuals, distinguishes oriented linear phase defects from squared reconstruction losses, extracts preferred-projection and finite-loop correction terms, and adds local bound helpers. Its final verdict is **useful constrained modification**: the estimator and correction layer is novel/useful as a diagnostic and falsification tool, but it does not derive the Einstein-Hilbert phase from arbitrary raw pulse records.

The 05S3 appendix turns the retained 05S2 correction classes into a correction-phenomenology novelty gate. It adds dated bounds and helper checks for preferred-projection scalarization and finite-loop higher-curvature diagnostics. Its final verdict is **useful bounded diagnostic only**: correction claims are better bounded and easier to falsify, but no Pulse-specific external signal survives.

The 05S4 appendix tests the most promising frontier tweak: whether pulse-loop records can carry an operational oriented phase $\delta\Theta_L$ that is additive, orientation-odd, and distinct from squared estimator loss. It defines the phase-readout record contract, proves a restricted additivity and reversal theorem, implements focused helpers, benchmarks COW, Sagnac-style, scalarization, and finite-loop artifact separation, and runs an adversarial review. Its final verdict is **useful bounded oriented-phase diagnostic**: the linear oriented phase is now a precise diagnostic and future-record contract, but the novel geometry-phase bridge remains conditionally blocked by physical-readout, coefficient, scalarization, and source-response assumptions.

The 05S5 appendix tests the spin and full-connection frontier: whether spin, polarization, gyroscope, or internal-state transport records add operational connection content beyond H3 metric frame holonomy. It defines tetrad and spin-connection record contracts, recovers standard spinor phase-response, proves that torsion-free spin holonomy is a representation lift of H3 frame holonomy, implements focused spin-holonomy residual helpers, benchmarks known gyroscope and polarization transport, and runs an adversarial review. Its final verdict is **useful bounded torsion/connection diagnostic**: 05S5 provides a strong spin/full-connection artifact filter and bounded Lorentz-connection residual diagnostic, but no novel connection-phase response, torsion physics, nonmetricity physics, coefficient rule, or source-response law is accepted.

---

## 11. Step 6: H5, Superposed Pulse Histories

### Question

Can a quantum object carry a superposition of proper-time or pulse-count histories, and does this reproduce known clock-interferometer visibility formulas?

### Proof Target

For two worldlines:

$$
|\Psi\rangle=\alpha|\gamma_1\rangle|\chi(\tau_1)\rangle+\beta|\gamma_2\rangle|\chi(\tau_2)\rangle
$$

recover visibility:

$$
\mathcal{V}(\Delta\tau)=\left|\mathrm{Tr}\left(\rho_C e^{-iH_C\Delta\tau/\hbar}\right)\right|
$$

### Acceptance Gates

H5 is accepted when:

- pure two-level clocks show the expected visibility oscillations
- mixed or broad energy states show the expected loss of visibility
- gravitational and velocity time-dilation contributions to $\Delta\tau$ are included
- the model distinguishes ordinary environmental decoherence from proper-time-induced distinguishability
- predictions are mapped to existing or proposed clock-interferometry experiments

H5 can begin after H1's finite-clock model is stable. It does not need to wait for the geometry-action step if it is treated as a conservative quantum-clock calculation.

The literature map and H5 summary report in `appendix/h5_superposed_pulse_histories.md` record the conservative benchmark formulas, experimental scale estimates, claims H5 must not overstate, experiment mapping, and what H5 can provide to H6. The first simulator in `src/pulse_model/calculations.py` implements:

$$
\mathcal{V}(\Delta\tau)=|\mathrm{Tr}(\rho_C e^{-iH_C\Delta\tau/\hbar})|
$$

The same calculation module now also supplies constant-rate weak-field inputs for height and velocity contributions to $\Delta\tau$. These helpers cover the narrow regime $|\Phi|/c^2 \ll 1$, $v^2/c^2 \ll 1$, and common coordinate-time intervals; full pulse-sequence path modelling remains outside this H5 slice.

H5 is accepted with limits as a conservative quantum-clock calculation. It supplies H6 with branch-clock overlap and proper-time distinguishability inputs, but it does not define quantum metric states, branch-specific gravitational fields, collapse dynamics, semiclassical sourcing, or energy/no-signaling consistency.

---

## 12. Step 7: H6, Classical Spacetime From Decohered Pulse Histories

### Question

Does classical spacetime emerge when alternative pulse-count metric histories decohere?

### Proof Target

Model states of the form:

$$
|\Psi\rangle=\sum_a c_a|g_a\rangle|M_a(g_a)\rangle
$$

and identify when one effective metric branch behaves classically.

### Acceptance Gates

H6 is accepted only when:

- H5 supplies a working account of superposed pulse histories
- branch distinguishability is quantified
- semiclassical, branch-specific, and collapse/decoherence models make distinguishable predictions
- energy conservation and no-signaling issues are addressed
- the result explains why classical GR is recovered in ordinary macroscopic regimes

The H6 appendix records the first reduced result. H6 is accepted with limits for branch bookkeeping, a factorized branch-overlap criterion, a two-branch decoherence/dominance toy model, and a comparison between semiclassical expectation-sourced, branch-specific classical-metric, and collapse/decoherence families.

The H6S1 appendix adds the first executable quantum source-response discriminator. It defines a two-branch weak-field source/probe arena, proves that expectation-sourced and branch-mixture responses share the same ensemble mean in the linear slice, implements helpers for branch potentials, pulse-count means, branch variance, branch separation, source-probe correlation, and clock visibility, and rejects an intentionally invalid remote-basis response rule. Its final verdict is **diagnostic tool**: H6S1 supplies useful source-response gates and observable targets, but no pulse-native response law, collapse mechanism, metric quantization, or new external prediction is accepted.

The H6S2 appendix strengthens H6S1 by adding ensemble-decomposition invariance. It proves that branch-mixture response is not an admissible spacelike law merely because a branch decomposition can be written down. Branch-conditioned variance, correlation, and visibility become valid targets only when the branch basis is supported by local pointer records, a causal selection rule, or comparison in a shared causal future. H6S2's final verdict is **diagnostic tool** with a separate clean no-go subtheorem; the pulse-native law remains open.

The stronger emergence claim remains blocked. H6 does not yet define a quantum Hilbert space of metrics, a physical rule for coherent metric superposition, a collapse or branch-selection law, a no-signaling state-update rule, energy-momentum accounting through selection, or a generic macroscopic derivation of one classical GR spacetime. H6 may use H5 as a bounded matter-side branch-distinguishability input and 05/05S as conditional low-energy source-to-metric support only when their assumptions are carried explicitly.

---

## 13. Step 8: H7, Vacuum Energy As Phase-Response

### Question

Is the cosmological constant problem better stated as a question about metric-sensitive phase-response rather than absolute vacuum phase density?

### Proof Target

Clarify whether only relational or renormalized vacuum phase-response gravitates:

$$
\rho_{\mathrm{vac}}^{\mathrm{naive}} \gg \rho_\Lambda^{\mathrm{observed}}
$$

without contradicting QFT in curved spacetime or precision cosmology.

### Acceptance Gates

H7 is accepted only if:

- H4's phase-response formalism is solid
- the geometry phase functional is understood well enough to define what couples to curvature
- renormalization assumptions are explicit
- standard QFT-in-curved-spacetime constraints are addressed
- the result produces either a known-consistent reformulation or a testable deviation

The H7 appendix records the completed constrained reformulation. H7 passes at the conservative bookkeeping level: it distinguishes a pure absolute bookkeeping phase from a uniform covariant vacuum action density, identifies the gravitationally relevant object as the metric variation of the renormalized effective action, carries H4 and 05/05S assumptions explicitly, and checks the observed dark-energy scale and CPL $w_0w_a$ parameterization with lightweight executable helpers.

The stronger vacuum-energy claim remains unaccepted. H7 does not derive $\Lambda$, does not solve the radiative-stability or naturalness problem, does not prove that absolute uniform vacuum phase fails to gravitate, does not derive a state-dependent or curvature-dependent residual stress tensor, and does not predict $w(a)$. The correct final label is constrained reformulation accepted with limits, not a solved cosmological-constant mechanism.

H7 should remain last because it is the easiest place to overclaim.

---

## 14. Parallel Work Allowed

Some work can proceed without violating the dependency spine.

| Work | Can proceed when | Reason |
|---|---|---|
| H4 field derivations | Now | They are standard variational calculations and can be checked independently. |
| H5 conservative clock simulations | After H1 review | They use known proper-time and quantum-clock formulas. |
| Literature map | Now | It reduces overclaim risk across all hypotheses. |
| Unit and dimensional tests | Now | They protect every later step. |
| H2 finite-data prototypes | After H2 theorem review starts | Algorithms expose hidden assumptions in the ideal theorem. |

Speculative interpretation should still wait for the gates it depends on.

---

## 15. Beads Tracking Convention

Use Beads for durable task tracking.

Recommended issue shapes:

- one epic or feature per major step
- one task per proof appendix, simulation, benchmark, or literature map
- explicit dependencies matching the proof spine
- acceptance criteria copied from the relevant section of this document

Example dependency logic:

```text
H3 curvature holonomy depends on H2 ideal metric reconstruction.
Geometry phase functional depends on H3 curvature holonomy and H4 phase-response.
H6 decohered spacetime depends on H5 superposed pulse histories and source-to-metric coupling.
H7 vacuum phase-response depends on H4 and the geometry phase functional.
```

Do not use this document as a checkbox backlog. Use it to decide what Beads issue should exist next and what acceptance gate that issue must satisfy.

---

## 16. Current Next Work

The current highest-value sequence is:

1. Use H7 downstream only as a constrained renormalized phase-response vocabulary; do not treat it as a cosmological-constant solution or a testable dark-energy mechanism.
2. Use completed 05S2 only as an executable curvature-estimator, scalarization, refinement, and correction-diagnostics layer; do not treat it as a raw-pulse derivation of the Einstein-Hilbert phase.
3. Use H6, H6S1, and H6S2 downstream only as bounded branch-distinguishability, source-to-metric comparison, and source-response diagnostic frameworks; do not treat the reduced toy models or the ensemble-invariance guardrail as a full emergence proof or a real source-response law.
4. Strengthen H2 only through explicit follow-up work: full finite-schema Shapiro and weak-wave records, residual/covariance/Jacobian checks, and richer raw-relational finite-graph tests beyond the completed H2S1 diagnostic slice.
5. Strengthen H3 only through explicit follow-up work: finite-loop error bounds, path-ordered nonconstant-curvature transport, Lorentz-signature boost holonomies, multi-component loop networks, and covariance/noise analysis.

This section is a proof-ladder pointer, not the live task queue. Use Beads for current assignment, dependencies, blockers, and completion state.
