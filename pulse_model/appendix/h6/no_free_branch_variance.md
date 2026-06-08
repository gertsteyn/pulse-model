---
title: H6S3 No Free Branch Variance Theorem
sidebar_label: No Free Branch Variance
sidebar_position: 5
---

# Appendix: H6S3 No Free Branch Variance Theorem

**Parent hypothesis:** H6: Classical spacetime emerges from decohered pulse-history structure  
**Status:** Completed with final project-rule classification: diagnostic tool  
**Purpose:** Turn the H6S2 ensemble-invariance gate into a strict no-free-branch-variance target for quantum source-response proposals.

---

## 1. Scope

H6S3 asks a narrower question than the full source-response problem:

> Can a probe-clock pulse distribution gain physical branch-dependent variance merely because an analyst chooses one ensemble decomposition of a fixed local density operator?

The target answer is no. A branch variance attached only to notation is not a physical source-response variance. Physical branch-dependent variance must be supported by one of these structures:

- a local pointer record or collapse-selection record
- an objectively stochastic classical pulse-geometry law
- a non-classical geometry or mediator sector

H6S3 is therefore a theorem and route-ledger step. It is not a pulse-native source-response law, not a metric-quantization proof, and not a choice of the later H6S4 route.

## 2. Inputs From H6S1 And H6S2

H6S3 cites [H6S1](./quantum_source_response_discriminator.md) as the weak-field diagnostic. H6S1 supplies the controlled source/probe arena, branch-conditioned pulse counts, probe-count variance diagnostics, ordinary instrument-noise ledgers, and no-signaling and conservation guardrails.

H6S3 cites [H6S2](./causal_pulse_response_kernel.md) as the ensemble-invariance admissibility gate. H6S2 supplies finite-dimensional density operators, equivalent ensemble decompositions, causal-domain labels, conservation and coefficient ledgers, and the rule that an admissible response cannot depend on an arbitrary decomposition of the same local density operator without local records or causal support.

The finite local source state may admit two ensemble descriptions:

$$
\rho_S=\sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

$$
\rho_S=\sum_j q_j |\phi_j\rangle\langle\phi_j|
$$

The H6S3 target concerns only the case where both descriptions represent the same local $\rho_S$ and no additional physical structure selects one decomposition as the branch basis available to the probe response.

## 3. Working Terms

**Branch variance** means variance in the probe pulse-count distribution that is attributed to branch-dependent source response. For a finite branch mixture with branch pulse counts $N_i$, it has the bookkeeping form:

$$
V_{\mathrm{branch}}=\sum_i p_i (N_i-\bar{N})^2
$$

where:

$$
\bar{N}=\sum_i p_i N_i
$$

This expression is only bookkeeping until the branch labels are tied to records, a stochastic geometry law, or a non-classical geometry or mediator sector.

**Probe pulse-count marginal** means the local probability distribution $P(N_C)$ for the probe clock readout after all inaccessible source labels are ignored. H6S3 cares about this marginal because H6S1 and H6S2 reject spacelike remote-basis changes in the probe marginal.

**Ordinary measurement or instrument noise** means readout uncertainty, detector noise, preparation jitter, environmental nuisance variation, or calibrated instrument variance attached to the probe apparatus. It is allowed as a noise ledger, but it is not branch-response variance unless the branch-support route is declared.

**Local pointer or collapse record** means a physical record that selects or conditions a branch basis inside the probe causal past, through a modeled causal channel, or only after source and probe records are compared in a shared causal future. A record-conditioned distribution may carry branch variance, but the record and conservation ledger do the physical work.

**Stochastic classical pulse-geometry route** means a route where geometry remains classical but an objective causal noise or selection law adds physical variance. This route requires the law, coefficient provenance, regulator provenance, and conservation account. H6S3 does not supply them.

**Non-classical geometry or mediator route** means a route where geometry, or a mediator coupled to geometry, carries branch information non-classically. This route requires a scoped sector, admissible coupling, conservation account, and recovery limit. H6S3 does not supply them.

**Density-only baseline** means a conservative response depending only on the local density operator and declared local operators, such as $\rho_S$ and a weak-field potential operator. It is decomposition-invariant and therefore supplies no free branch variance from a chosen ensemble decomposition.

