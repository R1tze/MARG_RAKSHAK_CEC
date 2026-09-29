import numpy as np
from scipy.signal import savgol_filter, find_peaks


def smooth_signal(current, window_length=11, polyorder=3):
    """
    Smooth a DPV current signal using Savitzky-Golay filtering.
    """
    current = np.asarray(current, dtype=float)

    if len(current) < window_length:
        return current

    return savgol_filter(
        current,
        window_length=window_length,
        polyorder=polyorder
    )


def find_dpv_peaks(potential, current, prominence=0.01):
    """
    Find peaks in a DPV signal.
    Returns peak locations and peak currents.
    """
    potential = np.asarray(potential, dtype=float)
    current = np.asarray(current, dtype=float)

    peaks, properties = find_peaks(
        current,
        prominence=prominence
    )

    return potential[peaks], current[peaks]


def process_dpv(potential, current):
    """
    Complete basic DPV processing pipeline.
    """
    smoothed = smooth_signal(current)

    peak_potential, peak_current = find_dpv_peaks(
        potential,
        smoothed
    )

    return {
        "potential": potential,
        "raw_current": current,
        "smoothed_current": smoothed,
        "peak_potential": peak_potential,
        "peak_current": peak_current
    }