---
title: Documentation Migration Map
sidebar_label: Migration Map
sidebar_position: 99
---

# Documentation Migration Map

**Issue:** `sci-i49.1`  
**Date:** June 8, 2026  
**Purpose:** Preserve every current Pulse Model documentation artifact during the reader-flow restructure. This is an audit map, not the durable task tracker; task ownership and completion status remain in Beads.

## Migration Rule

Do not delete or rewrite scientific content during the restructure. Move, split, or index existing material only when the destination is named here. Moved public paths need either a compatibility note at the old path or a verified site redirect. Scientific verdicts, caveats, equations, source anchors, verification commands, and code references must survive the migration.

## Target Reader Flow

The target documentation shape is:

1. `index.md` for the plain-language start page.
2. `current_status.md` for the live novelty/usefulness dashboard.
3. `roadmap.md` for the proof sequence and progress ledger.
4. `frontier_strategy.md` for promising routes to possible novelty.
5. `formal_model/` for the formal reference split out of the current long formalization.
6. `evidence/` for validation and acceptance reports.
7. `appendix/` grouped by hypothesis or research branch, with index pages.
8. `reviews/` for external/project reviews.
9. `author_and_citation.md` for attribution and citation.

## Authored Markdown Inventory

| Current path | Lines | Current role | Canonical destination | Migration action | Compatibility requirement | Owner task |
|---|---:|---|---|---|---|---|
| `pulse_model/index.md` | 121 | Plain-language project overview and current start page | `pulse_model/index.md` | Keep and update as the reader-facing index | Same path remains public | `sci-i49.2` |
| `pulse_model/pulse_model_formalization.md` | 2458 | Monolithic formal model, definitions, known-physics recovery, hypotheses, API, validation ladder, references, and historical agent workstreams | `pulse_model/formal_model/index.md`, `pulse_model/formal_model/definitions_and_axioms.md`, `pulse_model/formal_model/known_physics_recovery.md`, `pulse_model/formal_model/hypotheses_h1_h7.md`, `pulse_model/formal_model/validation_ladder.md`, `pulse_model/formal_model/references.md` | Split into focused formal reference pages; keep old path as compatibility/index page | Old path must link to every split destination and preserve enough context for old links | `sci-i49.4` |
| `pulse_model/proof_sequence.md` | 523 | Proof order, status vocabulary, progress ledger, and gate acceptance summary | `pulse_model/roadmap.md` | Move or copy into canonical roadmap, then maintain old path as compatibility note | Old `proof_sequence.md` remains valid because existing docs and external references use it | `sci-i49.3` |
| `pulse_model/promising_tweaks.md` | 149 | Frontier strategy and promising paths to novelty | `pulse_model/frontier_strategy.md` | Move or copy into canonical frontier strategy, then maintain old path as compatibility note | Old `promising_tweaks.md` remains valid because review-follow-up work references it | `sci-i49.3` |
| `pulse_model/known_physics_validation_report.md` | 138 | Step 0 known-physics validation report | `pulse_model/evidence/known_physics_validation.md` | Move or copy into evidence section with consistent report framing | Old path must link to canonical evidence report | `sci-i49.5` |
| `pulse_model/h2_acceptance_report.md` | 134 | H2 acceptance report | `pulse_model/evidence/acceptance_reports/h2_metric_reconstruction.md` | Move or copy into acceptance-report section | Old path must link to canonical report | `sci-i49.5` |
| `pulse_model/author_and_citation.md` | 51 | Author, citation, and project attribution | `pulse_model/author_and_citation.md` | Keep | Same path remains public | `sci-i49.9` |
| `pulse_model/reviews/review-2.md` | 582 | External/project review with three recommended paths | `pulse_model/reviews/review-2.md` | Keep, possibly add index/category metadata | Same path remains public; reviews category visibility should be intentional | `sci-i49.9` |
| `pulse_model/appendix/h1_time_is_relational_pulse_count.md` | 1351 | H1 proof and acceptance report | `pulse_model/appendix/h1_time_is_relational_pulse_count.md` | Keep in core appendix group, with appendix index link | Same path remains public | `sci-i49.6` |
| `pulse_model/appendix/h2_metric_reconstruction_from_pulse_comparisons.md` | 904 | H2 fixed-event theorem | `pulse_model/appendix/h2/metric_reconstruction_from_pulse_comparisons.md` | Move into H2 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h2_finite_pulse_record_schema.md` | 514 | H2 finite pulse-record schema | `pulse_model/appendix/h2/finite_pulse_record_schema.md` | Move into H2 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h2_finite_data_stability_and_gauge.md` | 298 | H2 finite-data stability and gauge conditions | `pulse_model/appendix/h2/finite_data_stability_and_gauge.md` | Move into H2 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h2_raw_relational_identifiability.md` | 276 | H2 raw relational identifiability sufficient conditions | `pulse_model/appendix/h2/raw_relational_identifiability.md` | Move into H2 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h2_raw_event_graph_reconstruction.md` | 1092 | H2S1 raw event-graph reconstruction diagnostic | `pulse_model/appendix/h2/raw_event_graph_reconstruction.md` | Move into H2 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h3_pulse_comparison_holonomy.md` | 427 | H3 curvature holonomy proof/diagnostic | `pulse_model/appendix/h3_pulse_comparison_holonomy.md` | Keep in core appendix group, with appendix index link | Same path remains public | `sci-i49.6` |
| `pulse_model/appendix/h4_stress_energy_as_phase_response.md` | 622 | H4 matter phase-response and stress-energy derivation | `pulse_model/appendix/h4_stress_energy_as_phase_response.md` | Keep in core appendix group, with appendix index link | Same path remains public | `sci-i49.6` |
| `pulse_model/appendix/h5_superposed_pulse_histories.md` | 365 | H5 quantum-clock/superposed-history visibility report | `pulse_model/appendix/h5_superposed_pulse_histories.md` | Keep in core appendix group, with appendix index link | Same path remains public | `sci-i49.6` |
| `pulse_model/appendix/h6_decohered_pulse_histories_classical_spacetime.md` | 507 | H6 decohered pulse histories and classical spacetime emergence report | `pulse_model/appendix/h6/decohered_pulse_histories_classical_spacetime.md` | Move into H6 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h6_quantum_source_response_discriminator.md` | 783 | H6S1 quantum source-response discriminator diagnostic | `pulse_model/appendix/h6/quantum_source_response_discriminator.md` | Move into H6 appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.6` |
| `pulse_model/appendix/h7_vacuum_phase_response.md` | 425 | H7 vacuum phase-response reformulation and report | `pulse_model/appendix/h7_vacuum_phase_response.md` | Keep in core appendix group, with appendix index link | Same path remains public | `sci-i49.6` |
| `pulse_model/appendix/geometry_phase_functional_from_pulse_consistency.md` | 695 | Step 5 base geometry phase functional argument | `pulse_model/appendix/geometry_action/phase_functional_from_pulse_consistency.md` | Move into geometry-action appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.7` |
| `pulse_model/appendix/geometry_action_strengthening_pulse_network.md` | 1189 | 05S pulse-network strengthening of geometry-action path | `pulse_model/appendix/geometry_action/pulse_network_strengthening.md` | Move into geometry-action appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.7` |
| `pulse_model/appendix/geometry_action_pulse_record_curvature_estimator.md` | 598 | 05S2 pulse-record curvature estimator and geometry-action gate | `pulse_model/appendix/geometry_action/pulse_record_curvature_estimator.md` | Move into geometry-action appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.7` |
| `pulse_model/appendix/geometry_action_correction_phenomenology.md` | 537 | 05S3 correction phenomenology and novelty gate | `pulse_model/appendix/geometry_action/correction_phenomenology.md` | Move into geometry-action appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.7` |
| `pulse_model/appendix/geometry_action_oriented_loop_phase.md` | 743 | 05S4 oriented-loop phase diagnostic | `pulse_model/appendix/geometry_action/oriented_loop_phase.md` | Move into geometry-action appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.7` |
| `pulse_model/appendix/geometry_action_spin_connection_holonomy.md` | 1200 | 05S5 spin/full-connection holonomy diagnostic | `pulse_model/appendix/geometry_action/spin_connection_holonomy.md` | Move into geometry-action appendix group | Old path must remain as compatibility note or verified redirect | `sci-i49.7` |
| `pulse_model/appendix/spin_connection_pulse_holonomy.md` | 19 | Existing compatibility note for renamed spin-connection appendix | `pulse_model/appendix/spin_connection_pulse_holonomy.md` | Keep or update as compatibility note to canonical spin-connection appendix | Same path remains public | `sci-i49.7` |

