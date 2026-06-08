---
title: H3 Pulse-Comparison Holonomy
sidebar_label: H3 Curvature Holonomy
sidebar_position: 4
---

# Appendix: H3 Pulse-Comparison Loop Observable

**Parent hypothesis:** 6.3 Hypothesis H3: Curvature is pulse-comparison holonomy  
**Status:** Accepted with limits for the first fixed-event or gauge-fixed curvature-holonomy slice  
**Purpose:** Define a closed-loop pulse and synchronization residual that can be measured from clock and signal records, derive how the corrected infinitesimal frame closure carries curvature tensor content, and provide first executable checks without assuming curvature as an input.

---

## 1. Boundary

H3 starts from the bounded H2 result: a loop protocol may use a fixed-event or explicitly gauge-fixed reconstructed metric object as context, but the observable itself must be built from operational records.

The observable may use:

- calibrated pulse counts
- signal emission and reception labels
- local phase, frequency, and direction readings
- local accelerometer and gyroscope readings
- instrument delay and calibration records
- meeting events or reflected signals that identify loop vertices

The observable must not use:

- coordinate event positions as observations
- coordinate time as an observed clock
- metric components as direct observations
- a connection or curvature tensor as an input correction
- an assumed result that the loop residual is already Riemann curvature

The observable definition supplies the protocol. The derivation below supplies the conditional small-loop relation between the corrected frame closure and curvature.

## 2. Loop Record

Let a closed loop be a cyclic list of clock stations:

$$
L=(C_0,C_1,\ldots,C_{m-1},C_m)
$$

with:

$$
C_m=C_0
$$

Each station has a calibrated pulse counter. Its local operational time reading at an event $e$ is:

$$
T_i(e)=\frac{N_i(e)-N_i(e_{i,0})}{f_i}
$$

Here $N_i$ is the pulse count, $f_i$ is the calibrated transition frequency, and $e_{i,0}$ is an arbitrary local zero event. The arbitrary zero is not physical. A valid loop residual must cancel all choices of $e_{i,0}$.

Neighboring stations exchange labeled signals. For each edge $C_i\to C_{i+1}$, the minimal two-way record is:

- $e_{i,i+1}$: emission event on $C_i$
- $r_{i,i+1}$: reception event on $C_{i+1}$
- $e_{i+1,i}$: return emission or reflection event on $C_{i+1}$
- $r_{i+1,i}$: return reception event on $C_i$

The return event can be an active retransmission or a calibrated reflection. Its local delay at $C_{i+1}$ is estimated by:

$$
\widehat{\rho}_{i+1}=T_{i+1}(e_{i+1,i})-T_{i+1}(r_{i,i+1})
$$

The edge synchronization offset assigned by $C_i$ to $C_{i+1}$ is:

$$
\sigma_{i,i+1}=T_{i+1}(r_{i,i+1})-\frac{T_i(e_{i,i+1})+T_i(r_{i+1,i})-\widehat{\rho}_{i+1}}{2}-\widehat{\alpha}_{i,i+1}
$$

The term $\widehat{\alpha}_{i,i+1}$ is the estimated one-way asymmetry correction for that edge. It is zero for a symmetric vacuum link between inertial stations in flat spacetime. In real records it may include calibrated propagation asymmetry, media effects, station motion during the exchange, or known reflection electronics.

This definition uses only local clock readings and signal labels. It does not require assigning a coordinate time to the reception event.

## 3. Scalar Synchronization Closure

The raw scalar loop residual is the sum of edge offsets around the loop:

$$
\Delta T_{\mathrm{raw}}(L)=\sum_{i=0}^{m-1}\sigma_{i,i+1}
$$

If every clock zero is shifted by a constant:

$$
T_i\mapsto T_i+b_i
$$

then each edge offset shifts by:

$$
\sigma_{i,i+1}\mapsto\sigma_{i,i+1}+b_{i+1}-b_i
$$

The loop sum is unchanged because the shifts telescope around the closed loop:

$$
\sum_{i=0}^{m-1}(b_{i+1}-b_i)=0
$$

So $\Delta T_{\mathrm{raw}}(L)$ is independent of arbitrary clock zero choices. A dimensionless pulse-count form can be defined with any stated reference frequency $f_\star$:

$$
\Delta N_{\mathrm{loop}}(L)=f_\star\Delta T_{\mathrm{raw}}(L)
$$

