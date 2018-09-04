#!/usr/bin/env python

import time

import ledshim

ledshim.set_clear_on_exit()
ledshim.set_brightness(0.5)


def show_all(state):
    for i in range(ledshim.NUM_PIXELS):
        val = state * 255
        ledshim.set_pixel(i, val, val, val)
    ledshim.show()


def dot():
    show_all(1)
    time.sleep(0.05)
    show_all(0)
    time.sleep(0.2)


def dash():
    show_all(1)
    time.sleep(0.2)
    show_all(0)
    time.sleep(0.2)


def space():
    time.sleep(0.2)


# 0 is a space, 1 is a dot and 2 is a dash
MORSE = '211101101211022101020120210212000'

while True:
    for m in MORSE:
        if m == '0':
            space()
        elif m == '1':
            dot()
        elif m == '2':
            dash()
