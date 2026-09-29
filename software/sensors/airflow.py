import random

from sensors.airflow_processing import pressure_to_airflow


class AirflowSimulator:
    """
    Simulated MPXV7002DP + ADS1115 airflow sensor.
    """

    def read_pressure(self):
        # Simulate occasional breathing
        if random.random() < 0.3:
            return random.uniform(0.5, 2.0)

        # Normal condition
        return random.uniform(-0.05, 0.05)


if __name__ == "__main__":
    sensor = AirflowSimulator()

    print("MARG RAKSHAK - AIRFLOW TEST")
    print("---------------------------")

    for _ in range(10):
        pressure = sensor.read_pressure()
        airflow = pressure_to_airflow(pressure)

        print(f"Pressure: {pressure:.3f} kPa")
        print(f"Estimated airflow: {airflow:.2f}")
        print("-" * 30)