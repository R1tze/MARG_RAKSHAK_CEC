class TFTDisplay:

    def __init__(self):
        pass

    def show_startup(self):
        print("MARG RAKSHAK")
        print("========================================")
        print("HARDWARE PLATFORM : Raspberry Pi Zero 2 W")
        print("HARDWARE MODE     : simulator")
        print("========================================")

    def show_breath_status(self, status):
        print(f"BREATH STATUS : {status}")

    def show_sample_status(self, status):
        print(f"SAMPLE STATUS : {status}")

    def show_result(self, result):
        print()
        print("RESULT")
        print("----------------------------------------")
        print(result)
        print("========================================")