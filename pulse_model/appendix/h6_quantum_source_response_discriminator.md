# Appendix: H6S1 Quantum Source-Response Discriminator

**Parent hypothesis:** H6: Classical spacetime emerges from decohered pulse-history structure  
**Status:** In progress for a weak-field quantum source-response discriminator  
**Purpose:** Turn H6 from branch bookkeeping into a bounded discriminator for what probe-clock pulse records compare against when a source is in a quantum superposition of matter or pulse-history branches.

---

## 1. Discriminator Contract

H6S1 asks a narrower question than full H6:

> When matter phase is quantum-superposed, what pulse-count geometry does a probe clock compare against?

The first answer is not a new gravity theory. It is a controlled two-branch weak-field arena that compares source-response model families by their probe pulse-count distributions.

The discriminator is allowed to compute or classify:

- mean probe pulse count
- pulse-count variance
- branch-conditioned probe pulse counts
- branch-separation or bimodality score
- source-probe correlation after source-branch readout
- internal clock visibility factor
- no-signaling and conservation guardrail status

The discriminator is not allowed to claim that matching one of these channels solves quantum gravity, metric quantization, collapse, or classical spacetime emergence.

## 2. Accepted Inputs

H6S1 may use these earlier results only within their accepted limits:

- H1 supplies calibrated local pulse counts and the equivalence between ideal pulse-count conditioning and ordinary single-time quantum predictions.
- H2 supplies bounded metric or potential inputs only inside controlled reconstruction or fixed-event assumptions. H6S1 must not infer arbitrary geometry from sparse records.
- H3 supplies curvature and holonomy diagnostics only as downstream guardrails, not as a source-response law.
- H4 supplies standard matter stress-energy as matter phase-response in the reviewed conservative cases.
- The geometry-action results supply only a conditional low-energy branch-local source-to-metric bridge when their locality, scalarization, refinement, boundary, and correction-suppression assumptions are explicit.
- H5 supplies branch proper-time and clock-visibility formulas for quantum systems carrying different pulse or proper-time histories.
- The existing H6 branch-decoherence appendix supplies branch records, reduced overlaps, and the warning that ensemble means can be degenerate.

The controlled H6S1 toy setup may assume a one-dimensional weak-field Newtonian potential and a stationary probe clock. That is an arena assumption for the discriminator, not an H6 emergence proof.

## 3. Prohibited Shortcuts

H6S1 must not start from:

- an unspecified quantum metric Hilbert space
- a solved collapse dynamics
- a hidden preferred pulse frame
- an already-selected classical branch without declaring the selection rule
- a smooth geometry beyond the weak-field toy assumptions needed for the source/probe benchmark
- source-response coefficients fitted after seeing experimental bounds
- environmental decoherence relabeled as metric-history decoherence
- an ensemble mean alone as the discriminator

H6S1 must also not modify geometry-action or H7 except as downstream guardrails. H7 vacuum-energy claims are not inputs to this work.

## 4. Result Labels And Artifact Labels

Every final H6S1 claim must use exactly one project-rule result label:

- known-physics reformulation
- diagnostic tool
- conditional derivation
- new prediction
- controlled modification
- clean no-go

Model-family labels used in this appendix are:

- expectation-sourced semiclassical response
- branch-specific metric response
- collapse/decoherence selection response
- pulse-native candidate response kernel
- intentionally invalid toy response

Artifact or failure labels used in this appendix are:

- ensemble-mean degeneracy
- gauge or branch-matching artifact
- chosen branch-basis artifact
- hidden collapse postulate
- decoherence double-counting
- remote-basis signaling
- conservation failure
- environmental backreaction omission
- fitted coefficient smuggling
- ordinary semiclassical equivalence
- H5/H6 scope violation
- experimental artifact exposure

Conservation labels are:

- branchwise conserved
- expectation conserved
- conservation requires environment
- inconsistent/rejected

No-signaling labels are:

- no-signaling passed
- causal channel required
- rejected for remote-basis signaling
- not yet classified

## 5. Required Files

The H6S1 work is complete only when these files exist and match the evidence:

- `pulse_model/appendix/h6_quantum_source_response_discriminator.md`
- `pulse_model/src/pulse_model/quantum_source_response.py`
- `pulse_model/tests/test_quantum_source_response.py`

The roadmap files are updated only at the final verdict step, if the H6 status, frontier order, or novelty/usefulness assessment changes:

