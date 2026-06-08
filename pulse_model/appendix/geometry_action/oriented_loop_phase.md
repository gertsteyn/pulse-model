---
title: 05S4 Oriented Loop Phase
sidebar_label: 05S4 Oriented Loop
sidebar_position: 6
---

# Appendix: 05S4 Oriented Loop Phase Novelty Path

**Parent hypothesis:** 05S4, Oriented loop phase novelty path  
**Status:** 05S4 final verdict: useful bounded oriented-phase diagnostic  
**Purpose:** Decide whether corrected pulse-loop records can carry an operationally measurable oriented physical phase increment that is additive, orientation-odd, distinct from estimator loss, and useful for the Step 5 geometry-action gate.

---

## 1. Boundary

05S4 starts from the closed Step 5, 05S, 05S2, and 05S3 results. It does not restart the conservative geometry-action result, and it does not treat curvature estimation, Regge analogy, COW phase recovery, Sagnac recovery, or squared reconstruction loss as a new derivation.

The frontier question is narrower:

> Does a corrected local loop record contain a physical phase increment $\delta\Theta_L$ that is linear, additive across independent loops, odd under loop orientation reversal, and operationally distinct from an estimator loss?

05S4 may become useful in one of two ways. It may strengthen the geometry-action route if the record-level phase selects the oriented linear defect without importing the target action. Or it may fail cleanly and provide an artifact filter that keeps Step 5 caveats honest.

05S4 explicitly does not yet derive:

- the Einstein-Hilbert action from arbitrary pulse records
- Newton's constant $G$
- the cosmological constant $\Lambda$
- metric quantization
- external deviations from known physics
- a source-response map from matter records to metric dynamics

## 2. Accepted Inputs

05S4 may use these inputs only inside their accepted limits.

| Input | Accepted use | Prohibited use |
|---|---|---|
| H2 metric and frame reconstruction | Supply local events, frames, areas, volumes, and gauge-fixed reconstruction metadata when H2 conditions hold | Infer arbitrary sparse-record geometry or hide missing gauge conditions |
| H3 loop holonomy | Supply corrected small-loop frame closure, oriented loop areas, and tensor-ready curvature projections | Treat scalar timing residuals as the full curvature tensor or an action density |
| H4 phase response | Distinguish ordinary matter phase and stress-energy inputs from geometric phase claims | Count known matter phase as new geometry phase |
| 05 conservative geometry action | Provide the low-energy comparison target and caveat ledger | Define $\delta\Theta_L$ by copying the target action |
| 05S conditional pulse-Regge bridge | Provide the linear hinge-defect language and boundary/correction guardrails | Treat the conditional bridge as an unconditional raw-pulse derivation |
| 05S2 curvature estimator | Provide loop records, scalarization residuals, refinement reports, and orientation-loss checks | Promote squared loss to physical phase |
| 05S3 novelty gate | Keep correction and external-phenomenology claims bounded | Reopen external deviations without a response map |
| Synthetic records | Test signs, additivity, cancellation, and artifact separation | Claim physical detection |

## 3. Prohibited Shortcuts

The following shortcuts fail the 05S4 contract:

- defining $\delta\Theta_L$ as the Einstein-Hilbert or Regge action evaluated on a loop
- fitting a phase coefficient after seeing a benchmark and calling it derived
- using squared residual loss as a phase
- hiding calibration, matter, acceleration, rotation, signal, instrument, finite-loop, or plane-coverage artifacts
- treating COW, Sagnac, redshift, or matter-wave phase recovery as new physics
- using H7 vacuum phase-response, cosmology, torsion, nonlocal kernels, or lattice memory as hidden support
- ignoring cycle-wrap ambiguity or phase gauge conventions
- calling an oriented diagnostic a source-response law before a source-response map exists

## 4. Oriented Loop Phase Record Fields

An honest 05S4 loop record must separate observed fields, reconstructed fields, and correction ledgers.

| Field | Meaning | Unit | Status |
|---|---|---:|---|
| $L$ | loop identifier and ordered traversal | none | Observed protocol label |
| $p$ | base event or base station | none | Observed or reconstructed |
| $(a,b)$ | canonical local two-plane | none | H2/H3 reconstruction |
| $s_L$ | loop orientation sign | dimensionless | Observed traversal convention |
| $A_L$ | positive loop area | $m^2$ | H2 reconstruction or synthetic input |
| $\ell_L$ | loop scale | $m$ | Quality metadata |
| $V_c$ | associated cell volume or quadrature volume | $m^4$ | H2 or 05S reconstruction |
| $\Phi_{\mathrm{raw}}(L)$ | raw closed phase sum or interferometric phase readout | radians | Observed |
| $\Phi_{\mathrm{cal}}(L)$ | calibration and clock-zero correction ledger | radians | Artifact ledger |
| $\Phi_{\mathrm{mat}}(L)$ | ordinary matter-wave or internal-clock phase ledger | radians | Known-physics ledger |
| $\Phi_{\mathrm{rot}}(L)$ | rotation, acceleration, or Sagnac-like ledger | radians | Artifact or known-physics ledger |
| $\Phi_{\mathrm{inst}}(L)$ | instrument, signal, medium, and electronics ledger | radians | Artifact ledger |
| $\Phi_{\ell}(L)$ | finite-loop correction ledger | radians | 05S2/05S3 diagnostic |
| $\Delta_{\mathrm{scal}}$ | scalarization residual tied to the loop family | $m^{-2}$ | 05S2 diagnostic |
| $Q_L$ | uncertainty, wrap, and quality metadata | mixed | Required metadata |

The candidate corrected loop phase is:

$$
\phi_L=\Phi_{\mathrm{raw}}(L)-\Phi_{\mathrm{cal}}(L)-\Phi_{\mathrm{mat}}(L)-\Phi_{\mathrm{rot}}(L)-\Phi_{\mathrm{inst}}(L)-\Phi_{\ell}(L)
$$

