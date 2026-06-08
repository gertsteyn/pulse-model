---
title: H6S4-C Minimal Stochastic Classical Pulse Geometry
sidebar_label: Minimal Stochastic Pulse Geometry
sidebar_position: 6
---

# Appendix: H6S4-C Minimal Stochastic Classical Pulse Geometry

**Parent hypothesis:** H6: Classical spacetime emerges from decohered pulse-history structure
**Status:** Completed with final project-rule classification: diagnostic tool
**Purpose:** Select the stochastic classical pulse-geometry route after H6S3 and state the candidate gate without pretending that a law has already been found.

---

## 1. Scope

H6S4-C asks whether the Pulse Model can define the smallest admissible stochastic classical source-response rule after the H6S1, H6S2, and H6S3 gates.

The route keeps geometry classical but allows an objective, causal pulse-geometry noise process if and only if that process is declared before external comparison and passes the ledgers below. It must not reuse arbitrary ensemble branch labels as physical source-response inputs.

This appendix cites:

- [H6S1](./quantum_source_response_discriminator.md) for the weak-field source/probe discriminator, branch-conditioned pulse-count diagnostics, ordinary instrument-noise separation, no-signaling checks, and conservation guardrails.
- [H6S2](./causal_pulse_response_kernel.md) for ensemble-decomposition invariance, causal-domain labels, conservation ledgers, coefficient ledgers, and rejection of unsupported remote-basis marginal changes.
- [H6S3](./no_free_branch_variance.md) for the no-free-branch-variance theorem and the route ledger requiring records, stochastic classical pulse geometry, or non-classical geometry before branch variance is physical.
- [review-4](../../reviews/review-4.md) for the decision to try H6S4-C first and to stop adding guardrail-only H6 work unless this route fails.

H6S4-C must end with exactly one final project-rule classification:

- controlled modification
- clean no-go
- diagnostic tool

The skeleton in this file is not yet any of those final results. It is the admission gate for later proof and code.

## 2. Candidate Gate

The minimum response shape is:

$$
R_C(\rho_{\mathrm{local}}, O_{\mathrm{source}}, P_{\mathrm{local}}, D_{\mathrm{causal}}, L_{\mathrm{cons}}, L_{\mathrm{coeff}}, L_{\mathrm{reg}}) \mapsto P(N_C)
$$

Here:

- $\rho_{\mathrm{local}}$ is the local source density operator or an explicitly declared local source record.
- $O_{\mathrm{source}}$ is the declared source operator or local source-record observable used by the response.
- $P_{\mathrm{local}}$ is the local pulse-record input available to the probe response.
- $D_{\mathrm{causal}}$ is the declared causal domain.
- $L_{\mathrm{cons}}$ is the conservation ledger.
- $L_{\mathrm{coeff}}$ is the coefficient ledger.
- $L_{\mathrm{reg}}$ is the regulator ledger.
- $P(N_C)$ is a normalized finite probe pulse-count marginal.

The candidate gate is passed only if the response rule is:

- normalized
- finite
- decomposition-invariant when no physical selector exists
- causal
- conservation-accounted
- coefficient-disciplined
- regulator-declared
- separated from ordinary instrument noise
- compared against the required baselines before external comparison

Passing this gate still does not make the rule an accepted law. The final verdict controls promotion.

## 3. Allowed Inputs

H6S4-C may use:

| Input | Rule |
|---|---|
| Local density operator | Allowed when the response depends only on $\rho_{\mathrm{local}}$ and declared local operators. |
| Local source records | Allowed only when the record exists in the probe causal past, arrives through a modeled causal channel, or is used in shared-future comparison. |
| Local pulse records | Allowed as probe-accessible record data, not as an undeclared branch selector. |
| Source operators | Allowed when the operator, units, domain, and coefficient status are declared before comparison. |
| Causal domain | Required for every response report. |
| Conservation ledger | Required for candidate status. |
| Coefficient ledger | Required for candidate status; fit-after-observation coefficients are rejected. |
| Regulator ledger | Required when any cutoff, smoothing, finite-size parameter, or correlation scale affects the observable. |
| Artifact ledger | Required for ordinary instrument noise, environmental decoherence, source-preparation spread, calibration drift, and postselection. |

