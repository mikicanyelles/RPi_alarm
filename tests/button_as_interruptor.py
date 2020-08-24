#! /usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

# GPIO SETUP

LED = 26
BUTTON = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

init = 0
previous_status = 0

def button(BUTTON, init, previous_status):
    
    actual_status = GPIO.input(BUTTON)
    if actual_status and previous_status == 0:
        init = 1 - init
        sleep(0.1) # For avoiding problems with the button

    previous_status = actual_status
    
    return init, previous_status


def led(LED, init):
    if init == 1:
        GPIO.output(LED, True)
    else :
        GPIO.output(LED, False)



try :

    while True:
        init, previous_status = button(BUTTON, init, previous_status)
        led(LED, init)

except KeyboardInterrupt:
    GPIO.cleanup()