The oriented phase candidate is:

$$
\delta\Theta_L=s_L\phi_L
$$

This definition is an operational record contract, not a geometry-action derivation. A record with no independent phase readout may still supply H3 curvature and 05S2 estimator diagnostics, but it cannot support an oriented-loop phase claim.

## 5. Candidate Observable Contract

The candidate observable $\delta\Theta_L$ must satisfy the following before it can be used downstream:

- **Physical readout:** $\Phi_{\mathrm{raw}}(L)$ must come from a clock phase, interferometric phase, frequency-comparison phase, or frame-transport phase readout. A least-squares residual is not enough.
- **Gauge safety:** closed-loop phase must cancel arbitrary clock-zero and phase-origin choices, or the remaining gauge convention must be stated and bounded.
- **Cycle-wrap handling:** the record must state the unwrapping convention or an allowed interval for $\delta\Theta_L$.
- **Artifact visibility:** all known non-geometric phase ledgers must remain visible.
- **Orientation rule:** reversing the loop traversal must send $\delta\Theta_L\to-\delta\Theta_L$ after applying the same canonical record convention.
- **Composition rule:** independent local loops must add linearly up to explicitly tracked shared-boundary, finite-loop, and artifact terms.
- **Loss separation:** the squared loss $\sum_L|\delta\Theta_L|^2$ may be an estimator cost, but it is not the physical phase.
- **Scalarization rule:** a cell-level geometry-phase candidate must explain how local two-plane phases contract to a Lorentz-signed scalar density without preferred projection.

## 6. Gauge And Calibration Requirements

The phase readout is usable only if these checks are passed or explicitly classified as failures:

| Requirement | Pass condition | Failure label |
|---|---|---|
| Clock-zero cancellation | Closed edge phase sums cancel arbitrary per-station phase offsets | `gauge-artifact` |
| Phase-origin convention | A global phase shift changes no closed-loop result | `gauge-artifact` |
| Cycle-wrap control | Phase is unwrapped by a stated rule or bounded interval | `gauge-artifact` |
| Calibration ledger | Removing calibration changes is explicit and finite | `calibration-artifact` |
| Matter phase separation | Known matter or internal-clock phase is not counted as geometry phase | `matter-phase-contamination` |
| Rotation and acceleration separation | Sagnac-like and noninertial terms are listed or independently bounded | `calibration-artifact` |
| Instrument and signal ledger | Medium, electronics, and delay terms are listed or bounded | `calibration-artifact` |
| Finite-loop reporting | $\Phi_{\ell}(L)$ and $\ell_L$ are recorded when non-negligible | `finite-loop-artifact` |
| Plane coverage | Local two-plane family is complete enough for scalarization | `scalarization-failure` |

## 7. Artifact Ledger

05S4 treats a nonzero corrected phase as a candidate only after the artifact ledger is exhausted. The ledger has these categories:

| Category | Examples | Allowed status |
|---|---|---|
| Calibration | clock offsets, phase-zero choices, path-length calibration | Must cancel or be subtracted with uncertainty |
| Matter phase | COW, de Broglie phase, internal-clock phase, redshift phase | Known-physics recovery unless a new geometric residual remains |
| Rotation and acceleration | Sagnac phase, platform rotation, noninertial transport | Artifact or known-framework term |
| Signal and medium | refractive delay, electronics delay, asymmetric propagation | Artifact term |
| Finite-loop | nonzero loop-size correction, coarse resolution, boundary leakage | Diagnostic or artifact unless invariant |
| Estimator loss | squared timing or curvature residuals | Diagnostic only |
| Coverage | missing or biased local two-plane family | Scalarization guardrail |

## 8. Failure Labels

05S4 uses these failure labels throughout the appendix.

| Label | Meaning |
|---|---|
| `estimator-loss-only` | The available quantity is a reconstruction cost or timing residual, not a physical phase. |
| `orientation-loss` | The proposed quantity is sign-blind under loop reversal. |
| `nonadditive-phase` | Independent loop composition does not add without unexplained cross terms. |
| `calibration-artifact` | The effect disappears under allowed calibration, rotation, acceleration, signal, instrument, or medium corrections. |
| `matter-phase-contamination` | Ordinary matter-wave, internal-clock, redshift, COW, or Sagnac phase is being counted as geometry phase. |
| `gauge-artifact` | Clock-zero, phase-origin, frame-gauge, or cycle-wrap choices change the claimed phase. |
| `finite-loop-artifact` | The phase scales away with loop refinement or is dominated by finite-loop correction terms. |
| `scalarization-failure` | Local two-plane data cannot contract to an unbiased Lorentz scalar density. |
| `known-framework-equivalent` | The result is standard matter phase, Sagnac physics, Regge bookkeeping, or EFT language in new notation. |
| `scope-violation` | The claim uses H2, H3, H4, H6, H7, or external phenomenology beyond accepted scope. |

## 9. Verdict Labels

05S4 must end with exactly one primary verdict label.

### Novel Geometry-Phase Bridge

This label requires all of the following:

- $\delta\Theta_L$ is operationally read from records before any action comparison
- independent loop phases add linearly with tracked boundary terms
- loop reversal changes the sign
- squared loss remains separate from physical phase
- scalarization to the local Lorentz scalar density succeeds without preferred projection
- artifact, matter-phase, calibration, finite-loop, and gauge explanations are bounded
- the bridge selects the linear geometry-phase defect without importing the Einstein-Hilbert or Regge action as the definition
- any remaining coefficient is fixed by a predeclared normalization rule or clearly marked as still matched by the Newtonian limit

### Useful Bounded Oriented-Phase Diagnostic

This label applies when 05S4 supplies executable sign, additivity, gauge, artifact, scalarization, or benchmark checks that make the Step 5 caveats sharper, but it does not produce an unconditional geometry-phase derivation.