## 4. Prohibited Inputs

H6S4-C must not use:

- arbitrary ensemble branch labels as physical response inputs
- remote-basis choices as spacelike causes of the probe marginal
- hidden collapse or pointer selection not declared as a physical record route
- fit-after-observation coefficients
- undeclared conservation accounting
- undeclared regulators or smoothing scales
- ordinary instrument noise relabeled as pulse-geometry noise
- environmental decoherence double-counted as stochastic geometry
- external target data to choose the law
- H7, finite-loop, geometry-action, or additional guardrail-only work as a substitute for the H6S4-C route decision

## 5. Required Ledgers

The later H6S4-C law or no-go theorem must declare these ledgers before code or promotion.

| Ledger | Required content | Failure status |
|---|---|---|
| Stochastic variable | The noise variable or stochastic process, its domain, and whether it is classical, objective, and local. | Missing law blocks controlled-modification status. |
| Coupling target | Whether the process couples to $T_{\mu\nu}$, phase density, pulse records, curvature records, potential-operator variance, or another justified local object. | Missing target blocks candidate status. |
| Causal support | The support of noise correlations and whether the probe lies inside the causal domain. | Spacelike remote-basis marginal dependence is rejected. |
| Conservation | Energy-momentum or pulse-accounting status, including environment or reservoir terms if needed. | Missing account blocks candidate status. |
| Coefficients | Names, dimensions, numerical role, and provenance of every amplitude, coupling, or scale. | Fit-after-observation is rejected; exploratory-only cannot support prediction. |
| Regulators | Finite-size input, cutoff, smoothing, or correlation length, with provenance. | Undeclared regulator blocks candidate status. |
| GR and QM recovery | Limit in which the response reduces to the density-only or standard semiclassical baseline. | Missing recovery limit blocks law status. |
| No-signaling | Demonstration that equivalent decompositions of the same $\rho_{\mathrm{local}}$ give the same probe marginal without records. | Remote-basis marginal change is rejected. |
| Artifact separation | Ordinary instrument noise, environmental decoherence, source spread, drift, leakage, and postselection are separated from pulse-geometry noise. | Double-counting blocks candidate status. |
| Observable | Fixed excess pulse-count variance, covariance, visibility loss, timing jitter, or a precise statement that no such observable survives. | No fixed observable forces diagnostic-only or clean no-go. |

## 6. Required Baselines

Every later H6S4-C report must compare the proposed route against:

| Baseline | Role |
|---|---|
| Density-only expectation response | Conservative response depending on $\rho_{\mathrm{local}}$ or $\langle T_{\mu\nu}\rangle$, with no free branch variance. |
| Invalid ensemble branch response | Rejected bad rule used to expose decomposition artifacts. |
| Pointer-record response | Record-conditioned comparator; allowed only with declared local records, causal support, and ledgers. |
| Ordinary instrument noise | Probe or apparatus noise ledger kept separate from pulse-geometry noise. |
| H6S3 no-free-branch-variance theorem | The no-go control: chosen ensemble notation alone cannot create physical branch variance. |
| Known stochastic semiclassical gravity | Conceptual comparator to check whether H6S4-C is only a renamed known framework. |

## 7. Result-Class Discipline

H6S4-C may be classified as controlled modification only if it supplies a concrete law before external comparison, with all ledgers complete and at least one fixed diagnostic observable.

H6S4-C must be classified as clean no-go if the minimal stochastic classical route cannot pass the required assumptions, collapses into an already-known framework without a distinct Pulse Model contribution, or requires an inadmissible input such as remote-basis dependence, hidden collapse, or fit-after-observation coefficients.

H6S4-C must be classified as diagnostic tool if the work remains a route ledger, baseline comparator, or failure diagnostic without a promotable law.

Only one of these classifications may be the final H6S4-C result.

## 8. Forbidden Overclaims

This appendix must not claim:

- a Pulse Model stochastic source-response law exists before it is stated
- metric quantization has been proved
- collapse has been derived
- branch-specific metrics are physical by notation alone
- ordinary instrument noise is new pulse-geometry noise
- an exploratory coefficient is a prediction
- a stochastic classical route is novel merely because it uses pulse-count language
- H6 classical-spacetime emergence is solved

