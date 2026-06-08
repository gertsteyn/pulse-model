---
title: H6S4-Q Minimal Non-Classical Pulse Geometry
sidebar_label: Minimal Quantum Pulse Geometry
sidebar_position: 7
---

# Appendix: H6S4-Q Minimal Non-Classical Pulse Geometry

**Parent hypothesis:** H6: Classical spacetime emerges from decohered pulse-history structure  
**Status:** Completed with final project-rule classification: conditional derivation  
**Purpose:** Test whether a scoped quantum mediator or non-classical geometry sector can carry source-branch pulse information without arbitrary ensemble labels.

---

## 1. Scope

H6S4-Q is the next H6 route after H6S4-C completed as a diagnostic finite stochastic classical pulse-potential comparator. H6S4-Q asks whether the missing carrier of branch information can be a non-classical mediator or geometry sector rather than a classical stochastic pulse-potential law.

The route is narrow. It must define a finite source, probe-clock, and mediator setup before implementation, or else state why no minimal non-classical version can pass the route gate. It must not continue H6S4-C except as a baseline comparator.

This appendix cites:

- [H6S1](./quantum_source_response_discriminator.md) for the weak-field quantum source/probe discriminator, ordinary noise separation, no-signaling checks, and conservation guardrails.
- [H6S2](./causal_pulse_response_kernel.md) for ensemble-decomposition invariance, local-record requirements, causal-domain labels, conservation ledgers, coefficient ledgers, and rejection of unsupported remote-basis marginal changes.
- [H6S3](./no_free_branch_variance.md) for the no-free-branch-variance theorem and the route ledger requiring records, stochastic classical pulse geometry, or non-classical geometry before branch variance is physical.
- [H6S4-C](./minimal_stochastic_pulse_geometry.md) for the stochastic classical finite pulse-potential comparator that remains diagnostic only.
- [review-5](../../reviews/review-5.md) for the decision to stop treating H6S4-C as the novelty route and test H6S4-Q as the next serious route.
- [frontier strategy](../../frontier_strategy.md) for the project rule that no new-physics claim is allowed without a fixed observable distinction from accepted GR and QM baselines.

H6S4-Q must end with exactly one final project-rule classification:

- controlled modification
- conditional derivation
- clean no-go
- diagnostic tool

The skeleton in this file is not yet any of those final results. It is the admission gate for the mediator candidate, code, and final review.

## 2. Route Gate

The minimum response shape is:

$$
R_Q(\rho_{\mathrm{source}}, \rho_{\mathrm{probe}}, \rho_{\mathrm{mediator}}, U_{\mathrm{source,mediator}}, U_{\mathrm{mediator,probe}}, D_{\mathrm{causal}}, L_{\mathrm{cons}}, L_{\mathrm{coeff}}, L_{\mathrm{reg}}, L_{\mathrm{rec}}) \mapsto P_{\mathrm{joint}}(r_S,r_M,r_C)
$$

Here:

- $\rho_{\mathrm{source}}$ is the finite local source density operator.
- $\rho_{\mathrm{probe}}$ is the finite probe-clock state or declared probe readout state.
- $\rho_{\mathrm{mediator}}$ is the mediator or non-classical geometry state.
- $U_{\mathrm{source,mediator}}$ is the declared source-mediator coupling.
- $U_{\mathrm{mediator,probe}}$ is the declared mediator-probe readout coupling.
- $D_{\mathrm{causal}}$ is the causal-domain declaration for the response.
- $L_{\mathrm{cons}}$ is the conservation ledger.
- $L_{\mathrm{coeff}}$ is the coefficient ledger.
- $L_{\mathrm{reg}}$ is the regulator ledger.
- $L_{\mathrm{rec}}$ is the record and artifact ledger.
- $P_{\mathrm{joint}}(r_S,r_M,r_C)$ is a normalized finite joint source, mediator, and probe record distribution.

The route gate is passed only if the response is:

- finite and normalized
- based on a declared mediator or geometry state space
- independent of arbitrary ensemble decompositions when no physical record selects them
- causal, with no remote-basis marginal dependence
- conservation-accounted
- coefficient-disciplined before external comparison
- regulator-declared
- separated from ordinary instrument noise, environmental decoherence, source-preparation spread, calibration drift, leakage, and postselection
- compared against required baselines before any novelty claim

Passing this gate still does not make the route an accepted law. The final verdict controls promotion.

## 3. Required Ledgers