### Blocked Conditional Bridge

This label applies when the oriented phase path remains possible only after assuming the missing physical phase, additivity, scalarization, source-response, or coefficient rule.

### Clean No-Go

This label applies when no honest operational $\delta\Theta_L$ can be defined, or when every candidate collapses to estimator loss, known physics, gauge artifact, or scope violation.

## 10. Ordered 05S4 Task Sequence

The 05S4 tasks must be completed in order:

1. Define oriented loop phase contract and novelty bar.
2. Define the operational oriented-loop phase observable.
3. Prove or falsify additivity and orientation oddness.
4. Derive scalarization and geometry-action bridge consequences.
5. Implement focused oriented-loop phase helpers and tests.
6. Benchmark oriented loop phase against known physics examples.
7. Run adversarial novelty and artifact review.
8. Write final oriented-loop phase verdict and update roadmap.

Each task may downgrade the path. Later tasks must not strengthen the claim unless all earlier gates remain satisfied.

## 11. 05S4.2 Operational Observable

05S4.2 admits an operational oriented-loop phase only for records that report a phase-like closed-loop quantity before any geometry-action comparison. The definition is record-level:

$$
\Phi_{\mathrm{raw}}(L)=\sum_i \Delta\phi_i+2\pi n_L
$$

where $\Delta\phi_i$ are signed edge, arm, or comparison phase increments around the ordered loop and $n_L$ is the declared unwrap integer. If the instrument reports a direct interferometric loop phase, this equation is the bookkeeping convention for that reported phase. If the record contains only fitted arrival-time residuals or curvature-estimator errors, 05S4 labels the quantity `estimator-loss-only`.

The corrected canonical loop phase is:

$$
\phi_L=\Phi_{\mathrm{raw}}(L)-\Phi_{\mathrm{cal}}(L)-\Phi_{\mathrm{mat}}(L)-\Phi_{\mathrm{rot}}(L)-\Phi_{\mathrm{inst}}(L)-\Phi_{\ell}(L)
$$

The oriented loop phase is:

$$
\delta\Theta_L=s_L\phi_L
$$

The unit of $\Phi_{\mathrm{raw}}$, every ledger term, $\phi_L$, and $\delta\Theta_L$ is radians. Radians are dimensionless, but the field names keep the phase status explicit.

### 11.1 Observable Sources

The accepted readout sources are:

| Readout | What is observed | 05S4 status |
|---|---|---|
| Closed clock-phase comparison | accumulated local oscillator or internal-clock phase around a loop | Candidate only after clock-zero and calibration cancellation |
| Interferometric phase | recombined arm phase with a declared loop orientation | Candidate only after ordinary matter-wave and path ledgers are removed |
| Frequency-comparison loop | integrated beat phase over a closed exchange protocol | Candidate only after oscillator, link, and signal ledgers are removed |
| Frame-transport phase | rotation or boost phase of a transported local frame or polarization basis | Candidate only when H3 frame conventions and noninertial artifacts are explicit |
| Scalar timing residual | arrival-time or synchronization residual | Diagnostic only unless converted to a physical phase by a declared oscillator frequency and artifact model |
| Curvature estimator loss | squared residual, fit error, or scalarization cost | `estimator-loss-only` |

This separates observed phase readings from H2/H3 reconstructed objects. H2 may supply $A_L$, $\ell_L$, $V_c$, and local frames. H3 may supply $\mathcal{K}_L$ and curvature projections. Neither H2 nor H3 supplies $\delta\Theta_L$ unless the record also contains a physical phase readout.

### 11.2 Clock-Zero And Phase-Gauge Cancellation

Let a pure clock-zero contribution on edge $i\to i+1$ be:

$$
\Delta\phi_i^{0}=b_{i+1}-b_i
$$

For a closed loop with vertex $N+1=1$:

$$
\sum_{i=1}^{N}\Delta\phi_i^{0}=0
$$

Therefore arbitrary station phase origins cancel in the closed sum. A candidate record must either use a closed-sum protocol with this cancellation or put the residual convention in $\Phi_{\mathrm{cal}}(L)$ with an uncertainty bound. A global phase shift $b_i\to b_i+b_0$ must not change $\delta\Theta_L$.

### 11.3 Cycle Wrap And Sign Convention

The record must store either:

- an unwrapped phase $\Phi_{\mathrm{raw}}(L)$ and the integer $n_L$
- a bounded wrapped interval plus a stated rule for choosing $n_L$
- a failure label `gauge-artifact`

The canonical plane convention is the same local two-plane convention used by 05S2. The field $s_L$ records traversal orientation and is applied exactly once. The canonical corrected phase $\phi_L$ is not squared, absolutized, or refit when orientation changes.

### 11.4 Difference From H3 Residuals And 05S2 Loss

The H3 scalar residual $\Delta T_{\mathrm{H3}}(L)$ is a timing or comparison projection of loop closure. It may help calibrate a phase readout if a physical oscillator frequency is specified, but by itself it is not $\delta\Theta_L$.

The 05S2 curvature estimator uses signed loop defects to estimate curvature, and may also use sign-blind losses for fitting or diagnostics. These objects have different roles:

| Quantity | Role | Orientation behavior | 05S4 status |
|---|---|---|---|
| $\delta\Theta_L$ | Candidate physical loop phase | Odd under loop reversal | Admitted if operationally read |
| $\phi_L^2$ or $\lvert\phi_L\rvert^2$ | Fit loss or noise statistic | Even under loop reversal | Diagnostic only |
| $\Delta T_{\mathrm{H3}}(L)$ | Timing projection of closure | Protocol-dependent | Diagnostic unless tied to phase |
| $\widehat{R}$ | Curvature estimator output | Lorentz scalar after full coverage | Geometry input, not phase |
| $\Delta_{\mathrm{scal}}$ | Scalarization residual | Detects biased plane sampling | Guardrail, not phase |

