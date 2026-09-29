import matplotlib.pyplot as plt


def plot_dpv(result):
    potential = result["potential"]
    raw_current = result["raw_current"]
    smoothed_current = result["smoothed_current"]

    peak_potential = result["peak_potential"]
    peak_current = result["peak_current"]

    plt.figure(figsize=(9, 5))

    plt.plot(
        potential,
        raw_current,
        label="Raw DPV"
    )

    plt.plot(
        potential,
        smoothed_current,
        label="Smoothed DPV"
    )

    plt.scatter(
        peak_potential,
        peak_current,
        label="Detected Peak"
    )

    plt.xlabel("Potential (V)")
    plt.ylabel("Current")
    plt.title("MARG RAKSHAK - DPV Signal")

    plt.legend()
    plt.grid(True)

    plt.show()