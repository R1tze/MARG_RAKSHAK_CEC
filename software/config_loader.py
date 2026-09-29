import json


CONFIG_PATH = "config/device_config.json"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    config = load_config()

    print("MARG RAKSHAK - CONFIGURATION")
    print("============================")

    print(
        "CO2 threshold:",
        config["breath_validation"]["co2_threshold_ppm"]
    )

    print(
        "Airflow threshold:",
        config["breath_validation"]["airflow_threshold"]
    )

    print(
        "DPV LOD:",
        config["dpv"]["lod"]
    )

    print(
        "DPV LOQ:",
        config["dpv"]["loq"]
    )