- `pulse_model/proof_sequence.md`
- `pulse_model/promising_tweaks.md`

## 6. Ordered Task Sequence

The implementation order is:

1. Define this discriminator contract, appendix scope, and result labels.
2. Define the two-branch weak-field source/probe record schema.
3. Derive expectation, branch-mixture, collapse, and pulse-native response families.
4. Derive discriminator observables beyond ensemble mean.
5. Add no-signaling and conservation guardrail contracts.
6. Implement the focused helper module and tests.
7. Map discriminator outputs to experimental observable classes.
8. Run the adversarial novelty and artifact review.
9. Write the final verdict and update roadmap files.

Later sections are appended only after the earlier contract is in place.

## 7. Two-Branch Weak-Field Source/Probe Schema

The first H6S1 arena is a one-dimensional source-position superposition with one stationary probe clock at a relational position $P$. The source branches are labeled $a$ and $b$.

The source state is recorded as:

$$
|S\rangle = \sqrt{p_a}|a\rangle + e^{i\varphi}\sqrt{p_b}|b\rangle
$$

with:

$$
p_b = 1 - p_a
$$

The branch labels are bookkeeping labels for records. They are not observables until tied to a source readout, environmental record, or branch-stable preparation protocol.

### 7.1 Observed Or Declared Inputs

The minimal input record contains:

| Field | Meaning | Handling rule |
|---|---|---|
| `branch_label_a`, `branch_label_b` | Distinct source branch labels. | Labels may be relabeled; only relational outputs are meaningful. |
| `probability_a`, `probability_b` | Branch probabilities. | Each must be finite and nonnegative, and the pair must sum to one. |
| `relative_phase_rad` | Relative source-branch phase $\varphi$. | Recorded because it matters for coherent variants, but the first diagonal weak-field mixture uses only probabilities. |
| `branch_overlap` | Reduced branch overlap magnitude, written as the absolute value of $\Gamma_{ab}$. | Must lie in $[0,1]$; used for visibility/decoherence guardrails, not as a collapse rule. |
| `source_position_a_m`, `source_position_b_m` | One-dimensional relational source locations. | Generator or preparation inputs for the controlled arena. |
| `probe_position_m` | One-dimensional relational probe-clock location. | Shared relational location used for both branches. |
| `coordinate_duration_s` | Common weak-field benchmark duration $T$. | Must be nonnegative; it is a calculation parameter, not universal time ontology. |
| `clock_frequency_hz` | Probe clock pulse frequency $f_C$. | Must be nonnegative and interpreted as a calibrated local clock transition. |
| `source_mass_kg` | Source mass $M$. | Must be nonnegative. |
| `softening_radius_m` | Optional softening radius. | Must be nonnegative; if zero, coincident source/probe inputs are singular and rejected. |
| `instrumental_noise_stddev_pulses` | Optional probe readout noise in pulse counts. | Must be nonnegative and kept separate from branch variance. |

The branch weak-field potentials at the probe are:

$$
\Phi_a(P)=-\frac{GM}{\sqrt{(P-x_a)^2+\epsilon^2}}
$$

$$
\Phi_b(P)=-\frac{GM}{\sqrt{(P-x_b)^2+\epsilon^2}}
$$

Here $\epsilon$ is the softening radius. With $\epsilon=0$, the denominator is $|P-x_a|$ or $|P-x_b|$.

### 7.2 Derived Quantities

The branch-conditioned probe proper times are:

$$
\tau_a^{(P)} = T(1+\Phi_a(P)/c^2)
$$

$$
\tau_b^{(P)} = T(1+\Phi_b(P)/c^2)
$$

The branch-conditioned probe pulse counts are:

$$
N_a = f_C\tau_a^{(P)}
$$

$$
N_b = f_C\tau_b^{(P)}
$$

The expectation-sourced weak-field potential is:

$$
\bar{\Phi}(P)=p_a\Phi_a(P)+p_b\Phi_b(P)
$$

The corresponding expectation-sourced probe pulse count is:

$$
N_{\mathrm{exp}}=f_C T(1+\bar{\Phi}(P)/c^2)
$$

### 7.3 Observed, Inferred, Gauge, And Nuisance Separation

Observed or declared record fields are branch labels, branch probabilities, relative phase, reduced branch overlap, source/probe relational locations, benchmark duration, clock frequency, source mass, softening radius, and optional noise ledger.

Inferred quantities are branch potentials, branch proper times, branch pulse counts, expectation-sourced pulse count, branch-mixture statistics, source-probe correlation, branch-separation score, and clock visibility.

