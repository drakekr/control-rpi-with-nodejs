#!/usr/bin/python3

import os
import sys
import time
import pifacecad

def clcdprint(songname):
  if songname == "":
    buff = pifacecad.LCDBitmap([0x02, 0x0a, 0x17, 0x16, 0x0a, 0x02, 0x10, 0x1e])
    cad.lcd.store_custom_bitmap(0, buff)
    buff = pifacecad.LCDBitmap([0x11, 0x17, 0x11, 0x17, 0x1d, 0x02, 0x05, 0x02])
    cad.lcd.store_custom_bitmap(1, buff)
    buff = pifacecad.LCDBitmap([0x08, 0x1c, 0x02, 0x0a, 0x17, 0x0a, 0x02, 0x02])
    cad.lcd.store_custom_bitmap(2, buff)
    buff = pifacecad.LCDBitmap([0x01, 0x09, 0x17, 0x15, 0x17, 0x01, 0x01, 0x00])
    cad.lcd.store_custom_bitmap(3, buff)
    buff = pifacecad.LCDBitmap([0x04, 0x0a, 0x0a, 0x04, 0x00, 0x0a, 0x0a, 0x1f])
    cad.lcd.store_custom_bitmap(4, buff)
    buff = pifacecad.LCDBitmap([0x3f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f])
    cad.lcd.store_custom_bitmap(5, buff)
    cad.lcd.store_custom_bitmap(6, buff)
    cad.lcd.store_custom_bitmap(7, buff)
#    cad.lcd.store_custom_bitmap(8, buff)
    cad.lcd.clear()
    cad.lcd.write_custom_bitmap(0)
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write_custom_bitmap(2)
    cad.lcd.write_custom_bitmap(3)
    cad.lcd.write_custom_bitmap(4)
    cad.lcd.write_custom_bitmap(5)
    cad.lcd.write_custom_bitmap(6)
    cad.lcd.write_custom_bitmap(7)
#    cad.lcd.write_custom_bitmap(12)
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
