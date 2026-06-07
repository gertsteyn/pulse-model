# Appendix: H4 Stress-Energy As Phase-Response

**Parent hypothesis:** 6.4 Hypothesis H4: Stress-energy is phase-response density  
**Status:** Accepted with limits for standard scalar, electromagnetic, and point-particle matter systems  
**Purpose:** Recover standard stress-energy tensors from matter phase response and keep the Pulse Model interpretation separated from the standard variational identity.

---

## 1. Shared Conventions

This appendix uses the same conventions as the main formalization.

- The metric signature is $(-,+,+,+)$.
- Stress-energy is varied with respect to the inverse metric $g^{\mu\nu}$.
- The matter action and matter phase are related by $S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}$.
- Metric variations hold matter fields fixed unless explicitly stated.
- Boundary fields or variations are assumed fixed, or variations have compact support.
- All equations are local tensor equations. Coordinate choices are not physical observables.

The standard inverse-metric variation convention is:

$$
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

Since $S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}$, the same identity can be written as:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta \Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

This is the H4 phase-response identity. It is not a new stress-energy definition. It is the standard definition rewritten in matter-phase variables.

Equivalently, a small inverse-metric perturbation changes matter phase by:

$$
\delta\Theta_{\mathrm{m}}=-\frac{1}{2\hbar}\int d^4x\,\sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}
$$

So stress-energy is the local coefficient that tells how matter phase responds when the pulse-count metric is varied.

## 2. Boundary Assumptions

The scalar derivation below uses a minimally coupled real scalar field. The action contains no derivatives of the metric, so the metric variation does not require a metric boundary term.

When deriving the scalar field equation from variations of $\phi$, the usual integration-by-parts boundary term is discarded by assuming fixed boundary values or compactly supported field variations. H4 does not rely on field-equation variation for the stress-energy definition, but the conservation proof in Section 11 uses the matter equations and boundary assumptions explicitly.

## 3. Scalar Field Action

Let $\phi$ be a real scalar field with potential $V(\phi)$. The minimally coupled matter action is:

$$
S_\phi=\int d^4x\,\sqrt{-g}\,\mathcal{L}_\phi
$$

with:

$$
\mathcal{L}_\phi=-\frac{1}{2}g^{\alpha\beta}\nabla_\alpha\phi\nabla_\beta\phi - V(\phi)
$$

For a scalar field, $\nabla_\mu\phi=\partial_\mu\phi$.

In a local orthonormal frame, every term in $T_{\hat{a}\hat{b}}$ recovered below has units of energy density or pressure. The potential $V$ has the same units as the kinetic scalar density. The phase $\Theta_\phi$ is dimensionless, and the factor $\hbar$ in the phase-response identity restores the action units needed by the standard stress-energy variation.

## 4. Variation With Respect To The Inverse Metric

Use the standard determinant variation:

$$
\delta\sqrt{-g}=-\frac{1}{2}\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}
$$

Holding $\phi$ fixed during the metric variation gives:

$$
\delta\mathcal{L}_\phi=-\frac{1}{2}\nabla_\mu\phi\nabla_\nu\phi\,\delta g^{\mu\nu}
$$

Therefore:

$$
\delta S_\phi=-\frac{1}{2}\int d^4x\,\sqrt{-g}\,\left(\nabla_\mu\phi\nabla_\nu\phi+g_{\mu\nu}\mathcal{L}_\phi\right)\delta g^{\mu\nu}
$$

So:

$$
\frac{\delta S_\phi}{\delta g^{\mu\nu}}=-\frac{1}{2}\sqrt{-g}\,\left(\nabla_\mu\phi\nabla_\nu\phi+g_{\mu\nu}\mathcal{L}_\phi\right)
$$

Insert this into the inverse-metric definition:

$$
T_{\mu\nu}^{(\phi)}=\nabla_\mu\phi\nabla_\nu\phi+g_{\mu\nu}\mathcal{L}_\phi
$$

Using the scalar Lagrangian, the standard scalar-field stress-energy tensor is:

