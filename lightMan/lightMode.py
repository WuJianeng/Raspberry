#!/usr/bin/env python
# -- coding:utf-8 --
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#need to set up every channel which are using as an input or an output;
GPIO.setup(12,GPIO.OUT)

def close():
	GPIO.output(12,GPIO.LOW)
	

def sos():
        for i in range(3):
                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.3)
        for j in range(3):
                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.8)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.8)
        for k in range(3):
                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.3)
        GPIO.output(12,GPIO.LOW)
	

def ipChange():
        for i in range(10):
                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.2)
	GPIO.output(12,GPIO.LOW)
	

def tempWarn():
        for i in range(30):
                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.08)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.08)
	GPIO.output(12,GPIO.LOW)
	

def normal():
	print('output...')
	GPIO.output(12,GPIO.HIGH)
	time.sleep(10)
	print('Close...')
	GPIO.output(12,GPIO.LOW)
	time.sleep(10)
