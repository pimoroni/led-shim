#!/usr/bin/env python

import math
import time

import ledshim

ledshim.set_clear_on_exit()


def show_graph(v, r, g, b):
    v *= ledshim.NUM_PIXELS
    for x in range(ledshim.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        ledshim.set_pixel(x, r, g, b)
        v -= 1

    ledshim.show()


ledshim.set_brightness(0.6)

try:
    while True:
        t = time.time()
        v = (math.sin(t) + 1) / 2   # Get a value between 0 and 1
        show_graph(v, 255, 0, 255)  # Use it as the graph intensity
        time.sleep(0.01)

except KeyboardInterrupt:
    pass
