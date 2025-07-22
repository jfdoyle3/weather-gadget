#  Weather Gadget
# ----------------
#
# https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&hourly=temperature_2m&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch
# 

# System Imports
import os
import sys

# Add a directory to sys.path
sys.path.append("/display/lcd")
sys.path.append("/network")
sys.path.append("/resources")

# Project Imports
from wifiConnect import *
from apiCalls import *
from ledCodes import *
from lcd import *
from button import *

def powerOff():
    lcdOff()
    sys.exit()


def main():
    print("wifi init")
    ip=wifiConnect()
        
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
        
        
        buttonPress()
        
    except Exception as e:
        print("Error:", e)
    
    powerOff()
    
# Main
if __name__ == "__main__":
    main()