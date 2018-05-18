# LED SHIM
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

Alternatively, on Raspbian, you can download the `pimoroni-dashboard` and install your product by browsing to the relevant entry:

```bash
sudo apt-get install pimoroni
```
(you will find the Dashboard under 'Accessories' too, in the Pi menu - or just run `pimoroni-dashboard` at the command line)

If you choose to download examples you'll find them in `/home/pi/Pimoroni/ledshim/`.

### Manual install:

#### Library install for Python 3:

on Raspbian:

```bash
sudo apt-get install python3-ledshim
```

other environments: 

```bash
sudo pip3 install ledshim
```

#### Library install for Python 2:

on Raspbian:

```bash
sudo apt-get install python-ledshim
```

other environments: 

```bash
sudo pip2 install ledshim
```

### Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you should clone this repository, `cd` to the library directory, and run:

```bash
sudo python3 setup.py install
```
(or `sudo python setup.py install` whichever your primary Python environment may be)

In all cases you will have to enable the i2c bus.

## Documentation & Support

* Guides and tutorials - https://learn.pimoroni.com/led-shim
* Function reference - http://docs.pimoroni.com/ledshim/
* GPIO Pinout - https://pinout.xyz/pinout/led_shim
* Get help - http://forums.pimoroni.com/c/support
