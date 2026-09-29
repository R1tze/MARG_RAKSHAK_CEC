def pressure_to_airflow(pressure):
    """
    Convert differential pressure to estimated airflow.

    Demo relationship only.
    The real system must be calibrated experimentally.
    """

    if pressure <= 0:
        return 0.0

    airflow = pressure * 2.0

    return airflow


if __name__ == "__main__":
    test_pressures = [0.0, 0.5, 1.0, 1.5, 2.0]

    print("MARG RAKSHAK - AIRFLOW PROCESSING TEST")
    print("--------------------------------------")

    for pressure in test_pressures:
        airflow = pressure_to_airflow(pressure)

        print(
            f"Pressure: {pressure:.2f} kPa "
            f"-> Estimated airflow: {airflow:.2f}"
        )