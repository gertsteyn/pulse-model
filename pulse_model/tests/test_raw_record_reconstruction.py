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
    synthesize_meeting_case,
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
        self.assertNotIn("rank-deficient", reconstruction.degeneracy_labels)

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

    def test_rank_report_exposes_sparse_one_way_underdetermination(self) -> None:
        case = synthesize_static_reciprocal_signal_case(distance=1.0)
        one_way_record = RawEventRecord(
            clocks=case.raw_record.clocks,
            events=case.raw_record.events,
            signals=case.raw_record.signals[:1],
        )

        reconstruction = reconstruct_raw_event_graph(one_way_record, reference_clock_id="A")

        self.assertEqual(reconstruction.rank_report.variable_count, 2)
        self.assertEqual(reconstruction.rank_report.rank, 1)
        self.assertEqual(reconstruction.rank_report.nullity, 1)
        self.assertEqual(len(reconstruction.rank_report.nullspace_basis), 1)
        self.assertIn("rank-deficient", reconstruction.degeneracy_labels)
        self.assertIn("missing-reciprocal-signals", reconstruction.degeneracy_labels)

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


if __name__ == "__main__":
    unittest.main()

