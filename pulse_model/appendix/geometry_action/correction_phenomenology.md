---
title: 05S3 Correction Phenomenology
sidebar_label: 05S3 Corrections
sidebar_position: 5
---

# Appendix: 05S3 Correction Phenomenology And Novelty Gate

**Parent hypothesis:** 05S3, Correction phenomenology and novelty gate  
**Status:** 05S3 final verdict: useful bounded diagnostic only  
**Purpose:** Decide whether the correction classes retained by 05S2 can become externally constrained, falsifiable physics signals without weakening the caveats accepted in 05, 05S, or 05S2.

---

## 1. Boundary

05S3 starts from the completed 05S2 verdict: useful constrained modification. It does not restart the Step 5 derivation, and it does not treat arbitrary raw pulse counts as a derivation of the Einstein-Hilbert action.

The only retained 05S2 correction inputs admitted at the start of 05S3 are:

- preferred-projection scalarization residuals from biased local two-plane sampling
- finite-loop higher-curvature scale effects exposed by nonzero refinement bias

The following classes are out of scope unless a later Beads epic explicitly opens them with new evidence:

- torsion
- nonlocal kernels
- lattice memory
- H7 vacuum-energy effects
- cosmology-level deviations
- derivations of $G$ or $\Lambda$

05S3 also keeps the 05S2 squared-loss result narrow. A squared reconstruction loss is an estimator diagnostic and a failure trigger if it is promoted to a physical phase. It is not an admitted candidate signal.

## 2. Accepted Inputs

05S3 may use these inputs:

| Input | Accepted use | Prohibited use |
|---|---|---|
| H2 metric and frame reconstruction | Provide local frames, loop areas, and cell volumes inside the accepted H2 scope | Infer arbitrary sparse-record geometry without H2 conditions |
| H3 loop holonomy | Provide corrected small-loop defects inside the accepted H3 scope | Treat finite-loop closure defects as action terms without correction checks |
| 05 low-energy action | Comparison target for known-physics recovery | Training target for pulse-record estimators |
| 05S conditional pulse-Regge bridge | Conditional bridge when oriented phase assumptions are explicit | Unconditional raw-pulse derivation |
| 05S2 estimator | Compute curvature, scalarization, refinement, and correction diagnostics | Hide missing coverage, finite-loop bias, or estimator losses |
| Synthetic records | Benchmark dimensions, signs, and bound propagation | Claim physical detection |

## 3. Candidate Observable Channels

05S3 admits exactly two candidate correction channels at the contract stage.

### 3.1 Preferred-Projection Scalarization

The 05S2 scalarization residual is:

$$
\Delta_{\mathrm{scal}}=\widehat{R}_w-\widehat{R}
$$

Its relative size is:

$$
\rho_{\mathrm{scal}}=|\Delta_{\mathrm{scal}}|/\max(|\widehat{R}|,R_{\mathrm{floor}})
$$

The observable channel is not a bare nonzero anisotropic sectional ledger. Ordinary curvature can be anisotropic. The channel exists only when a pulse-record ensemble carries a persistent preferred local two-plane projection after calibration, coverage, gauge, and finite-resolution explanations have been removed.

The first observable handles are:

- the signed residual $\Delta_{\mathrm{scal}}$ in $m^{-2}$
- the dimensionless residual norm $\rho_{\mathrm{scal}}$
- the plane-weight pattern $w_{ab}$
- the anisotropic ledger $A_{ab}$ only as a diagnostic explaining which planes drive the projection

The channel vanishes when the local two-plane weights reduce to unbiased scalar quadrature or when the curvature pattern is orthogonal to the sampling bias.

### 3.2 Finite-Loop Higher-Curvature Scale

The 05S2 finite-loop refinement model is:

$$
e_R(\ell)=B_R\ell^2+O(\ell^3)
$$

where $B_R$ has dimension $m^{-4}$ and $\ell$ has dimension $m$. The observable channel is a persistent nonzero finite-loop bias that does not converge away at available loop scales and can be bounded without tuning after seeing the benchmark.

The first observable handles are:

- the coefficient $B_R$ in $m^{-4}$
- the loop scale $\ell$ in $m$
- the scalar correction $\Delta R_{\ell}=B_R\ell^2$ in $m^{-2}$
- the relative finite-loop error $\rho_{\ell}=|\Delta R_{\ell}|/\max(|R_{\mathrm{ref}}|,R_{\mathrm{floor}})$
- the maximum allowed loop scale $\ell_{\max}$ for a stated relative bound

The channel vanishes in the continuum estimator when $\ell\to0$ and the refinement slope stays positive.

## 4. Dimensions And Coefficients

| Symbol | Meaning | Dimension | Source |
|---|---|---:|---|
| $\widehat{R}$ | full scalar-curvature estimate | $m^{-2}$ | 05S2 estimator |
| $\widehat{R}_w$ | weighted or biased scalar estimate | $m^{-2}$ | 05S2 estimator |
| $\Delta_{\mathrm{scal}}$ | preferred-projection scalarization residual | $m^{-2}$ | 05S2 correction basis |
| $\rho_{\mathrm{scal}}$ | relative scalarization size | dimensionless | 05S2 helper |
| $w_{ab}$ | local two-plane quadrature or coverage weight | dimensionless | pulse-record contract |
| $A_{ab}$ | anisotropic sectional residual ledger | $m^{-2}$ | 05S2 estimator |
| $B_R$ | finite-loop scalar bias coefficient | $m^{-4}$ | 05S2 refinement helper |
| $\ell$ | representative loop scale | $m$ | pulse-record contract |
| $\Delta R_{\ell}$ | finite-loop scalar correction | $m^{-2}$ | 05S2 refinement model |
| $\rho_{\ell}$ | relative finite-loop correction size | dimensionless | 05S2 helper |
| $\ell_{\max}$ | largest loop scale allowed by a stated bound | $m$ | 05S2 helper |

