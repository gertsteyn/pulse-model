# Appendix: H7 Vacuum Phase-Response

**Parent hypothesis:** 8. Hypothesis H7: Vacuum energy as phase-response  
**Status:** Constrained reformulation accepted with limits; no cosmological-constant solution or testable H7 deviation accepted  
**Purpose:** Map the QFT-in-curved-spacetime, renormalization, cosmological-constant, and observational constraints that any H7 claim must satisfy, formalize the allowed distinction between absolute vacuum phase and metric-sensitive vacuum phase-response, and test the resulting parameterization against cosmology constraints.

---

## 1. Scope

H7 asks whether the cosmological-constant problem can be restated as a question about metric-sensitive phase-response rather than absolute vacuum phase density.

The completed H7 result is deliberately conservative. It does not propose a Pulse Model solution, and it does not claim that absolute uniform vacuum phase fails to gravitate. It records the constraints, accepted reformulation, and rejected stronger claims that any later extension must respect.

The conservative target remains:

$$
\rho_{\mathrm{vac}}^{\mathrm{naive}} \gg \rho_\Lambda^{\mathrm{observed}}
$$

without contradicting QFT in curved spacetime, covariant stress-energy conservation, renormalization practice, or precision cosmology.

## 2. Allowed Inputs From Earlier Gates

H7 is downstream of H4, 05, 05S, and H6. Each input is allowed only within its closed verdict.

| Input | What H7 may use | What H7 must not infer |
|---|---|---|
| [H4 matter phase-response](./h4_stress_energy_as_phase_response.md) | The standard inverse-metric variation convention for stress-energy, rewritten as matter phase-response. | H4 did not cover renormalized vacuum stress-energy, anomalies, spinors, fluids, or nonminimal quantum matter as accepted results. |
| [05 geometry-action result](./geometry_phase_functional_from_pulse_consistency.md) | A conditional smooth, low-energy Einstein-Hilbert plus cosmological-constant phase under explicit locality, scalarization, metric-only, boundary, and second-order assumptions. | 05 did not derive $G$, derive $\Lambda$, solve vacuum-energy renormalization, or prove that absolute vacuum phase is nongravitating. |
| [05S geometry-action strengthening](./geometry_action_strengthening_pulse_network.md) | Stronger conditional support for the same low-energy source-to-metric bridge when admissibility, locality, hinge-defect, scalarization, replacement-invariance, boundary, and correction-suppression assumptions are carried. | 05S did not prove arbitrary pulse records dynamically enforce those assumptions and did not solve the cosmological-constant problem. |
| [H6 decohered histories](./h6_decohered_pulse_histories_classical_spacetime.md) | A warning that source-to-metric rules, branch selection, energy accounting, no-signaling, and classical metric emergence must remain explicit. | H6 did not establish a full metric Hilbert space, branch-selection law, no-signaling metric update rule, or macroscopic emergence theorem. |

The H4 phase-response identity remains the matter-side convention:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

H7 treats an analogous renormalized vacuum phase-response as meaningful only when it is tied to a specified metric-dependent renormalized functional and its effective stress tensor.

## 3. QFT-In-Curved-Spacetime Constraints

The relevant standard benchmark is QFT on a classical curved background, with backreaction added only through a renormalized expectation value. The minimum constraints are:

- **Local covariance:** the construction of observables and stress-energy must be local and covariant, not tied to a preferred pulse station, foliation, global vacuum, or coordinate time.
- **State dependence:** curved spacetime generally lacks a unique global vacuum. A vacuum phase-response claim must name the state class, usually a physically admissible Hadamard or equivalent state, and must not treat one preferred vacuum as locally covariant by default.
- **Renormalized stress-energy:** the source is not a formal divergent zero-point sum. It must be a renormalized expectation value or a renormalized effective-action variation:

$$
\langle T_{\mu\nu}\rangle_{\mathrm{ren}}=-\frac{2}{\sqrt{-g}}\frac{\delta W_{\mathrm{ren}}}{\delta g^{\mu\nu}}
$$

- **Conservation:** the renormalized source used in a semiclassical or 05-style low-energy equation must satisfy:

$$
\nabla^\mu \langle T_{\mu\nu}\rangle_{\mathrm{ren}}=0
$$

This is required by the Bianchi identity if the left side is the Einstein-Hilbert plus cosmological-constant response.

