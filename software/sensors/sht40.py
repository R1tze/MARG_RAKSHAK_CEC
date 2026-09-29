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


if __name__ == "__main__":
    sensor = SHT40Simulator()

    print("MARG RAKSHAK - SHT40 TEST")
    print("-------------------------")

    for _ in range(5):
        data = sensor.read()

        print(f"Temperature: {data['temperature']} °C")
        print(f"Humidity: {data['humidity']} %")
        print("-" * 30)