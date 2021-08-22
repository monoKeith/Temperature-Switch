## Temperature-Switch

A temperature controlled switch implemented in Micropython.

Can be used for precise temperature control in areas like [sous-vide](https://en.wikipedia.org/wiki/Sous_vide).

This software was tested on Raspberry Pi Pico. Attached with:
- I2C 128*64 mono-color display
- 3 LEDs for displaying status
- Rotary encoder to set target temperature
- Relay to control heating element (for example, a cheap rice-cooker that don't have any built-in microcontroller)