### 11.5 Artifact Ledger For The Observable

A record-level claim must report the ledger before comparing with any geometry-action target:

| Ledger term | Required handling |
|---|---|
| $\Phi_{\mathrm{cal}}(L)$ | subtract declared clock, path, and phase-origin calibration terms |
| $\Phi_{\mathrm{mat}}(L)$ | subtract or classify ordinary matter-wave, internal-clock, redshift, or COW phase |
| $\Phi_{\mathrm{rot}}(L)$ | subtract or classify Sagnac, acceleration, and noninertial frame terms |
| $\Phi_{\mathrm{inst}}(L)$ | subtract or classify instrument, electronics, medium, and signal-delay terms |
| $\Phi_{\ell}(L)$ | report finite-loop correction and refinement behavior |
| $\Delta_{\mathrm{scal}}$ | report scalarization failure or preferred-projection risk for the loop family |

**05S4.2 result:** an honest operational definition is available, but only as an extended pulse-loop phase record. Existing H3 and 05S2 records become eligible for this path only when they include a physical phase readout and the artifact ledger above. Without that extra readout, the status is `estimator-loss-only` or diagnostic, not a geometry-phase bridge.

## 12. 05S4.3 Additivity And Orientation Oddness

05S4.3 gives a restricted theorem. It is strong enough to justify executable oriented-phase checks, but it is not yet a geometry-action derivation.

### 12.1 Restricted Theorem

For a finite set of local loop records satisfying the 05S4.2 observable contract, define:

$$
\delta\Theta_L=s_L\phi_L
$$

where $\phi_L$ is the corrected canonical phase after subtracting the declared artifact ledgers. For independent local loops $L_1$ and $L_2$, the composed phase is:

$$
\delta\Theta_{L_1\cup L_2}=\delta\Theta_{L_1}+\delta\Theta_{L_2}+B_{12}+C_{12}+F_{12}
$$

Here:

- $B_{12}$ is a shared-boundary term.
- $C_{12}$ is a cross-calibration, signal, matter, or rotation artifact term.
- $F_{12}$ is a finite-loop overlap or refinement term.

If the two loops are independently corrected, share no uncancelled boundary phase, and have no unmodeled cross-artifact or finite-loop overlap, then:

$$
\delta\Theta_{L_1\cup L_2}=\delta\Theta_{L_1}+\delta\Theta_{L_2}
$$

This is additivity of the corrected record-level phase. It follows from linear summation of phase increments, not from the Einstein-Hilbert action.

### 12.2 Shared-Boundary Accounting

For adjacent loops with a shared edge traversed in opposite directions, the shared-edge phase cancels when both records use the same calibrated edge convention:

$$
\Delta\phi_e+\Delta\phi_{-e}=0
$$

The same cancellation must hold for calibration, signal, matter, rotation, instrument, and finite-loop ledgers assigned to that shared edge. If the shared-edge ledger is not anti-oriented or independently subtracted, the composition result is `nonadditive-phase` or `calibration-artifact`.

Boundary terms may remain when the composed region has an external boundary. Those terms are allowed only when they are listed as boundary data rather than hidden inside the local bulk phase.

### 12.3 Orientation Reversal

Let $-L$ be the same canonical loop record traversed in the opposite orientation, with the same canonical corrected phase $\phi_L$ and $s_{-L}=-s_L$. Then:

$$
\delta\Theta_{-L}=-\delta\Theta_L
$$

The phase is therefore orientation-odd under the record convention. If reversing the loop does not change the sign after applying the same artifact model, the candidate fails with `orientation-loss`, `calibration-artifact`, or `matter-phase-contamination` depending on the ledger.

### 12.4 Gauge Invariance

Clock-zero and phase-origin changes add edge-exact terms to the raw closed sum. Because a closed loop sums edge differences, those exact terms cancel before the orientation sign is applied. Therefore the restricted theorem is gauge-safe only under the 05S4.2 closed-loop protocol or an equivalent calibrated loop-phase readout.

Frame relabeling changes component labels for H2/H3 reconstructed areas and frame generators, but it must not change the corrected scalar phase readout. If a frame convention changes $\delta\Theta_L$ without a corresponding relabeling rule, the record is `gauge-artifact`.

### 12.5 Finite-Loop And Artifact Behavior

Finite-loop correction terms are allowed only as explicit terms:

$$
\delta\Theta_L=\delta\Theta_L^{0}+\delta\Theta_{\ell,L}
$$

where $\delta\Theta_L^{0}$ is the refined or corrected phase candidate and $\delta\Theta_{\ell,L}$ is the finite-loop ledger. If $\delta\Theta_{\ell,L}$ dominates or does not decrease under refinement, the result is a bounded diagnostic or `finite-loop-artifact`, not a novel bridge.

Artifact ledgers must also add linearly or cancel on shared boundaries. Nonlinear calibration updates, cycle-wrap jumps, or cross-loop instrument response move the claim to `nonadditive-phase` until explicitly bounded.

### 12.6 Squared Loss Comparison

For a loop reversal, the oriented linear phase changes sign:

$$
\delta\Theta_{-L}=-\delta\Theta_L
$$

The squared loss does not:

$$
\lvert\delta\Theta_{-L}\rvert^2=\lvert\delta\Theta_L\rvert^2
$$

Thus a squared reconstruction statistic cannot select the oriented linear defect required by the Step 5 geometry-phase bridge. It remains an estimator diagnostic and failure trigger.

### 12.7 05S4.3 Result

The physical linear defect survives as a restricted record-level algebraic candidate:

- it is additive for independent corrected loop phase records
- it is odd under loop reversal
- clock-zero and phase-origin terms cancel in closed-loop phase sums
- shared boundaries cancel when anti-oriented and consistently calibrated
- squared loss is rejected as the physical phase

