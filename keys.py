#duty()
import machine
import time
import math
# Define the frequencies of several musical notes in Hz
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523
# Create a PWM object representing pin 25 and assign it to the buzzer variable
buzzer = machine.PWM(machine.Pin(25))
key_C4 = machine.TouchPad(machine.Pin(4))
key_D4 = machine.TouchPad(machine.Pin(15))
key_E4 = machine.TouchPad(machine.Pin(13))
key_F4 = machine.TouchPad(machine.Pin(12))
key_G4 = machine.TouchPad(machine.Pin(14))
key_A4 = machine.TouchPad(machine.Pin(27))
key_B4 = machine.TouchPad(machine.Pin(33))
key_C5 = machine.TouchPad(machine.Pin(32))
# Define a tone function that takes as input a Pin object representing the
#buzzer, a frequency in Hz, and a duration in milliseconds
def average(keys):
    frequency = 0
    for key in keys:
        frequency += key
    frequency /= len(keys)
    print(f"frequency {frequency}")
    return frequency
    
def tone(buzzer, keys):
    frequency = average(keys)
    buzzer.freq(int(frequency)) # Set the frequency
    buzzer.duty(512) # Set the duty cycle
    time.sleep_ms(50)
    buzzer.duty(0)
    # Pause for the duration in milliseconds

#t4 = key_C4.read()
#t15 = key_D4.read()
#t13 = key_E4.read()
#t12 = key_F4.read()
#t14 = key_G4.read()
#t27 = key_A4.read()
#t33 = key_B4.read()
#t32 = key_C5.read()

while True:
    # Play a sequence of notes with different frequency inputs and durations
    t = 300
    keys = []
    if t > key_C4.read():
        keys.append(C4)
    if t > key_D4.read():
        keys.append(D4)
    if t > key_E4.read():
        keys.append(E4)
    if t > key_F4.read():
        keys.append(F4)
    if t > key_G4.read():
        keys.append(G4)
    if t > key_A4.read():
        keys.append(A4)
    if t > key_B4.read():
        keys.append(B4)
    if t > key_C5.read():
        keys.append(C5)
    if len(keys) > 0:
        tone(buzzer, keys)
    buzzer.duty(0) # Set the duty cycle to 0 to stop the tone
