def extract_voc_features(sensor_data):
    """
    Extract useful VOC-related features from a BME688 reading.
    """

    return {
        "temperature": sensor_data["temperature"],
        "humidity": sensor_data["humidity"],
        "pressure": sensor_data["pressure"],
        "gas_resistance": sensor_data["gas_resistance"]
    }


def calculate_voc_response(sensor_1_features, sensor_2_features):
    """
    Calculate the difference between two BME688 gas-resistance readings.

    This is a development feature for sensor-fusion experiments.
    It is not a validated substance-identification method.
    """

    gas_1 = sensor_1_features["gas_resistance"]
    gas_2 = sensor_2_features["gas_resistance"]

    return abs(gas_1 - gas_2)


def calculate_voc_signal(
    sensor_1_features,
    sensor_2_features,
    gas_resistance_threshold=100000
):
    """
    Demo VOC support decision based on average gas resistance.

    This is a development/demo rule only.
    It is NOT a validated substance-identification method.
    """

    gas_1 = sensor_1_features["gas_resistance"]
    gas_2 = sensor_2_features["gas_resistance"]

    average_gas_resistance = (gas_1 + gas_2) / 2

    if average_gas_resistance < gas_resistance_threshold:
        return True

    return False