---
title: H6S2 Causal Pulse-Response Kernel
sidebar_label: Causal Pulse Response
sidebar_position: 4
---

# Appendix: H6S2 Causal Pulse-Response Kernel

**Parent hypothesis:** H6: Classical spacetime emerges from decohered pulse-history structure  
**Status:** Completed with final project-rule classification: diagnostic tool  
**Purpose:** Turn the H6S1 no-signaling guardrail into an ensemble-decomposition-invariance test for causal source-response proposals.

---

## 1. Scope

H6S2 asks a single question:

> When a local source density operator admits multiple ensemble decompositions, may a gravitational or pulse response depend on the chosen branch decomposition?

The working H6S2 hypothesis is:

> A valid pulse-response kernel must be decomposition-invariant for different ensemble decompositions of the same local density operator unless the distinction is tied to a local record inside the probe causal past, a declared causal channel, or later comparison in a shared causal future.

Let the local source state available to the response rule be:

$$
\rho_S=\sum_i p_i |\psi_i\rangle\langle\psi_i|
$$

and also:

$$
\rho_S=\sum_j q_j |\phi_j\rangle\langle\phi_j|
$$

If no local pointer record, causal channel, or later shared-future comparison selects one decomposition over the other, an admissible response must not distinguish them:

$$
\mathcal{R}(\{p_i,|\psi_i\rangle\})=\mathcal{R}(\{q_j,|\phi_j\rangle\})
$$

This is an admissibility filter, not a new source-response law.

### 1.1 Admissibility Proposition: Decomposition-Dependent Response Implies Signaling Risk

Let $E_Z$ and $E_X$ be two operational preparation or steering descriptions of the same local source density operator:

$$
\rho_S=\sum_i p_i^{(Z)} |z_i\rangle\langle z_i|
$$

and:

$$
\rho_S=\sum_j p_j^{(X)} |x_j\rangle\langle x_j|
$$

Suppose a candidate source-response rule assigns probe marginals:

$$
P_Z(N_C)=\mathcal{R}(E_Z)
$$

and:

$$
P_X(N_C)=\mathcal{R}(E_X)
$$

If:

$$
P_Z(N_C)\ne P_X(N_C)
$$

solely because $E_Z$ rather than $E_X$ was chosen, and no local pointer record, declared causal channel, or shared-future comparison selects that decomposition for the probe, then the rule fails H6S2 admissibility for spacelike source response.

Proof:

1. In finite-dimensional quantum theory, remote steering can give different ensemble descriptions of the same reduced density operator $\rho_S$ without changing the local density operator available at the probe.
2. H6S1's no-signaling guardrail requires the probe marginal to be unchanged by a remote basis choice outside the probe causal past unless a causal channel is declared.
3. If a gravitational or pulse response depends on $E_Z$ or $E_X$ as an arbitrary branch decomposition, rather than on $\rho_S$ or local records, then the remote party's choice of ensemble description changes the local probe marginal.
4. That converts a remote basis choice into a spacelike source-response signal. Therefore the response is not admissible as a spacelike source-response law.

The admissible alternatives are density-operator response, local-record-conditioned response, response through a modeled causal channel, or correlation analysis after comparison in a shared causal future. Branch labels are not physical response inputs unless tied to local records or an explicit causal channel.

This proposition does not prove that gravity is quantum, does not rule out all classical-gravity or hybrid models, does not prove collapse, and does not discover the pulse-native law. It only rejects decomposition-dependent branch-response kernels when the decomposition is unsupported by local records or causal support.

### 1.2 Consequence For H6S1 Observable Channels

H6S1 showed that the ensemble mean is degenerate in the linear weak-field slice and that variance, bimodality, source-probe correlation, branch-conditioned shifts, and visibility are the interesting discriminator channels. H6S2 adds the admissibility condition for those channels: branch-conditioned variance, correlation, and visibility are meaningful response targets only when the branch basis is supported by local pointer records, a causal selection rule, or comparison in a shared causal future. Without that support, branch-mixture variance can be an ensemble-decomposition artifact rather than physical source response.

## 2. Allowed Inputs And Non-Inputs

H6S2 may use:

- the H6S1 weak-field source/probe discriminator and its no-signaling guardrail
- finite-dimensional trace-one positive semidefinite density matrices and ensemble decompositions
- local pulse records and local environmental pointer records
- declared causal-domain labels
- conservation, coefficient, regulator, gauge, branch-matching, and artifact ledgers

H6S2 must not use:

- arbitrary branch labels as physical response inputs
- a remote basis choice as a spacelike source-response cause
- a fitted-after-observation source-response coefficient
- an undeclared conservation account
- an invented pulse-native law
- metric quantization, collapse, or branch-specific physical metrics as assumptions

## 3. Response Families

H6S2 compares four response families. Only the first is a known-physics reformulation. The others are admissibility targets, diagnostics, or rejected bad rules until their ledgers are complete.