| Ledger | Required content | Failure status |
|---|---|---|
| Mediator sector | Hilbert-space dimension, basis status, state, and whether the sector is a quantum mediator, non-classical geometry degree of freedom, or known-framework stand-in. | Missing mediator blocks the route. |
| Source-mediator coupling | Operator, domain, coefficient, and whether it can carry source branch information through quantum correlations rather than labels. | Missing coupling blocks candidate status. |
| Mediator-probe readout | Operator, probe record, and observable readout map. | Missing readout gives no admissible response distribution. |
| Branch-information carrier | Entanglement, correlation, local record, or declared causal channel that carries branch information. | Arbitrary ensemble labels are rejected. |
| Causal support | Whether the probe lies inside the causal domain or only a shared-future comparison is made. | Spacelike remote-basis marginal dependence is rejected. |
| Conservation | Energy, momentum, or pulse-accounting status, including mediator and environment terms if needed. | Missing account blocks promotion. |
| Coefficients | Names, dimensions, numerical role, and provenance of every coupling, scale, or amplitude. | Exploratory-only or fit-after-observation coefficients cannot support law status. |
| Regulators | Finite-size input, cutoff, smoothing, correlation length, or truncation and its provenance. | Undeclared regulator blocks candidate status. |
| Classical recovery | Limit in which the mediator response recovers the density-only weak-field or accepted classical baseline. | Missing recovery limit blocks law status. |
| Known-framework comparison | Relation to fixed-background quantum matter, linearized quantum gravity, gravitationally mediated entanglement models, pointer/decoherence bookkeeping, and H6S4-C. | Ordinary known theory in Pulse Model language cannot be promoted as new physics. |
| Artifact separation | Ordinary instrument noise, environmental decoherence, source spread, drift, leakage, and postselection. | Double-counting blocks promotion. |
| Fixed observable | Entanglement witness, visibility loss, conditional probe shift, covariance, timing correlation, or a precise statement that no observable survives. | No fixed observable forces diagnostic tool, conditional derivation, or clean no-go. |

## 4. Allowed Inputs

H6S4-Q may use:

| Input | Rule |
|---|---|
| Local source density operator | Allowed when the response depends on $\rho_{\mathrm{source}}$ and declared local operators, not on arbitrary decompositions. |
| Probe-clock state | Allowed as the finite target of the mediator readout and pulse-count observable. |
| Mediator or geometry state | Required for this route; it must be explicitly finite at the executable stage. |
| Source-mediator coupling | Allowed only when operator, coefficient status, and causal domain are declared before comparison. |
| Mediator-probe coupling | Allowed only when the probe readout map is declared before comparison. |
| Local records | Allowed only when physically present in the probe causal past, carried by a modeled causal channel, or compared later in a shared future. |
| Conservation ledger | Required for candidate promotion. |
| Coefficient ledger | Required for candidate promotion; fitted-after-observation coefficients are rejected. |
| Regulator ledger | Required when any truncation, cutoff, smoothing, finite size, or correlation scale affects the observable. |
| Artifact ledger | Required for ordinary noise, environmental decoherence, source-preparation spread, calibration drift, leakage, and postselection. |

## 5. Prohibited Inputs

H6S4-Q must not use:

- arbitrary ensemble branch labels as physical response inputs
- a remote basis choice as a spacelike cause of the local probe marginal
- hidden collapse or undeclared pointer selection
- a mediator sector named only in prose with no finite state space at the executable stage
- fit-after-observation coefficients
- undeclared conservation accounting
- undeclared regulators or truncations
- ordinary instrument noise relabeled as pulse geometry
- environmental decoherence double-counted as mediator physics
- source-preparation spread or calibration drift promoted to source response
- postselected correlations treated as unconditional probe marginals
- new-physics claims without a fixed observable that differs from accepted baselines

## 6. Required Baselines

Every H6S4-Q report must compare the proposed route against:

| Baseline | Role |
|---|---|
| Density-only expectation response | Conservative response depending on the local density operator or $\langle T_{\mu\nu}\rangle$, with no free branch variance. |
| H6S4-C stochastic pulse-potential comparator | Classical stochastic finite pulse-potential baseline that remains diagnostic only. |
| Pointer-record or collapse-selection response | Record-conditioned comparator; allowed only with declared local records, causal support, and ledgers. |
| Ordinary instrument noise | Probe or apparatus noise ledger kept separate from mediator response. |
| Fixed-background quantum matter | Quantum source and probe on a fixed background, with no dynamical mediator response. |
| Standard linearized quantum gravity | Known quantum mediator baseline for weak-field source-probe response. |
| Gravitationally mediated entanglement models | Known comparator for mediator-carried source-probe correlations and entanglement witnesses. |
| H6S3 no-free-branch-variance theorem | The no-go control: chosen ensemble notation alone cannot create physical branch variance. |

## 7. Observable Classes

The route may study these observable classes only after the ledgers and baselines are declared:

| Observable class | Admission rule |
|---|---|
| Source-probe covariance | Must arise from mediator-carried correlations, not arbitrary branch labels. |
| Mediator-source correlation | Must be computed from declared source-mediator coupling. |
| Mediator-probe correlation | Must be computed from declared mediator-probe readout. |
| Entanglement witness | Must state the witness, state space, and baseline relation to known quantum mediator models. |
| Conditional probe shift | Must condition on a local record, causal channel, or shared-future comparison. |
| Visibility loss | Must separate mediator response from ordinary decoherence and instrument noise. |
| Timing correlation | Must declare pulse-count or clock-readout map and artifact ledgers. |
| Pulse-count distribution | Must be a normalized finite distribution with known mean and variance baselines. |

