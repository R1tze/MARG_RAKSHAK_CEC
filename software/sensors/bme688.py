import random


class BME688Simulator:
    """
    Simulated BME688 VOC sensor for PC development.

    The real Raspberry Pi version will later read
    gas resistance, temperature, humidity and pressure.
    """

    def read(self):
        return {
            "temperature": round(random.uniform(24.0, 32.0), 2),
            "humidity": round(random.uniform(40.0, 70.0), 2),
            "pressure": round(random.uniform(990.0, 1020.0), 2),
            "gas_resistance": round(random.uniform(5000, 50000), 2)
        }


if __name__ == "__main__":
    sensor = BME688Simulator()

    print("MARG RAKSHAK - BME688 TEST")
    print("--------------------------")

    for _ in range(5):
        data = sensor.read()

        print(f"Temperature: {data['temperature']} °C")
        print(f"Humidity: {data['humidity']} %")
        print(f"Pressure: {data['pressure']} hPa")
        print(f"Gas resistance: {data['gas_resistance']} Ω")
        print("-" * 30)