## 4. Theorem And Proof

### 4.1 Theorem: No Free Branch Variance

Let a finite-dimensional local source density operator $\rho_S$ have two or more ensemble decompositions. Let one decomposition be $E$:

$$
\rho_S=\sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

and let another be $F$:

$$
\rho_S=\sum_j q_j |\phi_j\rangle\langle\phi_j|
$$

Assume the probe has:

- no local pointer record selecting either decomposition
- no collapse-selection record available in the probe causal past
- no declared causal selection rule or modeled causal channel
- no stochastic classical pulse-geometry law
- no non-classical geometry or mediator sector

Then an admissible probe response must assign the same probe pulse-count marginal to every such decomposition:

$$
\mathcal{R}(\{p_i,|\psi_i\rangle\})=\mathcal{R}(\{q_j,|\phi_j\rangle\})
$$

Consequently, any branch-response variance that changes when the analyst changes only the ensemble decomposition of the same $\rho_S$ is not a physical source-response variance. It is a decomposition artifact unless one of the missing physical structures is supplied.

### 4.2 Proof

Fix the local density operator $\rho_S$ and all local probe ledgers: probe clock frequency, benchmark duration, instrument-noise model, conservation ledger, coefficient provenance, regulator provenance, causal-domain label, and gauge or branch-matching declaration.

By H6S2 ensemble invariance, a response rule is admissible only if equivalent ensemble decompositions of the same local $\rho_S$ give the same local probe marginal, unless a local record, modeled causal channel, or shared-future comparison physically selects a decomposition. Under the H6S3 assumptions, no such selector exists. There is also no stochastic classical pulse-geometry law and no non-classical geometry or mediator sector that could carry extra branch information.

Therefore the response cannot use the decomposition label as a physical input. It must reduce to a response of the local density operator and the declared local ledgers:

$$
P(N_C)=\mathcal{R}(\rho_S,L_{\mathrm{local}})
$$

For the two displayed decompositions this gives:

$$
P_E(N_C)=P_F(N_C)=P(N_C)
$$

where $P_E(N_C)$ and $P_F(N_C)$ denote the probe marginals obtained by writing the response in the first or second ensemble notation. If the two marginals differed solely because the decomposition notation changed, the rule would fail the H6S2 admissibility gate. In a steering setting, that difference could turn a remote basis choice into a local probe-marginal change without a causal channel, which H6S2 rejects.

Now compute a bookkeeping branch variance for decomposition $E$:

$$
V_E=\sum_i p_i (N_i^{(E)}-\bar{N}_E)^2
$$

with:

$$
\bar{N}_E=\sum_i p_i N_i^{(E)}
$$

Compute the analogous bookkeeping variance for decomposition $F$:

$$
V_F=\sum_j q_j (N_j^{(F)}-\bar{N}_F)^2
$$

with:

$$
\bar{N}_F=\sum_j q_j N_j^{(F)}
$$

The branch numbers $N_i^{(E)}$ and $N_j^{(F)}$ are physical response inputs only if the branches are selected by records, a causal selection rule, stochastic classical pulse geometry, or a non-classical geometry or mediator sector. Those structures are absent by assumption. Hence the response has one physical probe marginal $P(N_C)$, while $V_E$ and $V_F$ are variances attached to non-selected decompositions.

If $V_E\ne V_F$, the claimed branch variance cannot be an invariant physical variance of the source response, because the physical input $\rho_S$ and all local ledgers are unchanged. If $V_E=V_F$ accidentally, the equality does not make the branch variance physical; it still lacks a branch-support route. In both cases, the variance is not available merely from choosing a decomposition.

Ordinary measurement or instrument noise is separate. If the local apparatus has a fixed noise kernel $K$, the observed distribution may be:

$$
P_{\mathrm{obs}}(N_C)=\sum_m P(m)K(N_C-m)
$$

This ordinary probe noise can contribute to the observed variance, but it is not branch-response variance. It remains attached to the instrument ledger and must not change when only the analyst's ensemble decomposition changes. If a claimed noise term is branch-correlated, then it is no longer ordinary instrument noise; it requires a local record, a stochastic law, or a non-classical sector, which are excluded by the theorem assumptions.

