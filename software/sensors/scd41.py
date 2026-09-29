import random


class SCD41Simulator:
    """
    Simulated SCD41 CO2 sensor for PC development.

    Later this can be replaced with the real SCD41
    Raspberry Pi implementation.
    """

    def __init__(self):
        self.base_co2 = 450

    def read_co2(self):
        """
        Return a simulated CO2 reading in ppm.
        """

        # Normal room-air variation
        if random.random() < 0.3:
         return random.randint(2500, 4500)

        return self.base_co2 + random.randint(-20, 20)

        return co2


if __name__ == "__main__":
    sensor = SCD41Simulator()

    print("MARG RAKSHAK - SCD41 SENSOR TEST")
    print("--------------------------------")

    for _ in range(10):
        co2 = sensor.read_co2()
        print(f"CO2: {co2} ppm")
        from breath_gate import is_valid_breath


if __name__ == "__main__":
    sensor = SCD41Simulator()

    print("MARG RAKSHAK - BREATH SENSOR TEST")
    print("--------------------------------")

    for _ in range(10):
        co2 = sensor.read_co2()
        valid = is_valid_breath(co2)

        if valid:
            print(f"CO2: {co2} ppm -> VALID BREATH")
        else:
            print(f"CO2: {co2} ppm -> WAITING FOR BREATH")