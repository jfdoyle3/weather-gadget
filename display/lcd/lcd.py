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
sys.path.append("/resources")

from pico_i2c_lcd import I2cLcd
from ledCodes import *
from machine import I2C
from machine import Pin
import utime as time
 
 
i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

def lcdClear():
      lcd.clear()

def lcdText(message,x,y):
      lcd.move_to(x,y)
      lcd.putstr(message)
      
def lcdNotConnected():
      lcdClear()
      lcdText('WiFi',0,0)
      lcdText('Not Connected',0,1)
        
def lcdConnected():
      lcdClear()
      lcdText('WiFi',0,0)
      lcdText('Connected',0,1)
      
def lcdOff():
      lcd.clear()
      lcd.backlight_off()
      ledOff()
      lcd.display_off()
      
      
'''     
def wifiWait(timeDelay);        
      lcdText('Initalizing WiFi',0,0)
      lcdText('.',waitDisplay,1)
      time.sleep(timeDelay)
      waitDisplay -= 1
'''