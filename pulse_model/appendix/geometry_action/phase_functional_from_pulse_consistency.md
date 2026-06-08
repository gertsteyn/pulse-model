---
title: Geometry Phase Functional From Pulse Consistency
sidebar_label: Phase Functional
sidebar_position: 2
---

# Appendix: Geometry Phase Functional From Pulse Consistency

**Parent hypothesis:** Step 5, Geometry phase functional  
**Status:** Accepted with limits as a useful conservative low-energy geometry-action result; 05S strengthens this conditionally without making it a fundamental derivation from raw pulse data  
**Purpose:** Identify the viable routes for deriving, motivating, or falsifying the Einstein-Hilbert geometric phase functional from pulse-count consistency without assuming the target action.

---

## 1. Route Survey

The target is the geometric phase:

$$
\Theta_{\mathrm{geom}}\stackrel{?}{=}\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U (R-2\Lambda)\sqrt{-g}\,d^4x
$$

The survey verdict is conservative:

> The simplest viable route is not a direct derivation of $R\sqrt{-g}$ from pulse counts alone. It is a constrained low-energy uniqueness route: if H2 gives a smooth Lorentzian metric from pulse and signal records, H3 gives curvature as the local holonomy defect of pulse comparison, H4 gives conserved matter phase-response, and the geometric response is local, diffeomorphism invariant, metric-only, and second order in derivatives, then the Einstein-Hilbert functional is the unique leading candidate in four dimensions, up to a cosmological constant, boundary terms, and higher-curvature corrections.

This is useful, but it is not yet a fundamental derivation. The missing Pulse Model assumption is why pulse-consistency cost must be local and second order in the smooth-metric limit.

### 1.1 Acceptance Constraints

Any route must satisfy the proof-sequence gate:

- explain why the scalar curvature $R$ is the correct local geometric phase density, or name the missing assumption
- preserve diffeomorphism invariance
- combine with H4 matter phase-response to yield:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}
$$

- recover the Newtonian weak-field limit
- avoid a preferred foliation or universal clock
- handle boundary terms or explicitly exclude boundary variations

The route survey therefore rejects any argument that merely starts from the Einstein-Hilbert action and varies it. That verifies the known theory; it does not derive the geometry phase from pulse consistency.

## 2. Candidate Routes

| Route | What it adds | What it can prove | Smuggling risk | Survey verdict |
|---|---|---|---|---|
| Low-energy uniqueness / Lovelock route | Locality, diffeomorphism invariance, four dimensions, metric-only dynamics, at most second derivatives | Selects $G_{\mu\nu}+\Lambda g_{\mu\nu}$ as the leading conserved metric response | High if locality and two-derivative dynamics are presented as pulse-derived without proof | Recommended first route because assumptions are explicit and testable |
| Curvature-holonomy density route | H3 loop residuals become a local curvature measure | Can motivate curvature as a pulse-consistency defect | Medium if scalar contraction $R$ is chosen without explaining why other invariants are suppressed | Good bridge from H3 to the action, but not sufficient alone |
| Regge / simplicial route | A discrete metric network with hinge deficits and cell volumes | Gives a discrete action shaped like curvature defect times hinge area, with continuum relation to $R\sqrt{-g}$ under regular limits | Medium if the triangulation or deficit action is inserted by analogy rather than recovered from pulse records | Best discrete prototype for 05.2 |
| Causal or interval-count route | Order, volume, and interval counts instead of a differentiable metric | Can recover a scalar-curvature estimator in causal-set-like settings | Medium to high because pulse records are richer than pure causal order but not automatically causal sets | Useful comparison, not the primary Pulse Model route |
| Heat-kernel / spectral route | A spectral operator whose asymptotic expansion contains curvature scalars | Can recover Einstein-Hilbert plus higher-curvature terms from a chosen operator | High unless the pulse network naturally defines the operator | Keep as inspiration for future pulse-network Laplacians |
| Induced-gravity route | Matter quantum fluctuations generate an effective metric action | Can motivate why matter phase-response might induce a geometry term | High because it shifts the derivation to quantum matter assumptions and has cosmological-constant risk | Not first; useful for H7 and quantum corrections |
| Thermodynamic or entanglement route | Horizon entropy, local equilibrium, or entanglement equilibrium | Can yield Einstein equations as an equation of state under strong entropy assumptions | High because entropy-area density is an extra assumption, not a pulse-count result | Conceptually relevant, but outside the conservative 05 path |

## 3. Recommended First Route

The first route to carry forward is the low-energy uniqueness route, with an explicit Pulse Model input layer.

### 3.1 Inputs From Earlier Gates

Use accepted inputs only within their accepted limits, and label any stronger use as conditional:

1. H2 supplies the bounded smooth Lorentzian metric object reconstructed from pulse and signal records:

$$
\mathcal{D}_{\mathrm{pulse}}\Rightarrow [g_{\mu\nu}]
$$

2. H3 supplies the first fixed-event or gauge-fixed local curvature observable as a pulse-comparison holonomy defect:

$$
\Delta_{\mathrm{loop}}\Rightarrow R^\rho{}_{\sigma\mu\nu}
$$

3. H4 supplies reviewed matter phase-response for scalar, electromagnetic, and point-particle matter:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

4. H4 conservation supplies, on matter equations of motion:

$$
\nabla_\mu T^{\mu\nu}=0
$$

These inputs are closed but bounded. The geometry route may use H2, H3, and H4 as accepted-with-limits premises only inside their stated scopes: fixed-event or restricted finite metric reconstruction, first-slice curvature-holonomy observables, and standard matter stress-energy phase response. Any stronger use remains conditional and must be reopened as explicit follow-up work rather than treated as already proved.

### 3.2 New Assumptions Needed At The Geometry Gate

The uniqueness route requires these additional assumptions:

- the smooth limit of pulse-consistency cost is local
- the leading long-wavelength geometric response is metric-only
- no preferred clock field, foliation, lattice frame, or universal pulse survives in the continuum action
- the leading equations contain no derivatives higher than second order in the metric
- the theory is four-dimensional in the accepted continuum regime
- boundary data are fixed, or the correct boundary phase is added
- higher-curvature corrections are allowed only as suppressed corrections outside the leading gate

These assumptions are not cosmetic. They are exactly where the Pulse Model could fail to derive Einstein-Hilbert gravity from deeper pulse principles.

## 4. Why The Low-Energy Route Selects Einstein-Hilbert

If the field equation is local, diffeomorphism invariant, metric-only, symmetric, divergence-free, and second order in four dimensions, the geometric side has the form:

$$
aG_{\mu\nu}+b g_{\mu\nu}
$$

for constants $a$ and $b$. Combining with H4 gives a stationary total phase condition:

$$
\frac{\delta\Theta_{\mathrm{geom}}}{\delta g^{\mu\nu}}+\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}=0
$$

The corresponding leading bulk functional is:

$$
\Theta_{\mathrm{geom}}=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U (R-2\Lambda)\sqrt{-g}\,d^4x
$$

The Newtonian limit fixes the coefficient of $R$ to:

$$
\frac{c^3}{16\pi G}
$$

The constant term is the cosmological constant contribution. This route explains why Einstein-Hilbert is the simplest compatible leading action, but it does not yet explain why pulse consistency forbids leading terms such as $R^2$, $R_{\mu\nu}R^{\mu\nu}$, extra scalar fields, torsion, or nonlocal network terms.

## 5. 05.2 Candidate Functional

The 05.2 candidate has two layers:

1. A discrete pulse-consistency phase built from corrected local loop holonomies, hinge areas, and cell volumes.
2. A leading continuum phase selected by locality, diffeomorphism invariance, metric-only response, and second-order field equations.

This is a candidate, not a completed derivation. The Pulse Model input is the operational curvature defect from H3. The additional geometry-gate assumption is that a dense, unbiased, smooth pulse network admits a local scalar coarse-graining of those defects.

### 5.1 Operational Discrete Layer

H3 defines a closed-loop pulse comparison residual for the accepted first slice. In a smooth limit, the tensor-ready bridge is:

$$
\Delta_{\mathrm{loop}}\sim R^\rho{}_{\sigma\mu\nu}A^{\mu\nu}
$$

where $A^{\mu\nu}$ is the small loop area bivector and the exact contraction depends on the transported object and clock-comparison protocol.

For each codimension-two hinge $h$ in a pulse-cell decomposition, let:

- $A_h$ be the hinge area inferred from the bounded H2 metric object
- $V_\sigma$ be the four-volume of cell $\sigma$
- $s_h$ and $s_\sigma$ be the Lorentzian orientation and signature signs fixed by the chosen local convention
- $\epsilon_h$ be the corrected deficit angle or boost parameter around the hinge, reconstructed from H3 frame-closure generators

The operational relation between H3 loop data and the hinge defect is:

$$
\epsilon_h=\sum_{k\in h}w_{h,k}\langle B_h,\mathcal{K}_{L_{h,k}}\rangle_\eta+O(\ell_h^3)
$$

Here $L_{h,k}$ are small loops linking the hinge, $w_{h,k}$ are reconstruction weights, $B_h$ is the unit bivector normal to the hinge, and $\mathcal{K}_{L_{h,k}}$ is the corrected H3 frame-closure generator. The contraction is performed in the local Lorentz frame. This keeps scalar timing residuals in their proper role: they may constrain selected projections, but the hinge defect is defined from the tensor-ready frame closure.