### 3.1 Density-Operator Expectation Response

Inputs:

- local density operator $\rho$
- finite potential operator $\hat{\Phi}$
- probe clock frequency $f_C$
- benchmark duration $T$

The response is:

$$
N_{\mathrm{exp}}=f_C T(1+\mathrm{Tr}(\rho \hat{\Phi})/c^2)
$$

This is a known-physics reformulation because it depends on $\rho$, not on an arbitrary ensemble decomposition of $\rho$.

### 3.2 Pointer-Record Branch Response

Inputs:

- local pointer records or diagonal branch records
- pointer projectors $\Pi_a$
- branch probabilities conditioned on the local record
- branch pulse counts $N_a$
- causal-domain status for the record

The response is a finite probe distribution:

$$
P(N_C)=\sum_a P(a|R_{\mathrm{local}})\delta(N_C-N_a)
$$

This family is admissible only when pointer conditioning is supported by a declared local record inside the probe causal past, a modeled causal channel, or comparison in a shared causal future. It is a diagnostic response family, not a new law.

### 3.3 Invalid Ensemble-Dependent Branch Response

Inputs:

- an externally chosen ensemble decomposition of $\rho_S$
- branch pulse counts attached to that decomposition

The bad response is:

$$
P_{\mathrm{bad}}(N_C|E)=\sum_i p_i\delta(N_C-N_i)
$$

This family is rejected when changing $E$ while keeping $\rho_S$ fixed changes the probe marginal without a local record or causal channel. It is kept only as a diagnostic bad rule for tests and theorem statements.

### 3.4 Pulse-Native Candidate Response Contract

H6S2 does not invent the pulse-native law. A future candidate must at least have the contract:

$$
\mathcal{R}:(\rho_{\mathrm{local}},\mathcal{P}_{\mathrm{local}},R_{\mathrm{env}},L_{\mathrm{cons}},D_{\mathrm{causal}},L_{\mathrm{coeff}})\mapsto P(N_C)
$$

The contract requires:

- a normalized finite probe distribution
- decomposition invariance
- causal support only
- no remote-basis marginal dependence
- a conservation status
- a gauge or branch-matching declaration
- coefficient and regulator provenance
- an artifact ledger
- pointer conditioning only when records exist

No response family becomes an accepted Pulse Model law merely by satisfying notation. Conservation status and causal support must be declared, and later tasks must still prove or test the claimed admissibility.

## 4. Causal-Domain Labels

H6S2 uses exactly these causal-domain labels:

| Label | Rule |
|---|---|
| `inside-probe-causal-past` | Allowed only when the relevant record exists and conservation, coefficient, regulator, gauge, and artifact ledgers are declared. |
| `compared-in-shared-future` | Allowed for correlation analysis after records meet in a shared causal future; not allowed as a spacelike influence. |
| `spacelike-remote-choice` | Rejected if the probe marginal changes. |
| `causal-channel-declared` | Allowed only when the channel is modeled or described explicitly. |
| `not-declared` | Blocked. |

## 5. Conservation Labels

H6S2 uses these conservation labels:

| Label | Meaning |
|---|---|
| `branchwise-conserved` | Every branch source used by the response has its own conservation account. |
| `expectation-conserved` | Conservation is only at the expectation-source level. |
| `conservation-requires-environment` | A discontinuous branch update needs an environment, collapse sector, or other ledger. |
| `not-yet-classified` | The family has not supplied the required conservation account. |
| `inconsistent-rejected` | The response is rejected because its source update or marginal change is inconsistent with the guardrails. |

Every response family must report the source of energy-momentum accounting, whether conservation is branchwise, in expectation, or environment-assisted, whether a discontinuous branch update occurs, and whether an environment or collapse sector carries any missing ledger.

## 6. Coefficient And Regulator Provenance

H6S2 uses exactly these coefficient provenance labels:

| Label | Rule |
|---|---|
| `derived` | The coefficient follows from the stated model assumptions before comparison with observations. |
| `calibrated-before-test` | The coefficient is fixed by an independent calibration before the target comparison. |
| `fixed-by-known-limit` | The coefficient is fixed by a known limiting case. |
| `exploratory-only` | The coefficient is used only for diagnostics and cannot support a prediction claim. |
| `fit-after-observation rejected` | Fitting the coefficient after seeing the target observation is rejected. |

Any regulator must also state whether it is a finite-size physical input, a numerical softening device, or an exploratory diagnostic parameter.

## 7. Project-Rule Classification Discipline

H6S2 uses exactly one final project-rule label:

- known-physics reformulation
- diagnostic tool
- conditional derivation
- new prediction
- controlled modification
- clean no-go

The final H6S2 project-rule classification is:

> diagnostic tool

The clean no-go subtheorem is separate: decomposition-dependent spacelike branch response is not admissible when it changes the probe marginal without local records or causal support. That subtheorem is not the final project-rule classification for the whole H6S2 artifact.

