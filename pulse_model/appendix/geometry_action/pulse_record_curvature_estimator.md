---
title: 05S2 Pulse-Record Curvature Estimator
sidebar_label: 05S2 Curvature Estimator
sidebar_position: 4
---

# Appendix: 05S2 Pulse-Record Curvature Estimator And Geometry-Action Gate

**Parent hypothesis:** 05S2, Novel/useful geometry-action strengthening  
**Status:** 05S2 final verdict: useful constrained modification  
**Purpose:** Test whether finite pulse-loop records can define a curvature estimator, a controlled scalarization limit, and an honest bridge to a geometry phase without importing the Einstein-Hilbert action as an input.

---

## 1. Boundary

The closed 05 appendix accepts the Einstein-Hilbert plus cosmological-constant phase only as a conservative low-energy geometry-action result. The closed 05S appendix strengthens that result conditionally: admissible pulse networks with locality, scalarization, refinement, boundary, and correction assumptions can support the usual low-energy action, but 05S does not derive that action from arbitrary raw pulse data.

05S2 is the next, narrower test. It asks whether the pulse records themselves can support an executable curvature-estimator layer strong enough to make the 05S assumptions measurable, falsifiable, or replaceable by controlled correction terms.

05S2 may use H2 and H3 only inside their accepted limits:

- H2 supplies reconstructed event regions, metric scaffolds, local frames, loop areas, and cell volumes when the finite record is rich enough.
- H3 supplies corrected local frame-closure generators for small loops.
- 05 supplies the conservative low-energy Einstein-Hilbert comparison target.
- 05S supplies the admissible pulse-network conditions and the conditional pulse-Regge bridge.

05S2 must not treat the target action as training data. The estimator must start from pulse-loop records and report curvature, coverage, residuals, and validation failures before any action decision is made.

## 2. Pulse-Record Schema

An observed pulse-record package for 05S2 is:

$$
\mathcal{R}=(E,C,S,F,L,A,Q)
$$

where:

- $E$ is the finite set of operational event labels used by the record.
- $C$ contains clock segment identifiers, calibrated pulse counts, and timing uncertainties.
- $S$ contains signal emission, reception, reflection, and meeting links.
- $F$ contains local frame, direction, polarization, accelerometer, gyroscope, and instrument metadata when available.
- $L$ contains oriented loop records.
- $A$ contains independent artifact and calibration corrections.
- $Q$ contains quality metadata such as resolution scale, curvature-variation scale, missing channels, and uncertainty bounds.

Each loop record used by the estimator must provide or reconstruct:

- a loop identifier
- a local frame identifier
- a canonical local two-plane $(a,b)$ in a local orthonormal frame
- a loop orientation sign $s_L$
- a positive loop area $A_L$
- a corrected signed canonical-plane defect $\epsilon_L$
- a positive cell volume contribution $V_L$ or an explicit quadrature weight
- a resolution scale $\ell_L$
- a known benchmark scalar curvature $R_{\mathrm{true}}$ only for synthetic tests, never as estimator input
- optional uncertainty and artifact metadata

The plane convention follows the 05S `pulse_regge.py` local frame order:

$$
(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)
$$

The local Lorentz signature is:

$$
(-,+,+,+)
$$

The sectional curvature value represented by a loop is estimated by applying the loop-orientation sign exactly once:

$$
K_{ab,L}=s_L\epsilon_L/A_L
$$

This is the small-loop H3 relation, not an action assumption. The record contract is deliberately not "pre-oriented defect plus orientation metadata": $\epsilon_L$ is signed in the canonical local-plane convention, and $s_L$ is the traversal orientation. Finite-loop and artifact corrections must remain visible as residuals or correction terms.

## 3. Reconstructed Objects

The estimator may use these reconstructed objects only when the record states the needed H2/H3 assumptions:

- local Lorentz frames and frame-comparison conventions
- loop area bivectors
- corrected frame-closure generators
- cell volume weights
- benchmark smooth geometry labels for synthetic validation
- curvature-variation scale estimates

These are not primitive observations. The central report must keep observed records, reconstructed H2/H3 quantities, estimator outputs, and geometry-action conclusions separate.

## 4. Estimator Contract

Given a finite set of loop records in one local cell, the estimator returns:

- per-plane sectional curvature estimates $\widehat{K}_{ab}$
- plane coverage diagnostics
- scalar curvature estimate $\widehat{R}$
- scalarization residuals
- refinement diagnostics when multiple resolution levels are supplied
- validation failures for incomplete, inconsistent, or non-finite inputs

