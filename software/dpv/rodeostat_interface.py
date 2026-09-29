class RodeostatSimulator:
    """
    Simulated Rodeostat potentiostat for PC development.

    Later this can be replaced with the real Rodeostat
    hardware/library interface.
    """

    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Rodeostat: CONNECTED")

    def disconnect(self):
        self.connected = False
        print("Rodeostat: DISCONNECTED")

    def run_dpv(self, potential_start=0.0, potential_end=0.5, points=101):
        if not self.connected:
            raise RuntimeError("Rodeostat is not connected")

        import numpy as np

        potential = np.linspace(
            potential_start,
            potential_end,
            points
        )

        # Simulated DPV response
        current = (
            np.exp(
                -((potential - 0.25) / 0.03) ** 2
            ) * 0.15
        )

        return potential, current


if __name__ == "__main__":

    print("MARG RAKSHAK - RODEOSTAT TEST")
    print("-----------------------------")

    rodeostat = RodeostatSimulator()

    rodeostat.connect()

    potential, current = rodeostat.run_dpv()

    print(f"Potential points: {len(potential)}")
    print(f"Current points: {len(current)}")

    print(f"First potential: {potential[0]:.3f} V")
    print(f"Last potential: {potential[-1]:.3f} V")

    rodeostat.disconnect()