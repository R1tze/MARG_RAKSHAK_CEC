class CondensateCollector:
    """
    Simulated breath-condensate collection system.

    The real prototype will use the Peltier condenser
    and physical collection path.
    """

    def __init__(self, target_volume=50):
        self.volume = 0.0
        self.target_volume = target_volume

    def collect(self, amount):
        if amount > 0:
            self.volume += amount

        if self.volume > self.target_volume:
            self.volume = self.target_volume

    def is_ready(self):
        return self.volume >= self.target_volume

    def status(self):
        return {
            "volume_uL": round(self.volume, 2),
            "target_uL": self.target_volume,
            "ready": self.is_ready()
        }


if __name__ == "__main__":
    collector = CondensateCollector(target_volume=50)

    print("MARG RAKSHAK - CONDENSATE TEST")
    print("--------------------------------")

    collector.collect(20)
    print(collector.status())

    collector.collect(15)
    print(collector.status())

    collector.collect(15)
    print(collector.status())