- **Regularization and counterterms:** divergences and scheme dependence must be absorbed into allowed local gravitational counterterms, including the cosmological constant, Newton constant, boundary terms, and higher-curvature terms when they are within the effective description.
- **Renormalization ambiguity:** finite local curvature terms are not automatically new physics. H7 must distinguish a physical residual from a counterterm choice or a fitted value of $\Lambda$.
- **Trace and anomaly terms:** conformal or trace anomalies can generate curvature-dependent stress-energy. They are metric-sensitive phase-responses, but they are not a solution to the constant vacuum-energy contribution unless their magnitude, conservation, and observational effects are controlled.
- **Backreaction regime:** if H7 uses semiclassical gravity, the equation is at most:

$$
G_{\mu\nu}+\Lambda_{\mathrm{ren}}g_{\mu\nu}+\Delta_{\mu\nu}^{\mathrm{curv}}=\frac{8\pi G_{\mathrm{ren}}}{c^4}\langle T_{\mu\nu}\rangle_{\mathrm{ren}}
$$

where $\Delta_{\mu\nu}^{\mathrm{curv}}$ represents higher-curvature or other allowed local effective-action responses. Ignoring it is an assumption that must be justified by scale suppression.

## 4. Renormalization And Cosmological-Constant Pitfalls

H7 must avoid several standard traps.

First, a constant term in a nongravitational Lagrangian may be physically irrelevant, but a constant action density coupled to $\sqrt{-g}$ has a metric variation. A vacuum term of the schematic form:

$$
S_{\mathrm{vac}}=-\rho_{\mathrm{vac}}\int_U \sqrt{-g}\,d^4x
$$

contributes a vacuum-like stress tensor proportional to $g_{\mu\nu}$ and is degenerate with a cosmological-constant counterterm. Therefore the statement "absolute phase does not gravitate" is not allowed unless H7 supplies a variational, symmetry, or renormalization argument that removes that metric variation without breaking covariance and conservation.

Second, renormalization alone is not a naturalness solution. The observed effective value can always be expressed as a renormalized parameter, but H7 must not count that bookkeeping as an explanation unless a protective mechanism or testable residual is supplied.

Third, naive cutoff sums are useful for exposing the hierarchy but are not themselves the covariant renormalized source. A valid H7 comparison must separate:

- bare or cutoff-dependent vacuum terms
- counterterm choices
- finite renormalized effective stress-energy
- curvature-dependent anomalous or higher-derivative responses
- the measured late-time dark-energy component

Fourth, any proposal that cancels vacuum energy must still pass the equivalence-principle, energy-conservation, and radiative-stability questions. A cancellation that works in one state, epoch, or cutoff scheme but fails under standard model thresholds, curvature changes, or renormalization-group running is not enough.

## 5. Absolute Phase Versus Metric-Sensitive Response

The useful H7 distinction is not between "phase" and "energy." It is between a bookkeeping phase that is not part of the metric-dependent action and a covariant action term whose metric variation contributes to the source.

### 5.1 Absolute Bookkeeping Phase

An absolute phase counter may be represented schematically as:

$$
\Theta_{\mathrm{abs}}=\theta_0 N
$$

where $N$ is an external count or normalization not varied with the metric. If this object is not a functional of $g_{\mu\nu}$, then:

$$
\frac{\delta\Theta_{\mathrm{abs}}}{\delta g^{\mu\nu}}=0
$$

This is not a dynamical result. It is only the statement that something omitted from the metric-dependent action cannot source the metric through metric variation. H7 may use this category only for unobservable global phases, state normalization phases, or other pure bookkeeping quantities.

This category does not solve the cosmological-constant problem, because the problem concerns vacuum contributions that appear in a generally covariant effective action.

### 5.2 Uniform Covariant Action Density

A uniform vacuum contribution that is part of the covariant effective action has the schematic form:

$$
\Theta_0[g]=-\frac{1}{\hbar}\rho_0\int_U \sqrt{-g}\,d^4x
$$

Its phase-response is metric-sensitive:

$$
T_{\mu\nu}^{(0)}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_0}{\delta g^{\mu\nu}}
$$

and is vacuum-like:

$$
T_{\mu\nu}^{(0)}=-\rho_0 g_{\mu\nu}
$$

up to the chosen sign and unit convention for the action density. The important point is invariant: a uniform covariant density is degenerate with a cosmological-constant term. It cannot be discarded by calling it absolute phase.

### 5.3 Counterterm And Renormalized-Response Split

The H7-compatible split is:

$$
\Theta_{\mathrm{eff}}[g,\omega;\mu]=\Theta_{\mathrm{geom}}^{\mathrm{bare}}[g]+\Theta_{\mathrm{ct}}[g;\mu]+\Theta_{\mathrm{vac}}^{\mathrm{ren}}[g,\omega;\mu]
$$

Here:

- $g$ is the smooth low-energy metric in the accepted 05/05S regime
- $\omega$ is the chosen quantum state or state class
- $\mu$ is the renormalization scale or scheme label
- $\Theta_{\mathrm{ct}}$ contains local counterterms, including the cosmological constant, Newton constant, higher-curvature, and boundary terms
- $\Theta_{\mathrm{vac}}^{\mathrm{ren}}$ is the finite state-dependent and curvature-dependent residual after regularization and counterterm choice

The vacuum phase-response relevant to a source-to-metric equation is:

$$
T_{\mu\nu}^{\mathrm{vac,H7}}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{vac}}^{\mathrm{ren}}}{\delta g^{\mu\nu}}
$$

It may be decomposed only after the renormalization convention is stated:

$$
T_{\mu\nu}^{\mathrm{vac,H7}}=-\rho_{\Lambda,\mathrm{eff}}g_{\mu\nu}+T_{\mu\nu}^{\mathrm{state}}+T_{\mu\nu}^{\mathrm{curv}}
$$

The terms mean:

- $\rho_{\Lambda,\mathrm{eff}}$ is the observed or fitted constant vacuum-like contribution after bare terms and counterterms are combined
- $T_{\mu\nu}^{\mathrm{state}}$ is state-dependent finite stress-energy
- $T_{\mu\nu}^{\mathrm{curv}}$ is curvature-dependent anomalous or higher-derivative response

Each term must satisfy the combined conservation law:

$$
\nabla^\mu T_{\mu\nu}^{\mathrm{vac,H7}}=0
$$

or be paired with explicit geometric counterterms whose variation makes the total equation conserved.

### 5.4 Low-Energy Source Equation

Within the accepted 05/05S assumptions, the branch-local low-energy equation may be written as:

$$
G_{\mu\nu}+\Lambda_{\mathrm{fit}}g_{\mu\nu}+\Delta_{\mu\nu}^{\mathrm{curv}}=\frac{8\pi G_{\mathrm{ren}}}{c^4}\left(T_{\mu\nu}^{\mathrm{matter}}+T_{\mu\nu}^{\mathrm{state}}\right)
$$

This is a conservative effective-field-theory organization. It says the constant vacuum-like part is absorbed into $\Lambda_{\mathrm{fit}}$, while nonconstant finite vacuum response may remain on the source side or be moved into curvature terms by convention.

The equation is H7-compatible only if:

- $T_{\mu\nu}^{\mathrm{matter}}$ uses the H4 inverse-metric phase-response convention
- the geometric side keeps the 05/05S smooth, local, metric-only, diffeomorphism-invariant, boundary-aware, low-energy assumptions
- H6 branch-local source-to-metric risks are not hidden if the source is assigned branch by branch
- $\Delta_{\mu\nu}^{\mathrm{curv}}$ is negligible only when a scale argument makes it negligible

### 5.5 What The Formalization Decides

This formalization accepts a narrow distinction:

- A pure absolute bookkeeping phase has no metric source because it is not a metric functional.
- A uniform covariant vacuum action density is metric-sensitive and contributes as a cosmological-constant-like term.
- The only conservative H7 object that can gravitate is the metric variation of the renormalized effective action.
- Calling that object "phase-response" is compatible with H4, but it is not yet a solution to the cosmological-constant problem.

Therefore 08.2 produces a constrained formal vocabulary, not a new vacuum-energy mechanism. A stronger H7 claim still needs a symmetry, dynamical cancellation, radiative-stability argument, or testable residual that explains why $\rho_{\Lambda,\mathrm{eff}}$ is small.

## 6. Observational Constraint Map

Numerical observational limits are dated because they move. The current H7 reference point for this appendix is 2026-06-07.

