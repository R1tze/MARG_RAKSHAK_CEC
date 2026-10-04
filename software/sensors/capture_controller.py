from sensors.peltier import PeltierSimulator, PeltierReal
from sensors.condensate import CondensateCollector


class CaptureController:

    def __init__(
        self,
        target_volume=50,
        peltier_power=70,
        mode="simulator"
    ):

        if mode == "real":
            self.peltier = PeltierReal()
        else:
            self.peltier = PeltierSimulator()

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