The reference frequency only changes the unit used to report the residual. It does not change whether the loop closes.

## 4. Corrected H3 Residual

The H3 residual is the raw loop closure after subtracting non-curvature artifacts that are measured or calibrated independently:

$$
\Delta T_{\mathrm{H3}}(L)=\Delta T_{\mathrm{raw}}(L)-\widehat{\Delta T}_{\mathrm{art}}(L)
$$

The artifact model is not allowed to contain curvature as a fitted input. It may contain independently measured or controlled quantities:

$$
\widehat{\Delta T}_{\mathrm{art}}=\Delta T_{\mathrm{cal}}+\Delta T_{\mathrm{sig}}+\Delta T_{\mathrm{acc}}+\Delta T_{\mathrm{rot}}+\Delta T_{\mathrm{inst}}+\Delta T_{\mathrm{finite}}
$$

where:

- $\Delta T_{\mathrm{cal}}$ covers clock calibration error, drift, and environmental frequency shifts
- $\Delta T_{\mathrm{sig}}$ covers media delay, multipath, reflection delay, antenna delay, and signal species effects
- $\Delta T_{\mathrm{acc}}$ covers non-gravitational acceleration of the stations, measured by accelerometers
- $\Delta T_{\mathrm{rot}}$ covers rotation and Sagnac-type effects, measured by gyroscopes or by an independently specified platform motion model
- $\Delta T_{\mathrm{inst}}$ covers local electronics, phase-wrap, timestamping, and readout biases
- $\Delta T_{\mathrm{finite}}$ covers finite loop size, finite light-time, and failure to compare events in the intended infinitesimal limit

A nonzero raw loop sum is therefore not automatically curvature. It is H3 evidence only after the correction ledger is stated and bounded.

## 5. Tensor-Ready Frame Closure

The scalar closure is the minimum pulse-count observable. It is not by itself enough to recover all components of curvature. For the H3 curvature task, the same loop record should also support a frame-closure observable.

Attach a calibrated local orthonormal frame or instrument frame $E_i$ to each station event. Direction, polarization, frequency-ratio, accelerometer, and gyroscope records define an operational edge transport map:

$$
\Lambda_{i,i+1}:E_i\to E_{i+1}
$$

This map is a data product of the edge comparison protocol. It is not assumed to be Levi-Civita parallel transport. Known non-gravitational acceleration, station rotation, and instrument offsets are corrected before forming the loop map.

The closed-loop frame residual is:

$$
\mathcal{H}_L=\Lambda_{m-1,0}\Lambda_{m-2,m-1}\cdots\Lambda_{0,1}
$$

For a small loop close to the identity, report the generator:

$$
\mathcal{K}_L=\log\mathcal{H}_L
$$

The curvature relation is not put into the definition of $\Lambda_{i,i+1}$. It is derived only after assuming a smooth fixed-event metric limit and independently corrected edge transports.

## 6. Smooth Transport Limit

For the curvature derivation, assume the corrected edge maps approach Levi-Civita parallel transport for the smooth metric object supplied by the bounded H2 result. This is an extra smooth-limit assumption, not part of the raw observable definition.

For a vector $V^\rho$ transported along a small displacement $dx^\mu$:

$$
dV^\rho=-\Gamma^\rho{}_{\sigma\mu}V^\sigma dx^\mu
$$

Equivalently:

$$
\nabla_\mu V^\rho=0
$$

The curvature tensor is defined by the commutator of covariant derivatives:

$$
(\nabla_\mu\nabla_\nu-\nabla_\nu\nabla_\mu)V^\rho=R^\rho{}_{\sigma\mu\nu}V^\sigma
$$

This equation is not an observation. It is the smooth geometric identity that connects a transport rule to the infinitesimal failure of transport around a closed loop.

Consider a small loop based at event $p$ with tangent directions $u^\mu$ and $v^\mu$, side parameters $\epsilon$ and $\eta$, and orientation $u$ then $v$ then $-u$ then $-v$. Its area bivector is:

$$
A^{\mu\nu}=\frac{1}{2}\epsilon\eta(u^\mu v^\nu-v^\mu u^\nu)
$$

Using the commutator identity, the corrected loop transport acts on $V^\rho$ as:

$$
(\mathcal{H}_L{}^\rho{}_\sigma-\delta^\rho{}_\sigma)V^\sigma=R^\rho{}_{\sigma\mu\nu}V^\sigma A^{\mu\nu}+O(\ell^3)
$$

