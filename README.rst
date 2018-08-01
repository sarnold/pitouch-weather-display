===========================================================
 Weather.py - A PyGame-based weather data/forecast display
===========================================================

Original code written by Jim Kemp http://www.ph-elec.com/ and downloaded
from: http://www.instructables.com/id/Raspberry-Pi-Internet-Weather-Station/step4/Source-Code/

Scheduler, backlight, and display adjustments by Stephen Arnold.  Note the
legacy branch contains the original code.

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

The Basics
==========

The old behavior (see legacy branch) was to stay on the weather display all
the time; using the keyboard to switch displays would automatically switch
back to the weather display after five minutes.  The new behavior is to
switch between the weather and site-info displays once each minute (nominal).

The site-info (help) display starts on the minute and then waits for approx. one
minute to switch.  The weather data lookup is now run via scheduler (instead
of being tied to the one-minute display cycle) and defaults to 15 minutes
(since external observations are hourly).

The code still supports GPIO buttons (eg, for a small PiTFT display) but the
X-10 serial interface is commented out.

The code requires a network interface for time and weather data sync (currently
uses weather.com).  On the updated master branch, set backlight_control to False
if you don't want the display to dim during non-daylight hours. Use legacy branch
if you want the original behavior.

To Localize
===========

Edit weather.py and change the following as needed:

* Zip code in UpdateWeather function
* Display size depending on your display (see comments)
* backlight_control and tap_mode

To run from a console
=====================

Change to Weather source directory and run the command::

  $ sudo DISPLAY=:0 python weather.py

To run in the background with logging, try::

  $ sudo DISPLAY=:0 python -u weather.py > >(tee -a out.log) 2> >(tee err.log >&2) &

.. note:: On Raspbian at least, sudo is required to access the framebuffer;
          even after adding the pi user to the video group, the following
          exception is raised without sudo.
          
          ``Exception: No suitable video driver found!``


Keyboard and Touch Controls
===========================

The main keyboard and touch controls only depend on pygame, however, if
backlight_control is enabled, touch_mode="backlight" depends on the
rpi-backlight tool (see below).  If you don't have the required display
hardware, set backlight_control="False".

* Keyboard controls

  * q or keypad Enter - quit program
  * u or keypad '+' - raise backlight 10%
  * d or keypad '-' - lower backlight 10%
  * c - switch to calendar display
  * w - switch to weather display
  * h - switch to site info display

* Touch / Click controls

  * tap_mode unset

    * double-tap - quit program
    * single-tap - does nothing

  * tap_mode="backlight"

    * double-tap - turn backlight off
    * single-tap - turn backlight on

.. note:: The backlight min/max commands are controlled by schedulers
          according to sunrise/sunset.

Pi Foundation Touch Display
===========================

For rpi-backlight control on this display, install

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


