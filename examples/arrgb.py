#!/usr/bin/env python

import time

import ledshim

r, g, b = 255, 0, 0

delay = 0.1

half_way = ledshim.NUM_PIXELS // 2

while True:
    # Turn pixels on
    for x in range(half_way):
        ledshim.set_pixel(half_way - 1 - x, r, g, b)
        ledshim.set_pixel(half_way + x, r, g, b)
        ledshim.show()
        time.sleep(delay)

    # Turn pixels off
    for x in range(half_way):
        ledshim.set_pixel(x, 0, 0, 0)
        ledshim.set_pixel(ledshim.NUM_PIXELS - 1 - x, 0, 0, 0)
        ledshim.show()
        time.sleep(delay)