Gauge or matching quantities are the branch labels, one-dimensional coordinate origin, orientation, and any branch-matching map that identifies the same relational probe location across branches. H6S1 treats absolute coordinate position as gauge scaffolding; the calculated observables are differences, distributions, and correlations tied to the common probe record.

Nuisance quantities are instrumental readout noise, preparation uncertainty, environmental records, technical contrast loss, source localization width hidden by the point-source toy model, and any softening radius. They must not be folded into branch-mixture variance without a ledger.

### 7.4 Validity Limits And Rejection Rules

The weak-field toy is valid only when:

- source/probe separations are finite or explicitly softened
- $|\Phi|/c^2$ is small enough for the first weak-field rate formula to be meaningful
- the probe is stationary in the chosen controlled arena
- branch probabilities are preparation probabilities, not fitted response coefficients
- the same relational probe location is used in both branches

The implementation must reject:

- singular coincident source/probe inputs when `softening_radius_m` is zero
- non-finite numbers
- negative probabilities or probabilities greater than one
- probability pairs that do not sum to one
- negative mass, duration, clock frequency, softening radius, or instrumental noise
- branch labels that are empty or identical
- weak-field rates that would make the probe proper time negative in the toy calculation

The toy may soften coincident inputs for numerical tests, but the softened result must be labeled as a regulator-dependent benchmark, not a point-source prediction.

## 8. Source-Response Model Families

This section defines the model families compared by the discriminator. The first two are ordinary weak-field calculation families. The third adds a selection rule placeholder. The fourth is only a Pulse Model constraint target.

### 8.1 Expectation-Sourced Semiclassical Response

The expectation-sourced family assigns one effective weak-field source to the source state.

Inputs:

- branch probabilities $p_a$ and $p_b$
- branch source positions $x_a$ and $x_b$
- source mass $M$
- shared probe location $P$
- weak-field benchmark duration $T$
- probe clock frequency $f_C$

The source potential at the probe is:

$$
\bar{\Phi}(P)=p_a\Phi_a(P)+p_b\Phi_b(P)
$$

The probe pulse count is:

$$
N_{\mathrm{exp}}=f_C T(1+\bar{\Phi}(P)/c^2)
$$

Output:

- one probe pulse-count value, before instrumental noise
- no branch-conditioned pulse spread from the source response itself

Assumptions:

- the weak-field source can be represented by the expectation of branch-local source data
- the source state is not collapsed by the calculation
- off-diagonal source terms are either absent from the reduced weak-field source or separately negligible in this toy arena

Guardrail placeholders:

- conservation status: expectation conserved
- no-signaling status: not yet classified until the update rule under remote measurements is stated

Classification for this family:

> known-physics reformulation

### 8.2 Branch-Specific Metric Response

The branch-specific family assigns one weak-field response per decohered or branch-resolved source record.

Inputs:

- branch probabilities $p_a$ and $p_b$
- branch source positions $x_a$ and $x_b$
- shared probe location $P$
- source mass $M$
- benchmark duration $T$
- clock frequency $f_C$
- branch-basis and matching data showing that $N_a$ and $N_b$ refer to the same probe record protocol

The branch pulse counts are:

$$
N_a=f_C T(1+\Phi_a(P)/c^2)
$$

$$
N_b=f_C T(1+\Phi_b(P)/c^2)
$$

The probe pulse-count distribution is:

$$
P(N_C)=p_a\delta(N_C-N_a)+p_b\delta(N_C-N_b)
$$

Output:

- a branch-correlated pulse-count mixture
- branch-conditioned pulse counts $N_a$ and $N_b$
- no claim of coherent metric superposition

Assumptions:

- the source branch basis has already been made stable by records, environment, or preparation
- branch potentials can be compared at a shared relational probe location
- each branch source is admissible for the low-energy branch-local bridge

Guardrail placeholders:

- conservation status: branchwise conserved if each branch source is conserved; otherwise inconsistent/rejected
- no-signaling status: not yet classified until branch selection and source readout are causal

Classification for this family:

> bookkeeping/diagnostic target

### 8.3 Collapse Or Decoherence Selection Response

The collapse/decoherence family adds a rule that changes the effective source used by the probe.

Inputs:

- the pre-selection source state or branch mixture
- branch probabilities or selection probabilities
- branch source data and branch potentials
- a selection, decoherence, or collapse timing rule
- an environment or collapse-sector ledger if conservation is not branchwise
- the same probe record fields used by the expectation and branch-specific families

