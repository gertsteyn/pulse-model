"""Executable H1 toy model for pulse-conditioned single-time evolution."""

from __future__ import annotations

import math
from dataclasses import dataclass


_LEADING_UNIFORM_WINDOW_MAX_PHASE_WIDTH_RAD = 1.0


@dataclass(frozen=True)
class PulseConditionedTwoLevelModel:
    """Two-level system conditioned on a calibrated pulse counter.

    The model uses the finite-dimensional Hamiltonian
    ``H = hbar * omega / 2 * sigma_x`` with initial state ``|0>`` and measures
    the excited-state projector ``|1><1|``. Standard evolution gives
    ``P(1; tau) = sin(omega * tau / 2)^2``.
    """

    clock_frequency_hz: float
    rabi_angular_frequency_rad_per_s: float

    def __post_init__(self) -> None:
        _require_positive("clock_frequency_hz", self.clock_frequency_hz)
        _require_nonnegative(
            "rabi_angular_frequency_rad_per_s",
            self.rabi_angular_frequency_rad_per_s,
        )

    def proper_time_at_pulse_count_s(self, pulse_count: float) -> float:
        """Return calibrated clock proper time, tau = n / f_C."""

        _require_finite("pulse_count", pulse_count)
        if pulse_count < 0.0:
            raise ValueError("pulse_count must be nonnegative")

        return pulse_count / self.clock_frequency_hz

    def standard_excited_probability(self, proper_time_s: float) -> float:
        """Return ordinary Born probability at a proper-time parameter."""

        _require_nonnegative("proper_time_s", proper_time_s)

        angle = 0.5 * self.rabi_angular_frequency_rad_per_s * proper_time_s
        return math.sin(angle) ** 2

    def sharp_window_excited_probability(self, pulse_count: float) -> float:
        """Return the sharp-readout relational probability at pulse count n."""

        proper_time_s = self.proper_time_at_pulse_count_s(pulse_count)
        return self.standard_excited_probability(proper_time_s)

    def finite_window_excited_probability(
        self,
        center_pulse_count: float,
        window_width_pulses: float,
    ) -> float:
        """Return the uniform finite-window relational probability.

        This computes:

        ``(1 / delta_tau) * integral_W sin(omega * tau / 2)^2 d tau``

        for the proper-time window centered at ``center_pulse_count / f_C``.
        A zero-width window returns the sharp-readout value.
        """

        _require_uniform_window_in_nonnegative_domain(
            center_pulse_count,
            window_width_pulses,
        )
        center_proper_time_s = self.proper_time_at_pulse_count_s(center_pulse_count)

        omega = self.rabi_angular_frequency_rad_per_s
        if window_width_pulses == 0.0 or omega == 0.0:
            return self.standard_excited_probability(center_proper_time_s)

        window_width_s = window_width_pulses / self.clock_frequency_hz
        phase_width = omega * window_width_s
        averaged_cosine = (
            2.0
            * math.sin(0.5 * phase_width)
            * math.cos(omega * center_proper_time_s)
            / phase_width
        )
        return 0.5 * (1.0 - averaged_cosine)

    def leading_resolution_correction(
        self,
        center_pulse_count: float,
        resolution_stddev_pulses: float,
    ) -> float:
        """Return the leading finite-resolution correction to the sharp result.

        For a normalized symmetric readout kernel with pulse-count standard
        deviation ``resolution_stddev_pulses``, the correction is
        ``sigma_tau^2 / 2 * P''(tau_n)``. In this two-level model,
        ``P''(tau_n) = omega^2 / 2 * cos(omega * tau_n)``.
        """

        center_proper_time_s = self.proper_time_at_pulse_count_s(center_pulse_count)
        _require_nonnegative("resolution_stddev_pulses", resolution_stddev_pulses)

        sigma_tau_s = resolution_stddev_pulses / self.clock_frequency_hz
        omega = self.rabi_angular_frequency_rad_per_s
        return 0.25 * sigma_tau_s**2 * omega**2 * math.cos(omega * center_proper_time_s)

    def leading_uniform_window_resolution_probability(
        self,
        center_pulse_count: float,
        window_width_pulses: float,
    ) -> float:
        """Return the small-window leading probability for a uniform window.

        This approximation is only used when ``omega * delta_tau <= 1``.
        Use ``finite_window_excited_probability`` for wider uniform windows.
        """

        _require_uniform_window_in_nonnegative_domain(
            center_pulse_count,
            window_width_pulses,
        )
        _require_small_uniform_window_phase_width(
            self.rabi_angular_frequency_rad_per_s,
            window_width_pulses / self.clock_frequency_hz,
        )

        resolution_stddev_pulses = window_width_pulses / math.sqrt(12.0)
        return self.sharp_window_excited_probability(
            center_pulse_count
        ) + self.leading_resolution_correction(
            center_pulse_count,
            resolution_stddev_pulses,
        )


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_uniform_window_in_nonnegative_domain(
    center_pulse_count: float,
    window_width_pulses: float,
) -> None:
    _require_nonnegative("center_pulse_count", center_pulse_count)
    _require_nonnegative("window_width_pulses", window_width_pulses)
    if center_pulse_count - 0.5 * window_width_pulses < 0.0:
        raise ValueError("uniform window must not extend below pulse_count 0")


def _require_small_uniform_window_phase_width(
    rabi_angular_frequency_rad_per_s: float,
    window_width_s: float,
) -> None:
    phase_width = rabi_angular_frequency_rad_per_s * window_width_s
    if phase_width > _LEADING_UNIFORM_WINDOW_MAX_PHASE_WIDTH_RAD:
        raise ValueError(
            "omega * window_width_pulses / clock_frequency_hz must be <= 1 "
            "for leading uniform-window approximation"
        )


def _require_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")
