# Pulse Model

The Pulse Model is a research project about time, clocks, quantum phase, and
gravity.

Its starting idea is that time is not a universal background flow. Time is what
physical systems locally accumulate and what clocks count. The project asks
whether spacetime can be understood as the rule system that keeps local clock
counts and quantum phase histories consistent with each other.

This is a research program, not a claimed finished theory. The model must first
reproduce known physics, then make any new claims precise enough to prove,
simulate, or falsify.

## Read The Docs

The published documentation is here:

https://gertsteyn.github.io/pulse-model/

Useful starting points in the repository:

- [Overview](pulse_model/index.md)
- [The formal Pulse Model](pulse_model/pulse_model_formalization.md)
- [Proof sequence](pulse_model/proof_sequence.md)
- [Known-physics validation report](pulse_model/known_physics_validation_report.md)

## Repository Layout

- `pulse_model/` contains the research documents.
- `pulse_model/appendix/` contains focused proofs and formal targets.
- `pulse_model/src/pulse_model/` contains the Python calculation helpers.
- `pulse_model/tests/` contains the known-physics and model-check tests.
- `docusaurus.config.ts` configures the documentation site.

## Local Development

Install and run the documentation site:

```bash
npm ci
npm run start
```

Build and typecheck the site:

```bash
npm run typecheck
npm run build
```

Run the Python checks from the model package:

```bash
cd pulse_model
uv run pytest
```

The Python package currently targets Python `>=3.14,<3.15`.

## Publishing

The documentation is deployed to GitHub Pages from GitHub Actions when changes
land on `main`.

## License

Research text, documentation, diagrams, and other non-code content are licensed
under the [Creative Commons Attribution 4.0 International License](LICENSE-DOCS.md).

Source code is licensed under the [Apache License, Version 2.0](LICENSE).

Recommended attribution:

```text
Pulse Model, Gert Steyn, https://gertsteyn.github.io/pulse-model/
```

Citation metadata is available in [CITATION.cff](CITATION.cff).
