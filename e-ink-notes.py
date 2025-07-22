# e-ink test

# System Imports
import os
import sys

# Add a directory to sys.path
sys.path.append("/display/e-ink")
sys.path.append("/network")
sys.path.append("/resources")


from einkdriver import *

# Initalize Display
epd = EPD_2in13_V4_Landscape()
# Clear Display
epd.Clear()
# Fill Screen 00 = Clear/White   FF = Black
epd.fill(0xFF)
epd.text("Boo!",20,20,0x00)
epd.display(epd.buffer)
epd.delay_ms(2000)


