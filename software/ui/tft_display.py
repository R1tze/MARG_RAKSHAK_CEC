class TFTDisplay:
    """
    Software interface for the MARG RAKSHAK TFT display.

    Hardware-specific drawing will be connected later.
    """

    def show_startup(self):
        print("MARG RAKSHAK")
        print("System Starting...")

    def show_breath_status(self, status):
        print(f"BREATH: {status}")

    def show_sample_status(self, status):
        print(f"SAMPLE: {status}")

    def show_result(self, result):
        print()
        print("RESULT")
        print("------")
        print(result)


if __name__ == "__main__":
    display = TFTDisplay()

    display.show_startup()
    display.show_breath_status("VALID")
    display.show_sample_status("READY")
    display.show_result("PRESUMPTIVE POSITIVE")