The result is still conditional. It depends on the existence of a real phase readout and a complete artifact ledger. It does not assume the desired action, but it also does not yet prove that pulse records physically contain the geometry phase needed by Step 5.

## 13. 05S4.4 Scalarization And Bridge Consequences

05S4.4 asks whether the oriented phase candidate can feed the same local scalarization route needed by Step 5. The answer is useful but still conditional: the phase selects a linear oriented defect if a phase-to-defect normalization is supplied, but 05S4 does not derive that normalization or the source-response law.

### 13.1 Phase-To-Defect Map

For one local loop in plane $(a,b)$, H3 and 05S2 use the signed small-loop defect:

$$
K_{ab,L}=s_L\epsilon_L/A_L
$$

05S4 can compare an operational phase to that defect only through a declared normalization:

$$
\delta\Theta_L=\alpha_{\Theta}\,s_L\epsilon_L+\delta\Theta_{\ell,L}+\delta\Theta_{\partial,L}
$$

where:

- $\alpha_{\Theta}$ is a predeclared phase-to-defect coefficient in radians.
- $\delta\Theta_{\ell,L}$ is the finite-loop correction ledger.
- $\delta\Theta_{\partial,L}$ is a boundary or shared-edge ledger term.

Equivalently, when $\alpha_{\Theta}$ is known and nonzero:

$$
\widehat{K}^{\Theta}_{ab,L}=\delta\Theta_L/(\alpha_{\Theta}A_L)
$$

This equation is not an action definition. It is a diagnostic map from an observed oriented phase to the same sectional-curvature channel used by H3 and 05S2.

### 13.2 H2 And H3 Reconstructed Inputs

The bridge requires these reconstructed inputs:

| Reconstructed input | Source | 05S4 use |
|---|---|---|
| local frame and plane $(a,b)$ | H2/H3 | identify the canonical two-plane |
| positive area $A_L$ | H2 | convert linear defect to sectional density |
| loop orientation $s_L$ | loop protocol | apply the sign once |
| cell volume $V_c$ | H2 or 05S | normalize a local density or quadrature contribution |
| frame closure $\mathcal{K}_L$ | H3 | compare phase-derived defect to tensor-ready holonomy |
| loop scale $\ell_L$ | H2/quality metadata | expose finite-loop correction terms |
| plane coverage | 05S2 | decide whether scalarization is unbiased |

None of these reconstructed inputs is allowed to define the physical phase. They only test whether a phase readout, if present, matches the existing curvature and scalarization route.

### 13.3 Full Local Two-Plane Coverage Rule

A local cell may attempt scalarization only when the loop family covers the six canonical Lorentz two-planes:

$$
(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)
$$

For phase-derived sectional values $\widehat{K}^{\Theta}_{ab}$, the Lorentz-sign scalar contraction is:

$$
\widehat{R}_{\Theta}=2\sum_{a<b}\eta_{aa}\eta_{bb}\widehat{K}^{\Theta}_{ab}
$$

with local signature:

$$
(-,+,+,+)
$$

The sampled or biased scalar is:

$$
\widehat{R}_{\Theta,w}=2\sum_{a<b}w_{ab}\eta_{aa}\eta_{bb}\widehat{K}^{\Theta}_{ab}
$$

The scalarization guardrail is:

$$
\Delta_{\Theta,\mathrm{scal}}=\widehat{R}_{\Theta,w}-\widehat{R}_{\Theta}
$$

Missing planes, negative or tuned weights, spatial-only projection, or persistent preferred-plane residuals give `scalarization-failure` or a useful bounded diagnostic, not a novel bridge.

### 13.4 Finite-Loop Correction Terms

The phase-derived local density must report the same finite-loop risks as 05S2:

$$
\widehat{K}^{\Theta}_{ab,L}=\widehat{K}^{\Theta,0}_{ab}+\ell_L^2 C^{\Theta}_{ab}+O(\ell_L^3)
$$

and:

$$
\widehat{R}_{\Theta}(\ell)=\widehat{R}_{\Theta}^{0}+B_{\Theta}\ell^2+O(\ell^3)
$$

If the correction coefficient is nonzero, 05S4 may use it as a refinement diagnostic. It cannot call it a physical finite scale unless the scale is invariant, measured before comparison, and not removable by refinement.

### 13.5 Boundary Handling

The additive phase theorem allows shared interior boundaries to cancel when adjacent loops use opposite orientations and consistent ledgers. External boundaries remain separate:

$$
\Theta_{\mathrm{cell}}=\sum_{L\in c}\delta\Theta_L+\Theta_{\partial c}
$$

where $\Theta_{\partial c}$ must be reported as boundary data. It cannot be hidden inside the bulk scalar density. This mirrors the 05S boundary caution without importing the Regge action as the definition.

### 13.6 Coefficient Status

The decisive unresolved coefficient is $\alpha_{\Theta}$. 05S4 can use an injected $\alpha_{\Theta}$ for executable diagnostics, sign tests, and benchmark projections. It cannot count the bridge as novel unless $\alpha_{\Theta}$ is fixed by operational pulse records, a predeclared normalization law, or a later source-response derivation.

If downstream work chooses $\alpha_{\Theta}$ by matching the Newtonian limit, then 05S4 remains a useful route to sharper diagnostics, but not a derivation of $G$.

### 13.7 Bridge Classification

The 05S4.4 bridge classification is:

**Useful bounded oriented-phase diagnostic, with the novel geometry-phase bridge still conditional.**

The useful part is real: $\delta\Theta_L$ selects a linear, orientation-odd object and gives direct tests for additivity, scalarization, finite-loop contamination, and squared-loss confusion. The missing part is also explicit: 05S4 has not proved that real pulse records contain a geometry phase with a derived $\alpha_{\Theta}$ or a source-response law. Therefore the path may continue to executable diagnostics and benchmarks, but the final verdict cannot be a novel bridge unless those missing pieces are supplied later in the epic.

