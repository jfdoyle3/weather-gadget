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


rssi=wlan.status('rssi')
print(f'RSSI: {rssi} dBm')


# Wait for connect or fail
wait = 10
waitDisplay=0
while 0 < wait:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
#    wait -= 1
#    oledText('Initalizing WiFi',0,0)
#    oledText('.',waitDisplay,1)
#    time.sleep(1)
#    waitDisplay += 1

# Handle connection error
if wlan.status() != 3:
    # raise RuntimeError('wifi connection failed')
    RuntimeError('wifi connection failed')
else:
    ip=wlan.ifconfig()[0]
   # print(ip)
   # oledConnected()
   # time.sleep(.5)
   # oledClear()
    print(ip)
    
    
import mip
mip.install("ssd1306")
    
    
    
    
    
    
    
''''   
   # No WiFi connection - Exit
    if not isinstance(ip, str):
        lcdNotConnected()
        errorCode(3,.5)   # 3 blinks no connection
        powerOff()
        
    # Connected to net
    lcdConnected()
    print(ip)
    ledOn()
'''