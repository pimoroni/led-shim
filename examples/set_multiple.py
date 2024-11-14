#!/usr/bin/env python

import time

import ledshim

# Just green
print('Green')
ledshim.set_multiple_pixels(range(0, 28), (0, 255, 0))
ledshim.show()
time.sleep(1)

# Sweep from yellow to blue, whee!
print('Yellow -> Blue')
ledshim.set_multiple_pixels(range(0, 28), from_colour=(255, 255, 0), to_colour=(0, 0, 255))
ledshim.show()
time.sleep(1)

# Half and half
print('Blue | Red -> Yellow')
ledshim.set_multiple_pixels(range(0, 14), from_colour=(0, 0, 255), to_colour=(128, 128, 255))
ledshim.set_multiple_pixels(range(14, 28), from_colour=(128, 0, 0), to_colour=(255, 255, 0))
ledshim.show()
time.sleep(1)
