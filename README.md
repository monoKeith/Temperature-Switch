## Temperature-Switch

A temperature controlled switch implemented in Micropython.

Can be used for precise temperature control in areas like [sous-vide](https://en.wikipedia.org/wiki/Sous_vide).

This software was tested on Raspberry Pi Pico. Attached with:
- DS18B20 temperature sensor
- I2C 128*64 mono-color display
- 3 LEDs for displaying status
- Rotary encoder to set target temperature
- Relay to control heating element (for example, a cheap rice-cooker that don't have any built-in microcontroller)

Connections:
- Temperature sensor - GP16
- I2C display: SDA - GP26, SCL - GP27
- LEDs: GREEN - GP20, YELLOW - GP19, RED - GP18
- Rotary encoder (no pullup resistor required): GP12, GP13
- Relay: Share pin with RED LED - GP18.

Status:
- Green: temperature above target (heating off)
- Red: temperature below target (heating on)
- Yellow: updating display content
