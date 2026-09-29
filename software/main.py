from sensors.scd41 import SCD41Simulator
from sensors.breath_gate import is_valid_breath


def main():
    sensor = SCD41Simulator()

    print("MARG RAKSHAK")
    print("============")
    print("Breath validity monitoring started")
    print()

    for _ in range(10):
        co2 = sensor.read_co2()
        valid = is_valid_breath(co2)

        print(f"CO2: {co2} ppm")

        if valid:
            print("Status: VALID BREATH")
        else:
            print("Status: WAITING FOR BREATH")

        print("-" * 30)


if __name__ == "__main__":
    main()