## Generated Or Cache Markdown Excluded From Research Migration

These files live under `pulse_model`, but they are generated dependency/cache artifacts, not Pulse Model research documents. They should not be moved into the research documentation structure.

| Current path | Lines | Role | Migration action |
|---|---:|---|---|
| `pulse_model/.venv/lib/python3.14/site-packages/pip/_vendor/idna/LICENSE.md` | 31 | Dependency license inside local virtual environment | Exclude from documentation migration |
| `pulse_model/.venv/lib/python3.14/site-packages/pip-26.0.dist-info/licenses/src/pip/_vendor/idna/LICENSE.md` | 31 | Dependency license inside local virtual environment | Exclude from documentation migration |
| `pulse_model/.pytest_cache/README.md` | 8 | Pytest cache readme | Exclude from documentation migration |

## Section-Level Split Map For The Formal Model

| Current formalization sections | Destination | Owner task |
|---|---|---|
| Abstract, 0 Reading guide, 1 Core hypothesis | `formal_model/index.md` and `formal_model/definitions_and_axioms.md` | `sci-i49.4` |
| 2 Current gaps in physics targeted by the model | `current_status.md` or `frontier_strategy.md`, with detailed copy preserved under `formal_model/index.md` | `sci-i49.2`, `sci-i49.4` |
| 3 Definitions and notation, 4 Axioms and principles | `formal_model/definitions_and_axioms.md` | `sci-i49.4` |
| 5 Known physics recovered, 5.15 Known-physics derivation audit | `formal_model/known_physics_recovery.md` | `sci-i49.4` |
| 6 Pulse Model as a bridge program, 15 Open conjectures, 18 Current best formal statement | `formal_model/hypotheses_h1_h7.md` | `sci-i49.4` |
| 7 Core mathematical object, 8 Important insights, 9 Testable extensions, 10 Failure modes and constraints | `formal_model/index.md` or focused subsections in `formal_model/hypotheses_h1_h7.md` | `sci-i49.4` |
| 11 Codex agent workstreams, 12 Suggested repository structure, 13 Minimal computational API, 20 Immediate next actions, 21 Short version for agents | Preserve as historical/current operating material inside `formal_model/validation_ladder.md` or compatibility page; mark historical if superseded by Beads and the new roadmap | `sci-i49.4`, `sci-i49.8` |
| 14 Validation ladder, 16 Success, 17 Failure | `formal_model/validation_ladder.md` | `sci-i49.4` |
| 19 References and starting sources | `formal_model/references.md` | `sci-i49.4` |

