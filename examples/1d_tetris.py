#!/usr/bin/env python

import time
from random import randint

import ledshim

MAX_SIZE = 4
MAX_GRID = ledshim.NUM_PIXELS + MAX_SIZE - 1

OFF = (0, 0, 0)
grid = [OFF] * (MAX_GRID + 1)

ledshim.set_clear_on_exit()


# The tetris algorithm fail when random_color was 0,0,0 now avoided
def random_color():
    return (randint(0, 255), randint(0, 255), randint(1, 50))


def random_tile(max_size, min_size=1):
    return (randint(min_size, max_size), random_color())


def place(tile):
    for i in range(0, tile[0]):
        grid[MAX_GRID - i - len(tile)] = tile[1]


def update():
    for i in range(ledshim.NUM_PIXELS):
        ledshim.set_pixel(i, grid[i][0], grid[i][1], grid[i][2])
    ledshim.show()


def has_lines():
    return grid[0] != OFF


def get_lines():
    lines = []
    for i, color in enumerate(grid):
        if color == OFF:
            return lines
        else:
            lines.append(i)
    return lines


def blink_lines():
    def hide():
        for line in get_lines():
            ledshim.set_pixel(line, 0, 0, 0)
        ledshim.show()

    hide()
    time.sleep(0.5)
    update()
    time.sleep(0.5)
    hide()
    time.sleep(0.5)


def remove_lines():
    for line in get_lines():
        grid[line] = OFF


def gravity():
    grid.append(OFF)
    grid.pop(0)


def main():
    ledshim.set_brightness(0.6)
    place(random_tile(MAX_SIZE))
    update()

    while True:
        time.sleep(0.5)

        if has_lines():
            blink_lines()
            remove_lines()
            place(random_tile(MAX_SIZE))
        else:
            gravity()

        update()


if __name__ == '__main__':
    main()
