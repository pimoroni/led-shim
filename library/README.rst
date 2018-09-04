LED SHIM
========

|Build Status| |Coverage Status| |PyPi Package| |Python Versions|

https://shop.pimoroni.com/products/led-shim

28 tiny RGB LED pixels in a single row that just slip right onto your
Pi's pins, no soldering required! LED SHIM is ideal for status updates,
notifications, a VU meter, or as a bar graph for sensor readings.

Installing
----------

Full install (recommended):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've created an easy installation script that will install all
pre-requisites and get your LED SHIM up and running with minimal
efforts. To run it, fire up Terminal which you'll find in Menu ->
Accessories -> Terminal on your Raspberry Pi desktop, as illustrated
below:

.. figure:: http://get.pimoroni.com/resources/github-repo-terminal.png
   :alt: Finding the terminal

   Finding the terminal

In the new terminal window type the command exactly as it appears below
(check for typos) and follow the on-screen instructions:

.. code:: bash

    curl https://get.pimoroni.com/ledshim | bash

Alternatively, on Raspbian, you can download the ``pimoroni-dashboard``
and install your product by browsing to the relevant entry:

.. code:: bash

    sudo apt-get install pimoroni

(you will find the Dashboard under 'Accessories' too, in the Pi menu -
or just run ``pimoroni-dashboard`` at the command line)

If you choose to download examples you'll find them in
``/home/pi/Pimoroni/ledshim/``.

Manual install:
~~~~~~~~~~~~~~~

Library install for Python 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python3-ledshim

other environments:

.. code:: bash

    sudo pip3 install ledshim

Library install for Python 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python-ledshim

other environments:

.. code:: bash

    sudo pip2 install ledshim

Development:
~~~~~~~~~~~~

If you want to contribute, or like living on the edge of your seat by
having the latest code, you should clone this repository, ``cd`` to the
library directory, and run:

.. code:: bash

    sudo python3 setup.py install

(or ``sudo python setup.py install`` whichever your primary Python
environment may be)

In all cases you will have to enable the i2c bus.

Documentation & Support
-----------------------

-  Guides and tutorials - https://learn.pimoroni.com/led-shim
-  Function reference - http://docs.pimoroni.com/ledshim/
-  GPIO Pinout - https://pinout.xyz/pinout/led\_shim
-  Get help - http://forums.pimoroni.com/c/support

.. |Build Status| image:: https://travis-ci.com/pimoroni/led-shim.svg?branch=master
   :target: https://travis-ci.com/pimoroni/led-shim
.. |Coverage Status| image:: https://coveralls.io/repos/github/pimoroni/led-shim/badge.svg?branch=master
   :target: https://coveralls.io/github/pimoroni/led-shim?branch=master
.. |PyPi Package| image:: https://img.shields.io/pypi/v/ledshim.svg
   :target: https://pypi.python.org/pypi/ledshim
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/ledshim.svg
   :target: https://pypi.python.org/pypi/ledshim
