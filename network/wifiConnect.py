# WiFi Connection


# System Imports
import sys
import os

# Add a directory to sys.path
sys.path.append("/display/lcd")
sys.path.append("/network")
sys.path.append("/resources")

import network
import utime as time
from secrets import *
from lcd import *
from ledCodes import *

def wifiConnect():
    lcdText("Wifi Connect",0,0)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets['ssid'],secrets['password'])
    
    lcdClear()
    

    # Wait for connect or fail
    wait = 10
    waitDisplay=0
    while 0 < wait:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        lcdText('Initalizing WiFi',0,0)
        lcdText('.',waitDisplay,1)
        time.sleep(1)
        waitDisplay += 1

    # Handle connection error
    if wlan.status() != 3:
        # raise RuntimeError('wifi connection failed')
        lcdNotConnected()
        errorCode(3,.5)   # 3 blinks no connection
        powerOff()
        # return RuntimeError('wifi connection failed')
    else:
        ip=wlan.ifconfig()[0]
        print(ip)
        lcdConnected()
        time.sleep(.5)
        lcdClear()
        return ip
    
    
    
    
    
    
    
    
    
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