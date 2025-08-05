# Scrap
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

i2c = I2C(0,sda=Pin(16), scl=Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

ip=wifiConnect()
print(ip)
# res=getWeather()
print(res)
print('temp: '+str(round(res['current']['temperature_2m']))
print('time: '+res['current']['time'])
temp=str(round(res['current']['temperature_2m']))
dateTime=res['current']['time']
time=dateTime[-5:]
hour=int(time[:2])
minute=time[-2:]
date=dateTime[:10]
print(time)
print(hour)
print(minute)
print(date)
# oled.text(f'{temp}',0,0,1)
# oled.show()
if hour>=12 and hour<=23:
    hourPM=hour-12
    print(str(hourPM)+':'+str(minute)+'PM')

if hour>=0 and hour<=11:
    print(str(hour)+':'+str(minute)+'AM')
# PM 12:00 - 23
# AM 0 - 11