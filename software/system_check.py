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

    print("MARG RAKSHAK - SYSTEM CHECK")
    print("============================")

    checks = []

    try:
        SCD41Simulator()
        checks.append(("SCD41 CO2", "OK"))
    except Exception:
        checks.append(("SCD41 CO2", "FAILED"))

    try:
        AirflowSimulator()
        checks.append(("Airflow", "OK"))
    except Exception:
        checks.append(("Airflow", "FAILED"))

    try:
        BME688Array()
        checks.append(("BME688 Array", "OK"))
    except Exception:
        checks.append(("BME688 Array", "FAILED"))

    try:
        SHT40Simulator()
        checks.append(("SHT40", "OK"))
    except Exception:
        checks.append(("SHT40", "FAILED"))

    try:
        CaptureController()
        checks.append(("Peltier/Capture", "OK"))
    except Exception:
        checks.append(("Peltier/Capture", "FAILED"))

    try:
        RodeostatSimulator()
        checks.append(("Rodeostat", "OK"))
    except Exception:
        checks.append(("Rodeostat", "FAILED"))

    try:
        process_dpv
        classify_signal
        checks.append(("DPV Processing", "OK"))
    except Exception:
        checks.append(("DPV Processing", "FAILED"))

    try:
        fuse_results
        checks.append(("Fusion", "OK"))
    except Exception:
        checks.append(("Fusion", "FAILED"))

    try:
        DatabaseLogger()
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