## 9. Appendix Work Boundary

The route-scope skeleton is complete. The next sections state the minimal finite stochastic candidate and keep final status open until executable checks and adversarial review are complete.

## 10. H6S4-C.2 Minimal Finite Stochastic Candidate

H6S4-C does not choose an arbitrary ensemble branch distribution. The minimal candidate is a finite weak-field stochastic pulse-potential response defined by the spectral distribution of a declared local potential operator.

Let $\hat{\Phi}_C$ be a finite Hermitian pulse-potential operator for the source degrees of freedom inside the declared causal domain of probe clock $C$. Let its spectral values and projectors be $\phi_k$ and $\Pi_k$. The local source state is $\rho_{\mathrm{local}}$.

The objective classical stochastic variable is:

$$
\Phi_C^{\mathrm{stoch}}=\phi_k
$$

with probabilities:

$$
p_k=\mathrm{Tr}(\rho_{\mathrm{local}}\Pi_k)
$$

The probe pulse-count values are:

$$
N_{C,k}=f_C T_C(1+\phi_k/c^2)
$$

The response marginal is:

$$
P(N_C=N_{C,k})=p_k
$$

Equal pulse-count values are merged into one distribution point. No random sampling is part of the executable rule; the API must return the finite distribution and its deterministic moments.

The density-only baseline uses:

$$
\bar{\Phi}_C=\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C)
$$

and:

$$
N_{\mathrm{exp}}=f_C T_C(1+\bar{\Phi}_C/c^2)
$$

The stochastic variable may be written as a zero-mean pulse-count fluctuation around the density-only mean:

$$
\delta N_C=f_C T_C(\Phi_C^{\mathrm{stoch}}-\bar{\Phi}_C)/c^2
$$

This gives the fixed excess pulse-count variance:

$$
V_C^{\mathrm{geom}}=(f_C T_C/c^2)^2[\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C^2)-\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C)^2]
$$

The corresponding timing-jitter variance is:

$$
\sigma_{\tau,C}^2=(T_C/c^2)^2[\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C^2)-\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C)^2]
$$

No visibility-loss law is claimed at this step. H6S5 may map this variance to visibility only if it supplies a separate interferometer or clock-readout observable map.

### 10.1 Coupling Target

The H6S4-C.2 candidate couples to potential-operator variance in the finite weak-field source/probe arena:

$$
\mathrm{Var}_{\rho}(\hat{\Phi}_C)=\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C^2)-\mathrm{Tr}(\rho_{\mathrm{local}}\hat{\Phi}_C)^2
$$

It does not directly couple to phase density, pulse records, curvature records, or arbitrary branch labels. Pulse records are probe readouts and ledger inputs, not a hidden branch selector.

In a later covariant theory the analogous object would have to be a conserved stress-energy noise kernel for $T_{\mu\nu}$. H6S4-C.2 does not claim that full covariant law.

### 10.2 Causal Support

The operator $\hat{\Phi}_C$ is admissible only when its construction is tied to source data in the declared causal domain of probe $C$, or to records compared in a shared causal future. A spacelike remote basis choice may change an ensemble description of $\rho_{\mathrm{local}}$, but it cannot change the spectral probabilities $p_k$ unless it changes $\rho_{\mathrm{local}}$ or a declared local record.

Therefore equivalent decompositions of the same local state give the same stochastic response:

$$
R_C(E_Z)=R_C(E_X)
$$

whenever:

$$
\rho(E_Z)=\rho(E_X)
$$

The candidate has no remote-basis marginal dependence.

### 10.3 Ledger Status

