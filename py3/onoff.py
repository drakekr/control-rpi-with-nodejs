#!/usr/bin/python3

import os
import sys
import time
import pifacecad

cad = pifacecad.PiFaceCAD()

if len(sys.argv) is 1:
  exit()

if sys.argv[1] == "on":
  cad.lcd.backlight_on()

if sys.argv[1] == "off":
  cad.lcd.backlight_off()
