---
title: 05S5 Spin And Full Connection Holonomy
sidebar_label: 05S5 Spin Connection
sidebar_position: 7
---

# Appendix: 05S5 Spin And Full Connection Holonomy Frontier

**Parent hypothesis:** 05S5, spin and full connection holonomy frontier  
**Status:** 05S5 final verdict: useful bounded torsion/connection diagnostic  
**Purpose:** Decide whether pulse, phase, spin, polarization, gyroscope, or local-frame transport records can honestly access spin/full-connection structure beyond the metric Levi-Civita curvature already bounded by H2 and H3.

---

## 1. Boundary

05S5 starts after the accepted-with-limits H2, H3, H4, Step 5, 05S, 05S2, 05S3, and 05S4 results. It does not restart metric reconstruction, curvature recovery, stress-energy recovery, or the conservative geometry-action comparison.

The frontier question is narrower:

> Does an operational spin, polarization, gyroscope, or internal-state transport record contain connection-sensitive phase or holonomy content that is not already fixed by H3 metric frame holonomy, local Lorentz gauge convention, standard spinor GR, Berry phase, magnetic coupling, or instrument calibration?

05S5 can be useful in several ways:

- recover standard spinor and polarization transport in pulse language without overclaiming novelty
- prove that torsion-free spin holonomy is only a representation lift of H3 frame holonomy
- define bounded residual diagnostics for independent connection, torsion-like, or nonmetricity-like channels
- produce a clean no-go if no honest operational residual survives
- identify the precise source-response map needed before a stronger claim can be made

05S5 explicitly does not yet derive:

- the Einstein-Hilbert action
- Newton's constant $G$
- the cosmological constant $\Lambda$
- metric quantization
- torsion physics
- nonmetricity dynamics
- external deviations from known physics
- a conserved source-response law for independent connection structure

## 2. Accepted Inputs

05S5 may use these inputs only inside their accepted limits.

| Input | Accepted use | Prohibited use |
|---|---|---|
| H2 metric and frame reconstruction | Supply local events, tetrads, areas, volumes, frame metadata, and uncertainty ledgers when H2 conditions hold | Treat tetrad gauge or frame labels as physical structure |
| H3 frame holonomy | Supply corrected local Lorentz frame closure and curvature-ready loop generators | Count a spinor or polarization representation lift as new curvature |
| H4 phase response | Supply conservative matter phase-response and stress-energy identities for standard matter | Treat standard matter response as a new connection law |
| Step 5 and 05S geometry action | Supply the conditional low-energy comparison target and caveat ledger | Define spin/full-connection novelty by copying the target action |
| 05S2 curvature estimator | Supply finite-loop, scalarization, and correction diagnostics | Promote estimator loss to physical spin phase |
| 05S3 correction gate | Keep external phenomenology and fitted coefficients bounded | Introduce new spin or torsion coefficients after seeing constraints |
| 05S4 oriented phase contract | Supply phase-readout, orientation, additivity, and artifact-ledger discipline | Treat a phase readout as geometry without scalarization or response law |
| Synthetic records | Test algebra, signs, gauge covariance, loop reversal, and artifact separation | Claim detection of independent connection physics |

## 3. Prohibited Shortcuts

The following shortcuts fail the 05S5 contract:

- treating tetrad gauge, local Lorentz frame labels, or spin basis choices as physical degrees of freedom
- claiming novelty from the standard Dirac spin connection in curved spacetime
- claiming novelty from the Spin double-cover sign change alone
- treating polarization transport, geodetic precession, frame dragging, or Fermi-Walker transport as new physics when H3 already fixes the metric holonomy
- hiding magnetic, electromagnetic, Berry, material-medium, spin-preparation, detector-axis, or calibration terms in a connection residual
- importing torsion, nonmetricity, Einstein-Cartan, teleparallel, or metric-affine dynamics without a Pulse-specific coefficient or source-response law
- fitting any phase-to-connection coefficient after comparing with observations
- using H7, cosmology, quantum source-response, finite-loop physics, or vacuum residual claims as hidden support
- calling a bounded residual a theory of torsion or full connection before conservation and source-response are supplied

## 4. Spin And Full-Connection Record Fields

An honest 05S5 record must separate observed fields, reconstructed geometry, artifact ledgers, and inferred residuals.

| Field | Meaning | Unit | Status |
|---|---|---:|---|
| $L$ | loop or transport protocol identifier | none | Observed protocol label |
| $p$ | base event or base station | none | Observed or reconstructed |
| $e^{\hat a}{}_\mu$ | tetrad or local orthonormal frame convention | dimensionless | H2/H3 reconstruction plus gauge choice |
| $s_L$ | loop orientation sign | dimensionless | Observed traversal convention |
| $A_L^{\hat a\hat b}$ | oriented local area bivector | $m^2$ | H2/H3 reconstruction |
| $\mathcal{H}_L$ | corrected H3 local Lorentz frame holonomy | dimensionless matrix | H3 data product |
| $\mathcal{K}_L$ | small-loop H3 frame-holonomy generator | dimensionless matrix | H3 data product |
| $\mathcal{U}_{\mathrm{obs}}(L)$ | observed spin, polarization, gyroscope, or internal-state holonomy | dimensionless matrix or phase | Observed |
| $\Phi_{\mathrm{obs}}(L)$ | observed spin-sensitive scalar phase, when a scalar phase channel is used | radians | Observed |
| $\Phi_{\mathrm{prep}}(L)$ | spin preparation and state-selection phase ledger | radians | Artifact ledger |
| $\Phi_{\mathrm{mag}}(L)$ | magnetic and electromagnetic coupling ledger | radians | Known-physics or artifact ledger |
| $\Phi_{\mathrm{Berry}}(L)$ | Berry, material, medium, and basis-transport ledger | radians | Known-physics or artifact ledger |
| $\Phi_{\mathrm{det}}(L)$ | detector-axis, analyzer, and readout convention ledger | radians | Artifact ledger |
| $\Phi_{\mathrm{inst}}(L)$ | instrument drift, electronics, cycle-wrap, and calibration ledger | radians | Artifact ledger |
| $\Phi_{\ell}(L)$ | finite-loop correction ledger | radians | Diagnostic ledger |
| $\mathcal{U}_{\mathrm{LC}}(L)$ | torsion-free metric spin or polarization transport predicted from H3 | dimensionless matrix or phase | Reconstructed baseline |
| $\mathcal{R}_{\mathrm{conn}}(L)$ | residual after subtracting the H3 Levi-Civita baseline and ledgers | dimensionless matrix or phase | Candidate diagnostic |
| $Q_L$ | uncertainty, wrap, gauge, and quality metadata | mixed | Required metadata |

The record-level scalar phase correction, when a scalar spin phase is the measured channel, is:

$$
\phi_{\mathrm{spin}}(L)=\Phi_{\mathrm{obs}}(L)-\Phi_{\mathrm{prep}}(L)-\Phi_{\mathrm{mag}}(L)-\Phi_{\mathrm{Berry}}(L)-\Phi_{\mathrm{det}}(L)-\Phi_{\mathrm{inst}}(L)-\Phi_{\ell}(L)
$$

This is not yet an independent-connection claim. It is only the corrected spin-sensitive phase channel.

For a matrix holonomy channel, the residual must compare observed transport to the torsion-free H3 baseline in the same representation:

$$
\mathcal{R}_{\mathrm{conn}}(L)=\mathcal{U}_{\mathrm{obs}}(L)\mathcal{U}_{\mathrm{LC}}(L)^{-1}
$$

This residual is a candidate diagnostic only after local-frame gauge behavior and all ledgers are stated.

## 5. Gauge And Local Lorentz Requirements

The tetrad satisfies:

$$
g_{\mu\nu}=\eta_{\hat a\hat b}e^{\hat a}{}_\mu e^{\hat b}{}_\nu
$$

A local Lorentz relabeling changes the tetrad by:

$$
e^{\hat a}{}_\mu\mapsto\Lambda^{\hat a}{}_{\hat b}e^{\hat b}{}_\mu
$$

This relabeling is gauge. A valid physical claim must either be invariant under this change or transform by conjugation in a way that leaves eigenphase, trace, norm, or another declared invariant unchanged.

The torsion-free spin connection baseline is the representation connection induced by the H2/H3 metric and tetrad choice. It is not an independent new field in 05S5. For a spinor representation, the connection one-form has the standard schematic form:

$$
\Omega_\mu=\frac{1}{4}\omega_{\mu\hat a\hat b}\gamma^{\hat a}\gamma^{\hat b}
$$

05S5 uses this only as known-physics baseline bookkeeping. A different local frame changes the displayed connection coefficients, but not a closed-loop gauge-invariant holonomy claim.

## 6. Artifact Ledger

05S5 treats a nonzero spin or connection residual as a candidate only after the artifact ledger is exhausted.