Thus an admissible density-only response may have ordinary probe noise, and it may have whatever variance is already present in the invariant local probe marginal. It may not gain physical branch pulse-count variance for free from an arbitrary decomposition of the same density operator.

### 4.3 Clean No-Go Sub-Result

No physical branch pulse-count variance follows from ensemble notation alone. Without physical records, stochastic classical pulse geometry, or non-classical pulse geometry, a decomposition-dependent branch variance is not an admissible source-response variance.

This is a clean no-go sub-result inside H6S3. It is not the final project-rule classification for the whole H6S3 artifact.

### 4.4 Limits Of The Theorem

This theorem does not prove metric quantization, does not prove collapse, does not supply a new pulse-native source-response law, and does not produce a new external prediction. It also does not reject every hybrid classical-quantum gravity model. It rejects only the unsupported move from an arbitrary ensemble decomposition of $\rho_S$ to physical branch-dependent probe variance.

## 5. Allowed Inputs

H6S3 may use:

- H6S1 weak-field source/probe pulse-count diagnostics
- H6S1 separation between branch variance and ordinary instrumental noise
- H6S1 no-signaling and conservation guardrails
- H6S2 finite-dimensional trace-one positive semidefinite density matrices
- H6S2 equivalent ensemble decompositions of the same local density operator
- H6S2 density-operator response, pointer-record response, invalid ensemble-response, and pulse-native candidate ledgers
- declared local records, causal-domain labels, coefficient provenance, regulator provenance, gauge or branch-matching ledgers, and artifact ledgers

## 6. Non-Inputs

H6S3 must not use:

- arbitrary ensemble branch labels as physical response inputs
- a remote basis choice as a spacelike source-response cause
- an undeclared pointer basis or hidden collapse postulate
- an objective stochastic pulse-geometry law that has not been stated
- a non-classical geometry or mediator sector that has not been scoped
- coefficients fitted after the target observation
- a conservation account borrowed from notation alone
- metric quantization, collapse, branch-specific physical metrics, or a pulse-native response law as assumptions
- H6S4 route selection, H6S5 observable-map work, or later external-comparison claims

## 7. Project-Rule Classification Discipline

H6S3 must end with exactly one final project-rule label:

- known-physics reformulation
- diagnostic tool
- conditional derivation
- new prediction
- controlled modification
- clean no-go

The final H6S3 project-rule classification is:

> diagnostic tool

The no-free-branch-variance result is a clean no-go subtheorem inside that diagnostic tool. It is not a second final project-rule classification for the whole H6S3 artifact.

## 8. Route Ledger

H6S3 leaves one conservative baseline and three admissible branch-variance routes. None is promoted to a Pulse Model response law by H6S3.

| Route | Branch-variance status | Required physical support | Required ledgers | Allowed downstream use | Prohibited downstream use |
|---|---|---|---|---|---|
| Density-only response | Conservative baseline with no free branch variance. The probe marginal depends on $\rho_S$ and local operators, not an ensemble notation. | Local density operator, local operators, and ordinary instrument-noise ledger if noise is included. | Expectation-source conservation account; coefficient and regulator provenance if any nontrivial operator or regulator is introduced. | Baseline marginal, no-free-variance control, and negative tests for unsupported branch response. | Treating zero free branch variance as a new H6 signal or as the final pulse-native law. |
| Pointer-record or collapse-selection response | Branch variance can be record-conditioned, not notation-conditioned. | Local pointer record inside the probe causal past, modeled causal channel, declared collapse-selection record, or shared-future comparison of records. | Conservation ledger for branchwise or environment-assisted accounting; causal-domain declaration; branch-matching and artifact ledgers; coefficient provenance if a response coefficient appears. | Branch-conditioned diagnostics, source-probe correlation analysis, and candidate route requirements for later work. | Treating branch variance as physical without the record, or treating H6S3 as a collapse proof. |
| Stochastic classical pulse geometry | Branch variance can be physical only if classical geometry has an objective causal noise or selection law. | A stated stochastic classical pulse-geometry law before comparison with target observations. | Objective noise-law statement; coefficient provenance; regulator provenance; conservation account; no-signaling and artifact ledgers. | Future candidate-law constraints and tests for whether a stochastic classical route is coherent. | Borrowing arbitrary ensemble variance as noise, fitting coefficients after observation, or claiming H6S3 supplied the stochastic law. |
| Non-classical geometry or mediator | Branch variance can be physical only inside a scoped non-classical geometry or mediator sector. | A declared geometry or mediator sector that can carry branch information non-classically. | Sector scope; coupling assumptions; conservation ledger; recovery limit to the density-only or classical baseline; coefficient and artifact ledgers. | Comparator requirements for a future non-classical route. | Claiming metric quantization, quantum gravity, or a mediator law from H6S3 alone. |

