# System Imports
import os
import sys


# Add a directory to sys.path
# sys.path.append("/display")


from machine import Pin, I2C
import DS3231

i2c = I2C(1,sda=Pin(14), scl=Pin(15))
ds = DS3231(i2c)

