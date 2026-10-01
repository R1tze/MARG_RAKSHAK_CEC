from sensors.capture_controller import CaptureController
from sensors.scd41 import SCD41Simulator
from sensors.airflow import AirflowSimulator
from sensors.airflow_processing import pressure_to_airflow
from sensors.sample_gate import is_valid_sample
from sensors.bme688_array import BME688Array
from sensors.voc_processing import (
    extract_voc_features,
    calculate_voc_signal
)
from sensors.sht40 import SHT40Simulator

from db.database import DatabaseLogger

from ui.display import show_result
from ui.tft_display import TFTDisplay

from config_loader import load_config

import numpy as np

from dpv.processing import process_dpv
from dpv.decision import classify_signal
from dpv.rodeostat_interface import RodeostatSimulator

from fusion.fusion import fuse_results


def main():

    # Load configuration
    config = load_config()

    # Sensors
    co2_sensor = SCD41Simulator()
    airflow_sensor = AirflowSimulator()
    voc_sensor = BME688Array()
    sht40_sensor = SHT40Simulator()

    # Capture system using configuration
    capture = CaptureController(
        target_volume=config["condensate"]["target_volume_uL"],
        peltier_power=config["peltier"]["default_power_percent"]
    )

    # Rodeostat
    rodeostat = RodeostatSimulator()
    rodeostat.connect()

    # Database
    database = DatabaseLogger()

    # Display
    display = TFTDisplay()
    display.show_startup()

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
        valid_sample = is_valid_sample(
            co2,
            airflow,
            co2_threshold=config["breath_validation"]["co2_threshold_ppm"],
            airflow_threshold=config["breath_validation"]["airflow_threshold"]
        )

        # BME688 array
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

        # Breath + condensate + DPV
        if valid_sample:

            print("Status: VALID BREATH SAMPLE")
            display.show_breath_status("VALID")

            capture.start_capture()

            # Simulated condensate collection
            capture.add_condensate(
                config["condensate"]["target_volume_uL"]
            )

            if capture.is_ready():

                print("Condensate: READY FOR DPV ANALYSIS")
                display.show_sample_status("READY")

                # Rodeostat DPV sweep
                potential, current = rodeostat.run_dpv(
                    potential_start=config["rodeostat"]["potential_start"],
                    potential_end=config["rodeostat"]["potential_end"],
                    points=config["rodeostat"]["points"]
                )

                # Process DPV
                dpv_result = process_dpv(
                    potential,
                    current
                )

                # Detect strongest peak
                if len(dpv_result["peak_current"]) > 0:

                    peak_index = np.argmax(
                        dpv_result["peak_current"]
                    )

                    peak_current = dpv_result["peak_current"][
                        peak_index
                    ]

                    peak_potential = dpv_result["peak_potential"][
                        peak_index
                    ]

                    # DPV decision
                    decision = classify_signal(
                        peak_current,
                        lod=config["dpv"]["lod"],
                        loq=config["dpv"]["loq"]
                    )

                    # Demo VOC support signal
                    # Calculate VOC support from both BME688 sensors
                    voc_signal = calculate_voc_signal(
    voc_features_1,
    voc_features_2,
    gas_resistance_threshold=config["voc"]["gas_resistance_threshold_ohms"]
)

                    # Fuse DPV + VOC
                    final_result = fuse_results(
                        decision,
                        voc_signal
                    )

                    # Display result
                    display.show_result(final_result)

                    show_result(
                        breath_status="VALID",
                        sample_status="READY",
                        peak_potential=peak_potential,
                        peak_current=peak_current,
                        dpv_decision=decision,
                        final_result=final_result
                    )

                    print(
                        f"DPV peak potential: "
                        f"{peak_potential:.3f} V"
                    )

                    print(
                        f"DPV peak current: "
                        f"{peak_current:.4f}"
                    )

                    print(
                        f"DPV decision: {decision}"
                    )

                    print(
                        f"Final result: {final_result}"
                    )

                    # Save result
                    database.log_result(
                        co2=co2,
                        airflow=airflow,
                        peak_potential=peak_potential,
                        peak_current=peak_current,
                        dpv_decision=decision,
                        final_result=final_result
                    )

                    print("Result saved to database.")

                else:

                    print("DPV: NO PEAK DETECTED")
                    print("DPV decision: INCONCLUSIVE")

                capture.stop_capture()

            else:

                print("Condensate: COLLECTING")

        else:

            print("Status: WAITING FOR VALID BREATH")

        print("-" * 40)

    database.close()


if __name__ == "__main__":
    main()