# Appendix: 05S Geometry Action Strengthening From Pulse Networks

**Parent hypothesis:** 05S, Strengthen geometry action from pulse-network continuum limit  
**Status:** 05S.9 decision complete: stronger conditional derivation; not a fundamental derivation from raw pulse data  
**Purpose:** Make the hidden geometry-action assumptions from 05 explicit by defining the admissible pulse-network continuum limit and the proof obligations needed before pulse consistency can honestly be claimed to select the Einstein-Hilbert phase.

---

## 1. Boundary

The closed 05 appendix, `geometry_phase_functional_from_pulse_consistency.md`, accepted the Einstein-Hilbert plus cosmological-constant phase only as a conservative low-energy result with explicit limits. It did not prove that raw pulse data force locality, scalarization to $R$, refinement invariance, suppression of higher-curvature corrections, or full Lorentzian Regge boundary behavior.

05S is the strengthening lane for exactly those missing assumptions. It may use accepted H2 and H3 inputs within their stated limits, and it may compare against the 05 candidate, but it must keep the following layers separate:

- observed finite pulse records
- reconstructed H2 metric and local frame data
- corrected H3 loop holonomy observables
- pulse-cell descriptions used for coarse graining
- continuum geometry-action claims

The target is not to restate the 05 low-energy uniqueness route. The target is to determine whether admissible pulse networks supply enough structure to justify the assumptions that 05 had to leave conditional.

## 2. Inputs Carried From Earlier Gates

### 2.1 H2 Metric Input

H2 supplies a bounded fixed-event or gauge-fixed metric reconstruction input:

$$
\mathcal{D}_{\mathrm{pulse}}\Rightarrow [g_{\mu\nu}]
$$

In 05S this means:

- a smooth event-region representation may be used only as a reconstructed or fixed-event scaffold
- metric areas, volumes, causal order, and local orthonormal frames may be used only inside the H2 scope
- arbitrary sparse raw records are not assumed to reconstruct a smooth metric
- coordinate labels are gauge, not observations

The H2 input does not by itself give a local action. It gives the candidate smooth geometry on which locality, scalarization, and refinement questions can be asked.

### 2.2 H3 Holonomy Input

H3 supplies a corrected local frame-closure observable:

$$
\mathcal{K}_L{}^{\hat a}{}_{\hat b}=R^{\hat a}{}_{\hat b\hat c\hat d}A^{\hat c\hat d}+O(\ell^3)
$$

within the accepted small-loop, fixed-event or gauge-fixed smooth-limit slice. In 05S this means:

- $\mathcal{K}_L$ is the tensor-ready observable
- scalar timing residuals are only protocol-dependent projections
- acceleration, rotation, signal, instrument, and finite-loop corrections remain in a separate correction ledger
- time-space boost holonomies are not yet executable in H3 and must remain conditional until conventions and tests are supplied

The H3 input does not by itself give the scalar curvature $R$. It supplies local curvature tensor samples that must still be contracted, averaged, and shown to be independent of pulse-network scaffolding.

### 2.3 05 Geometry-Action Input

The accepted 05 result supplies the conditional low-energy candidate:

$$
\Theta_{\mathrm{geom}}^{(0)}[g]=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x
$$

05S must not treat this as already derived from pulse data. It is the comparison target and downstream conservative fallback. A stronger 05S result must remove or control the exact assumptions that 05 left open.

## 3. Observed, Reconstructed, And Forbidden Data

### 3.1 Observed Records

The finite observed record for a pulse network contains only local and relational data:

- clock identifiers and calibrated transition types
- ordered pulse counts on each clock
- signal emission, reception, return, and reflection labels
- meeting-event labels when two local records are identified operationally
- local frequency, phase, direction, polarization, accelerometer, gyroscope, and instrument-delay records when available
- loop orientation records and the order in which local stations are visited
- independent correction-ledger entries for known non-curvature artifacts

These are the data that may be called observations.

### 3.2 Reconstructed Objects

The following objects may be reconstructed from observed records, accepted earlier gates, and stated smooth-limit assumptions:

- event-region representations up to diffeomorphism
- metric class and local Lorentz frames within the H2 scope
- loop area bivectors and cell volumes within the H2 scope
- corrected H3 frame-closure generators
- local curvature samples in the H3 small-loop limit
- pulse-cell complexes used as coarse-graining descriptions

These are not primitive observations. Every use must remain traceable to H2, H3, or an explicit 05S assumption.

### 3.3 What Must Not Be Assumed

05S must not assume:

- a coordinate lattice as physical structure
- station labels, clock zero choices, or arbitrary loop labels as action data
- a universal pulse count, preferred foliation, preferred frame, or preferred loop-plane distribution
- that a scalar timing residual is the full curvature tensor
- that a squared reconstruction loss is automatically a physical phase
- that locality, scalarization, refinement invariance, or higher-curvature suppression has already been proved by 05

If any of these structures survives into the continuum action, the result is a controlled modification or failure of the strong Einstein-Hilbert derivation, not a stronger derivation.

## 4. Admissible Finite Pulse Networks

An admissible finite pulse network at resolution scale $\ell_n$ is a record package:

$$
\mathcal{P}_n=(E_n,C_n,S_n,I_n,F_n,L_n,A_n,Q_n)
$$

where:

- $E_n$ is a finite set of operationally identified events, such as meetings, emissions, receptions, and reflections
- $C_n$ is a finite set of clock segments with ordered calibrated pulse-count records
- $S_n$ is a finite set of labeled signal links between clock events
- $I_n$ is the incidence data connecting clocks, signals, and events
- $F_n$ is the available local frame and instrument data
- $L_n$ is a finite family of oriented loop records
- $A_n$ is the independent artifact and calibration correction ledger
- $Q_n$ is the stated quality metadata, including uncertainty bounds, missing channels, and scale estimates

The network is admissible for 05S only if the following conditions are met.

### 4.1 Incidence And Clock Regularity

Signal and meeting labels must consistently pair local events. Clock pulse records must be calibrated to an operational time unit within the earlier H1 and H2 limits. Clock zero choices must cancel from loop and cell quantities.

### 4.2 Causal And Metric Regularity

There must be at least one H2-compatible smooth Lorentzian reconstruction on the region being studied. The local signal and clock data must be rich enough to define the relevant loop areas, hinge areas, cell volumes, and local frames to the required accuracy.

### 4.3 Correction-Ledger Separation

Known non-curvature effects must remain separated from the H3 residuals:

$$
\Delta_{\mathrm{H3}}=\Delta_{\mathrm{raw}}-\widehat{\Delta}_{\mathrm{art}}
$$

The artifact model may use independently measured calibration, media, acceleration, rotation, finite-loop, and instrument data. It may not fit a curvature tensor and then call the remaining residual curvature evidence.

### 4.4 Loop Orientation And Local Frames

Each loop used for geometry-action work must carry:

- an orientation
- a base local frame or a stated frame-comparison convention
- an H2-derived area bivector
- a corrected H3 frame generator when tensor information is needed
- an uncertainty or finite-loop error estimate

Changing local Lorentz frame components may relabel tensors, but it must not change scalar hinge defects or final continuum densities.

### 4.5 Scale Separation

The characteristic loop, cell, and correction scales must satisfy:

$$
\ell_{\mathrm{clock}}\leq \ell_{\mathrm{loop}}\leq \ell_{\mathrm{cell}}\ll L_R
$$

where $L_R$ is the local curvature-variation scale in the reconstructed H2 geometry. This is a working regularity condition, not a derived fact. Later 05S tasks must say what fails when the hierarchy is absent.

## 5. Pulse-Cell Complexes

A pulse-cell complex $\mathcal{C}_n$ is a coarse-graining description of an admissible pulse network. It is not a physical lattice unless replacement-invariance fails.

It contains:

