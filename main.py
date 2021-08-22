import machine, onewire, ds18x20, time
import display

# Setup temp sensor
ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found a ds18x20 device')
 

# Init
d = display.Display()

while True:
    d.run()
    ds_sensor.convert_temp()
    for rom in roms:
        temp = ds_sensor.read_temp(rom)
        d.set_cur_temp(temp)

