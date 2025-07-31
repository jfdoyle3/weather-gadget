# Display
#
# LCD 1602 Display connection
#  
#  LCD:           PICO:
#   GND             GND       PIN ANY
#   VCC             VBUS      PIN 40
#   SDA             I2C0 SDA  PIN 1
#   SCL             I2C0 SCL  PIN 2

# System Imports
import sys
import os

# Add a directory to sys.path
sys.path.append("/display/lcd/drivers")


from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
import utime as time
 
i2c = I2C(id=0,sda=Pin(16), scl=Pin(17),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

lcdText("Hi",0,0)