## 8. Result-Class Discipline

H6S4-Q may be classified as a controlled modification only if it supplies a concrete mediator or geometry law before external comparison, with all ledgers complete, a classical recovery limit, and at least one fixed observable distinction from accepted baselines.

H6S4-Q may be classified as a conditional derivation only if it reduces to a known quantum mediator framework while giving a clean Pulse Model derivation or record contract. It must name the known framework recovered and must not claim new physics.

H6S4-Q must be classified as a clean no-go if the minimal non-classical route cannot pass the required assumptions, fails conservation or causal support, has no admissible mediator sector, depends on arbitrary ensemble labels, or cannot recover the accepted weak-field limit.

H6S4-Q must be classified as a diagnostic tool if it remains a route ledger, baseline comparator, admissibility test, or failure diagnostic without a promotable law.

Only one of these classifications may be the final H6S4-Q result.

## 9. Forbidden Overclaims

This appendix must not claim:

- a Pulse Model quantum geometry law exists before it is stated
- metric quantization has been proved
- collapse has been derived
- branch-specific metrics are physical by notation alone
- standard quantum mediator theory is new physics because it is written in pulse-count language
- ordinary decoherence, instrument noise, source spread, drift, leakage, or postselection is a mediator response
- exploratory coefficients support prediction status
- H6 classical-spacetime emergence is solved

## 10. Appendix Work Boundary

The route-scope skeleton is complete when this file states the H6S4-Q gate, allowed inputs, prohibited inputs, required ledgers, required baselines, observable classes, and final result-class discipline. Later sections must either define a minimal finite mediator candidate, derive the record distributions, implement executable checks, compare known frameworks, and run adversarial review, or record why that would be dishonest.

## 11. H6S4-Q.2 Minimal Finite Mediator Candidate

The minimal route candidate is a finite quantum mediator comparator. It is intentionally no more exotic than a source, mediator, and probe-clock system coupled by finite unitary maps. Its value for the Pulse Model is to test whether branch information can be carried by declared quantum correlations rather than by arbitrary ensemble labels.

The pre-code result class is:

> conditional-derivation candidate

It is not a controlled-modification candidate yet. If the construction remains equivalent to standard finite quantum mediator theory or weak-field linearized quantum gravity, the final result must stay a conditional derivation or diagnostic tool, not new physics.

### 11.1 State Spaces And States

The finite state spaces are:

$$
\mathcal{H}=\mathcal{H}_S\otimes\mathcal{H}_M\otimes\mathcal{H}_C
$$

where:

- $\mathcal{H}_S$ is the finite source Hilbert space.
- $\mathcal{H}_M$ is the finite mediator or non-classical geometry Hilbert space.
- $\mathcal{H}_C$ is the finite probe-clock Hilbert space.

The initial state is:

$$
\rho_0=\rho_S\otimes\rho_M\otimes\rho_C
$$

Here $\rho_S$, $\rho_M$, and $\rho_C$ are finite trace-one positive semidefinite density operators. For the smallest branch-information test, $\mathcal{H}_S$, $\mathcal{H}_M$, and $\mathcal{H}_C$ may each be two-dimensional. A coherent source preparation may be written:

$$
|\psi_S\rangle=\alpha |0\rangle+\beta |1\rangle
$$

but the response rule receives $\rho_S=|\psi_S\rangle\langle\psi_S|$ or another density operator, not an external ensemble label.

The mediator ready state may be:

$$
\rho_M=|m_0\rangle\langle m_0|
$$

and the probe-clock ready state may be:

$$
\rho_C=|c_0\rangle\langle c_0|
$$

These are finite candidate inputs, not claims that physical geometry is two-dimensional.

### 11.2 Couplings

Let $A_S$ be the finite source operator whose alternatives would classically source different weak fields. Let $B_M$ be the mediator response operator, and let $Q_C$ be the probe-clock readout operator.

The source-mediator coupling is:

$$
U_{SM}=\exp[-i g_{SM} A_S\otimes B_M\otimes I_C]
$$

The mediator-probe coupling is:

$$
U_{MC}=\exp[-i g_{MC} I_S\otimes B_M\otimes Q_C]
$$

The final state is:

$$
\rho_f=U_{MC}U_{SM}\rho_0 U_{SM}^{\dagger}U_{MC}^{\dagger}
$$

The couplings are admissible only when the source-mediator interaction lies in the declared source-to-mediator causal domain and the mediator-probe readout lies in the declared mediator-to-probe causal domain. A shared-future comparison may use correlations in the final records, but it is not a spacelike influence on the probe marginal.

