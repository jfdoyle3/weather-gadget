from machine import Pin
import time

button2 = Pin(14, Pin.IN, Pin.PULL_UP)
button1= Pin(15, Pin.IN, Pin.PULL_UP)

def buttonPress():
    while True:
        if button1.value() == 0:
            print("Button1 is pressed")
            break
        else:
            print("Button1 is not pressed")
            
        if button2.value() == 0:
            print("Button2 is pressed")
            break
        else:
            print("Button2 is not pressed")
        time.sleep(0.1)   
