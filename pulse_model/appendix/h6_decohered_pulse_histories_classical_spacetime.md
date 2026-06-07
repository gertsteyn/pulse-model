# Appendix: H6 Decohered Pulse Histories And Classical Spacetime

**Parent hypothesis:** 7. Hypothesis H6: Classical spacetime emerges from decohered pulse-history structure  
**Status:** Accepted with limits for the reduced branch-decoherence toy model and model comparison; full classical-spacetime emergence not accepted  
**Purpose:** Define the conservative metric-branch state model, reduced distinguishability criterion, model comparison, and final H6 emergence verdict.

---

## 1. Scope

H6 asks whether one effective classical spacetime can be understood as the stable branch of a larger set of alternative pulse-count or matter-source histories.

This appendix does not solve H6. It fixes the first bookkeeping layer:

- what degrees of freedom are treated quantum mechanically
- what metric data remain classical or effective
- what counts as a pulse-history branch
- what source-to-metric rule each model family assumes
- which H5 and 05 inputs are allowed
- which risks must remain visible for later H6 work

The first H6 slice is deliberately taxonomic. It is a controlled way to compare models, not a claim that metric superposition has been established.

## 2. Inputs And Assumptions From Earlier Gates

H6 may use two earlier results, both with limits.

### 2.1 H5 Branch-Distinguishability Input

[H5](./h5_superposed_pulse_histories.md) supplies a bounded matter-side distinguishability input. If two branches carry different proper times or pulse counts, an internal clock state may have a branch overlap:

$$
\Gamma_{ab}^{(C)}=\mathrm{Tr}(\rho_C e^{-iH_C(\tau_a-\tau_b)/\hbar})
$$

The corresponding clock visibility is:

$$
\mathcal{V}_{ab}^{(C)}=|\Gamma_{ab}^{(C)}|
$$

H6 may use this overlap as one branch-distinguishability factor. H5 does not define metric quantum states, branch-specific gravitational fields, collapse dynamics, semiclassical sourcing, or energy/no-signaling consistency.

### 2.2 05 And 05S Geometry-Action Input

[The 05 geometry-action result](./geometry_phase_functional_from_pulse_consistency.md) is accepted with limits as a useful conservative result. H6 may use it only as a smooth, low-energy, branch-local classical source-to-metric rule under the 05 assumptions:

- H2 supplies metric data within its accepted scope
- H3 supplies curvature-holonomy input within its accepted scope
- H4 supplies conserved matter phase-response within its accepted scope
- the pulse-consistency cost has a local scalar smooth limit
- the leading response is metric-only, diffeomorphism invariant, and second order
- pulse clocks, stations, and loop labels remain measurement scaffolding rather than action fields
- finite-region variations include the required boundary and joint phases

Under those assumptions, the branch-local source-to-metric equation may be taken as:

$$
G_{\mu\nu}[g_a]+\Lambda g_{\mu\nu}^{(a)}=\frac{8\pi G}{c^4}T_{\mu\nu}^{(a)}
$$

This is not a derivation of general relativity from pulse counts alone. It is the conditional low-energy equation H6 may use when a candidate branch has a smooth classical metric and a conserved effective source.

[The 05S strengthening result](./geometry_action_strengthening_pulse_network.md) may now be used as a stronger conditional support for the same low-energy source-to-metric bridge. H6 may cite 05S only when its admissibility, locality, hinge-defect, scalarization, replacement-invariance, boundary, and correction-suppression assumptions are carried explicitly. 05S does not prove that arbitrary raw pulse records dynamically enforce those conditions, and it does not solve H6 branch selection, metric quantization, energy conservation, no-signaling, or H7 vacuum questions.

### 2.3 Inputs Not Allowed Yet

H6 must not use H7 or vacuum-energy claims as inputs. Vacuum phase-response and renormalization questions are downstream of the H6 source-to-metric choice.

H6 must also not treat 05 or 05S as a metric-superposition theory, a collapse theory, or a proof that classical spacetime emerges. They provide only the conditional low-energy source-to-metric bridge used inside each candidate H6 model family.

## 3. Branch Data Model

A pulse-history branch is a candidate coarse-grained history in which matter, clocks, pulse records, and an effective metric can be consistently described together. A branch label $a$ is not by itself physical; it is a bookkeeping label for a set of relational data.

The minimal branch record is:

$$
\mathcal{B}_a=(\mathcal{R}_a,\rho_M^{(a)},\rho_C^{(a)},J_a,g_a,\chi_a)
$$