$$
T_{\mu\nu}^{(\phi)}=\nabla_\mu\phi\nabla_\nu\phi-g_{\mu\nu}\left(\frac{1}{2}\nabla_\alpha\phi\nabla^\alpha\phi+V(\phi)\right)
$$

This has the expected sign for signature $(-,+,+,+)$.

## 5. Phase-Response Form

The scalar matter phase is:

$$
\Theta_\phi=\frac{S_\phi}{\hbar}
$$

The variation becomes:

$$
\delta\Theta_\phi=-\frac{1}{2\hbar}\int d^4x\,\sqrt{-g}\,T_{\mu\nu}^{(\phi)}\delta g^{\mu\nu}
$$

Equivalently:

$$
T_{\mu\nu}^{(\phi)}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_\phi}{\delta g^{\mu\nu}}
$$

The Pulse Model interpretation is therefore conservative at this stage:

> The scalar field contributes to geometry through the response of its phase to metric variation. The pulse-language statement is exactly the standard stress-energy tensor written in phase variables.

This does not derive the Einstein equation or a geometric action. It only verifies that the matter side of the source term can be expressed as phase-response without changing the known physics.

## 6. Energy Density, Momentum Flux, Pressure, And Stress

Let $u^\mu$ be a unit future-directed timelike observer:

$$
u^\mu u_\mu=-1
$$

Define the spatial projector:

$$
h_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu
$$

Define the observer-time and spatial derivatives of the scalar:

$$
\dot{\phi}=u^\mu\nabla_\mu\phi
$$

$$
D_\mu\phi=h_\mu{}^\alpha\nabla_\alpha\phi
$$

The energy density measured by the observer is:

$$
\rho_\phi=T_{\mu\nu}^{(\phi)}u^\mu u^\nu=\frac{1}{2}\dot{\phi}^2+\frac{1}{2}D_\alpha\phi D^\alpha\phi+V(\phi)
$$

The momentum density or energy flux, using $q_\mu=-h_\mu{}^\alpha T_{\alpha\beta}u^\beta$, is:

$$
q_\mu^{(\phi)}=-\dot{\phi}D_\mu\phi
$$

The spatial stress tensor is:

$$
S_{\mu\nu}^{(\phi)}=h_\mu{}^\alpha h_\nu{}^\beta T_{\alpha\beta}^{(\phi)}
$$

which gives:

$$
S_{\mu\nu}^{(\phi)}=D_\mu\phi D_\nu\phi+h_{\mu\nu}\left(\frac{1}{2}\dot{\phi}^2-\frac{1}{2}D_\alpha\phi D^\alpha\phi-V(\phi)\right)
$$

The isotropic pressure is the spatial trace:

$$
p_\phi=\frac{1}{3}h^{\mu\nu}S_{\mu\nu}^{(\phi)}
$$

so:

$$
p_\phi=\frac{1}{2}\dot{\phi}^2-\frac{1}{6}D_\alpha\phi D^\alpha\phi-V(\phi)
$$

For a homogeneous scalar in the observer frame, $D_\mu\phi=0$, so:

$$
\rho_\phi=\frac{1}{2}\dot{\phi}^2+V(\phi)
$$

$$
p_\phi=\frac{1}{2}\dot{\phi}^2-V(\phi)
$$

These are the standard scalar-field energy density and pressure expressions. The pressure term is not an added mass-density assumption; it is part of the same metric phase-response tensor.

## 7. Electromagnetic Field Action

This section uses rationalized relativistic units for compactness. In SI conventions, the electromagnetic action and stress-energy tensor carry the usual overall factor $1/\mu_0$. That factor does not change the metric variation or phase-response structure.

Let $A_\mu$ be the electromagnetic potential and:

$$
F_{\mu\nu}=\nabla_\mu A_\nu-\nabla_\nu A_\mu
$$

The field strength is invariant under the gauge transformation $A_\mu\mapsto A_\mu+\nabla_\mu\chi$, because the antisymmetrized second derivative of a scalar vanishes. The stress-energy tensor below is therefore gauge invariant because it depends only on $F_{\mu\nu}$.