At the current executable level, H3 has only checked spatial frame-plane holonomies. Lorentzian time-space boost defects are part of the formal 05.2 candidate, but they remain conditional on the downstream H3 follow-up that fixes explicit Lorentz-signature boost conventions. The leading geometry-action candidate may still be tested as a continuum low-energy bridge, but the discrete Lorentzian prototype is not yet fully executable.

The discrete candidate is:

$$
\Theta_{\mathrm{pc}}^{\mathrm{disc}}=\frac{c^3}{8\pi G\hbar}\sum_h s_h A_h\epsilon_h-\frac{c^3\Lambda}{8\pi G\hbar}\sum_\sigma s_\sigma V_\sigma+\Theta_{\mathrm{bdry}}+\Theta_{\mathrm{hi}}
$$

$\Theta_{\mathrm{bdry}}$ is a boundary phase, left for 05.4. $\Theta_{\mathrm{hi}}$ collects suppressed higher-curvature, torsion, nonlocal, lattice-anisotropy, or finite-loop corrections. It is allowed as an error or correction budget, but it is not part of the leading 05.2 candidate.

The coefficient is chosen so that the standard Regge-to-continuum relation gives the Einstein-Hilbert normalization:

$$
2\sum_h s_h A_h\epsilon_h\to\int_U R\sqrt{-g}\,d^4x
$$

and:

$$
\sum_\sigma s_\sigma V_\sigma\to\int_U\sqrt{-g}\,d^4x
$$

Therefore:

$$
\Theta_{\mathrm{pc}}^{\mathrm{disc}}\to\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x+\Theta_{\mathrm{bdry}}+\Theta_{\mathrm{hi}}
$$

This motivates the target functional from pulse-loop consistency, but it does not derive the coefficient $G$ or the cosmological constant from pulse data. Those constants remain empirical or matching constants at this gate.

### 5.2 Continuum Leading Layer

In the smooth long-wavelength regime, the most general local metric-only phase density compatible with diffeomorphism invariance has the schematic form:

$$
\Theta_{\mathrm{pc}}^{\mathrm{cont}}=\frac{1}{\hbar}\int_U d^4x\,\sqrt{-g}\left(\lambda_0+\lambda_1 R+\lambda_2 R^2+\lambda_3 R_{\mu\nu}R^{\mu\nu}+\lambda_4 R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}+\cdots\right)
$$

The 05.2 leading candidate keeps only the terms whose metric variation can give second-order metric equations in four dimensions:

$$
\Theta_{\mathrm{geom}}^{(0)}[g]=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x
$$

The candidate relation to $R\sqrt{-g}$ is therefore conditional:

- if H3 loop defects coarse-grain to a local scalar curvature density
- if the continuum response is metric-only and diffeomorphism invariant
- if higher-derivative and nonlocal terms are suppressed in the leading long-wavelength gate
- if no preferred clock, foliation, or lattice frame remains after refinement

then the leading continuum phase is the Einstein-Hilbert phase, up to a cosmological constant and boundary term.

### 5.3 Replacement And Diffeomorphism Symmetry

The discrete layer must be invariant under replacement of the pulse-cell description by another description that encodes the same physical loop, area, orientation, and volume data. Concretely, the candidate may depend on:

- calibrated pulse counts and signal records only through H2 metric quantities, H3 corrected frame closures, and stated artifact corrections
- oriented hinge areas, cell volumes, and local Lorentz contractions
- boundary data, when the boundary is part of the varied region

It must not depend on:

- station labels
- coordinate labels
- arbitrary clock zero choices
- a universal pulse count used as preferred time
- an uncorrected scalar loop residual treated as curvature

In the continuum limit, this replacement symmetry becomes diffeomorphism invariance. Local Lorentz frame changes only relabel the components of $\mathcal{K}_L$ and $B_h$; their contraction in $\epsilon_h$ is a scalar once the hinge orientation is fixed.

### 5.4 Why Linear Defect, Not Squared Residual

A statistical fitting loss such as:

$$
\chi^2_{\mathrm{loop}}=\sum_L\frac{\Delta_L^2}{\sigma_L^2}
$$

is useful for estimating a metric from noisy data, but it is not the leading geometry phase candidate. Since $\Delta_L$ is first order in curvature times loop area, a squared loss naturally produces curvature-squared behavior in the smooth limit. That would point toward $R^2$, $R_{\mu\nu}R^{\mu\nu}$, or protocol-dependent quadratic invariants, not the Einstein-Hilbert term.

The leading candidate is therefore linear in oriented curvature defect:

$$
\sum_h s_h A_h\epsilon_h
$$

This is the smallest bridge from H3 holonomy to a scalar geometric phase. Its weakness is also explicit: linear scalarization requires a complete and unbiased sampling of local two-planes. If the pulse network supplies only preferred loop planes, or if the weighting is protocol-dependent, the candidate fails as a diffeomorphism-invariant leading action and must be replaced by an anisotropic, higher-curvature, or nonlocal functional.

### 5.5 05.2 Outcome

05.2 accepts the following candidate for downstream checks:

$$
\Theta_{\mathrm{geom}}^{(0)}[g]=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x
$$

with the discrete pulse-consistency prototype:

$$
\Theta_{\mathrm{pc}}^{\mathrm{disc}}=\frac{c^3}{8\pi G\hbar}\sum_h s_h A_h\epsilon_h-\frac{c^3\Lambda}{8\pi G\hbar}\sum_\sigma s_\sigma V_\sigma+\Theta_{\mathrm{bdry}}+\Theta_{\mathrm{hi}}
$$

The candidate is accepted only as a conditional low-energy bridge. It does not yet prove that pulse consistency forces locality, a metric-only response, second-order equations, or the absence of nonlocal pulse-network terms. Later 05 checks test the consistency of those assumptions, and the 05.5 report keeps them as downstream limits.

## 6. 05.3 Einstein Equation And Newtonian Limit Check

05.3 checks whether the 05.2 leading candidate has the correct variational response and weak-field normalization when combined with H4 matter phase-response.

### 6.1 Variation Convention

H4 uses inverse-metric variation and the local phase-response identity:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

For the SI-normalized Einstein-equation check, use coordinates with $x^0=ct$ and four-volume $d^4x$. Restoring the standard action-volume factor gives:

$$
\delta\Theta_{\mathrm{m}}=-\frac{1}{2\hbar c}\int_U d^4x\,\sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}
$$

In units with $c=1$, this is the H4 identity as written.

The leading geometric phase from 05.2 is:

$$
\Theta_{\mathrm{geom}}^{(0)}=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x
$$

Ignoring the boundary variation for this 05.3 bulk check gives:

$$
\delta\Theta_{\mathrm{geom}}^{(0)}=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U d^4x\,\sqrt{-g}\,(G_{\mu\nu}+\Lambda g_{\mu\nu})\delta g^{\mu\nu}+\delta\Theta_{\mathrm{bdry}}
$$

The boundary term is not dropped as a mathematical fact. It is deferred to 05.4, where fixed-boundary data or a Gibbons-Hawking-York-type phase must be stated.

### 6.2 Einstein Equation Recovery

Stationary total phase requires:

$$
\delta\Theta_{\mathrm{geom}}^{(0)}+\delta\Theta_{\mathrm{m}}=0
$$

For compactly supported metric variations, or after the correct boundary phase is supplied, the bulk coefficient of $\delta g^{\mu\nu}$ must vanish:

$$
\frac{c^3}{16\pi G}(G_{\mu\nu}+\Lambda g_{\mu\nu})-\frac{1}{2c}T_{\mu\nu}=0
$$

Therefore the 05.2 candidate recovers:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}
$$

This passes the 05.3 Einstein-equation check, conditional on the 05.2 assumptions and the 05.4 boundary treatment. It does not prove the 05.2 assumptions. It only shows that once the leading phase is the Einstein-Hilbert phase with the stated normalization, H4 matter phase-response supplies the standard source term with the correct sign and $c$ powers.

### 6.3 Newtonian Weak-Field Limit

Use the weak, static, slow-motion metric convention already used in the known-physics ladder:

$$
g_{00}\approx -\left(1+\frac{2\Phi}{c^2}\right)
$$

with $\Phi\to0$ at infinity. For nonrelativistic matter:

$$
T_{00}\approx \rho c^2
$$

and pressure, momentum flux, and time derivatives are negligible at leading order. With $\Lambda$ negligible on the local scale, the $00$ component of the linearized geometric side is:

$$
G_{00}\approx \frac{2}{c^2}\nabla^2\Phi
$$

The recovered Einstein equation then gives:

$$
\frac{2}{c^2}\nabla^2\Phi=\frac{8\pi G}{c^4}\rho c^2
$$

so:

$$
\nabla^2\Phi=4\pi G\rho
$$

This is the Poisson equation for the Newtonian potential. Combined with the already accepted known-physics proper-time action:

$$
L=\frac{1}{2}mv^2-m\Phi
$$

it gives:

$$
\mathbf{a}=-\nabla\Phi
$$

Thus the candidate recovers both the correct gravitational field normalization and the known Newtonian equation of motion in the weak, static, pressure-negligible regime.

