def extract_voc_features(sensor_data):
    """
    Extract useful features from BME688 data.

    These are software features for development.
    They are not drug-specific signatures.
    """

    return {
        "temperature": sensor_data["temperature"],
        "humidity": sensor_data["humidity"],
        "pressure": sensor_data["pressure"],
        "gas_resistance": sensor_data["gas_resistance"],
    }


if __name__ == "__main__":
    test_data = {
        "temperature": 31.28,
        "humidity": 48.44,
        "pressure": 991.37,
        "gas_resistance": 47137.37,
    }

    features = extract_voc_features(test_data)

    print("MARG RAKSHAK - VOC FEATURE TEST")
    print("--------------------------------")

    for name, value in features.items():
        print(f"{name}: {value}")