#!/usr/bin/env python

import random
import time

import ledshim

ledshim.set_clear_on_exit()

while True:
    pixels = random.sample(range(ledshim.NUM_PIXELS), random.randint(1, 5))
    for i in range(ledshim.NUM_PIXELS):
        if i in pixels:
            ledshim.set_pixel(i, 255, 150, 0)
        else:
            ledshim.set_pixel(i, 0, 0, 0)
    ledshim.show()
    time.sleep(0.05)
