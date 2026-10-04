class RodeostatSimulator:
    """
    Simulated Rodeostat potentiostat for PC development.
    """

    def __init__(self, scenario="positive"):
        self.connected = False
        self.scenario = scenario

    def connect(self):
        self.connected = True
        print("Rodeostat: CONNECTED")
        print(f"DPV simulation scenario: {self.scenario.upper()}")

    def disconnect(self):
        self.connected = False
        print("Rodeostat: DISCONNECTED")

    def run_dpv(
        self,
        potential_start=0.0,
        potential_end=0.5,
        points=101
    ):
        if not self.connected:
            raise RuntimeError("Rodeostat is not connected")

        import numpy as np

        potential = np.linspace(
            potential_start,
            potential_end,
            points
        )

        if self.scenario == "positive":
            peak_current = 0.15

        elif self.scenario == "inconclusive":
            peak_current = 0.07

        elif self.scenario == "negative":
            peak_current = 0.02

        else:
            raise ValueError(
                "Unknown DPV scenario. "
                "Use positive, inconclusive, or negative."
            )

        current = (
            np.exp(
                -((potential - 0.25) / 0.03) ** 2
            ) * peak_current
        )

        return potential, current


class RodeostatReal:
    """
    Real IO Rodeo Rodeostat interface.

    The exact API may depend on the installed
    Rodeostat Python library and hardware version.
    """

    def __init__(self):
        self.connected = False
        self.rodeostat = None

    def connect(self):
        try:
            from rodeostat import Rodeostat

            self.rodeostat = Rodeostat()
            self.connected = True

            print("Rodeostat: CONNECTED")

        except ImportError:
            raise RuntimeError(
                "Rodeostat library is not installed. "
                "Install the IO Rodeo Rodeostat library "
                "on the Raspberry Pi."
            )

    def disconnect(self):
        self.connected = False
        self.rodeostat = None

        print("Rodeostat: DISCONNECTED")

    def run_dpv(
        self,
        potential_start=0.0,
        potential_end=0.5,
        points=101
    ):
        if not self.connected:
            raise RuntimeError(
                "Rodeostat is not connected"
            )

        raise NotImplementedError(
            "Real Rodeostat DPV command must be "
            "mapped to the installed IO Rodeo "
            "Rodeostat library API."
        )