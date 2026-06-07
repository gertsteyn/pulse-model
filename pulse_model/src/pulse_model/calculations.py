"""Pure SI-unit calculations for the conservative Pulse Model layer."""

from __future__ import annotations

import math
from collections.abc import Iterable

SPEED_OF_LIGHT_M_PER_S = 299_792_458.0
REDUCED_PLANCK_CONSTANT_J_S = 1.054_571_817e-34
GRAVITATIONAL_CONSTANT_M3_PER_KG_S2 = 6.674_30e-11
MEGAPARSEC_M = 3.085_677_581_491_367e22


def proper_time_flat(
    coordinate_time_s: float,
    velocity_m_per_s: float,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return flat-spacetime proper time for inertial motion.

    Args:
        coordinate_time_s: Elapsed inertial-frame coordinate time in seconds.
        velocity_m_per_s: Speed magnitude in meters per second.
        speed_of_light_m_per_s: Speed of light in meters per second.
    """

    _require_nonnegative("coordinate_time_s", coordinate_time_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)
    _require_finite("velocity_m_per_s", velocity_m_per_s)

    if abs(velocity_m_per_s) > speed_of_light_m_per_s:
        raise ValueError("velocity_m_per_s must not exceed speed_of_light_m_per_s")

    beta_squared = (velocity_m_per_s / speed_of_light_m_per_s) ** 2
    return coordinate_time_s * math.sqrt(max(0.0, 1.0 - beta_squared))


def weak_field_dtaudt(
    potential_m2_per_s2: float,
    velocity_m_per_s: float,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return weak-field, low-velocity d tau / dt.

    The convention is Phi -> 0 at infinity, so a deeper gravitational
    potential has a more negative ``potential_m2_per_s2``.
    """

    _require_finite("potential_m2_per_s2", potential_m2_per_s2)
    _require_finite("velocity_m_per_s", velocity_m_per_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    c_squared = speed_of_light_m_per_s**2
    return 1.0 + potential_m2_per_s2 / c_squared - velocity_m_per_s**2 / (2.0 * c_squared)


def weak_field_delta_tau_s(
    coordinate_time_s: float,
    branch_1_potential_m2_per_s2: float,
    branch_2_potential_m2_per_s2: float,
    branch_1_velocity_m_per_s: float = 0.0,
    branch_2_velocity_m_per_s: float = 0.0,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return weak-field, low-velocity branch proper-time difference.

    The returned sign is ``tau_1 - tau_2`` for two branches held over a common
    coordinate-time interval with constant potentials and speed magnitudes.
    """

    _require_nonnegative("coordinate_time_s", coordinate_time_s)
    _require_not_superluminal(
        "branch_1_velocity_m_per_s",
        branch_1_velocity_m_per_s,
        speed_of_light_m_per_s,
    )
    _require_not_superluminal(
        "branch_2_velocity_m_per_s",
        branch_2_velocity_m_per_s,
        speed_of_light_m_per_s,
    )

    branch_1_rate = weak_field_dtaudt(
        branch_1_potential_m2_per_s2,
        branch_1_velocity_m_per_s,
        speed_of_light_m_per_s,
    )
    branch_2_rate = weak_field_dtaudt(
        branch_2_potential_m2_per_s2,
        branch_2_velocity_m_per_s,
        speed_of_light_m_per_s,
    )
    return coordinate_time_s * (branch_1_rate - branch_2_rate)


def height_delta_tau_s(
    coordinate_time_s: float,
    height_difference_m: float,
    gravity_m_per_s2: float = 9.806_65,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return uniform-field height contribution to ``tau_1 - tau_2``.

    A positive ``height_difference_m`` means branch 1 is higher than branch 2
    when ``gravity_m_per_s2`` is positive.
    """

    _require_finite("height_difference_m", height_difference_m)
    _require_finite("gravity_m_per_s2", gravity_m_per_s2)
    return weak_field_delta_tau_s(
        coordinate_time_s,
        gravity_m_per_s2 * height_difference_m,
        0.0,
        speed_of_light_m_per_s=speed_of_light_m_per_s,
    )


def velocity_delta_tau_s(
    coordinate_time_s: float,
    branch_1_velocity_m_per_s: float,
    branch_2_velocity_m_per_s: float,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return low-velocity time-dilation contribution to ``tau_1 - tau_2``."""

    return weak_field_delta_tau_s(
        coordinate_time_s,
        0.0,
        0.0,
        branch_1_velocity_m_per_s,
        branch_2_velocity_m_per_s,
        speed_of_light_m_per_s,
    )


def schwarzschild_radius(
    mass_kg: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return the Schwarzschild radius ``2 G M / c^2`` in meters."""

    _require_nonnegative("mass_kg", mass_kg)
    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    return 2.0 * gravitational_constant_m3_per_kg_s2 * mass_kg / speed_of_light_m_per_s**2


def schwarzschild_static_dtaudt(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return exact Schwarzschild ``d tau / dt`` for a static outside clock.

    The result applies outside a non-rotating spherical mass in Schwarzschild
    coordinates. Static clocks are not valid at or inside the Schwarzschild
    radius, so those radii raise ``ValueError``.
    """

    schwarzschild_radius_m = _require_schwarzschild_outside_radius(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    return math.sqrt(1.0 - schwarzschild_radius_m / radius_m)


def schwarzschild_radial_freefall_from_rest_at_infinity_dtaudt(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return ``dt / d tau`` for radial Schwarzschild free fall from infinity.

    The geodesic starts at rest at infinity and is evaluated outside the
    Schwarzschild radius. The result uses Schwarzschild coordinate time.
    """

    schwarzschild_radius_m = _require_schwarzschild_outside_radius(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    return 1.0 / (1.0 - schwarzschild_radius_m / radius_m)


def schwarzschild_radial_freefall_from_rest_at_infinity_drdtau_m_per_s(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return inward ``dr / d tau`` for radial free fall from rest at infinity."""

    schwarzschild_radius_m = _require_schwarzschild_outside_radius(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    return -speed_of_light_m_per_s * math.sqrt(schwarzschild_radius_m / radius_m)


def schwarzschild_radial_null_coordinate_speed_m_per_s(
    mass_kg: float,
    radius_m: float,
    outward: bool = True,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return ``dr / dt`` for a radial null ray in Schwarzschild coordinates."""

    schwarzschild_radius_m = _require_schwarzschild_outside_radius(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    sign = 1.0 if outward else -1.0
    return sign * speed_of_light_m_per_s * (1.0 - schwarzschild_radius_m / radius_m)


def schwarzschild_radial_null_light_time_s(
    mass_kg: float,
    start_radius_m: float,
    end_radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return Schwarzschild-coordinate light time for a radial null segment."""

    schwarzschild_radius_m = _require_schwarzschild_outside_radius(
        mass_kg,
        start_radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )
    _require_schwarzschild_outside_radius(
        mass_kg,
        end_radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    tortoise_delta_m = (end_radius_m - start_radius_m) + schwarzschild_radius_m * math.log(
        (end_radius_m - schwarzschild_radius_m)
        / (start_radius_m - schwarzschild_radius_m)
    )
    return abs(tortoise_delta_m) / speed_of_light_m_per_s


def schwarzschild_tidal_eigenvalues_per_s2(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
) -> tuple[float, float, float]:
    """Return local Schwarzschild geodesic-deviation eigenvalues.

    The tuple is ``(radial, transverse, transverse)`` in reciprocal seconds
    squared. Multiplying an eigenvalue by a local separation gives the
    corresponding relative acceleration component.
    """

    _require_nonnegative("mass_kg", mass_kg)
    _require_positive("radius_m", radius_m)
    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)

    transverse_per_s2 = -gravitational_constant_m3_per_kg_s2 * mass_kg / radius_m**3
    radial_per_s2 = -2.0 * transverse_per_s2
    return radial_per_s2, transverse_per_s2, transverse_per_s2


def de_sitter_static_dtaudt(
    cosmological_constant_per_m2: float,
    radius_m: float,
) -> float:
    """Return static-patch de Sitter ``d tau / dt``.

    The benchmark uses ``ds^2 = -(1 - Lambda r^2 / 3)c^2 dt^2 + ...`` and is
    valid inside the cosmological horizon for nonnegative ``Lambda``.
    """

    _require_nonnegative("cosmological_constant_per_m2", cosmological_constant_per_m2)
    _require_nonnegative("radius_m", radius_m)

    metric_factor = 1.0 - cosmological_constant_per_m2 * radius_m**2 / 3.0
    if metric_factor <= 0.0:
        raise ValueError("radius_m must be inside the de Sitter static horizon")

    return math.sqrt(metric_factor)


def hubble_parameter_per_s(
    hubble_km_per_s_mpc: float,
    megaparsec_m: float = MEGAPARSEC_M,
) -> float:
    """Return a Hubble parameter in reciprocal seconds."""

    _require_positive("hubble_km_per_s_mpc", hubble_km_per_s_mpc)
    _require_positive("megaparsec_m", megaparsec_m)

    return hubble_km_per_s_mpc * 1000.0 / megaparsec_m


def critical_density_energy_j_per_m3(
    hubble_km_per_s_mpc: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return the critical energy density ``3 H^2 c^2 / (8 pi G)``."""

    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    hubble_per_s = hubble_parameter_per_s(hubble_km_per_s_mpc)
    return (
        3.0
        * hubble_per_s**2
        * speed_of_light_m_per_s**2
        / (8.0 * math.pi * gravitational_constant_m3_per_kg_s2)
    )


def dark_energy_density_j_per_m3(
    hubble_km_per_s_mpc: float,
    dark_energy_fraction: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return ``Omega_DE`` times the critical energy density."""

    _require_nonnegative("dark_energy_fraction", dark_energy_fraction)

    return dark_energy_fraction * critical_density_energy_j_per_m3(
        hubble_km_per_s_mpc,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )


def cosmological_constant_from_energy_density_per_m2(
    energy_density_j_per_m3: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return ``Lambda = 8 pi G rho / c^4`` for a vacuum energy density."""

    _require_nonnegative("energy_density_j_per_m3", energy_density_j_per_m3)
    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    return (
        8.0
        * math.pi
        * gravitational_constant_m3_per_kg_s2
        * energy_density_j_per_m3
        / speed_of_light_m_per_s**4
    )


def cosmological_constant_from_hubble_fraction_per_m2(
    hubble_km_per_s_mpc: float,
    dark_energy_fraction: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return the effective ``Lambda`` implied by ``H0`` and ``Omega_DE``."""

    return cosmological_constant_from_energy_density_per_m2(
        dark_energy_density_j_per_m3(
            hubble_km_per_s_mpc,
            dark_energy_fraction,
            gravitational_constant_m3_per_kg_s2,
            speed_of_light_m_per_s,
        ),
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )


def vacuum_energy_hierarchy_ratio(
    candidate_vacuum_density_j_per_m3: float,
    observed_dark_energy_density_j_per_m3: float,
) -> float:
    """Return candidate vacuum energy density divided by the observed scale."""

    _require_nonnegative("candidate_vacuum_density_j_per_m3", candidate_vacuum_density_j_per_m3)
    _require_positive("observed_dark_energy_density_j_per_m3", observed_dark_energy_density_j_per_m3)

    return candidate_vacuum_density_j_per_m3 / observed_dark_energy_density_j_per_m3


def cpl_dark_energy_density_ratio(
    scale_factor: float,
    w0: float = -1.0,
    wa: float = 0.0,
) -> float:
    """Return ``rho_DE(a) / rho_DE(1)`` for the CPL ``w0-wa`` model."""

    _require_positive("scale_factor", scale_factor)
    _require_finite("w0", w0)
    _require_finite("wa", wa)

    power = -3.0 * (1.0 + w0 + wa)
    return scale_factor**power * math.exp(3.0 * wa * (scale_factor - 1.0))


def schwarzschild_circular_geodesic_angular_frequency(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return Schwarzschild circular-geodesic coordinate angular frequency.

    The result is ``d phi / dt`` in radians per second for an equatorial
    timelike circular geodesic, using Schwarzschild coordinate time ``t``.
    Timelike circular geodesics require ``radius_m > 3 G M / c^2``.
    """

    _require_schwarzschild_timelike_circular_geodesic_radius(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    return math.sqrt(gravitational_constant_m3_per_kg_s2 * mass_kg / radius_m**3)


def schwarzschild_circular_geodesic_dtaudt(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float = GRAVITATIONAL_CONSTANT_M3_PER_KG_S2,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return exact ``d tau / dt`` for a timelike circular Schwarzschild geodesic.

    This includes the gravitational and orbital-motion contributions for a
    free circular orbit. The result is not the static-clock rate.
    """

    _require_schwarzschild_timelike_circular_geodesic_radius(
        mass_kg,
        radius_m,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    return math.sqrt(
        1.0
        - 3.0
        * gravitational_constant_m3_per_kg_s2
        * mass_kg
        / (radius_m * speed_of_light_m_per_s**2)
    )


def pulse_count(frequency_hz: float, proper_time_s: float) -> float:
    """Return accumulated pulse count for a stable clock transition."""

    _require_nonnegative("frequency_hz", frequency_hz)
    _require_nonnegative("proper_time_s", proper_time_s)

    return frequency_hz * proper_time_s


def free_massive_phase(
    mass_kg: float,
    proper_time_s: float,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> float:
    """Return dimensionless free massive action phase, S / hbar."""

    _require_nonnegative("mass_kg", mass_kg)
    _require_nonnegative("proper_time_s", proper_time_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)
    _require_positive("reduced_planck_constant_j_s", reduced_planck_constant_j_s)

    return -(mass_kg * speed_of_light_m_per_s**2 * proper_time_s) / reduced_planck_constant_j_s


def gravitational_redshift(
    emitter_potential_m2_per_s2: float,
    receiver_potential_m2_per_s2: float,
    speed_of_light_m_per_s: float = SPEED_OF_LIGHT_M_PER_S,
) -> float:
    """Return weak-field fractional shift (nu_received - nu_emitted) / nu_emitted."""

    _require_finite("emitter_potential_m2_per_s2", emitter_potential_m2_per_s2)
    _require_finite("receiver_potential_m2_per_s2", receiver_potential_m2_per_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    return (emitter_potential_m2_per_s2 - receiver_potential_m2_per_s2) / speed_of_light_m_per_s**2


def cow_phase_shift(
    mass_kg: float,
    gravity_m_per_s2: float,
    area_m2: float,
    velocity_m_per_s: float,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> float:
    """Return the COW gravitational phase shift for a uniform field.

    Positive inputs return the benchmark magnitude m g A / (hbar v). A signed
    ``area_m2`` may be used to encode an interferometer orientation convention.
    """

    _require_nonnegative("mass_kg", mass_kg)
    _require_finite("gravity_m_per_s2", gravity_m_per_s2)
    _require_finite("area_m2", area_m2)
    _require_positive("velocity_m_per_s", velocity_m_per_s)
    _require_positive("reduced_planck_constant_j_s", reduced_planck_constant_j_s)

    return mass_kg * gravity_m_per_s2 * area_m2 / (reduced_planck_constant_j_s * velocity_m_per_s)


def clock_visibility(
    delta_tau_s: float,
    energy_levels_j: Iterable[float],
    probabilities: Iterable[float],
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> float:
    """Return internal-clock path visibility for discrete energy levels."""

    _require_finite("delta_tau_s", delta_tau_s)
    _require_positive("reduced_planck_constant_j_s", reduced_planck_constant_j_s)

    energies = list(energy_levels_j)
    weights = list(probabilities)

    if not energies:
        raise ValueError("energy_levels_j must not be empty")
    if len(energies) != len(weights):
        raise ValueError("energy_levels_j and probabilities must have the same length")

    for index, energy in enumerate(energies):
        _require_finite(f"energy_levels_j[{index}]", energy)
    for index, probability in enumerate(weights):
        _require_nonnegative(f"probabilities[{index}]", probability)

    total_probability = math.fsum(weights)
    if not math.isclose(total_probability, 1.0, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("probabilities must sum to 1")

    real = 0.0
    imag = 0.0
    for energy, probability in zip(energies, weights, strict=True):
        phase = energy * delta_tau_s / reduced_planck_constant_j_s
        real += probability * math.cos(phase)
        imag -= probability * math.sin(phase)

    return math.hypot(real, imag)


def clock_visibility_series(
    delta_tau_values_s: Iterable[float],
    energy_levels_j: Iterable[float],
    probabilities: Iterable[float],
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> list[float]:
    """Return visibility values for a sequence of proper-time differences."""

    energies = list(energy_levels_j)
    weights = list(probabilities)
    return [
        clock_visibility(
            delta_tau_s,
            energies,
            weights,
            reduced_planck_constant_j_s,
        )
        for delta_tau_s in delta_tau_values_s
    ]


def two_level_clock_visibility(
    delta_tau_s: float,
    transition_frequency_hz: float,
    excited_state_probability: float = 0.5,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> float:
    """Return the H5 visibility benchmark for a two-level clock.

    ``transition_frequency_hz`` is the clock transition frequency, so the
    energy gap is ``2 pi hbar f``. ``excited_state_probability`` is the initial
    state's energy-basis weight in the excited state.
    """

    _require_nonnegative("transition_frequency_hz", transition_frequency_hz)
    _require_probability("excited_state_probability", excited_state_probability)
    _require_positive("reduced_planck_constant_j_s", reduced_planck_constant_j_s)

    energy_gap_j = 2.0 * math.pi * reduced_planck_constant_j_s * transition_frequency_hz
    return clock_visibility(
        delta_tau_s,
        [0.0, energy_gap_j],
        [1.0 - excited_state_probability, excited_state_probability],
        reduced_planck_constant_j_s,
    )


def two_level_clock_visibility_series(
    delta_tau_values_s: Iterable[float],
    transition_frequency_hz: float,
    excited_state_probability: float = 0.5,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> list[float]:
    """Return two-level clock visibility values across a delta-tau grid."""

    return [
        two_level_clock_visibility(
            delta_tau_s,
            transition_frequency_hz,
            excited_state_probability,
            reduced_planck_constant_j_s,
        )
        for delta_tau_s in delta_tau_values_s
    ]


def gaussian_energy_spread_visibility(
    delta_tau_s: float,
    energy_stddev_j: float,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> float:
    """Return the Gaussian broad-energy visibility envelope.

    This is ``exp(-sigma_E^2 delta_tau^2 / (2 hbar^2))``. It models the
    characteristic-function envelope for a broad energy distribution and does
    not include environmental or technical contrast loss.
    """

    _require_finite("delta_tau_s", delta_tau_s)
    _require_nonnegative("energy_stddev_j", energy_stddev_j)
    _require_positive("reduced_planck_constant_j_s", reduced_planck_constant_j_s)

    scaled_time = energy_stddev_j * delta_tau_s / reduced_planck_constant_j_s
    return math.exp(-0.5 * scaled_time**2)


def gaussian_energy_spread_visibility_series(
    delta_tau_values_s: Iterable[float],
    energy_stddev_j: float,
    reduced_planck_constant_j_s: float = REDUCED_PLANCK_CONSTANT_J_S,
) -> list[float]:
    """Return Gaussian broad-energy visibility values across a delta-tau grid."""

    return [
        gaussian_energy_spread_visibility(
            delta_tau_s,
            energy_stddev_j,
            reduced_planck_constant_j_s,
        )
        for delta_tau_s in delta_tau_values_s
    ]


def gaussian_branch_record_overlap(
    record_separation: float,
    coherence_width: float = 1.0,
) -> float:
    """Return a toy Gaussian overlap between two branch records.

    The inputs are dimensionless reduced-model coordinates. The same helper can
    represent an ordinary environmental record overlap or a metric-history
    record overlap, but callers should keep those factors separate.
    """

    _require_finite("record_separation", record_separation)
    _require_positive("coherence_width", coherence_width)

    scaled_separation = record_separation / coherence_width
    return math.exp(-0.5 * scaled_separation**2)


def combined_branch_overlap(
    clock_overlap: float,
    environmental_overlap: float = 1.0,
    metric_history_overlap: float = 1.0,
    technical_overlap: float = 1.0,
) -> float:
    """Return the H6 reduced branch-overlap magnitude.

    The factors are visibility or overlap magnitudes in ``[0, 1]``. Keeping
    ``environmental_overlap`` and ``metric_history_overlap`` separate prevents
    ordinary environmental decoherence from being mislabeled as a metric-history
    effect.
    """

    _require_probability("clock_overlap", clock_overlap)
    _require_probability("environmental_overlap", environmental_overlap)
    _require_probability("metric_history_overlap", metric_history_overlap)
    _require_probability("technical_overlap", technical_overlap)

    return clock_overlap * environmental_overlap * metric_history_overlap * technical_overlap


def branch_distinguishability(
    clock_overlap: float,
    environmental_overlap: float = 1.0,
    metric_history_overlap: float = 1.0,
    technical_overlap: float = 1.0,
) -> float:
    """Return the reduced branch distinguishability ``1 - |Gamma|``."""

    return 1.0 - combined_branch_overlap(
        clock_overlap,
        environmental_overlap,
        metric_history_overlap,
        technical_overlap,
    )


def two_branch_coherence_magnitude(
    branch_probability: float,
    total_branch_overlap: float,
) -> float:
    """Return the off-diagonal magnitude for a two-branch reduced state."""

    _require_probability("branch_probability", branch_probability)
    _require_probability("total_branch_overlap", total_branch_overlap)

    return math.sqrt(branch_probability * (1.0 - branch_probability)) * total_branch_overlap


def two_branch_decohered(
    branch_probability: float,
    total_branch_overlap: float,
    coherence_threshold: float = 0.01,
) -> bool:
    """Return whether the two-branch off-diagonal term is below a threshold."""

    _require_nonnegative("coherence_threshold", coherence_threshold)
    return (
        two_branch_coherence_magnitude(branch_probability, total_branch_overlap)
        <= coherence_threshold
    )


def effective_branch_dominates(
    branch_probability: float,
    total_branch_overlap: float,
    probability_threshold: float = 0.9,
    coherence_threshold: float = 0.01,
) -> bool:
    """Return whether one effective branch is both probable and decohered."""

    _require_probability("probability_threshold", probability_threshold)
    dominant_probability = max(branch_probability, 1.0 - branch_probability)
    return dominant_probability >= probability_threshold and two_branch_decohered(
        branch_probability,
        total_branch_overlap,
        coherence_threshold,
    )


def _require_finite(name: str, value: float) -> None:
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _require_nonnegative(name: str, value: float) -> None:
    _require_finite(name, value)
    if value < 0.0:
        raise ValueError(f"{name} must be nonnegative")


def _require_probability(name: str, value: float) -> None:
    _require_nonnegative(name, value)
    if value > 1.0:
        raise ValueError(f"{name} must be at most 1")


def _require_positive(name: str, value: float) -> None:
    _require_finite(name, value)
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def _require_not_superluminal(
    name: str,
    velocity_m_per_s: float,
    speed_of_light_m_per_s: float,
) -> None:
    _require_finite(name, velocity_m_per_s)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)
    if abs(velocity_m_per_s) > speed_of_light_m_per_s:
        raise ValueError(f"{name} must not exceed speed_of_light_m_per_s")


def _require_schwarzschild_timelike_circular_geodesic_radius(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float,
    speed_of_light_m_per_s: float,
) -> None:
    _require_nonnegative("mass_kg", mass_kg)
    _require_positive("radius_m", radius_m)
    _require_positive("gravitational_constant_m3_per_kg_s2", gravitational_constant_m3_per_kg_s2)
    _require_positive("speed_of_light_m_per_s", speed_of_light_m_per_s)

    minimum_radius_m = (
        3.0
        * gravitational_constant_m3_per_kg_s2
        * mass_kg
        / speed_of_light_m_per_s**2
    )
    if radius_m <= minimum_radius_m:
        raise ValueError("radius_m must be greater than 3 G M / c^2")


def _require_schwarzschild_outside_radius(
    mass_kg: float,
    radius_m: float,
    gravitational_constant_m3_per_kg_s2: float,
    speed_of_light_m_per_s: float,
) -> float:
    _require_positive("radius_m", radius_m)
    schwarzschild_radius_m = schwarzschild_radius(
        mass_kg,
        gravitational_constant_m3_per_kg_s2,
        speed_of_light_m_per_s,
    )

    if radius_m <= schwarzschild_radius_m:
        raise ValueError("radius_m must be greater than the Schwarzschild radius")

    return schwarzschild_radius_m