### 11.3 Record Distribution

Choose finite readout projectors $\Pi_{r_S}^S$, $\Pi_{r_M}^M$, and $\Pi_{r_C}^C$ for source, mediator, and probe records. The joint record distribution is:

$$
P(r_S,r_M,r_C)=\mathrm{Tr}[(\Pi_{r_S}^S\otimes\Pi_{r_M}^M\otimes\Pi_{r_C}^C)\rho_f]
$$

The probe marginal is:

$$
P_C(r_C)=\sum_{r_S,r_M}P(r_S,r_M,r_C)
$$

The source-probe covariance, mediator-source correlation, mediator-probe correlation, and any entanglement witness must be computed from $\rho_f$ or from this finite record distribution. They may not be attached to an analyst-chosen ensemble decomposition of $\rho_S$.

### 11.4 Branch-Information Carrier

The branch-information carrier is quantum correlation between $S$, $M$, and $C$ after the declared couplings. The mediator can carry branch information only if $U_{SM}$ correlates the source alternatives with mediator degrees of freedom and $U_{MC}$ transfers mediator-dependent information into the probe readout or into shared-future correlations.

This is admissible because the carrier is in $\rho_f$ and its declared records. It is not an arbitrary label such as "the $Z$ ensemble" or "the $X$ ensemble" for the same local density operator.

If two preparation descriptions give the same $\rho_S$ and no local record selects one description, then the route requires the same local probe marginal:

$$
P_C(r_C|\rho_S,E_Z)=P_C(r_C|\rho_S,E_X)
$$

The equality is a no-signaling admissibility condition. Joint correlations may differ only when the physical preparation, mediator state, coupling, or record ledger differs, not when notation alone differs.

### 11.5 Ledgers For The Minimal Candidate

| Requirement | H6S4-Q.2 status |
|---|---|
| Mediator sector | Declared as finite $\mathcal{H}_M$ with state $\rho_M$. |
| Source state | Declared as finite $\rho_S$, with coherent two-level preparations allowed as density operators. |
| Probe-clock state | Declared as finite $\rho_C$ with probe readout projectors. |
| Source-mediator coupling | Declared as $U_{SM}$ with operator $A_S\otimes B_M$ and coefficient $g_{SM}$. |
| Mediator-probe coupling | Declared as $U_{MC}$ with operator $B_M\otimes Q_C$ and coefficient $g_{MC}$. |
| Branch-information carrier | Quantum correlations in $\rho_f$ and declared records, not ensemble labels. |
| Causal support | Source-to-mediator and mediator-to-probe links must be inside the declared causal domain; shared-future correlations are allowed only as comparisons. |
| Gauge or representation status | The finite basis is a representation for a comparator. No gauge-invariant continuum geometry is derived at this step. Any physical claim must be invariant under basis relabeling or inherited from a named known framework. |
| Conservation status | The closed finite unitary preserves trace and joint probability. Energy-momentum conservation is only conditionally accounted by the declared Hamiltonian or by inheritance from a known quantum mediator embedding. No independent Pulse Model stress-energy ledger is supplied. |
| Coefficient provenance | $g_{SM}$ and $g_{MC}$ must be fixed by a known weak-field mediator limit or independent calibration for conditional derivation status. Any new pulse-native coefficient is exploratory-only until derived before comparison. |
| Regulator provenance | Finite dimensions and any truncation are explicit regulators. No regulator-independent continuum limit is claimed. |
| Classical weak-field recovery | In the diagonal weak-coupling limit, the probe mean must reduce to the density-only weak-field response. This is inherited from the known mediator baseline, not newly derived here. |
| Observable status | Candidate observables are source-probe covariance, mediator correlations, entanglement witness, conditional probe shift, visibility loss, timing correlation, and pulse-count distribution. None is a new prediction until a fixed distinction from known baselines survives. |

### 11.6 Classical Weak-Field Recovery Target

The probe pulse-count readout may be attached to a finite readout value $\phi_C(r_C)$ by:

$$
N_C(r_C)=f_C T_C(1+\phi_C(r_C)/c^2)
$$

The recovery requirement is that the density-only mean is recovered when the mediator is treated in the accepted weak-field limit:

$$
\langle N_C\rangle=f_C T_C(1+\langle\Phi_C\rangle/c^2)
$$

This recovery condition is not a new Pulse Model law. It is the known weak-field baseline that the finite mediator comparator must match before any distributional observable can be considered.

### 11.7 Local No-Go Boundary

The chosen minimal finite candidate survives as a test object, so H6S4-Q is not locally no-go at this step. The candidate fails controlled-modification status unless later work supplies all of the following:

- a pulse-native mediator or geometry law distinct from known quantum mediator theory
- a gauge or representation-invariant physical interpretation
- full conservation accounting beyond closed finite-unitary probability preservation
- coefficient provenance fixed before external comparison
- regulator status beyond a finite toy truncation
- a fixed observable that differs from density-only, H6S4-C, pointer/decoherence, ordinary noise, and standard quantum mediator baselines

