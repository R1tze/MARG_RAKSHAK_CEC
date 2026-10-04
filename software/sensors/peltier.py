class PeltierSimulator:
    """
    Simulated Peltier controller for PC development.
    """

    def __init__(self):
        self.power = 0
        self.enabled = False

    def start(self, power=70):
        self.power = power
        self.enabled = True
        print(f"Peltier: ON ({power}%)")

    def stop(self):
        self.power = 0
        self.enabled = False
        print("Peltier: OFF")

    def status(self):
        return {
            "enabled": self.enabled,
            "power": self.power
        }


class PeltierReal:
    """
    Real Peltier controller for Raspberry Pi.

    Uses GPIO PWM through gpiozero.
    """

    def __init__(self, gpio_pin=18):
        from gpiozero import PWMOutputDevice

        self.device = PWMOutputDevice(
            gpio_pin,
            frequency=1000
        )

        self.power = 0
        self.enabled = False

    def start(self, power=70):
        power = max(0, min(100, power))

        self.device.value = power / 100.0

        self.power = power
        self.enabled = power > 0

        print(f"Peltier: ON ({power}%)")

    def stop(self):
        self.device.value = 0

        self.power = 0
        self.enabled = False

        print("Peltier: OFF")

    def status(self):
        return {
            "enabled": self.enabled,
            "power": self.power
        }