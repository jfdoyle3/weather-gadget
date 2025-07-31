from machine import I2C, Pin
import utime

zeroSDA=[0,4,8,12,14,16,20]
zeroSCL=[1,5,9,13,15,17,21]


oneSDA=[2,6,10,14,18,26]
oneSCL=[3,7,11,15,19,27]

i2cZero = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
i2cOne = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
print('Scanning I2C bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C devices found")
else:
    print('I2C devices found:', len(devices))
    for device in devices:
        print("Decimal address: ", device, " | Hex address: ", hex(device))
utime.sleep(2)