The scalar curvature estimator is:

$$
\widehat{R}=2\sum_{a<b}\eta_{aa}\eta_{bb}\widehat{K}_{ab}
$$

with missing planes treated as a validation failure unless the call explicitly asks for a biased-coverage diagnostic. The sampled or biased scalar estimate is:

$$
\widehat{R}_{w}=2\sum_{a<b}w_{ab}\eta_{aa}\eta_{bb}\widehat{K}_{ab}
$$

The preferred-projection scalarization residual is:

$$
\Delta_{\mathrm{scal}}=\widehat{R}_{w}-\widehat{R}
$$

The anisotropic residual tensor for the local diagonal sectional basis is:

$$
A_{ab}=\widehat{K}_{ab}-K_{\mathrm{iso},ab}
$$

where $K_{\mathrm{iso},ab}$ is the constant-curvature sectional value that would reproduce $\widehat{R}$ in the same Lorentz convention.

The implementation must satisfy these rules:

- no use of the Einstein-Hilbert action in the estimator
- no use of target scalar curvature except in test assertions
- no hidden completion of missing planes by symmetry unless the benchmark declares that symmetry
- no conversion of squared reconstruction loss into a physical phase
- no preferred spatial-only plane set treated as Lorentz-invariant scalarization
- no negative plane weights; plane weights are quadrature or coverage weights, not arbitrary cancellation coefficients
- all finite-loop, artifact, coverage, and orientation failures remain visible

## 5. Benchmark Matrix

The minimum benchmark set is:

| Benchmark | Record input | Expected estimator result | Required diagnostic |
|---|---|---|---|
| Flat zero | all corrected defects vanish | $\widehat{R}=0$ | full coverage, zero scalarization residual |
| Constant curvature | all six sectional planes match one curvature scale with Lorentz signs | $\widehat{R}=12k$ | refinement preserves scalar estimate |
| Weak-field local tidal | spatial and time-space sectional values differ with known weak-field pattern | scalar estimate matches analytic trace | anisotropic residuals are reported |
| Biased plane coverage | preferred spatial-only or time-space-only loop family | sampled scalar differs from full scalar | nonzero $\Delta_{\mathrm{scal}}$ classified as correction or failure |

Synthetic records may use analytically known curvature values. Physical records must not import target curvature as an estimator input.

## 6. Error Metrics

For a benchmark with known scalar curvature $R_{\mathrm{true}}$, the scalar error is:

$$
e_R=\widehat{R}-R_{\mathrm{true}}
$$

The relative scalar error is:

$$
e_{\mathrm{rel}}=|e_R|/\max(|R_{\mathrm{true}}|,R_{\mathrm{floor}})
$$

where $R_{\mathrm{floor}}$ is a stated nonzero numerical floor for tests near flat space.

For refinement level $n$ with representative loop scale $\ell_n$, the reported convergence slope between adjacent levels is:

$$
p_n=\log(|e_{R,n}|/|e_{R,n+1}|)/\log(\ell_n/\ell_{n+1})
$$

This slope is only meaningful when both errors are positive and the same benchmark is being refined.

The scalarization residual norm is:

$$
\rho_{\mathrm{scal}}=|\Delta_{\mathrm{scal}}|/\max(|\widehat{R}|,R_{\mathrm{floor}})
$$

The plane-coverage score is the fraction of the six local two-planes represented by valid loop records:

$$
q_{\mathrm{plane}}=N_{\mathrm{planes}}/6
$$

Passing the estimator benchmark does not prove the action. It only proves that the pulse-record curvature estimator behaves correctly on controlled inputs.

## 7. Novelty And Outcome Criteria

05S2 must end with exactly one of these verdict labels.

| Verdict | Meaning |
|---|---|
| Novel effective derivation | Pulse records define curvature, scalarization residuals vanish under stated admissible refinement, and the physical phase bridge selects the oriented linear defect without importing the target action. |
| Useful constrained modification | The estimator is valid and the leading failure produces bounded correction terms such as anisotropic scalarization or finite-loop higher-curvature contributions. |
| Blocked or unchanged conditional 05 | The estimator is useful, but the bridge to a physical geometry phase remains an assumption; 05 and 05S remain the downstream source. |
| Clean failure | The estimator does not converge, scalarization is generically preferred-frame dependent, or the natural pulse-record functional contradicts the needed geometry-action structure. |