If $\Lambda$ is retained, the local Poisson equation receives the standard large-scale correction:

$$
\nabla^2\Phi=4\pi G\rho-\Lambda c^2
$$

This term is negligible for the local known-physics checks but belongs in later cosmology-facing work.

### 6.4 Higher-Curvature Ambiguity

05.2 allowed a correction budget:

$$
\Theta_{\mathrm{hi}}=\frac{1}{\hbar}\int_U d^4x\,\sqrt{-g}\,(\lambda_2 R^2+\lambda_3 R_{\mu\nu}R^{\mu\nu}+\lambda_4 R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}+\cdots)
$$

These terms are not harmless if they enter at the same order as the Einstein-Hilbert term. Their metric variation generally adds higher-derivative or extra-mode contributions to the field equation, and the Newtonian limit no longer reduces uniquely to the Poisson equation above.

The 05.3 decision is therefore:

- if $\Theta_{\mathrm{hi}}$ is suppressed at scales tested by the known-physics ladder, it is a controlled correction outside the leading gate
- if pulse consistency naturally gives unsuppressed curvature-squared, torsion, anisotropic, or nonlocal terms, the strong Einstein-Hilbert derivation fails and 05.5 must label the result as a controlled modification or clean failure

The current candidate passes 05.3 only as a leading low-energy functional.

## 7. 05.4 Invariance, Boundary Terms, And Conservation

05.4 checks whether the candidate preserves the required symmetry, avoids a preferred pulse frame, handles boundary terms, and remains compatible with H4 conservation.

### 7.1 Continuum Diffeomorphism Invariance

The continuum leading candidate is:

$$
\Theta_{\mathrm{geom}}^{(0)}=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x
$$

The integrand is a scalar density built only from the metric and its Levi-Civita curvature. If the region $U$ and its boundary data are carried along by an active diffeomorphism, or if the diffeomorphism has compact support inside $U$, the value of the bulk integral is unchanged.

Thus the smooth continuum candidate preserves diffeomorphism invariance. It contains no explicit coordinate labels, station labels, clock-zero choices, preferred lapse, preferred foliation, or universal pulse count.

The discrete pulse prototype has a stricter condition. The hinge sum:

$$
\sum_h s_h A_h\epsilon_h
$$

is acceptable only if the labels of hinges, cells, loops, and stations are replaceable descriptions of the same oriented geometric data. The weights used to reconstruct $\epsilon_h$ must be built from H2 metric data, H3 corrected frame closures, orientations, and local Lorentz contractions, not from arbitrary station numbering or preferred network directions.

The 05.4 symmetry decision is therefore:

- the continuum leading candidate is diffeomorphism invariant
- the discrete prototype is invariant under replacement of equivalent pulse-cell descriptions only under the scalarization and unbiased-refinement assumptions already named in 05.2
- if a preferred clock field, lattice frame, or fixed loop-plane weighting survives refinement, the result is not Einstein-Hilbert gravity but a modified or failed geometry-action candidate

### 7.2 Preferred-Frame Risk

Pulse records require local clocks and signal exchanges, but those are measurement scaffolding, not fields in the leading continuum action. The following uses are allowed:

- local frames and tetrads used to report H3 frame closures
- fixed-event or gauge-fixed H2 reconstructions used to assign loop areas and volumes
- calibrated clock frequencies and signal records used to remove protocol artifacts
- local Lorentz contractions used to form scalar hinge defects

The following would break the 05 leading candidate:

- a universal pulse count used as physical time
- a globally preferred foliation
- station labels or clock zero choices entering $\Theta_{\mathrm{geom}}$
- a nondynamical timelike vector field in the leading action
- anisotropic loop weights not determined by the metric, orientation, or error model

If such a structure is required, 05.5 must label the result as a controlled modification or failure, not as a derivation of the Einstein-Hilbert functional.

### 7.3 Boundary Terms

The bulk Einstein-Hilbert variation contains a surface variation because $R$ contains second derivatives of the metric. Therefore 05.3 was valid only for compactly supported variations or as a bulk calculation with boundary handling deferred.

For a finite region $U$ with fixed induced boundary metric $h_{ab}$, the leading boundary phase should be:

$$
\Theta_{\mathrm{bdry}}^{(0)}=\frac{1}{\hbar}\frac{c^3}{8\pi G}\int_{\partial U}\varepsilon K\sqrt{|h|}\,d^3y
$$

Here $K$ is the trace of the extrinsic curvature of $\partial U$, $h$ is the determinant of the induced boundary metric, and $\varepsilon$ records whether the boundary segment is timelike or spacelike under the chosen sign convention. Null boundaries, corners, and joints require the corresponding null or joint phases.

