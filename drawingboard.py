# Drawing Board
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

'''
# oled.rect(0,0,4,4,1)
oled.line(10, 0, 13,0, 1)
oled.line(10,10,13,10,1)
oled.line(10,0,9,2,1)
'''


def degreeSymb(x,y,text):
    oled.hline(x+10,y+0,3,1)
    oled.vline(x+9,y+1,3,1)
    oled.vline(x+13,y+1,3,1)
    oled.hline(x+10,y+4,3,1)
    oled.text(f'{text}',x+15,y+0,1)



degreeSymb(0,0,'F')

oled.show()

utime.sleep(5)
print("power off")
oled.poweroff()