- cells $\sigma$ covering the reconstructed region $U_n$
- codimension-two hinges $h$ where curvature defects are assigned
- boundary cells and boundary hinges when $U_n$ has a boundary
- oriented loop families $L_{h,k}$ linking or probing each hinge
- H2-derived volumes $V_\sigma$ and hinge areas $A_h$
- local Lorentz bivectors $B_h$ normal to hinges where the H3 generator is contracted

The complex is admissible only if every geometric object used in the action candidate is either observed, reconstructed from H2/H3 within scope, or declared as a 05S assumption. It must not carry station labels or arbitrary cell labels into the continuum action.

## 6. Refinement Maps And Continuum Limit

A refinement sequence is a family:

$$
\mathcal{P}_n\to\mathcal{P}_{n+1}
$$

with associated pulse-cell complexes:

$$
\mathcal{C}_n\to\mathcal{C}_{n+1}
$$

The sequence is admissible when:

- incidence data are preserved or resolved into finer incidence data without changing already observed coarse events
- calibrated pulse intervals converge to the same H2 proper-time assignments where both resolutions overlap
- signal and frame records refine the same local causal and frame structure
- loop families shrink in physical H2 size while remaining rich enough to sample local two-planes
- correction-ledger terms either converge, are subtracted with bounded residuals, or are carried as explicit corrections
- boundary data converge to the same induced boundary geometry when a finite region is varied

The continuum limit is a smooth Lorentzian limit inherited from H2 and H3:

$$
(\mathcal{P}_n,\mathcal{C}_n)\to(U,[g],\mathcal{K}_L)
$$

This notation means convergence of the reconstructed metric object and corrected local holonomy samples, not convergence of coordinate labels.

## 7. Gauge Freedoms

05S must quotient or cancel the following gauge freedoms:

- diffeomorphism freedom in the reconstructed event-region representation
- local Lorentz frame rotations and boosts at each station or cell
- clock zero choices
- station and signal identifier relabelings
- pulse-cell subdivision labels
- loop-basis choices that span the same local two-plane information
- boundary chart choices

An expression is admissible as a geometry-action candidate only if it is unchanged by these replacements, except for known boundary terms or correction terms that are explicitly tracked.

## 8. Proof Obligations Created By 05S.1

The admissible-object definition turns the missing 05 assumptions into concrete obligations.

### 8.1 Locality And Additivity

Prove or bound when the smooth pulse-consistency phase has the form:

$$
\Theta_{\mathrm{pc}}=\sum_{\sigma\in\mathcal{C}_n}\Theta_\sigma+\sum_{h\in\mathcal{C}_n}\Theta_h+\Theta_{\partial U}+\Theta_{\mathrm{corr}}
$$

rather than an unsuppressed nonlocal functional of the entire pulse network.

Required inputs include record density, causal regularity, finite correlation length or screening assumptions, correction-ledger bounds, and boundary-flux accounting.

### 8.2 Scalarization

Prove or falsify when unbiased local sampling of H3 frame holonomies gives the scalar curvature density:

$$
R\sqrt{-g}
$$

rather than protocol-dependent projections, anisotropic contractions, or curvature-squared densities.

Required inputs include a loop-plane measure, Lorentzian orientation signs, local bivector contractions, and a rule excluding preferred loop distributions.

### 8.3 Refinement And Replacement Invariance

Show that changing cell decomposition, loop basis, station labels, or refinement path leaves the continuum phase unchanged up to boundary terms and controlled corrections.

This is the point where pulse cells stop being a preferred lattice and become only a description of the same geometry.

### 8.4 Correction Suppression Or Classification

Classify higher-curvature, torsion, anisotropic, finite-loop, nonlocal, and lattice-memory terms as:

- suppressed corrections
- controlled modifications with new scales
- fatal ambiguities that block a stronger 05 result

05S must not hide these terms inside statistical reconstruction error. Statistical losses estimate geometry from data; physical phase terms determine the source-to-metric response.

## 9. 05S.1 Outcome

05S.1 defines the mathematical object that later 05S tasks study: an admissible finite pulse network, its pulse-cell complex, refinement maps, loop families, local frame data, H2/H3 smooth-limit inputs, gauge freedoms, and proof obligations.

Accepted for downstream 05S tasks:

- observed records are local pulse, signal, incidence, frame, and correction-ledger data
- H2 metric objects and H3 frame holonomies may be used only within their accepted limits
- pulse-cell complexes are coarse-graining descriptions, not physical lattices unless replacement invariance fails
- locality, scalarization, refinement invariance, and correction suppression are explicit proof obligations

Not accepted by 05S.1:

- a derivation of the Einstein-Hilbert phase
- full Lorentzian hinge-defect coverage
- local additivity of the pulse-consistency phase
- unbiased scalarization to $R$
- refinement independence
- suppression of higher-curvature, torsion, anisotropic, or nonlocal corrections

The next 05S task may now use this admissible-object definition to derive or bound Lorentzian hinge defects from H3 frame holonomies.

## 10. 05S.2 Lorentzian Hinge Defects From H3 Holonomies

05S.2 asks whether the tensor-ready H3 frame closure can supply the discrete defects needed by a Lorentzian pulse-Regge candidate.

The answer is conditional but useful: for non-null hinges with a stated local Lorentz convention, the corrected H3 generator projects onto the hinge normal bivector to give the rotation angle or boost rapidity around that hinge. This is enough to define the formal pulse-Regge defect used by later 05S tasks. It is not yet full executable Lorentzian coverage, because H3 has only executable spatial-plane checks.

### 10.1 Local Lorentz Generator Convention

Use local orthonormal frame indices $\hat a,\hat b,\ldots$ with signature:

$$
\eta_{\hat a\hat b}=\mathrm{diag}(-1,1,1,1)
$$

The corrected H3 loop generator is first lowered into Lorentz-algebra form:

$$
\mathcal{K}_{L\hat a\hat b}=\eta_{\hat a\hat c}\mathcal{K}_L{}^{\hat c}{}_{\hat b}
$$

For Levi-Civita frame transport in the smooth H2 limit, it is antisymmetric:

$$
\mathcal{K}_{L\hat a\hat b}=-\mathcal{K}_{L\hat b\hat a}
$$

The H3 small-loop relation becomes:

$$
\mathcal{K}_{L\hat a\hat b}=R_{\hat a\hat b\hat c\hat d}A_L^{\hat c\hat d}+O(\ell_L^3)
$$

This is the object that may be projected onto a hinge. A scalar timing residual is not enough for this step.

### 10.2 Hinge Normal Bivector

For a non-null codimension-two hinge $h$, let $B_h^{\hat a\hat b}$ be the oriented unit bivector in the two-plane normal to the hinge. It is built from the H2 local metric and the chosen orientation convention. The hinge must have a nondegenerate normal plane.

The projected defect sampled by one loop $L_{h,k}$ is:

$$
\epsilon_{h,k}=\frac{1}{2}B_h^{\hat a\hat b}\mathcal{K}_{L_{h,k}\hat a\hat b}
$$

The factor $1/2$ avoids double-counting antisymmetric index pairs. The sign of $\epsilon_{h,k}$ is fixed jointly by the loop orientation and the hinge bivector orientation.

For a rotation-type normal plane, $\epsilon_{h,k}$ is an ordinary rotation angle. For a boost-type normal plane, $\epsilon_{h,k}$ is a boost rapidity. Both are dimensionless Lorentz-algebra parameters.

The coarse hinge defect is the weighted local estimate:

$$
\epsilon_h=\sum_k w_{h,k}\epsilon_{h,k}+\epsilon_{h,\mathrm{finite}}+\epsilon_{h,\mathrm{art}}
$$

where:

- $w_{h,k}$ are local reconstruction weights built from H2 geometry, loop orientation, and uncertainty data
- $\epsilon_{h,\mathrm{finite}}$ is the finite-loop truncation error
- $\epsilon_{h,\mathrm{art}}$ is any remaining bounded correction-ledger residual

The leading pulse-Regge term uses $A_h\epsilon_h$, where $A_h$ is the H2-derived hinge area.

