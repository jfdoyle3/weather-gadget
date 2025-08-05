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
temp=-5
x=0
y=50
tempX,tempY=x+0, y+0



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
oled.text('F',symX+17,symY+0,1)


# Large Degree Symbol
# oled.text('999',0,0,1)
# oled.hline(10,0,3,1)
# oled.vline(9,0,3,1)
# oled.vline(x+13,y+1,3,1)
# oled.hline(x+10,y+4,3,1)
# oled.text('F',x+15,y+0,1)

oled.show()

utime.sleep(5)
print("power off")
oled.poweroff()
