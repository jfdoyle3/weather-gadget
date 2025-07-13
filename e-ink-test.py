# e-ink test

# System Imports
import os
import sys

# Add a directory to sys.path
sys.path.append("/display/e-ink")
sys.path.append("/network")
sys.path.append("/resources")


from einkdriver import *



epd = EPD_2in13_V4_Landscape()
epd.Clear()

epd.fill(0x00)
epd.text("Waveshare", 20, 100, 0xff)
epd.display(epd.buffer)
epd.delay_ms(2000)

