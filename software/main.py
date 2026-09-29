from sensors.scd41 import SCD41Simulator
from sensors.airflow import AirflowSimulator
from sensors.airflow_processing import pressure_to_airflow
from sensors.sample_gate import is_valid_sample


def main():
    co2_sensor = SCD41Simulator()
    airflow_sensor = AirflowSimulator()

    print("MARG RAKSHAK")
    print("============")
    print("Breath sample monitoring started")
    print()

    for _ in range(10):

        # Read CO2
        co2 = co2_sensor.read_co2()

        # Read differential pressure
        pressure = airflow_sensor.read_pressure()

        # Convert pressure to estimated airflow
        airflow = pressure_to_airflow(pressure)

        # Check complete breath sample
        valid = is_valid_sample(co2, airflow)

        print(f"CO2: {co2} ppm")
        print(f"Pressure: {pressure:.3f} kPa")
        print(f"Estimated airflow: {airflow:.2f}")

        if valid:
            print("Status: VALID BREATH SAMPLE")
        else:
            print("Status: WAITING FOR VALID BREATH")

        print("-" * 40)


if __name__ == "__main__":
    main()