No 05S3 coefficient may be fitted after seeing an external bound and then counted as a success. A coefficient is usable only when it is measured from a pulse-record diagnostic, supplied as a predeclared benchmark value, or bounded conservatively as an unknown.

## 5. Required Records

A physical or synthetic 05S3 record must state:

- the 05S2 pulse-loop records used to compute $\widehat{R}$, $\widehat{R}_w$, $\Delta_{\mathrm{scal}}$, and any refinement report
- local frame and plane convention
- loop areas, loop scales, orientation signs, and corrected signed defects
- plane coverage and plane weights
- calibration and artifact ledger
- gauge or frame convention
- reference curvature or benchmark observable used only for validation or bounds
- uncertainty or tolerance chosen before comparison
- whether the record is synthetic, internal known-physics evidence, or external observational evidence

Incomplete records may still be useful as diagnostics, but they cannot support a candidate new-physics signal.

## 6. Failure Labels

05S3 uses these failure labels throughout the appendix.

| Label | Meaning |
|---|---|
| `coverage-failure` | Required local two-plane coverage is missing or underdetermined. |
| `sampling-artifact` | A preferred projection is explained by biased loop selection or weights. |
| `calibration-artifact` | The correction disappears under allowed calibration or artifact corrections. |
| `finite-resolution-bias` | The effect scales away with loop refinement or violates a stated loop-scale bound. |
| `orientation-loss` | The proposed phase term is sign-blind under loop reversal. |
| `known-framework-equivalent` | The channel is just a standard EFT, PPN, or reconstruction parameter in new notation. |
| `unsupported-channel` | The channel requires torsion, nonlocality, lattice memory, H7, or cosmology evidence not present in 05S2. |
| `tuned-after-bound` | A coefficient is chosen after seeing the bound and counted as a success. |
| `scope-violation` | The claim uses H2, H3, H6, or H7 outside its accepted scope. |

## 7. Outcome Criteria

05S3 must end with exactly one primary verdict label.

### Candidate New-Physics Signal

This label requires all of the following:

- the signal comes from an admitted 05S2 channel
- the coefficient or residual is measurable from records before comparison
- current external or internal bounds do not already exclude it
- the signal is not merely a known EFT, PPN, or estimator artifact in new notation
- a named observable can falsify it with a stated scaling law
- H2, H3, 05, 05S, and 05S2 caveats remain intact

### Useful Bounded Diagnostic Only

This label applies when the correction layer improves validation, resolution requirements, or artifact detection, but no Pulse-specific external signal survives the novelty review.

### Ruled-Out Correction

This label applies when an admitted correction maps cleanly to a known bound and the allowed size is incompatible with the correction needed for a physical claim.

### Clean No-Go

This label applies when no admitted channel can be parameterized without violating scope, covariance, conservation, orientation, or record-completeness requirements.

## 8. Constraint Map

**Source lookup date:** June 8, 2026.

This map is a guardrail for later 05S3 tasks. It does not yet claim a bound on a Pulse Model coefficient unless the admitted 05S3 parameter can be mapped to the source's observable without changing definitions.

### 8.1 Preferred-Projection Scalarization

