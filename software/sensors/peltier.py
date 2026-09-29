class PeltierController:
    """
    Simulated Peltier cooling controller.

    The real Raspberry Pi version will control
    the Peltier through a MOSFET using PWM.
    """

    def __init__(self):
        self.power = 0
        self.enabled = False

    def start(self, power=70):
        self.power = power
        self.enabled = True

    def stop(self):
        self.power = 0
        self.enabled = False

    def status(self):
        return {
            "enabled": self.enabled,
            "power": self.power
        }


if __name__ == "__main__":
    peltier = PeltierController()

    print("MARG RAKSHAK - PELTIER TEST")
    print("---------------------------")

    print("Starting Peltier...")
    peltier.start(70)

    print(peltier.status())

    print("Stopping Peltier...")
    peltier.stop()

    print(peltier.status())