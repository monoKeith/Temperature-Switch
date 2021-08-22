from machine import Pin, I2C
from oled import Write, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20

SDA_PIN, SCL_PIN = 26, 27

class Display():

    def __init__(Self):
        # Vars
        Self.need_update = False
        Self.cur_temp = ""
        # Settings
        Self.i2c=I2C(1, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
        Self.oled = SSD1306_I2C(128, 64, Self.i2c)
        Self.lg_font = Write(Self.oled, ubuntu_mono_20)
        Self.md_font = Write(Self.oled, ubuntu_mono_15)

    def run(Self):
        # Update display if needed
        if not Self.need_update:
            return
        Self.oled.fill(0)
        # Current Temp
        Self.lg_font.text(Self.cur_temp, 0, 0)
        Self.oled.show()


    def set_cur_temp(Self, temp):
        if Self.cur_temp == temp :
            return
        Self.need_update = True
        Self.cur_temp = "{actual:.1f} C".format(actual=temp)