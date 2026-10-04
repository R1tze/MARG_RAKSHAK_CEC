from sensors.bme688 import BME688Simulator, BME688Real


class BME688Array:

    def __init__(self, mode="simulator"):
        if mode == "real":
            self.sensor_1 = BME688Real(address=0x76)
            self.sensor_2 = BME688Real(address=0x77)
        else:
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