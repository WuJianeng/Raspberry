#!/usr/bin/env python
# coding = 'utf-8'
from RPi import GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
LED = 36
SOUND = 38
SWITCH = 40

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SOUND, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN)

try:
    while True:
        if GPIO.input(SWITCH):
            GPIO.output(LED, GPIO.HIGH)
            GPIO.output(SOUND, GPIO.HIGH)
	    time.sleep(0.2)
            GPIO.output(LED, GPIO.LOW)
            GPIO.output(SOUND, GPIO.LOW)
except KeyboardInterrupt:
    print('User press CTRL+c, exit')
finally:
    GPIO.cleanup()


