# Get request
#
#  free API:
#
#   https://official-joke-api.appspot.com/random_joke
import os
import sys


# Add a directory to sys.path
# sys.path.append("/display")
sys.path.append("/network")
sys.path.append("/resources")


# Project Imports
from wifiConnect import *
import requests


def freeTest():
    res=requests.get("https://official-joke-api.appspot.com/random_joke")
    print(f"raw response: {res.text}")
    return res

def apiToken():
    res=requests.get("https://official-joke-api.appspot.com/random_joke")
    print(f"raw response: {res.text}")
    return res

def freeWeather():
    res=requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")
    print(f"raw response: {res.text}")
    return res


def main():
    ip=wifiConnect()
    req=freeWeather()
    
    '''
    jdata=req.json()
    print("-----------------------------")
    print(f"json pass through: {jdata}")
    print("-----------------------------")
    print(jdata["type"])
    print(jdata["setup"])
    print(jdata["punchline"])
    
    print(jdata.keys())
    print(jdata.values())
    
    keys=jdata.keys()
    print(list(keys))
    '''

# Main
if __name__ == "__main__":
    main()
