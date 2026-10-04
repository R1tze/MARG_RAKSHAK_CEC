import random


class SCD41Simulator:
    """
    Simulated SCD41 CO2 sensor for PC development.

    The simulator is used on Windows.
    The real SCD41 implementation will be added
    for Raspberry Pi hardware later.
    """

    def __init__(self):
        self.base_co2 = 450

    def read_co2(self):
        """
        Return a simulated CO2 reading in ppm.
        """

        # Simulate a breath sample sometimes.
        if random.random() < 0.3:
            return random.randint(2500, 4500)

        # Normal room-air variation.
        return self.base_co2 + random.randint(-20, 20)


if __name__ == "__main__":
    from breath_gate import is_valid_breath

    sensor = SCD41Simulator()

    print("MARG RAKSHAK - SCD41 SENSOR TEST")
    print("--------------------------------")

    for _ in range(10):
        co2 = sensor.read_co2()
        valid = is_valid_breath(co2)

        if valid:
            print(f"CO2: {co2} ppm -> VALID BREATH")
        else:
            print(f"CO2: {co2} ppm -> WAITING FOR BREATH")