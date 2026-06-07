---
title: Known-Physics Validation Report
sidebar_label: Known-Physics Validation
sidebar_position: 4
---

# Known-Physics Validation Report

**Issues:** `sci-b8v.2`, `sci-b8v.8`, `sci-4be`, `sci-b8v.9`  
**Date:** June 7, 2026  
**Gate:** `00 Known-physics recovery ladder`

## Verdict

The known-physics recovery ladder is **accepted with limits**.

The conservative first slice is accepted as an internally checked and executable reformulation for:

- special-relativistic time dilation
- weak-field gravitational and velocity clock-rate terms
- Newtonian acceleration from the weak-field action
- weak-field gravitational redshift
- rest-phase detuning by gravitational potential
- free massive phase scaling
- COW gravitational phase magnitude and scaling
- exact Schwarzschild static-clock time dilation outside the horizon
- Schwarzschild timelike circular geodesic residuals and normalization
- radial Schwarzschild free fall from rest at infinity
- radial Schwarzschild null propagation, including integrated coordinate light time
- local Schwarzschild geodesic-deviation tidal eigenvalues
- non-Schwarzschild de Sitter static-patch clock rate
- standard scalar-field, electromagnetic-field, and point-particle stress-energy as matter phase response
- on-shell covariant conservation of stress-energy from diffeomorphism invariance

This acceptance is not an exhaustive claim about every GR solution or matter model. It says the representative Level 0-4 known-physics checks in the proof sequence now have reviewed derivations, executable benchmarks, and lightweight H4 formula checks with stated assumptions, signs, units, and limiting cases.

## Artifacts

Derivations:

- [The formal Pulse Model](./pulse_model_formalization.md), especially sections 5, 5.15, and 14.
- [The proof roadmap](./proof_sequence.md), especially Step 0 and the progress ledger.
- [H4 stress-energy as phase-response](./appendix/h4_stress_energy_as_phase_response.md), covering scalar, electromagnetic, point-particle, and conservation evidence.

Code:

- `src/pulse_model/calculations.py` implements the minimal pure Python API for proper time, weak-field clock rate, exact static-Schwarzschild clock rate, timelike circular Schwarzschild geodesic rates, radial free fall, radial null propagation, local Schwarzschild tidal eigenvalues, de Sitter static-clock rate, pulse count, free massive phase, weak-field redshift, COW phase, and clock visibility.

Executable checks:

- `tests/test_calculations.py` checks the API-level formulas, units in names, signs, scaling, and input validation.
- `tests/test_sr_weak_field_benchmarks.py` checks SR time dilation, weak-field signs, GPS-scale clock corrections, circular-orbit zero-dilation altitude, and Newtonian acceleration from $-\nabla\Phi$.
- `tests/test_phase_redshift_cow_benchmarks.py` checks one-meter redshift, rest-phase detuning, free massive phase scaling, and COW phase magnitude/scaling.
- `tests/test_schwarzschild_clock_benchmarks.py` checks exact static-clock time dilation outside a Schwarzschild horizon, weak-field agreement, near-horizon behavior, and invalid static-clock radii.
- `tests/test_schwarzschild_geodesic_benchmarks.py` checks a timelike circular Schwarzschild geodesic using the radial geodesic residual, four-velocity normalization, weak-field agreement, non-static clock-rate separation, and invalid circular-orbit radii.
- `tests/test_broader_full_metric_benchmarks.py` checks radial Schwarzschild free-fall normalization, radial null coordinate speed, integrated radial light time, local geodesic-deviation tidal eigenvalues, and de Sitter static-patch clock rate.
- `tests/test_h4_stress_energy_phase_response.py` checks the H4 phase-response sign convention, scalar pressure/stress, electromagnetic anisotropic stress and Poynting flux, and point-particle momentum-flux components.

Targeted known-physics verification command:

```bash
PYTHONPATH=src .venv/bin/python -m unittest tests.test_calculations tests.test_sr_weak_field_benchmarks tests.test_phase_redshift_cow_benchmarks tests.test_schwarzschild_clock_benchmarks tests.test_schwarzschild_geodesic_benchmarks tests.test_broader_full_metric_benchmarks tests.test_h4_stress_energy_phase_response
```

Latest targeted known-physics verification result in this run: 40 tests passed under Python 3.14.3.

The Docusaurus build also passed:

```bash
npm run build
```

## Benchmark Status

