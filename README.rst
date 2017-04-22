========================================================
 Weather - A PyGame-based weather data/forecast display
========================================================

Original code written by Jim Kemp http://www.ph-elec.com/

Downloaded from:

http://www.instructables.com/id/Raspberry-Pi-Internet-Weather-Station/step4/Source-Code/

Dependencies
============

Python:

* pywapi - https://pypi.python.org/pypi/pywapi
* schedule - https://pypi.python.org/pypi/schedule
* pygame - https://pypi.python.org/pypi/Pygame

If there is no deb package for any of the above, try "pip install [package_name]".

Also, for buttons and usb-serial X10 interfaces:

* RPi.GPIO (should already be installed in Raspbian)
* python-serial
* and (possibly) wiringpi

For rpi-backlight control:

* rpi-backlight

The rpi-backlight tool is available either via deb package or manual build/install;
see `the rpi-backlight github repo`_ and the `deb package build howto`_ for details.

.. _the rpi-backlight github repo: https://github.com/sarnold/rpi-backlight
.. _deb package build howto: https://github.com/sarnold/af_alg/blob/master/deb-build-howto.rst

Mostly you can ignore the sources.list and other setup details, just install the
build dependencies, clone the repo, cd and run the build command, then install it::

  $ sudo apt-get install devscripts build-essential
  $ cd ~/src
  $ git clone https://github.com/sarnold/rpi-backlight
  $ cd rpi-backlight
  $ debuild -b -uc -us
  $ sudo dpkg -i ../rpi-backlight_0.0.1-1-raspbian+1_armhf.deb

.. note:: rpi-backlight only works with the Pi Foundation touch display:
          https://www.raspberrypi.org/products/raspberry-pi-touch-display/

Comment out the X10 import (and pyserial) to run just the weather interface.

Also requires a network interface for time and weather data sync (currently
uses weather.com).  On the updated master branch, set backlight_control to False
if you don't want the display to dim during nightime hours. The flip period
is currently one minute (to match the weather mode refresh) and is not really
that flexible without refactoring the timing of display refresh and data
lookup.  Use legacy branch if you want the original behavior.

To Localize
===========

Edit weather.py and change the following as needed:

* Zip code in UpdateWeather function
* Display size depending on your display (see comments)

To run from a console
=====================

Change to Weather source diectory and run the command::

  $ DISPLAY=:0 python weather.py

To run in the backgound with logging, try::

  DISPLAY=:0 python -u weather.py > >(tee -a out.log) 2> >(tee err.log >&2) &