The schematic record update is:

$$
(\rho_S,\Phi_{\mathrm{pre}}) \rightarrow (a,\Phi_a)
$$

or:

$$
(\rho_S,\Phi_{\mathrm{pre}}) \rightarrow (b,\Phi_b)
$$

Output:

- one selected branch pulse count per run if selection occurs before the probe record
- a branch-mixture distribution across runs if the selection statistics are $p_a$ and $p_b$
- no selection of a unique observed branch from environmental decoherence alone

Assumptions:

- a selection time or causal ordering relative to the probe record is declared
- selection probabilities are fixed before comparison with observations
- the environment or collapse sector carries any missing conservation ledger

Guardrail placeholders:

- conservation status: conservation requires environment unless a branchwise conservation account is supplied
- no-signaling status: not yet classified until remote-basis choices are shown not to alter the distant probe marginal

Classification for this family:

> blocked conditional bridge

### 8.4 Pulse-Native Candidate Response Kernel

The pulse-native family is not a proposed law yet. H6S1 defines only the contract a future law must satisfy.

A future candidate response kernel would have the form:

$$
\mathcal{R}:\{\mathcal{B}_a,p_a,\Gamma_{ab},J_a\}\mapsto P(N_C)
$$

Here $\mathcal{B}_a$ are branch records, $p_a$ are branch probabilities, $\Gamma_{ab}$ are branch overlaps, $J_a$ are branch source data, and $P(N_C)$ is a probe pulse-count distribution.

Allowed inputs:

- local pulse-history records
- branch probabilities fixed by preparation or prior quantum dynamics
- branch overlaps and visibility factors
- branch source data with conservation status
- relational probe/source geometry in the controlled arena

Required outputs:

- a normalized probe pulse-count distribution
- explicit mean, variance, branch-correlation, and visibility behavior
- no-signaling status
- conservation status
- coefficient and regulator ledger

Assumptions that cannot be hidden:

- branch basis selection
- environmental backreaction
- causal update rule
- gauge or branch matching
- energy and momentum accounting

Guardrail placeholders:

- conservation status: not accepted until classified by the guardrail
- no-signaling status: rejected unless the probe marginal is invariant under remote basis choice without a causal channel

Classification for this family:

> speculative constraint target

### 8.5 Mean Degeneracy In The Linear Weak-Field Slice

The branch-specific ensemble mean is:

$$
\langle N_C\rangle_{\mathrm{mix}}=p_aN_a+p_bN_b
$$

Substituting the weak-field branch counts gives:

$$
\langle N_C\rangle_{\mathrm{mix}}=f_C T(1+(p_a\Phi_a(P)+p_b\Phi_b(P))/c^2)
$$

Therefore:

$$
\langle N_C\rangle_{\mathrm{mix}}=N_{\mathrm{exp}}
$$

This equality holds in the linear weak-field source/probe slice, including the symmetric equal-probability case. The ensemble mean alone is therefore not an H6S1 discriminator.

## 9. Discriminator Observables Beyond Ensemble Mean

The H6S1 discriminator starts from branch proper times and converts them into probe pulse counts:

$$
N_i=f_C\tau_i^{(P)}
$$

for $i\in\{a,b\}$.

This weak-field relation is operational because the probe clock records pulses. The potentials are intermediate calculation scaffolding in the controlled arena.

### 9.1 Mean Probe Pulse Count

The branch-mixture mean is:

$$
\mu_N=p_aN_a+p_bN_b
$$

In the linear weak-field slice, $\mu_N=N_{\mathrm{exp}}$. This equality is useful because it prevents overclaiming: mean shift alone cannot distinguish expectation-sourced response from a branch mixture.

### 9.2 Branch-Conditioned Pulse Counts

If a source branch is read out locally and later compared with the probe record, the branch-conditioned pulse counts are:

$$
\mu_{N|a}=N_a
$$

$$
\mu_{N|b}=N_b
$$

The conditional shift is:

$$
\Delta N_{ab}=N_a-N_b
$$

This is the direct branch-correlated channel. It is meaningful only when the source branch readout and probe record are compared through an allowed causal or later classical channel.

### 9.3 Branch-Mixture Variance

Before instrumental noise, the branch-mixture variance is:

$$
\sigma_{N,\mathrm{branch}}^2=p_a p_b(N_a-N_b)^2
$$

