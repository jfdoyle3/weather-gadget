# Error codes
# .5 time good default number

from machine import Pin
import time

LED=Pin("LED",Pin.OUT)

def errorCode(number,timing):
    for blink in range(0,number):
        time.sleep(timing)
        LED.on()
        time.sleep(timing) 
        LED.off()

def errorCodeVariBlink(number,onTime,offTime):
    for blink in range(0,number):
        time.sleep(.5)
        LED.on()
        time.sleep(.5) 
        LED.off()

def ledOn():
    LED.on()

def ledOff():
    LED.off()
    