## 14. 05S4.5 Executable Helpers

The 05S4 executable layer lives in `src/pulse_model/oriented_loop_phase.py`, with tests in `tests/test_oriented_loop_phase.py`.

The implementation intentionally has a small scope:

| Helper | Purpose | Explicit non-goal |
|---|---|---|
| `PhaseComparisonEdge` and `closed_phase_sum_rad` | Check closed-loop phase summation, phase-zero cancellation, and explicit cycle unwraps | Does not infer a physical phase from timing data |
| `OrientedLoopPhaseRecord` | Store one corrected canonical phase record with artifact ledgers and orientation | Does not hide calibration, matter, rotation, instrument, or finite-loop terms |
| `linear_oriented_phase_rad` | Sum oriented phases as the candidate physical linear object | Does not square, fit, or absolutize the phase |
| `oriented_phase_squared_loss_rad2` | Expose the sign-blind estimator-loss comparator | Does not count squared loss as physical phase |
| `reverse_loop_orientation` | Check orientation reversal under the canonical record convention | Does not change the canonical phase by hand |
| `compose_oriented_loop_phases` | Report additive composition and explicit nonadditive boundary or artifact terms | Does not silently cancel shared-boundary failures |
| `estimate_oriented_phase_curvature` | Convert phase-derived defects into the existing 05S2 curvature estimator when $\alpha_{\Theta}$ is supplied | Does not derive $\alpha_{\Theta}$ or the Einstein-Hilbert action |
| `synthesize_oriented_phase_records_from_sectional_curvatures` | Build deterministic synthetic records for sign, scalarization, and refinement tests | Does not represent physical detection |

The tests cover:

- flat zero phase
- clock or phase-zero cancellation in a closed loop
- constant-curvature oriented phase recovery through the existing scalar estimator
- loop reversal
- additive composition and explicit nonadditive shared-boundary terms
- distinction between linear oriented phase and squared loss
- artifact subtraction and finite-loop correction reporting
- scalarization residual exposure under biased plane weights
- rejection of non-finite, non-closed, or physically invalid inputs

05S4.5 does not implement a general relativity engine, a matter interferometer model, or an Einstein-Hilbert action evaluator. It only makes the already justified record-level algebra executable.

### 14.1 Verification

The implementation task was checked with:

```bash
uv run python -m unittest tests.test_oriented_loop_phase
uv run python -m compileall src/pulse_model/oriented_loop_phase.py tests/test_oriented_loop_phase.py
uv run python -m unittest discover -s tests
```

The focused test file passed 8 tests. The full `pulse_model` unittest suite passed 133 tests after adding the 05S4 helper.

## 15. 05S4.6 Benchmark Matrix

The benchmark matrix is conservative. Passing a row means the oriented-loop bookkeeping behaves correctly for that controlled case. It does not by itself prove a new geometry phase.

| Benchmark | Expected sign and scaling | Artifact ledger | Executable evidence | 05S4 status |
|---|---|---|---|---|
| Flat corrected loops | $\delta\Theta_L=0$ and $\widehat{R}_{\Theta}=0$ | all ledgers zero or fully subtracted | `test_flat_zero_phase_records_have_zero_composition_and_curvature` | Useful diagnostic evidence: zero stays zero. |
| Clock or phase-zero cancellation | exact phase-origin edge terms sum to zero around a closed loop; unwrap adds $2\pi n_L$ | clock-zero ledger cancels before orientation sign | `test_closed_phase_sum_cancels_clock_zero_offsets` | Useful diagnostic evidence for gauge safety. |
| Loop reversal | $\delta\Theta_{-L}=-\delta\Theta_L$ | same canonical phase and ledgers, reversed traversal sign | `test_loop_reversal_changes_linear_phase_but_not_squared_loss` | Useful diagnostic evidence: oriented phase keeps sign. |
| Squared loss comparison | $\lvert\delta\Theta_{-L}\rvert^2=\lvert\delta\Theta_L\rvert^2$ | not an artifact; this is the diagnostic contrast | `test_loop_reversal_changes_linear_phase_but_not_squared_loss` | Blocks squared loss as physical phase. |
| Adjacent-loop composition | independent loops add linearly; explicit shared-boundary term creates additive error | shared boundary must cancel or be reported | `test_independent_loop_composition_is_additive_and_reports_cross_terms` | Useful diagnostic evidence; nonzero untracked boundary is `nonadditive-phase`. |
| COW or matter-wave phase orientation | ordinary matter phase has its own sign convention and scaling such as $m g A/(\hbar v)$ | $\Phi_{\mathrm{mat}}(L)$ must subtract known matter phase before geometry claims | `test_cow_matter_phase_and_rotation_phase_are_ledgers_not_geometry`; existing COW benchmark tests | Known-physics recovery, not novelty. |
| Sagnac or rotation artifact separation | rotation phase may be orientation-sensitive, but it is a noninertial or platform ledger term | $\Phi_{\mathrm{rot}}(L)$ must be subtracted or bounded | `test_cow_matter_phase_and_rotation_phase_are_ledgers_not_geometry` | Known-framework-equivalent or artifact unless an independent residual remains. |
| Constant-curvature synthetic records | phase-derived sectional values recover $\widehat{R}_{\Theta}=12k$ for constant curvature scale $k$ | synthetic record has no physical detection claim | `test_constant_curvature_phase_records_recover_existing_scalar_estimator` | Useful diagnostic evidence for scalar contraction. |
| Biased plane coverage | spatial-only weights give nonzero $\Delta_{\Theta,\mathrm{scal}}$ | coverage ledger exposes preferred projection | `test_scalarization_residual_is_exposed_for_biased_plane_coverage` | Useful diagnostic evidence; not a clean scalar phase. |
| Finite-loop correction reporting | finite-loop ledger changes reported correction and should decrease under refinement for a continuum diagnostic | $\Phi_{\ell}(L)$ remains visible | `test_artifact_ledgers_subtract_and_report_finite_loop_correction`; existing 05S2 refinement tests | Useful diagnostic evidence; physical finite scale remains blocked. |

