#!/usr/bin/env python

import random
import time

import ledshim

ledshim.set_clear_on_exit()
ledshim.set_brightness(0.4)

while True:
    for i in range(ledshim.NUM_PIXELS):
        ledshim.set_pixel(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    ledshim.show()
    time.sleep(0.05)
