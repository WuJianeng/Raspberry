#!/usr/bin/env python
# -- coding:utf-8 --
import RPi.GPIO as GPIO
import time
PIN_ON = 40
GPIO.setmode(GPIO.BOARD)
#need to set up every channel which are using as an input or an output;
GPIO.setup(PIN_ON, GPIO.OUT)

STOP_TIME = 0.2
def sound():
	GPIO.output(PIN_ON, GPIO.HIGH)
	time.sleep(STOP_TIME)
	GPIO.output(PIN_ON, GPIO.LOW)
	time.sleep(STOP_TIME)

if __name__ == '__main__':
	for i in range(10):
		sound()
