#!/usr/bin/env python

import time

import ledshim

ledshim.set_clear_on_exit()

REDS = [0] * ledshim.NUM_PIXELS * 2
SCAN = [1, 2, 4, 8, 16, 32, 64, 128, 255]
REDS[ledshim.NUM_PIXELS - len(SCAN):ledshim.NUM_PIXELS + len(SCAN)] = SCAN + SCAN[::-1]

start_time = time.time()

while True:
    # Sine wave, spends a little longer at min/max
    # delta = (time.time() - start_time) * 8
    # offset = int(round(((math.sin(delta) + 1) / 2) * (ledshim.NUM_PIXELS - 1)))

    # Triangle wave, a snappy ping-pong effect
    delta = (time.time() - start_time) * ledshim.NUM_PIXELS * 2
    offset = int(abs((delta % len(REDS)) - ledshim.NUM_PIXELS))

    for i in range(ledshim.NUM_PIXELS):
        ledshim.set_pixel(i, REDS[offset + i], 0, 0)

    ledshim.show()

    time.sleep(0.05)
