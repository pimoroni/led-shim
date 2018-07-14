.. role:: python(code)
   :language: python

Welcome
-------

This documentation will guide you through the methods available in the LED SHIM Python library.

LED SHIM provides a row of 24 tiny RGB LEDs which you can light up with any colour you like!

* More information - https://shop.pimoroni.com/products/led-shim
* Get the code - https://github.com/pimoroni/led-shim
* GPIO pinout - https://pinout.xyz/pinout/led_shim
* Get help - http://forums.pimoroni.com/c/support

.. currentmodule:: ledshim.is31fl3731.Matrix

At A Glance
-----------

.. autoclassoutline:: ledshim.is31fl3731.Matrix
   :members:

.. toctree::
   :titlesonly:
   :maxdepth: 0

Set A Single Pixel In Buffer
----------------------------

When you set a pixel it will not immediately display on LED SHIM, you must call :python:`ledshim.show()`.

.. automethod:: ledshim.is31fl3731.Matrix.set_pixel
   :noindex:

Display Buffer
--------------

All of your changes to LED SHIM are stored in a Python buffer. To display them
on LED SHIM you must call :python:`ledshim.show()`.

.. automethod:: ledshim.is31fl3731.Matrix.show
   :noindex:

Clear Buffer
------------

.. automethod:: ledshim.is31fl3731.Matrix.clear
   :noindex:

Get The Display Size
--------------------

.. automethod:: ledshim.is31fl3731.Matrix.get_shape
   :noindex:
