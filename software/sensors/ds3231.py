from datetime import datetime


class DS3231Simulator:
    """
    Simulated DS3231 RTC for PC development.
    """

    def read_datetime(self):
        return datetime.now()

    def read_timestamp(self):
        return self.read_datetime().isoformat(
            timespec="seconds"
        )


class DS3231Real:
    """
    Real DS3231 RTC using I2C on Raspberry Pi.

    Uses the adafruit_ds3231 library.
    """

    def __init__(self):
        import board
        import busio
        import adafruit_ds3231

        i2c = busio.I2C(board.SCL, board.SDA)

        self.rtc = adafruit_ds3231.DS3231(i2c)

    def read_datetime(self):
        return self.rtc.datetime

    def read_timestamp(self):
        return self.read_datetime().isoformat(
            timespec="seconds"
        )


if __name__ == "__main__":

    rtc = DS3231Simulator()

    print("MARG RAKSHAK - DS3231 TEST")
    print("---------------------------")
    print("Datetime:", rtc.read_datetime())
    print("Timestamp:", rtc.read_timestamp())