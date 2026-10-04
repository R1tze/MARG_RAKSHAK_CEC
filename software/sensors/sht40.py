import random


class SHT40Simulator:
    """
    Simulated SHT40 temperature and humidity sensor.
    """

    def read(self):
        return {
            "temperature": round(random.uniform(24.0, 32.0), 2),
            "humidity": round(random.uniform(40.0, 70.0), 2)
        }


class SHT40Real:
    """
    Real SHT40 temperature and humidity sensor
    for Raspberry Pi using I2C.
    """

    def __init__(self):
        import board
        import busio
        import adafruit_sht4x

        i2c = busio.I2C(board.SCL, board.SDA)

        self.sensor = adafruit_sht4x.SHT4x(i2c)

    def read(self):
        temperature, humidity = self.sensor.measurements

        return {
            "temperature": temperature,
            "humidity": humidity
        }


if __name__ == "__main__":

    sensor = SHT40Simulator()

    print("MARG RAKSHAK - SHT40 TEST")
    print("-------------------------")

    for _ in range(5):

        data = sensor.read()

        print(f"Temperature: {data['temperature']} °C")
        print(f"Humidity: {data['humidity']} %")
        print("-" * 30)