### 10.3 Orientation And Sign Rules

The sign conventions must satisfy these checks.

Reversing loop orientation flips the H3 generator:

$$
\mathcal{K}_{-L\hat a\hat b}=-\mathcal{K}_{L\hat a\hat b}+O(\ell_L^3)
$$

Therefore:

$$
\epsilon_{h,k}(-L)=-\epsilon_{h,k}(L)+O(\ell_L^3)
$$

Reversing the hinge normal bivector also flips the projected defect:

$$
B_h^{\hat a\hat b}\mapsto -B_h^{\hat a\hat b}
$$

The discrete action must therefore carry a consistent orientation sign $s_h$ so that the product used in the hinge sum refers to an oriented geometric region, not to arbitrary loop-label choices:

$$
s_hA_h\epsilon_h
$$

Under a local Lorentz frame change $\Lambda^{\hat a}{}_{\hat b}$, both $\mathcal{K}_{L\hat a\hat b}$ and $B_h^{\hat a\hat b}$ transform tensorially. Their contraction is invariant. This is the key reason the hinge defect must be formed from the tensor-ready H3 frame closure rather than from a scalar synchronization channel.

### 10.4 Null And Timelike Caveats

The non-null hinge construction is the honest first target. Degenerate cases need extra conventions:

- a null hinge does not have a unique unit normal bivector without additional screen-space and null-normal normalization choices
- near-null hinges can amplify errors in the normal-bivector reconstruction
- timelike edges or mixed signature cells require a consistent Lorentzian simplex convention before signs can be compared across cells
- corners and boundary hinges require separate boundary and joint terms

05S may use non-null spacelike and timelike hinge interiors for the first pulse-Regge strengthening. It must not claim full null-boundary or null-hinge coverage until those conventions are supplied.

### 10.5 What Is Proved, Conditional, And Missing

Accepted for later 05S tasks:

- if H3 corrected frame transport converges to Levi-Civita transport for the H2 metric, then $\mathcal{K}_{L\hat a\hat b}$ is the local Lorentz generator carrying curvature content
- for a non-null hinge with an oriented normal bivector, $\frac{1}{2}B_h^{\hat a\hat b}\mathcal{K}_{L\hat a\hat b}$ is the hinge-normal rotation angle or boost rapidity sampled by that loop
- reversing loop orientation or hinge orientation flips the defect sign
- local Lorentz frame changes leave the bivector contraction invariant

Still conditional:

- H3 has executable spatial-plane rotation checks, not explicit time-space boost-holonomy checks
- finite-loop errors beyond the leading $O(\ell_L^3)$ statement are not yet bounded
- null hinges, null boundaries, and Lorentzian joints need extra normalization and sign conventions
- the weighted loop family around a hinge must still be shown to be unbiased and refinement-stable

Additional H3 or prototype work required for full Lorentzian coverage:

- an explicit $\mathrm{so}(1,3)$ generator helper that checks metric antisymmetry
- boost-plane tests for time-space holonomies and orientation reversal
- rejection or separate handling of null and near-null hinge normals
- a simple Lorentzian benchmark where the sign of a boost defect is independently known
- a boundary or joint sign convention compatible with the discrete action

### 10.6 05S.2 Outcome

05S.2 provides the formal bridge from H3 frame holonomies to Lorentzian pulse-Regge hinge defects:

$$
\epsilon_h=\sum_k w_{h,k}\frac{1}{2}B_h^{\hat a\hat b}\mathcal{K}_{L_{h,k}\hat a\hat b}+\epsilon_{h,\mathrm{finite}}+\epsilon_{h,\mathrm{art}}
$$

This bridge is strong enough to support the next 05S questions about locality, scalarization, refinement, and corrections. It does not yet upgrade 05, because unbiased loop sampling, local additivity, refinement invariance, and correction suppression remain unproved.

## 11. 05S.3 Locality And Additivity Of Pulse-Consistency Cost

05S.3 attacks the first major gap in the closed 05 result: why a pulse-consistency phase should become a sum of local cell and hinge terms rather than an unsuppressed nonlocal functional of the entire pulse network.

The honest result is a restricted sufficient-conditions theorem. Local additivity is not obtained from pulse records alone. It follows only if the admissible pulse-network refinement has local support, controlled correlations, local correction ledgers, and boundary-flux accounting.

### 11.1 Separate Estimator Loss From Physical Phase

Finite records often require a statistical reconstruction loss, for example:

$$
\mathcal{E}_{\mathrm{stat}}=(d-M[g])^TC^{-1}(d-M[g])
$$

where $d$ is a data vector, $M[g]$ is a model prediction, and $C$ is a covariance model. This object estimates a metric or nuisance parameters from noisy data. It is allowed to be nonlocal because instruments, clocks, and calibration errors can have correlated uncertainty.

The physical geometry phase is different. It is the object varied against the H4 matter phase to obtain source-to-metric response. 05S may not convert a nonlocal estimator covariance into a nonlocal physical action unless the model explicitly chooses a nonlocal gravity modification.

Thus 05S.3 studies locality of $\Theta_{\mathrm{pc}}$, not locality of every possible reconstruction algorithm.

### 11.2 Restricted Locality Theorem

Let $\mathcal{P}_n$ be an admissible pulse network with pulse-cell complex $\mathcal{C}_n$ and characteristic cell scale $\ell_n$. Suppose the following conditions hold on a region $U$.

**Record density.** Every compact subregion of $U$ contains enough clock, signal, frame, and loop data to reconstruct H2 metric quantities and H3 local frame closures at scale $\ell_n$, with bounded cell valence and no macroscopic holes in the loop family.

**Causal regularity.** Signal incidence is compatible with one smooth time-oriented Lorentzian H2 geometry, and local causal neighborhoods refine to local causal neighborhoods in the limit $\ell_n\to0$.

**Local correction ledger.** Calibration, media, acceleration, rotation, finite-loop, and instrument corrections decompose into cell-local pieces plus boundary flux terms and residuals bounded by the correction budget.

**Finite dependence range.** After conditioning on boundary data and conserved charges, the part of the pulse-consistency phase assigned to a cell star depends only on records inside a bounded neighboring cell star of physical radius $\xi_n$, with $\xi_n/L_R\to0$ in the continuum limit.

**Refinement regularity.** Refinement does not create a preferred long-range lattice memory. Cell diameters shrink, valence remains bounded, loop orientations become locally rich, and overlap regions carry compatible H2/H3 reconstructions.

Then the pulse-consistency phase has an additive local form up to boundary and controlled residual terms:

$$
\Theta_{\mathrm{pc}}[\mathcal{P}_n,U]=\sum_{h\subset U^\circ}\theta_h+\sum_{\sigma\subset U^\circ}\theta_\sigma+\Theta_{\partial U}+\Theta_{\mathrm{corr}}+\Theta_{\mathrm{nl}}
$$

with:

$$
\lim_{n\to\infty}\Theta_{\mathrm{nl}}=0
$$

or with $\Theta_{\mathrm{nl}}$ bounded by an explicitly retained correction scale. Here $U^\circ$ denotes the interior of $U$. The hinge terms may carry curvature defects, the cell terms may carry volume or cosmological terms, and $\Theta_{\partial U}$ carries boundary and flux data.

This theorem is conditional. The finite-dependence and refinement-regularity assumptions are the new physics assumptions that 05 had not proved.

### 11.3 Why The Theorem Is Plausible

Under the assumptions above, changing records inside one small cell star changes only:

- local H2 metric quantities in that cell star
- local H3 loop generators whose loops pass through or link that cell star
- correction-ledger entries supported in that cell star
- boundary flux entries if the cell star touches $\partial U$

Interior cell stars can therefore be varied independently once shared hinge and boundary data are held fixed. Additivity follows by summing local contributions and subtracting overlap double-counting through the ordinary cell-complex incidence rules.