| Source or benchmark | Observable | Current bound or constraint | Provenance | Status for 05S3 |
|---|---|---|---|---|
| 05S2 biased constant-curvature adversary | $\rho_{\mathrm{scal}}$ against a predeclared local scalar tolerance | $\rho_{\mathrm{scal}}=0.5$ fails the representative internal tolerance $\epsilon_R=0.01$ | Internal repository evidence | Bounded diagnostic; large biased plane sampling is excluded as clean scalarization. |
| Yagi, Blas, Barausse, and Yunes, `PhysRevD.89.084067` | weak-field preferred-frame PPN parameters | Solar-system tests require $|\alpha_1| \le 10^{-4}$ and $|\alpha_2| \le 10^{-7}$ | External literature, lookup June 8, 2026: [CERN PDF](https://cds.cern.ch/record/1632455/files/PhysRevD.89.084067.pdf) | Bounded; a persistent preferred projection must not imply larger PPN preferred-frame effects. |
| Yagi, Blas, Barausse, and Yunes, `PhysRevD.89.084067` | strong-field preferred-frame counterparts | pulsar observations require $|\hat\alpha_1| \le 10^{-5}$ and $|\hat\alpha_2| \le 10^{-9}$ | External literature, lookup June 8, 2026: [CERN PDF](https://cds.cern.ch/record/1632455/files/PhysRevD.89.084067.pdf) | Bounded; neutron-star or compact-binary claims face stronger preferred-frame limits. |
| Cassini Shapiro-delay result as summarized by NIST | PPN light-propagation parameter $\gamma$ | $\sigma_{\gamma}=2.3\times10^{-5}$ and result consistent with $\gamma=1$ | External literature summary, lookup June 8, 2026: [NIST](https://www.nist.gov/publications/accurate-light-time-correction-due-gravitating-mass) | Bounded where a scalarization channel changes the ordinary weak-field metric response. |
| GW170817 and GRB 170817A joint observation | relative GW and EM propagation speed | $(v_{\mathrm{GW}}-v_{\mathrm{EM}})/c$ constrained between $-3\times10^{-15}$ and $+7\times10^{-16}$ | External multi-messenger literature, lookup June 8, 2026: [LIGO DCC P1700308](https://dcc.ligo.org/LIGO-P1700308/public) | Indirect but severe; any preferred projection that changes tensor propagation speed is essentially ruled out at this level. |

**Constraint outcome:** preferred-projection scalarization remains admitted only as a local record diagnostic unless a later parameterization maps it cleanly to a small preferred-frame observable. A large persistent preferred-plane effect is already strongly bounded by known preferred-frame and propagation tests.

### 8.2 Finite-Loop Higher-Curvature Scale

| Source or benchmark | Observable | Current bound or constraint | Provenance | Status for 05S3 |
|---|---|---|---|---|
| 05S2 synthetic finite-loop refinement | loop-scale bound from $B_R\ell^2$ | for $B_R=6.0$, $R_{\mathrm{ref}}=3.0$, and $\epsilon_R=0.01$, $\ell_{\max}\approx0.070710678$ m | Internal repository evidence | Bounded diagnostic; any finite-loop claim must state the allowed resolution scale. |
| Lee, Adelberger, Cook, Fleischer, and Heckel, `PhysRevLett.124.101101` | short-distance inverse-square and Yukawa-like deviation | data covered 52 um to 3.0 mm; gravitational-strength Yukawa ranges above 38.6 um excluded at 95 percent confidence | External literature, lookup June 8, 2026: [arXiv](https://arxiv.org/abs/2002.11761), [University of Washington](https://phys.washington.edu/news/2020/04/06/experiment-finds-gravity-still-works-down-50-micrometers) | Bounded only if the finite-loop proxy maps to a Yukawa-like short-range force; otherwise it is not directly applicable. |
| LVK, `Tests of General Relativity with GWTC-3`, v3 | GW dispersion and non-GR waveform residuals | no evidence for GW dispersion or non-GR polarizations; graviton-mass bound $m_g \le 2.42\times10^{-23}$ eV/$c^2$ at 90 percent credibility | External literature, lookup June 8, 2026: [LIGO DCC P2100275](https://dcc.ligo.org/LIGO-P2100275/public), [arXiv v3](https://arxiv.org/abs/2112.06861) | Bounded for finite-loop models that imply dispersion or extra polarizations; otherwise qualitative. |
| GW170817 and GRB 170817A joint observation | propagation-speed deviation over cosmological baseline | $(v_{\mathrm{GW}}-v_{\mathrm{EM}})/c$ constrained between $-3\times10^{-15}$ and $+7\times10^{-16}$ | External multi-messenger literature, lookup June 8, 2026: [LIGO DCC P1700308](https://dcc.ligo.org/LIGO-P1700308/public) | Bounded for finite-loop corrections that alter tensor speed; not applicable to a purely local estimator-bias term. |
| Higher-curvature EFT comparison | curvature-squared or finite-resolution effective term | no single number applies until $B_R$ is mapped to a specific EFT operator and source-response convention | External framework comparison plus 05S2 caveat | Unconstrained as Pulse-specific physics; known-framework-equivalent until mapped. |

**Constraint outcome:** finite-loop effects remain useful as resolution bounds and convergence diagnostics. They can become external phenomenology only after 05S3.3 maps $B_R$ to a physical response channel such as short-range force modification, GW dispersion, or a standard higher-curvature EFT coefficient.

### 8.3 Out-Of-Scope Channels

| Channel | Constraint status | 05S3 status |
|---|---|---|
| Squared-loss promotion | rejected by the 05S2 orientation check before external bounds | Failure trigger, not a candidate signal. |
| Torsion | no admitted 05S2 observable | `unsupported-channel`. |
| Nonlocal kernel | no admitted cross-cell response kernel | `unsupported-channel`. |
| Lattice memory | no admitted nonconvergent persistent refinement pattern | `unsupported-channel`. |
| H7 vacuum energy or cosmology | explicitly not opened by 05S3.1 | Not applicable. |

## 9. Effective Parameterization

The 05S3 parameterization is intentionally minimal. It exposes record-level correction sizes that can be bounded, and it separates those from any stronger source-to-metric interpretation.

### 9.1 Preferred-Projection Scalarization Parameter

The signed preferred-projection parameter is:

$$
\lambda_P=\Delta_{\mathrm{scal}}/\max(|\widehat{R}|,R_{\mathrm{floor}})
$$

The nonnegative size used for bounds is:

$$
\rho_P=|\lambda_P|
$$

The plane-bias ledger is:

$$
P_{ab}=w_{ab}-1
$$

so the residual can be written in the 05S2 local two-plane convention as:

$$
\Delta_{\mathrm{scal}}=2\sum_{a<b}P_{ab}\eta_{aa}\eta_{bb}\widehat{K}_{ab}
$$

**Dimensions:** $\Delta_{\mathrm{scal}}$ has dimension $m^{-2}$; $\lambda_P$, $\rho_P$, and $P_{ab}$ are dimensionless.

**Sign convention:** $\lambda_P>0$ means the weighted preferred projection reports a larger scalar curvature than the full six-plane estimator. $\lambda_P<0$ means the weighted projection reports a smaller scalar curvature.

**Relation to 05S2 helpers:** `scalarization_relative_norm` computes $\rho_P$. The signed numerator is `estimate.scalarization_residual_per_m2`. Plane weights enter through the same `plane_weights` argument used by `estimate_pulse_record_curvature`.

**Limiting behavior:** $\lambda_P$ vanishes when $P_{ab}=0$ for every plane, when curvature anisotropy is orthogonal to the plane-bias ledger, or when calibration and artifact correction remove the biased sampling.

**Physical interpretation:** as a scalar effective term, $\lambda_P$ is only diagnostic. A scalar replacement

$$
R_{\mathrm{eff}}=\widehat{R}+\Delta_{\mathrm{scal}}
$$

does not by itself define a covariant source-to-metric theory. To become a physical preferred-frame term, $P_{ab}$ must be promoted from a sampling ledger to a measured frame field or projection structure with stated dynamics and with a conserved correction source:

$$
\nabla_{\mu}T_{\mathrm{corr}}^{\mu\nu}=0
$$

05S3 has no such dynamics. Therefore the admitted executable status is `anisotropic preferred-projection diagnostic`. It can be compared to PPN preferred-frame language only after a later model maps $\lambda_P$ to parameters such as $\alpha_1$ or $\alpha_2$. Without that map, it is not a candidate new-physics signal.

### 9.2 Finite-Loop Higher-Curvature Parameter

The signed finite-loop scalar correction at loop scale $\ell$ is:

$$
\Delta R_{\ell}=B_R\ell^2
$$

The relative finite-loop size is:

$$
\rho_{\ell}=|\Delta R_{\ell}|/\max(|R_{\mathrm{ref}}|,R_{\mathrm{floor}})
$$

For a stated allowed relative error $\epsilon_R$, the maximum permitted loop scale is:

$$
\ell_{\max}=\sqrt{\epsilon_R\max(|R_{\mathrm{ref}}|,R_{\mathrm{floor}})/|B_R|}
$$

when $B_R\ne0$. If $B_R=0$, the scale bound is infinite for this correction.

For comparison with a scalar higher-curvature proxy, define:

$$
c_2=B_R/R_{\mathrm{ref}}^2
$$

when $|R_{\mathrm{ref}}|>0$, so that:

$$
\Delta R_{\ell}=c_2\ell^2R_{\mathrm{ref}}^2
$$

The corresponding action-proxy coefficient would be:

$$
a_2=c_2\ell^2
$$

with dimension $m^2$, but this is only a comparison to ordinary curvature-squared EFT language. 05S3 does not derive the corrected field equations from this estimator.

**Dimensions:** $B_R$ has dimension $m^{-4}$; $\Delta R_{\ell}$ and $R_{\mathrm{ref}}$ have dimension $m^{-2}$; $\rho_{\ell}$ and $c_2$ are dimensionless; $a_2$ has dimension $m^2$.

**Sign convention:** $B_R>0$ means finite loops overestimate the scalar curvature relative to the refinement target. $B_R<0$ means finite loops underestimate it.

**Relation to 05S2 helpers:** `finite_loop_bias_coefficients_per_m4` estimates $B_R$ from refinement reports. `finite_loop_relative_error` computes $\rho_{\ell}$. `max_loop_scale_for_finite_loop_bound` computes $\ell_{\max}$.

**Limiting behavior:** the correction vanishes when $B_R=0$, when $\ell\to0$ with positive convergence, or when the loop scale is below a stated tolerance bound.

**Physical interpretation:** finite-loop bias can be modeled as a `finite-loop higher-curvature proxy` only if a physical cutoff or source-response mechanism makes $\ell$ nonzero in the effective description. If $\ell$ is merely estimator resolution, the term is a convergence diagnostic. If it maps to $R^2$ or another standard EFT operator, it is `known-framework-equivalent` unless a Pulse-specific coefficient is measured before comparison.

### 9.3 Channel Classification After Parameterization

| Channel | Minimal parameter | Executable status | Physical status before later tasks |
|---|---|---|---|
| Preferred-projection scalarization | $\lambda_P$ and $\rho_P$ | Computable from 05S2 scalarization helpers | Diagnostic-only unless mapped to a conserved preferred-frame response. |
| Finite-loop higher-curvature scale | $B_R$, $\rho_{\ell}$, and $\ell_{\max}$ | Computable from 05S2 refinement helpers | Resolution bound or known-framework proxy unless a physical finite cutoff is justified. |
| Squared-loss promotion | none admitted | Orientation check rejects it | Rejected as leading physical phase. |
| Torsion, nonlocal kernel, lattice memory, H7, cosmology | none admitted | No 05S2 observable | `unsupported-channel` or not applicable. |

The surviving executable parameterization is therefore useful but conservative. It can support bound propagation and falsification checks, but it does not yet produce a candidate new-physics signal.

## 10. 05S3.4 Executable Helpers

The focused helper implementation is in `src/pulse_model/correction_phenomenology.py`, with tests in `tests/test_correction_phenomenology.py`.

The helper API implements:

- `preferred_projection_parameter`, which returns signed $\lambda_P$, nonnegative $\rho_P$, the scalarization residual in $m^{-2}$, reference scalar curvature in $m^{-2}$, unit strings, sign, and classification
- `finite_loop_parameter`, which returns $B_R$, loop scale, scalar correction $B_R\ell^2$, relative size, $\ell_{\max}$, pass/fail status against an injected relative bound, unit strings, sign, and classification
- `require_supported_correction_channel`, which admits only `preferred-projection-scalarization` and `finite-loop-higher-curvature`
- `project_relative_correction_to_benchmark`, which linearly projects a dimensionless correction onto an existing benchmark value for bookkeeping only

The tests verify:

| Test target | Checked result |
|---|---|
| Preferred-projection normalization | the biased constant-curvature adversary gives $\lambda_P=-0.5$ and $\rho_P=0.5$ |
| Finite-loop bound propagation | the helper reproduces the 05S2 $\ell_{\max}$ scale and classifies loop scales below or above the injected bound |
| Zero finite-loop bias | $B_R=0$ gives zero correction and infinite $\ell_{\max}$ |
| Unsupported channels | squared-loss promotion, torsion, nonlocal kernels, and H7 vacuum energy are rejected |
| Dimension and sign sanity | nonfinite values, zero loop scale, and negative bounds raise `ValueError` |
| Known-physics projection | a dimensionless correction is projected onto the existing gravitational-redshift helper output without claiming a new field equation |

No external numerical constants are hidden in code. Source-derived bounds remain injected by callers or recorded in the appendix.

## 11. 05S3.5 Bounds Table

The bounds below use the 05S3 helper outputs and the constraint map from Section 8. A bound is counted as a pass only when the parameter and the observation have the same domain. Conditional mappings are not successes.

### 11.1 Retained-Channel Bounds

| Parameter | Units | Benchmark or observation | Bound or status | Source date | Provenance | Result | Remains testable |
|---|---:|---|---|---|---|---|---|
| $\rho_P$ | dimensionless | 05S2 biased constant-curvature adversary | internal local sanity bound $\rho_P \le 0.01$; measured adversary $\rho_P=0.5$ | June 7, 2026 | Internal repository evidence | Fail as clean scalarization; useful as diagnostic. | Yes, by computing plane weights and residuals from records. |
| $\lambda_P$ | dimensionless | weak-field preferred-frame PPN mapping | conditional bound $|M_1\lambda_P| \le 10^{-4}$ and $|M_2\lambda_P| \le 10^{-7}$ for model maps $M_1$ and $M_2$ | June 8, 2026 | External literature from Section 8 | Unconstrained as Pulse-specific physics until $M_1$ or $M_2$ is derived; direct unit mapping of $\rho_P=0.5$ would fail. | Yes, only after a macroscopic preferred-frame map exists. |
| $\lambda_P$ | dimensionless | compact-object preferred-frame mapping | conditional bound $|\hat M_1\lambda_P| \le 10^{-5}$ and $|\hat M_2\lambda_P| \le 10^{-9}$ | June 8, 2026 | External literature from Section 8 | Unconstrained as Pulse-specific physics; direct unit mapping would fail. | Yes, only after a strong-field response map exists. |
| $\lambda_P$ | dimensionless | GW170817 speed mapping | conditional bound $-3\times10^{-15} \le M_c\lambda_P \le 7\times10^{-16}$ | June 8, 2026 | External multi-messenger bound from Section 8 | Not applicable unless preferred projection changes tensor propagation speed. | Yes, if a propagation-speed map is derived. |
| $B_R$ and $\ell$ | $m^{-4}$ and $m$ | 05S2 finite-loop synthetic refinement | require $\rho_{\ell} \le 0.01$; for $B_R=6.0$ and $R_{\mathrm{ref}}=3.0$, $\ell_{\max}=0.07071067811865475$ m | June 7, 2026 | Internal repository evidence and 05S3 helper output | Pass for $\ell=0.035355339059327376$ m with $\rho_{\ell}=0.0025$; fail for $\ell=0.1414213562373095$ m with $\rho_{\ell}=0.04$. | Yes, by changing loop scale and checking convergence. |
| $\ell$ as a Yukawa range proxy | $m$ | short-distance inverse-square test | if a gravitational-strength Yukawa map is derived, ranges above 38.6 um are excluded at 95 percent confidence | June 8, 2026 | External literature from Section 8 | Conditional only; the 05S3 finite-loop estimator has no Yukawa-force map. | Yes, if a short-range force map is derived. |
| $B_R$ as GW dispersion proxy | $m^{-4}$ | LVK GWTC-3 tests | no evidence for dispersion or non-GR polarizations; $m_g \le 2.42\times10^{-23}$ eV/$c^2$ at 90 percent credibility | June 8, 2026 | External literature from Section 8 | Conditional only; no map from $B_R$ to dispersion or polarization has been derived. | Yes, if a waveform propagation map is derived. |
| $c_2=B_R/R_{\mathrm{ref}}^2$ and $a_2=c_2\ell^2$ | dimensionless and $m^2$ | higher-curvature EFT comparison | no Pulse-specific external range until a specific EFT operator and source-response convention are selected | June 8, 2026 | Framework comparison plus 05S2 caveat | Known-framework-equivalent or unconstrained; not a Pulse-specific signal. | Yes, as an EFT comparison after operator selection. |

### 11.2 Bound Outcome

The retained channels do not yet produce a candidate new-physics signal.

Preferred-projection scalarization has an actual internal bound as a record diagnostic. The adversarial value $\rho_P=0.5$ fails a predeclared one-percent local tolerance, which is useful because it exposes biased plane sampling instead of hiding it. External preferred-frame and GW-speed bounds are severe, but they constrain $\lambda_P$ only after a model maps the pulse-record projection to PPN parameters or propagation speed.

Finite-loop higher-curvature effects have an actual internal loop-scale bound. For the synthetic 05S2 coefficient, the helper gives $\ell_{\max}=0.07071067811865475$ m at one-percent relative tolerance. External inverse-square and GW bounds are conditional because 05S3 has not derived a Yukawa, dispersion, polarization, or field-equation map from $B_R$.

No coefficient is adjusted after seeing a bound. The executable tests keep the measured coefficient fixed while changing only the injected bound, so a pass means "below this predeclared tolerance," not "retuned to fit."

## 12. 05S3.6 Signal Windows

**Candidate new-physics window result:** no externally novel signal window survives 05S3.6.

Two falsifiable diagnostic windows survive. They are useful because they can fail future records cleanly, not because they currently predict a new external deviation.

### 12.1 Surviving Diagnostic Windows

| Window | Physical channel | Required correction size | Current bound | Proposed observable | Expected scaling | Degeneracies | Required data quality | Why not already excluded |
|---|---|---|---|---|---|---|---|---|
| Preferred-plane scalarization residual | anisotropic preferred-projection diagnostic | $\rho_P>\epsilon_R$ after calibration and full six-plane reconstruction, with $\epsilon_R$ predeclared | internal sanity bound uses $\epsilon_R=0.01$; external PPN/GW bounds apply only after a response map | compare $\Delta_{\mathrm{scal}}$ across deliberately changed loop-plane coverage and frame conventions | $\Delta_{\mathrm{scal}}=2\sum_{a<b}P_{ab}\eta_{aa}\eta_{bb}\widehat{K}_{ab}$ | biased loop sampling, calibration drift, ordinary Weyl anisotropy, frame convention | complete local two-plane records, artifact ledger, repeatable reweighting or independent loop families | it is not claimed as external physics; it is excluded only if it persists as a preferred-frame metric effect above external bounds. |
| Finite-loop convergence failure | finite-resolution or higher-curvature diagnostic | nonzero $B_R$ with $\rho_{\ell}>\epsilon_R$ at available $\ell$, or failure of positive convergence toward zero | internal finite-loop bound gives $\ell_{\max}=0.07071067811865475$ m for the 05S2 synthetic coefficient and $\epsilon_R=0.01$ | scalar curvature error versus loop scale across at least three refinement levels | $e_R(\ell)=B_R\ell^2+O(\ell^3)$ | finite-resolution bias, benchmark curvature error, missing planes, artifact correction, source-to-metric ambiguity | matched records at multiple loop scales, stable H2/H3 reconstruction, known synthetic or independently benchmarked target | it is a resolution requirement unless a physical cutoff is justified; as a diagnostic it is not excluded by external force or GW bounds. |

### 12.2 Conditional Non-Windows

| Candidate | What would be needed | Why it is not a current surviving signal |
|---|---|---|
| Preferred-frame external deviation | a derived map from $\lambda_P$ to PPN parameters or GW propagation speed, with conservation and covariance conditions satisfied | absent map; direct unit mapping would be severely bounded by preferred-frame and GW-speed tests. |
| Short-range finite-loop force | a derived map from $\ell$ or $B_R$ to a Yukawa-like gravitational-strength force range | absent map; if gravitational-strength and Yukawa-like, ranges above 38.6 um are already excluded. |
| Higher-curvature EFT signal | a specific operator, source-response convention, and premeasured coefficient such as $a_2$ | otherwise it is standard EFT language with a renamed coefficient, not a Pulse-specific prediction. |
| GW dispersion or extra polarization | a derived propagation equation linking $B_R$ to waveform dispersion, polarization, or graviton-mass-like behavior | absent map; current LVK tests report no evidence for these deviations and bound simple dispersion proxies. |

### 12.3 Window Verdict

The surviving windows are falsifiable record-quality and convergence windows:

- If $\rho_P$ remains above a predeclared tolerance after full coverage, calibration, and reweighting, the preferred-projection channel fails as clean scalarization.
- If $B_R\ell^2$ fails a predeclared loop-scale bound or does not converge away, the finite-loop channel fails as a continuum estimator.

Neither window currently supports a Pulse-specific external signal. The useful output is a no-window verdict for novelty, plus two concrete diagnostic tests that future records can pass or fail.

## 13. 05S3.7 Adversarial Review

The review below treats every surviving diagnostic window and every rejected or conditional channel as guilty until it survives mundane explanations. No row currently earns the label `pulse-specific`.

| Candidate or channel | Estimator artifact | Calibration artifact | Biased loop-plane sampling | Finite-resolution bias | Gauge or frame convention | EFT or PPN equivalence | H2/H3 scope risk | H6 source-to-metric ambiguity | H7 overclaim risk | Final label |
|---|---|---|---|---|---|---|---|---|---|---|
| Preferred-plane scalarization residual | possible if weights are chosen after seeing curvature | possible; must survive artifact ledger | central risk; $P_{ab}$ may just be bad coverage | secondary risk if loop families differ by scale | high unless frame convention is fixed and varied | maps to preferred-frame language only after extra model | H2/H3 must supply valid frames, areas, and defects | high for any metric-response claim | low if kept local; high if cosmology is inferred | diagnostic-only |
| Finite-loop convergence failure | possible if target curvature or error floor is chosen badly | possible if loop defects carry scale-dependent artifacts | possible if refinement changes plane coverage | central risk; may be ordinary finite resolution | moderate if loop scale is frame or reconstruction dependent | maps to standard higher-curvature EFT if promoted | H2/H3 must be stable across refinement levels | high for any source-to-metric claim | low if kept local; high if used for cosmology | diagnostic-only |
| Preferred-frame external deviation | not enough estimator evidence | not separable without response model | likely if inherited from $\lambda_P$ | not primary | high; needs macroscopic preferred frame | direct PPN equivalence if mapped | extends beyond current H2/H3 record layer | unresolved | possible if cosmology is claimed | no-go |
| Short-range finite-loop force | not produced by estimator alone | unknown | not primary | high; could be cutoff artifact | moderate | Yukawa or fifth-force equivalent if mapped | requires source-response beyond 05S2 | unresolved | low unless cosmology inferred | no-go |
| Higher-curvature EFT signal | not produced by estimator alone | unknown | not primary | high; $B_R$ may be resolution error | low if scalar invariant map exists | ordinary EFT equivalent | requires physical cutoff beyond H2/H3 estimator | unresolved | possible if used for dark energy | known-framework equivalent |
| GW dispersion or extra polarization | not produced by estimator alone | unknown | not primary | possible if finite-loop scale is physical | high; needs propagation convention | standard modified-dispersion or polarization test | beyond current H3 small-loop closure | unresolved | possible if cosmology inferred | no-go |
| Squared-loss promotion | yes; it is a reconstruction loss | possible | not primary | not primary | loses orientation sign | curvature-squared loss if promoted | violates 05S2 oriented-phase bridge | unresolved | possible if overclaimed | no-go |
| Torsion | no supported estimator observable | unknown | not primary | not primary | requires independent connection convention | known torsion frameworks exist | no H3 torsion observable admitted | unresolved | low unless cosmology inferred | no-go |
| Nonlocal kernel | no supported estimator observable | unknown | not primary | not primary | requires cross-cell convention | known nonlocal gravity equivalent if mapped | beyond local H2/H3 scope | unresolved | high if cosmology inferred | no-go |
| Lattice memory | no supported estimator observable | unknown | possible | central unsupported claim | depends on refinement gauge | known discretization artifact risk | beyond current refinement evidence | unresolved | low unless cosmology inferred | no-go |
| H7 vacuum energy or cosmology | out of scope | out of scope | out of scope | out of scope | out of scope | standard cosmology constraints would apply | not opened by 05S3 | unresolved | central risk | no-go |

### 13.1 Review Outcome

The review downgrades all surviving windows to `diagnostic-only`. The preferred-projection window is most vulnerable to biased loop-plane sampling and frame convention. The finite-loop window is most vulnerable to ordinary finite-resolution bias. Both are still useful because those vulnerabilities are measurable and falsifiable.

Every attempted external signal either lacks a response map, collapses to a known EFT or PPN parameter, or requires H2, H3, H6, or H7 assumptions that 05S3 is not allowed to extend. This makes the final verdict difficult to inflate: the only defensible primary label is `useful bounded diagnostic only`.

## 14. 05S3 Final Verdict

**Primary verdict label:** useful bounded diagnostic only.

05S3 is a useful level-up, but it does not produce a candidate new-physics signal. The correction phenomenology turns the 05S2 retained correction classes into dated, bounded, executable diagnostics:

- preferred-projection scalarization is now a signed and normalized record diagnostic with internal bounds and conditional external preferred-frame comparisons
- finite-loop higher-curvature scale effects are now loop-scale resolution requirements with explicit bound propagation
- external PPN, inverse-square, GW-speed, and GWTC-3 constraints are recorded with source dates and applicability limits
- unsupported channels are rejected before they can become speculative claims

The novelty gate rejects a stronger conclusion because every possible external signal either lacks a source-to-metric response map, reduces to standard EFT or PPN language, is vulnerable to sampling or finite-resolution artifacts, or would require H2, H3, H6, or H7 assumptions beyond their accepted scope.

### 14.1 Accepted Inputs

05S3 accepts these bounded inputs:

- H2 local frames, areas, and reconstruction scaffolds only inside accepted H2 scope
- H3 corrected small-loop defects only inside accepted H3 scope
- 05 and 05S as conditional geometry-action comparison and bridge inputs
- 05S2 pulse-record curvature estimates, scalarization residuals, refinement reports, and correction helpers
- external constraints dated June 8, 2026, only as bounds on matched observables
- synthetic benchmark records only as executable validation evidence

### 14.2 Rejected Overclaims

05S3 rejects these stronger claims:

- preferred-projection scalarization is already a physical preferred-frame force
- finite-loop bias is already a physical short-range force, GW dispersion, or higher-curvature field equation
- a coefficient can be chosen after seeing an observational bound and counted as a success
- squared-loss promotion is a leading geometry phase
- torsion, nonlocal kernels, lattice memory, H7 vacuum energy, or cosmology channels are supported by 05S2
- 05S3 derives the Einstein-Hilbert action, $G$, or $\Lambda$ from raw pulse data

### 14.3 Channel Status

| Channel | Final status |
|---|---|
| Preferred-projection scalarization | Useful bounded diagnostic; externally conditional only after a conserved preferred-frame response map. |
| Finite-loop higher-curvature scale | Useful bounded diagnostic; externally conditional only after a physical cutoff and source-response map. |
| Squared-loss promotion | Rejected as leading physical phase. |
| Preferred-frame external deviation | No-go without a response map; PPN-equivalent if mapped. |
| Short-range finite-loop force | No-go without a Yukawa or force-law map. |
| Higher-curvature EFT signal | Known-framework equivalent unless a Pulse-specific coefficient is measured before comparison. |
| GW dispersion or extra polarization | No-go without a propagation equation; externally bounded if mapped. |
| Torsion, nonlocal kernels, lattice memory | Unsupported channels. |
| H7 vacuum energy or cosmology | Not applicable in 05S3. |

### 14.4 Sourced Bounds Used

| Bound class | Bound or constraint | Source date | Status |
|---|---|---|---|
| Internal scalarization tolerance | $\rho_P \le 0.01$ for the representative local sanity bound; adversary $\rho_P=0.5$ fails | June 7, 2026 | Actual internal diagnostic bound. |
| Internal finite-loop tolerance | for $B_R=6.0$, $R_{\mathrm{ref}}=3.0$, and $\epsilon_R=0.01$, $\ell_{\max}=0.07071067811865475$ m | June 7, 2026 | Actual internal resolution bound. |
| Weak-field preferred frame | $|\alpha_1| \le 10^{-4}$ and $|\alpha_2| \le 10^{-7}$ | June 8, 2026 | Conditional external bound if $\lambda_P$ maps to PPN parameters. |
| Strong-field preferred frame | $|\hat\alpha_1| \le 10^{-5}$ and $|\hat\alpha_2| \le 10^{-9}$ | June 8, 2026 | Conditional external bound if compact-object response is derived. |
| Cassini light propagation | $\sigma_{\gamma}=2.3\times10^{-5}$, consistent with $\gamma=1$ | June 8, 2026 | Conditional weak-field metric-response guardrail. |
| GW170817 speed | $(v_{\mathrm{GW}}-v_{\mathrm{EM}})/c$ between $-3\times10^{-15}$ and $+7\times10^{-16}$ | June 8, 2026 | Conditional propagation-speed guardrail. |
| Short-distance gravity | gravitational-strength Yukawa ranges above 38.6 um excluded at 95 percent confidence | June 8, 2026 | Conditional short-range-force guardrail. |
| GWTC-3 GR tests | no evidence for dispersion or non-GR polarizations; $m_g \le 2.42\times10^{-23}$ eV/$c^2$ at 90 percent credibility | June 8, 2026 | Conditional waveform-propagation guardrail. |

### 14.5 Verification Commands

The final 05S3 verification uses:

```bash
uv run python -m unittest tests.test_correction_phenomenology
uv run python -m unittest tests.test_pulse_record_curvature
uv run python -m unittest discover -s tests
npm run typecheck
npm run build
```

The Markdown math guardrail scan also checks the 05S3 appendix for forbidden math delimiters, equation environments, labels, tags, and text macros.

### 14.6 Downstream Use

Downstream work may use 05S3 as:

- a novelty gate for 05S2 correction claims
- a bounded diagnostic layer for preferred-plane scalarization residuals
- a loop-scale resolution requirement for finite-loop effects
- a guardrail against unsupported external phenomenology

Downstream work must not use 05S3 as:

- a candidate new-physics prediction
- a derivation of the Einstein-Hilbert action
- an external preferred-frame, short-range force, GW-dispersion, or cosmology claim without a new response-map epic

### 14.7 Next Beads Work

After `sci-ql0.8` closes, the 05S3 epic `sci-ql0` can close if all child tasks are closed. The next project task should be selected from `bd ready` after that closure.

## 15. Task Sequence

The 05S3 tasks must be completed in order:

1. Define this correction-signal contract and novelty bar.
2. Map dated external constraints for the retained channels.
3. Derive the minimal effective parameterization for surviving channels.
4. Implement focused correction-phenomenology helpers and tests where executable checks are honest.
5. Bound retained correction parameters against known physics and external constraints.
6. Identify surviving falsifiable signal windows.
7. Run adversarial novelty and artifact review.
8. Write the final novelty and usefulness verdict.

The expected useful path is conservative: a correction should become externally novel only if it survives bounds, artifact review, and the Pulse-specificity bar. Otherwise 05S3 should strengthen Step 5 by producing bounded diagnostics, ruled-out channels, or a clean no-go.
