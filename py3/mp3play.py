#!/usr/bin/python3

import os
import time
import pifacecad

def clcdprint(songname):
  if songname == "":
    buf = "Drake's\nMP3 Player"
  else:
    buf = "Now Playing :\n%s" % songname
  cad.lcd.clear()
  cad.lcd.write(buf)
  time.sleep(0.1)

cad = pifacecad.PiFaceCAD()

cad.lcd.clear()
cad.lcd.cursor_off()
cad.lcd.blink_off()
clcdprint("")

os.system("mocp -S");

while True:
  if(cad.switches[3].value):
    f = os.popen("mocp -p")
    f = os.popen("mocp -Q %title")
    songname = f.read()
    clcdprint(songname)

  if(cad.switches[0].value):
    f = os.popen("mocp -r")
    f = os.popen("mocp -Q %title")
    songname = f.read()
    clcdprint(songname)

  if(cad.switches[1].value):
    f = os.popen("mocp -f")
    f = os.popen("mocp -Q %title")
    songname = f.read()
    clcdprint(songname)

  if(cad.switches[4].value):
    f = os.popen("mocp -x")
    exit()