The entries mean:

- $\mathcal{R}_a$: pulse records, clock readouts, path labels, event coincidences, boundary data, and branch-closure data
- $\rho_M^{(a)}$: matter state or reduced matter state assigned to the branch
- $\rho_C^{(a)}$: internal clock state assigned to the branch, when an operational clock is present
- $J_a$: effective source data used by the source-to-metric rule, usually represented by $T_{\mu\nu}^{(a)}$
- $g_a$: classical or effective metric assigned to the branch, if the model family assigns one
- $\chi_a$: gauge, boundary, or relational matching data needed to compare branch $a$ with other branches

The branch is admissible only if its source and metric satisfy the conservation and boundary assumptions required by the chosen model family. In the branch-local Einstein-equation slice, that means $T_{\mu\nu}^{(a)}$ must be compatible with the Bianchi identity and the boundary data for $g_a$.

## 4. Quantum And Classical Degrees Of Freedom

The first H6 model keeps the degree-of-freedom split explicit.

Quantum degrees of freedom may include:

- matter fields or particles
- internal clock states
- center-of-mass wave packets
- environmental records that decohere branch labels
- branch labels used as a reduced-state basis after decoherence

Classical or effective degrees of freedom may include:

- one semiclassical metric sourced by an expectation value
- branch-conditioned classical metrics
- stochastic collapse-selected metrics
- boundary data and gauge-matching maps
- smooth low-energy source fields used in the 05 source-to-metric rule

The conservative H6 model does not assert that $g_a$ is a quantum state. When a formula uses $g_a$ beside a quantum state, $g_a$ is an effective classical label unless a later H6 task explicitly defines a quantum metric Hilbert space.

## 5. Candidate Model Families

H6 must compare at least three model families. They agree on the branch-data vocabulary above, but they disagree about how matter histories source metric structure.

### 5.1 Semiclassical Metric Sourced By Expectation Values

In the semiclassical family, matter and clocks remain quantum, but there is one effective classical metric $g_{\mathrm{sc}}$. The source is an expectation value in the quantum matter state:

$$
G_{\mu\nu}[g_{\mathrm{sc}}]+\Lambda g_{\mu\nu}^{\mathrm{sc}}=\frac{8\pi G}{c^4}\langle\hat{T}_{\mu\nu}\rangle_{\rho_M}
$$

In this family:

- quantum degrees of freedom: matter, clocks, and environmental records
- classical or effective degrees of freedom: a single metric $g_{\mathrm{sc}}$
- pulse-history branches: alternative matter, clock, or record histories inside one metric background
- branch-identifying data: pulse records, reduced matter states, clock overlaps, environment records, and a common gauge/boundary convention
- source-to-metric rule: expectation-value sourcing under the 05 low-energy assumptions

This family is conservative because it avoids branch-specific metrics. Its risk is that expectation-value sourcing can blur macroscopically distinct alternatives and can make state-update, energy-conservation, and no-signaling questions sharp.

### 5.2 Branch-Specific Classical Metrics Conditioned On Decohered Histories

In the branch-specific family, each decohered matter or pulse-history branch is assigned its own effective classical metric $g_a$. The branch state is best read as a classical-quantum bookkeeping ensemble:

$$
\rho_{\mathrm{eff}}=\sum_a p_a |a\rangle\langle a|\otimes\rho_M^{(a)}\otimes[g_a]
$$

Here $[g_a]$ is a classical branch label, not a metric ket. Each branch may use the branch-local source-to-metric equation:

$$
G_{\mu\nu}[g_a]+\Lambda g_{\mu\nu}^{(a)}=\frac{8\pi G}{c^4}T_{\mu\nu}^{(a)}
$$

In this family:

- quantum degrees of freedom: matter, clocks, and records inside each branch
- classical or effective degrees of freedom: one effective metric per decohered branch
- pulse-history branches: decohered alternatives with distinct matter-source and clock/pulse records
- branch-identifying data: $\mathcal{B}_a$, branch probability $p_a$, pairwise overlaps, boundary data, and gauge matching $\chi_a$
- source-to-metric rule: branch-local classical sourcing under the 05 low-energy assumptions

This family is useful for H6 because it gives later tasks explicit $g_a$ and $g_b$ handles to compare. Its risk is overclaiming: a set of branch-conditioned classical metrics is not yet a quantum superposition of metrics, and it does not by itself explain how one classical branch is selected or why energy is conserved through selection.

