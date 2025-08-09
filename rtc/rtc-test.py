# RTC Test
#
# DS3231 RTC
## System Imports
import os
import sys
import time


# Add a directory to sys.path
# sys.path.append("/display")


from machine import Pin, I2C
from ds3231 import DS3231
import urtc
import time

i2c = I2C(1,sda=Pin(14), scl=Pin(15))

rtc = urtc.DS3231(i2c)

initial_time_tuple = time.localtime()
initial_time_seconds = time.mktime(initial_time_tuple)
initial_time = urtc.seconds2tuple(initial_time_seconds)

# Convert to tuple compatible with the library
initial_time = urtc.seconds2tuple(initial_time_seconds)

# Sync the RTC
rtc.datetime(initial_time)


current_datetime = rtc.datetime()
print('Current date and time:')
print('Year:', current_datetime.year)
print('Month:', current_datetime.month)
print('Day:', current_datetime.day)
print('Hour:', current_datetime.hour)
print('Minute:', current_datetime.minute)
print('Second:', current_datetime.second)
print('Day of the Week:', days_of_week[current_datetime.weekday])




