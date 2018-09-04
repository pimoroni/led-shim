#!/usr/bin/env python

import colorsys
import math
import time

import ledshim

ledshim.set_clear_on_exit()

hue_range = 120
hue_start = 0
max_brightness = 0.8


def show_graph(v, r, g, b):
    v *= ledshim.NUM_PIXELS
    for x in range(ledshim.NUM_PIXELS):
        hue = ((hue_start + ((x / float(ledshim.NUM_PIXELS)) * hue_range)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        if v < 0:
            brightness = 0
        else:
            brightness = min(v, 1.0) * max_brightness

        ledshim.set_pixel(x, r, g, b, brightness)
        v -= 1

    ledshim.show()


ledshim.set_brightness(0.6)

try:
    while True:
        t = time.time() * 2
        v = (math.sin(t) + 1) / 2   # Get a value between 0 and 1
        show_graph(v, 255, 0, 255)  # Use it as the pixel index
        time.sleep(0.01)

except KeyboardInterrupt:
    pass
