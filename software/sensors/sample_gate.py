def is_valid_sample(co2, airflow, co2_threshold=1000, airflow_threshold=0.5):
    """
    Check whether both CO2 and airflow indicate a valid breath sample.

    Thresholds are demo values and must be experimentally calibrated
    for the real prototype.
    """

    co2_valid = co2 >= co2_threshold
    airflow_valid = airflow >= airflow_threshold

    return co2_valid and airflow_valid


if __name__ == "__main__":
    test_samples = [
        (450, 0.05),
        (3000, 0.05),
        (450, 2.0),
        (3000, 2.0),
    ]

    print("MARG RAKSHAK - SAMPLE VALIDITY TEST")
    print("-----------------------------------")

    for co2, airflow in test_samples:
        valid = is_valid_sample(co2, airflow)

        if valid:
            status = "VALID SAMPLE"
        else:
            status = "INVALID SAMPLE"

        print(
            f"CO2: {co2} ppm | "
            f"Airflow: {airflow:.2f} | "
            f"{status}"
        )