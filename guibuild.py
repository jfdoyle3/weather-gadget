# Display Sandbox
# resolution: 128x64
# characters: 16x5 standard text
#

from machine import Pin, I2C
import ssd1306
import utime
import framebuf

# using default address 0x3C
i2c = I2C(0,sda=Pin(16), scl=Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Header
def guiHeader():
    
        # WiFi Antenna
        oled.hline(0,0,9,1)
        oled.vline(4,0,8,1)
        oled.line(8,0,4,4,1)
        oled.line(0,0,4,4,1)

        # WIFI Strength
        oled.text('100%',15,0,1)
        # Time
        oled.text('2:09pm',80,0,1)
        # Header End

def guiGraphics():
        # Graphic
        oled.hline(0,9,128,1)
        # oled.vline(60,9,64,1)
        oled.hline(0,50,128,1)

def guiInfo(data1,data2):
        # Info
        oled.text('indoor   api',0,17,1)
        oled.text("23" + chr(176),0,33,1)
    
def guiFooter(ip):
        # Footer
        oled.text(' 192.168.1.207',0,56,1)
'''
# Display to Screen
oled.show()

utime.sleep(5)
print("power off")
oled.poweroff()
'''

'''
oled.text('ABCDEFGHIJKLMNOP',0,0,1)
oled.text('abcdefghijklmnop',0,7,1)
oled.text('1234567890!@#$%^',0,0,1)
oled.text('ABCDEFGHIJKLMNOP',0,0,1)
oled.text('abcdefghijklmnop',0,0,1)
oled.text('1234567890!@#$%^',0,0,1)
oled.text('ABCDEFGHIJKLMNOP',0,0,1)
oled.text('abcdefghijklmnop',0,0,1)
oled.text('1234567890!@#$%^',0,0,1)

oled.show()
'''
