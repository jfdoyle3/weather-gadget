# DC3231  - Real Time Clock:               I2C:1 SDA:14 SCL:15 
# SSD1306 - OLED 128x64 Display:           I2C:0 SDA:16 SCL:17
# BME280  - Temp &Humid &Barometer Sensor: I2C:1 SDA:18 SCL:19

# System Imports
import os
import sys
import json

# Add a directory to sys.path
sys.path.append("/display/oled")
sys.path.append("/network")
sys.path.append("/resources")
sys.path.append("/bme280")

from machine import Pin, I2C
import ssd1306
import bme280_float as bme280
import utime

# using default address 0x3C
i2c = I2C(sda=Pin(16), scl=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

i2cBME = machine.I2C(1, sda=machine.Pin(18), scl=machine.Pin(19), freq=40000)

display.text('Boo!!', 45, 32, 1)
utime.sleep(2)
display.show()
utime.sleep(2)
display.poweroff()
display.show()




# import bme280
print("Start")
# works w/o freq. May be needed if not working with LCD.


bme = bme280.BME280(i2c=i2cBME)


temp=bme.values[0]



print(temp)

print(bme.altitude)

print(bme.sealevel)
#val = i2c.readfrom_mem(0X76,0XD0, 1)[0]
#print(val)


print("End Of Line")
