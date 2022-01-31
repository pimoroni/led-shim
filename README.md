# LED SHIM

[![Build Status](https://travis-ci.com/pimoroni/led-shim.svg?branch=master)](https://travis-ci.com/pimoroni/led-shim)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/led-shim/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/led-shim?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/ledshim.svg)](https://pypi.python.org/pypi/ledshim)
[![Python Versions](https://img.shields.io/pypi/pyversions/ledshim.svg)](https://pypi.python.org/pypi/ledshim)

https://shop.pimoroni.com/products/led-shim

28 tiny RGB LED pixels in a single row that just slip right onto your Pi's pins, no soldering required! LED SHIM is ideal for status updates, notifications, a VU meter, or as a bar graph for sensor readings.

## Installing

### Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get your LED SHIM
up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the command exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
curl https://get.pimoroni.com/ledshim | bash
```

### Manual install:

```bash
python3 -m pip install ledshim
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
python3 setup.py install
```

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/led-shim
* Function reference - http://docs.pimoroni.com/ledshim/
* GPIO Pinout - https://pinout.xyz/pinout/led_shim
* Get help - http://forums.pimoroni.com/c/support