| Constraint class | Dated anchor | H7 consequence |
|---|---|---|
| CMB baseline | Planck 2018 base-$\Lambda$CDM gives $H_0=(67.4\pm0.5)\,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1}$ and $\Omega_m=0.315\pm0.007$ under the model assumptions. | A constant-vacuum H7 parameter must reproduce a dark-energy scale near the usual observed $\Lambda$CDM value, not a particle-physics cutoff scale. |
| Observed dark-energy scale | Combining a flat late-time $\Omega_\Lambda$ near $0.69$ with the Planck-scale $H_0$ gives $\Lambda$ of order $10^{-52}\,\mathrm{m}^{-2}$ and $\rho_\Lambda$ of order $5\times10^{-10}\,\mathrm{J}\,\mathrm{m}^{-3}$. | H7 must explain, fit, or deliberately parameterize this tiny effective source. Merely renaming it phase-response is not a prediction. |
| BAO and expansion history | DESI DR2 2025 uses the first three survey years and more than 14 million galaxies and quasars for BAO cosmology. Its key paper reports flat $\Lambda$CDM is a good description but is in mild tension with CMB-preferred parameters, and $w_0w_a$ dark energy can fit combined data better. | H7 must be compatible with BAO distances and must state whether it predicts constant $w=-1$, a $w_0w_a$-like deviation, or no calculable deviation. |
| Dynamical dark-energy hints | DESI DR2 reports a $3.1\sigma$ preference for $w_0w_a$ over $\Lambda$CDM with DESI BAO plus CMB, and $2.8$ to $4.2\sigma$ when supernova samples are included. DESI's extended analysis says current data prefer models with phantom crossing, while alternatives cannot yet be ruled out. | H7 cannot declare $\Lambda$CDM false or evolving dark energy established. It may use these data only as a consistency pressure on any claimed phase-response dynamics. |
| Supernova and low-redshift calibration | The 2025 PDG dark-energy review emphasizes that supernova calibration, sample choices, and coming Rubin/Roman data are central to deciding whether evolving dark energy is real. | A claimed low-redshift H7 deviation must survive SN systematics and should not be tuned to one compilation only. |
| Structure growth and lensing | The 2025 PDG review treats $S_8$ and weak-lensing tensions as unsettled, with baryonic feedback and intrinsic-alignment modeling still important. | H7 must not change the gravitational source in a way that spoils structure growth, lensing, or redshift-space distortion consistency. |
| Local and laboratory constraints | Reviews of the cosmological-constant problem discuss Casimir, Lamb-shift, planetary, atomic, and free-fall constraints as evidence and bounds, not as direct measurements of a gravitating absolute vacuum density. | H7 must not use Casimir-like effects as proof that all absolute zero-point energy gravitates or does not gravitate. |

## 7. Cosmology Consistency Test

The 08.2 formalization leaves one conservative effective parameterization:

$$
T_{\mu\nu}^{\mathrm{vac,H7}}=-\rho_{\Lambda,\mathrm{eff}}g_{\mu\nu}+T_{\mu\nu}^{\mathrm{state}}+T_{\mu\nu}^{\mathrm{curv}}
$$

The constant term is covariantly conserved when $\rho_{\Lambda,\mathrm{eff}}$ is constant:

$$
\nabla^\mu(-\rho_{\Lambda,\mathrm{eff}}g_{\mu\nu})=0
$$

so it is compatible with the Bianchi identity and the 05/05S low-energy source-to-metric equation. That compatibility is not a prediction. It only says the effective cosmological constant can be fitted in the standard way.

### 7.1 Observed Constant-Response Scale

The executable H7 helpers pin the conversion:

$$
\rho_{\mathrm{crit}}^{E}=\frac{3H_0^2c^2}{8\pi G}
$$

$$
\rho_{\Lambda,\mathrm{eff}}=\Omega_\Lambda\rho_{\mathrm{crit}}^{E}
$$

$$
\Lambda_{\mathrm{eff}}=\frac{8\pi G}{c^4}\rho_{\Lambda,\mathrm{eff}}
$$

Using $H_0=67.4\,\mathrm{km}\,\mathrm{s}^{-1}\,\mathrm{Mpc}^{-1}$ and $\Omega_\Lambda=0.685$ gives:

$$
\rho_{\mathrm{crit}}^{E}=7.67\times10^{-10}\,\mathrm{J}\,\mathrm{m}^{-3}
$$

$$
\rho_{\Lambda,\mathrm{eff}}=5.25\times10^{-10}\,\mathrm{J}\,\mathrm{m}^{-3}
$$

$$
\Lambda_{\mathrm{eff}}=1.09\times10^{-52}\,\mathrm{m}^{-2}
$$

This is the observed target scale. H7 can match it by setting $\rho_{\Lambda,\mathrm{eff}}$ to this value, but that is a fit. It does not explain why bare vacuum terms and counterterms combine to this small result.