Long-range constraints are not ignored. They must be one of:

- gauge constraints that only identify equivalent descriptions
- boundary or conserved-charge constraints carried by $\Theta_{\partial U}$
- local fields already included in the reconstructed H2/H3 description
- residual nonlocal terms assigned to $\Theta_{\mathrm{nl}}$

If a long-range pulse-network constraint cannot be placed in one of those categories, the strong local Einstein-Hilbert derivation is not established.

### 11.4 Boundary Flux And Global Constraints

Finite regions can have real boundary exchange. Matter stress-energy, clock calibration signals, radiation, and frame references may cross $\partial U$. Such flux does not violate locality if it is represented as boundary data:

$$
\delta\Theta_{\mathrm{pc}}[U]=\delta\Theta_{\mathrm{bulk}}[U]+\delta\Theta_{\partial U}
$$

The locality claim applies to compactly supported variations in the interior, or to finite-region variations after the correct boundary phase and flux conditions are supplied.

Global gauge constraints are not physical action terms. Diffeomorphism gauge, local Lorentz gauge, station relabeling, and clock-zero shifts must quotient descriptions rather than contribute new bulk phase.

### 11.5 Classification Of Nonlocal Terms

Nonlocal terms must be classified rather than hidden.

| Term type | Example | 05S classification |
|---|---|---|
| Gauge-identification term | same pulse network represented with different station labels or coordinates | Not a physical phase; quotient it |
| Boundary flux | radiation, matter, or calibration information crossing $\partial U$ | Boundary term if explicitly carried |
| Finite correlation tail | residual coupling between nearby cell stars with range $\xi_n$ | Suppressed correction if $\xi_n/L_R\to0$ |
| Reconstruction covariance | correlated clock or instrument uncertainty in $\mathcal{E}_{\mathrm{stat}}$ | Estimator effect, not a geometry phase |
| Known long-range field | a field whose local degrees of freedom are included in the model | Local after the field is included |
| Irreducible nonlocal kernel | pairwise network cost over distant records not expressible as boundary, gauge, or local field | Controlled modification if small; fatal ambiguity if unsuppressed |
| Lattice-memory term | dependence on refinement path or preferred loop graph at fixed continuum geometry | Controlled anisotropic modification if bounded; fatal if leading order |

The most important failure mode is an unsuppressed term of the schematic form:

$$
\Theta_{\mathrm{nl}}=\int_U d^4x\int_U d^4y\sqrt{-g(x)}\sqrt{-g(y)}K(x,y)\mathcal{I}(x,y)
$$

If $K(x,y)$ does not collapse to a local density, boundary term, gauge quotient, or suppressed correction in the continuum limit, then 05S cannot upgrade 05 to a strong local Einstein-Hilbert derivation.

### 11.6 Additive Pulse-Regge Candidate Under The Locality Assumptions

When the restricted theorem applies, the leading local discrete candidate has the form:

$$
\Theta_{\mathrm{pc}}^{\mathrm{loc}}=\frac{c^3}{8\pi G\hbar}\sum_h s_hA_h\epsilon_h-\frac{c^3\Lambda}{8\pi G\hbar}\sum_\sigma s_\sigma V_\sigma+\Theta_{\partial U}+\Theta_{\mathrm{corr}}
$$

This is now a local-additive candidate under explicit sufficient conditions. It remains conditional because later 05S tasks must still prove scalarization, refinement invariance, and correction suppression.

### 11.7 05S.3 Outcome

05S.3 accepts a restricted locality result:

- additive local pulse-cell phase is justified if record density, causal regularity, local correction ledgers, finite dependence range, boundary-flux accounting, and refinement regularity are imposed
- statistical reconstruction losses remain separate from the physical geometry phase
- nonlocal terms are classified as gauge, boundary, suppressed, controlled modifications, or fatal ambiguities

05S.3 does not prove that all admissible pulse networks satisfy these assumptions. It narrows the strong 05 path: a future upgrade is possible only for pulse-network continuum limits where unsuppressed irreducible nonlocal kernels and leading lattice-memory terms are absent.

## 12. 05S.4 Unbiased Scalarization To Ricci Scalar

05S.4 attacks the central scalarization gap. H3 gives tensor-valued frame holonomies; the Einstein-Hilbert action needs the scalar curvature density. The missing question is when local loop and hinge samples contract to $R\sqrt{-g}$ instead of a protocol-dependent projection.

The honest result is again conditional. Scalarization is justified if the local loop-plane quadrature converges to the scalar-curvature projector. It is not justified for arbitrary loop families, spatial-only H3 checks, positive-only boost averaging, or squared residual losses.

### 12.1 Local Curvature Scalar Sample

In one small cell star, write the H3 curvature sample schematically as:

$$
\mathcal{K}_{i\hat a\hat b}=R_{\hat a\hat b\hat c\hat d}A_i^{\hat c\hat d}+O(\ell_i^3)
$$

For a loop or hinge probe with normalized oriented bivector $B_i^{\hat a\hat b}$, the linear scalar sample is:

$$
\kappa_i=\frac{1}{2}B_i^{\hat a\hat b}\mathcal{K}_{i\hat a\hat b}
$$

After dividing by the loop-area normalization implicit in the weights, a local linear curvature estimator has the form:

$$
\mathcal{R}_{\mathrm{pulse}}=R_{\hat a\hat b\hat c\hat d}C_{\mathrm{loop}}^{\hat a\hat b\hat c\hat d}+O(\ell^2/L_R^2)+\mathcal{R}_{\mathrm{corr}}
$$

where the loop-plane quadrature tensor is:

$$
C_{\mathrm{loop}}^{\hat a\hat b\hat c\hat d}=\sum_i \omega_i B_i^{\hat a\hat b}B_i^{\hat c\hat d}
$$

The weights $\omega_i$ include orientation, area-to-volume normalization, uncertainty weighting, and any cell-complex incidence factors. They are not arbitrary fitting weights; they are part of the physical scalarization claim.

### 12.2 Scalar-Curvature Projector

With the H3 curvature-sign convention fixed, define the scalar-curvature projector $P_R$ by:

$$
R_{\hat a\hat b\hat c\hat d}P_R^{\hat a\hat b\hat c\hat d}=R
$$

A standard local expression for this projector is:

$$
P_R^{\hat a\hat b\hat c\hat d}=\frac{1}{2}(\eta^{\hat a\hat c}\eta^{\hat b\hat d}-\eta^{\hat a\hat d}\eta^{\hat b\hat c})
$$

up to the overall sign convention chosen for the Riemann tensor. The sign is not a free parameter after H3 and the Newtonian-limit check fix conventions.

The scalarization condition is therefore:

$$
C_{\mathrm{loop}}^{\hat a\hat b\hat c\hat d}\to P_R^{\hat a\hat b\hat c\hat d}
$$

Then:

$$
\mathcal{R}_{\mathrm{pulse}}\to R
$$

and the local additive phase from 05S.3 can become an Einstein-Hilbert density, subject to refinement and correction checks.

### 12.3 Lorentzian Orientation Weights

Lorentzian scalarization is not an ordinary positive average over all two-planes. The Lorentz group is noncompact, so there is no finite positive Lorentz-invariant probability measure over all boost-related planes.

05S therefore needs an algebraic local quadrature, not an informal statement that loops are sampled uniformly. The allowed weights are signed or orientation-sensitive weights that satisfy the projector identity above in the local frame. Equivalent routes are:

- a Regge-style hinge quadrature whose signed area-defect sum is known to converge to the scalar curvature density
- a symmetric local loop design whose second bivector moment equals $P_R$
- a discrete tetrad-based quadrature that includes both rotation and boost planes with the signs required by $\eta_{\hat a\hat b}$

If the pulse network supplies only positive weights over a preferred instrument distribution, scalarization is not proved.

### 12.4 Sufficient Conditions For Scalarization

Unbiased scalarization is accepted for a cell sequence only when all of these conditions hold.

