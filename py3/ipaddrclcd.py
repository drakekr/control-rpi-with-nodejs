#!/usr/bin/python3

import socket
import fcntl
import struct
import pifacecad as p

def get_ip(iface = 'eth0'):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sockfd = sock.fileno()
  ifreq = struct.pack('16sH14s', iface.encode('utf-8'), socket.AF_INET, b'\x00'*14)
  try:
    res = fcntl.ioctl(sockfd, 0x8915, ifreq)
  except:
    return None
  ip = struct.unpack('16sH2x4s8x', res)[2]
  return socket.inet_ntoa(ip)

greet = "Wired Connected"
ipaddr = get_ip("eth0")
if(ipaddr == None):
  greet = "Wireless Connected"
  ipaddr = get_ip("wlan0")
if(ipaddr == None):
  greet = "Hello UKC!"
  ipaddr = "No Internet"

cad = p.PiFaceCAD()

cad.lcd.backlight_on()
cad.lcd.write(greet)
cad.lcd.write("\n")
cad.lcd.write(ipaddr)
cad.lcd.cursor_off()
cad.lcd.blink_off()