If later work cannot supply these, the honest final classification is conditional derivation, diagnostic tool, or clean no-go.

## 12. H6S4-Q.3 Record Distributions, Observables, And Baselines

The finite mediator candidate has an admissible record distribution whenever the state spaces, couplings, causal support, and readout projectors in Section 11 are declared. The projectors must be complete on their readout sectors, and the final density operator must remain trace one.

The joint distribution is:

$$
P(r_S,r_M,r_C)=\mathrm{Tr}[(\Pi_{r_S}^S\otimes\Pi_{r_M}^M\otimes\Pi_{r_C}^C)\rho_f]
$$

It must satisfy:

$$
\sum_{r_S,r_M,r_C}P(r_S,r_M,r_C)=1
$$

and:

$$
P(r_S,r_M,r_C)\ge 0
$$

If these conditions fail, the candidate has no admissible finite response report.

### 12.1 Local Marginals

The source, mediator, and probe marginals are:

$$
P_S(r_S)=\sum_{r_M,r_C}P(r_S,r_M,r_C)
$$

$$
P_M(r_M)=\sum_{r_S,r_C}P(r_S,r_M,r_C)
$$

$$
P_C(r_C)=\sum_{r_S,r_M}P(r_S,r_M,r_C)
$$

The local probe marginal $P_C(r_C)$ is the no-signaling-sensitive object. It may depend on $\rho_S$, $\rho_M$, $\rho_C$, declared couplings, and causal support. It may not depend on an arbitrary ensemble decomposition of the same $\rho_S$.

### 12.2 Correlation Observables

Let $X_S(r_S)$, $X_M(r_M)$, and $X_C(r_C)$ be declared finite readout values for source, mediator, and probe records. Their means are computed from the joint distribution, for example:

$$
\bar X_S=\sum_{r_S,r_M,r_C}X_S(r_S)P(r_S,r_M,r_C)
$$

The source-probe covariance is:

$$
\mathrm{Cov}_{SC}=\sum_{r_S,r_M,r_C}[X_S(r_S)-\bar X_S][X_C(r_C)-\bar X_C]P(r_S,r_M,r_C)
$$

The mediator-source covariance is:

$$
\mathrm{Cov}_{SM}=\sum_{r_S,r_M,r_C}[X_S(r_S)-\bar X_S][X_M(r_M)-\bar X_M]P(r_S,r_M,r_C)
$$

The mediator-probe covariance is:

$$
\mathrm{Cov}_{MC}=\sum_{r_S,r_M,r_C}[X_M(r_M)-\bar X_M][X_C(r_C)-\bar X_C]P(r_S,r_M,r_C)
$$

These covariances are candidate observables only when the readout maps and artifact ledgers are declared. They are diagnostic-only if they reproduce known quantum mediator correlations with renamed variables.

### 12.3 Entanglement Witness

A possible entanglement witness must be declared as a finite Hermitian operator $W_{SC}$ or $W_{SMC}$. For a source-probe witness, define:

$$
\rho_{SC}=\mathrm{Tr}_M(\rho_f)
$$

and:

$$
w_{SC}=\mathrm{Tr}(W_{SC}\rho_{SC})
$$

A negative witness value can be used only according to the declared witness convention. Even then, a source-probe entanglement witness is a known quantum-mediator observable unless H6S4-Q supplies a pulse-native distinction from standard gravitationally mediated entanglement models.

### 12.4 Conditional Probe Shift

The conditional probe distribution after a declared mediator record is:

$$
P(r_C|r_M)=P(r_M,r_C)/P_M(r_M)
$$

where $P_M(r_M)>0$. The conditional probe shift is:

$$
\Delta_C(r_M)=\sum_{r_C}X_C(r_C)P(r_C|r_M)-\sum_{r_C}X_C(r_C)P_C(r_C)
$$

This is admissible only as a local-record, causal-channel, or shared-future comparison. It is not an unconditional spacelike probe shift.

### 12.5 Visibility Loss

Visibility claims require a declared probe coherence functional $\mathcal{V}_C(\rho_C^f)$, where:

$$
\rho_C^f=\mathrm{Tr}_{SM}(\rho_f)
$$

The visibility difference is:

$$
\Delta\mathcal{V}_C=\mathcal{V}_C(\rho_C^f)-\mathcal{V}_C(\rho_C^0)
$$

This observable is diagnostic-only unless ordinary decoherence, instrument noise, source-preparation spread, calibration drift, leakage, and postselection are separated from mediator response.

### 12.6 Timing And Pulse-Count Observables

Let $N_C(r_C)$ be a declared finite pulse-count readout. The pulse-count mean is:

$$
\bar N_C=\sum_{r_C}N_C(r_C)P_C(r_C)
$$

