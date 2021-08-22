from machine import Pin
from state import State
import onewire, ds18x20

class TempSensor():

    def __init__(self, state):
        # Setup temp sensor
        self.sensor = ds18x20.DS18X20(onewire.OneWire(Pin(16)))
        self.state = state
        self.reset()

    def reset(self):
        roms = self.sensor.scan()
        self.rom = roms[0] if len(roms) >= 1 else None

    def run(self):
        try:
            self.sensor.convert_temp()
            temp = self.sensor.read_temp(self.rom)
            self.state.set_actual_temp(temp)
        except Exception:
            self.state.set_sensor_err()
            self.reset()
            print("TempSensor error, retrying...")
