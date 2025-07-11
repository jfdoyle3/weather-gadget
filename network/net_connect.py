# Network Connection


# System Imports
import sys
import os

# Add a directory to sys.path
sys.path.append("/display")

import network
import time
from secrets import *
from lcd import *

def net_connect(ssid=secrets['ssid'],psk=secrets['password']):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)

    # Wait for connect or fail
    wait = 10
    waitDisplay=0
    while wait > 0:
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
        return RuntimeError('wifi connection failed')
    else:
        ip=wlan.ifconfig()[0]
        return ip