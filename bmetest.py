#
# Example. Using I2C at P9, P10
#

import os
import sys


# Add a directory to sys.path



from machine import I2C
from bme280_float import *
from utime import sleep

i2c = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19))
#i2c=I2C(0)
bme280 = BME280(i2c=i2c)
while True:
    print(bme280.values)
    sleep(1)