| Category | Examples | Allowed status |
|---|---|---|
| Local frame and tetrad convention | Lorentz gauge, tetrad orientation, frame handedness, sign convention | Gauge or convention, not physics |
| Spin preparation | initial spinor phase, polarization state, analyzer axis, state-selection bias | Must be fixed, randomized, or subtracted |
| Spin double cover | $2\pi$ rotation sign, $4\pi$ spinor return, representation branch | Known representation behavior |
| Magnetic and electromagnetic coupling | Zeeman phase, Aharonov-Bohm phase, field gradients, shielding leakage | Known-physics ledger or contamination |
| Berry and material media | adiabatic basis phase, birefringence, fiber or crystal transport, medium anisotropy | Known-physics ledger or contamination |
| Noninertial transport | Fermi-Walker transport, platform rotation, geodetic precession, frame dragging | Known metric or instrument term |
| Instrument and detector | detector-axis drift, readout bias, electronics, calibration, phase wrap | Artifact ledger |
| Finite loop | loop-size correction, unresolved gradients, boundary leakage | Diagnostic or artifact unless invariant |
| External framework | Einstein-Cartan, teleparallel, metric-affine, SME-style coefficient | Known-framework term unless Pulse supplies a source-response law |

## 7. Failure Labels

05S5 uses these failure labels throughout the appendix.

| Label | Meaning |
|---|---|
| `known-spinor-GR-only` | The result is standard spinor or polarization coupling in torsion-free curved spacetime. |
| `representation-lift-only` | The spin or polarization holonomy is only the expected representation of the H3 frame holonomy. |
| `gauge-artifact` | Local Lorentz, tetrad, spin-basis, phase-origin, or cycle-wrap choices change the claimed effect. |
| `frame-convention-artifact` | The effect is caused by frame handedness, sign convention, or detector-axis convention. |
| `spin-preparation-artifact` | The effect is caused by preparation, analyzer, state-selection, or spin basis choices. |
| `Berry-phase-contamination` | Berry, medium, material, or adiabatic basis phases have not been separated. |
| `magnetic-contamination` | Magnetic, electromagnetic, Zeeman, or Aharonov-Bohm phases have not been separated. |
| `torsion-unsupported` | The record does not contain an observable requiring torsion-like structure. |
| `nonmetricity-unsupported` | The record does not contain an observable requiring nonmetricity-like structure. |
| `coefficient-smuggling` | A new coefficient is fitted or chosen after comparison instead of fixed beforehand. |
| `conservation-failure` | The proposed response violates required local Lorentz or diffeomorphism identities. |
| `source-response-missing` | A residual is bounded, but no conserved source-response map is supplied. |
| `known-framework-equivalent` | The result is a standard external torsion, nonmetricity, or spin-coupling framework in new notation. |
| `scope-violation` | The claim uses unsupported H7, cosmology, quantum source-response, finite-loop, or external-deviation assumptions. |

## 8. Verdict Labels

05S5 must end with exactly one primary verdict label.

### Novel Connection-Phase Response

This label requires all of the following:

- an operational spin, polarization, gyroscope, or internal-state transport record exists before any action comparison
- the residual is not fixed by H3 metric Levi-Civita holonomy or its spin/polarization representation lift
- local Lorentz gauge, Spin double-cover sign, spin preparation, Berry, magnetic, detector, finite-loop, and instrument explanations are bounded
- the effect has a predeclared coefficient or normalization rule
- the effect has a conserved source-response map or a falsifiable response law
- the effect produces a comparison-ready observable without fitting after the fact

### Useful Conservative Spin-Connection Recovery

This label applies when 05S5 cleanly recovers standard spinor, polarization, or gyroscope transport from the accepted H2/H3/H4 inputs, and shows that no new independent connection content is established.

### Useful Bounded Torsion/Connection Diagnostic

This label applies when 05S5 defines executable or operational residual checks that bound independent connection, torsion-like, or nonmetricity-like channels, but the Pulse Model still lacks a source-response law or fixed coefficient.

### Blocked Conditional Bridge

This label applies when a stronger connection-phase bridge remains possible only after assuming a missing physical readout, gauge-invariant residual, source-response map, conservation identity, coefficient rule, or external constraint mapping.

### Clean No-Go

This label applies when every candidate collapses to known spinor GR, representation lift, gauge artifact, frame convention, spin preparation, Berry or magnetic contamination, known external framework, or scope violation.

## 9. Ordered 05S5 Task Sequence

The 05S5 tasks must be completed in order:

1. Define spin/full-connection contract and novelty bar.
2. Define tetrad, spin-connection, and operational record schema.
3. Recover standard spinor phase-response and conservation limits.
4. Derive spin holonomy from H3 frame holonomy and identify independent content.
5. Define independent connection, torsion, and nonmetricity diagnostics or no-go.
6. Implement focused spin-connection holonomy helpers and tests.
7. Benchmark spin/full-connection diagnostics against known physics and constraints.
8. Run adversarial novelty and artifact review.
9. Write final spin/full-connection verdict and update roadmap.

Each task may downgrade the path. Later tasks must not strengthen the claim unless all earlier gates remain satisfied.

## 10. 05S5.2 Tetrad And Operational Record Schema

05S5.2 turns the contract into a concrete record schema. The schema has three layers:

| Layer | Examples | Allowed use |
|---|---|---|
| Observed | spin analyzer outcomes, polarization angle, gyroscope axis, interferometer phase, local field monitor, detector timestamp | Define the operational transport or phase readout |
| Reconstructed | H2 tetrad, H3 Lorentz holonomy, loop area bivector, torsion-free Levi-Civita spin lift | Build the standard metric baseline with stated gauge conventions |
| Inferred | residual connection holonomy, torsion-like residual, nonmetricity-like residual, coefficient map | Candidate diagnostic only after ledgers and gauge behavior pass |

No inferred quantity may be fed back into the observed or reconstructed layer as if it were directly measured.

### 10.1 Local Frame Variables

The local tetrad $e^{\hat a}{}_\mu$ and inverse tetrad $e_{\hat a}{}^\mu$ satisfy:

$$
e^{\hat a}{}_\mu e_{\hat b}{}^\mu=\delta^{\hat a}{}_{\hat b}
$$

$$
e^{\hat a}{}_\mu e_{\hat a}{}^\nu=\delta_\mu{}^\nu
$$

$$
g_{\mu\nu}=\eta_{\hat a\hat b}e^{\hat a}{}_\mu e^{\hat b}{}_\nu
$$

The local metric is:

$$
\eta_{\hat a\hat b}=\mathrm{diag}(-1,1,1,1)
$$

The tetrad is not unique. A local Lorentz transformation $\Lambda^{\hat a}{}_{\hat b}(p)$ gives an equally valid tetrad at the same event. Therefore record fields must state:

- the local frame convention used for reporting components
- whether the frame is reconstructed by H2, transported by H3, attached to an instrument, or synthetic
- the orientation and time-orientation convention
- the uncertainty or calibration metadata for the frame

A component such as $A_L^{\hat a\hat b}$ is a reported local-frame component of an oriented area bivector. The physical loop area is not the coordinate component alone; it is the area plus the frame convention and uncertainty ledger.

### 10.2 Torsion-Free Spin Connection Baseline

The baseline spin connection is the torsion-free metric-compatible connection induced by the H2 metric and the chosen tetrad. It is defined by tetrad compatibility:

$$
\nabla_\mu e^{\hat a}{}_\nu=\partial_\mu e^{\hat a}{}_\nu-\Gamma^\rho{}_{\nu\mu}e^{\hat a}{}_\rho+\omega_\mu{}^{\hat a}{}_{\hat b}e^{\hat b}{}_\nu=0
$$

Metric compatibility gives antisymmetry in the local Lorentz indices:

$$
\omega_{\mu\hat a\hat b}=-\omega_{\mu\hat b\hat a}
$$

The torsion-free Cartan condition is:

$$
T^{\hat a}=de^{\hat a}+\omega^{\hat a}{}_{\hat b}\wedge e^{\hat b}=0
$$

This baseline is known-physics recovery. It is not a new Pulse field. A record that matches this baseline receives `known-spinor-GR-only` or `representation-lift-only`, depending on the channel.

### 10.3 Possible Independent Connection Components

05S5 may name independent connection components only as diagnostics until a source-response law exists. The general local connection can be decomposed schematically as:

$$
\widetilde{\omega}^{\hat a}{}_{\hat b}=\omega^{\hat a}{}_{\hat b}+C^{\hat a}{}_{\hat b}
$$

Here $\omega^{\hat a}{}_{\hat b}$ is the torsion-free H3 baseline and $C^{\hat a}{}_{\hat b}$ is a candidate residual connection one-form. The residual may be classified by what it would change:

| Candidate | Diagnostic content | Required before physics claim |
|---|---|---|
| Lorentz-connection residual | extra antisymmetric local-frame transport beyond H3 Levi-Civita holonomy | gauge-covariant observable and conserved source-response map |
| Torsion-like residual | nonzero closure of $de^{\hat a}+\widetilde{\omega}^{\hat a}{}_{\hat b}\wedge e^{\hat b}$ | operational translation or spin-response record not fixed by H3 |
| Nonmetricity-like residual | local length, angle, or metric compatibility failure under transport | metric-comparison record and calibration proof |
| Coefficient residual | scalar or matrix coefficient multiplying a retained channel | coefficient fixed before observational comparison |

If the record cannot distinguish $C^{\hat a}{}_{\hat b}$ from gauge, preparation, Berry, magnetic, detector, or finite-loop terms, the channel is unsupported.

### 10.4 Spin, Polarization, And Gyroscope Transport Observables

The accepted operational readouts are:

| Readout | Observed record | Baseline comparison | Common failure mode |
|---|---|---|---|
| Spinor interferometer | relative spin-sensitive output phase or population | Spin lift of H3 Lorentz holonomy plus magnetic and Berry ledgers | `magnetic-contamination` or `Berry-phase-contamination` |
| Polarization loop | analyzer angle, Stokes vector, or Jones vector after a closed path | vector or spin-1 representation of H3 frame holonomy plus medium ledger | `known-spinor-GR-only` or material contamination |
| Gyroscope loop | local axis orientation after transport | Fermi-Walker or Levi-Civita transport from H3 and acceleration ledgers | known geodetic or frame-dragging recovery |
| Internal-state Ramsey loop | closed-loop phase difference between prepared internal states | standard matter Hamiltonian plus H4 phase-response and field ledgers | spin-preparation or magnetic artifact |
| Synthetic holonomy | declared matrix in a chosen representation | algebraic baseline for tests only | no physical detection |

For a representation $R$, the Wilson-loop-style transport is:

$$
\mathcal{U}_R(L)=\mathcal{P}\exp\left(-\oint_L \Gamma_R\right)
$$

The path-ordering symbol and connection representation are bookkeeping. A physical claim requires a record of the preparation, path, readout, baseline, and artifact ledgers.

### 10.5 Spin Versus Lorentz Representation Behavior

The H3 frame holonomy lives in the local Lorentz representation. Spinor transport uses a lift into the Spin representation. Locally this lift has the same Lie algebra data, but the global representation is double covered.

For a spatial rotation angle $\theta$ about a declared axis, a spin-half phase convention has the schematic eigenphase:

$$
\phi_{\mathrm{spin}}=\frac{1}{2}\theta
$$

The same $2\pi$ Lorentz-frame rotation can map a spinor amplitude to its negative:

$$
|\psi\rangle\mapsto-|\psi\rangle
$$

This sign is known representation behavior. It is not a new connection effect unless the protocol observes an interference phase relative to a reference arm and all preparation, analyzer, magnetic, Berry, and detector ledgers are controlled. A density-matrix or intensity-only readout may be insensitive to the sign.

### 10.6 Phase-Wrap And Branch Conventions

Scalar spin-sensitive phase records must state a principal interval and unwrap integer:

$$
\Phi_{\mathrm{obs}}=\Phi_{\mathrm{principal}}+2\pi n_L
$$

where $n_L$ is an integer fixed by the protocol or uncertainty model before comparison. Spinor double-cover branches must additionally state whether the comparison is modulo $2\pi$ in observed interferometer phase or modulo $4\pi$ in spinor-amplitude return.

A residual that changes when the branch convention changes is labeled `gauge-artifact` unless the branch is fixed by an independent observed interference record.

### 10.7 Artifact Ledger Required By The Record Schema

Every 05S5 operational record must carry, bound, or explicitly mark missing these ledgers:

| Ledger | Required fields | Failure label if not controlled |
|---|---|---|
| Frame convention | tetrad gauge, handedness, time orientation, detector-axis convention | `frame-convention-artifact` |
| Spin preparation | prepared state, analyzer basis, reference arm, state-selection rule | `spin-preparation-artifact` |
| Magnetic and electromagnetic | local field monitor, shielding state, charge or magnetic moment, modeled phase | `magnetic-contamination` |
| Berry and medium | basis path, adiabaticity condition, medium response, material anisotropy | `Berry-phase-contamination` |
| Instrument drift | phase zero, electronics, detector alignment, timestamping, calibration drift | `gauge-artifact` or `frame-convention-artifact` |
| Finite loop | loop scale, boundary leakage, unresolved gradients, refinement behavior | `torsion-unsupported` or `source-response-missing` |

### 10.8 Minimal Record Acceptance Gate

A record is accepted for 05S5 analysis only if:

- the observed spin, polarization, gyroscope, or internal-state readout is recorded before fitting any geometry residual
- the H2/H3 reconstructed baseline is listed separately from the observed readout
- the representation and double-cover convention are stated
- phase-wrap and branch conventions are explicit
- every artifact ledger is subtracted, bounded, or marked missing
- any residual is classified as inferred and not treated as a source-response law

If any item fails, the record may still be useful for calibration or known-physics recovery, but it cannot support a connection-novelty claim.

## 11. 05S5.3 Standard Spinor Phase-Response And Conservation Limits

05S5.3 adds the conservative spinor matter side. The goal is not novelty. The goal is to state exactly what standard spinor phase-response already supplies before 05S5 asks for independent connection physics.

### 11.1 Accepted Spinor Baseline

The accepted baseline is a minimally coupled Dirac field on a smooth tetrad background with the torsion-free spin connection from Section 10.2. The flat local gamma matrices satisfy:

$$
\gamma^{\hat a}\gamma^{\hat b}+\gamma^{\hat b}\gamma^{\hat a}=2\eta^{\hat a\hat b}I
$$

The curved gamma matrices are:

$$
\gamma^\mu=e_{\hat a}{}^\mu\gamma^{\hat a}
$$

The spinor covariant derivative is:

$$
D_\mu\psi=\partial_\mu\psi+\Omega_\mu\psi
$$

For the adjoint spinor:

$$
D_\mu\bar{\psi}=\partial_\mu\bar{\psi}-\bar{\psi}\Omega_\mu
$$

The minimally coupled Hermitian Dirac action can be written as:

$$
S_D=\int d^4x\,e\left[\frac{i\hbar c}{2}\left(\bar{\psi}\gamma^\mu D_\mu\psi-(D_\mu\bar{\psi})\gamma^\mu\psi\right)-mc^2\bar{\psi}\psi\right]
$$

Here:

$$
e=\sqrt{-g}
$$

The matter phase is:

$$
\Theta_D=\frac{S_D}{\hbar}
$$

This is standard Dirac-in-curved-spacetime physics. In 05S5 it receives the label `known-spinor-GR-only` unless a later residual survives the independent-connection gates.

### 11.2 Spin Connection Phase-Response

Treating the tetrad and spin connection as independent variables for response bookkeeping gives the first-order variation:

$$
\delta S_D=\int d^4x\,e\,\tau^\mu{}_{\hat a}\delta e^{\hat a}{}_\mu+\frac{1}{2}\int d^4x\,e\,s^\mu{}_{\hat a\hat b}\delta\omega_\mu{}^{\hat a\hat b}
$$

Equivalently:

$$
\delta\Theta_D=\frac{1}{\hbar}\int d^4x\,e\,\tau^\mu{}_{\hat a}\delta e^{\hat a}{}_\mu+\frac{1}{2\hbar}\int d^4x\,e\,s^\mu{}_{\hat a\hat b}\delta\omega_\mu{}^{\hat a\hat b}
$$

The coefficients $\tau^\mu{}_{\hat a}$ and $s^\mu{}_{\hat a\hat b}$ are the tetrad-response and spin-connection-response densities in this convention. The spin-current density is antisymmetric:

$$
s^\mu{}_{\hat a\hat b}=-s^\mu{}_{\hat b\hat a}
$$

For a minimally coupled Dirac field, the spin-current coefficient is the standard local Lorentz generator response. A common convention gives it proportional to the axial spin density, but 05S5 does not need that component formula for the gate. What matters here is the response structure:

- metric or tetrad variation supplies the stress-energy side already bounded by H4
- spin-connection variation supplies the spin-current side in first-order bookkeeping
- in torsion-free GR, $\omega_\mu{}^{\hat a\hat b}$ is not independent after imposing the Levi-Civita constraint
- a nonzero spin current alone does not prove torsion or independent connection dynamics

If a later task proposes an independent connection response, it must state whether $\delta\omega$ is an independent variation, a constrained variation induced by $\delta e$, or a residual diagnostic field.

### 11.3 Local Lorentz Identity