With independent instrumental pulse-count noise $\sigma_{\mathrm{inst}}$, the observed variance ledger is:

$$
\sigma_{N,\mathrm{obs}}^2=p_a p_b(N_a-N_b)^2+\sigma_{\mathrm{inst}}^2
$$

This variance is not automatically new physics. It can be source preparation spread, branch correlation, selection timing, or ordinary noise unless the ledger separates the channels.

### 9.4 Branch Separation Or Bimodality Score

A compact branch-separation score is:

$$
S_N=\frac{|N_a-N_b|}{\sigma_{\mathrm{inst}}}
$$

If $\sigma_{\mathrm{inst}}=0$ and $N_a\ne N_b$, the idealized score is unbounded. If $N_a=N_b$, the score is zero. A large score names a target for bimodal pulse records; it does not by itself identify which source-response family is correct.

### 9.5 Source-Probe Correlation

Let $B$ be a branch indicator with $B=1$ for branch $a$ and $B=0$ for branch $b$. The source-probe covariance in pulse units is:

$$
\mathrm{Cov}(B,N_C)=p_a p_b(N_a-N_b)
$$

Without added independent noise and with $N_a\ne N_b$, the branch indicator and pulse count are perfectly correlated or anticorrelated. With independent instrumental noise, the Pearson correlation is:

$$
\rho_{BN}=\frac{p_a p_b(N_a-N_b)}{\sqrt{p_a p_b(p_a p_b(N_a-N_b)^2+\sigma_{\mathrm{inst}}^2)}}
$$

This channel is operational only after source-branch information and probe records are compared causally.

### 9.6 Internal Clock Visibility

For a probe with internal clock state $\rho_C$ and Hamiltonian $H_C$, the branch visibility factor is:

$$
V_{ab}=|\mathrm{Tr}(\rho_C e^{-iH_C(\tau_a-\tau_b)/\hbar})|
$$

For a discrete energy-basis mixture with probabilities $q_j$ and energies $E_j$, this becomes:

$$
V_{ab}=\left|\sum_j q_j e^{-iE_j(\tau_a-\tau_b)/\hbar}\right|
$$

Visibility loss is a clock-state overlap signal. It must be kept separate from environmental contrast loss and technical dephasing.

### 9.7 Observable Summary

| Channel | Expectation-sourced response | Branch-specific or pre-probe selection response | H6S1 status |
|---|---|---|---|
| Ensemble mean $\mu_N$ | One value at $N_{\mathrm{exp}}$. | Same mean in the linear weak-field slice. | Degenerate. |
| Variance $\sigma_N^2$ | Zero source-response variance before noise. | $p_a p_b(N_a-N_b)^2$ before noise. | Useful discriminator target. |
| Branch-conditioned count | No branch-conditioned metric count unless extra records are supplied. | $N_a$ or $N_b$ tied to source branch. | Useful discriminator target. |
| Branch separation | Zero for a single expectation response. | $S_N$ with the numerator defined by the absolute branch-count difference. | Useful target if noise ledger is controlled. |
| Source-probe correlation | No branch correlation from the metric response alone. | Correlation appears when source branch and probe count are compared. | Useful target with causal readout. |
| Visibility factor | Depends on one effective probe time unless additional path branches exist. | Depends on $\tau_a-\tau_b$. | Useful clock-state target. |

The operational H6S1 statement is therefore:

> Ensemble mean is a degeneracy check; variance, bimodality, source-probe correlation, branch-conditioned shifts, and visibility are the discriminator channels.

## 10. No-Signaling And Conservation Guardrail Contracts

Every source-response rule must pass two guardrails before it can be treated as a possible Pulse Model law.

### 10.1 No-Signaling Marginal Test

For a source measurement basis choice $B_{\mathrm{remote}}$ outside the probe's causal past, the probe marginal distribution must not change unless a causal interaction channel is included.

The guardrail condition is:

$$
P(N_C|B_{\mathrm{remote}}=Z)=P(N_C|B_{\mathrm{remote}}=X)
$$

for the same local preparation and no causal channel to the probe.

The guardrail labels are:

| Condition | Label | Decision |
|---|---|---|
| Probe marginal is invariant under remote basis choice. | no-signaling passed | Allowed at this gate. |
| Probe marginal changes but a causal source-probe channel is explicitly included. | causal channel required | Not a spacelike no-signaling violation, but must be modeled. |
| Probe marginal changes without a causal channel. | rejected for remote-basis signaling | Rejected. |
| The rule does not define the marginal. | not yet classified | Not accepted as a response law. |

The intentionally invalid toy rule is:

$$
P_{\mathrm{bad}}(N_C|Z)=p_a\delta(N_C-N_a)+p_b\delta(N_C-N_b)
$$

$$
P_{\mathrm{bad}}(N_C|X)=\frac{1}{2}\delta(N_C-N_a)+\frac{1}{2}\delta(N_C-N_b)
$$

If $p_a\ne 1/2$ and $N_a\ne N_b$, this rule changes the distant probe marginal by remote basis choice alone. It is rejected for remote-basis signaling.

The valid branch-mixture bookkeeping rule is different. It allows source and probe records to be compared after both records are inside a shared causal future, but it does not let a remote basis choice change the probe marginal at spacelike separation.

### 10.2 Conservation Classification

In the low-energy branch-local bridge, source data must be compatible with conservation:

$$
\nabla_\mu T^{\mu\nu}=0
$$

The H6S1 conservation labels are:

| Family | Conservation label | Reason |
|---|---|---|
| Expectation-sourced semiclassical response | expectation conserved | The source is conserved only at the expectation-value level, assuming the semiclassical source is well-defined and compatible with the background equation. |
| Branch-specific metric response | branchwise conserved | Allowed only if every branch source used by a branch-local metric is conserved with its branch boundary data. |
| Collapse/decoherence selection response | conservation requires environment | A discontinuous selected-source update needs an environment, collapse sector, or other ledger for energy and momentum accounting. |
| Pulse-native candidate kernel | not yet classified | The kernel is not admitted until it states its conservation account. |
| Intentionally invalid toy response | inconsistent/rejected | Remote-basis signaling and undefined conservation accounting fail the guardrails. |

This section does not solve conservation for collapse or pulse-native variants. It prevents those variants from being treated as accepted Pulse Model laws before the missing ledger exists.

### 10.3 Gate Rule

A candidate response rule may be used downstream only if it supplies:

- a normalized probe marginal distribution
- a no-signaling classification
- a conservation classification
- any causal channel or environment ledger needed for those classifications
- the source of every coefficient or regulator

If any item is missing, the rule remains a diagnostic target or blocked conditional bridge.

## 11. Observable-Class Benchmark Matrix

This section names experimental or phenomenological observable classes. It records no current numerical bounds, dates, or experiment-status claims. Therefore no external numerical sourcing is used here. Any later task that records exact bounds or dates must verify them against current primary or review sources.

| Observable class | Observable | Model-family expectation | Required control variables | Artifact ledger | Current work supplies | Result classification |
|---|---|---|---|---|---|---|
| Source superpositions | Probe pulse-count mean and variance for a source prepared in two location branches. | Expectation-sourced response and branch mixture share the weak-field mean; branch mixture adds $p_a p_b(N_a-N_b)^2$ before noise. | Source branch probabilities, source/probe separation, source mass, probe duration, clock frequency, softening or finite-size model, readout noise. | Source preparation spread, finite source size, vibration, electromagnetic coupling, thermal drift, background gravitational gradients. | Calculation in `quantum_source_response.py`. | useful diagnostic |
| Quantum clocks | Internal clock visibility tied to $\tau_a-\tau_b$. | Branch-conditioned response can reduce internal clock visibility through the H5 overlap formula; expectation-sourced response gives one effective probe time unless another branch degree of freedom is modeled. | Clock transition frequency or energy distribution, coherence time, branch proper-time difference, internal-state preparation, environmental contrast factors. | Ordinary dephasing, laser phase noise, trap shifts, blackbody shifts, collisions, finite readout contrast. | Calculation through branch visibility helpers using H5 formulas. | useful diagnostic |
| Branch-correlated probe timing | Conditional pulse count $N_a$ or $N_b$ after source branch readout. | Branch-specific or pre-probe selection response predicts source-probe covariance; expectation-sourced response has no branch-conditioned metric shift by itself. | Source readout timing, causal ordering, branch labels, shared probe protocol, readout channel, probability calibration. | Postselection bias, delayed-choice misinterpretation, classical communication leakage, detector imbalance. | Calculation for covariance and correlation; experimental protocol is only a target. | diagnostic target |
| Gravitationally mediated entanglement style tests | Whether probe/source correlations exceed a classical expectation-source description. | H6S1 does not compute an entanglement witness; it names variance/correlation channels that could be embedded in such protocols. | Source masses, separations, coherence, branch distinguishability, shielding, non-gravitational coupling bounds, timing of branch readout. | Electromagnetic leakage, Casimir backgrounds, vibration, patch potentials, environmental decoherence, fitted gravitational coefficient. | Target only. | blocked conditional bridge |
| Visibility-loss probes | Probe clock or path visibility as a function of branch proper-time difference. | Branch-conditioned response maps $\Delta\tau$ into $V_{ab}$; expectation-sourced response has no two-branch visibility loss unless the probe itself carries branches. | Energy distribution, branch duration, source/probe geometry, environmental visibility, technical contrast. | Environmental decoherence double-counting, clock-state preparation error, uncontrolled path distinguishability, readout loss. | Calculation through branch visibility helpers; experiment-specific model is target only. | useful diagnostic |
| Null and degeneracy cases | Equal branch potentials, zero source mass, zero duration, zero clock frequency, or equal branch probabilities with only mean readout. | The discriminator should report zero branch separation or mean degeneracy rather than inventing a signal. | Symmetry of branch geometry, zero or calibrated control values, noise floor, matched source/probe location. | False positive from numerical softening, label-order artifact, instrument offset, hidden branch selection. | Calculation and rejection/degeneracy checks. | clean no-go for that channel |