Here $\ell$ is the characteristic loop size. Reversing the loop orientation reverses the sign of $A^{\mu\nu}$ and therefore reverses the sign of the leading holonomy.

Since $\mathcal{H}_L=I+O(\ell^2)$ for a small loop, its logarithm has the same leading term:

$$
\mathcal{K}_L{}^\rho{}_\sigma=R^\rho{}_{\sigma\mu\nu}A^{\mu\nu}+O(\ell^3)
$$

In the local orthonormal frame of the base station this becomes:

$$
\mathcal{K}_L{}^{\hat a}{}_{\hat b}=R^{\hat a}{}_{\hat b\hat c\hat d}A^{\hat c\hat d}+O(\ell^3)
$$

This is the H3 holonomy-curvature relation. The loop protocol measures $\mathcal{K}_L$ and the oriented loop area supplied by the fixed-event or gauge-fixed reconstruction. The curvature tensor is the infinitesimal density that explains the leading corrected frame closure.

## 7. Scalar Residual As A Projection

The scalar synchronization residual $\Delta T_{\mathrm{H3}}(L)$ is not the full curvature tensor. It is a protocol-dependent projection of the tensor-ready frame closure onto clock synchronization, frequency comparison, or phase comparison channels.

For a small loop, its leading form can only be:

$$
\Delta T_{\mathrm{H3}}(L)=\mathcal{P}^{\hat b}{}_{\hat a}R^{\hat a}{}_{\hat b\hat c\hat d}A^{\hat c\hat d}+O(\ell^3)+\epsilon_{\mathrm{model}}
$$

where $\mathcal{P}^{\hat b}{}_{\hat a}$ is the stated sensitivity of the chosen pulse-comparison protocol and $\epsilon_{\mathrm{model}}$ is the remaining bounded artifact or fitting error. Different loop orientations, transported axes, signal polarizations, and clock-comparison channels are needed to recover different curvature components.

This is why H3 must keep the frame closure $\mathcal{K}_L$ as the main tensor-ready observable. A scalar loop time residual can confirm selected curvature projections, but it cannot by itself establish the full Riemann tensor.

## 8. Geodesic-Deviation Signal

An equivalent local curvature signal comes from neighboring freely falling clock worldlines. Let $U^{\hat a}$ be the reference clock four-velocity and let $\xi^{\hat i}$ be a small spatial separation in the clock's local Fermi frame. For freely falling clocks:

$$
\frac{d^2\xi^{\hat i}}{d\tau^2}=-R^{\hat i}{}_{\hat 0\hat j\hat 0}\xi^{\hat j}
$$

Over a short proper-time interval $\Delta\tau$, the relative displacement signal is:

$$
\delta\xi^{\hat i}=-\frac{1}{2}R^{\hat i}{}_{\hat 0\hat j\hat 0}\xi^{\hat j}(\Delta\tau)^2+O((\Delta\tau)^3)
$$

Pulse ranging between the clocks can measure this local tidal projection without assigning coordinate components to the clock positions. This is not a separate definition of curvature; it is the same tensor content sampled through a geodesic-deviation protocol rather than a closed frame-transport protocol.

## 9. Flat-Spacetime Expectation

In simply connected Minkowski spacetime with inertial stations, calibrated clocks, vacuum signals, symmetric propagation, and fixed instrument delays:

$$
\widehat{\Delta T}_{\mathrm{art}}(L)=0
$$

Each edge offset has the form:

$$
\sigma_{i,i+1}=b_{i+1}-b_i
$$

where $b_i$ is the arbitrary clock zero offset. Therefore:

$$
\Delta T_{\mathrm{H3}}(L)=0
$$

and, for the frame observable:

$$
\mathcal{H}_L=I
$$

$$
\mathcal{K}_L=0
$$

Flat spacetime has $R^\rho{}_{\sigma\mu\nu}=0$, so the small-loop relation also gives:

$$
\mathcal{K}_L=O(\ell^3)
$$

Flat spacetime can still produce a nonzero raw residual if the stations accelerate, rotate, sit on a noninertial platform, use asymmetric media, or have unmodeled delays. Those are protocol artifacts. A valid H3 simulation must show that the corrected residual vanishes in flat spacetime when those effects are supplied to the correction model.

## 10. What H3 Measures