Local Lorentz invariance links the antisymmetric tetrad response and spin-current divergence. Under an infinitesimal local Lorentz rotation $\lambda_{\hat a\hat b}$ with:

$$
\lambda_{\hat a\hat b}=-\lambda_{\hat b\hat a}
$$

the tetrad and connection variations have the schematic form:

$$
\delta e^{\hat a}{}_\mu=\lambda^{\hat a}{}_{\hat b}e^{\hat b}{}_\mu
$$

$$
\delta\omega_\mu{}^{\hat a\hat b}=-D_\mu\lambda^{\hat a\hat b}
$$

On shell and after discarding the boundary term, invariance implies the response identity:

$$
\tau_{[\hat a\hat b]}+\frac{1}{2}D_\mu s^\mu{}_{\hat a\hat b}=0
$$

The factor depends on the chosen normalization of $s^\mu{}_{\hat a\hat b}$. The required content is invariant: local Lorentz symmetry does not allow an arbitrary antisymmetric stress response unrelated to spin current. A proposed connection residual that violates this identity is labeled `conservation-failure`.

### 11.4 Diffeomorphism Identity

Diffeomorphism invariance supplies the matter conservation condition. In torsion-free minimally coupled GR, the symmetric stress-energy tensor obeys the on-shell identity:

$$
\nabla_\mu T^{\mu\nu}=0
$$

In first-order tetrad bookkeeping with spin current, the conservation law can be written with additional spin-connection response terms before imposing the torsion-free constraint. 05S5 treats those terms as formal bookkeeping unless the task explicitly supplies an independent connection field and its source-response law.

The practical gate is:

- torsion-free baseline: stress-energy conservation reduces to the H4 matter-side identity
- independent connection proposal: the proposed stress, spin current, and connection response must obey compatible local Lorentz and diffeomorphism identities
- diagnostic residual: if the residual is measured but no conserved source-response law is supplied, label it `source-response-missing`

### 11.5 Accepted, Formal, And Unsupported Formulas

The status of spinor formulas in 05S5 is:

| Formula or claim | 05S5 status |
|---|---|
| Curved gamma matrices from the H2 tetrad | Accepted baseline |
| Torsion-free spin connection induced by H2/H3 metric data | Accepted baseline |
| Hermitian minimally coupled Dirac action | Accepted standard spinor recovery |
| Tetrad phase-response coefficient | Accepted as conservative H4 extension in tetrad variables |
| Spin-current response to independent $\delta\omega$ | Accepted as first-order response bookkeeping |
| Full symbolic proof of the Dirac stress-energy tensor in all conventions | Formal target, not completed here |
| Einstein-Cartan torsion sourced by spin current | Known-framework-equivalent unless Pulse supplies its own source-response coefficient |
| Any external spin-gravity anomaly | Unsupported until an operational residual and coefficient map are fixed |

### 11.6 05S5.3 Gate Decision

05S5.3 passes only as conservative known-physics recovery:

- standard spinor matter has a phase-response formulation in tetrad and spin-connection variables
- spin current is the response to spin-connection variation in first-order bookkeeping
- local Lorentz invariance and diffeomorphism invariance constrain the response coefficients
- torsion-free GR removes the independent spin connection as a new field
- no Pulse-specific connection dynamics, torsion law, nonmetricity law, or source-response coefficient has been derived

The resulting label for this task is `known-spinor-GR-only` unless later tasks isolate a residual not already fixed by the standard baseline.

## 12. 05S5.4 Spin Holonomy As H3 Frame-Holonomy Lift

05S5.4 connects operational spin or polarization transport to the accepted H3 frame-holonomy observable. The result is restrictive: in the torsion-free metric-compatible case, spin holonomy is a representation lift of the same local Lorentz holonomy already measured by H3.

### 12.1 H3 Small-Loop Input

H3 supplies the corrected local Lorentz frame holonomy:

$$
\mathcal{H}_L=\Lambda_{m-1,0}\Lambda_{m-2,m-1}\cdots\Lambda_{0,1}
$$

For a small loop based at $p$, its generator is:

$$
\mathcal{K}_L=\log\mathcal{H}_L
$$

In a local orthonormal frame:

$$
\mathcal{K}_L{}^{\hat a}{}_{\hat b}=R^{\hat a}{}_{\hat b\hat c\hat d}A_L^{\hat c\hat d}+O(\ell^3)
$$

Reversing the loop orientation sends:

$$
A_L^{\hat c\hat d}\mapsto-A_L^{\hat c\hat d}
$$

and therefore:

$$
\mathcal{K}_L\mapsto-\mathcal{K}_L+O(\ell^3)
$$

For the exact reversed path, the holonomy is inverted:

$$
\mathcal{H}_{L^{-1}}=\mathcal{H}_L^{-1}
$$

### 12.2 Spinor Representation Lift

In the Dirac spinor representation, the torsion-free spin connection induces a spin holonomy:

$$
\mathcal{U}_{1/2,\mathrm{LC}}(L)=\mathcal{P}\exp\left(-\oint_L\Omega_\mu dx^\mu\right)
$$

Using the convention from Section 5:

$$
\Omega_\mu=\frac{1}{4}\omega_{\mu\hat a\hat b}\gamma^{\hat a}\gamma^{\hat b}
$$

For a small loop, the spin-holonomy generator is the same H3 generator represented on spinors:

$$
\log\mathcal{U}_{1/2,\mathrm{LC}}(L)=-\frac{1}{4}\mathcal{K}_{L\hat a\hat b}\gamma^{\hat a}\gamma^{\hat b}+O(\ell^3)
$$

The overall sign follows the edge-transport convention. Changing that convention changes both the H3 baseline and the spin lift. It does not create independent physics.

The same logic applies to any finite-dimensional representation $R$:

$$
\mathcal{U}_{R,\mathrm{LC}}(L)=R(\mathcal{H}_L)
$$

up to the declared representation convention and branch choice.

### 12.3 Gauge Covariance

Under a local Lorentz relabeling at the base event:

$$
\mathcal{H}_L\mapsto\Lambda(p)\mathcal{H}_L\Lambda(p)^{-1}
$$

The spin lift transforms by conjugation:

$$
\mathcal{U}_{1/2,\mathrm{LC}}(L)\mapsto S(p)\mathcal{U}_{1/2,\mathrm{LC}}(L)S(p)^{-1}
$$

where $S(p)$ is a Spin lift of $\Lambda(p)$. Therefore only conjugation-invariant quantities, or explicitly covariant comparisons in the same transported basis, can be used as physical observables.

Acceptable invariant summaries include:

- eigenphases after the branch convention is fixed
- trace or normalized trace in a declared representation
- generator norm in a declared local-frame metric
- comparison of observed and predicted holonomies after both are expressed in the same base frame

A raw component of $\mathcal{U}_{1/2}$ in an arbitrary spin basis is not a physical residual.

### 12.4 Double-Cover Branch

The Lorentz holonomy may have two Spin lifts:

$$
S(\mathcal{H}_L)
$$

and:

$$
-S(\mathcal{H}_L)
$$

For infinitesimal loops connected continuously to the identity, 05S5 uses the identity-connected lift. For larger loops or protocols containing a $2\pi$ rotation, the observed interference reference must state the branch. Otherwise a sign mismatch is classified as `gauge-artifact` or `frame-convention-artifact`.

The double-cover sign can be physically visible in an interferometer, but it is standard spinor representation behavior. By itself it receives `representation-lift-only`.

### 12.5 Restricted Theorem

Under the following assumptions:

- H2 supplies a smooth metric and local tetrad in the accepted domain
- H3 supplies corrected local Lorentz frame holonomy $\mathcal{H}_L$
- the connection is torsion-free and metric-compatible
- the spin, polarization, or gyroscope channel is minimally coupled to that connection
- preparation, magnetic, Berry, detector, finite-loop, and instrument ledgers are controlled
- the representation and branch convention are fixed before comparison

then the predicted spin or polarization holonomy is completely fixed by $\mathcal{H}_L$ through the chosen representation:

$$
\mathcal{U}_{R,\mathrm{LC}}(L)=R(\mathcal{H}_L)
$$

Consequently, matching the predicted holonomy is useful known-physics recovery, not independent connection evidence. The accepted label for this standard case is `representation-lift-only`, with `known-spinor-GR-only` for the underlying spinor matter coupling.

### 12.6 Independent Content Residual

The only residual that can pass beyond the representation-lift theorem is:

$$
\mathcal{R}_{R,\mathrm{conn}}(L)=\mathcal{U}_{R,\mathrm{obs}}(L)R(\mathcal{H}_L)^{-1}\mathcal{U}_{R,\mathrm{art}}(L)^{-1}
$$