The Maxwell action is:

$$
S_{\mathrm{EM}}=\int d^4x\,\sqrt{-g}\,\mathcal{L}_{\mathrm{EM}}
$$

with:

$$
\mathcal{L}_{\mathrm{EM}}=-\frac{1}{4}F_{\alpha\beta}F^{\alpha\beta}
$$

When varying the inverse metric, hold the lower-index field strength $F_{\mu\nu}$ fixed. The metric only enters through $\sqrt{-g}$ and through the raised indices in $F^{\alpha\beta}$.

The Lagrangian variation is:

$$
\delta\mathcal{L}_{\mathrm{EM}}=-\frac{1}{2}F_{\mu\alpha}F_\nu{}^\alpha\delta g^{\mu\nu}
$$

Using the determinant variation from the shared conventions:

$$
\delta S_{\mathrm{EM}}=-\frac{1}{2}\int d^4x\,\sqrt{-g}\,\left(F_{\mu\alpha}F_\nu{}^\alpha+g_{\mu\nu}\mathcal{L}_{\mathrm{EM}}\right)\delta g^{\mu\nu}
$$

So:

$$
T_{\mu\nu}^{(\mathrm{EM})}=F_{\mu\alpha}F_\nu{}^\alpha+g_{\mu\nu}\mathcal{L}_{\mathrm{EM}}
$$

Equivalently:

$$
T_{\mu\nu}^{(\mathrm{EM})}=F_{\mu\alpha}F_\nu{}^\alpha-\frac{1}{4}g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
$$

This is the standard electromagnetic stress-energy tensor for signature $(-,+,+,+)$. It is symmetric, gauge invariant, and traceless in four spacetime dimensions:

$$
T^\mu{}_{\mu}^{(\mathrm{EM})}=0
$$

The electromagnetic phase is:

$$
\Theta_{\mathrm{EM}}=\frac{S_{\mathrm{EM}}}{\hbar}
$$

Therefore:

$$
T_{\mu\nu}^{(\mathrm{EM})}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{EM}}}{\delta g^{\mu\nu}}
$$

This is again the standard tensor, written in phase-response variables.

## 8. Electromagnetic Energy Density, Flux, Pressure, And Stress

For an observer with four-velocity $u^\mu$, define electric and magnetic fields measured by that observer:

$$
E_\mu=F_{\mu\nu}u^\nu
$$

$$
B_\mu=\frac{1}{2}\epsilon_{\mu\nu\alpha\beta}u^\nu F^{\alpha\beta}
$$

Both are spatial:

$$
E_\mu u^\mu=0
$$

$$
B_\mu u^\mu=0
$$

In the observer's local orthonormal frame, the energy density is:

$$
\rho_{\mathrm{EM}}=T_{\mu\nu}^{(\mathrm{EM})}u^\mu u^\nu=\frac{1}{2}\left(E^2+B^2\right)
$$

The momentum density or energy flux is the Poynting vector:

$$
q_{\hat{i}}^{(\mathrm{EM})}=\left(E\times B\right)_{\hat{i}}
$$

The spatial stress components are:

$$
S_{\hat{i}\hat{j}}^{(\mathrm{EM})}=-E_{\hat{i}}E_{\hat{j}}-B_{\hat{i}}B_{\hat{j}}+\frac{1}{2}\delta_{\hat{i}\hat{j}}\left(E^2+B^2\right)
$$

The isotropic pressure is the spatial trace divided by three:

$$
p_{\mathrm{EM}}=\frac{1}{3}S_{\hat{i}}{}^{\hat{i}}=\frac{1}{6}\left(E^2+B^2\right)=\frac{1}{3}\rho_{\mathrm{EM}}
$$

The full stress tensor is generally anisotropic. For example, a pure electric field has tension along the field direction and pressure transverse to it. This matters for H4 because electromagnetic stress-energy cannot be reduced to mass density or scalar clock-rate change.

## 9. Point-Particle Worldline Action

