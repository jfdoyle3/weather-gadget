# BME280 Library
#
# bme.values returns: Temperature C, Pressure, humidity

import os
import sys

# Add a directory to sys.path
sys.path.append("/display/oled")
sys.path.append("/network")
sys.path.append("/bme280")

from machine import I2C, Pin
import bme280_float as bme280


i2cBME = I2C(1, sda=Pin(18), scl=Pin(19), freq=40000)
bme = bme280.BME280(i2c=i2cBME)

# def getTemp():
temp=bme.values[0]
press=bme.values[1]
humid=bme.values[2]
altitude=bme.altitude
seaLevel=bme.sealevel
dewPoint=bme.dew_point


def getTempC():
    temp=temp
    return tempC

def getTempF():
    tempLen=len(temp)
    celTemp=temp[:-1]
    celTempFloat=float(celTemp)
    fahrenheit=(celTempFloat*1.8)+32
    tempF="{:.2f}F".format(fahrenheit)
    return tempF



'''
temp=bme.values[0]



print(temp)

print(bme.altitude)

print(bme.sealevel)
'''