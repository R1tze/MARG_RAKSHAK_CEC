from sensors.peltier import PeltierController
from sensors.condensate import CondensateCollector


class CaptureController:
    """
    Controls the simulated Peltier condenser
    and condensate collection process.
    """

    def __init__(self, target_volume=50, peltier_power=70):
        self.peltier = PeltierController()
        self.collector = CondensateCollector(
            target_volume=target_volume
        )
        self.peltier_power = peltier_power

    def start_capture(self):
        self.peltier.start(self.peltier_power)

    def add_condensate(self, amount):
        if self.peltier.enabled:
            self.collector.collect(amount)

    def is_ready(self):
        return self.collector.is_ready()

    def stop_capture(self):
        self.peltier.stop()

    def status(self):
        return {
            "peltier": self.peltier.status(),
            "condensate": self.collector.status()
        }


if __name__ == "__main__":
    capture = CaptureController()

    print("MARG RAKSHAK - CAPTURE CONTROLLER")
    print("---------------------------------")

    capture.start_capture()
    print("Capture started")

    capture.add_condensate(20)
    print(capture.status())

    capture.add_condensate(30)
    print(capture.status())

    if capture.is_ready():
        print("Condensate ready for electrochemical analysis")

    capture.stop_capture()
    print("Capture stopped")