Here $\mathcal{U}_{R,\mathrm{art}}(L)$ is the ordered product of preparation, magnetic, Berry, detector, finite-loop, and instrument correction transports in the same representation. This convention treats the artifact correction as left-applied before the Levi-Civita representation lift, so an artifact-explained record has $\mathcal{U}_{R,\mathrm{obs}}(L)=\mathcal{U}_{R,\mathrm{art}}(L)R(\mathcal{H}_L)$. The order matters when artifact and baseline holonomies do not commute. If the correction is scalar-phase-only, this equation is replaced by the scalar phase ledger from Section 4.

For a residual close to identity:

$$
\Delta\mathcal{K}_{R,\mathrm{conn}}(L)=\log\mathcal{R}_{R,\mathrm{conn}}(L)
$$

This residual is only a candidate diagnostic. It becomes independent connection evidence only if it is:

- not removable by local Lorentz gauge or branch convention
- not explained by H3 frame holonomy in another representation
- not explained by spin preparation, magnetic, Berry, detector, finite-loop, or instrument ledgers
- additive or composition-safe under independent loops
- tied to a conserved source-response map or a predeclared falsifiable coefficient rule

Without the last item, the correct label is `source-response-missing`, not novelty.

### 12.7 05S5.4 Gate Decision

05S5.4 establishes a reduction result:

- torsion-free spin, polarization, and gyroscope holonomy are fixed by H3 frame holonomy plus representation choice
- loop reversal inverts the holonomy and flips the small-loop generator
- local Lorentz gauge changes the displayed matrices by conjugation, not by physical content
- Spin double-cover signs are standard representation behavior
- independent content requires a residual against $R(\mathcal{H}_L)$ after all artifact ledgers are applied

The standard channel is therefore `representation-lift-only`. A nonzero residual remains a bounded diagnostic until 05S5.5 decides whether torsion, nonmetricity, or independent connection labels are supported.

## 13. 05S5.5 Independent Connection, Torsion, And Nonmetricity Diagnostics

05S5.5 asks whether any residual from Section 12 can honestly be interpreted as independent connection structure. The answer is strict: 05S5 may define bounded diagnostics, but it does not derive torsion physics, nonmetricity physics, or a source-response law.

### 13.1 Diagnostic Taxonomy

| Channel | Operational record | Tensor or representation content | Dimension | Default label |
|---|---|---|---:|---|
| Lorentz-connection residual | spin, polarization, or frame holonomy after H3 baseline and ledgers | adjoint local Lorentz generator or representation generator | dimensionless, or $m^{-2}$ after area division | `source-response-missing` |
| Torsion-like closure residual | translational endpoint, Burgers-vector, or loop-closure displacement not fixed by H2/H3 | local vector-valued two-form density | $m$, or $m^{-1}$ after area division | `torsion-unsupported` |
| Nonmetricity-like drift residual | length, angle, clock-rate, or inner-product drift under transport | symmetric local-frame metric-compatibility residual | dimensionless, or $m^{-1}$ by path length | `nonmetricity-unsupported` |

The diagnostics are intentionally not interchangeable. A spinor phase residual is not automatically torsion. A length drift is not automatically Lorentz curvature. A tetrad gauge change is not either.

### 13.2 Lorentz-Connection Residual

The retained Lorentz-connection diagnostic is the residual holonomy already defined in Section 12:

$$
\mathcal{R}_{R,\mathrm{conn}}(L)=\mathcal{U}_{R,\mathrm{obs}}(L)R(\mathcal{H}_L)^{-1}\mathcal{U}_{R,\mathrm{art}}(L)^{-1}
$$

Near identity:

$$
\Delta\mathcal{K}_{R,\mathrm{conn}}(L)=\log\mathcal{R}_{R,\mathrm{conn}}(L)
$$

If the representation map can be inverted on the measured subspace, this may be reported as a local Lorentz generator:

$$
\Delta K_{\mathrm{conn}}{}^{\hat a}{}_{\hat b}(L)
$$

The area-normalized diagnostic is:

$$
\Delta B_{\mathrm{conn}}{}^{\hat a}{}_{\hat b}(L)=\frac{\Delta K_{\mathrm{conn}}{}^{\hat a}{}_{\hat b}(L)}{A_L}
$$

where $A_L$ is the positive local loop area attached to the measured two-plane. The units of $\Delta B_{\mathrm{conn}}$ are $m^{-2}$.

This channel is retained only as a bounded diagnostic. It vanishes when:

- the observed holonomy equals the H3 Levi-Civita representation lift after ledgers
- the residual changes by gauge convention or branch choice
- the residual is explained by magnetic, Berry, detector, finite-loop, or instrument terms
- the residual appears only in an unobservable spinor-basis component

It can become novelty only if a later theory supplies a conserved source-response map, such as a predeclared relation between spin current and $\Delta B_{\mathrm{conn}}$. 05S5 does not supply that map.

### 13.3 Torsion-Like Residual

Torsion is not a spin phase by definition. Operationally, 05S5 requires a translational closure record. A candidate loop displacement residual has the form:

$$
b_L^{\hat a}=\Delta x_{\mathrm{obs}}^{\hat a}(L)-\Delta x_{\mathrm{LC}}^{\hat a}(L)-\Delta x_{\mathrm{art}}^{\hat a}(L)
$$

For a small loop, a torsion-like density would scale as:

$$
b_L^{\hat a}=T^{\hat a}{}_{\hat b\hat c}A_L^{\hat b\hat c}+O(\ell^3)
$$

The vector $b_L^{\hat a}$ has units of length. The density $T^{\hat a}{}_{\hat b\hat c}$ has units $m^{-1}$.

This channel requires a record that independently compares endpoint closure, lattice-like Burgers vector, pulse-marker translation, or equivalent displacement data. H3 frame rotation is not enough. H2 coordinate reconstruction is not enough if it already assumes a smooth torsion-free event manifold.

05S5 therefore gives torsion the default label `torsion-unsupported`. It may be upgraded only to a bounded diagnostic if all of the following are present:

- an operational translational closure record independent of pure frame rotation
- a loop-area and orientation convention from H2/H3
- an artifact ledger for actuator, station motion, signal path, platform acceleration, and finite-loop effects
- gauge-covariant reporting of $b_L^{\hat a}$ in the base local frame
- evidence that the residual cannot be removed by event-identification or frame-convention choices

Even then, novelty still requires a source-response law and coefficient rule.

### 13.4 Nonmetricity-Like Residual

Nonmetricity requires failure of metric compatibility, not merely spin precession. A candidate record must compare length, angle, clock-rate, or inner-product preservation under a closed transport protocol.

For a transported local vector $v^{\hat a}$, define the observed norm drift:

$$
\Delta q_L(v)=\eta_{\hat a\hat b}v_{\mathrm{out}}^{\hat a}v_{\mathrm{out}}^{\hat b}-\eta_{\hat a\hat b}v_{\mathrm{in}}^{\hat a}v_{\mathrm{in}}^{\hat b}-\Delta q_{\mathrm{art}}(v)
$$

For two transported vectors $u^{\hat a}$ and $v^{\hat a}$, define the inner-product drift:

$$
\Delta q_L(u,v)=\eta_{\hat a\hat b}u_{\mathrm{out}}^{\hat a}v_{\mathrm{out}}^{\hat b}-\eta_{\hat a\hat b}u_{\mathrm{in}}^{\hat a}v_{\mathrm{in}}^{\hat b}-\Delta q_{\mathrm{art}}(u,v)
$$

The nonmetricity one-form would be:

$$
Q_{\mu\hat a\hat b}=-D_\mu\eta_{\hat a\hat b}
$$

In the Levi-Civita baseline:

$$
Q_{\mu\hat a\hat b}=0
$$

05S5 gives this channel the default label `nonmetricity-unsupported`. It may be retained as a bounded diagnostic only if an independent length, angle, frequency-ratio, or inner-product transport record survives detector-scale, clock-calibration, medium, and frame-convention ledgers.

### 13.5 Source-Response Requirements

A residual is not a theory. To become a Pulse-specific connection response, a retained channel must supply:

| Requirement | Meaning | Failure label |
|---|---|---|
| Source variable | a stress, spin-current, hypermomentum-like, or pulse-record source stated before comparison | `source-response-missing` |
| Coefficient rule | a fixed coefficient, normalization, or scaling law not fitted after seeing bounds | `coefficient-smuggling` |
| Conservation identity | compatibility with local Lorentz and diffeomorphism response identities | `conservation-failure` |
| Gauge behavior | invariant or covariant residual under local Lorentz and branch changes | `gauge-artifact` |
| Artifact closure | magnetic, Berry, detector, finite-loop, and instrument ledgers bounded | contamination or artifact labels |
| Known-framework comparison | statement of equivalence or difference from Einstein-Cartan, teleparallel, metric-affine, or SME-style models | `known-framework-equivalent` |

Spin current is the natural source candidate for a Lorentz-connection or torsion-like response, but 05S5.3 only recovered standard first-order response bookkeeping. It did not derive a Pulse-specific equation connecting spin current to residual connection holonomy.

