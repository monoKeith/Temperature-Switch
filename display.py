import gc
from machine import Pin, I2C
from lib.oled import Write, SSD1306_I2C
from lib.oled import ubuntu_mono_15, ubuntu_mono_20

SDA_PIN, SCL_PIN = 26, 27
ONBOARD_LED = 25
GREEN_PIN, YELLOW_PIN, RED_PIN = 20, 19, 18

class Display():

    def __init__(self, state):
        # Vars
        self.need_update = False
        self.actual_temp = 0
        self.actual_temp_txt = ""
        self.sensor_init = False
        self.target_temp = 0
        self.target_temp_txt = ""
        self.uptime = 0
        self.uptime_txt = ""
        self.state = state
        # LEDs
        self.green = Pin(GREEN_PIN, Pin.OUT)
        self.yellow = Pin(YELLOW_PIN, Pin.OUT)
        self.red = Pin(RED_PIN, Pin.OUT)
        self.onboard_led = Pin(ONBOARD_LED, Pin.OUT)
        # Settings
        self.i2c = I2C(1, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.lg_font = Write(self.oled, ubuntu_mono_20)
        self.md_font = Write(self.oled, ubuntu_mono_15)
        # Init
        self.oled.fill(0)
        self.lg_font.text("TARGET:", 0, 0)
        self.lg_font.text("ACTUAL:", 0, 21)

    def run(self):
        self.onboard_led.on()
        self.yellow.on()
        self.update()
        self.onboard_led.off()
        self.yellow.off()

    def update(self):
        self.update_actual_temp()
        self.update_target_temp()
        self.update_uptime()
        self.update_socket()
        # Update display if needed
        if not self.need_update:
            return
        # Draw
        self.oled.show()
        # Finish
        self.need_update = False
        gc.collect()

    def update_actual_temp(self):
        temp = self.state.get_actual_temp()
        sensor_init = self.state.get_sensor_init()
        if sensor_init == self.sensor_init and temp == self.actual_temp:
            return
        self.need_update = True
        self.actual_temp = temp
        self.sensor_init = sensor_init
        self.actual_temp_txt = "{actual:2.1f}C".format(actual=temp) if sensor_init else "ERROR"
        self.lg_font.text(self.actual_temp_txt, 72, 21)

    def update_target_temp(self):
        temp = self.state.get_target_temp()
        if self.target_temp == temp:
            return
        self.need_update = True
        self.target_temp = temp
        self.target_temp_txt = "{target:2.1f}C".format(target=temp)
        self.lg_font.text(self.target_temp_txt, 72, 0)

    def update_uptime(self):
        uptime = self.state.get_uptime()
        if self.uptime == uptime:
            return
        self.need_update = True
        self.uptime = uptime
        minutes = int(uptime / 60)
        hours = int(minutes / 60)
        self.uptime_txt = "{h:02d}:{m:02d}:{s:02d}".format(h=hours, m=minutes % 60, s=uptime % 60)
        self.lg_font.text(self.uptime_txt, 23, 42)

    def update_socket(self):
        if self.state.get_socket_on():
            self.red.on()
            self.green.off()
        else:
            self.red.off()
            self.green.on()
