from sensors.capture_controller import CaptureController
from sensors.scd41 import SCD41Simulator, SCD41Real
from sensors.airflow import AirflowSimulator, AirflowReal
from sensors.airflow_processing import pressure_to_airflow
from sensors.sample_gate import is_valid_sample
from sensors.bme688_array import BME688Array
from sensors.voc_processing import (
    extract_voc_features,
    calculate_voc_signal,
    calculate_voc_response
)
from sensors.sht40 import SHT40Simulator, SHT40Real

from db.database import DatabaseLogger

from ui.display import show_result
from ui.tft_display import TFTDisplay

from config_loader import load_config

import numpy as np

from dpv.processing import process_dpv
from dpv.decision import classify_signal
from dpv.rodeostat_interface import RodeostatSimulator, RodeostatReal

from fusion.fusion import fuse_results
from sensors.ds18b20 import DS18B20Simulator, DS18B20Real
from sensors.ds3231 import DS3231Simulator, DS3231Real
from sensors.max17048 import MAX17048Simulator, MAX17048Real
from ui.controls import ControlsSimulator, ControlsReal


def main():

    # Load configuration
    config = load_config()

    hardware_platform = config["hardware"]["platform"]
    hardware_mode = config["hardware"]["mode"]
    print("### HARDWARE CONFIG LOADED ###")
    print("PLATFORM:", hardware_platform)
    print("MODE:", hardware_mode)

         # Sensors
    if hardware_mode == "real":
        co2_sensor = SCD41Real()
    else:
        co2_sensor = SCD41Simulator()

    if hardware_mode == "real":
        airflow_sensor = AirflowReal()
    else:
        airflow_sensor = AirflowSimulator()

    voc_sensor = BME688Array(mode=hardware_mode)
    if hardware_mode == "real":
        sht40_sensor = SHT40Real()
    else:
        sht40_sensor = SHT40Simulator()
            # DS18B20 temperature sensors
    if hardware_mode == "real":
        peltier_temp_sensor = DS18B20Real()
        heatsink_temp_sensor = DS18B20Real()
    else:
        peltier_temp_sensor = DS18B20Simulator(sensor_id=1)
        heatsink_temp_sensor = DS18B20Simulator(sensor_id=2)
            # DS3231 real-time clock
    if hardware_mode == "real":
        rtc = DS3231Real()
    else:
        rtc = DS3231Simulator()
            # MAX17048 battery fuel gauge
    if hardware_mode == "real":
        battery = MAX17048Real()
    else:
        battery = MAX17048Simulator()
            # RGB LED, buzzer, and buttons
    if hardware_mode == "real":
        controls = ControlsReal()
    else:
        controls = ControlsSimulator()

       # Capture system
    capture = CaptureController(
        target_volume=config["condensate"]["target_volume_uL"],
        peltier_power=config["peltier"]["default_power_percent"],
        mode=hardware_mode
    )

        # Rodeostat
    if hardware_mode == "real":
        rodeostat = RodeostatReal()
    else:
        rodeostat = RodeostatSimulator(
    scenario=config["rodeostat"]["simulator_scenario"]
)

    rodeostat.connect()

    # Database
    database = DatabaseLogger()

    # Display
    print("MARG RAKSHAK")
    print("========================================")
    print(f"HARDWARE PLATFORM : {hardware_platform}")
    print(f"HARDWARE MODE     : {hardware_mode}")
    print("========================================")
    print("Sensor monitoring started")
    print()

    display = TFTDisplay()
    display.show_startup()

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
        print("DEBUG valid_sample:", valid_sample)

        # BME688 array
        voc_array = voc_sensor.read()

        voc_features_1 = extract_voc_features(
            voc_array["sensor_1"]
        )

        voc_features_2 = extract_voc_features(
            voc_array["sensor_2"]
        )

        voc_response = calculate_voc_response(
            voc_features_1,
            voc_features_2
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
        print(f"VOC response difference: {voc_response:.2f} Ω")

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

                    peak_current = dpv_result["peak_current"][peak_index]
                    peak_potential = dpv_result["peak_potential"][peak_index]

                    # DPV decision
                    decision = classify_signal(
                        peak_current,
                        lod=config["dpv"]["lod"],
                        loq=config["dpv"]["loq"]
                    )

                    # VOC support signal
                    voc_signal = calculate_voc_signal(
                        voc_features_1,
                        voc_features_2,
                        gas_resistance_threshold=
                        config["voc"]["gas_resistance_threshold_ohms"]
                    )

                    # Fuse DPV + VOC
                    final_result = fuse_results(
                        decision,
                        voc_signal,
                        sample_valid=valid_sample
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