**Tensor-ready loops.** The loop family supplies enough independent H3 frame closures to sample the local bivector space, not just one scalar timing channel.

**Lorentzian plane coverage.** Both spatial rotation and time-space boost sectors are represented, or the omitted sector is proved irrelevant by symmetry or by the specific spacetime class under study.

**Projector convergence.** The weighted bivector second moment converges to $P_R$:

$$
\Delta C^{\hat a\hat b\hat c\hat d}=C_{\mathrm{loop}}^{\hat a\hat b\hat c\hat d}-P_R^{\hat a\hat b\hat c\hat d}
$$

with:

$$
R_{\hat a\hat b\hat c\hat d}\Delta C^{\hat a\hat b\hat c\hat d}\to0
$$

in the continuum limit, or else the residual is carried as an anisotropic correction.

**Orientation consistency.** Reversing loop or hinge orientation flips the signed defect and does not change the final oriented scalar density.

**Finite-loop suppression.** Terms from variation of curvature across loops scale away relative to the leading linear curvature term.

**Correction-ledger separation.** Calibration or protocol artifacts are subtracted before scalarization. They are not allowed to imitate missing curvature components.

### 12.5 Failure Cases

Scalarization fails or downgrades in these cases.

| Failure | Result |
|---|---|
| Spatial-loop-only sampling in a general Lorentzian geometry | Samples only selected curvature components; not $R$ |
| Preferred loop-plane distribution | Produces $R_{\hat a\hat b\hat c\hat d}C^{\hat a\hat b\hat c\hat d}$ with a preferred tensor $C$ |
| Positive-only boost averaging | Not Lorentz invariant; needs signed quadrature or a restricted frame choice |
| Scalar timing residual only | Protocol projection, not tensor scalarization |
| Squared residual physical phase | Curvature-squared or protocol-squared action, not Einstein-Hilbert |
| Finite-loop terms unsuppressed | Higher-derivative or nonlocal correction |
| Hinge or loop orientation inconsistent | Sign-ambiguous action |

The anisotropic failure has a simple diagnostic:

$$
\mathcal{R}_{\mathrm{pulse}}=R+R_{\hat a\hat b\hat c\hat d}\Delta C^{\hat a\hat b\hat c\hat d}
$$

If the second term is leading order, the result is a preferred-frame or preferred-loop gravity candidate, not a derivation of the Einstein-Hilbert action.

### 12.6 Prototype Checks

The 05S.6 prototype includes focused algebraic checks rather than hiding this assumption in prose:

- a constant-curvature case where the quadrature returns the expected scalar curvature
- an orientation-reversal check
- a deliberately anisotropic quadrature where $\Delta C$ produces a nonzero preferred-projection residual
- explicit metric-lowering behavior for a time-space boost generator
- rejection or explicit exclusion of null cases outside the implemented convention

These checks will test the algebraic scalarization condition. They will not prove that arbitrary experimental pulse networks satisfy it.

### 12.7 05S.4 Outcome

05S.4 accepts a conditional scalarization theorem:

- H3 frame holonomies reduce to the Ricci scalar only when the local loop-plane quadrature tensor converges to the scalar-curvature projector
- Lorentzian orientation weights must be signed or algebraic, not a naive positive average over boost planes
- spatial-only, scalar-only, anisotropic, or squared-residual constructions do not derive the Einstein-Hilbert density

This strengthens 05 by naming the exact scalarization condition. It does not yet prove that the pulse network dynamically enforces that condition. If later refinement and correction checks pass, the 05S result can become a stronger conditional derivation; if they fail, the outcome remains unchanged 05 or a controlled anisotropic modification.

## 13. 05S.5 Refinement And Replacement Invariance

05S.5 asks when the pulse-cell description stops being a preferred lattice and becomes only a replaceable description of the same smooth geometry.

The result is a restricted replacement-invariance theorem. It applies to regular refinements and local replacements that preserve H2 geometry, corrected H3 defects, scalarization quadrature, and boundary data. It does not claim full triangulation independence for arbitrary Lorentzian cell complexes.

### 13.1 Allowed Replacements

The following replacements are allowed if they preserve the same observed and reconstructed physical content:

- station, signal, event, and cell relabeling
- clock-zero changes
- local Lorentz frame changes
- replacing a loop basis by another loop basis with the same local bivector second moment
- subdividing cells while preserving the same H2 metric region and boundary data
- local cell moves that keep nondegenerate hinge normals, bounded valence, and compatible orientations
- refinement paths whose maximum H2 cell diameter tends to zero

The following are not gauge replacements:

- changing the physical boundary of $U$
- changing flux through $\partial U$
- deleting a curvature sector from the loop-plane quadrature
- introducing a preferred station lattice or preferred loop orientation
- changing the correction ledger without carrying the residual as a correction

### 13.2 Replacement-Invariance Theorem

Let $\mathcal{C}_n$ and $\mathcal{C}'_n$ be two pulse-cell complexes for the same admissible pulse network region $U$, or for two refinements representing the same H2/H3 continuum data on $U$. Let $\ell_n$ be the larger of their maximum H2 cell diameters.

Assume:

- the locality conditions of 05S.3 hold for both complexes
- the hinge defects are constructed by the 05S.2 non-null bivector projection
- the scalarization tensors of both complexes converge to $P_R$
- both complexes are shape-regular enough to avoid degenerate cell volumes and ill-conditioned hinge normals
- the same induced boundary geometry and boundary flux data are held fixed
- correction-ledger residuals are bounded by a shared correction budget

Then the local pulse-Regge candidate satisfies:

$$
\Theta_{\mathrm{pc}}^{\mathrm{loc}}[\mathcal{C}_n]-\Theta_{\mathrm{pc}}^{\mathrm{loc}}[\mathcal{C}'_n]=\Delta\Theta_{\partial U}+E_n
$$

where $\Delta\Theta_{\partial U}$ is the change in boundary or joint description, and:

$$
E_n\to0
$$

when finite-loop, scalarization, nonlocal, lattice-memory, and correction-ledger residuals all vanish under refinement. If any residual has a nonzero continuum limit, it must be retained as a controlled correction or failure mode.

### 13.3 Error Ledger

The replacement error is not a single hidden term. It decomposes as:

$$
E_n=E_{\mathrm{loop}}+E_{\mathrm{scalar}}+E_{\mathrm{refine}}+E_{\mathrm{nl}}+E_{\mathrm{corr}}
$$

with:

- $E_{\mathrm{loop}}$ from finite-loop truncation in H3
- $E_{\mathrm{scalar}}$ from failure of the loop-plane quadrature to reach $P_R$
- $E_{\mathrm{refine}}$ from cell-shape irregularity or refinement-path memory
- $E_{\mathrm{nl}}$ from nonlocal terms classified in 05S.3
- $E_{\mathrm{corr}}$ from correction-ledger residuals

Replacement invariance is accepted only when each term vanishes, becomes a boundary term, or is retained as an explicit correction. It is not accepted by averaging unexplained residuals away.

### 13.4 Boundary Changes

For fixed induced boundary geometry and compatible boundary flux data, refinement of the boundary description may change only the representation of the boundary phase and joint terms:

$$
\Theta_{\partial U}=\Theta_{\mathrm{GHY}}+\Theta_{\mathrm{joint}}+\Theta_{\mathrm{flux}}
$$

In the discrete pulse-Regge description this means boundary hinge and joint sums may be redistributed under subdivision, but their continuum limit must agree with the same boundary geometry.

If the physical boundary is moved, or if flux through the boundary is changed, the action is allowed to change. That is physics, not a failure of replacement invariance.

### 13.5 Regge-To-Continuum Connection

Under the regularity assumptions above, the local defect sum has the standard Regge-to-continuum form:

$$
2\sum_{h\subset U^\circ}s_hA_h\epsilon_h\to\int_U R\sqrt{-g}\,d^4x
$$

and the cell-volume sum converges to:

$$
\sum_{\sigma\subset U}s_\sigma V_\sigma\to\int_U\sqrt{-g}\,d^4x
$$

Therefore the local pulse-Regge candidate converges to:

$$
\Theta_{\mathrm{pc}}^{\mathrm{loc}}\to\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x+\Theta_{\partial U}+\Theta_{\mathrm{corr}}
$$

This connection is conditional on 05S.2 through 05S.4 and on regular refinement. It is not a proof that arbitrary pulse-cell complexes, arbitrary Lorentzian triangulations, or arbitrary raw pulse networks are triangulation-independent.

### 13.6 Failure Implications

The theorem fails in ways that have clear meanings.

| Failure | Consequence |
|---|---|
| Cell labels or station graph survive refinement | Preferred-lattice or preferred-frame modification |
| Loop basis changes $C_{\mathrm{loop}}$ at leading order | Scalarization failure or anisotropic gravity |
| Degenerate or near-null hinges dominate | Lorentzian Regge convention incomplete |
| Boundary joints omitted | Variational principle incomplete |
| Nonlocal term survives refinement | Nonlocal controlled modification or strong-05 failure |
| Finite-loop errors do not shrink | Higher-derivative or finite-size correction |
| Different refinement paths give different bulk limits | Replacement invariance fails |

These failures do not necessarily kill the conservative 05 result. They block the stronger claim that pulse-network consistency alone selects the Einstein-Hilbert action.

### 13.7 05S.5 Outcome

05S.5 accepts a restricted refinement and replacement-invariance theorem:

- regular pulse-cell replacements preserve the local pulse-Regge candidate up to boundary terms and explicit residuals
- the discrete hinge sum connects to the Einstein-Hilbert density only when locality, hinge-defect construction, scalarization, and regular refinement assumptions all hold
- full triangulation independence is not claimed

This gives 05S a coherent route from local pulse-Regge sums to the continuum Einstein-Hilbert phase, but it remains a stronger conditional derivation rather than a fundamental derivation from raw pulse records.

## 14. 05S.6 Lorentzian Pulse-Regge Prototype

05S.6 adds a deliberately small executable prototype in `src/pulse_model/pulse_regge.py`, with tests in `tests/test_pulse_regge.py`.

The prototype implements only algebraic checks needed by 05S:

- raising and lowering the first index of local Lorentz generators with $\eta_{\hat a\hat b}$
- projection of a lowered local Lorentz generator onto an oriented contravariant hinge normal bivector
- oriented interior hinge sums $\sum_h s_hA_h\epsilon_h$
- scalar-curvature integral relation $2\sum_hs_hA_h\epsilon_h$
- local plane-quadrature scalarization residuals
- a symbolic constant-curvature refinement benchmark
- oriented cell-volume sums $\sum_\sigma s_\sigma V_\sigma$
- a simple boundary hinge sum $\sum_bs_bA_b\psi_b$
- validation that invalid axes, non-antisymmetric generators, zero areas, and invalid orientations are rejected

It is not a mesh generator, path-ordered transport solver, full Lorentzian Regge calculus implementation, or numerical GR engine.

### 14.1 Executable Coverage

The tests cover:

- flat zero-defect behavior
- spatial rotation-plane hinge projection
- time-space boost-plane hinge projection through explicit Lorentz metric lowering
- loop or hinge orientation reversal
- linear scaling with area and defect
- scalarization residual detection for biased loop-plane quadrature
- constant-curvature refinement scaling where $2\sum A_h\epsilon_h=RV$
- oriented cell-volume signs
- boundary orientation sign for a discrete boundary hinge

This gives an executable check of the algebraic spine used by 05S.2 through 05S.5.

### 14.2 What The Prototype Does Not Prove

The prototype does not prove:

- that real pulse networks supply the required loop-plane quadrature
- that arbitrary Lorentzian triangulations are refinement independent
- that null hinges or joints are handled
- that finite-loop H3 errors are bounded in a general metric
- that $G$ or $\Lambda$ are derived from pulse records

Those remain correction and decision-report issues for later 05S tasks.

### 14.3 05S.6 Outcome

05S.6 accepts a focused executable prototype for the algebraic pulse-Regge strengthening path. It supports the conditional derivation by testing signs, linearity, projection, boundary orientation, and refinement scaling in controlled examples. It does not upgrade 05 by itself.

## 15. 05S.7 Correction Taxonomy

05S.7 classifies the terms that can prevent 05S from becoming a strong derivation of the Einstein-Hilbert action. The goal is not broad phenomenology. The goal is to decide whether corrections are suppressed, controlled modifications, or fatal unsuppressed alternatives.

### 15.1 Schematic Correction Budget

The local leading candidate after 05S.2 through 05S.6 is:

$$
\Theta_{\mathrm{EH}}=\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x+\Theta_{\partial U}
$$

The correction budget is:

$$
\Theta_{\mathrm{pc}}=\Theta_{\mathrm{EH}}+\Theta_{\mathrm{finite}}+\Theta_{\mathrm{scalar}}+\Theta_{\mathrm{hc}}+\Theta_{\mathrm{torsion}}+\Theta_{\mathrm{nl}}+\Theta_{\mathrm{lattice}}+\Theta_{\mathrm{corr}}
$$

Each correction must be assigned one of three statuses:

- suppressed correction: vanishes in the 05S continuum limit or is negligible inside the accepted low-energy domain
- controlled modification: remains with an explicit scale, sign, and observable consequence
- fatal ambiguity: appears at leading order without a unique controlled form, so the strong 05 derivation fails

### 15.2 Correction Classes

| Class | Forced by pulse-network structure? | Scaling or proof obligation | Known-physics boundary | 05S decision trigger |
|---|---|---|---|---|
| Finite-loop corrections | Yes, because H3 loops have nonzero size | Must scale to zero with $\ell_{\mathrm{loop}}/L_R$ or be retained as higher-derivative terms | Existing weak-field, redshift, tidal, and holonomy benchmarks require the leading local limit to dominate | Suppressed if refinement removes them; controlled if a finite loop scale remains; fatal if leading and unclassified |
| Scalarization anisotropy | Forced if loop-plane weights are biased | Governed by $R_{\hat a\hat b\hat c\hat d}\Delta C^{\hat a\hat b\hat c\hat d}$ | Preferred-frame and isotropy-sensitive tests constrain leading anisotropy | Suppressed if $\Delta C\to0$; controlled if a small anisotropic tensor remains; fatal if leading |
| Higher-curvature terms | Optional unless produced by squared residuals or finite-loop expansion | Must carry a scale such as $L_\ast^2R^2$ relative to $R$ | Known GR recovery and Newtonian-limit tests require these terms to be negligible in accepted benchmark regimes | Controlled if scale is explicit and small; fatal for strong 05 if unsuppressed |
| Torsion | Optional unless corrected transports fail to approach Levi-Civita transport | Must define an independent torsion observable or show torsion terms vanish | Standard matter phase-response and metric reconstruction currently assume metric-compatible torsion-free geometry | Controlled if an extra torsion sector is explicit; fatal to metric-only 05 if hidden and leading |
| Nonlocal kernels | Optional, but possible if pulse consistency has long-range pair costs | Must reduce to boundary, gauge, local fields, or suppressed kernels | Local GR recovery and conservation require no leading irreducible nonlocal bulk response | Controlled if kernel range and strength are explicit; fatal if unsuppressed and arbitrary |
| Lattice memory | Possible in any discrete description | Must vanish under replacement or become an explicit anisotropic correction | Lorentz and diffeomorphism recovery require no preferred cell graph in the leading action | Suppressed if refinement-independent; controlled if small; fatal if refinement path changes the bulk limit |
| Boundary and joint terms | Yes for finite regions | Must be carried as $\Theta_{\partial U}$, not mistaken for a bulk correction | Variational checks require fixed boundary data or correct boundary phase | Incomplete if omitted; not a bulk failure when handled |
| Correction-ledger residuals | Yes in finite records | Must remain estimator-side or be assigned to physical correction terms with scale | Existing benchmark tests require correction subtraction not to manufacture curvature | Suppressed if bounded; controlled if physical; fatal if used to hide missing curvature |

### 15.3 Higher-Curvature Terms

A schematic higher-curvature sector is:

$$
\Theta_{\mathrm{hc}}=\frac{1}{\hbar}\int_U\sqrt{-g}\,d^4x\,(\alpha_1L_\ast^2R^2+\alpha_2L_\ast^2R_{\mu\nu}R^{\mu\nu}+\alpha_3L_\ast^2R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}+\cdots)
$$

