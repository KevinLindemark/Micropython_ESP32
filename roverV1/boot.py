# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin, PWM
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = ''
password = ''

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
frequency = 5000
motor01 = PWM(Pin(2), frequency)
motor02 = PWM(Pin(12), frequency)
motor03 = PWM(Pin(13), frequency)
motor04 = PWM(Pin(23), frequency)