### 7.2 Dynamic-Response Parameterization

If H7 claims a residual time-dependent vacuum phase-response, the minimal observational language is an equation of state. The standard CPL form is:

$$
w(a)=w_0+w_a(1-a)
$$

with density evolution:

$$
\frac{\rho_{\mathrm{DE}}(a)}{\rho_{\mathrm{DE}}(1)}=a^{-3(1+w_0+w_a)}\exp(3w_a(a-1))
$$

The constant-response case is $w_0=-1$ and $w_a=0$, which gives:

$$
\rho_{\mathrm{DE}}(a)=\rho_{\mathrm{DE}}(1)
$$

DESI-style $w_0w_a$ parameters can therefore test a claimed H7 residual, but they cannot supply the H7 mechanism. A predictive H7 model must derive $w_0$, $w_a$, or a different $w(a)$ law from the metric-sensitive phase-response functional before comparing to data.

### 7.3 Adversarial Result

The H7 formalization passes a narrow consistency test:

- the constant term can be written as a covariantly conserved effective source
- the fitted value reproduces the observed dark-energy scale
- the optional CPL parameterization gives a standard way to express time-dependent deviations
- the calculation helpers make the target scale and density-ratio formula executable

It fails to reach an explanatory result:

- no mechanism derives $\rho_{\Lambda,\mathrm{eff}}$
- no symmetry or dynamics protects the fitted value against radiative corrections
- no state-dependent or curvature-dependent residual is derived
- no $w(a)$ prediction is produced
- no H6 branch-selection issue is solved by the vacuum formalization

Therefore 08.3 yields a consistent constrained parameterization, but it is non-predictive unless a later theory supplies a residual law. The honest H7 failure mode is naturalness and predictivity, not covariance.

The focused executable checks live in `tests/test_h7_vacuum_phase_response.py` and cover the observed scale conversion, hierarchy-ratio bookkeeping, the CPL density-ratio formula, and invalid inputs.

## 8. Minimum Acceptance Standard For Later H7 Extensions

A later H7 proposal is viable only if it can answer all of the following.

1. What is the exact metric-dependent functional being varied?
2. Which part is bare, which part is counterterm, and which part is renormalized finite response?
3. Does the resulting source obey covariant conservation?
4. Is the source state-dependent, and if so what class of states is allowed?
5. Does it reduce to the accepted H4/05 source-to-metric convention in the smooth low-energy branch-local regime?
6. Does it merely fit $\Lambda_{\mathrm{ren}}$, or does it predict a residual scale or time dependence?
7. If it predicts dynamics, does it give an equation of state compatible with CMB, BAO, SN, lensing, and local constraints?
8. Does it avoid using the reduced H6 branch-decoherence bookkeeping as a solved classical-spacetime emergence theorem?

The final report below applies this classification without hiding the limitation: if no residual parameterization is supplied beyond $\Lambda_{\mathrm{fit}}$, the honest result is a non-predictive constrained reformulation.

## 9. H7 Final Report

### 9.1 Final Label

H7 is a **constrained reformulation accepted with limits**.

The accepted part is narrow:

> Gravity couples to the metric variation of the renormalized effective action. In phase language, that source can be called renormalized metric-sensitive vacuum phase-response.

This is compatible with H4, 05, 05S, H6 warnings, QFT-in-curved-spacetime constraints, and current cosmology when treated as effective-field-theory bookkeeping.

It is not a solution to the cosmological-constant problem. It does not derive $\Lambda$, does not protect the observed value against radiative corrections, and does not produce a new testable deviation.

### 9.2 What H7 Accepts

H7 accepts the following limited claims.

1. A pure absolute bookkeeping phase has no stress-energy response only when it is not a functional of $g_{\mu\nu}$.
2. A uniform covariant vacuum action density coupled through $\sqrt{-g}$ is metric-sensitive and is degenerate with a cosmological-constant term.
3. The conservative gravitational source is the metric variation of a renormalized effective action, not a raw zero-point sum.
4. The fitted constant-response parameterization is covariantly conserved and can match the observed dark-energy scale:

$$
\rho_{\Lambda,\mathrm{eff}}\simeq5.25\times10^{-10}\,\mathrm{J}\,\mathrm{m}^{-3}
$$

$$
\Lambda_{\mathrm{eff}}\simeq1.09\times10^{-52}\,\mathrm{m}^{-2}
$$