The route ledger is intentionally strict: later H6 work must choose and defend a route before branch variance can be treated as physical. H6S3 does not choose the H6S4 route and does not supply a response law.

## 9. Accepted Outputs

H6S3 accepts these outputs:

- the no-free-branch-variance theorem for finite local density operators
- the clean no-go subtheorem: no physical branch pulse-count variance without physical records, stochastic classical pulse geometry, or non-classical pulse geometry
- the separation between ordinary probe noise and claimed branch-response variance
- the density-only baseline as the conservative no-free-variance control
- the route ledger distinguishing record-conditioned, stochastic-classical, and non-classical branch-variance routes
- executable finite helpers in `src/pulse_model/no_free_branch_variance.py`
- focused deterministic tests in `tests/test_no_free_branch_variance.py`

These outputs are diagnostic tools for future candidate response laws. They are not themselves a response law.

## 10. Allowed Downstream Uses

Downstream H6 work may use H6S3 to:

- reject branch variance that depends only on an arbitrary ensemble decomposition of the same $\rho_S$
- keep density-only response as the conservative baseline
- demand a local record, causal support or shared-future comparison, conservation ledger, branch-matching ledger, and artifact ledger before using pointer-record branch variance
- demand an objective causal noise law, coefficient provenance, regulator provenance, conservation account, no-signaling guardrail, and artifact ledger before using stochastic classical pulse geometry
- demand a scoped geometry or mediator sector, coupling assumptions, conservation ledger, coefficient provenance, artifact ledger, and recovery limit before using non-classical branch variance
- reuse the finite helper and test pattern as a guardrail for later candidates

## 11. Prohibited Downstream Uses

Downstream H6 work must not use H6S3 to:

- treat a chosen ensemble decomposition as a physical branch basis by notation alone
- infer a pulse-native source-response law
- choose the H6S4 route
- promote H6S1 or H6S2 variance diagnostics to new physics
- claim metric quantization, collapse, branch-specific physical metrics, stochastic geometry, or a mediator law
- make a new external prediction
- reject all hybrid classical-quantum gravity models
- fit branch-variance coefficients after seeing a target observation

## 12. Remaining Assumptions

H6S3 still assumes:

- finite-dimensional local density operators and finite probe pulse-count distributions
- the H6S2 ensemble-invariance admissibility gate
- fixed local probe ledgers when ensemble decompositions are compared
- no undeclared pointer basis, collapse rule, stochastic law, non-classical sector, or mediator
- ordinary instrument noise is declared separately from branch-response variance
- conservation, coefficient, regulator, causal-domain, and artifact ledgers remain mandatory for later routes

These assumptions are enough for the no-free-branch-variance theorem. They are not enough to construct the future response law.

## 13. Rejected Overclaims

H6S3 must not claim:

- a pulse-native source-response law has been discovered
- branch-dependent variance is a new external prediction
- metric quantization has been proved
- collapse has been proved
- branch-specific metrics are physical without a supporting route
- stochastic classical geometry has been supplied
- non-classical pulse geometry or a mediator law has been supplied
- H6S1 or H6S2 already contains the response law
- all hybrid classical-quantum gravity models are ruled out
- H6S4 has been chosen

H6S3 also must not create H6S4 tasks inside this appendix. Its job is to state the theorem target, prove the no-free-branch-variance result, and hand off a strict route ledger.

## 14. Verification Artifacts

The focused executable artifacts are:

- `src/pulse_model/no_free_branch_variance.py`
- `tests/test_no_free_branch_variance.py`

The focused tests construct equivalent $Z$-basis and $X$-basis decompositions of the same mixed density operator. They show that arbitrary branch counts can give different branch variances across decompositions, and that this is a diagnostic failure without records, stochastic classical pulse geometry, or non-classical geometry.
