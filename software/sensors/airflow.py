import random
from sensors.airflow_processing import pressure_to_airflow


class AirflowSimulator:
    """
    Simulated MPXV7002DP differential-pressure sensor
    for PC development.
    """

class AirflowSimulator:
    """Simulated MPXV7002DP differential-pressure sensor
    for PC development.
    """

    def read_pressure(self):
        # Simulate a valid breath airflow for PC testing
        return random.uniform(0.8, 2.0)

        # Simulate no-breath condition
        return random.uniform(0.0, 0.05)


class AirflowReal:
    """
    Real MPXV7002DP differential-pressure sensor
    connected through an ADS1115 ADC.

    The ADS1115 provides the analog-to-digital conversion
    because the Raspberry Pi has no analog input.
    """

    def __init__(
        self,
        ads_channel=0,
        vcc=5.0,
        sensor_offset_v=2.5
    ):
        import board
        import busio
        import adafruit_ads1x15.ads1115 as ADS
        from adafruit_ads1x15.analog_in import AnalogIn

        self.vcc = vcc
        self.sensor_offset_v = sensor_offset_v

        i2c = busio.I2C(board.SCL, board.SDA)

        self.ads = ADS.ADS1115(i2c)

        channels = [
            ADS.P0,
            ADS.P1,
            ADS.P2,
            ADS.P3
        ]

        self.channel = AnalogIn(
            self.ads,
            channels[ads_channel]
        )

    def read_pressure(self):
        """
        Read sensor voltage and convert it to
        differential pressure in kPa.

        MPXV7002DP transfer-function conversion
        must be calibrated against the actual hardware.
        """

        voltage = self.channel.voltage

        # Approximate transfer-function calculation.
        # Final calibration must be performed on the prototype.
        pressure = (voltage - self.sensor_offset_v) / 0.04

        return pressure


if __name__ == "__main__":

    sensor = AirflowSimulator()

    print("MARG RAKSHAK - AIRFLOW SENSOR TEST")
    print("-----------------------------------")

    for _ in range(10):

        pressure = sensor.read_pressure()

        airflow = pressure_to_airflow(pressure)

        print(
            f"Pressure: {pressure:.3f} kPa "
            f"-> Estimated airflow: {airflow:.2f}"
        )