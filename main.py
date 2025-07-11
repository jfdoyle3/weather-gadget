## Weather
##----------------
## Uncomment here the LCD Display
## and resources/init.py
## To enable Display

# System Imports
import sys
import os

# Add a directory to sys.path
sys.path.append("/display")
sys.path.append("/network")
sys.path.append("/resources")

# Project Imports
import network
import time
import urequests as requests
from machine import Pin
from net_connect import net_connect
from ledCodes import *
from secrets import *
from lcd import *

def main():
    ip=net_connect(ssid=secrets['ssid'],psk=secrets['password'])
        
    # No WiFi connection - Exit
    if not isinstance(ip, str):
        lcdNotConnected()
        errorCode(3,.5)   # 3 blinks no connection
        lcdOff()
        sys.exit()
        
    # Connected to net
    lcdConnected()
    ledOn()
    
    
    # Request from url - output as text
    res = requests.get(url='https://api.weather.gov/points/41.87092932,-71.42788283')
    print(res.text)
    ledOff()
    lcdOff()
    sys.exit()
# Main
if __name__ == "__main__":
    main()