Relative to the Einstein-Hilbert term, these are suppressed when:

$$
L_\ast^2|R|\ll1
$$

in the domain where 05 claims low-energy recovery. If the pulse network naturally produces squared residuals as the physical phase, the higher-curvature sector is not a small correction by default. It becomes the leading theory, and the strong Einstein-Hilbert derivation fails unless a separate argument suppresses it.

### 15.4 Torsion

Torsion appears if corrected edge transports do not converge to Levi-Civita transport. A schematic torsion sector is:

$$
\Theta_{\mathrm{torsion}}\sim\frac{1}{\hbar}\int_U\sqrt{-g}\,d^4x\,\gamma T_{\lambda\mu\nu}T^{\lambda\mu\nu}
$$

05S currently has no accepted torsion observable. Therefore torsion must be treated as:

- absent by the H3 Levi-Civita smooth-transport assumption
- an explicit controlled extension with new observables and couplings
- a failure of the metric-only 05 strengthening if it is required but hidden

### 15.5 Anisotropy And Lattice Memory

Anisotropy enters through the scalarization residual:

$$
\Theta_{\mathrm{scalar}}=\frac{1}{\hbar}\int_U\sqrt{-g}\,d^4x\,\lambda_A R_{\hat a\hat b\hat c\hat d}\Delta C^{\hat a\hat b\hat c\hat d}
$$

Lattice memory enters when the continuum limit depends on the refinement path or cell graph:

$$
\Theta_{\mathrm{lattice}}=\frac{1}{\hbar}\int_U\sqrt{-g}\,d^4x\,\lambda_L\mathcal{L}_{\mathrm{cell}}(g,\mathcal{G}_{\mathrm{refine}})
$$

where $\mathcal{G}_{\mathrm{refine}}$ denotes the surviving graph or refinement data. If $\mathcal{G}_{\mathrm{refine}}$ survives as a physical field or background, the leading action is not diffeomorphism-invariant Einstein-Hilbert gravity.

### 15.6 Nonlocal Corrections

A nonlocal correction has the schematic form already identified in 05S.3:

$$
\Theta_{\mathrm{nl}}=\int_Ud^4x\int_Ud^4y\sqrt{-g(x)}\sqrt{-g(y)}K(x,y)\mathcal{I}(x,y)
$$

It is acceptable only if:

- it reduces to boundary or gauge data
- it can be represented by local fields already included in the model
- the kernel is short-range enough to become a derivative expansion with suppressed coefficients
- it is retained as a controlled nonlocal modification with explicit scale and predictions

If none of these applies, the strong local geometry-action derivation fails.

### 15.7 Forced, Optional, And Bounded Corrections

Forced by finite pulse-network structure:

- finite-loop errors
- boundary and joint terms for finite regions
- correction-ledger residuals
- possible lattice-memory checks under refinement

Optional effective terms unless a later derivation forces them:

- curvature-squared terms
- torsion sectors
- irreducible nonlocal kernels
- preferred-frame anisotropic tensors

Bounded by the existing known-physics recovery ladder and standard GR/QM consistency requirements:

- finite-loop corrections must not spoil flat, weak-field, tidal, redshift, COW, and holonomy benchmarks
- higher-curvature and nonlocal corrections must not change the accepted Newtonian and Einstein-equation checks inside their stated domains
- torsion or anisotropy must not contradict the metric-only stress-energy phase-response and local Lorentz recovery already used by H2 through H4

This appendix does not add a broad numerical constraint framework. If a later correction is promoted to a controlled modification, it needs its own focused phenomenology task.

### 15.8 05S.7 Outcome

05S.7 accepts the correction taxonomy. The strong 05 upgrade remains viable only if finite-loop, anisotropic, higher-curvature, torsion, nonlocal, lattice-memory, boundary, and correction-ledger terms are either suppressed, converted to boundary/gauge data, or retained as explicit controlled modifications.

If any one of these terms appears unsuppressed and unconstrained at the same order as the Einstein-Hilbert term, 05S must not call the result a stronger derivation. The final decision must label it as a controlled modification or clean failure of strong 05.

## 16. 05S.8 Alternatives And Failure Modes

05S.8 compares the leading linear pulse-Regge defect candidate against nearby alternatives. This is an adversarial check: if an alternative is equally natural from pulse data and not suppressed, the final 05S report must not overclaim.

### 16.1 Candidate Comparison

| Candidate | Natural source | Strength | Problem for strong 05 | 05S disposition |
|---|---|---|---|---|
| Linear oriented hinge defect $\sum_hs_hA_h\epsilon_h$ | H3 frame holonomy plus Regge continuum limit | First order in curvature, orientation sensitive, connects to $R\sqrt{-g}$ under 05S.2 through 05S.5 | Needs locality, scalarization, refinement, and correction assumptions | Retain as leading conditional candidate |
| Squared residual cost $\sum_L\Delta_L^2/\sigma_L^2$ | Statistical fitting of noisy pulse records | Positive estimator for reconstruction | Removes orientation sign and gives curvature-squared behavior, not Einstein-Hilbert | Reject as physical phase unless model chooses higher-curvature modification |
| Curvature-squared action | Finite-loop expansion or squared holonomy residuals | Natural effective correction | Adds higher-derivative response and extra scales | Retain only as controlled correction |
| Torsionful transport action | Edge maps do not converge to Levi-Civita transport | Could model defects beyond metric curvature | Violates metric-only 05 unless new torsion observables and couplings are explicit | Controlled extension or failure of strong metric-only 05 |
| Preferred-frame or preferred-loop action | Biased station geometry or loop-plane sampling | Honest if the network really preserves preferred structure | Breaks diffeomorphism or local Lorentz recovery in the leading action | Controlled anisotropic modification if small; otherwise failure |
| Nonlocal network cost | Pairwise or global consistency constraints | May represent genuine long-range pulse structure | Not Einstein-Hilbert unless reducible to boundary, gauge, local fields, or suppressed kernels | Controlled nonlocal modification or failure |
| Spectral or heat-kernel route | Pulse network defines an operator whose expansion contains $R$ | Can naturally produce $R$ plus higher-curvature terms | Requires deriving the operator from pulse records; otherwise imports a new assumption | Future route, not accepted 05S derivation |
| Induced-gravity route | Quantum matter phase-response generates metric action | Connects geometry action to matter fluctuations | Shifts proof burden to QFT and vacuum renormalization; risks H7 cosmological-constant issues | Downstream comparison, not 05S proof |
| Causal or interval-count route | Use order and volume counts instead of frame holonomies | Useful independent comparison | Pulse records contain richer clock/frame data; scalar estimator assumptions remain | Comparison route, not current leading path |
| Scalarization-failure action | Loop quadrature gives $C_{\mathrm{loop}}\neq P_R$ | Honest output of biased pulse networks | Gives anisotropic or protocol-dependent curvature contraction | Controlled modification if small; failure if leading |

### 16.2 Why Squared Residuals Are Not The Leading Physical Phase

Squared residuals are useful for reconstruction:

$$
\chi^2_{\mathrm{loop}}=\sum_L\frac{\Delta_L^2}{\sigma_L^2}
$$

They answer the estimator question: which metric best fits noisy records under a covariance model? That is not the same question as: what geometric phase is varied against matter phase-response?