### 5.3 Collapse Or Decoherence Variants

Collapse/decoherence variants add a rule that suppresses or removes off-diagonal branch coherence and then assigns the effective metric from the selected or dominant branch. A schematic update is:

$$
\rho_M \rightarrow \rho_M^{(a)},\quad g \rightarrow g_a,\quad p_a=P(a)
$$

In this family:

- quantum degrees of freedom: pre-selection matter, clocks, and environmental records
- classical or effective degrees of freedom: the selected post-decoherence or post-collapse metric
- pulse-history branches: alternatives in the pre-selection state that become effectively classical records
- branch-identifying data: collapse/decoherence probabilities, branch records, post-selection sources, and source-to-metric boundary data
- source-to-metric rule: either expectation-value sourcing before selection or branch-local sourcing after selection, stated explicitly for the variant

This family gives H6 a way to discuss classical outcomes. Its risk is that any real collapse rule must pass energy-conservation and no-signaling checks. Pure environmental decoherence alone also does not choose a unique outcome; it only suppresses interference in a chosen basis.

## 6. Distinguishability And Decoherence Targets

For later H6 work, pairwise branch overlap should be tracked before any claim of classicality. H5 supplies the clock factor. H6 may multiply it by environmental, metric-history, and technical factors only when those factors are modeled separately:

$$
\Gamma_{ab}=\Gamma_{ab}^{(C)}\Gamma_{ab}^{(E)}\Gamma_{ab}^{(G)}\Gamma_{ab}^{(N)}
$$

Here $\Gamma_{ab}^{(E)}$ is ordinary environmental record overlap, $\Gamma_{ab}^{(G)}$ is any metric-history record overlap, and $\Gamma_{ab}^{(N)}$ is technical contrast loss or nuisance visibility. A small $\Gamma_{ab}^{(E)}$ must not be relabeled as metric-history decoherence.

A simple first distinguishability target for `sci-7sr.3` is:

$$
D_{ab}=1-|\Gamma_{ab}|
$$

This is only a first reduced measure. It is acceptable for a toy model, but a later H6 result must state which subsystem is traced out, which basis is stable, and whether the suppression is ordinary environmental decoherence, proper-time clock distinguishability, or a metric-history effect.

### 6.1 Reduced Two-Branch Criterion

The executable H6 toy criterion is intentionally minimal. For a two-branch reduced state with branch probability $p_a$ and total branch-overlap magnitude $|\Gamma_{ab}|$, the off-diagonal coherence magnitude is:

$$
C_{ab}=\sqrt{p_a(1-p_a)}|\Gamma_{ab}|
$$

The branch pair is treated as decohered in the toy model when:

$$
C_{ab}\leq\epsilon_{\mathrm{coh}}
$$

One effective branch dominates only when decoherence is accompanied by a sufficiently large branch probability:

$$
\max(p_a,1-p_a)\geq p_{\mathrm{dom}}
$$

So low overlap alone gives an effectively classical mixture, not a selected classical branch. Equal-probability branches with tiny overlap are decohered alternatives; they are not a single dominant spacetime branch.

The reduced helper `gaussian_branch_record_overlap` supplies a dimensionless toy record-overlap factor:

$$
\Gamma_{\mathrm{toy}}=\exp(-(\Delta r/\sigma)^2/2)
$$

The same toy form may be used for an environmental record or a metric-history record, but the factor must be passed separately to `combined_branch_overlap`. This keeps ordinary environmental decoherence distinct from metric-history distinguishability.

The implementation lives in `src/pulse_model/calculations.py`:

- `combined_branch_overlap` multiplies the separated clock, environmental, metric-history, and technical factors
- `branch_distinguishability` returns $1-|\Gamma_{ab}|$
- `two_branch_coherence_magnitude` returns $C_{ab}$
- `two_branch_decohered` applies the coherence threshold
- `effective_branch_dominates` requires both decoherence and a dominant branch probability

The regression tests in `tests/test_h6_branch_decoherence.py` cover the toy criterion and the separation between ordinary environmental and metric-history factors.

The first classicality criterion should therefore be conservative:

- branch records are stable under environmental monitoring
- pairwise overlaps are small for the relevant branch pairs
- the metric assignment is insensitive to unobservable gauge relabeling
- source-to-metric data are conserved in the branch
- probe pulse histories see one effective metric within experimental resolution

## 7. Model-Comparison Handles

The next H6 comparison task needs observables or failures that distinguish the model families. The first handles are:

