# WiFi Connection


# System Imports
import sys
import os

# Add a directory to sys.path


import network
import utime as time
from secrets import *

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'],secrets['password'])


# Wait for connect or fail
wait = 10

while 0 < wait:
    if wlan.status() < 0 or wlan.status() >= 3:
        print('wifi failed')
        sys.exit()
        break

# Handle connection error
if wlan.status() != 3:
    # raise RuntimeError('wifi connection failed')
    RuntimeError('wifi connection failed')
else:
    ip=wlan.ifconfig()[0]
    print('wifi connected')
    print(ip)
    
'''    
import mip
print('Installing libraries')
# Libaries

mip.install("ssd1306")

'''


print('libraries installed')
print('end of line')