This section uses $c=1$ for compact notation. With explicit units, the action is $S_{\mathrm{pp}}=-mc^2\int d\tau$.

Let a massive point particle follow a timelike worldline $z^\mu(\lambda)$. The reparametrization-invariant action is:

$$
S_{\mathrm{pp}}=-m\int d\lambda\,\sqrt{-g_{\mu\nu}(z)\frac{dz^\mu}{d\lambda}\frac{dz^\nu}{d\lambda}}
$$

Choosing proper time $\tau$ after the variation gives:

$$
u^\mu=\frac{dz^\mu}{d\tau}
$$

with:

$$
g_{\mu\nu}u^\mu u^\nu=-1
$$

Metric variation at fixed worldline gives:

$$
\delta S_{\mathrm{pp}}=\frac{m}{2}\int d\tau\,u^\mu u^\nu\delta g_{\mu\nu}(z(\tau))
$$

Using $\delta g_{\alpha\beta}=-g_{\alpha\mu}g_{\beta\nu}\delta g^{\mu\nu}$:

$$
\delta S_{\mathrm{pp}}=-\frac{m}{2}\int d\tau\,u_\mu u_\nu\delta g^{\mu\nu}(z(\tau))
$$

Define the covariant four-dimensional delta distribution by:

$$
\int d^4x\,\sqrt{-g}\,\delta_g^{(4)}(x,z(\tau))f(x)=f(z(\tau))
$$

Then:

$$
\delta S_{\mathrm{pp}}=-\frac{1}{2}\int d^4x\,\sqrt{-g}\left[m\int d\tau\,u_\mu u_\nu\delta_g^{(4)}(x,z(\tau))\right]\delta g^{\mu\nu}
$$

Therefore:

$$
T_{\mu\nu}^{(\mathrm{pp})}=m\int d\tau\,u_\mu u_\nu\delta_g^{(4)}(x,z(\tau))
$$

Equivalently:

$$
T^{\mu\nu}_{(\mathrm{pp})}=m\int d\tau\,u^\mu u^\nu\delta_g^{(4)}(x,z(\tau))
$$

This is the standard distributional point-particle stress-energy tensor. Its support is only on the worldline.

The point-particle phase is:

$$
\Theta_{\mathrm{pp}}=\frac{S_{\mathrm{pp}}}{\hbar}
$$

So:

$$
T_{\mu\nu}^{(\mathrm{pp})}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{pp}}}{\delta g^{\mu\nu}}
$$

The relation to proper time is direct: the action phase is proportional to accumulated proper time along the worldline, and the stress-energy tensor is the response of that worldline phase to the metric.

## 10. Point-Particle Energy Density, Momentum Flux, Pressure, And Stress

In a local orthonormal frame, the particle four-momentum is:

$$
p^{\hat{a}}=m u^{\hat{a}}
$$

For a particle crossing a spatial hypersurface, the stress-energy components can be written schematically as:

$$
T^{\hat{a}\hat{b}}_{(\mathrm{pp})}=\frac{p^{\hat{a}}p^{\hat{b}}}{p^{\hat{0}}}\delta^{(3)}(\mathbf{x}-\mathbf{z})
$$

Thus:

$$
T^{\hat{0}\hat{0}}_{(\mathrm{pp})}=p^{\hat{0}}\delta^{(3)}(\mathbf{x}-\mathbf{z})
$$

is the local energy density distribution,

$$
T^{\hat{0}\hat{i}}_{(\mathrm{pp})}=p^{\hat{i}}\delta^{(3)}(\mathbf{x}-\mathbf{z})
$$

is momentum density or energy flux, and:

$$
T^{\hat{i}\hat{j}}_{(\mathrm{pp})}=\frac{p^{\hat{i}}p^{\hat{j}}}{p^{\hat{0}}}\delta^{(3)}(\mathbf{x}-\mathbf{z})
$$

is spatial momentum flux or stress.

A single freely moving point particle is not an isotropic fluid, so it does not have an intrinsic scalar pressure in the fluid sense. A coarse-grained ensemble of particles can produce pressure and anisotropic stress through velocity dispersion:

$$
T^{\mu\nu}_{\mathrm{dust}}=\rho_0 u^\mu u^\nu
$$

for cold dust, and more general kinetic distributions give nonzero pressure and anisotropic stress. This is exactly why H4 must track the full tensor, not only rest mass density.

## 11. Conservation From Diffeomorphism Invariance

The conservation result is not an independent postulate. It follows when the matter action is diffeomorphism invariant, boundary terms vanish, and the matter fields satisfy their equations of motion.

Let $\psi^A$ denote all matter fields or worldline variables. A general first variation can be written schematically as:

$$
\delta S_{\mathrm{m}}=\int d^4x\,\sqrt{-g}\,E_A\delta\psi^A-\frac{1}{2}\int d^4x\,\sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}
$$

Here $E_A=0$ are the matter equations of motion. Boundary terms are assumed to vanish by compact support or fixed boundary data.

For an infinitesimal diffeomorphism generated by a compactly supported vector field $\xi^\mu$, the inverse metric changes by its Lie derivative:

$$
\delta_\xi g^{\mu\nu}=-\nabla^\mu\xi^\nu-\nabla^\nu\xi^\mu
$$

On shell, $E_A=0$, so diffeomorphism invariance gives:

$$
0=\delta_\xi S_{\mathrm{m}}=\int d^4x\,\sqrt{-g}\,T_{\mu\nu}\nabla^\mu\xi^\nu
$$

Integrating by parts and dropping the boundary term:

$$
0=-\int d^4x\,\sqrt{-g}\,\left(\nabla^\mu T_{\mu\nu}\right)\xi^\nu
$$

Since $\xi^\nu$ is arbitrary inside the integration region:

$$
\nabla^\mu T_{\mu\nu}=0
$$

Equivalently:

$$
\nabla_\mu T^{\mu\nu}=0
$$

In phase-response variables, this is the same statement because $S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}$. The phase-response tensor is conserved on shell when the matter phase is diffeomorphism invariant:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

The proof is local and does not depend on coordinates. It does depend on using the full tensor response. A scalar mass density alone cannot supply the momentum-flux and stress terms needed for covariant conservation.

### 11.1 Scalar Field

Varying the scalar field itself gives the usual equation of motion:

$$
\nabla_\mu\nabla^\mu\phi-\frac{dV}{d\phi}=0
$$

Using this on-shell condition in the diffeomorphism proof gives:

$$
\nabla_\mu T^{\mu\nu}_{(\phi)}=0
$$

Off shell, $\nabla_\mu T^{\mu\nu}_{(\phi)}$ is proportional to the scalar field equation. Conservation is therefore not expected for arbitrary field histories.

### 11.2 Electromagnetic Field

For free electromagnetic fields, varying $A_\mu$ gives:

$$
\nabla_\mu F^{\mu\nu}=0
$$

with source terms added when charged matter is included.

The free electromagnetic stress-energy tensor is conserved on shell:

$$
\nabla_\mu T^{\mu\nu}_{(\mathrm{EM})}=0
$$

When charged matter is present, the electromagnetic tensor alone is not separately conserved. It exchanges energy and momentum with charged matter:

$$
\nabla_\mu T^{\mu\nu}_{(\mathrm{EM})}=-F^\nu{}_\lambda J^\lambda
$$

The charged matter tensor has the opposite exchange term, so the total stress-energy tensor is conserved:

$$
\nabla_\mu\left(T^{\mu\nu}_{(\mathrm{EM})}+T^{\mu\nu}_{(\mathrm{charged})}\right)=0
$$

This is not a failure of H4. It is the expected local exchange between interacting subsystems.

### 11.3 Point Particles

For a freely falling point particle, varying the worldline gives the geodesic equation:

$$
u^\mu\nabla_\mu u^\nu=0
$$

Using that equation in the distributional stress-energy tensor gives:

$$
\nabla_\mu T^{\mu\nu}_{(\mathrm{pp})}=0
$$