The pulse-count variance is:

$$
V_N=\sum_{r_C}[N_C(r_C)-\bar N_C]^2P_C(r_C)
$$

Timing observables use a declared readout map $\tau_C(r_C)$ and the same finite distribution:

$$
\bar \tau_C=\sum_{r_C}\tau_C(r_C)P_C(r_C)
$$

A timing correlation with the source is:

$$
\mathrm{Cov}_{S\tau}=\sum_{r_S,r_M,r_C}[X_S(r_S)-\bar X_S][\tau_C(r_C)-\bar \tau_C]P(r_S,r_M,r_C)
$$

Pulse-count and timing observables are fixed candidate outputs only after the readout map, coefficients, causal support, and artifact ledger are declared.

### 12.7 Baseline Comparison

| Baseline | Same output as H6S4-Q | H6S4-Q difference status |
|---|---|---|
| Density-only expectation response | The weak-field mean $\bar N_C$ must reduce to the density-only mean in the accepted recovery limit. | Any surviving covariance, witness, visibility, or timing difference is beyond density-only response, but not automatically new physics. |
| H6S4-C stochastic pulse-potential comparator | H6S4-C gives a classical stochastic pulse-count distribution from a local potential operator. | H6S4-Q differs only if correlations or witnesses are mediator-carried quantum records rather than classical stochastic variance. This is diagnostic until known quantum mediator baselines are separated. |
| Pointer-record or collapse-selection response | Conditional shifts can look like record-conditioned branch response. | H6S4-Q is distinct only when the carrier is the declared mediator correlation in $\rho_f$, not hidden collapse or undeclared pointer selection. |
| Ordinary instrument noise | Observed variance, visibility loss, and timing jitter can be reproduced by apparatus noise. | H6S4-Q differs only after ordinary noise, drift, leakage, source spread, and postselection are ledgered separately. |
| Fixed-background quantum matter | Source and probe quantum states may evolve on a fixed background without dynamical mediator response. | H6S4-Q differs only when the mediator sector is dynamically coupled and affects joint records. |
| Standard linearized quantum gravity | Weak-field quantum mediator coupling can reproduce source-probe correlations and entanglement-style witnesses. | Current finite candidate is expected to be identical or weaker unless a pulse-native observable is later fixed. |
| Standard quantum-mediator entanglement models | The finite source-mediator-probe setup is structurally the same kind of mediator comparator. | Current status is conditional derivation or diagnostic tool, not new physics. |

### 12.8 Candidate-Difference Summary

The fixed outputs at this step are:

- admissible finite joint record distribution $P(r_S,r_M,r_C)$
- local probe marginal $P_C(r_C)$
- source-probe covariance $\mathrm{Cov}_{SC}$
- mediator-source covariance $\mathrm{Cov}_{SM}$
- mediator-probe covariance $\mathrm{Cov}_{MC}$
- optional entanglement witness value $w_{SC}$ or full-sector witness value
- conditional probe shift $\Delta_C(r_M)$
- visibility difference $\Delta\mathcal{V}_C$
- pulse-count mean $\bar N_C$ and variance $V_N$
- timing mean $\bar \tau_C$ and timing covariance $\mathrm{Cov}_{S\tau}$

The only possible candidate difference from density-only response is distributional or correlational. The only possible candidate difference from H6S4-C is quantum mediator-carried correlation rather than classical stochastic pulse-potential variance. Against standard linearized quantum gravity and standard quantum-mediator entanglement models, no fixed pulse-native distinction has been established at this step.

Therefore H6S4-Q.3 remains a conditional-derivation or diagnostic-comparator result before implementation and adversarial review.

## 13. H6S4-Q.6 Known-Framework Comparison

The finite H6S4-Q construction should be judged against known quantum and semiclassical mediator frameworks before any novelty claim. At this step the construction is a clean Pulse Model record contract for an ordinary finite quantum mediator, not a new physical law.

