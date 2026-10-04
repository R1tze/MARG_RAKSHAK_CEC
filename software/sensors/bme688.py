import random


class BME688Simulator:
    """
    Simulated BME688 sensor for PC development.
    """

    def read(self):
        return {
            "temperature": round(random.uniform(24.0, 32.0), 2),
            "humidity": round(random.uniform(40.0, 70.0), 2),
            "pressure": round(random.uniform(990.0, 1020.0), 2),
            "gas_resistance": round(random.uniform(5000, 50000), 2)
        }


class BME688Real:
    """
    Real BME688 sensor for Raspberry Pi.

    Uses the Bosch BME68x Python library.
    """

    def __init__(self, address=0x76):
        import board
        import busio
        from bme680 import BME680

        self.sensor = BME680(
            i2c_addr=address,
            i2c_device=busio.I2C(board.SCL, board.SDA)
        )

    def read(self):
        if self.sensor.get_sensor_data():
            data = self.sensor.data

            return {
                "temperature": data.temperature,
                "humidity": data.humidity,
                "pressure": data.pressure,
                "gas_resistance": data.gas_resistance
            }

        return None