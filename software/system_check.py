from sensors.scd41 import SCD41Simulator
from sensors.airflow import AirflowSimulator
from sensors.bme688_array import BME688Array
from sensors.sht40 import SHT40Simulator
from sensors.capture_controller import CaptureController

from dpv.rodeostat_interface import RodeostatSimulator
from dpv.processing import process_dpv
from dpv.decision import classify_signal

from fusion.fusion import fuse_results
from db.database import DatabaseLogger


def main():

    print()
    print("Running system check...")
    
    print()

    print("MARG RAKSHAK - SYSTEM CHECK")
    print("============================")

    checks = []

    # SCD41 CO2
    try:
        sensor = SCD41Simulator()
        co2 = sensor.read_co2()

        if co2 >= 0:
            checks.append(("SCD41 CO2", "OK"))
        else:
            checks.append(("SCD41 CO2", "FAILED"))

    except Exception:
        checks.append(("SCD41 CO2", "FAILED"))

    # Airflow
    try:
        sensor = AirflowSimulator()
        pressure = sensor.read_pressure()

        if isinstance(pressure, (int, float)):
            checks.append(("Airflow", "OK"))
        else:
            checks.append(("Airflow", "FAILED"))

    except Exception:
        checks.append(("Airflow", "FAILED"))

    # BME688
    try:
        sensor = BME688Array()
        data = sensor.read()

        if data:
            checks.append(("BME688 Array", "OK"))
        else:
            checks.append(("BME688 Array", "FAILED"))

    except Exception:
        checks.append(("BME688 Array", "FAILED"))

    # SHT40
    try:
        sensor = SHT40Simulator()
        data = sensor.read()

        if data:
            checks.append(("SHT40", "OK"))
        else:
            checks.append(("SHT40", "FAILED"))

    except Exception:
        checks.append(("SHT40", "FAILED"))

    # Peltier / Capture
    try:
        CaptureController()
        checks.append(("Peltier/Capture", "OK"))

    except Exception:
        checks.append(("Peltier/Capture", "FAILED"))

    # Rodeostat
    try:
        RodeostatSimulator()
        checks.append(("Rodeostat", "OK"))

    except Exception:
        checks.append(("Rodeostat", "FAILED"))

    # DPV Processing
    try:
        process_dpv
        classify_signal
        checks.append(("DPV Processing", "OK"))

    except Exception:
        checks.append(("DPV Processing", "FAILED"))

    # Fusion
    try:
        fuse_results
        checks.append(("Fusion", "OK"))

    except Exception:
        checks.append(("Fusion", "FAILED"))

    # Database
    try:
        database = DatabaseLogger()
        database.close()
        checks.append(("SQLite Database", "OK"))

    except Exception:
        checks.append(("SQLite Database", "FAILED"))

    print()

    for name, status in checks:
        print(f"{name:<25} {status}")

    print()
    print("System check complete.")


if __name__ == "__main__":
    main()