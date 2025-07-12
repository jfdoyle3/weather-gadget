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
import ujson
from machine import Pin
from wifiConnect import *
from apiCalls import *
from ledCodes import *
from secrets import *
from lcd import *

def powerOff():
    ledOff()
    lcdOff()
    sys.exit()


def main():
    ip=net_connect(ssid=secrets['ssid'],psk=secrets['password'])
        
    # No WiFi connection - Exit
    if not isinstance(ip, str):
        lcdNotConnected()
        errorCode(3,.5)   # 3 blinks no connection
        powerOff()
        
    # Connected to net
    lcdConnected()
    print(ip)
    ledOn()
    
    # res = requests.get(url='https://api.weather.gov/points/41.87092932,-71.42788283')
    # print(res.text)
    apiURL='https://official-joke-api.appspot.com/random_joke'
    # Make the HTTP GET request
    try:
        req=freeAPIRequest(apiURL)
        
        # Access parsed data
        print(req["type"])
        print(req["setup"])
        print(req["punchline"])
        
    except Exception as e:
        print("Error:", e)
    
    powerOff()
    
# Main
if __name__ == "__main__":
    main()