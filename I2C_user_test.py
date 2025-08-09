import machine


port=int(input('port number (0,1): '))

sdaPIN=int(input('SDA Pin number: '))
sclPIN=int(input('SCL Pin number: '))

i2c=machine.I2C(port,sda=sdaPIN, scl=sclPIN, freq=400000)
devices = i2c.scan()
if len(devices) == 0:
 print("No i2c device !")
else:
 print('i2c devices found:',len(devices))
for device in devices:
 print("Hexa address: ",hex(device))