| Requirement | H6S4-C.2 status |
|---|---|
| Stochastic variable | Declared as the spectral classical variable $\Phi_C^{\mathrm{stoch}}$ of the local finite potential operator. |
| Coupling target | Potential-operator variance in the finite weak-field source/probe arena. |
| Causal support | Declared local causal-domain operator; no spacelike remote-basis dependence. |
| Conservation | Conditionally branchwise conserved only in the static finite weak-field arena where each spectral potential value comes from a conserved source record. Outside that arena the conservation status is not-yet-classified and blocks law promotion. |
| Coefficients | No free stochastic amplitude. The pulse response coefficient is fixed by the weak-field redshift factor $f_C T_C/c^2$. Any extra amplitude is exploratory-only and cannot support prediction status. |
| Regulator | No new regulator beyond finite operator dimension and any H6S1 softening or finite-size source input. Any softening radius must be declared before comparison and cannot be fitted after observation. |
| GR recovery | The mean response is the density-only weak-field response $N_{\mathrm{exp}}$. |
| QM recovery | If $\rho_{\mathrm{local}}$ is sharp in $\hat{\Phi}_C$, or if $\hat{\Phi}_C$ has zero variance on the state, the stochastic excess variance vanishes. No collapse of the source state is claimed. |
| Observable | Fixed excess pulse-count variance $V_C^{\mathrm{geom}}$ and timing-jitter variance $\sigma_{\tau,C}^2$. |

### 10.4 Comparison With Known Stochastic Semiclassical Gravity

This candidate is conceptually close to stochastic semiclassical gravity: the classical response receives objective noise whose covariance is fixed by quantum source fluctuations. In the finite weak-field setting, $\hat{\Phi}_C$ is the local potential analogue of a stress-energy fluctuation source.

That closeness is a strength and a risk. It keeps the route physically disciplined, but it also means H6S4-C must not claim novelty merely for renaming a known stochastic semiclassical idea in pulse-count language. The possible Pulse Model contribution is narrower: a finite pulse-record response contract, strict no-ensemble-label gate, and a fixed pre-comparison pulse-count variance observable.

If later review finds that this is only known stochastic semiclassical gravity with renamed variables, the final H6S4-C verdict must downgrade to diagnostic tool or clean no-go rather than controlled modification.

### 10.5 Pre-Code Result Class

The H6S4-C.2 pre-code result is a controlled modification candidate, not an accepted law. It supplies a concrete finite stochastic response rule and a fixed excess variance before code is written.

The candidate must still be blocked or downgraded if executable checks or adversarial review find any of these failures:

- non-normalized or non-finite response distribution
- decomposition dependence for the same $\rho_{\mathrm{local}}$
- hidden use of arbitrary ensemble branch labels
- missing conservation ledger outside the static finite weak-field arena
- fit-after-observation coefficient
- undeclared regulator
- ordinary instrument noise double-counted as pulse-geometry noise
- equivalence to known stochastic semiclassical gravity with no distinct Pulse Model content

## 11. H6S4-C.4 Baseline And Failure Classification

The executable H6S4-C API compares the candidate against the required baselines rather than treating the stochastic variance as self-justifying.

| Baseline | H6S4-C handling rule |
|---|---|
| Density-only expectation response | The stochastic response must have the same mean as the density-only response. Its only proposed difference is the fixed excess pulse-count variance. |
| Invalid ensemble branch response | Kept only as a rejected diagnostic. Its variance may expose a branch-label artifact but is never the stochastic law. |
| Pointer-record response | Kept only as a record-conditioned comparator. Pointer variance requires records and ledgers and is not H6S4-C stochastic geometry. |
| Ordinary instrument noise | Added only to observed variance as an apparatus ledger. It remains separate from $V_C^{\mathrm{geom}}$. |
| H6S3 no-free-branch-variance theorem | Equivalent decompositions of the same $\rho_{\mathrm{local}}$ must give the same stochastic response when no physical selector exists. |

Route-failure classification follows these rules:

- missing coefficient provenance, conservation ledger, regulator provenance, causal support, or no-signaling guardrail gives `blocked`
- a diagnostic failure against H6S3 gives `clean-no-go-candidate`
- complete ledgers plus positive fixed excess variance gives `controlled-modification-candidate`
- zero fixed excess variance or missing no-free comparison gives `diagnostic-only`
- `accepted_as_law` remains false because the final H6S4-C verdict controls promotion

## 12. H6S4-C.6 Adversarial Physics And Ledger Review

This review stress-tests the finite stochastic pulse-potential candidate before the final verdict. The review distinguishes a coherent finite diagnostic from an accepted stochastic classical source-response law.

