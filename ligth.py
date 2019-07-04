#!/usr/bin/env python
# coding = 'utf-8'
import time
import RPi.GPIO as GPIO

LED = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
  
p = GPIO.PWM(LED, 50)
p.start(0)
try:
    while True:
        for dc in range(40, 100, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, 40, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
