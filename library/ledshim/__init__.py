from sys import version_info
from . import is31fl3731

__version__ = '0.0.1'

display = is31fl3731.LEDSHIM(None, address=0x75, gamma_table=is31fl3731.LED_GAMMA)

DISPLAY_HEIGHT = display._height
DISPLAY_WIDTH = display._width
NUM_PIXELS = display._width

pixel = display.set_pixel
set_pixel = display.set_pixel
set_all = display.set_all
set_brightness = display.set_brightness
show = display.show
width = display.width
height = display.height
clear = display.clear
get_buffer_shape = display.get_shape
get_shape = display.get_shape
set_clear_on_exit = display.set_clear_on_exit