The default bar for novelty is high. A numerical estimator alone is not a novel derivation. A squared residual loss alone is not the Einstein-Hilbert phase. A successful 05S2 result must isolate why the oriented linear defect is a physical phase contribution rather than merely a reconstruction statistic.

## 8. Comparison Context

05S2 may compare against existing ideas only as context:

- Regge calculus gives the known benchmark relation between oriented hinge defects and $\int R\sqrt{-g}\,d^4x$ in regular refinement limits.
- Causal-set scalar curvature estimators show that discrete relational data can sometimes estimate curvature, but pulse records include richer clock, signal, and frame information and are not automatically causal sets.
- Effective-field-theory logic says higher-curvature terms are expected when short-scale structure is integrated out; it does not by itself determine pulse-model coefficients.
- Emergent-locality approaches show how nonlocal microscopic data might become local, but locality must be tested or assumed in the pulse-record layer.

These comparisons are not proofs for 05S2. They define sanity checks and failure classifications.

## 9. Non-Goals

05S2 does not attempt to:

- build a general numerical-relativity engine
- reconstruct arbitrary sparse raw records into a metric
- derive $G$, $\Lambda$, or matter dynamics from pulse data
- solve H7 vacuum energy
- prove full Lorentzian Regge calculus
- use observational constraints as adjustable fit targets
- rewrite the accepted 05 result unless the final verdict justifies it

## 10. Task Sequence

The 05S2 tasks must be completed in order:

1. Define this contract.
2. Implement the first pulse-record curvature estimator.
3. Test refinement convergence and scalarization residuals.
4. Derive or falsify the estimator-to-action bridge.
5. Extract leading controlled correction terms.
6. Compare retained corrections to known-physics bounds.
7. Write the final novelty or usefulness decision.

The expected useful path is not guaranteed to be a strong derivation. The honest level-up is that every missing 05S assumption becomes executable, bounded, or explicitly failed.

## 11. 05S2.2 Executable Estimator Result

The first estimator is implemented in `src/pulse_model/pulse_record_curvature.py` and tested in `tests/test_pulse_record_curvature.py`.

The implementation accepts corrected small-loop records with local Lorentz plane, loop orientation, loop area, signed canonical-plane defect, optional weight, and optional loop scale. It reports:

- weighted sectional curvature estimates by local two-plane
- scalar curvature from the Lorentz-signature contraction
- sampled scalar curvature for a supplied plane-weight rule
- scalarization residual
- anisotropic residuals relative to the constant-curvature pattern
- plane coverage and validation failures

The checked synthetic benchmarks are:

| Benchmark | Result |
|---|---|
| Flat zero defects | full coverage, $\widehat{R}=0$, zero scalarization residual |
| Constant curvature | recovers $\widehat{R}=12k$ with zero anisotropic residual |
| Trace-free local tidal pattern | reports $\widehat{R}=0$ while keeping nonzero anisotropic tidal residuals |
| Biased spatial-only weights | reports nonzero scalarization residual instead of hiding preferred-plane sampling |
| Invalid or incomplete records | reports missing-plane validation failures or raises value errors for non-physical fields |

This completes only the estimator layer. It does not yet prove convergence under refinement or select a physical action.

## 12. 05S2.3 Refinement And Scalarization Result

Refinement diagnostics are implemented beside the estimator. A refinement report records the loop scale, scalar curvature error, relative error, plane coverage, scalarization residual, adjacent convergence slopes, scalar-error classification, aggregate scalarization classification, and a combined classification for each benchmark family.

For the deterministic constant-curvature benchmark, the synthetic finite-loop bias is:

$$
\delta K_{ab}=\eta_{aa}\eta_{bb}\alpha\ell^2
$$

with $\alpha=0.5$ in the test. For $k=0.125$, the true scalar curvature is:

$$
R_{\mathrm{true}}=12k=1.5
$$

The checked loop scales and scalar errors are:

| Loop scale $\ell$ | Scalar error $e_R$ | Adjacent slope |
|---|---:|---:|
| 0.4 | 0.96 | 2.0 to next level |
| 0.2 | 0.24 | 2.0 to next level |
| 0.1 | 0.06 | end |

This is not a physical-data convergence claim. It proves that the estimator reports the expected second-order refinement scaling when the synthetic record has a known $O(\ell^2)$ finite-loop bias.

The flat benchmark with zero defects has scalar-error classification `exact-within-floor` and scalarization classification `unbiased`: all scalar errors and scalarization residuals vanish.