The finite-region candidate is therefore:

$$
\Theta_{\mathrm{geom}}^{(0)}[U]=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x+\Theta_{\mathrm{bdry}}^{(0)}
$$

with additional joint phases when $\partial U$ is nonsmooth.

In the discrete layer, the matching boundary object is a Regge-style boundary extrinsic-curvature phase:

$$
\Theta_{\mathrm{bdry}}^{\mathrm{disc}}=\frac{c^3}{8\pi G\hbar}\sum_b s_b A_b\psi_b+\Theta_{\mathrm{joint}}^{\mathrm{disc}}
$$

where $b$ labels boundary hinges or faces, $A_b$ is the boundary hinge area, $\psi_b$ is the exterior-angle or boost defect, and $s_b$ carries the orientation and signature convention. The current 05 slice records this boundary prescription but does not implement a full boundary-hinge simulator.

The boundary decision is:

- for local bulk checks, compactly supported variations are sufficient
- for finite regions with fixed induced metric, include the Gibbons-Hawking-York-type phase and joint phases where needed
- without one of these boundary choices, the variational statement in 05.3 is incomplete

### 7.4 Conservation Compatibility With H4

The geometric side of the leading equation is compatible with conservation because the contracted Bianchi identity gives:

$$
\nabla_\mu G^{\mu\nu}=0
$$

Metric compatibility also gives:

$$
\nabla_\mu g^{\mu\nu}=0
$$

Therefore:

$$
\nabla_\mu(G^{\mu\nu}+\Lambda g^{\mu\nu})=0
$$

Using the 05.3 field equation:

$$
G^{\mu\nu}+\Lambda g^{\mu\nu}=\frac{8\pi G}{c^4}T^{\mu\nu}
$$

the source must obey:

$$
\nabla_\mu T^{\mu\nu}=0
$$

This matches H4 exactly: H4 derives covariant conservation on shell from diffeomorphism invariance of the matter phase. Open subsystems may exchange energy and momentum, but the total stress-energy tensor for the interacting system must be used as the source.

For a finite region, conservation also has boundary flux content. Stress-energy may cross $\partial U$ without violating local conservation; the boundary data and matter flux determine what is held fixed in the variational problem.

The conservation decision is:

- the leading continuum candidate is compatible with H4 on-shell conservation
- nonconserved matter histories cannot source the leading equation unless the missing stress-energy flux or external fields are included
- unsuppressed higher-curvature or nonlocal corrections must carry their own diffeomorphism-invariant conservation identity, or they fail the 05 gate

### 7.5 05.4 Outcome

The candidate preserves the required symmetry and conservation structure conditionally:

- continuum diffeomorphism invariance passes for the Einstein-Hilbert plus cosmological-constant phase
- preferred-frame risk is controlled only if pulse clocks, stations, and loop choices remain measurement scaffolding rather than leading action fields
- boundary handling is valid for compactly supported variations or finite-region variations with the Gibbons-Hawking-York-type phase and necessary joint phases
- conservation is compatible with H4 through the Bianchi identity and on-shell matter diffeomorphism invariance

The 05.5 report below carries this into the final useful-conservative decision. This is still not a strong derivation from pulse data alone, because discrete replacement invariance, refinement independence, scalarization, and full Lorentzian boundary-hinge handling remain conditional.

## 8. Routes Rejected For Now

The following are not acceptable derivations for the current proof sequence:

- "The action must be $\int R\sqrt{-g}d^4x$ because $R$ is the simplest scalar." This is a heuristic, not a derivation.
- "Vary Einstein-Hilbert and recover Einstein's equation." This checks consistency but assumes the target.
- "Use pulse count as a universal lattice time." This conflicts with H1 and risks a preferred foliation.
- "Add the first curvature scalar seen in a discrete model." This can smuggle in the continuum action unless the discrete observable is derived from pulse records.
- "Use entropy, spectral, or induced-gravity arguments without deriving the entropy density, operator, or quantum matter measure from pulse data." These routes can inspire future work but add independent assumptions.

## 9. Work Program And 05 Task Closure

05.2 has developed the candidate in two layers:

1. A discrete pulse-consistency cost built from loop residuals or hinge-like curvature defects.
2. A continuum leading functional selected by locality, diffeomorphism invariance, and second-order metric response.

The accepted 05.2 working candidate is the linear defect phase in Section 5.5. It remains conditional on the scalarization, locality, metric-only, and second-order assumptions named above.

05.3 has checked the variation and constants:

- Einstein's equation is recovered when the 05.2 candidate is combined with H4 matter phase-response and the standard SI action-volume factor
- the Newtonian Poisson equation and $\mathbf{a}=-\nabla\Phi$ are recovered in the weak, static, pressure-negligible regime
- higher-curvature terms are acceptable only as suppressed corrections; if unsuppressed, they are a fatal ambiguity for the strong Einstein-Hilbert derivation

05.4 has handled:

- continuum diffeomorphism invariance passes for the leading Einstein-Hilbert candidate
- absence of a preferred clock or foliation is conditional on pulse records remaining measurement scaffolding rather than action fields
- finite-region boundary terms require a Gibbons-Hawking-York-type phase plus joint phases where needed
- conservation is compatible with H4 through the Bianchi identity and on-shell matter diffeomorphism invariance

05.5 decides the outcome as a useful conservative result. The current 05 evidence supports the Einstein-Hilbert plus cosmological-constant phase as the leading low-energy geometry-action candidate under explicit assumptions. It does not support the stronger claim that pulse consistency alone has derived the action.

The four possible outcomes are now resolved as follows:

- strong success is not reached, because the pulse-to-locality, scalarization, and refinement assumptions remain assumed rather than derived
- useful conservative result is accepted, because the current candidate passes the Einstein-equation, Newtonian-limit, diffeomorphism-invariance, boundary, and conservation checks when those assumptions are supplied
- controlled modification is not required by the current evidence, but remains the correct label if pulse consistency later demands suppressed or testable higher-curvature, torsion, anisotropic, or nonlocal corrections
- clean failure is not reached, because no current check selects a different leading functional or requires a preferred structure

## 10. Reference Anchors

The following references are anchors for the route survey, not accepted Pulse Model premises:

- Lovelock-style uniqueness: [On second-order, divergence-free tensors](https://arxiv.org/abs/1306.4354)
- Regge and deficit curvature: [On the definition of curvature in Regge calculus](https://academic.oup.com/imajna/article/44/5/2698/7502804)
- Causal-set scalar curvature: [The Scalar Curvature of a Causal Set](https://arxiv.org/abs/1001.2725)
- Spectral action: [The Spectral Action Principle](https://arxiv.org/abs/hep-th/9606001)
- Induced-gravity comparison: [Inducing Gravity From Connections and Scalar Fields](https://arxiv.org/abs/1808.09348)
- Thermodynamic comparison: [Thermodynamics of Spacetime](https://arxiv.org/abs/gr-qc/9504004)
- Entanglement-equilibrium comparison: [Entanglement Equilibrium and the Einstein Equation](https://arxiv.org/abs/1505.04753)

## 11. 05.5 Geometry-Action Decision Report

The 05.1 route survey recommended a conservative route:

> Treat Einstein-Hilbert as the leading smooth, local, diffeomorphism-invariant, metric-only, second-order phase functional compatible with H2 metric reconstruction, H3 curvature holonomy, and H4 conserved matter phase-response.

05.2 turns that route into an explicit candidate:

- discrete layer: a Regge-shaped linear pulse-consistency phase $\sum_h s_h A_h\epsilon_h$ built from corrected H3 loop holonomies and H2 geometric measures
- continuum layer: the leading Einstein-Hilbert phase $\int_U(R-2\Lambda)\sqrt{-g}\,d^4x$ under locality, diffeomorphism invariance, metric-only response, and second-order assumptions
- rejection: squared loop-residual losses are treated as estimator costs, not as the leading geometry phase, because they naturally lead to curvature-squared terms

This was enough to run the 05.3 checks. It is not enough to claim that pulse consistency has derived general relativity. The central open assumption remains why the pulse-consistency functional has a local, scalar, metric-only, second-order smooth limit.

05.3 adds that the candidate has the correct bulk variational normalization:

- stationary total phase recovers $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}/c^4$
- the weak-field $00$ component recovers $\nabla^2\Phi=4\pi G\rho$ when $\Lambda$ and pressure are negligible
- higher-curvature terms must remain suppressed, or the strong Einstein-Hilbert claim fails

This was enough to run the 05.4 checks. It still does not prove the missing pulse-to-locality and scalarization assumptions, and it left boundary terms to be resolved by 05.4.

05.4 adds that the candidate has the required symmetry and boundary structure at the leading continuum level:

- the smooth Einstein-Hilbert plus cosmological-constant phase is diffeomorphism invariant
- the leading action contains no preferred pulse clock, foliation, station label, or lattice frame
- finite-region variations require $\Theta_{\mathrm{bdry}}^{(0)}$ and possible joint phases
- conservation is compatible with H4 because $\nabla_\mu(G^{\mu\nu}+\Lambda g^{\mu\nu})=0$ matches H4's on-shell $\nabla_\mu T^{\mu\nu}=0$

### 11.1 Decision Label

The 05 gate is accepted with limits as a useful conservative result.

It is a low-energy conditional motivation for the Einstein-Hilbert phase, not a strong derivation of that phase from raw pulse data. The strongest Pulse Model claim remains blocked until the model derives, rather than assumes, the missing locality, scalarization, refinement, and Lorentzian discrete-boundary inputs.

### 11.2 What 05 Accepts

Later work may use the following bounded result:

$$
\Theta_{\mathrm{geom}}^{(0)}[g]=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x+\Theta_{\mathrm{bdry}}^{(0)}
$$

This result is accepted only in the smooth, low-energy, metric regime where:

- H2 supplies the metric data within its accepted fixed-event or restricted finite-data scope
- H3 supplies curvature-holonomy input within its accepted fixed-event or gauge-fixed scope
- H4 supplies conserved matter phase-response within its accepted standard-matter scope
- the pulse-consistency cost has a local scalar smooth limit
- the leading response is metric-only, diffeomorphism invariant, and second order
- pulse clocks, stations, and loop labels remain measurement scaffolding rather than action fields
- finite-region variations include the boundary and joint phases required by the boundary data

Under those conditions, stationary total phase gives:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}
$$

and the weak, static, pressure-negligible limit gives:

$$
\nabla^2\Phi=4\pi G\rho
$$

### 11.3 What 05 Does Not Accept

05 does not establish:

- a fundamental derivation of Einstein-Hilbert gravity from pulse counts alone
- a derivation that pulse consistency must be local in the smooth limit
- a derivation that H3 tensor holonomies must scalarize exactly to $R$
- a proof that all higher-curvature, torsion, anisotropic, or nonlocal pulse-network terms are suppressed
- a full executable Lorentzian Regge pulse-cell model with boost hinges, null boundaries, and joints
- a derivation of $G$ or $\Lambda$ from pulse data
- a solution to vacuum-energy renormalization or the cosmological-constant problem

These are not presentation caveats. They are the precise limits on what later epics may claim.

### 11.4 Downstream Rules

H5 may continue to use known weak-field proper-time inputs and quantum-clock visibility formulas as conservative known-physics inputs. H5 should not cite 05 as a derivation of gravitational dynamics.

H6 may use the 05 result as a conditional branch-local classical source-to-metric equation only when the same smooth low-energy assumptions are explicitly carried forward. H6 must still decide whether metric branches are semiclassical, branch-specific, collapse-driven, or another model, and it must not treat metric superposition as solved by 05.

H7 may use the 05 result only to identify the metric-sensitive phase-response that couples to curvature in the low-energy effective description. H7 must not use 05 to claim that absolute vacuum phase does not gravitate, that $\Lambda$ is pulse-derived, or that renormalization has been solved.

Any later appendix that relies on 05 should cite the result as accepted with limits, and should carry forward the missing assumptions rather than hiding them.

### 11.5 Failure And Modification Triggers

The decision should be revised to controlled modification if future pulse-network analysis shows that the leading smooth phase necessarily contains suppressed but testable corrections, such as higher-curvature, torsion, anisotropic, or nonlocal terms. In that case the Einstein-Hilbert phase remains the low-energy anchor only after the correction scale and symmetry content are stated.

The decision should be revised to clean failure if future pulse-network analysis shows that the leading phase requires an unsuppressed preferred clock, preferred foliation, station-label dependence, unremovable anisotropic loop weighting, nonconserved matter sourcing, or a different leading functional incompatible with the Einstein-equation and Newtonian-limit checks above.

### 11.6 Final Verdict

05 succeeds at the conservative level and fails to reach the strong level.

The Pulse Model now has a usable low-energy geometry-action bridge:

- it can recover Einstein's equation from H4 matter phase-response once the Einstein-Hilbert leading phase is supplied under explicit assumptions
- it can recover the Newtonian limit with the correct normalization
- it can preserve diffeomorphism invariance, boundary consistency, and H4 conservation at the leading continuum level

But the model has not yet derived the Einstein-Hilbert action from pulse counts alone. The correct final label for 05 is useful conservative result: accepted with limits as conditional low-energy motivation.

### 11.7 05S Follow-Up

The follow-up appendix `pulse_network_strengthening.md` upgrades this result to a stronger conditional derivation. It defines admissible pulse networks, maps H3 frame holonomies to non-null Lorentzian hinge defects, states locality, scalarization, and refinement-invariance sufficient conditions, adds a small pulse-Regge prototype, and classifies corrections and alternatives.

This does not erase the 05 caveat. The stronger 05S result holds only when its admissibility, locality, scalarization, replacement-invariance, boundary, and correction-suppression assumptions are carried explicitly. The conservative fallback remains the 05 accepted-with-limits result above.