| Baseline | State space | Coupling | Recovery limit | Observable class | Coefficient status | Conservation status | H6S4-Q relation |
|---|---|---|---|---|---|---|---|
| Semiclassical expectation sourcing | Classical geometry sourced by $\langle T_{\mu\nu}\rangle$ or finite density-operator expectation data. | Source couples only through expectation values. | Recovers standard weak-field density-only response. | Probe mean and classical timing shift; no free branch covariance. | Fixed by known weak-field limit. | Conservation is at expectation-source level. | H6S4-Q is stronger as a comparator because it can represent mediator-carried correlations, but this is ordinary quantum-mediator structure, not a pulse-native law. |
| Fixed-background quantum matter | Quantum source and probe on a fixed classical background. | Matter evolves quantum mechanically without dynamical mediator response. | Recovers standard fixed-background QM. | Source/probe quantum statistics, ordinary decoherence, and apparatus observables. | Fixed by the chosen known matter Hamiltonian. | Conservation is the usual fixed-background or apparatus-ledger account. | H6S4-Q is distinct only when a declared mediator dynamically couples source and probe. Without that, it reduces to fixed-background quantum matter. |
| Standard linearized quantum gravity | Quantum matter plus weak quantum metric perturbation or graviton-like mediator sector. | Linearized gravitational coupling between source stress-energy and mediator, then mediator-probe response. | Recovers weak-field GR and ordinary quantum mediator behavior. | Source-probe correlations, phase shifts, entanglement witnesses, and timing correlations. | Fixed by Newton's constant, weak-field expansion, and known limit choices. | Conservation is inherited from the gauge-fixed or constraint-respecting linearized framework. | H6S4-Q is identical or weaker unless it supplies a pulse-native mediator law or observable not already contained in this baseline. |
| Gravitationally mediated entanglement mediator models | Finite source/probe systems plus a quantum mediator capable of entangling them. | Mediator-dependent phase or controlled interaction that can correlate source and probe. | Recovers standard nonrelativistic or weak-field mediator comparator. | Entanglement witness, source-probe covariance, conditional phase, and visibility. | Fixed by the chosen known mediator model or calibrated-before-test setup. | Conservation is model-dependent but belongs to the declared mediator Hamiltonian and apparatus ledger. | H6S4-Q is structurally the same kind of comparator. The finite API is a Pulse Model derivation of this structure, not a new prediction. |
| H6S4-C stochastic classical comparator | Classical stochastic pulse-potential values from a local finite potential operator. | Objective classical stochastic pulse-count response, not a quantum mediator. | Mean recovers density-only weak-field response. | Excess pulse-count variance and timing-jitter variance. | No free stochastic amplitude in the finite diagnostic; any new amplitude is exploratory-only. | Conservation is only conditionally accounted in the static finite weak-field arena. | H6S4-Q is distinct in carrier type: quantum correlations rather than classical stochastic variance. That distinction is diagnostic unless it survives known quantum-mediator comparison. |
| Pointer/decoherence bookkeeping | Source branch records, environmental records, or collapse placeholders. | Record-conditioned branch response after a declared local record or causal channel. | Recovers ordinary record-conditioned statistics and shared-future comparison. | Conditional probe shifts, branch correlations, visibility loss, and apparatus records. | Coefficients belong to the record, decoherence, or apparatus model. | Conservation requires environment, reservoir, or collapse-sector accounting when branch updates are discontinuous. | H6S4-Q is distinct only when the mediator carries the correlation without hidden collapse or undeclared pointer selection. Otherwise it is just pointer bookkeeping. |

### 13.1 Surviving Distinction Check

The current H6S4-Q candidate has these honest distinctions:

- It is stronger than density-only expectation sourcing as a diagnostic because it can encode source-probe correlations.
- It differs from H6S4-C because the carrier is quantum mediator correlation, not classical stochastic pulse-potential variance.
- It differs from pointer/decoherence bookkeeping only when the carrier is explicitly the mediator state and not a hidden local pointer branch.

These distinctions do not yet make new physics. Against standard linearized quantum gravity and gravitationally mediated entanglement mediator models, the finite candidate is ordinary quantum mediator theory written as a Pulse Model record contract.

No pulse-native fixed observable survives this comparison at H6S4-Q.6. Therefore there is no exact fixed observable to name as a new prediction. The pre-review classification remains:

> conditional derivation candidate, with diagnostic-comparator value

If later work claims a pulse-native distinction, it must name the exact observable, coefficient provenance, conservation account, regulator status, and baseline row that fails to reproduce it before external comparison.

## 14. H6S4-Q.7 Adversarial Physics And Ledger Review

This review stress-tests the finite quantum mediator route before the final verdict. The review asks whether H6S4-Q passes the H6 guardrails as a controlled modification, reduces to known quantum mediator theory, remains diagnostic, or fails cleanly.

