#!/usr/bin/env python

import time
from subprocess import PIPE, Popen

import ledshim

ledshim.set_clear_on_exit()


def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode()

    pos_start = output.index('=') + 1
    pos_end = output.rindex("'")

    temp = float(output[pos_start:pos_end])

    return temp


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

while True:
    v = get_cpu_temperature() / 100.0
    show_graph(v, 255, 255, 255)
    time.sleep(0.01)
