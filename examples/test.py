#!/usr/bin/env python
import time
import ledshim

for col in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
    r, g, b = col
    for x in range(ledshim.DISPLAY_WIDTH):
        ledshim.clear()
        ledshim.set_pixel(x, r, g, b)
        ledshim.show()
        time.sleep(0.2)
