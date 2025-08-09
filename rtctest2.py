# Import necessary modules
from machine import I2C, Pin
from ds3231_port import DS3231
import utime


# Initialize the I2C interface with the specified pins
i2c = I2C(1, scl=Pin(15), sda=Pin(14))
ds3231 = DS3231(i2c)

print('Initial values')
print('DS3231 time:', ds3231.get_time())
print('RTC time:   ', utime.localtime())

print('Setting DS3231 from RTC')
ds3231.save_time()  # Set DS3231 from RTC
print('DS3231 time:', ds3231.get_time())
print('RTC time:   ', utime.localtime())