| Issue | Classification | Review result |
|---|---|---|
| Ensemble-decomposition dependence | passed | The response depends on $\rho_{\mathrm{local}}$ and the declared local potential operator, not on an analyst's ensemble labels. Equivalent Z and X decompositions of the same density operator give the same response. |
| Remote-basis signaling | passed | A spacelike remote basis choice cannot change the probe marginal unless it changes the local density operator or a declared local record. The API comparison keeps the stochastic response invariant under equivalent decompositions. |
| Hidden collapse or pointer selection | passed | The candidate samples an objective classical potential variable for the response report but does not collapse the source state, select a pointer branch, or import pointer-record variance as the law. Pointer records remain a separate comparator. |
| Conservation accounting | blocked | Conservation is only conditionally accounted in the static finite weak-field arena where each spectral potential value is tied to a conserved source record. H6S4-C does not supply a general conserved stochastic source or stress-energy noise law. This blocks accepted-law and controlled-modification promotion. |
| Coefficient fitting | passed | The finite candidate has no free stochastic amplitude. The only pulse response coefficient is fixed by the weak-field redshift factor. Any added amplitude is classified as exploratory-only or fit-after-observation rejected. |
| Regulator dependence | diagnostic-only | The finite operator and any H6S1 softening are declared, but H6S4-C does not prove regulator-independent continuum behavior. This is acceptable for a finite diagnostic and insufficient for a law. |
| Ordinary noise double-counting | passed | Ordinary instrument noise is carried as a separate observed-variance ledger and is not included in $V_C^{\mathrm{geom}}$. |
| Artifact ledgers | diagnostic-only | The API requires an artifact ledger and the tests separate invalid ensemble, pointer-record, and ordinary-noise baselines. Real experimental artifact subtraction is not supplied at H6S4-C, so external prediction remains blocked. |
| GR and QM recovery | passed | The mean equals the density-only weak-field response, and the stochastic excess variance vanishes when $\rho_{\mathrm{local}}$ is sharp in $\hat{\Phi}_C$ or when the potential variance is zero. No source-state collapse is claimed. |
| Equivalence to known stochastic semiclassical gravity | diagnostic-only | The candidate is best understood as a finite weak-field pulse-record analogue of stochastic semiclassical gravity, with potential fluctuations replacing a full stress-energy noise kernel. That makes it disciplined but not a distinct accepted new framework. |
| Overclaims of new physics | passed | The appendix and API keep `accepted_as_law` false and reserve promotion for the final verdict. The present result must not be described as a new law or external prediction. |

The adversarial review blocks a final controlled-modification verdict. The remaining honest final classifications are diagnostic tool or clean no-go.

The review does not force a clean no-go for all H6S4 routes. The finite stochastic response is coherent as a route diagnostic, passes decomposition and no-signaling tests, and produces a fixed variance comparator. The failed assumption is stronger: H6S4-C has not supplied a general conserved stochastic classical source-response law distinct from known stochastic semiclassical gravity.

## 13. Final Verdict

Final project-rule classification:

> diagnostic tool

H6S4-C supplies a finite stochastic pulse-potential diagnostic, not an accepted stochastic classical source-response law.

The missing assumption is a general conserved stochastic classical source-response law distinct from known stochastic semiclassical gravity. The finite candidate is coherent inside the static weak-field spectral-potential arena, but its conservation ledger is not general, its continuum or regulator-independent status is not proved, and its structure is too close to known stochastic semiclassical gravity to claim a distinct controlled modification.

The accepted H6S4-C outputs are:

- a route-scope appendix and final diagnostic verdict
- a deterministic finite spectral-potential response API in `src/pulse_model/stochastic_pulse_geometry.py`
- focused tests in `tests/test_stochastic_pulse_geometry.py`
- a fixed diagnostic excess pulse-count variance comparator
- explicit baseline comparisons against density-only, invalid ensemble branch, pointer-record, ordinary-noise, and H6S3 no-free-branch-variance baselines

The rejected H6S4-C overclaims are:

- no accepted stochastic classical pulse-geometry law
- no controlled modification
- no new prediction
- no external comparison authorization
- no solution to the full quantum source-response problem

H6S4-C does not block all H6S4 routes. Pointer-record or collapse-selection routes still need a conservation-accounted selection law, and non-classical geometry or mediator routes still need a scoped sector and recovery limit. H6S5 may use the H6S4-C finite response only as a diagnostic observable comparator, not as a promoted law.
