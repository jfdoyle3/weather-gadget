# Get request
#
#  free API:
#
#   https://official-joke-api.appspot.com/random_joke
import os
import sys


# Add a directory to sys.path
sys.path.append("/network")
sys.path.append("/resources")


# Project Imports
from wifiConnect import *
from apiCalls import *
import requests
import json


'''
def main():
    ip=wifiConnect()
    print(ip)
    res=getWeather()    
    print(str(round(res['current']['temperature_2m']))+res['current_units']['temperature_2m'])
    
# Main
 if __name__ == "__main__":
     main()
'''