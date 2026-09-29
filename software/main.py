
import numpy as np

from dpv.decision import classify_signal
from dpv.plot import plot_dpv
from dpv.processing import process_dpv


# Demo DPV data
potential = np.linspace(-1.0, 1.0, 201)

current = (
    0.02 * potential
    + 0.15 * np.exp(-((potential - 0.25) ** 2) / 0.01)
)

# Process the DPV signal
result = process_dpv(potential, current)

print("MARG RAKSHAK - DPV TEST")
print("-----------------------")
print("Number of data points:", len(result["potential"]))

print("Detected peak potentials:")
print(result["peak_potential"])

print("Detected peak currents:")
print(result["peak_current"])
plot_dpv(result)
if len(result["peak_current"]) > 0:
    peak = result["peak_current"][0]

    decision = classify_signal(peak)

    print("Decision:", decision)
else:
    print("Decision: INCONCLUSIVE")
    print("\nDecision Tests")
print("-------------")

test_values = [0.02, 0.07, 0.15]

for peak in test_values:
    decision = classify_signal(peak)
    print(f"Peak current: {peak:.3f} -> {decision}")