'''
    Weather Gadget
   ----------------
 Open Weather Current Temp - small respaonse set
 https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch 

 Test - Random Joke
 https://official-joke-api.appspot.com/random_joke
''' 

# System Imports
import os
import sys


# Add a directory to sys.path
sys.path.append("/display/oled")
sys.path.append("/network")
sys.path.append("/resources")
sys.path.append("/bme280")


# Project Imports
from wifiConnect import *
from apiCalls import *
from ledCodes import *
from oledLib import *
from bme280Lib import *
import json
import network

    
    
def main():
    # initApp()
    
    ip=wifiConnect()
    
    print(ip)
    
    wlan = network.WLAN(network.STA_IF)
    rssi=wlan.status('rssi')
    print(f'RSSI: {rssi} dBm')
    
    clamped_rssi=max(min(rssi, -30),-90)
    percent=int((clamped_rssi +90) *100 /60)
    
    print(f'Signal Strength: {percent}%')
# Main
if __name__ == "__main__":
    main()