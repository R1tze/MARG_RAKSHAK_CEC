def is_valid_breath(co2, threshold=1000):
    """
    Check whether CO2 indicates a valid breath sample.

    Demo threshold only.
    Actual threshold should be calibrated experimentally.
    """

    if co2 >= threshold:
        return True

    return False


if __name__ == "__main__":
    test_values = [450, 700, 1000, 2500, 4000]

    print("MARG RAKSHAK - BREATH VALIDITY TEST")
    print("-----------------------------------")

    for co2 in test_values:
        valid = is_valid_breath(co2)

        if valid:
            print(f"CO2: {co2} ppm -> VALID BREATH")
        else:
            print(f"CO2: {co2} ppm -> INVALID BREATH")