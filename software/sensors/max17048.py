import random


class MAX17048Simulator:
    """
    Simulated MAX17048 battery fuel gauge.
    """

    def __init__(self):
        self.voltage = 7.4
        self.percentage = 85.0

    def read(self):
        # Small simulated variation
        self.voltage += random.uniform(-0.01, 0.01)
        self.percentage += random.uniform(-0.2, 0.2)

        self.voltage = max(6.0, min(8.4, self.voltage))
        self.percentage = max(0.0, min(100.0, self.percentage))

        return {
            "voltage": round(self.voltage, 2),
            "percentage": round(self.percentage, 1)
        }


class MAX17048Real:
    """
    Real MAX17048 battery fuel gauge using I2C.
    """

    def __init__(self):
        import board
        import busio
        from adafruit_max1704x import MAX17048

        i2c = busio.I2C(board.SCL, board.SDA)

        self.sensor = MAX17048(i2c)

    def read(self):
        return {
            "voltage": round(self.sensor.cell_voltage, 2),
            "percentage": round(self.sensor.cell_percent, 1)
        }


if __name__ == "__main__":

    battery = MAX17048Simulator()

    print("MARG RAKSHAK - MAX17048 TEST")
    print("-----------------------------")

    for _ in range(5):
        data = battery.read()

        print(f"Battery voltage: {data['voltage']} V")
        print(f"Battery level: {data['percentage']} %")
        print("-" * 30)