5. A time-dependent H7 residual can be tested only after it supplies a real $w(a)$ law or an equivalent observable parameterization.

### 9.3 What H7 Rejects

H7 rejects the following overclaims.

- Absolute uniform vacuum phase has been shown not to gravitate.
- The Pulse Model has derived the observed value of $\Lambda$.
- Renormalization bookkeeping solves the naturalness problem.
- DESI dynamical-dark-energy hints establish an H7 mechanism.
- Casimir-like or Lamb-shift effects decide the gravitational response of the absolute vacuum.
- H6 branch-decoherence bookkeeping solves source selection for vacuum stress-energy.

### 9.4 Dependency Accounting

The final H7 result depends on earlier gates only at their accepted levels.

| Dependency | H7 usage |
|---|---|
| H4 | Supplies the inverse-metric phase-response convention for stress-energy. H7 extends the language to renormalized effective-action variation but does not claim H4 already covered renormalized vacuum stress-energy. |
| 05 | Supplies a conditional smooth low-energy source-to-metric equation with an empirical or fitted $\Lambda$. H7 does not use 05 to derive $\Lambda$. |
| 05S | Strengthens the same low-energy geometry-action bridge only under explicit pulse-network assumptions. H7 does not use 05S as a vacuum-renormalization result. |
| H6 | Supplies warnings about source-to-metric choice, branch selection, energy accounting, and no-signaling. H7 does not use H6 as a solved emergence theorem. |

### 9.5 Verification

The final H7 implementation is supported by:

- `pulse_model/appendix/h7_vacuum_phase_response.md`
- `pulse_model/src/pulse_model/calculations.py`
- `pulse_model/tests/test_h7_vacuum_phase_response.py`

The verification set for the final report is:

```bash
env PYTHONPATH=src .venv/bin/python -m unittest tests.test_h7_vacuum_phase_response
env PYTHONPATH=src .venv/bin/python -m unittest discover -s tests
npm run typecheck
npm run build
```

### 9.6 Downstream Rule

Downstream work may cite H7 only as a constrained renormalized phase-response vocabulary and as a guardrail against vacuum-energy overclaims.

A stronger H7 successor would need at least one of:

- a symmetry or dynamical principle that fixes or protects $\rho_{\Lambda,\mathrm{eff}}$
- a derived state-dependent or curvature-dependent residual stress tensor
- a predicted $w(a)$ law compatible with CMB, BAO, SN, lensing, and local constraints
- an explicit failure showing that phase-response language cannot remain compatible with QFTCS and cosmology

Until such a successor exists, H7 is complete only at the constrained-reformulation level.

## 10. Source Anchors Used For The H7 Report

- Hollands and Wald, ["Quantum fields in curved spacetime"](https://arxiv.org/abs/1401.2026), for local/covariant QFTCS, physically reasonable states, nonlinear observables, stress-energy, and renormalization ambiguities.
- Fewster and Verch, ["Algebraic quantum field theory in curved spacetimes"](https://arxiv.org/abs/1504.00586), for local covariance, relative Cauchy evolution, stress-energy, state-selection limits, and the absence of a locally covariant preferred state.
- Hollands and Wald, ["Conservation of the stress tensor in perturbative interacting quantum field theory in curved spacetimes"](https://arxiv.org/abs/gr-qc/0404074), for stress-energy conservation conditions in curved-spacetime perturbation theory.
- Carroll, ["The Cosmological Constant"](https://arxiv.org/abs/astro-ph/0004075), and Martin, ["Everything You Always Wanted To Know About The Cosmological Constant Problem"](https://arxiv.org/abs/1205.3365), for the standard cosmological-constant and vacuum-energy problem framing.
- Planck Collaboration, ["Planck 2018 results. VI. Cosmological parameters"](https://arxiv.org/abs/1807.06209), for the base-$\Lambda$CDM CMB parameter baseline.
- DESI Collaboration, ["DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints"](https://arxiv.org/abs/2503.14738), and the [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/), for the 2025 BAO and dark-energy constraints.
- DESI Collaboration, ["Extended Dark Energy analysis using DESI DR2 BAO measurements"](https://arxiv.org/abs/2503.14743), for robustness checks around $w_0w_a$ and low-redshift dynamical-dark-energy trends.
- Particle Data Group, ["Dark Energy" review, 2025](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-dark-energy.pdf), for a dated synthesis of DESI, Planck, SN, $H_0$, and structure-growth constraints.