The H3 loop residual is first order in curvature times loop area:

$$
\Delta_L\sim R_{\hat a\hat b\hat c\hat d}A_L^{\hat c\hat d}
$$

Therefore a squared residual produces a second-order curvature object:

$$
\Delta_L^2\sim R_{\hat a\hat b\hat c\hat d}R_{\hat e\hat f\hat g\hat h}A_L^{\hat c\hat d}A_L^{\hat g\hat h}
$$

It also loses the orientation sign that makes the linear Regge defect add as a scalar curvature density. A squared loss can be retained as an estimator or promoted to a controlled higher-curvature physical modification. It cannot be silently used as the Einstein-Hilbert phase.

### 16.3 Why The Linear Defect Candidate Survives

The linear oriented defect remains the best 05S candidate because it is the only route in this appendix that simultaneously:

- uses the tensor-ready H3 observable rather than only scalar timing residuals
- keeps orientation signs
- is first order in curvature
- has a known Regge-to-continuum bridge to $R\sqrt{-g}$
- can include the 05 boundary prescription
- reduces to the accepted 05 low-energy candidate when the 05S assumptions hold

This is a conditional preference, not a proof from raw records. The candidate survives because the alternatives are either estimator tools, controlled corrections, or stronger modifications with extra assumptions.

### 16.4 Failure-Mode Decision Rules

The final 05S decision must apply these rules.

| Finding | Decision |
|---|---|
| Locality, scalarization, refinement, and correction suppression all hold only under explicit sufficient conditions | Stronger conditional derivation |
| Same route works but leaves finite controlled higher-curvature, torsion, anisotropic, or nonlocal terms | Controlled modification |
| Squared residual or curvature-squared term is the natural leading pulse phase | No Einstein-Hilbert derivation; controlled modification if scale is explicit |
| Preferred loop or lattice data survive at leading order | Strong 05 failure unless promoted to a constrained anisotropic model |
| Nonlocal kernel survives without scale or reduction | Clean failure of strong local 05 |
| Pulse data do not determine the needed loop-plane quadrature | Unchanged accepted-with-limits 05 |

### 16.5 05S.8 Outcome

05S.8 retains the linear oriented pulse-Regge defect as the leading candidate only under the assumptions made explicit by 05S.1 through 05S.7. Squared residuals remain estimator costs unless the model deliberately chooses a higher-curvature physical modification. Torsionful, preferred-frame, nonlocal, spectral, induced-gravity, and scalarization-failure routes are not discarded as impossible, but they do not support a stronger Einstein-Hilbert derivation without extra assumptions.

This sets up the final 05S decision: the work can honestly choose stronger conditional derivation, controlled modification, unchanged accepted-with-limits 05, or clean failure.

## 17. 05S.9 Strengthened Geometry-Action Decision Report

### 17.1 Decision Label

05S resolves to **stronger conditional derivation**.

It upgrades the closed 05 result from a broad low-energy uniqueness motivation to a pulse-network conditional derivation route:

- admissible pulse networks and pulse-cell complexes are explicitly defined
- corrected H3 frame holonomies are mapped to non-null Lorentzian hinge defects
- local additivity is given as a restricted sufficient-conditions theorem
- scalarization to $R$ is reduced to an explicit loop-plane quadrature condition
- refinement and replacement invariance are stated with an error ledger
- a small Python prototype checks projection, orientation, boundary sign, and refinement scaling
- higher-curvature, torsion, anisotropic, nonlocal, finite-loop, and lattice-memory alternatives are classified

This is stronger than the original 05 acceptance because the missing assumptions are now precise mathematical gates rather than informal caveats. It is still conditional because 05S does not prove that arbitrary raw pulse records dynamically enforce those gates.

### 17.2 Accepted 05S Result

05S accepts the following conditional statement.

If an admissible pulse-network refinement satisfies the 05S locality, hinge-defect, scalarization, replacement-invariance, boundary, and correction-suppression conditions, then the leading local pulse-Regge phase:

$$
\Theta_{\mathrm{pc}}^{\mathrm{loc}}=\frac{c^3}{8\pi G\hbar}\sum_h s_hA_h\epsilon_h-\frac{c^3\Lambda}{8\pi G\hbar}\sum_\sigma s_\sigma V_\sigma+\Theta_{\partial U}+\Theta_{\mathrm{corr}}
$$

has the continuum limit:

$$
\Theta_{\mathrm{pc}}^{\mathrm{loc}}\to\frac{1}{\hbar}\frac{c^3}{16\pi G}\int_U(R-2\Lambda)\sqrt{-g}\,d^4x+\Theta_{\partial U}+\Theta_{\mathrm{corr}}
$$

with $\Theta_{\mathrm{corr}}$ suppressed, converted to boundary or gauge data, or retained as an explicit controlled correction.

Under these assumptions, 05S supplies a concrete pulse-network route to the same low-energy source-to-metric bridge accepted in 05.

### 17.3 What 05S Does Not Accept

05S does not establish:

- a fundamental derivation of Einstein-Hilbert gravity from arbitrary raw pulse counts
- automatic locality of all pulse-consistency costs
- dynamic enforcement of the scalar-curvature projector $P_R$
- full Lorentzian coverage of null hinges, null boundaries, and joints
- suppression of every higher-curvature, torsion, anisotropic, or nonlocal correction without further assumptions
- a derivation of $G$ or $\Lambda$
- a solution to H7 vacuum-energy or renormalization issues

These limits are not failures of the conservative model. They define exactly where future work must act before claiming strong success.

### 17.4 Why This Is Not Merely Unchanged 05

The original 05 result said: if the smooth geometry phase is local, scalar, metric-only, second order, and properly bounded, the Einstein-Hilbert phase is the leading candidate.

05S adds a pulse-network mechanism for that statement:

- H3 frame holonomies become hinge defects through local Lorentz bivector projection
- local additivity is tied to finite-dependence and correction-ledger assumptions
- scalarization is tied to a precise loop-plane quadrature tensor
- refinement invariance is tied to allowed replacement moves and vanishing error terms
- the prototype verifies the algebraic Regge scaling spine

That is enough to label the result stronger conditional derivation rather than unchanged accepted-with-limits 05.

### 17.5 Why This Is Not Full Strong Success

Full strong success would require showing that pulse-network consistency itself forces the required local, scalar, refinement-invariant, correction-suppressed continuum limit. 05S does not prove that. It supplies sufficient conditions and failure diagnostics.

The final result therefore remains conditional:

- if the 05S conditions hold, the leading pulse-network phase is Einstein-Hilbert plus boundary and controlled corrections
- if the conditions fail mildly, the result becomes a controlled modification
- if they fail at leading order without control, strong 05 fails

### 17.6 Downstream Rules

Downstream work may cite 05S as a stronger conditional geometry-action input when the issue scope permits, but must carry the conditions explicitly.

H6 may use the Einstein equation as a branch-local low-energy source-to-metric rule from the conservative 05 result. H6 should use 05S only in tasks that explicitly opt into the strengthened 05S assumptions; a task that excludes 05S remains scoped to the conservative 05 input.

H7 may use the result only as the low-energy metric phase-response anchor. It must not treat 05S as a derivation of $\Lambda$, vacuum renormalization, or absolute vacuum phase behavior.

Any future controlled correction must name its scale, symmetry content, and known-physics boundary before it is used in later epics.

### 17.7 Final Verdict

05S strengthens 05, but conditionally.

The Pulse Model now has a coherent pulse-network route from corrected H3 holonomies to an Einstein-Hilbert leading phase:

$$
\mathcal{K}_L\to \epsilon_h\to \sum_hs_hA_h\epsilon_h\to \int_U R\sqrt{-g}\,d^4x
$$

That route is valid only for admissible continuum limits satisfying the explicit 05S assumptions. The final label is therefore **stronger conditional derivation**, with the original 05 accepted-with-limits result preserved as the conservative fallback.