The scalarization adversary uses constant-curvature records with spatial-only sampling weights. The full estimator still finds:

$$
\widehat{R}=12k
$$

but the sampled scalar is:

$$
\widehat{R}_w=6k
$$

so:

$$
\Delta_{\mathrm{scal}}=-6k
$$

For $k=0.25$, the test reports $|\Delta_{\mathrm{scal}}|=1.5$, scalar-error classification `exact-within-floor`, scalarization classification `preferred-projection-correction`, and combined classification `exact-within-floor-with-preferred-projection-correction`. This is the intended failure behavior: biased plane sampling is not hidden inside a clean scalar-error convergence label.

## 13. 05S2.4 Estimator-To-Action Bridge

### 13.1 Result

05S2.4 cleanly falsifies the strongest possible claim:

> A pulse-record curvature estimator by itself selects the Einstein-Hilbert phase.

The estimator layer selects signed curvature estimates. It does not by itself select a physical phase functional. The natural statistical object for reconstructing curvature from noisy loop records is a squared residual or squared defect loss, and that object loses orientation sign.

The oriented linear defect can still be retained, but only as a restricted conditional bridge:

> If the pulse records include an oriented physical phase increment that is additive under cell composition and odd under loop-orientation reversal, then the leading local term is the oriented linear defect. If the records supply only estimator residuals, the natural leading functional is sign-blind and behaves like a curvature-squared loss or a reconstruction penalty.

This keeps the 05S bridge alive, but only with explicit assumptions. It does not upgrade 05 to a fundamental raw-pulse derivation.

### 13.2 Executable Orientation Check

The implementation distinguishes, with $\epsilon_L$ as the signed canonical-plane defect and $s_L$ as the loop-orientation sign:

$$
L_{\mathrm{lin}}=\sum_L w_L s_L\epsilon_L
$$

from:

$$
L_{\mathrm{sq}}=\sum_L w_L\epsilon_L^2
$$

Under orientation reversal $s_L\to -s_L$:

$$
L_{\mathrm{lin}}\to -L_{\mathrm{lin}}
$$

but:

$$
L_{\mathrm{sq}}\to L_{\mathrm{sq}}
$$

The test `test_oriented_linear_defect_keeps_sign_while_squared_loss_does_not` verifies this behavior through `compare_orientation_sensitivity`. This is the key distinction between a physical oriented phase candidate and a reconstruction loss.

### 13.3 Restricted Theorem

For an admissible pulse-record refinement family, the leading linear bridge is justified only if all of these assumptions hold:

1. Corrected loop records carry oriented phase increments, not only timing-fit residuals.
2. Independent local loop contributions add linearly in the physical phase.
3. Reversing a loop orientation reverses the phase contribution.
4. H2 supplies the loop areas, local frames, and cell weights inside its accepted scope.
5. H3 supplies corrected frame-closure defects inside its accepted small-loop scope.
6. Full local two-plane coverage is available, or scalarization residuals are carried as corrections.
7. Refinement removes finite-loop bias or leaves it as an explicit higher-curvature correction.
8. Boundary terms and artifact ledgers are separated before the bulk phase is read off.
9. The overall coefficient is matched by the low-energy Newtonian limit, not derived by this estimator.

Under those assumptions, the leading local phase candidate is the oriented linear defect used by 05S. Without those assumptions, the estimator supports only a useful curvature diagnostic and a controlled correction/failure analysis.

### 13.4 Classification

The action-bridge gate therefore lands at this intermediate result:

| Candidate functional | Selected by estimator alone? | 05S2.4 classification |
|---|---|---|
| Oriented linear defect | No | Retained only under explicit oriented-phase assumptions |
| Squared residual or squared defect loss | Yes, as a reconstruction statistic | Useful estimator loss, not an Einstein-Hilbert phase |
| Curvature-squared effective term | Only if squared loss is promoted to physics | Controlled modification or failure trigger |
| Nonlocal or preferred-plane functional | Only if locality or scalarization fails | Correction or clean failure depending on size |

This is a useful strengthening because it makes the critical missing input precise. It is not yet a novel effective derivation.

## 14. 05S2.5 Correction Basis

The correction basis keeps only terms exposed by the executable checks in 05S2.2 through 05S2.4.

### 14.1 Preferred-Projection Scalarization

The scalarization correction is:

$$
\Delta_{\mathrm{scal}}=\widehat{R}_w-\widehat{R}
$$