### 15.1 Benchmark Outcome

No benchmark row supplies a candidate new-physics signal. The executable rows show that oriented-loop bookkeeping preserves the desired algebraic properties:

- zero loops stay zero
- clock-zero terms cancel in closed sums
- reversal changes the sign of the linear phase
- squared loss loses the sign
- independent loops add unless explicit cross terms are supplied
- known matter and rotation phases are ledger terms, not geometry phase
- synthetic phase-derived curvature reuses the 05S2 scalar estimator without importing an action
- biased coverage and finite-loop corrections remain visible

The result strengthens 05S4 as a diagnostic path. It does not yet turn $\delta\Theta_L$ into a novel geometry-phase bridge, because known COW and Sagnac-style rows are known-physics recovery and synthetic curvature rows use injected $\alpha_{\Theta}$.

### 15.2 Updated Verification

After adding the benchmark row for matter and rotation ledgers:

```bash
uv run python -m unittest tests.test_oriented_loop_phase
uv run python -m unittest discover -s tests
```

The focused 05S4 test file passed 9 tests. The full `pulse_model` unittest suite passed 134 tests.

## 16. 05S4.7 Adversarial Novelty And Artifact Review

This review treats every surviving 05S4 claim as suspect until it survives ordinary explanations. The labels below are intentionally severe.

| Claim or benchmark | Estimator-loss contamination | Matter phase contamination | COW, Sagnac, or rotation equivalence | Calibration and instrument artifacts | Finite-loop artifact | Gauge or cycle-wrap ambiguity | Biased loop-plane sampling | H2/H3 scope risk | Regge or EFT equivalence | Coefficient smuggling risk | Source-response or geometry-phase map | Label |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Operational $\delta\Theta_L$ record contract | low if physical phase readout is present; high otherwise | medium; must subtract $\Phi_{\mathrm{mat}}$ | medium; rotation-sensitive phases can imitate orientation oddness | medium; ledger required | medium; $\Phi_{\ell}$ required | medium; unwrap required | medium for scalar use | medium; H2/H3 provide reconstruction only | low at record level | medium if $\alpha_{\Theta}$ is asserted | missing until source-response is derived | useful diagnostic |
| Additivity theorem | low for linear records | low after ledger subtraction | low after ledger subtraction | medium if shared-boundary ledger is nonlinear | medium for overlapping finite loops | low for closed sums | not primary | low if local-loop assumptions hold | ordinary phase additivity | low | does not supply source-response | useful diagnostic |
| Orientation reversal | low for linear phase; squared loss fails | medium if matter phase is not separated | high for Sagnac-like phases unless ledgered | medium | low | low after sign convention | not primary | low | ordinary oriented phase behavior | low | does not supply source-response | useful diagnostic |
| Squared loss comparison | decisive; squared loss is estimator statistic | not primary | not primary | not primary | not primary | not primary | not primary | not primary | ordinary fit cost | high if promoted | no geometry-phase map | no-go for physical phase |
| Flat corrected loops | low | low | low after ledger subtraction | medium if correction model incomplete | low | low | low | low | known flat benchmark | low | no positive map supplied | useful diagnostic |
| Clock-zero cancellation | low | not primary | not primary | low for exact closed sums | not primary | central check; passes only with closed loop | not primary | low | ordinary gauge cancellation | low | no positive map supplied | useful diagnostic |
| Adjacent-loop composition | low for independent records | low after ledger subtraction | low after ledger subtraction | medium; shared-edge ledgers must cancel | medium; overlap terms must be listed | low if edge conventions match | not primary | medium near boundaries | ordinary additive phase bookkeeping | low | no source-response map | useful diagnostic |
| COW or matter-wave row | low | decisive if not subtracted | known matter-wave gravity phase | low in existing benchmark | not primary | ordinary interferometer phase convention | not primary | H4/known-physics scope | known-framework-equivalent | low | not a geometry phase | known-framework-equivalent |
| Sagnac or rotation row | low | not primary | decisive rotation equivalence | medium; platform model required | not primary | orientation convention required | not primary | H3 noninertial artifact scope | known-framework-equivalent | low | not a geometry phase | artifact or known-framework-equivalent |
| Constant-curvature synthetic row | low | none | none | none in synthetic input | low unless bias injected | low | low with full planes | medium; synthetic H2/H3 assumptions | Regge or curvature-estimator equivalent | high if $\alpha_{\Theta}$ is hidden | diagnostic only | useful diagnostic |
| Biased plane coverage row | low | none | none | none in synthetic input | low | low | decisive; exposes preferred projection | medium if coverage is claimed complete | ordinary scalarization diagnostic | medium if weights are tuned | no clean scalar map | useful diagnostic or scalarization-failure |
| Finite-loop refinement row | low | none | none | possible if resolution model is instrument-dependent | decisive if correction dominates | low | medium | medium; small-loop assumption | higher-curvature or cutoff equivalent if physical | high if scale chosen after comparison | no physical finite-scale map | useful diagnostic or finite-loop-artifact |
| Phase-to-defect bridge | low if readout exists | medium | medium | medium | medium | medium | medium | high; relies on accepted H2/H3 reconstruction | Regge-like linear defect unless phase is operationally independent | decisive; $\alpha_{\Theta}$ not derived | missing source-response law | blocked conditional bridge |

### 16.1 Severe Review Outcome

No claim currently deserves the label `pulse-specific` or `novel geometry-phase bridge`.

The strongest surviving result is narrower:

- an operational phase record can be defined without importing the target action
- the resulting linear phase is additive under restricted independence assumptions
- loop reversal keeps the sign information that squared loss destroys
- executable helpers expose gauge, artifact, finite-loop, and scalarization failures

