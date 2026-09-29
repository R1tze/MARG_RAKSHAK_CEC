from sensors.bme688 import BME688Simulator


class BME688Array:
    """
    Simulated two-sensor BME688 VOC array.
    """

    def __init__(self):
        self.sensor_1 = BME688Simulator()
        self.sensor_2 = BME688Simulator()

    def read(self):
        return {
            "sensor_1": self.sensor_1.read(),
            "sensor_2": self.sensor_2.read()
        }


if __name__ == "__main__":
    sensors = BME688Array()

    print("MARG RAKSHAK - BME688 ARRAY TEST")
    print("--------------------------------")

    data = sensors.read()

    print("BME688 Sensor 1:")
    print(data["sensor_1"])

    print()
    print("BME688 Sensor 2:")
    print(data["sensor_2"])