## Compatibility Paths To Preserve

The following old paths are important enough to remain valid after the restructure:

- `pulse_model/pulse_model_formalization.md`
- `pulse_model/proof_sequence.md`
- `pulse_model/promising_tweaks.md`
- `pulse_model/known_physics_validation_report.md`
- `pulse_model/h2_acceptance_report.md`
- every moved H2 appendix path under `pulse_model/appendix/`
- every moved H6 appendix path under `pulse_model/appendix/`
- every moved geometry-action appendix path under `pulse_model/appendix/`
- `pulse_model/appendix/spin_connection_pulse_holonomy.md`

The compatibility page may be a concise note that links to the canonical destination. It must not silently contradict the canonical verdict.

## Post-Migration No-Loss Audit

**Audit date:** June 8, 2026  
**Audit task:** `sci-i49.11`  
**Audit result:** Passed for documentation restructure content preservation.

### File Accounting

Every authored Markdown file listed in the original inventory is accounted for:

| Original role | Result |
|---|---|
| Reader index | `index.md` retained and updated to point to `current_status.md`, `roadmap.md`, `frontier_strategy.md`, `formal_model/`, `evidence/`, and `appendix/index.md`. |
| Formalization | `pulse_model_formalization.md` retained as the full-source compatibility page; focused content split into `formal_model/`. |
| Proof sequence | Full content mirrored to `roadmap.md`; `proof_sequence.md` retained as compatibility/full-content path. |
| Promising tweaks | Full content mirrored to `frontier_strategy.md`; `promising_tweaks.md` retained as compatibility/full-content path. |
| Known-physics validation | Full content mirrored to `evidence/known_physics_validation.md`; old path retained with canonical note. |
| H2 acceptance | Full content mirrored to `evidence/acceptance_reports/h2_metric_reconstruction.md`; old path retained with canonical note. |
| H1, H3, H4, H5, H7 appendices | Full technical files retained at original public paths with added frontmatter/status metadata where needed. |
| H2 appendices | Full technical files moved into `appendix/h2/`; old flat paths replaced by compatibility notes. |
| H6 appendices | Full technical files moved into `appendix/h6/`; old flat paths replaced by compatibility notes. |
| Geometry-action appendices | Full technical files moved into `appendix/geometry_action/`; old flat paths replaced by compatibility notes. |
| Review-2 spin path | `appendix/spin_connection_pulse_holonomy.md` retained and updated to the new canonical 05S5 path. |
| Review-2 | `reviews/review-2.md` retained with a path note explaining historical links. |
| Author/citation | `author_and_citation.md` retained. |

