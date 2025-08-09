from machine import Pin, SPI

# Define the SPI pins
sck = Pin(18)
mosi = Pin(19)
miso = Pin(20)

# Create a SPI object
spi = SPI(1, baudrate=10000000, sck=sck, mosi=mosi, miso=miso)

# Read data from the SPI bus
data = spi.read(10)  # Read 10 bytes   