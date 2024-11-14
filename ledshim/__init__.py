"""LED SHIM 28-pixel RGB LED display."""
from . import is31fl3731

__version__ = "0.0.3"

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


def set_multiple_pixels(indexes, from_colour, to_colour=None):
    """Set multiple pixels to a range of colours sweeping from from_colour to to_colour.

    :param from_colour: A tuple with 3 values representing the red, green and blue of the first colour
    :param to_colour: A tuple with 3 values representing the red, green and blue of the second colour

    """
    if to_colour is None:
        to_colour = from_colour

    length = float(len(indexes))
    step = 0
    from_r, from_g, from_b = from_colour
    to_r, to_g, to_b = to_colour
    step_r, step_g, step_b = to_r - from_r, to_g - from_g, to_b - from_b
    step_r /= length
    step_g /= length
    step_b /= length

    for index in indexes:
        set_pixel(index, from_r + (step_r * step), from_g + (step_g * step), from_b + (step_b * step))
        step += 1
