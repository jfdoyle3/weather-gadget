# Display Sandbox


# System Imports
import os
import sys


# Add a directory to sys.path
sys.path.append("/display/oled")
sys.path.append("/network")
sys.path.append("/resources")

from oledlib import *

oledText('boo!',45,34)