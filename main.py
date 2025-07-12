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
import ujason
from machine import Pin
from net_connect import net_connect
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
    
    # Make the HTTP GET request
    try:
        response = requests.get(url='https://official-joke-api.appspot.com/random_joke')
        print(response.text)
        json_data = response.json()  # Directly parse the JSON response
        response.close()
        
        # Process the parsed data (e.g., access a specific value)
        if "key" in json_data:
            print("Value:", json_data["key"])
    
        # Parse the JSON string
        data = ujson.loads(json_data)
        
        # Access parsed data
        print(f"Type: {data['type']}")
        print(f"setup: {data['setup']}")
        print(f"punchline: {data['punchline']}")

    except Exception as e:
        print("Error:", e)
    
    powerOff()
    
# Main
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    


