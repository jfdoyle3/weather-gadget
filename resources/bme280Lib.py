# BME280 Library
#
# bme.values returns: Temperature C, Pressure, humidity

from machine import I2C, Pin
from bme280_float import *
from utime import sleep
import math

i2c = I2C(1, sda=Pin(18), scl=Pin(19))
bme = BME280(i2c=i2c)


temp=bme.valuesRaw[0]
press=bme.valuesRaw[1]
humid=bme.valuesRaw[2]
altitude=bme.altitude
seaLevel=bme.sealevel
dewPoint=bme.dew_point


def getTempC():
    return round(temp)

def getTempF():
    fahrenheit=(temp*1.8)+32
    # tempF="{:.2f}F".format(fahrenheit)
    return round(fahrenheit)







print(f'C: {getTempC()}')
print(f'F: {getTempF()}')



print(bme.altitude)

print(bme.sealevel)
