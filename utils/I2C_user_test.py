# DC3231  - Real Time Clock:               I2C:1 SDA:14 SCL:15 
# SSD1306 - OLED 128x64 Display:           I2C:0 SDA:16 SCL:17
# BME280  - Temp &Humid &Barometer Sensor: I2C:1 SDA:18 SCL:19




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