- single-metric versus branch-metric proper times for a probe clock
- expectation-value source versus selected-branch source in a two-lump mass superposition
- whether off-diagonal branch terms affect a probe pulse history
- whether branch selection changes total energy or stress-energy conservation
- whether branch comparisons survive a diffeomorphism or gauge relabeling
- whether collapse/decoherence variants permit controllable signaling through metric response

These handles are not yet predictions. They are the required comparison axes for `sci-7sr.1`.

## 8. Model Comparison

This section compares the three H6 model families on one deliberately small source/probe setup. It does not decide H6 globally.

### 8.1 Two-Branch Source And Probe Setup

Use two decohered source branches, $a$ and $b$, with probabilities $p_a$ and $1-p_a$. The source is localized differently in the two branches, and a weak probe clock sits at a fixed relational location $P$ for a common coordinate interval $T$.

In the low-energy 05 slice, the branch-local potentials at the probe are $\Phi_a(P)$ and $\Phi_b(P)$. For a slow probe clock, the branch-conditioned clock times are approximated by:

$$
\tau_a^{(P)}=T(1+\Phi_a(P)/c^2)
$$

$$
\tau_b^{(P)}=T(1+\Phi_b(P)/c^2)
$$

The probe-clock difference between branch-conditioned metrics is:

$$
\Delta\tau_P=T(\Phi_a(P)-\Phi_b(P))/c^2
$$

The sci-7sr.3 criterion supplies the branch coherence:

$$
C_{ab}=\sqrt{p_a(1-p_a)}|\Gamma_{ab}|
$$

The comparison asks what the probe sees once $C_{ab}\leq\epsilon_{\mathrm{coh}}$, and whether a single branch dominates.

### 8.2 Compact Family Comparison

| Model family | Source-to-metric rule | What the probe clock sees | Equal-probability decohered branches | Off-diagonal branch terms |
|---|---|---|---|---|
| Semiclassical expectation-sourced metric | One metric sourced by the expectation value of the stress-energy operator. | One averaged weak-field potential and one averaged probe time. | A decohered equal mixture still gives one expectation-sourced metric, not a selected branch. | In the simplest reduced closure they enter only through the expectation value; if the expectation value has already decohered to a diagonal mixture, no branch-specific metric signal remains. |
| Branch-specific classical metrics | Each decohered branch uses its own classical source and branch-local 05 equation. | A branch-correlated clock reads the time for that branch's metric. | It is a mixture of two effective metrics, not one dominant classical spacetime. | They are neglected after decoherence; before decoherence the branch-specific classical picture has no accepted rule for coherent metric interference. |
| Collapse/decoherence variants | Before selection the rule must be specified; after selection the selected source determines the effective metric. | A selected run reads the selected branch metric if collapse or effective selection occurs before the probe record is fixed. | Pure decoherence gives a mixture; collapse adds a selection postulate or stochastic rule. | Collapse variants must say whether and how off-diagonal terms are physically removed; environmental decoherence alone only suppresses access to them. |

### 8.3 Observable Distinction And Degeneracy

The clean distinction in this reduced setup is not the ensemble mean. The semiclassical averaged probe time is:

$$
\tau_{\mathrm{sc}}^{(P)}=T(1+(p_a\Phi_a(P)+(1-p_a)\Phi_b(P))/c^2)
$$

The branch-specific ensemble mean is:

$$
\langle\tau^{(P)}\rangle=p_a\tau_a^{(P)}+(1-p_a)\tau_b^{(P)}
$$

These are equal in the linear weak-field approximation. Therefore an experiment that only measures the ensemble mean of the probe clock is degenerate between the expectation-sourced model and the branch-specific mixture in this first slice.

The first possible observable distinction is distributional or branch-correlated:

- expectation-sourced semiclassical model: one probe-clock value centered on the averaged potential
- branch-specific model: two branch-correlated probe-clock values, with weights $p_a$ and $1-p_a$
- collapse-after-selection model: one selected value per run, statistically matching the branch-specific distribution if selection occurs before the probe readout

The variance is a compact way to state the branch-specific signal:

$$
\mathrm{Var}(\tau^{(P)})=p_a(1-p_a)(\tau_a^{(P)}-\tau_b^{(P)})^2
$$

This variance is not automatically a metric-superposition signal. It is only a branch-correlated probe-clock spread. Ordinary source noise, environmental records, preparation uncertainty, and readout noise must be separated before any H6 interpretation.

### 8.4 Equal Probability Versus Dominance

