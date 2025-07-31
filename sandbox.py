# Sandbox
# Testbench idea

# System Imports
import os
import sys

sys.path.append("/bme280")



import machine
import bme280_float as bme280

i2c = machine.I2C(0, sda=machine.Pin(21), scl=machine.Pin(22))
bme = bme280.BME280(i2c=i2c)

print(bme.values)