H3 does not measure coordinate components of $R^\rho{}_{\sigma\mu\nu}$ directly.

It measures:

- finite loop frame closure $\mathcal{H}_L$
- small-loop generator $\mathcal{K}_L$ when the loop is close to identity
- scalar timing or phase projections such as $\Delta T_{\mathrm{H3}}(L)$
- geodesic-deviation projections such as $R^{\hat i}{}_{\hat 0\hat j\hat 0}\xi^{\hat j}$

Changing the base frame relabels $\mathcal{H}_L$ by conjugation and relabels the components of $\mathcal{K}_L$. That is a frame change, not a change in the physical loop closure. The physical content is the action of the corrected loop map on specified local instruments and the way that action scales with the oriented loop area.

Thus the accepted derivation is conditional:

- if the corrected edge maps converge to Levi-Civita transport for the smooth H2 metric object
- if the loop is small compared with curvature and nuisance-variation scales
- if acceleration, rotation, signal, and instrument artifacts are independently modeled

then the leading density of the corrected frame closure is Riemann curvature.

## 11. Executable First-Slice Simulations

The first executable H3 simulation lives in `src/pulse_model/h3_holonomy.py`, with tests in `tests/test_h3_holonomy.py`.

It has three deliberately small pieces:

- `corrected_loop_residual_s` checks the artifact-ledger rule $\Delta T_{\mathrm{H3}}=\Delta T_{\mathrm{raw}}-\widehat{\Delta T}_{\mathrm{art}}$.
- `simulate_frame_loop_holonomy` checks the local leading-order spatial frame closure $\mathcal{K}\sim R A$ for a stated curvature density and oriented loop area.
- `schwarzschild_tidal_ranging_residual_m` checks the geodesic-deviation projection for a Schwarzschild weak-field tidal setup.

The flat benchmark verifies that modeled artifacts can remove a raw timing residual and that zero curvature gives a zero frame generator:

$$
\mathcal{K}_L=0
$$

The frame-loop benchmark verifies linear scaling:

$$
\mathcal{K}_{ij}=\kappa A
$$

where $\kappa$ is the supplied sectional curvature density and $A$ is the oriented loop area. Reversing the loop orientation reverses the sign of the generator.

This first simulation only accepts spatial frame axes. Time-space boost holonomies require an explicit Lorentz-signature generator convention and are left outside this helper rather than silently represented as ordinary spatial rotations.

The Schwarzschild tidal benchmark uses the local eigenvalues:

$$
\lambda_r=\frac{2GM}{r^3}
$$

$$
\lambda_\perp=-\frac{GM}{r^3}
$$

and verifies the short-time ranging residual:

$$
\delta\xi=\frac{1}{2}\lambda\xi(\Delta\tau)^2
$$

The radial residual is positive, the transverse residual is negative, and the magnitude scales linearly with separation and quadratically with elapsed proper time.

These simulations do not yet implement a general path-ordered transport solver through an arbitrary metric. They verify the local H3 scaling laws and the flat-spacetime artifact boundary needed before the H3 acceptance report.

## 12. Assumptions For The First H3 Slice

The first H3 observable assumes:

- the loop vertices are identified by meeting events, reflected signals, or the bounded H2 fixed-event/gauge-fixed reconstruction
- all participating clocks are locally calibrated to a common time unit
- signal labels correctly pair emissions, receptions, and returns
- loop orientation is recorded
- local direction and acceleration records are optional for the scalar residual but required for tensor-ready frame closure
- correction terms are stated separately from the residual they correct
- corrected edge transports converge to smooth Levi-Civita transport only in the ideal small-loop limit
- the loop area bivector is supplied by the fixed-event or gauge-fixed reconstructed metric object, not by raw coordinate observations
- unresolved multipath, caustics, topology ambiguity, or missing clock calibration invalidates the curvature interpretation

This is deliberately narrower than the full H3 claim. It defines a measurement target that can be simulated and then related to curvature in later tasks.

## 13. Acceptance Report

### Verdict

H3 is **accepted with limits** for the first fixed-event or gauge-fixed slice.

Accepted:

- a coordinate-independent closed-loop pulse-comparison observable built from calibrated pulse counts, signal records, and local correction records
- a tensor-ready frame-closure observable $\mathcal{H}_L$ and small-loop generator $\mathcal{K}_L$
- the conditional smooth-limit relation $\mathcal{K}_L{}^{\hat a}{}_{\hat b}=R^{\hat a}{}_{\hat b\hat c\hat d}A^{\hat c\hat d}+O(\ell^3)$
- scalar timing residuals as protocol-dependent projections, not as the full curvature tensor
- geodesic deviation as an equivalent local tidal projection
- first executable checks for flat corrected closure, curvature-area scaling, orientation reversal, and Schwarzschild tidal scaling

Not accepted:

- automatic curvature recovery from arbitrary sparse raw pulse records
- a general path-ordered transport solver through arbitrary metrics
- recovery of all Riemann tensor components from one scalar timing loop
- use of unmodeled acceleration, rotation, media, instrument delay, or finite-loop effects as curvature evidence

### Evidence

| Requirement | Evidence | Decision |
|---|---|---|
| Coordinate-independent observable | Sections 2-5 define loop records, scalar closure, corrected residuals, and frame closure from local clock/signal/instrument records rather than coordinate observations. | Accepted for fixed-event or gauge-fixed H2 input. |
| Artifact separation | Section 4 separates calibration, signal, acceleration, rotation, instrument, and finite-loop corrections from the H3 residual. | Accepted with stated correction-ledger requirement. |
| Flat-spacetime expectation | Section 9 derives zero corrected scalar and frame residuals for inertial flat spacetime; `tests/test_h3_holonomy.py` verifies corrected flat timing closure and zero flat frame generator. | Accepted for the first executable slice. |
| Holonomy-curvature relation | Section 6 derives the small-loop relation between corrected frame closure, loop area, and Riemann curvature. | Accepted conditionally on the smooth Levi-Civita transport limit. |
| Curved benchmark | Section 11 and `tests/test_h3_holonomy.py` verify curvature-area scaling, orientation reversal, and Schwarzschild geodesic-deviation scaling. | Accepted as a first curved benchmark, not as exhaustive metric coverage. |
| Protocol projection boundary | Sections 7, 8, and 10 state that scalar timing and ranging channels measure projections of curvature, while frame closure is the tensor-ready object. | Accepted. |

### Geometry-Action Use

H3 can feed the geometry-action gate as a bounded input:

$$
\mathcal{K}_L{}^{\hat a}{}_{\hat b}\Rightarrow R^{\hat a}{}_{\hat b\hat c\hat d}A^{\hat c\hat d}
$$

The accepted input is not that pulse records alone derive the Einstein-Hilbert action. It is the narrower result that corrected local loop-comparison holonomy supplies a curvature observable in the smooth small-loop limit. The geometry-action gate must still justify how tensorial curvature data become a local scalar phase density such as $R\sqrt{-g}$, and why competing higher-curvature or nonlocal pulse-consistency costs are excluded or suppressed.

### Remaining Boundaries

Before stronger H3 claims are made, later work would need:

- finite-loop error bounds beyond the $O(\ell^3)$ statement
- simulations of path-ordered transport through nonconstant curvature fields
- explicit Lorentz-signature handling for time-space or boost holonomy generators
- recovery of multiple independent curvature components from a network of loop orientations and transported axes
- raw-relational event and signal identifiability beyond the bounded H2 start condition
- explicit noise, calibration, and nuisance-parameter covariance for experimental loop networks

These are downstream strengthenings. They do not block using the accepted first H3 slice as a curvature-holonomy input for geometry-action candidate work.

## 14. Acceptance For Observable, Derivation, And Simulation Tasks

This appendix accepts the following limited result:

> A coordinate-independent closed-loop pulse-comparison observable can be defined from calibrated pulse counts, signal exchanges, and local correction records. In the smooth small-loop limit, the corrected frame-closure generator satisfies $\mathcal{K}_L{}^{\hat a}{}_{\hat b}=R^{\hat a}{}_{\hat b\hat c\hat d}A^{\hat c\hat d}+O(\ell^3)$. The scalar timing residual is a protocol-dependent projection, and geodesic deviation supplies an equivalent local tidal projection. First executable simulations verify flat corrected closure, curvature-area scaling, orientation reversal, and Schwarzschild tidal geodesic-deviation scaling. H3 is accepted with limits as a first curvature-holonomy input for geometry-action work.

The next proof move is the geometry-action candidate task, which must explain how accepted H3 curvature-holonomy data and H4 matter phase-response constrain a geometric phase functional.
