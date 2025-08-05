#
#    Weather Gadget
#   ----------------
# Open Weather Current Temp - small respaonse set
# https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch 
#
# Test - Random Joke
# https://official-joke-api.appspot.com/random_joke
# 
# API Time
# curl "http://worldtimeapi.org/api/timezone/America/New_York"
# 
# Display:  I2C:0 SDA:16 SCL:17
# BME280    I2C:1 SDA:18 SCL:19

# System Imports
import os
import sys


# Add a directory to sys.path
# sys.path.append("/display")
sys.path.append("/network")
sys.path.append("/resources")


# Project Imports
from wifiConnect import *
from apiCalls import *
from ledCodes import *
from oledLib import *
from bme280Lib import *
from gui import *

    
    
def main():
    # was a function on some itteration - keeping to
    # remeber to make one
    # initApp()
    
    print('Start')
    ip, percent=wifiConnect()

    # indoorTemp=getTempF()
    guiHeader(percent)
    guiGraphics()
    # guiInfo(indoorTemp)
    displayGUI()

    
    
# Main
if __name__ == "__main__":
    main()