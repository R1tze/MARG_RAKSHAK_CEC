import random


class SCD41Simulator:
    """
    Simulated SCD41 CO2 sensor for PC development.
    """

    def __init__(self):
        self.base_co2 = 450

    def read_co2(self):
    # Simulate a valid breath sample for PC testing
        return random.randint(2500, 4500)


class SCD41Real:
    """
    Real SCD41 CO2 sensor for Raspberry Pi.

    Uses the Adafruit SCD4X library over I2C.
    """

    def __init__(self):
        import board
        import busio
        import adafruit_scd4x

        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_scd4x.SCD4X(self.i2c)

        self.sensor.start_periodic_measurement()

    def read_co2(self):
        """
        Read CO2 concentration from the real SCD41.
        """

        if self.sensor.data_ready:
            return self.sensor.CO2

        return None


if __name__ == "__main__":
    from breath_gate import is_valid_breath

    sensor = SCD41Simulator()

    print("MARG RAKSHAK - SCD41 SENSOR TEST")
    print("--------------------------------")

    for _ in range(10):
        co2 = sensor.read_co2()

        if co2 is None:
            print("CO2: WAITING FOR SENSOR DATA")
            continue

        valid = is_valid_breath(co2)

        if valid:
            print(f"CO2: {co2} ppm -> VALID BREATH")
        else:
            print(f"CO2: {co2} ppm -> WAITING FOR BREATH")