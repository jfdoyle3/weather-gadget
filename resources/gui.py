# Display Sandbox
# resolution: 128x64
# characters: 16x5 standard text
#
# https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html

from machine import Pin, I2C
import ssd1306
import utime
import framebuf

# using default address 0x3C
i2c = I2C(0,sda=Pin(16), scl=Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Header
def guiHeader(rssi):
        # WiFi Antenna
        oled.hline(0,0,9,1)
        oled.vline(4,0,8,1)
        oled.line(8,0,4,4,1)
        oled.line(0,0,4,4,1)

        # WIFI Strength
        oled.text(f'{rssi}%',15,0,1)
        # Time
        oled.text('2:09pm',80,0,1)
        # Header End

def guiGraphics():
        # Graphic
        oled.hline(0,9,128,1)
        # oled.vline(60,9,64,1)
        oled.hline(0,50,128,1)
        

def guiInfo(x,y,temp,unit):
        # Info
        oled.text('indoor',0,17,1)
        # oled.text('indoor   api',0,17,1)
        # oled.text(f'{indoor}',0,33,1)
        degreeSymb(x,y,temp,unit)
        

        
def guiFooter(ip):
        # Footer
        oled.text(f"{ip}",0,56,1)

# Display
def showGUI():
    oled.show()
        
def displayOff():
    oled.poweroff()

def displayDelayOff(time):
    utime.sleep(time)
    oled.powerOff()

def degreeSymb(x,y,temp,unit):
    tempX,tempY=x+0, y+0
    
    # Spacing between temp and symbol
    # negative is a 'Digit' when counting digits
    #
    # One Digit
    # symX, symY=x-1, y+0
    # two Digits
    # symX, symY=x+8, y+0
    # three Digits
    # symX, symY=x+16, y+0
    # Four Digits
    # symX, symY=x+23, y+0
    
    if temp>=-99 and temp<=999:
        symX, symY=x+16, y+0

    if temp>=-9 and temp<=99:
        symX, symY=x+8, y+0

    if temp>=0 and temp<=9:
        symX, symY=x-1, y+0
   
    # small Degree Symbol
    oled.text(f'{temp}',tempX,tempY,1)
    oled.hline(symX+10,symY+0,2,1)
    oled.vline(symX+9,symY+1,2,1)
    oled.vline(symX+12,symY+1,2,1)
    oled.hline(symX+10,symY+3,2,1)
    oled.text(f'{unit}',symX+15,symY+0,1)

    
# Mock Display
def guiMock():
        oled.hline(0,0,7,1)
        oled.vline(3,0,8,1)
        oled.line(0,0,3,3,1)
        oled.line(7,0,3,3,1)
        oled.text(f'{rssi}%',15,0,1)
        oled.text('2:09pm',80,0,1)
        oled.hline(0,9,128,1)
        oled.vline(60,9,42,1)
        oled.text('indoor    outdoor',0,17,1)
        oled.text('100F     100F',0,33,1)
        oled.hline(0,50,128,1)
        oled.text(str(ip),0,56,1)
        oled.show()