| Benchmark | Status | Evidence |
|---|---|---|
| SR time dilation | Accepted for first slice | Written derivation plus `test_sr_time_dilation_matches_lorentz_factor`. |
| Weak-field gravity plus velocity | Accepted for first slice | Written derivation plus weak-field sign, GPS-scale, and zero-dilation tests. |
| Newtonian acceleration | Accepted for first slice | Written derivation plus finite-difference check of $\mathbf{a}=-\nabla\Phi$ for a central potential. |
| Gravitational redshift | Accepted for weak-field first slice | Written derivation plus one-meter redshift sign and magnitude test. |
| Rest-phase detuning | Accepted for weak-field first slice | Written derivation plus phase detuning test matching $-m\Phi t/\hbar$. |
| Free massive phase | Accepted for first slice | Written derivation plus linear mass/time scaling tests for $S/\hbar$. |
| COW phase | Accepted for first slice | Written derivation plus representative neutron case and mass/gravity/area/velocity scaling tests. |
| Schwarzschild time dilation | Accepted for exact static-clock first slice | Written derivation plus exact outside-horizon static-clock tests, weak-field agreement, and invalid-radius checks. |
| Geodesics from stationary proper time | Accepted for first curved-metric slice | Weak-field Newtonian limit plus Schwarzschild circular-geodesic residual, four-velocity normalization, weak-field agreement, and domain checks are executable. |
| Broader full-metric GR checks | Accepted with representative limits | Radial free fall, radial null propagation, integrated radial light time, local geodesic-deviation tidal signs, and de Sitter static-patch clock rate are executable without introducing a general GR engine. |
| Stress-energy as phase-response | Accepted with H4 limits | H4 recovers scalar, electromagnetic, and point-particle stress-energy from the standard inverse-metric action variation, rewrites it as matter phase response, covers pressure/stress components, derives on-shell conservation from diffeomorphism invariance, and now has lightweight executable sign/component checks. |

## Assumptions

The accepted first slice uses the following assumptions:

- metric signature $(-,+,+,+)$
- Newtonian potential convention $\Phi=-GM/r$, with $\Phi\to0$ at infinity
- weak-field expansion through first order in $\Phi/c^2$
- low-velocity expansion through first order in $v^2/c^2$
- SI units in all Python functions and tests
- static Schwarzschild clock-rate tests apply only outside the horizon of a non-rotating spherical mass
- circular geodesic tests use equatorial timelike Schwarzschild geodesics with $r > 3GM/c^2$
- coordinate angular frequency is checked through the radial geodesic residual and four-velocity normalization, not treated as an invariant by itself
- radial free-fall checks use the exact Schwarzschild geodesic that starts at rest at infinity
- radial null speed and radial light-time checks use Schwarzschild coordinates outside the horizon and separate coordinate artifacts from null-interval checks
- geodesic-deviation checks use local Schwarzschild tidal eigenvalues in the vacuum exterior
- de Sitter static-clock checks use a nonnegative cosmological constant and stay inside the static-patch horizon
- stress-energy uses the inverse-metric convention $T_{\mu\nu}=-(2/\sqrt{-g})\delta S_{\mathrm{m}}/\delta g^{\mu\nu}$
- matter phase is related to matter action by $S_{\mathrm{m}}=\hbar\Theta_{\mathrm{m}}$, giving $T_{\mu\nu}=-(2\hbar/\sqrt{-g})\delta\Theta_{\mathrm{m}}/\delta g^{\mu\nu}$
- H4 metric variations hold matter fields or worldlines fixed, use compact-support or fixed-boundary assumptions, and require on-shell matter equations for separate conservation claims
- interacting open subsystems may exchange stress-energy; covariant conservation applies to the total on-shell matter tensor derived from a diffeomorphism-invariant action
- ideal clocks and idealized matter-wave paths
- no Earth rotation in the circular-orbit zero-dilation benchmark
- uniform-field and nonrelativistic assumptions for the COW benchmark

These assumptions are appropriate for the current conservative recovery ladder. They are not sufficient for arbitrary spacetime reconstruction, a general-purpose GR solver, or quantum-gravity claims.

## Reformulation Boundary

At this stage, the pulse language is a **validated conservative reformulation**, not a new physical theory.

The implemented checks show that pulse count and phase language can reproduce known formulas with correct signs, units, and limiting behavior in the tested regimes. They do not show that the metric itself, the Einstein-Hilbert action, or the coupling equation between geometry and stress-energy has been derived from pulse consistency. Those remain downstream proof obligations.

## Residual Gaps

The accepted gate leaves these boundaries outside the current claim:

- exhaustive coverage of metrics not used in the representative benchmarks, such as Kerr, general FLRW dynamics, generic lensing configurations, and arbitrary numerical spacetimes
- broader matter-model coverage if later claims depend on fluids, spinors, nonminimal couplings, quantum expectation values, anomalies, or renormalized vacuum stress-energy
- optional symbolic or broader stress-energy variation checks if the project later wants machine-checked H4 algebra beyond the lightweight sign/component tests
- a defensible route from pulse-comparison consistency to the geometric phase functional

## Gate Decision

The `00 Known-physics recovery ladder` is **accepted with limits**:

- accepted for the conservative Level 0-3 first slice, exact static-Schwarzschild clock rates, a first timelike circular Schwarzschild geodesic slice, and the standard H4 stress-energy action-variation evidence
- accepted for a representative Level 4 extension covering radial timelike motion, radial null propagation, integrated light time, local geodesic deviation, and a non-Schwarzschild de Sitter static metric
- not a basis for advancing speculative geometry-action, vacuum-energy, or quantum-gravity claims as established results

The parent epic `sci-b8v` can close when this report, the proof ledger, and Beads state agree. The next honest step after this gate is to use the accepted functions, benchmarks, and H4 matter-side source evidence as support for downstream work, while keeping geometry-action recovery as an explicit prerequisite for stronger claims.
