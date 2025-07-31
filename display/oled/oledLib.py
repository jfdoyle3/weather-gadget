

# System Imports
import os
import sys
import json

# Add a directory to sys.path
sys.path.append("/display/oled/driver")
sys.path.append("/network")
sys.path.append("/resources")

from machine import Pin, I2C
import ssd1306
import utime

# using default address 0x3C
i2c = I2C(sda=Pin(16), scl=Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


def oledText(text,x,y):
    oled.text(text, x, y, 1)
    oled.show()

def oledOff():
    oled.poweroff()
    oled.show()

def oledClear():
    oled.fill(0)
    oled.show()

def oledConnected():
      oledClear()
      oledText('WiFi',0,0)
      oledText('Connected',0,1)

def oledNotConnected():
      oledClear()
      oledText('WiFi',0,0)
      oledText('Not Connected',0,1)