### 13.6 Conditions For Vanishing

All independent-connection diagnostics vanish in the conservative baseline when:

$$
\mathcal{U}_{R,\mathrm{obs}}(L)=\mathcal{U}_{R,\mathrm{art}}(L)R(\mathcal{H}_L)
$$

$$
b_L^{\hat a}=0
$$

$$
\Delta q_L(u,v)=0
$$

These are the expected results for torsion-free, metric-compatible, artifact-controlled known physics.

### 13.7 05S5.5 Gate Decision

05S5.5 retains only one executable-ready diagnostic class:

- **Lorentz-connection holonomy residual:** retained as a bounded diagnostic with label `source-response-missing`.

The other channels remain unsupported unless future records supply new operational data:

- **Torsion-like residual:** `torsion-unsupported` without a translational closure record independent of H3 frame rotation.
- **Nonmetricity-like residual:** `nonmetricity-unsupported` without an independent length, angle, or inner-product drift record.

No channel receives the `novel connection-phase response` label in 05S5.5. The best possible downstream status after this gate is a useful bounded torsion/connection diagnostic, unless later tasks add evidence that was not available here.

## 14. 05S5.6 Executable Spin-Connection Holonomy Helpers

05S5.6 adds a focused executable layer in `src/pulse_model/spin_connection_holonomy.py` with tests in `tests/test_spin_connection_holonomy.py`.

The code implements only the channels justified by Sections 12 and 13:

| Helper area | What is checked | 05S5 status |
|---|---|---|
| Spatial H3 generator lift | maps a spatial H3 frame-holonomy generator into a spin-half holonomy | useful conservative recovery |
| Identity and flat holonomy | zero H3 generator maps to identity spin holonomy | `representation-lift-only` |
| Loop reversal | reversed loop uses inverse spin holonomy | useful sign and orientation check |
| Local-frame relabeling | observed and baseline holonomies transform by conjugation with invariant residual norm | gauge-covariant diagnostic |
| Spin double cover | $2\pi$ rotation gives spinor sign change and $4\pi$ returns to identity | known representation behavior |
| Scalar spin phase record | subtracts preparation, magnetic, Berry, detector, instrument, and finite-loop ledgers | artifact filter |
| Matrix holonomy residual | computes residual against the H3 spin lift and artifact holonomy | bounded connection diagnostic |
| Input validation | rejects nonfinite phases, invalid branches, unsupported boost generators, non-antisymmetric generators, singular matrices, and invalid areas | guardrail |

The retained executable residuals classify as:

| Condition | Code classification | Appendix label |
|---|---|---|
| observed holonomy or phase equals the H3 representation lift after ledgers | `representation-lift-only` | useful conservative recovery |
| nonzero residual with no source-response law | `source-response-missing` | useful bounded diagnostic only |
| nonzero residual with a supplied source-response flag | `bounded-connection-diagnostic` | diagnostic, not accepted novelty by itself |

The executable layer deliberately does not implement:

- boost-sector spin holonomy
- full Dirac equation evolution
- Einstein-Cartan dynamics
- torsion solving
- nonmetricity solving
- metric-affine field equations
- external-constraint fitting

Those omissions are part of the 05S5.5 gate decision. Torsion-like diagnostics need translational closure records before code would be honest. Nonmetricity-like diagnostics need independent length, angle, or inner-product drift records before code would be honest. Neither record type is present in 05S5.

### 14.1 Verification For 05S5.6

Focused verification:

```bash
uv run python -m unittest tests.test_spin_connection_holonomy
```

Expected result:

```text
Ran 9 tests
OK
```

The full suite remains a final epic-level check after downstream benchmark and verdict sections are complete.

## 15. 05S5.7 Benchmark And Constraint Matrix

05S5.7 benchmarks the retained spin/full-connection diagnostics against known physics and external constraint families. The central rule is conservative:

> External bounds are not imported as Pulse bounds unless 05S5 supplies a parameter map from the measured residual to the external coefficient.

05S5 currently lacks that map. Therefore external constraint values below are dated context, not fitted limits on the Pulse Model.

### 15.1 Sources Checked

Sources checked on 2026-06-08:

- Gravity Probe B final results: Everitt et al., 2011, arXiv:1105.3456 and Phys. Rev. Lett. 106, 221101, reports geodetic drift $-6601.8\pm18.3$ mas/yr and frame-dragging drift $-37.2\pm7.2$ mas/yr versus GR predictions $-6606.1$ mas/yr and $-39.2$ mas/yr. Link: [arXiv:1105.3456](https://arxiv.org/abs/1105.3456)
- SME Data Tables: Kostelecky and Russell, arXiv:0801.0287, last revised 2026-02-05 as v19, 2026 edition. Link: [arXiv:0801.0287](https://arxiv.org/abs/0801.0287)
- Torsion constraints from Lorentz-violation bounds: Kostelecky, Russell, and Tasson, arXiv:0712.4393, Phys. Rev. Lett. 100, 111102, reports constraints involving 19 of 24 torsion components down to order $10^{-31}$ GeV. Link: [arXiv:0712.4393](https://arxiv.org/abs/0712.4393)
- Nonmetricity constraints from Lorentz-violation bounds: Foster, Kostelecky, and Xu, arXiv:1612.08744, Phys. Rev. D 95, 084033, reports constraints involving 40 nonmetricity components down to order $10^{-43}$ GeV. Link: [arXiv:1612.08744](https://arxiv.org/abs/1612.08744)
- Gravitational Faraday holonomy: recent polarization-transport benchmark for known curved-spacetime parallel transport and projection effects. Link: [EPJ C 2025 article](https://link.springer.com/article/10.1140/epjc/s10052-025-14086-0)

### 15.2 Internal Benchmark Matrix

| Benchmark | Observable | Expected sign or scaling | Artifact ledger | Provenance | 05S5 status |
|---|---|---|---|---|---|
| Flat identity transport | spinor holonomy from zero H3 generator | identity holonomy, zero residual | none beyond numerical tolerance | internal executable test | known-physics recovery |
| Small spatial loop | spin-half lift of H3 spatial generator | spin phase is half the local rotation angle by convention | branch and representation convention | H3 plus 05S5 helper | `representation-lift-only` |
| Loop reversal | reversed spin holonomy | inverse holonomy; small-loop generator changes sign | same branch and detector basis | H3 theorem and executable test | useful diagnostic |
| Local-frame relabeling | conjugated observed and baseline holonomies | residual norm invariant under conjugation | tetrad gauge and spin basis | 05S5 helper | gauge-covariant diagnostic |
| Spin double cover | spinor return under $2\pi$ and $4\pi$ rotations | $2\pi$ changes spinor sign, $4\pi$ returns identity | interference branch and analyzer basis | standard spin representation and executable test | `representation-lift-only` |
| Scalar spin phase ledger | corrected scalar phase residual | observed phase minus Levi-Civita, preparation, magnetic, Berry, detector, instrument, and finite-loop ledgers | all scalar ledgers visible | 05S5 helper | artifact filter |
| Matrix artifact holonomy | observed holonomy minus H3 lift and artifact holonomy | identity residual when artifact model explains the difference | ordered artifact transport | 05S5 helper | artifact filter |
| Nonzero Lorentz-connection residual | residual matrix against H3 lift | residual norm scales as generator mismatch; area density scales as residual divided by loop area | all spin, Berry, magnetic, detector, finite-loop, and instrument ledgers | 05S5 retained diagnostic | `source-response-missing` |

### 15.3 Known-Physics Constraint Matrix

| Constraint family | What it tests | Expected 05S5 behavior | Artifact or scope guard | External provenance | 05S5 use |
|---|---|---|---|---|---|
| Gyroscope geodetic and frame-dragging precession | metric spin-axis transport in Earth orbit | recover GR precession as H3 frame transport or Fermi-Walker transport | patch potentials, gyro calibration, spacecraft roll, guide-star modeling | GP-B final result, 2011 | benchmark only, no residual fit |
| Polarization parallel transport and gravitational Faraday holonomy | photon polarization transport around curved paths | classify as known vector or spin-1 representation transport unless a residual survives medium and projection ledgers | plasma, birefringence, source polarization, projection convention | gravitational Faraday holonomy literature | known-physics recovery |
| Magnetic and electromagnetic spin phases | Zeeman, Aharonov-Bohm, field-gradient, and shielding-sensitive spin phases | subtract or bound before connection residual is considered | local field monitors and shielding model | standard spin Hamiltonian and SME tables for anomaly searches | artifact ledger |
| Berry and material phases | adiabatic basis phase, fiber or crystal birefringence, material polarization transport | subtract or label contamination | medium, path, adiabaticity, analyzer convention | standard geometric-phase physics | artifact ledger |
| Torsion searches through fermion couplings | possible torsion components mapped to spin couplings | no direct 05S5 torsion bound because translational closure and Pulse coefficient map are absent | known-framework equivalence and coefficient smuggling | torsion constraints down to order $10^{-31}$ GeV for mapped components | context only |
| Nonmetricity searches through fermion and photon couplings | possible nonmetricity components mapped to matter/photon couplings | no direct 05S5 nonmetricity bound because length/angle drift record and Pulse map are absent | known-framework equivalence and coefficient smuggling | nonmetricity constraints down to order $10^{-43}$ GeV for mapped components | context only |
| SME Lorentz and CPT coefficient tables | broad matter, photon, neutrino, and gravity-sector coefficients | no import until residual is mapped to a named coefficient | coefficient basis and frame convention | 2026 SME Data Tables v19 | future comparison index only |

### 15.4 Constraint Import Rule

An external numerical bound can enter a future 05S5 successor only if all of the following are true:

- the 05S5 residual is operationally measured or synthetically predeclared before comparison
- the residual is mapped to a named external coefficient or source-response law
- units and frame conventions match
- magnetic, Berry, detector, material, finite-loop, and instrument ledgers are already bounded
- the coefficient is not chosen after seeing the bound

Until then, external constraint families are guardrails. They prevent overclaiming, but they do not validate or falsify a Pulse-specific residual.

### 15.5 05S5.7 Gate Decision

The benchmark matrix supports a useful bounded diagnostic only:

- the flat, loop-reversal, gauge-covariance, double-cover, scalar-ledger, and matrix-ledger checks pass internally
- GP-B and polarization transport remain known metric transport benchmarks
- torsion and nonmetricity external bounds cannot be imported without new operational records and coefficient maps
- the 2026 SME Data Tables are relevant future comparison infrastructure, not current evidence

The retained 05S5 residual remains `source-response-missing`.

## 16. 05S5.8 Adversarial Novelty And Artifact Review

05S5.8 stress-tests every surviving claim. The review is intentionally severe. A claim is not Pulse-specific unless it survives gauge, artifact, known-framework, coefficient, conservation, scope, and source-response checks.

### 16.1 Review Key

| Check | Meaning |
|---|---|
| Gauge and frame | local Lorentz gauge, tetrad convention, frame handedness, and detector-axis convention |
| Spin and branch | Spin double-cover sign, spin basis, preparation, analyzer, and phase-wrap branch |
| EM and Berry | magnetic, electromagnetic, Berry, material, medium, and adiabatic contamination |
| Known GR or lift | ordinary Fermi-Walker, geodetic, frame-dragging, polarization parallel transport, or representation-lift explanation |
| Known framework | Einstein-Cartan, teleparallel, metric-affine, SME, or other external framework equivalence |
| Coefficient and conservation | coefficient smuggling, local Lorentz identity, diffeomorphism identity, and source-response-map absence |
| Scope | H2, H3, H4, 05S4, H7, finite-loop, quantum-source, and external-deviation boundary |

### 16.2 Claim Review Table

| Claim or benchmark | Gauge and frame | Spin and branch | EM and Berry | Known GR or lift | Known framework | Coefficient and conservation | Scope | Final label |
|---|---|---|---|---|---|---|---|---|
| Standard Dirac phase-response in tetrad variables | gauge covariant only after tetrad convention | spin basis is conventional | charged fields need EM ledger | standard curved-spacetime Dirac theory | no new framework needed | conservation identities are standard; no new response law | inside H4 extension | useful conservative recovery |
| Spin-current response to independent connection variation | convention dependent without first-order setup | spin generator normalization must be declared | EM spin terms must be separated | standard first-order matter response | Einstein-Cartan already covers a known version | no Pulse coefficient or connection equation | formal target only | known-framework-equivalent |
| H3 frame holonomy lifted to spin-half holonomy | conjugation only; invariants survive | branch must be fixed | no EM/Berry content by itself | exactly representation lift | no independent connection | no new source-response | inside H3/05S5 | useful conservative recovery |
| Flat identity transport test | no preferred frame remains | no branch issue near identity | no artifact present | flat known physics | no external framework | no source needed | synthetic only | useful conservative recovery |
| Loop reversal and inverse holonomy test | same base-frame convention required | branch must be consistent | no artifact present | ordinary holonomy inversion | no external framework | no source needed | synthetic/internal | useful conservative recovery |
| Local-frame relabeling covariance test | passes by conjugation-invariant residual norm | spin basis relabeling handled | no artifact present | standard gauge covariance | no external framework | no source needed | synthetic/internal | useful bounded diagnostic |
| Spin double-cover sign | sign can be branch convention | exactly Spin double-cover behavior | no artifact present | standard spinor representation | no external framework | no source-response | inside known spin physics | useful conservative recovery |
| Scalar spin phase artifact ledger | frame and detector axes must be recorded | preparation and branch are explicit ledgers | magnetic and Berry ledgers are explicit | may reduce to standard phase accounting | no new framework | nonzero remainder lacks source law | inside 05S4 phase-ledger discipline | useful bounded diagnostic |
| Matrix holonomy artifact ledger | same representation and base frame required | spin branch must be fixed | artifact holonomy must include EM/Berry terms | known lift subtracted first | no new framework | nonzero remainder lacks source law | inside 05S5 helper scope | useful bounded diagnostic |
| Nonzero Lorentz-connection residual | can be gauge artifact unless conjugation-safe | can be branch or preparation artifact | can be EM/Berry contamination | can be missed representation lift | may map to SME or metric-affine coefficient | source-response map absent | no external fit allowed | blocked conditional bridge |
| GP-B geodetic and frame-dragging benchmark | guide-star and gyro-frame conventions matter | spin axis is classical gyroscope, not spinor novelty | patch potentials and instrument effects dominate ledger | ordinary GR precession | no torsion claim | no Pulse coefficient | known-physics benchmark only | useful conservative recovery |
| Polarization gravitational Faraday holonomy | projection and tetrad convention central | polarization basis and analyzer matter | plasma, birefringence, and medium effects central | known polarization transport | no independent connection | no Pulse coefficient | benchmark only | useful conservative recovery |
| Torsion-like residual | translational frame convention unresolved | spin phase alone is insufficient | force and actuator artifacts likely | not fixed by spin holonomy alone | Einstein-Cartan and torsion searches already known | no translational record, coefficient, or conservation law | outside current records | no-go |
| Nonmetricity-like residual | length and angle standards are calibration-heavy | spin branch not decisive | material and clock calibration likely | not fixed by spin holonomy alone | metric-affine and SME mappings already known | no inner-product drift record or source law | outside current records | no-go |
| SME, torsion, and nonmetricity external constraints | coefficient frame conventions dominate | spin-sector mappings are basis dependent | many bounds are artifact-ledger sensitive | external frameworks, not Pulse derivations | known-framework comparison only | no Pulse map, so direct import is coefficient smuggling | external comparison only | blocked conditional bridge |

### 16.3 Adversarial Gate Decision

No row receives `pulse-specific`. The surviving useful outputs are:

- **Useful conservative recovery:** standard Dirac phase-response, H3-to-spin representation lift, flat identity, loop reversal, Spin double-cover behavior, GP-B-style gyroscope precession, and polarization transport benchmarks.
- **Useful bounded diagnostic:** local-frame covariance checks, scalar phase ledgers, matrix holonomy residual ledgers, and residual norm checks.
- **Blocked conditional bridge:** nonzero Lorentz-connection residuals and external-constraint comparisons, because both need a source-response map and coefficient rule.
- **No-go for current records:** torsion-like and nonmetricity-like claims, because 05S5 has no translational closure or independent length/angle drift record.

The adversarial result downgrades 05S5 from possible novelty to a conservative recovery plus bounded diagnostic unless a future task adds a new operational residual and source-response law.

## 17. 05S5 Final Verdict

**Primary verdict label:** useful bounded torsion/connection diagnostic

**Review-2 project-rule classification:** diagnostic tool

The label is deliberately narrow. 05S5 produced a useful bounded connection-holonomy diagnostic and a conservative spin-connection recovery. It did not support torsion physics, nonmetricity physics, or a novel connection-phase response. The word torsion remains in the label only because the verdict category covers the whole torsion/connection frontier; the actual retained executable channel is the Lorentz-connection holonomy residual.

The project-rule classification is `diagnostic tool` rather than `known-physics reformulation`, `conditional derivation`, `new prediction`, `controlled modification`, or `clean no-go`. The reason is that 05S5 does more than rewrite standard spinor GR: it adds explicit record contracts, artifact ledgers, executable residual checks, and no-import rules. It still does not modify the theory or predict a new signal.

Review-2 suggested the artifact names `pulse_model/appendix/spin_connection_pulse_holonomy.md`, `pulse_model/src/pulse_model/spin_connection.py`, and `pulse_model/tests/test_spin_connection.py`. 05S5 keeps the epic-local canonical names aligned to the existing 05S geometry-action appendix sequence and the narrower holonomy-residual scope, while adding thin compatibility artifacts for discoverability.

| Review-2 requested path | Compatibility artifact | Canonical source |
|---|---|---|
| `pulse_model/appendix/spin_connection_pulse_holonomy.md` | `pulse_model/appendix/spin_connection_pulse_holonomy.md` | `pulse_model/appendix/geometry_action/spin_connection_holonomy.md` |
| `pulse_model/src/pulse_model/spin_connection.py` | `pulse_model/src/pulse_model/spin_connection.py` | `pulse_model/src/pulse_model/spin_connection_holonomy.py` |
| `pulse_model/tests/test_spin_connection.py` | `pulse_model/tests/test_spin_connection.py` | `pulse_model/tests/test_spin_connection_holonomy.py` |

### 17.1 Accepted Inputs

05S5 accepts:

- H2 local frames and tetrads inside the accepted H2 reconstruction domain
- H3 corrected local Lorentz frame holonomy as the metric Levi-Civita baseline
- H4 matter phase-response identities as conservative source-side bookkeeping
- 05S4 artifact-ledger discipline for phase and holonomy records
- synthetic records for algebraic sign, branch, gauge, and residual tests
- external constraint families only as dated guardrails, not as fitted Pulse bounds

### 17.2 Accepted Outputs

05S5 adds:

- a spin/full-connection record contract with observed, reconstructed, and inferred fields separated
- a tetrad and spin-connection schema with local Lorentz gauge requirements
- conservative Dirac spinor phase-response and spin-current bookkeeping
- a restricted theorem that torsion-free spin and polarization holonomy are representation lifts of H3 frame holonomy
- a bounded Lorentz-connection residual diagnostic against the H3 lift after artifact ledgers
- executable checks for flat identity, small-loop spin lift, loop reversal, gauge covariance, Spin double-cover behavior, scalar phase ledgers, matrix artifact ledgers, and invalid records
- benchmark and constraint matrices that prevent GP-B, gravitational Faraday rotation, SME, torsion, and nonmetricity constraints from being misused
- an adversarial review that assigns no Pulse-specific novelty label

### 17.3 Rejected Overclaims

05S5 rejects:

- novelty from rewriting standard Dirac theory in tetrad variables
- novelty from the spin-half representation lift of H3 frame holonomy
- novelty from the $2\pi$ spinor sign by itself
- any torsion claim without an independent translational closure record
- any nonmetricity claim without an independent length, angle, or inner-product drift record
- importing Einstein-Cartan, metric-affine, teleparallel, SME, or other external-framework coefficients as Pulse predictions
- fitting a connection coefficient after seeing external bounds
- treating GP-B, geodetic precession, frame dragging, polarization transport, magnetic phases, or Berry phases as new Pulse effects

### 17.4 Downstream Allowed Uses

Downstream work may use 05S5 to:

- test whether a spin, polarization, gyroscope, or internal-state record reduces to H3 Levi-Civita holonomy
- subtract spin-preparation, magnetic, Berry, detector, instrument, and finite-loop ledgers before considering a residual
- check local-frame covariance of a residual by conjugation-invariant norms
- classify nonzero residuals as `source-response-missing` until a source-response law exists
- use external constraint families as a checklist for future coefficient mappings
- guide H6S1 quantum source-response or a future spin-current response proposal without treating either as already derived

### 17.5 Downstream Prohibited Uses

Downstream work must not use 05S5 to:

- claim a novel connection-phase response
- claim torsion or nonmetricity detection
- derive Einstein-Hilbert dynamics, $G$, $\Lambda$, or metric quantization
- bypass H2, H3, H4, or 05S4 assumptions
- import SME, torsion, or nonmetricity numerical bounds without a Pulse coefficient map
- treat a synthetic residual as an experimental signal
- treat a spinor branch sign as an independent connection observable

### 17.6 Remaining Assumptions

The main blockers are:

- no operational translational closure record for torsion-like diagnostics
- no operational length, angle, or inner-product drift record for nonmetricity-like diagnostics
- no Pulse-specific source-response law connecting spin current or another source to a connection residual
- no predeclared coefficient or normalization rule for a nonzero residual
- no external-constraint parameter map
- no boost-sector or full Lorentz spin-holonomy executable helper
- no full symbolic Dirac stress-energy proof in the project convention

### 17.7 Final Verification Commands

Focused Python verification:

```bash
uv run python -m unittest tests.test_spin_connection_holonomy tests.test_spin_connection
```

Full Python verification:

```bash
uv run python -m unittest discover -s tests
```

Docs and packaging verification for the final epic pass:

```bash
npm run typecheck
npm run build
```

Markdown math scan for touched docs: run the project forbidden-delimiter scan against this appendix, `roadmap.md`, and `frontier_strategy.md`.

### 17.8 Roadmap Result

05S5 is a useful level-up, not a breakthrough. It closes the spin/full-connection frontier as a disciplined diagnostic layer:

- stronger than 05S4 for spin and frame-transport artifact handling
- useful for future spin-sensitive or polarization-sensitive records
- not sufficient to promote Step 5 to a novel geometry-action derivation
- not sufficient to claim torsion, nonmetricity, or independent connection dynamics

The next frontier should move to quantum source-response, where the missing source-response law can be attacked directly rather than hidden inside spin-holonomy residuals.

## 18. Review-2 Follow-Up Acceptance Gates

05S5 was reopened after the final verdict for narrow review-2 closure checks. These checks improve discoverability and acceptance bookkeeping; they do not reopen the physics verdict unless a later dependency explicitly changes the source-response status.

### 18.1 Compatibility Artifact Crosswalk

Status: complete.

The compatibility paths requested by review-2 are present and mapped in the final-verdict crosswalk table. The compatibility appendix and Python module redirect to the canonical 05S5 artifacts without duplicating physics.

### 18.2 Torsion-Free Scalar-Clock Invariance Gate

Status: complete.

In the torsion-free, metric-compatible limit, scalar clock pulse accumulation remains:

$$
dN=f\,d\tau
$$

The spin connection affects spinor, polarization, gyroscope, or internal-frame transport through representation holonomy. It does not change scalar proper-time counting unless one of these additional structures is supplied:

- a metric or proper-time change that changes $d\tau$
- a nonmetricity-like length, angle, frequency-ratio, or inner-product drift record
- a separate source-response law that modifies scalar clock accumulation

05S5 derives none of those structures. Therefore a representation-lift-only spin holonomy can coexist with unchanged scalar pulse count. This is checked in `tests/test_spin_connection_holonomy.py` by computing scalar proper time and pulse count, then computing a torsion-free spin lift with `representation-lift-only` classification and verifying the scalar pulse count is unchanged.

The accepted review-2 criterion is:

| Criterion | 05S5 status |
|---|---|
| Scalar clock pulse accumulation remains $dN=f\,d\tau$ in the torsion-free spin-connection limit | Passed |
| Spin-connection holonomy affects spinor/internal-frame transport rather than scalar proper-time counting | Passed |
| Changes to scalar pulse accumulation require metric/proper-time change, nonmetricity-like drift, or a separate source-response law | Passed |
| 05S5 derives such a scalar-clock modification | No |

### 18.3 Post-H6S1 Source-Response Reconciliation

Status: complete.

H6S1 closed with the project-rule classification `diagnostic tool`. It supplies weak-field quantum source/probe discriminator gates, observable classes, and no-signaling and conservation guardrails. It does not supply a pulse-native source-response law.

For 05S5 specifically, H6S1 supplies a guardrail only. It does not add:

- a spin-current-to-connection source-response map
- a Lorentz-connection residual equation
- a torsion or nonmetricity coefficient rule
- a scalar-clock modification law
- a conservation-closed independent-connection dynamics

Therefore H6S1 does not change any 05S5 label. The 05S5 final verdict remains **useful bounded torsion/connection diagnostic**. The retained Lorentz-connection residual remains `source-response-missing`, and torsion-like and nonmetricity-like claims remain unsupported until a future task supplies an operational residual plus a conserved, predeclared source-response law.

The refreshed roadmap files already match this boundary: `roadmap.md` keeps 05S5 as a diagnostic layer without accepted source-response, and `frontier_strategy.md` recommends a quantum source-response law successor using H6S1 gates rather than treating H6S1 as the law itself.

| Dependency question | Reconciliation |
|---|---|
| Does H6S1 supply a relevant spin-current or connection source-response law? | No |
| Does H6S1 supply useful guardrails for future connection-response proposals? | Yes |
| Does H6S1 change the 05S5 primary verdict? | No |
| Does H6S1 remove the `source-response-missing` label from 05S5 residuals? | No |
