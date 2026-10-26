from machine import Pin, PWM
import time

#Assign LED junctions (colors) to their respective Pin on the PLC
RED_PIN = 26
GREEN_PIN = 27
BLUE_PIN = 25

#create alias variables for easier program writing
red = PWM(Pin(RED_PIN))
green = PWM(Pin(GREEN_PIN))
blue = PWM(Pin(BLUE_PIN))

#define Pin BAUD
red.freq(1000)
blue.freq(1000)
green.freq(1000)

def set_color(r,g,b):
    red.duty(r)
    blue.duty(b)
    green.duty(g)

while True:

    set_color(1023, 0, 0) #red
    time.sleep(1)
    
    set_color(0, 1023, 0) #green
    time.sleep(1)
    
    set_color(0, 0, 1023) #blue
    time.sleep(1)
    
    set_color(0, 1023, 1023) #weird purple
    time.sleep(1)