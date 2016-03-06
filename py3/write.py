#!/usr/bin/python3

import os
import sys
import time
import pifacecad

def clcdprint(songname):
  if songname == "":
    buf = "Drake's\nMessage Show"
  else:
    buf = songname
  cad.lcd.clear()
  cad.lcd.write(buf)
  time.sleep(0.1)

cad = pifacecad.PiFaceCAD()

cad.lcd.clear()
cad.lcd.cursor_off()
cad.lcd.blink_off()
if len(sys.argv) is 1:
  clcdprint("")
else:
  clcdprint(sys.argv[1])

if len(sys.argv) is 3:
  cad.lcd.backlight_on()