| Issue | Classification | Review result |
|---|---|---|
| Ensemble-decomposition dependence | passed | The executable route receives density matrices and declared mediator records, not ensemble labels. Equivalent decompositions of the same $\rho_S$ give the same local probe marginal in the focused tests. |
| Remote-basis signaling | passed | A remote basis choice cannot change $P_C(r_C)$ unless it changes the local density operator, mediator state, coupling, or declared record ledger. |
| Hidden collapse or undeclared pointer selection | passed | The candidate uses finite unitary source-mediator and mediator-probe couplings. Conditional shifts require declared mediator records or shared-future comparison, not hidden collapse. |
| No preferred frame | conditional-derivation-only | The finite API itself is a Hilbert-space comparator, not a covariant spacetime construction. Any no-preferred-frame status is inherited from a named known framework such as linearized quantum gravity, not derived pulse-natively here. |
| Mediator Hilbert-space scope | diagnostic-only | A finite $\mathcal{H}_M$ is declared and executable, but it is a truncation or comparator sector. It does not establish a physical geometry Hilbert space for the Pulse Model. |
| Gauge or representation dependence | blocked | The finite basis is a representation choice. H6S4-Q has not supplied a gauge-invariant or representation-independent pulse-geometry law. This blocks controlled-modification status. |
| Conservation accounting | blocked | Closed finite unitarity preserves trace and joint probability, and known frameworks may supply Hamiltonian conservation. H6S4-Q does not supply an independent conserved Pulse Model stress-energy or geometry ledger. |
| Coefficient fitting | passed | The API blocks exploratory-only and fit-after-observation coefficient provenance. Complete reports use known-limit or independently fixed coefficients only. |
| Regulator dependence | diagnostic-only | Finite dimensions and truncations are explicit regulators. No regulator-independent continuum result is claimed. |
| Ordinary instrument noise | passed | Ordinary noise is ledgered separately and cannot be promoted to mediator response. |
| Environmental decoherence double-counting | passed | Visibility loss and conditional shifts are diagnostic unless environmental decoherence and apparatus ledgers are separated. |
| Source-preparation spread | diagnostic-only | Source spread can change $\rho_S$ or preparation records, but it is not a mediator law. It remains an artifact or preparation ledger. |
| Calibration drift | diagnostic-only | Drift can mimic timing or pulse-count shifts and must stay in the artifact ledger. It cannot supply a pulse-native observable. |
| Postselection | passed | The route distinguishes unconditional probe marginals from conditional or shared-future records. Postselected correlations are not treated as local probe marginals. |
| Classical weak-field recovery | conditional-derivation-only | The recovery target is declared as the density-only weak-field limit. The route inherits this from known quantum mediator baselines rather than deriving a new Pulse Model recovery theorem. |
| Equivalence to known quantum mediator models | conditional-derivation-only | The finite source-mediator-probe construction is structurally ordinary quantum mediator theory. This forces conditional derivation or diagnostic-tool status unless a pulse-native fixed observable is later supplied. |
| Overclaims of new physics | passed | The appendix and API keep `accepted_as_law` false and do not classify the route as a new prediction. |

### 14.1 Review Consequence

H6S4-Q passes the no-signaling, no-arbitrary-ensemble-label, hidden-collapse, coefficient, and artifact-separation gates. It does not pass the stronger controlled-modification gates for gauge or representation independence, independent conservation accounting, regulator independence, or baseline-distinct observable novelty.

The failed required gates force the final verdict away from controlled modification. The remaining honest final classes are conditional derivation, diagnostic tool, or clean no-go. Because the finite mediator candidate is executable and coherent, the route is not a clean no-go under the chosen minimal setup. Because it reduces to known quantum mediator structure while adding a useful Pulse Model record contract, the leading final verdict is conditional derivation unless the final project-status update chooses the broader diagnostic-tool label.

## 15. Final Verdict

Final project-rule classification:

> conditional derivation

H6S4-Q recovers the known finite quantum mediator framework used by standard weak-field quantum mediator and gravitationally mediated entanglement style models. In Pulse Model language, the recovered structure is a finite source-mediator-probe record contract:

$$
\rho_0=\rho_S\otimes\rho_M\otimes\rho_C
$$

with declared source-mediator and mediator-probe unitary couplings, followed by finite joint records and local probe marginals:

$$
P(r_S,r_M,r_C)=\mathrm{Tr}[(\Pi_{r_S}^S\otimes\Pi_{r_M}^M\otimes\Pi_{r_C}^C)\rho_f]
$$

The Pulse Model derivation value is narrow but useful:

- it states the no-arbitrary-ensemble-label contract for a non-classical mediator route
- it gives an executable finite record-distribution API
- it separates local probe marginals from shared-future and conditional correlations
- it keeps density-only, H6S4-C stochastic, pointer/decoherence, ordinary-noise, fixed-background, and standard quantum-mediator baselines explicit
- it blocks controlled-modification status when conservation, gauge or representation independence, regulator independence, coefficient provenance, or fixed baseline-distinct observables are missing

This does not claim new physics. It does not define a Pulse Model quantum geometry law, prove metric quantization, derive collapse, supply an independent conserved stress-energy response ledger, or produce a fixed pulse-native observable distinct from standard quantum mediator baselines.

The missing assumptions for promotion are:

- a gauge or representation-invariant Pulse Model mediator or geometry law
- independent conservation accounting beyond closed finite-unitary probability preservation or inheritance from known frameworks
- regulator status beyond finite truncation
- coefficient provenance fixed before external comparison
- a fixed observable not reproduced by density-only, H6S4-C, pointer/decoherence, ordinary-noise, fixed-background, standard linearized quantum gravity, or standard quantum-mediator baselines

Therefore H6S4-Q is complete as a conditional derivation and comparator. It may be used in H6S5 as the non-classical mediator baseline, but not as an accepted law or new prediction.
