import network
import utime
import sys
import esp
esp.osdebug(None)

import gc
gc.collect()

# turn off the WiFi Access Point
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

ssid = 'hotspot navn'
password = 'hotspot kode'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
# wait until the device is connected to the WiFi network
MAX_ATTEMPTS = 20
attempt_count = 0
while not station.isconnected() and attempt_count < MAX_ATTEMPTS:
    attempt_count += 1
    utime.sleep(1)

if attempt_count == MAX_ATTEMPTS:
    print('could not connect to the WiFi network')
    sys.exit()

print('Connection successful')
print(station.ifconfig())