If $p_a=1/2$ and $C_{ab}$ is below threshold, H6 has two decohered alternatives. It does not have one dominant classical spacetime. In that case:

- semiclassical sourcing gives a single averaged metric
- branch-specific sourcing gives a diagonal mixture of two metrics
- collapse variants need an extra rule to explain why one branch is realized in a run

One effective branch dominates only when the sci-7sr.3 criterion has both parts:

$$
C_{ab}\leq\epsilon_{\mathrm{coh}}
$$

$$
\max(p_a,1-p_a)\geq p_{\mathrm{dom}}
$$

This distinction matters because decoherence suppresses interference, while dominance identifies a high-weight branch. H6 must not replace one with the other.

### 8.5 Risk Review For The Comparison

Energy conservation: the branch-specific and collapse families must keep each branch source compatible with the branch-local Bianchi identity. A discontinuous collapse from an expectation-sourced metric to a selected-source metric needs explicit energy and momentum accounting.

No-signaling: an expectation-sourced metric or collapse-triggered metric can become nonlinear if distant measurement choices change the effective source. H6 must not accept a model unless the metric response is tied to local records, causal update rules, or another mechanism that prevents controllable faster-than-light signaling.

Gauge and diffeomorphism matching: $\Phi_a(P)$ and $\Phi_b(P)$ are meaningful only after a shared relational probe location, boundary convention, and matching map are specified. A difference in coordinate potential is not an observable distinction by itself.

Branch selection and preferred basis: branch-specific and collapse variants must explain why the source-localization basis is stable. Environmental decoherence can justify a reduced diagonal basis only relative to a system-environment split; it does not by itself supply a fundamental branch-selection rule.

Degeneracy: in the linear weak-field toy setup, ensemble means are degenerate. A useful next H6 comparison must target branch-correlated probe records, variance, bimodality, or timing of selection relative to probe readout.

Boundaries: this comparison does not establish metric superposition, a collapse mechanism, classical emergence, H7 vacuum claims, or 05S strengthening results. It only identifies where the current H6 families agree, differ, or remain degenerate in a two-branch source/probe slice.

## 9. Required Risks And Boundaries

H6 must keep the following risks explicit.

### Energy Conservation

The 05 source-to-metric rule relies on conserved source data. If branch selection or collapse changes the source discontinuously, the model must explain where the corresponding energy and momentum accounting goes. A branch-local equation with nonconserved $T_{\mu\nu}^{(a)}$ is not admissible in the 05 low-energy slice.

### No-Signaling

Any state-dependent metric response can become nonlinear when combined with measurement updates. H6 must check that a controllable choice of measurement basis cannot change a distant effective metric signal faster than allowed by the causal structure of the model.

### Gauge And Diffeomorphism Matching

Metric branches cannot be compared by coordinate components alone. H6 comparisons require relational observables, shared boundary data, or an explicit matching map $\chi_a$. Without that, differences between $g_a$ and $g_b$ may be gauge artifacts.

### Branch Selection And Preferred Basis

Decoherence suppresses interference relative to a system-environment split and basis. H6 must state why the chosen pulse-history branch basis is stable and physically relevant. It must not assume the answer by choosing convenient branch labels.

### Overclaim Boundaries

This appendix does not establish:

- metric superposition
- classical spacetime emergence
- a collapse mechanism
- a derivation of the Einstein-Hilbert action from pulse counts alone
- a solution to vacuum energy or the cosmological-constant problem
- a proof that branch-specific metrics are compatible with energy conservation and no-signaling

## 10. H6 Emergence Report

### 10.1 Verdict

H6 is **accepted with limits at the reduced toy-model level**.

The current Pulse Model can now do the following narrow job:

- define branch records and branch-conditioned effective metric data
- keep quantum matter/clock records separate from classical or effective metric labels
- quantify reduced branch distinguishability with separated clock, environmental, metric-history, and technical overlap factors
- state when a two-branch reduced state is decohered in the toy model
- distinguish decohered equal-probability alternatives from one dominant effective branch
- compare semiclassical expectation-sourced, branch-specific classical-metric, and collapse/decoherence model families on the same two-branch source/probe setup

This is enough to make H6 a coherent reduced model comparison. It is not enough to claim that the Pulse Model has explained classical spacetime emergence.

### 10.2 What Is Accepted

The accepted reduced H6 result is:

$$
\Gamma_{ab}=\Gamma_{ab}^{(C)}\Gamma_{ab}^{(E)}\Gamma_{ab}^{(G)}\Gamma_{ab}^{(N)}
$$

