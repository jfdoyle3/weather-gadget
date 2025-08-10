from machine import I2C, Pin
import utime

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
print('Scanning I2C bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found")
else:
    print('I2C devices found:', len(devices))
    for device in devices:
        print("Decimal address: ", device, " | Hex address: ", hex(device))
utime.sleep(2)