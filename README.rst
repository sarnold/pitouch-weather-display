========================================================
 Weather - A PyGame-based weather data/forecast display
========================================================

Original code written by Jim Kemp http://www.ph-elec.com/

Downloaded from:

http://www.instructables.com/id/Raspberry-Pi-Internet-Weather-Station/step4/Source-Code/

Dependencies
============

pywapi
python-pygame

For buttons and usb-serial X10 interface:

RPi.GPIO
python-serial
some X10 module
and (possibly) wiringpi

Comment out the X10 import (and pyserial) to run just the weather interface.

To Localize
===========

Edit weather.py and change the following as needed:

* Zip code in UpdateWeather function
* Display size depending on your display (see comments)

To run from a console
=====================

Change to Weather source diectory and run the command:

  $ DISPLAY=:0 python weather.py


