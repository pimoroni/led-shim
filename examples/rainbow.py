#!/usr/bin/env python

import colorsys
import time

import ledshim

spacing = 360.0 / 16.0
hue = 0

ledshim.set_clear_on_exit()
ledshim.set_brightness(0.8)

while True:
    hue = int(time.time() * 100) % 360
    for x in range(ledshim.NUM_PIXELS):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        ledshim.set_pixel(x, r, g, b)

    ledshim.show()
    time.sleep(0.0001)