with a two-branch coherence magnitude:

$$
C_{ab}=\sqrt{p_a(1-p_a)}|\Gamma_{ab}|
$$

and a toy decoherence condition:

$$
C_{ab}\leq\epsilon_{\mathrm{coh}}
$$

One effective branch is called dominant in this reduced model only when decoherence is accompanied by high branch weight:

$$
\max(p_a,1-p_a)\geq p_{\mathrm{dom}}
$$

The accepted source-to-metric input is conditional. For branch-local classical metrics, H6 may use the 05/05S low-energy Einstein-equation bridge only in the admissible smooth regime and only with the 05/05S assumptions carried forward.

### 10.3 What Remains Blocked

The stronger H6 claim remains blocked.

H6 does not yet establish:

- a quantum Hilbert space of metric states
- a physical rule for coherent metric superposition
- a collapse mechanism or fundamental branch-selection law
- a no-signaling state-update rule for metric response
- energy-momentum accounting through collapse or branch selection
- gauge-invariant comparison of arbitrary branch metrics without shared boundary or relational matching data
- recovery of one classical GR spacetime in generic macroscopic regimes from pulse-history decoherence alone

Those are not formatting caveats. They are the reasons H6 is accepted only as a reduced toy-model and taxonomy result.

### 10.4 Toy-Model Outcome

At the toy-model level, H6 is not failed. The branch-overlap criterion is explicit and tested in `tests/test_h6_branch_decoherence.py`, and the model comparison identifies a concrete degeneracy:

- ensemble-mean probe-clock measurements are degenerate between semiclassical expectation-sourced metrics and branch-specific mixtures in the linear weak-field slice
- branch-correlated variance, bimodality, or selection timing are the first handles that could distinguish model families
- equal-probability decohered branches form a mixture, not one selected classical spacetime

The toy model therefore succeeds as a diagnostic and comparison tool. It fails only if it is misread as an emergence proof.

### 10.5 Prerequisites For A Stronger H6 Claim

A stronger H6 claim requires at least:

- a precise choice between semiclassical, branch-specific, collapse/decoherence, or another source-to-metric rule
- a gauge-invariant branch-comparison observable or boundary matching prescription
- an energy-conservation account for source updates and selected branches
- a no-signaling account for state-dependent metric response
- a stable branch basis derived from actual record/environment dynamics, not chosen by convenience
- a macroscopic limit showing why ordinary observers recover one GR metric inside the accepted 05/05S low-energy regime
- explicit separation of ordinary environmental decoherence from proper-time clock distinguishability and metric-history distinguishability

Until those prerequisites are met, H6 should be used downstream as a bounded source-to-metric and branch-distinguishability framework, not as a completed emergence theory.

### 10.6 Downstream Status

H6 now provides H7 and later work with a disciplined warning: metric-sensitive phase-response should be analyzed only after a source-to-metric rule is named and its branch-selection risks are visible. H6 does not license H7 vacuum-energy claims, and it does not derive $\Lambda$, vacuum renormalization, or absolute vacuum phase behavior.

The final H6 label for this appendix is:

> Accepted with limits for reduced branch-decoherence bookkeeping and model comparison; blocked for full classical-spacetime emergence.

## 11. Handoff To Later Work

This appendix unblocks `sci-7sr.3` by defining:

- branch records $\mathcal{B}_a$
- pairwise clock overlaps $\Gamma_{ab}^{(C)}$
- total reduced overlaps $\Gamma_{ab}$
- first distinguishability target $D_{ab}$
- two-branch coherence magnitude $C_{ab}$
- a threshold criterion for reduced decoherence
- a probability-plus-decoherence criterion for one effective branch to dominate
- the need to separate ordinary environmental decoherence from clock/proper-time distinguishability
- executable toy helpers in `src/pulse_model/calculations.py` with tests in `tests/test_h6_branch_decoherence.py`

It unblocks `sci-7sr.1` by defining model-comparison families:

- one semiclassical expectation-sourced metric
- branch-specific classical metrics conditioned on decohered histories
- collapse/decoherence variants with explicit source-update rules
- a two-branch source/probe comparison that distinguishes ensemble-mean degeneracy from branch-correlated probe-clock variance

It completes `sci-7sr.2` by recording the H6 verdict: reduced toy-model H6 is accepted with limits, while full classical-spacetime emergence remains blocked on the prerequisites named above.