in the distributional sense. If the particle is charged or subject to external forces, its stress-energy is not separately conserved; the force term is balanced by stress-energy exchange with the interacting field.

### 11.4 Boundary And Off-Shell Subtleties

The conservation proof assumes:

- compactly supported diffeomorphism generators, or boundary conditions that remove surface terms
- matter equations of motion are satisfied
- all interacting subsystems that exchange energy and momentum are included in the total matter action
- any gauge constraints and worldline constraints are handled consistently

Off shell, or for an open subsystem, $\nabla_\mu T^{\mu\nu}$ need not vanish. The correct statement is that the total stress-energy tensor derived from a diffeomorphism-invariant matter action is covariantly conserved on shell.

This completes the H4 conservation derivation needed for the scalar, electromagnetic, and point-particle phase-response slices.

## 12. H4 Summary Report

### Verdict

H4 is **accepted with limits** for the standard matter systems checked here.

The accepted result is conservative:

- the standard inverse-metric stress-energy definition is recovered
- scalar-field, electromagnetic-field, and point-particle tensors have the expected signs
- energy density, momentum density, pressure, momentum flux, and anisotropic stress appear as tensor components
- covariant conservation follows on shell from diffeomorphism invariance
- open subsystems are allowed to exchange energy and momentum, so only the total interacting stress-energy tensor must be conserved
- `tests/test_h4_stress_energy_phase_response.py` protects the main sign and component conventions with lightweight executable checks

### Evidence

| Matter system or property | Result | Section |
|---|---|---|
| Shared phase-response identity | $T_{\mu\nu}=-(2\hbar/\sqrt{-g})\delta\Theta_{\mathrm{m}}/\delta g^{\mu\nu}$ | Sections 1 and 5 |
| Scalar field | Standard minimally coupled scalar stress-energy recovered | Sections 3 through 6 |
| Electromagnetic field | Standard Maxwell stress-energy recovered, gauge invariant and traceless | Sections 7 and 8 |
| Point particle | Standard distributional worldline stress-energy recovered | Sections 9 and 10 |
| Conservation | $\nabla_\mu T^{\mu\nu}=0$ recovered on shell from diffeomorphism invariance | Section 11 |
| Executable sign checks | Phase-response sign, scalar pressure/stress, electromagnetic anisotropic stress, Poynting flux, and point-particle momentum flux covered | `tests/test_h4_stress_energy_phase_response.py` |

### Standard Identity Versus Pulse Model Interpretation

The standard identity is:

$$
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

The Pulse Model rewrite is:

$$
T_{\mu\nu}=-\frac{2\hbar}{\sqrt{-g}}\frac{\delta\Theta_{\mathrm{m}}}{\delta g^{\mu\nu}}
$$

These equations are mathematically equivalent because $S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}$. The new language is interpretive: stress-energy is matter phase-response to the metric. It is not a new tensor and not a changed coupling rule.

This separation matters. H4 does not prove that the Einstein-Hilbert action follows from pulse consistency. It supplies the matter-side source tensor that any geometry-action derivation must couple to.

### Geometry-Action Readiness

H4 can feed the geometry-action gate as a reviewed matter-side input:

- the source tensor is the standard $T_{\mu\nu}$
- the source tensor includes pressure and stress, not only mass density
- conservation is compatible with diffeomorphism invariance
- interacting subsystems must be treated as a conserved total

H4 does not by itself determine the geometric phase functional. The geometry-action work must still explain why the metric variation of the geometric side produces the Einstein tensor, what boundary terms are required, and how the Newtonian limit is recovered.

### Remaining Boundaries

This appendix is enough for the current H4 acceptance gate, but it does not cover every matter model. Fluids, spinor fields, nonminimal curvature couplings, quantum expectation values, anomalies, and renormalized vacuum stress-energy remain downstream or specialized work.

For Step 0 known-physics validation, the stress-energy gap can now be reviewed against this appendix: the standard action-variation convention, signs, units, pressure/stress components, and conservation assumptions are all explicit.