The immediate experimentally meaningful observable classes are therefore variance, bimodality or branch separation, source-probe correlation, visibility loss, and conditional probe shift. H6S1 supplies calculations for the weak-field toy channels and names broader protocol classes, but it does not fit or claim a new external bound.

## 12. Adversarial Novelty And Artifact Review

This review decides what survives after the most likely overclaims are removed.

| Check | Failure mode | H6S1 result | Surviving claim label |
|---|---|---|---|
| Ensemble-mean degeneracy | Treating $N_{\mathrm{exp}}=\langle N_C\rangle_{\mathrm{mix}}$ as a discriminator. | Rejected. The mean equality is a degeneracy check, not a signal. | artifact |
| Gauge or branch-matching artifact | Comparing branch potentials at coordinate locations that do not identify the same relational probe record. | The schema requires one shared relational probe location and matching data; arbitrary branch metric comparison remains blocked. | blocked conditional bridge |
| Chosen branch basis | Choosing source localization branches for convenience and treating them as fundamental. | H6S1 uses branch labels only as controlled preparation records; a stable branch basis remains an assumption or environment-derived input. | useful diagnostic |
| Hidden collapse postulate | Reading branch-mixture outputs as proof that one branch physically collapses before the probe record. | Rejected. Collapse/decoherence variants are only classified unless they provide timing, probability, conservation, and no-signaling rules. | blocked conditional bridge |
| Decoherence double-counting | Counting environmental visibility loss and metric-history visibility loss as the same effect. | The observable matrix and schema require separate environmental, technical, and branch-response ledgers. | useful diagnostic |
| Remote-basis signaling | Allowing a remote source measurement basis to change the spacelike probe marginal. | The invalid toy rule is rejected by code and by the guardrail contract. | clean no-go |
| Conservation failure | Letting a selected source metric change without energy and momentum accounting. | Branch-specific response is allowed only branchwise; collapse variants require an environment or collapse-sector ledger. | blocked conditional bridge |
| Environmental backreaction omission | Ignoring the apparatus/environment needed to prepare or read out source branches. | The current helper does not model this; broader protocols remain targets only. | blocked conditional bridge |
| Fitted coefficient smuggling | Using softening, source-response coefficients, or pulse-native kernels as adjustable fits. | H6S1 has no new fitted coefficient. Softening is a regulator in the toy arena. | useful diagnostic |
| Ordinary semiclassical equivalence | Claiming new physics from expectation-sourced weak-field calculations alone. | Rejected. Expectation-sourced response is a known-physics reformulation. | known-physics reformulation |
| H5/H6 scope violation | Treating H5 visibility or H6 branch bookkeeping as a solved quantum source-response law. | Rejected. H6S1 uses H5/H6 only as bounded inputs and reports a diagnostic, not a law. | useful diagnostic |
| Experimental artifact exposure | Treating variance, bimodality, or visibility loss as gravitational source-response without controlling non-gravitational artifacts. | The matrix lists artifact ledgers and marks protocol-level claims as targets unless the current helper supplies the calculation. | useful diagnostic |

The claims that survive are:

