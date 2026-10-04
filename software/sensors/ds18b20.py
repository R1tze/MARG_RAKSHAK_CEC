import random


class DS18B20Simulator:
    """
    Simulated DS18B20 temperature sensor for PC development.
    """

    def __init__(self, sensor_id=1):
        self.sensor_id = sensor_id

    def read_temperature(self):
        return round(random.uniform(20.0, 35.0), 2)


class DS18B20Real:
    """
    Real DS18B20 temperature sensor using
    Raspberry Pi 1-Wire.
    """

    def __init__(self, sensor_id=None):
        from w1thermsensor import W1ThermSensor

        if sensor_id is None:
            self.sensor = W1ThermSensor()
        else:
            self.sensor = W1ThermSensor(sensor_id)

    def read_temperature(self):
        return round(
            self.sensor.get_temperature(),
            2
        )


if __name__ == "__main__":

    sensor = DS18B20Simulator()

    print("MARG RAKSHAK - DS18B20 TEST")
    print("----------------------------")

    for _ in range(5):
        temperature = sensor.read_temperature()
        print(f"Temperature: {temperature} °C")