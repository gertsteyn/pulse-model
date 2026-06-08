# Appendix Compatibility Note: Spin Connection Pulse Holonomy

**Canonical source:** [05S5 Spin And Full Connection Holonomy Frontier](./geometry_action_spin_connection_holonomy.md)

This file is a compatibility artifact for the review-2 requested path `pulse_model/appendix/spin_connection_pulse_holonomy.md`.

The canonical 05S5 appendix is `pulse_model/appendix/geometry_action_spin_connection_holonomy.md`. It contains the spin/full-connection record contract, tetrad and spin-connection conventions, standard spinor recovery, H3 representation-lift theorem, bounded connection residual diagnostic, benchmarks, adversarial review, and final verdict.

This compatibility file does not fork the physics. It exists only so reviewers and agents looking for the review-2 filename can find the canonical 05S5 artifact.

The matching compatibility code paths are:

| Review-2 requested path | Compatibility path | Canonical source |
|---|---|---|
| `pulse_model/appendix/spin_connection_pulse_holonomy.md` | this file | `pulse_model/appendix/geometry_action_spin_connection_holonomy.md` |
| `pulse_model/src/pulse_model/spin_connection.py` | thin re-export module | `pulse_model/src/pulse_model/spin_connection_holonomy.py` |
| `pulse_model/tests/test_spin_connection.py` | smoke alias-contract test | `pulse_model/tests/test_spin_connection_holonomy.py` |

Use the canonical appendix for citations, verdicts, and scope decisions.
