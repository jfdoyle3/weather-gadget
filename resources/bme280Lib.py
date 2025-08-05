# BME280 Library
#
# bme.values returns: Temperature C, Pressure, humidity

from machine import I2C, Pin
from bme280_float import *
from utime import sleep

i2c = I2C(1, sda=Pin(18), scl=Pin(19))
bme = BME280(i2c=i2c)

# def getTemp():
temp=bme.valuesRaw[0]
press=bme.valuesRaw[1]
humid=bme.valuesRaw[2]
altitude=bme.altitude
seaLevel=bme.sealevel
dewPoint=bme.dew_point

'''
def getTempC():
    temp=bme.values[0]
    return temp

def getTempF():
    tempLen=len(temp)
    celTemp=temp[:-1]
    celTempFloat=float(celTemp)
    fahrenheit=(celTempFloat*1.8)+32
    tempF="{:.2f}F".format(fahrenheit)
    return tempF
'''


temp=bme.values[0]
tempRaw=bme.valuesRaw[0]



print(temp)

print(f'Raw: {tempRaw}')

print(bme.altitude)

print(bme.sealevel)