## 8. Forbidden Overclaims

H6S2 must not claim:

- a pulse-native source-response law has been discovered
- metric quantization has been proved
- collapse has been proved
- branch-specific metrics are physical
- H6S1 variance or visibility is new physics by itself
- all hybrid classical-quantum gravity models are ruled out

The accepted target for this appendix is an ensemble-decomposition-invariance admissibility filter for causal pulse response.

## 9. Observable Impact On H6S1

H6S1 remains correct that the ensemble mean is degenerate in the linear weak-field source/probe slice. Measuring only the mean probe pulse count still cannot distinguish density-operator expectation response from a branch-mixture bookkeeping response.

H6S2 changes the status of the distributional channels. Variance, bimodality, source-probe correlation, branch-conditioned shifts, and visibility are admissible response targets only when the branch basis is supported by:

- local pointer records inside the probe causal past
- a declared causal selection rule or modeled channel
- comparison of source and probe records in a shared causal future

Without that support, a branch-mixture variance or visibility calculation can be an ensemble-decomposition artifact. It is then a useful diagnostic failure mode, not evidence for a physical branch-specific metric response.

## 10. Accepted Outputs

H6S2 accepts these outputs:

- ensemble-decomposition invariance guardrail
- finite-dimensional examples using equivalent $Z$-basis and $X$-basis decompositions of the same density operator
- density-operator response helper
- pointer-record branch-response helper
- invalid ensemble-response rejection
- causal-domain labels
- conservation ledgers
- coefficient ledgers

These outputs are tools for testing candidate response rules. They are not a pulse-native response law.

## 11. Response-Family Ledger

No response family becomes an accepted Pulse law unless conservation status and causal support are declared.

| Response family | Final status | Causal admissibility | Decomposition-invariance status | Conservation accounting source | Conservation mode | Discontinuous branch update | Coefficient provenance | Regulator provenance | Gauge or branch matching | Artifact ledger | Allowed downstream use |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Density-operator expectation response | known-physics reformulation | Allowed when $\rho$ and $\hat{\Phi}$ are local inputs. | Invariant by construction because it depends on $\rho$. | Semiclassical expectation-source assumptions. | expectation | No. | derived or fixed-by-known-limit | none unless a finite operator regulator is declared | Not branch-specific. | ordinary semiclassical equivalence; ensemble-mean degeneracy | Baseline probe marginal and same-density guardrail. |
| Pointer-record branch response | diagnostic response family | Allowed only for local pointer records, declared causal channels, or shared-future comparisons. | Invariant unless an actual record selects the pointer basis. | Branch source ledger or environment record ledger. | branchwise or environment-assisted | Only if a declared selection update is part of the record. | derived or calibrated-before-test | declared finite record or source-size regulator | Required. | pointer-basis, postselection, and branch-matching artifacts | Branch-conditioned variance, correlation, and visibility targets. |
| Invalid ensemble-dependent response | rejected diagnostic bad rule | Rejected for spacelike remote choice when the probe marginal changes. | Fails when equal-density decompositions produce different marginals. | none accepted | rejected | Not admitted. | none accepted | none accepted | arbitrary decomposition choice | chosen ensemble decomposition artifact; remote-basis signaling | Negative tests and the no-go subtheorem. |
| Pulse-native candidate contract | blocked candidate contract | Blocked until causal support is declared. | Required but not supplied by notation alone. | missing until a candidate law supplies it | unclassified | Not admitted unless accounted for. | derived, calibrated-before-test, fixed-by-known-limit, or exploratory-only; fit-after-observation rejected | required if any regulator appears | Required. | required before downstream use | Future candidate-law contract only. |

## 12. Rejected Overclaims

H6S2 rejects these overclaims:

- no pulse-native law has been discovered
- no metric quantization proof has been supplied
- no collapse proof has been supplied
- no proof has been supplied that branch-specific metrics are physical
- H6S1 variance, bimodality, correlation, and visibility are not promoted to new physics by themselves
- not all hybrid classical-quantum gravity models are rejected

## 13. Verification

Commands already run during the H6S2 implementation sequence:

```bash
uv run python -m unittest tests.test_causal_pulse_response
```

```bash
uv run python -m unittest discover -s tests
```

```bash
npm run typecheck
```

```bash
npm run build
```

Final H6S2 closure also completed the link review, review-3 traceability check, repeated math-format scan, and cross-document consistency pass after roadmap and status pointers were updated.

## 14. Reader-Flow Integration

H6S2 is now integrated into the active reader-flow documents: the H6 appendix index, roadmap, proof sequence, current status, frontier strategy, and compatibility strategy page all point to this appendix and its executable code/test artifacts.

The result remains a diagnostic tool, with the clean no-go subtheorem named separately. It does not supply the pulse-native source-response law.