Its dimension is $m^{-2}$. Its sign is fixed by the plane-weight bias:

$$
\Delta_{\mathrm{scal}}=2\sum_{a<b}(w_{ab}-1)\eta_{aa}\eta_{bb}\widehat{K}_{ab}
$$

It vanishes when the local two-plane sampling is unbiased, or when the curvature pattern happens to be orthogonal to the sampling bias. It does not vanish merely because the scalar curvature estimate is accurate.

The anisotropic sectional residual ledger is:

$$
A_{ab}=\widehat{K}_{ab}-\eta_{aa}\eta_{bb}\widehat{R}/12
$$

This tensor-like six-plane ledger has dimension $m^{-2}$. It is not itself a beyond-GR correction, because ordinary Weyl curvature can make it nonzero. It becomes a correction only when the pulse network weights couple to it through a preferred projection.

The quantitative helper `scalarization_relative_norm` reports:

$$
\rho_{\mathrm{scal}}=|\Delta_{\mathrm{scal}}|/\max(|\widehat{R}|,R_{\mathrm{floor}})
$$

For the tested biased constant-curvature case with $k=0.25$, the result is:

$$
\Delta_{\mathrm{scal}}=-1.5
$$

and:

$$
\rho_{\mathrm{scal}}=0.5
$$

### 14.2 Finite-Loop Higher-Curvature Scale

The deterministic refinement test exposes a scalar finite-loop bias:

$$
e_R(\ell)=B_R\ell^2+O(\ell^3)
$$

where $B_R$ has dimension $m^{-4}$. The helper `finite_loop_bias_coefficients_per_m4` estimates:

$$
B_R=e_R/\ell^2
$$

For the tested constant-curvature refinement, the coefficient is:

$$
B_R=6.0
$$

at every checked level. This correction vanishes in the continuum estimator when $\ell\to0$ and the refinement slope remains positive. If a physical cutoff prevents refinement below a finite $\ell$, it behaves like a higher-curvature or finite-loop effective correction.

### 14.3 Squared-Loss Promotion

The squared defect loss remains:

$$
L_{\mathrm{sq}}=\sum_L w_L\epsilon_L^2
$$

It is retained as an estimator loss and as a failure trigger if someone tries to promote it to the physical phase. It is not retained as the leading geometry phase in 05S2 because it is sign-blind under orientation reversal.

### 14.4 Unsupported Classes

The current 05S2 executable work does not support claims for:

- torsion, because no independent antisymmetric connection or closure observable has been implemented
- nonlocal kernels, because no cross-cell response kernel has been measured
- lattice memory, because no persistent nonconvergent refinement pattern has been observed

These remain explicitly unclaimed. The helper `extract_correction_basis` returns them as unsupported terms, not as retained physics.

## 15. 05S2.6 Bounds And Testability

The bounds comparison is dated June 7, 2026. It uses the repository's accepted known-physics benchmarks and the executable 05S2 synthetic checks. No external observational number is imported in this task; if later work tries to promote a correction to phenomenology, it must add dated external sources at that point.

### 15.1 Bounds Table

| Retained correction | Constraining benchmark or observation | Allowed scale or coefficient | Testability |
|---|---|---|---|
| Preferred-projection scalarization | Plane-coverage diagnostics, local Lorentz invariance, and the accepted weak-field/tidal benchmark requirement that no preferred loop-plane family survive as scalar gravity | Relative scalarization norm must stay below the benchmark tolerance chosen before comparison | Directly testable from loop-plane weights and curvature records |
| Finite-loop higher-curvature scale | Refinement convergence of the estimator on known synthetic geometries and any future scalar-curvature benchmark | Relative finite-loop scalar error must stay below the benchmark tolerance chosen before comparison | Testable by changing loop scale and measuring convergence slope |
| Squared-loss promotion | Orientation-sensitivity check from 05S2.4 | Not allowed as the leading physical geometry phase in 05S2 because it loses orientation sign | Testable by reversing loop orientation |

The repository-level numerical helper for scalarization uses:

$$
\rho_{\mathrm{corr}}=|\Delta R|/\max(|R|,R_{\mathrm{floor}})
$$

The biased constant-curvature adversary gives:

$$
\rho_{\mathrm{corr}}=0.5
$$

so it fails a representative one-percent local sanity bound:

$$
\epsilon_R=0.01
$$

This one-percent value is a deterministic repository test threshold, not an observational constraint.

For finite-loop corrections, the helper `max_loop_scale_for_finite_loop_bound` computes:

$$
\ell_{\max}=\sqrt{\epsilon_R\max(|R|,R_{\mathrm{floor}})/|B_R|}
$$

For the synthetic coefficient $B_R=6.0$, reference scalar curvature $R=3.0$, and $\epsilon_R=0.01$, the checked value is:

$$
\ell_{\max}\approx0.070710678
$$

Loop scales below this threshold pass the stated local tolerance; loop scales above it fail. This is useful because it converts the finite-loop correction from a vague caveat into a concrete resolution requirement.

### 15.2 Bound Outcome

The bounds gate does not rule in a new physical deviation. It says:

- preferred-projection scalarization is a measurable correction or failure, not hidden noise
- finite-loop bias is acceptable only with an explicit loop-scale bound or a positive convergence slope to zero
- squared-loss promotion is rejected as the leading physical phase
- torsion, nonlocal kernels, and lattice memory remain unbounded because they are not retained by the current executable evidence

No arbitrary coefficient tuning is counted as success. A correction is useful only if it is measured from the record, forced below a stated tolerance, or exposed as a failure of the strong 05S2 claim.

## 16. 05S2 Final Verdict

**Verdict label:** Useful constrained modification.

05S2 is a major level-up for Step 5 because it turns several 05/05S assumptions into executable diagnostics:

- pulse-loop records now estimate sectional and scalar curvature without using the target action as input
- refinement reports quantify scalar error, scalarization residual, plane coverage, and convergence slope
- biased plane sampling is exposed as a preferred-projection correction or failure
- the estimator-to-action bridge now has a clean sign test separating oriented physical phase from squared reconstruction loss
- retained corrections have quantitative helper functions and local bounds

It is not a novel effective derivation of the Einstein-Hilbert action. The decisive reason is 05S2.4: the estimator alone does not select the physical phase. A squared residual is the natural reconstruction statistic and loses orientation sign. The oriented linear defect survives only under an explicit oriented-phase additivity assumption.

### 16.1 Accepted Inputs

05S2 accepts these bounded inputs:

- H2 metric and frame reconstruction inside its accepted scope
- H3 corrected small-loop frame-closure defects inside its accepted scope
- 05 conservative low-energy Einstein-Hilbert comparison target
- 05S admissible pulse-network and pulse-Regge assumptions
- synthetic benchmark records with analytically known curvature for executable validation

### 16.2 Rejected Overclaims

05S2 rejects these stronger claims:

- arbitrary raw pulse data derive $R\sqrt{-g}$
- a curvature estimator is automatically a physical action
- a squared reconstruction loss is the Einstein-Hilbert phase
- spatial-only or otherwise preferred loop-plane sampling can be hidden inside scalar curvature
- finite-loop or artifact effects can be ignored without a bound
- torsion, nonlocal kernels, or lattice memory are supported by the current executable evidence

### 16.3 Correction Status

| Correction class | Status |
|---|---|
| Preferred-projection scalarization | Retained as a measurable correction or failure; bounded by $\rho_{\mathrm{corr}}$ |
| Finite-loop higher-curvature scale | Retained as a resolution-dependent correction; bounded by $\ell_{\max}$ |
| Squared-loss promotion | Rejected as leading phase; kept as estimator loss and failure trigger |
| Torsion | Unsupported |
| Nonlocal kernels | Unsupported |
| Lattice memory | Unsupported |

### 16.4 Verification Commands

The final 05S2 verification used:

```bash
uv run python -m unittest tests.test_pulse_record_curvature
uv run python -m unittest tests.test_pulse_regge
uv run python -m unittest discover -s tests
```

The final repository documentation and frontend checks are recorded in the session close-out, because they run after this decision text is written.

### 16.5 Downstream Use

Downstream work may use 05S2 as:

- an executable pulse-record curvature estimator
- a scalarization and refinement diagnostic layer
- a controlled correction ledger for preferred-plane and finite-loop failures
- a guardrail against confusing estimator losses with physical phases

Downstream work must not use 05S2 as a fundamental derivation of the Einstein-Hilbert phase from arbitrary pulse counts. The conservative 05 result and the stronger conditional 05S bridge remain the source of the Step 5 geometry-action input, with the 05S2 diagnostics carried when novelty or correction claims are made.

### 16.6 Next Beads Work

After 05S2 closes, the next unblocked work should be selected from `bd ready`. H7 work remains separate from this epic unless Beads dependencies explicitly connect it.
