---
title: H6P1 Pulse Closure Response Principle
sidebar_label: Pulse Closure Response
sidebar_position: 8
---

# Appendix: H6P1 Pulse Closure Response Principle

**Parent hypothesis:** H6: Classical spacetime emerges from decohered pulse-history structure
**Status:** Completed with final project-rule classification: diagnostic tool
**Purpose:** Attempt to define a Pulse-native source-response principle from gauge-invariant closed pulse and phase record defects.

---

## 1. Scope

H6P1 tests whether closed pulse or phase records can do more than diagnose curvature or branch response. The target is a source-response principle built from gauge-invariant loop closure defects.

The attempt is deliberately narrow. It may end in one of four classes:

| Class | Admission rule |
|---|---|
| Controlled modification | Allowed only if a conserved, coefficient-fixed response term is produced and at least one fixed observable is distinct from H6S4-C, H6S4-Q, and standard known baselines. |
| Conditional derivation | Allowed if the construction reduces to known stochastic semiclassical response or a known quantum mediator structure, with a useful Pulse Model record contract. |
| Clean no-go | Required if no invariant closure functional can be defined or if the response necessarily uses inadmissible gauge, ensemble, covariance, conservation, or coefficient inputs. |
| Diagnostic tool | Required if the work defines useful closure machinery but does not produce a promotable response law. |

The final H6P1 result is a diagnostic tool. A finite invariant closure functional and response-gradient analogue can be executed, but the construction does not supply a general conservation proof, continuum covariance law, or baseline-distinct observable.

## 2. Closed Pulse And Phase Defects

Let $e$ label oriented phase or pulse comparison edges. Let $\theta_e$ be the corrected edge record after calibration, ordinary instrument artifacts, matter phase artifacts, and finite-loop artifacts have been ledgered separately.

A closed record loop $L$ is represented by signed edge coefficients $s_{Le}$. The oriented closure defect is:

$$
\Delta_L = \sum_e s_{Le}\theta_e
$$

The signed coefficients must close at every node. For a pure node-potential relabeling to cancel, each node must receive zero net signed incidence from the loop. The finite API rejects loop records that are named as closed but do not satisfy this incidence check.

The sign convention is part of the loop record. Reversing the loop orientation sends:

$$
s_{Le} \mapsto -s_{Le}
$$

and therefore:

$$
\Delta_L \mapsto -\Delta_L
$$

This is the pulse-closure analogue of the oriented-loop phase result from 05S4. It keeps linear orientation information rather than immediately squaring the defect.

## 3. Closure Functional

