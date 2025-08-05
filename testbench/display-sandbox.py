# Display Sandbox

from machine import Pin, I2C
import ssd1306
import utime
import framebuf

# using default address 0x3C
i2c = I2C(sda=Pin(16), scl=Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text('Boo!!',0,0)
oled.show()

utime.sleep(5)
print("power off")
oled.poweroff()
