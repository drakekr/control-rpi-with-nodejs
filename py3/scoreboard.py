#!/usr/bin/python3

import time
import pifacecad

def clcdprint(ateam, ateamscore, bteam, bteamscore):
  buf = "%s : %d\n%s : %d" % (ateam, ateamscore, bteam, bteamscore)
  cad.lcd.clear()
  cad.lcd.write(buf)
  time.sleep(0.1)

def winprint(teamname):
  if(teamname == ""):
    buf = "Unbelivable!\nTie Game!"
  else:
    buf = "Congratulation\n%s Wins" % teamname

  for i in range(0, 10):
    if(i % 2 == 0):
      cad.lcd.clear()
    else:
      cad.lcd.write(buf)
    time.sleep(1)

cad = pifacecad.PiFaceCAD()
ateam = "A Team"
bteam = "B Team"
ateamscore = 0
bteamscore = 0

inputok = False

while not inputok:
  ateam = input("What's the name of A-Team? :")
  if len(ateam) > 10:
    print("Name is too long")
  if len(ateam) < 1:
    print("Please input name")
  inputok = True

inputok = False

while not inputok:
  bteam = input("What's the name of B-Team? :")
  if len(bteam) > 10:
    print("Name is too long")
  if len(bteam) < 1:
    print("Please input name")
  inputok = True

cad.lcd.clear()
cad.lcd.cursor_off()
cad.lcd.blink_off()
clcdprint(ateam, ateamscore, bteam, bteamscore)

while True:
  if(cad.switches[3].value):
    ateamscore = 0
    bteamscore = 0
    clcdprint(ateam, ateamscore, bteam, bteamscore)

  if(cad.switches[0].value):
    ateamscore += 1
    clcdprint(ateam, ateamscore, bteam, bteamscore)

  if(cad.switches[1].value):
    bteamscore += 1
    clcdprint(ateam, ateamscore, bteam, bteamscore)

  if(cad.switches[4].value):
    if(ateamscore > bteamscore):
      winprint(ateam)
      exit()
    if(ateamscore < bteamscore):
      winprint(bteam)
      exit()
    winprint('')
    exit()
