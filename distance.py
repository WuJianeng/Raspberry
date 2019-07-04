#!/usr/bin/env python
# coding = utf-8
from RPi import GPIO
import time
import sys

Frequence = 5
Trig  = 38
Echo = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

def distance():
    try:
            GPIO.output(Trig,GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(Trig, GPIO.LOW)
	    

            while GPIO.input(Echo) == GPIO.LOW:
                Start_time = time.time()

            while GPIO.input(Echo) == GPIO.HIGH:
                Stop_time = time.time()
    except KeyboardInterrupt:
        print('User press CTRL+c, exit')
    distance = 34300 * (Stop_time - Start_time) / 2
    return distance

if __name__ == '__main__':
    try:
        while True:
            dis = distance()
            print('Distance: %.2f cm'%dis)
            time.sleep(1.0 / Frequence)
    except KeyboardInterrupt:
        print('User press CTRL+c, exit')
        sys.exit()
    finally:
	GPIO.cleanup()