| Surviving claim | Evidence | Label |
|---|---|---|
| Linear weak-field mean degeneracy is explicit and executable. | Appendix derivation and `source_response_discriminator` tests. | known-physics reformulation |
| Branch-mixture variance, branch separation, source-probe covariance, and visibility are valid discriminator channels in the toy arena. | Appendix formulas and focused unit tests. | useful diagnostic |
| Remote-basis marginal dependence without a causal channel is rejected. | Appendix guardrail and invalid toy-rule test. | clean no-go |
| A pulse-native response law remains a constrained target, not an accepted law. | Kernel contract plus missing conservation/no-signaling/branch-basis inputs. | blocked conditional bridge |

No surviving H6S1 claim is a new prediction or controlled modification. The evidence supports a diagnostic tool and one clean rejection gate for an invalid response rule.

## 13. Final Verdict

The final H6S1 project-rule classification is:

> diagnostic tool

### 13.1 Accepted Inputs

H6S1 accepts only:

- calibrated probe pulse counts from H1/H5-style clock records
- the H5 internal-clock visibility formula
- the existing H6 branch-record and reduced-overlap bookkeeping
- a controlled one-dimensional weak-field Newtonian source/probe arena
- branch probabilities, branch labels, branch overlap, and source/probe relational positions as declared setup fields
- 05/05S low-energy source-to-metric reasoning only as conditional background, not as a quantum source-response law

### 13.2 Accepted Outputs

H6S1 supplies:

- an appendix contract for the quantum source-response discriminator
- deterministic helpers for softened branch potentials, branch proper times, pulse counts, expectation-sourced mean, branch-mixture variance, branch separation, source-probe covariance, and source-probe correlation
- internal clock visibility helpers using the H5 branch proper-time difference
- finite probe marginal distributions for expectation-sourced and branch-mixture bookkeeping
- a no-signaling guardrail that rejects the intentionally invalid remote-basis toy rule
- a conservation classifier for the model families
- an observable-class matrix that names source superpositions, quantum clocks, branch-correlated probe timing, gravitationally mediated entanglement style tests, visibility-loss probes, and null cases

### 13.3 Rejected Overclaims

H6S1 rejects these claims:

- the ensemble mean is a discriminator in the linear weak-field slice
- the branch-mixture helper proves metric superposition
- the branch-mixture helper proves collapse or branch selection
- a pulse-native response kernel has been discovered
- source-response can ignore no-signaling and conservation guardrails
- environmental decoherence can be counted as metric-history decoherence without a separate ledger
- any current H6S1 output is a new external experimental prediction

### 13.4 Allowed Downstream Uses

Downstream work may use H6S1 to:

- test candidate source-response kernels against mean, variance, branch-correlation, visibility, no-signaling, and conservation gates
- design synthetic weak-field source/probe examples without comparing only ensemble means
- reject response rules whose probe marginal depends on a remote basis choice without a causal channel
- name observable classes and artifact ledgers before any experimental-bound comparison
- keep H6 source-response work separate from geometry-action and H7 vacuum claims

### 13.5 Prohibited Downstream Uses

Downstream work must not use H6S1 to:

- claim quantum gravity is solved
- claim classical spacetime emergence is solved
- claim a collapse mechanism is supplied
- treat branch-specific classical metrics as a quantum metric Hilbert space
- fit softening radii or response coefficients to observations as if H6S1 had derived them
- bypass gauge/branch matching, conservation, no-signaling, or environmental backreaction accounting
- promote variance, bimodality, or visibility loss to a gravitational source-response signal without controlling ordinary artifacts

### 13.6 Remaining Assumptions

The unresolved assumptions are:

- the source branch basis must be prepared, stabilized, or derived rather than chosen by convenience
- branch potentials are compared only after a shared relational probe location and matching convention are declared
- the weak-field point-source arena ignores finite source size except through optional softening
- the helper does not model environmental backreaction, electromagnetic leakage, or a full experimental protocol
- collapse/decoherence variants still need causal timing, probability, and conservation ledgers
- a real pulse-native source-response law still needs a normalized kernel, coefficients fixed before comparison, no-signaling proof, and conservation account

### 13.7 Verification Commands

Verified in this environment with:

```bash
uv run python -m unittest tests.test_quantum_source_response
```

```bash
uv run python -m unittest tests.test_h5_visibility tests.test_h6_branch_decoherence
```

The command below was attempted first, but this environment does not currently have `pytest` installed:

```bash
uv run pytest tests/test_quantum_source_response.py
```
