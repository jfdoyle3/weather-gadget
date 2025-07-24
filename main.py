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
import json

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
    

def initApp():
     print("wifi init")
     lcdClear()
     ip=wifiConnect()


def main():
    initApp()
    '''        
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
    
    # res = requests.get(url='https://api.weather.gov/points/41.87092932,-71.42788283')
    # print(res.text)
    apiURL='https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch '
    # Make the HTTP GET request
    try:
        # req=freeAPIRequest(apiURL)
        with open('/files/f.json') as f:
            data = json.load(f)
        
        # Access parsed data
        print(data)
        print('>>------------------------->')
        print('<-------------------------<<')
        
        temp="{:.0f}".format(data['current']['temperature_2m'])
        unit=data['current_units']['temperature_2m']
        
        print(f"{temp}{unit}")
        
        #lcdText(f"{temp}{unit}",0,0)
        lcdText("Hi",0,0)
        
        buttonPress()
        
    except Exception as e:
        print("Error:", e)
    
    powerOff()
    
# Main
if __name__ == "__main__":
    main()