Let $C_{LL'}$ be the intrinsic closure covariance of the loop defects. H6P1 uses the covariance-weighted functional:

$$
I[g,\rho,R] = \frac{1}{2}\sum_{LL'}\Delta_L C^{-1}_{LL'}\Delta_{L'}
$$

This is orientation-even. If every loop orientation is reversed, $\Delta$ changes sign, but $I$ is unchanged.

Ordinary instrument noise is not part of the intrinsic closure covariance. The finite prototype therefore carries a separate positive semidefinite ordinary-noise covariance ledger and does not use it in $C^{-1}$ for $I$. Observed variance may include apparatus noise, but closure-response promotion may not relabel apparatus noise as intrinsic pulse-geometry covariance.

For independent loop blocks, block-diagonal covariance gives additive contributions:

$$
I_{A\cup B}=I_A+I_B
$$

when $C_{AB}=0$ and the loop families share no covariance block.

## 4. Pure Gauge Relabeling

A pure edge relabeling by node potentials has the finite form:

$$
\theta_{ab} \mapsto \theta_{ab}+\lambda_b-\lambda_a
$$

For a closed loop:

$$
\sum_e s_{Le}(\lambda_{\mathrm{end}(e)}-\lambda_{\mathrm{start}(e)})=0
$$

Therefore $\Delta_L$ is unchanged by pure relabeling. If a proposed loop family fails this test, the closure functional is not a physical observable and H6P1 must be classified as clean no-go for that candidate.

The executable prototype checks this directly by applying node-offset relabelings to finite edge records and comparing the closure defects before and after relabeling.

## 5. Finite Source-Response Analogue

The continuum target would be:

$$
J_{\mathrm{pulse}}^{\mu\nu} = -\hbar\frac{\delta I}{\delta g_{\mu\nu}}
$$

H6P1 does not prove this tensor law.

The finite analogue introduces declared control parameters $g_a$ and edge sensitivities $d\theta_e/dg_a$. With fixed intrinsic covariance, the finite response component is:

$$
J_a = -\hbar\frac{dI}{dg_a}
$$

where:

$$
\frac{dI}{dg_a} = \sum_{LL'}\frac{d\Delta_L}{dg_a}C^{-1}_{LL'}\Delta_{L'}
$$

and:

$$
\frac{d\Delta_L}{dg_a} = \sum_e s_{Le}\frac{d\theta_e}{dg_a}
$$

This is executable, but it is not by itself a stress-energy tensor, a conserved source law, or a new gravitational equation. It is a finite closure-response diagnostic.

## 6. Promotion Ledgers

The finite response can be promoted only if all of these ledgers are complete before external comparison:

| Ledger | Required content | Failure consequence |
|---|---|---|
| Intrinsic covariance | A finite positive-definite closure covariance block $C_{LL'}$ or a continuum covariance rule with stated domain. | Missing covariance blocks promotion. |
| Gauge invariance | Closure defects unchanged by pure node-potential relabeling. | Failure gives clean no-go for the candidate. |
| Conservation | A proof that the response source is conserved, or a declared known framework that supplies conservation. | Missing proof blocks promotion. |
| Coefficients | Every coefficient fixed by derivation, known limit, or calibration before the test. | Exploratory or fit-after-observation coefficients are rejected. |
| Ensemble invariance | Equivalent decompositions of the same positive semidefinite trace-one $\rho$ give the same closure response unless a physical record selects a decomposition. | Ensemble dependence blocks promotion. |
| Artifact separation | Ordinary instrument noise, calibration drift, finite-loop artifacts, environmental decoherence, and postselection are ledgered separately. | Double-counting blocks promotion. |
| H6S4-C/Q baselines | The result is compared to stochastic semiclassical and quantum mediator structures. | No new-physics claim is allowed without a surviving baseline-distinct observable. |

## 7. Executable Prototype

The executable artifact is `src/pulse_model/pulse_closure_response.py`, with focused checks in `tests/test_pulse_closure_response.py`.

The finite API defines:

- `ClosureEdgeRecord` for corrected oriented edge records
- `ClosedPulseLoop` for signed edge-incidence loop records
- `ClosureCovarianceKernel` for intrinsic closure covariance plus a separate ordinary-noise ledger
- `ClosureMetricSensitivity` for finite edge sensitivities
- `closure_defect` and `closure_functional` for $\Delta_L$ and $I$
- `finite_closure_response` for $J_a=-\hbar dI/dg_a$
- `check_pure_gauge_invariance` for pure gauge relabeling
- `compare_closure_responses_for_decompositions` for ensemble-decomposition invariance
- `compare_closure_baselines` for H6S4-C and H6S4-Q baseline status

### 7.1 Required Checks

| Check | Executable result |
|---|---|
| Loop orientation reversal changes sign of $\Delta_L$ | Reversing all loop coefficients negates the closure defect. |
| Loop records close at nodes | Malformed loop incidence is rejected even when covariance is missing. |
| Closure functional is orientation-even | $I$ is unchanged under loop reversal. |
| Independent loop contributions add correctly | Block-diagonal covariance gives additive $I$. |
| Pure gauge relabeling leaves observables unchanged | Node-potential shifts leave closed-loop defects invariant. |
| Equivalent ensemble decompositions of the same $\rho$ give the same closure response | Z and X decompositions of the same density matrix give identical closure response reports. |
| Missing covariance kernel blocks promotion | The finite report has no functional and records the missing intrinsic covariance. |
| Missing conservation proof blocks promotion | `not-yet-classified` conservation blocks candidate status. |
| Arbitrary fitted coefficients are rejected | Fit-after-observation provenance blocks promotion. |
| Ordinary instrument noise is separated from intrinsic closure covariance | Ordinary noise changes the noise ledger but not intrinsic $I$. |
| H6S4-C and H6S4-Q baselines are compared | Baseline ledgers force conditional derivation or diagnostic status unless a fixed distinction survives. |

The tests also cover the four result classes. The controlled-modification branch exists only as a guarded classification path: complete covariance, conservation, coefficient, artifact, gauge, and baseline ledgers plus a fixed baseline-distinct observable are required. The H6P1 artifact itself does not satisfy that branch.

The guarded controlled-modification path requires the fixed observable to be distinct from both H6S4-C and H6S4-Q. A contradictory ledger that marks an observable as distinct while also reducing to either required baseline blocks promotion.

## 8. Baseline Comparison

### 8.1 H6S4-C

If the closure covariance $C_{LL'}$ is interpreted as an intrinsic stochastic covariance of closed pulse records, it plays the same structural role as the H6S4-C stochastic pulse-potential covariance or, in a fuller continuum setting, a stress-energy noise kernel.

That is a disciplined route, but it is not automatically new. Without an independent conserved stochastic closure source and a fixed observable not reproduced by stochastic semiclassical baselines, H6P1 reduces to a known stochastic-style comparator.

### 8.2 H6S4-Q

If the closure covariance or closure response is carried by a finite mediator record, then H6P1 reduces to the H6S4-Q pattern: source, mediator, and probe records with local marginals and shared-future correlations.

That can be a useful conditional derivation of a record contract, but it does not define a Pulse-native quantum geometry law unless it supplies a gauge-invariant mediator sector, independent conservation accounting, fixed coefficient provenance, and a baseline-distinct observable.

### 8.3 No New-Physics Claim

No H6P1 observable is promoted here. The finite response components are closure-gradient diagnostics. They can be used to compare candidate covariance and mediator stories, but they do not survive the H6S4-C and H6S4-Q baselines as a new prediction.

## 9. Adversarial Review

| Issue | Review result |
|---|---|
| Invariant closure observable | Passed for closed signed edge-incidence records. Pure node-potential relabeling leaves $\Delta_L$ unchanged. |
| Orientation handling | Passed. $\Delta_L$ is orientation-odd and $I$ is orientation-even. |
| Additivity | Passed in the finite independent block case. This does not prove continuum locality. |
| Covariance status | Diagnostic-only. A finite positive-definite covariance can be supplied, but H6P1 does not derive a general intrinsic closure covariance law. |
| Ordinary noise separation | Passed in the finite prototype. Ordinary instrument noise is ledgered separately from intrinsic closure covariance. |
| Conservation | Blocked for promotion. No independent proof shows that the closure-gradient response is a conserved tensor source. |
| Coefficients | Guarded. The API rejects fit-after-observation and exploratory-only coefficients for promotion. H6P1 does not derive a new coefficient. |
| Ensemble decomposition | Passed for the finite density-matrix response. Equivalent decompositions of the same $\rho$ give the same closure response. |
| Relation to H6S4-C | Conditional or diagnostic. Closure covariance resembles known stochastic response structure unless a distinct conserved law is supplied. |
| Relation to H6S4-Q | Conditional or diagnostic. Mediator-carried closure correlations reduce to known mediator record structure unless a distinct Pulse-native mediator law is supplied. |
| Baseline-distinct observable | Not supplied. This blocks controlled-modification status and any new-physics claim. |

## 10. Final Verdict

Final project-rule classification:

> diagnostic tool

H6P1 succeeds in defining useful finite closure machinery:

- gauge-invariant closed pulse or phase defects $\Delta_L$
- an orientation-even intrinsic covariance functional $I$
- additive independent-loop behavior
- pure gauge relabeling invariance
- ensemble-decomposition-invariant finite response reports
- a finite response-gradient analogue $J_a=-\hbar dI/dg_a$
- explicit blockers for missing covariance, missing conservation, fitted coefficients, ordinary-noise relabeling, and missing baseline comparison

H6P1 does not produce a controlled modification. It does not derive a conserved tensor response, a continuum intrinsic closure covariance law, a new pulse-native coefficient, or a fixed observable distinct from H6S4-C stochastic and H6S4-Q quantum mediator baselines.

The honest use of H6P1 downstream is as a diagnostic closure-response contract. It can test future covariance or mediator proposals, but it must not be treated as a new source-response law or a new physics prediction.
