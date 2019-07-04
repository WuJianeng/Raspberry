#!/usr/bin/env python
# coding = utf-8
from RPi import GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Bee = 40
GPIO.setup(Bee, GPIO.OUT)

def Ring():
    try:
            GPIO.output(Bee,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(Bee, GPIO.LOW)
    except KeyboardInterrupt:
        pass
    finally:
        pass

if __name__ == '__main__':
    try:
        while True:
            Ring()
            time.sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
	print('User press CTRL+c, exit')
        sys.exit()