The generated `.venv` and `.pytest_cache` Markdown files remain excluded from the research documentation migration.

### Formalization Heading Accounting

The original `pulse_model_formalization.md` major sections are preserved as follows:

| Original sections | New canonical home |
|---|---|
| Abstract, reading guide, core hypothesis | `formal_model/index.md` and `formal_model/definitions_and_axioms.md` |
| Current gaps in physics | `formal_model/validation_ladder.md`, with reader-facing summary in `current_status.md` |
| Definitions and notation; axioms and principles | `formal_model/definitions_and_axioms.md` |
| Known physics recovered and derivation audit | `formal_model/known_physics_recovery.md` |
| H1-H7 bridge program, open conjectures, current best formal statement | `formal_model/hypotheses_h1_h7.md` |
| Core mathematical object, insights, testable extensions, failure modes | `formal_model/definitions_and_axioms.md` and `formal_model/validation_ladder.md` |
| Codex workstreams, suggested repository structure, minimal computational API | `formal_model/workstreams_and_api.md` |
| Validation ladder, success criteria, failure criteria, immediate next actions, short version | `formal_model/validation_ladder.md` |
| References and starting sources | `formal_model/references.md` |

The full original formalization remains available at `pulse_model_formalization.md`, so no formalization section was deleted.

### Verdict Preservation

The final verdicts and downstream boundaries are preserved in the canonical reader flow:

| Result | Preserved verdict |
|---|---|
| Known-physics validation | Accepted with limits for the conservative recovery ladder. |
| H1 | Accepted with limits for the conservative single-clock, single-time theorem. |
| H2 | Accepted for ideal fixed-event uniqueness; partially accepted for finite-data prototype slices; arbitrary sparse-record reconstruction not accepted. |
| H2S1 | Final project-rule classification: diagnostic tool. |
| H3 | Accepted with limits for the first fixed-event or gauge-fixed curvature-holonomy slice. |
| H4 | Accepted with limits for standard scalar, electromagnetic, and point-particle matter systems. |
| 05 | Accepted with limits as useful conservative low-energy geometry-action support. |
| 05S | Stronger conditional derivation; not a fundamental derivation from raw pulse data. |
| 05S2 | Useful constrained modification. |
| 05S3 | Useful bounded diagnostic only. |
| 05S4 | Useful bounded oriented-phase diagnostic. |
| 05S5 | Useful bounded torsion/connection diagnostic; review-2 classification diagnostic tool. |
| H5 | Accepted with limits for conservative quantum-clock visibility and weak-field proper-time inputs. |
| H6 | Accepted with limits for reduced branch-decoherence bookkeeping and model comparison; full emergence blocked. |
| H6S1 | Final project-rule classification: diagnostic tool. |
| H7 | Constrained reformulation accepted with limits; no cosmological-constant solution or testable deviation accepted. |

### Equations, Sources, Verification, And Artifacts

No equations, source citations, verification commands, or code/test artifact references were intentionally deleted.

Preservation checks used:

- Authored Markdown line-count scan after migration: 20,923 total lines, excluding generated `.venv` and `.pytest_cache` Markdown.
- Verdict grep across `roadmap.md`, `current_status.md`, `evidence/`, and `appendix/`.
- Verification/artifact grep for `src/pulse_model`, `tests/`, `Verification`, `unittest`, `pytest`, and `npm run build`.
- Old-path grep for moved files; remaining hits are in this migration map, review-2 historical links, compatibility/full-source pages, or historical workstream tree text.

### Intentional Deletions

No authored research content was intentionally deleted.

The only content excluded from the migration target was generated/cache Markdown under `.venv` and `.pytest_cache`, as recorded in the generated/cache inventory above.
