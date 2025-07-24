# Sandbox
# Test Code

# System Imports
import os
import sys
import json

# Add a directory to sys.path
sys.path.append("/display/lcd")
sys.path.append("/network")
sys.path.append("/resources")



# Project Imports
from wifiConnect import *
from apiCalls import *
from ledCodes import *
from lcd import *
from button import *# System Imports
import os
import sys
import json

# Add a directory to sys.path
sys.path.append("/display/lcd")
sys.path.append("/network")
sys.path.append("/resources")



# Project Imports
from wifiConnect import *
from apiCalls import *
from ledCodes import *
from lcd import *
from button import *




from machine import Pin
import time

# Define GPIO pins
switch_pin = Pin(16, Pin.IN, Pin.PULL_DOWN) # Common pin connected to GP14, with pull-down resistor
output_pin_a = Pin(15, Pin.OUT) # Output pin connected to GP15
output_pin_b = Pin(13, Pin.OUT) # Output pin connected to GP13

while True:
    if switch_pin.value() == 1:
        print("Switch is on")
    else:
        print("Switch of off")
    time.sleep(0.1) # Delay for stability