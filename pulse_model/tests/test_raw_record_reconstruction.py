"""Executable H2S1 raw event-graph reconstruction checks."""

from __future__ import annotations

import unittest

from pulse_model.raw_record_reconstruction import (
    RawClock,
    RawClockEvent,
    RawEventRecord,
    RawMeeting,
    RawSignalLink,
    SyntheticRawCase,
    TruthEvent,
    merge_meeting_events,
    reconstruct_raw_event_graph,
    recover_event_order,
    synthesize_flat_three_clock_network,
    synthesize_inconsistent_record,
    synthesize_meeting_case,
    synthesize_single_clock_case,
    synthesize_sparse_underdetermined_case,
    synthesize_static_reciprocal_signal_case,
)


class RawRecordReconstructionTests(unittest.TestCase):
    def test_raw_schema_validation_rejects_bad_clock_event_and_signal_records(self) -> None:
        with self.assertRaises(ValueError):
            reconstruct_raw_event_graph(RawEventRecord(clocks=(), events=()))

        duplicate_clock_record = RawEventRecord(
            clocks=(RawClock("A", 1.0), RawClock("A", 1.0)),
            events=(RawClockEvent("A:0", "A", 0, 0.0),),
        )
        with self.assertRaises(ValueError):
            reconstruct_raw_event_graph(duplicate_clock_record)

        nonmonotone_record = RawEventRecord(
            clocks=(RawClock("A", 1.0),),
            events=(
                RawClockEvent("A:0", "A", 0, 2.0),
                RawClockEvent("A:1", "A", 1, 1.0),
            ),
        )
        with self.assertRaises(ValueError):
            recover_event_order(nonmonotone_record)

        signal_mismatch_record = RawEventRecord(
            clocks=(RawClock("A", 1.0), RawClock("B", 1.0)),
            events=(
                RawClockEvent("A:0", "A", 0, 0.0),
                RawClockEvent("B:1", "B", 0, 1.0),
            ),
            signals=(
                RawSignalLink("s", "A", "A:0", 3.0, "B", "B:1", 1.0),
            ),
        )
        with self.assertRaises(ValueError):
            reconstruct_raw_event_graph(signal_mismatch_record)

    def test_event_order_recovery_and_meeting_merge_constraints(self) -> None:
        case = synthesize_meeting_case(frequency_hz=2.0)
        reconstruction = reconstruct_raw_event_graph(case.raw_record, reference_clock_id="A")
        merge = reconstruction.meeting_merge

        self.assertEqual(
            reconstruction.ordered_event_ids_by_clock["A"],
            ("A:before", "A:meet", "A:after"),
        )
        self.assertEqual(reconstruction.ordered_event_ids_by_clock["B"], ("B:meet", "B:after"))
        self.assertEqual(
            merge.representative_by_event_id["A:meet"],
            merge.representative_by_event_id["B:meet"],
        )
        self.assertIn("A:before", reconstruction.partial_order.topological_order)
        self.assertIn("rank-deficient", reconstruction.degeneracy_labels)

    def test_meeting_conflict_is_rejected_before_embedding(self) -> None:
        record = RawEventRecord(
            clocks=(RawClock("A", 1.0), RawClock("B", 1.0)),
            events=(
                RawClockEvent("A:0", "A", 0, 0.0),
                RawClockEvent("A:1", "A", 1, 1.0),
                RawClockEvent("B:0", "B", 0, 0.0),
            ),
            meetings=(RawMeeting("bad", ("A:0", "A:1", "B:0")),),
        )

        with self.assertRaises(ValueError):
            merge_meeting_events(record)

    def test_static_reciprocal_signals_recover_simple_embedding_and_null_residuals(self) -> None:
        case = synthesize_static_reciprocal_signal_case(distance=3.0, frequency_hz=10.0)
        reconstruction = reconstruct_raw_event_graph(case.raw_record, reference_clock_id="A")
        coordinates = {coordinate.event_id: coordinate for coordinate in reconstruction.event_coordinates}

        self.assertAlmostEqual(coordinates["A:emit"].t, 0.0)
        self.assertAlmostEqual(coordinates["A:emit"].x, 0.0)
        self.assertAlmostEqual(coordinates["A:receive"].t, 6.0)
        self.assertAlmostEqual(coordinates["A:receive"].x, 0.0)
        self.assertAlmostEqual(coordinates["B:turn"].t, 3.0)
        self.assertAlmostEqual(coordinates["B:turn"].x, 3.0)
        self.assertTrue(all(residual.is_satisfied for residual in reconstruction.null_signal_residuals))
        self.assertTrue(all(abs(residual.residual) < 1.0e-12 for residual in reconstruction.null_signal_residuals))
        self.assertEqual(reconstruction.rank_report.variable_names, ("B.beta", "B.distance"))
        self.assertEqual(reconstruction.rank_report.rank, 2)
        self.assertEqual(reconstruction.rank_report.nullity, 0)
        self.assertEqual(reconstruction.rank_report.non_gauge_nullity, 0)
        self.assertNotIn("rank-deficient", reconstruction.degeneracy_labels)
        self.assertIn("mirror-boost-ambiguity", reconstruction.degeneracy_labels)
        self.assertIn("valid", reconstruction.degeneracy_labels)

    def test_uncalibrated_clock_reports_calibration_ambiguity(self) -> None:
        case = synthesize_static_reciprocal_signal_case(distance=1.0)
        record = RawEventRecord(
            clocks=(
                case.raw_record.clocks[0],
                RawClock("B", 1.0, calibration_status="uncalibrated"),
            ),
            events=case.raw_record.events,
            signals=case.raw_record.signals,
        )

        reconstruction = reconstruct_raw_event_graph(record, reference_clock_id="A")

        self.assertIn("calibration-ambiguity", reconstruction.degeneracy_labels)
        self.assertIn("valid", reconstruction.degeneracy_labels)
        self.assertIn("calibration_status", reconstruction.consumed_observed_fields)

    def test_non_reference_signal_is_included_in_rank_report(self) -> None:
        case = synthesize_flat_three_clock_network(frequency_hz=2.0)

        reconstruction = reconstruct_raw_event_graph(case.raw_record, reference_clock_id="A")

        self.assertEqual(case.generator_case_id, "flat_three_clock_network")
        self.assertIn("s-bc", reconstruction.rank_report.residual_names)
        self.assertEqual(reconstruction.rank_report.variable_count, 4)
        self.assertEqual(reconstruction.rank_report.residual_count, 5)
        self.assertEqual(reconstruction.rank_report.rank, 4)
        self.assertTrue(all(residual.is_satisfied for residual in reconstruction.null_signal_residuals))
        self.assertIn("valid", reconstruction.degeneracy_labels)

    def test_non_reference_signal_uses_the_resolved_orientation_branch(self) -> None:
        record = RawEventRecord(
            clocks=(RawClock("A", 1.0), RawClock("B", 1.0), RawClock("C", 1.0)),
            events=(
                RawClockEvent("A:0", "A", 0, 0.0),
                RawClockEvent("A:2", "A", 1, 2.0),
                RawClockEvent("A:4", "A", 2, 4.0),
                RawClockEvent("B:1", "B", 0, 1.0),
                RawClockEvent("B:3", "B", 1, 3.0),
                RawClockEvent("C:2", "C", 0, 2.0),
            ),
            signals=(
                RawSignalLink("s-ab", "A", "A:0", 0.0, "B", "B:1", 1.0),
                RawSignalLink("s-ba", "B", "B:1", 1.0, "A", "A:2", 2.0),
                RawSignalLink("s-ac", "A", "A:0", 0.0, "C", "C:2", 2.0),
                RawSignalLink("s-ca", "C", "C:2", 2.0, "A", "A:4", 4.0),
                RawSignalLink("s-cb", "C", "C:2", 2.0, "B", "B:3", 3.0),
            ),
        )

        reconstruction = reconstruct_raw_event_graph(record, reference_clock_id="A")

        self.assertIn("s-cb", reconstruction.rank_report.residual_names)
        self.assertEqual(reconstruction.rank_report.rank, 4)
        self.assertNotIn("noisy-inconsistency", reconstruction.degeneracy_labels)
        self.assertTrue(all(residual.is_satisfied for residual in reconstruction.null_signal_residuals))

    def test_rank_report_exposes_sparse_one_way_underdetermination(self) -> None:
        case = synthesize_sparse_underdetermined_case()

        reconstruction = reconstruct_raw_event_graph(case.raw_record, reference_clock_id="A")

        self.assertEqual(case.generator_case_id, "sparse_underdetermined")
        self.assertEqual(reconstruction.rank_report.variable_count, 2)
        self.assertEqual(reconstruction.rank_report.rank, 1)
        self.assertEqual(reconstruction.rank_report.nullity, 1)
        self.assertEqual(len(reconstruction.rank_report.nullspace_basis), 1)
        self.assertIn("rank-deficient", reconstruction.degeneracy_labels)
        self.assertIn("missing-reciprocal-signals", reconstruction.degeneracy_labels)
        self.assertIn("valid", reconstruction.degeneracy_labels)
        self.assertNotIn("noisy-inconsistency", reconstruction.degeneracy_labels)
        self.assertEqual(reconstruction.event_coordinates, ())
        self.assertEqual(reconstruction.null_signal_residuals, ())

    def test_partial_order_cycle_is_rejected_as_inconsistent_record(self) -> None:
        record = RawEventRecord(
            clocks=(RawClock("A", 1.0), RawClock("B", 1.0)),
            events=(
                RawClockEvent("A:0", "A", 0, 0.0),
                RawClockEvent("A:1", "A", 1, 1.0),
                RawClockEvent("B:0", "B", 0, 0.0),
            ),
            signals=(
                RawSignalLink("s0", "A", "A:1", 1.0, "B", "B:0", 0.0),
            ),
            meetings=(RawMeeting("m0", ("A:0", "B:0")),),
        )

        with self.assertRaises(ValueError):
            reconstruct_raw_event_graph(record)

    def test_generator_only_coordinates_do_not_leak_into_solver_inputs(self) -> None:
        case = synthesize_static_reciprocal_signal_case(distance=2.0, frequency_hz=5.0)
        altered_truth_case = SyntheticRawCase(
            raw_record=case.raw_record,
            truth_events=(
                TruthEvent("A:emit", 100.0, 200.0, 300.0),
                TruthEvent("A:receive", 400.0, 500.0, 600.0),
                TruthEvent("B:turn", 700.0, 800.0, 900.0),
            ),
            generator_case_id="tampered_truth_sidecar",
        )

        original = reconstruct_raw_event_graph(case.raw_record, reference_clock_id="A")
        tampered = reconstruct_raw_event_graph(altered_truth_case.raw_record, reference_clock_id="A")

        self.assertEqual(original.event_coordinates, tampered.event_coordinates)
        self.assertEqual(original.null_signal_residuals, tampered.null_signal_residuals)
        self.assertNotIn("t", original.consumed_observed_fields)
        self.assertNotIn("x", original.consumed_observed_fields)
        self.assertNotIn("truth_event_id", original.consumed_observed_fields)

    def test_generator_contract_cases_are_available(self) -> None:
        cases = (
            synthesize_single_clock_case(),
            synthesize_static_reciprocal_signal_case(),
            synthesize_meeting_case(),
            synthesize_flat_three_clock_network(),
            synthesize_sparse_underdetermined_case(),
        )

        self.assertEqual(
            {case.generator_case_id for case in cases},
            {
                "single_inertial_clock",
                "separated_inertial_clocks",
                "crossing_inertial_clocks",
                "flat_three_clock_network",
                "sparse_underdetermined",
            },
        )
        single = reconstruct_raw_event_graph(cases[0].raw_record, reference_clock_id="A")
        self.assertIn("insufficient-clocks", single.degeneracy_labels)
        self.assertIn("valid", single.degeneracy_labels)

        inconsistent = synthesize_inconsistent_record()
        self.assertEqual(inconsistent.generator_case_id, "inconsistent_record")
        with self.assertRaises(ValueError):
            reconstruct_raw_event_graph(inconsistent.raw_record)


if __name__ == "__main__":
    unittest.main()
