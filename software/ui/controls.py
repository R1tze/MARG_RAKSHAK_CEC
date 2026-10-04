class ControlsSimulator:
    """
    Simulated RGB LED, buzzer, and buttons for PC development.
    """

    def set_led(self, color):
        print(f"LED: {color}")

    def beep(self, duration=0.2):
        print(f"BUZZER: {duration:.1f}s")

    def button_pressed(self, button):
        return False


class ControlsReal:
    """
    Raspberry Pi GPIO controls for RGB LED, buzzer, and buttons.

    GPIO pin numbers must be matched to the final PCB wiring.
    """

    def __init__(
        self,
        led_red=17,
        led_green=27,
        led_blue=22,
        buzzer=23,
        button=24
    ):
        from gpiozero import LED, Buzzer, Button

        self.led_red = LED(led_red)
        self.led_green = LED(led_green)
        self.led_blue = LED(led_blue)

        self.buzzer = Buzzer(buzzer)
        self.button = Button(button)

    def set_led(self, color):
        self.led_red.off()
        self.led_green.off()
        self.led_blue.off()

        if color == "red":
            self.led_red.on()
        elif color == "green":
            self.led_green.on()
        elif color == "blue":
            self.led_blue.on()

    def beep(self, duration=0.2):
        self.buzzer.on()
        self.buzzer.off()

    def button_pressed(self, button="main"):
        return self.button.is_pressed