# WiFi Connection
#
# Try catch here.


# System Imports
import sys
import os

# Add a directory to sys.path
sys.path.append("/display/oled")
sys.path.append("/network")
sys.path.append("/resources")

import network
import utime as time
from secrets import *
from oledLib import *
from ledCodes import *

def wifiConnect():
   # oledText("Wifi Connect",0,0)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets['ssid'],secrets['password'])
    
    # oledClear()



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
     #   oledNotConnected()
        errorCode(3,.5)   # 3 blinks no connection
     #   powerOff()
        # return RuntimeError('wifi connection failed')
    else:
        ip=wlan.ifconfig()[0]
       # print(ip)
       # oledConnected()
       # time.sleep(.5)
       # oledClear()
        rssi=wlan.status('rssi')
        clamped_rssi=max(min(rssi, -30),-90)
        percent=int((clamped_rssi +90) *100 /60)
        return ip,percent
    
    
    
    
    
    
    
    
    
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