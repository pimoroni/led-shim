import time

import ledshim

for x in range(ledshim.width):
    ledshim.set_pixel(x,255,0,0)
    ledshim.show()
    time.sleep(0.05)

time.sleep(0.1)
ledshim.clear()
ledshim.show()

for x in range(ledshim.width):
    ledshim.set_pixel(x,0,255,0)
    ledshim.show()
    time.sleep(0.05)

time.sleep(0.1)
ledshim.clear()
ledshim.show()

for x in range(ledshim.width):
    ledshim.set_pixel(x,0,0,255)
    ledshim.show()
    time.sleep(0.05)