The novelty blocker is also clear:

- real records must still provide the physical phase readout
- known matter and rotation phases explain important orientation-sensitive examples
- the phase-to-defect coefficient $\alpha_{\Theta}$ is injected, not derived
- no source-response map turns the phase diagnostic into field equations
- synthetic curvature benchmarks are useful, but they are not physical detection

Therefore the adversarial label for 05S4 before the final verdict is:

**Useful diagnostic, with the geometry-phase bridge blocked conditionally by physical-readout, coefficient, scalarization, and source-response assumptions.**

## 17. 05S4 Final Verdict

**Primary label:** Useful bounded oriented-phase diagnostic.

05S4 is a real level-up for Step 5 discipline, but it is not a novel geometry-phase bridge. The epic turns the promising oriented-loop phase idea into an operational record contract, a restricted additivity and orientation theorem, executable algebra checks, a benchmark matrix, and an adversarial novelty gate.

The strongest accepted result is:

> If a corrected pulse-loop record contains a physical phase readout with a complete artifact ledger, then the oriented quantity $\delta\Theta_L=s_L\phi_L$ is the right linear object to test. It is additive under restricted independent-loop composition, odd under loop reversal, and distinct from squared reconstruction loss.

That result is useful because it sharpens the exact missing assumption in Step 5. It does not prove that arbitrary pulse records contain the Einstein-Hilbert geometry phase.

### 17.1 Accepted Inputs

05S4 accepts:

- H2 reconstructed events, local frames, areas, loop scales, and cell volumes inside H2 scope
- H3 corrected frame-closure and curvature-holonomy data inside H3 scope
- H4 known matter-phase and stress-energy guardrails
- 05 and 05S as conditional geometry-action comparison and bridge inputs
- 05S2 curvature estimator, scalarization, refinement, and orientation-loss diagnostics
- 05S3 correction and novelty guardrails
- extended loop records with a real phase readout and explicit ledgers
- synthetic records for sign, additivity, scalarization, and artifact tests

### 17.2 Rejected Overclaims

05S4 rejects:

- $\delta\Theta_L$ has been observed in existing pulse records without adding a phase readout
- a timing residual or squared estimator loss is a physical geometry phase
- COW, Sagnac, redshift, or ordinary matter phase recovery is new geometry physics
- synthetic constant-curvature phase records are physical detection
- the coefficient $\alpha_{\Theta}$ is derived
- $G$, $\Lambda$, metric quantization, external deviations, or a source-response law are derived
- Step 5 is upgraded to an unconditional derivation of the Einstein-Hilbert action

### 17.3 Channel Status

| Channel or claim | Final 05S4 status |
|---|---|
| Operational oriented loop phase record | Admitted as an extended record contract. |
| Additive linear phase | Restricted theorem for independent corrected loop records. |
| Orientation reversal | Passed as record-level algebra. |
| Squared loss as phase | Rejected. |
| Phase-to-curvature scalarization | Useful diagnostic when $\alpha_{\Theta}$ and full plane coverage are supplied. |
| COW or matter-wave phase | Known-physics recovery and ledger term. |
| Sagnac or rotation phase | Known-framework or artifact ledger term. |
| Finite-loop phase correction | Diagnostic or artifact unless invariant and not removable by refinement. |
| Novel geometry-phase bridge | Blocked conditionally by physical-readout, coefficient, scalarization, and source-response assumptions. |

### 17.4 Downstream Allowed Uses

Downstream work may use 05S4 as:

- the record contract for future physical loop-phase measurements
- an executable sign and additivity diagnostic
- a guardrail against promoting squared loss to physical phase
- a gauge, artifact, matter-phase, rotation, finite-loop, and scalarization filter
- a way to test whether a future phase readout can be mapped into the 05S2 curvature estimator
- a bounded explanation of why the oriented-loop path is useful but not yet novel

### 17.5 Downstream Prohibited Uses

Downstream work must not use 05S4 as:

- a derivation of the Einstein-Hilbert action
- a derivation of $G$ or $\Lambda$
- evidence for external deviations from GR or QM
- proof that existing H3 timing residuals are geometry phases
- permission to ignore COW, Sagnac, matter-wave, calibration, or instrument ledgers
- permission to tune $\alpha_{\Theta}$ after seeing a benchmark or bound
- a source-response or field-equation map

### 17.6 Remaining Assumptions

The remaining load-bearing assumptions are:

- a physical loop phase readout exists for the relevant pulse-loop records
- phase wrap, clock-zero, calibration, matter, rotation, signal, instrument, and finite-loop ledgers can be independently controlled
- local H2/H3 reconstruction supplies reliable planes, areas, loop scales, and volumes
- full local Lorentz two-plane coverage is available for scalarization
- $\alpha_{\Theta}$ is fixed by a future operational rule or source-response derivation, not by after-the-fact fitting
- boundary terms can be separated from bulk local phase

### 17.7 Final Verification

Final 05S4 verification uses:

```bash
uv run python -m unittest tests.test_oriented_loop_phase
uv run python -m unittest discover -s tests
npm run typecheck
npm run build
```

The Markdown math guardrail scan also checks the 05S4 appendix, `roadmap.md`, and `frontier_strategy.md` for forbidden math delimiters, equation environments, labels, tags, and text macros.

### 17.8 Roadmap Result

The oriented-loop phase path is no longer just a proposed frontier. It has been tested and downgraded to a useful bounded diagnostic. It remains the correct contract if a future experiment or model supplies a real loop-phase readout, but it is not the next standalone novelty claim.

After `sci-wc9.8` closes, the 05S4 epic `sci-wc9` can close if all child tasks are closed. The next frontier should be selected from Beads and should carry the 05S4 lesson: no phase-response or source-response claim counts as novel until the operational readout, coefficient, artifact ledger, and response map are all explicit.
