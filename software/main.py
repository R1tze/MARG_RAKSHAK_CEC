from sensors.capture_controller import CaptureController
from sensors.scd41 import SCD41Simulator
from sensors.airflow import AirflowSimulator
from sensors.airflow_processing import pressure_to_airflow
from sensors.sample_gate import is_valid_sample
from sensors.bme688_array import BME688Array
from sensors.voc_processing import extract_voc_features
from sensors.sht40 import SHT40Simulator


def main():
    co2_sensor = SCD41Simulator()
    airflow_sensor = AirflowSimulator()
    voc_sensor = BME688Array()
    sht40_sensor = SHT40Simulator()
    capture = CaptureController()

    print("MARG RAKSHAK")
    print("============")
    print("Sensor monitoring started")
    print()

    for _ in range(10):

        # CO2
        co2 = co2_sensor.read_co2()

        # Airflow
        pressure = airflow_sensor.read_pressure()
        airflow = pressure_to_airflow(pressure)

        # Breath validity
        valid_sample = is_valid_sample(co2, airflow)

        # Two BME688 sensors
        voc_array = voc_sensor.read()

        voc_features_1 = extract_voc_features(
            voc_array["sensor_1"]
        )

        voc_features_2 = extract_voc_features(
            voc_array["sensor_2"]
        )

        # SHT40
        sht40_data = sht40_sensor.read()

        print(f"CO2: {co2} ppm")
        print(f"Airflow pressure: {pressure:.3f} kPa")
        print(f"Estimated airflow: {airflow:.2f}")

        print()
        print("BME688 Sensor 1:")
        print(f"Temperature: {voc_features_1['temperature']} °C")
        print(f"Humidity: {voc_features_1['humidity']} %")
        print(f"Pressure: {voc_features_1['pressure']} hPa")
        print(f"Gas resistance: {voc_features_1['gas_resistance']} Ω")

        print()
        print("BME688 Sensor 2:")
        print(f"Temperature: {voc_features_2['temperature']} °C")
        print(f"Humidity: {voc_features_2['humidity']} %")
        print(f"Pressure: {voc_features_2['pressure']} hPa")
        print(f"Gas resistance: {voc_features_2['gas_resistance']} Ω")

        print()
        print("SHT40:")
        print(f"Temperature: {sht40_data['temperature']} °C")
        print(f"Humidity: {sht40_data['humidity']} %")

        print()

        # Breath + condensate capture
        if valid_sample:
            print("Status: VALID BREATH SAMPLE")

        capture.start_capture()

        capture.add_condensate(20)
        capture.add_condensate(30)

        if capture.is_ready():
                print("Condensate: READY FOR DPV ANALYSIS")
                capture.stop_capture()
        else:
                print("Condensate: COLLECTING")

    else:
        print("Status: WAITING FOR VALID BREATH")

        print("-" * 40)


if __name__ == "__main__":
    main()