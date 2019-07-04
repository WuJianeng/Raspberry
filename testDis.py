#!/usr/bin/env python
# coding = utf-8

from RPi import GPIO
import time
import sys
import Ring
import distance

LIMIT = 50.0
def test():
	try:
		dis = distance.distance()
		print('Distance: %.2f cm'%dis)
		if dis < LIMIT:
			Ring.Ring()
			time.sleep(0.2)
	except KeyboardInterrupt:
		print('User press CTRL+C, exit')
		sys.exit()

if __name__ == '__main__':
	#GPIO.setmode(GPIO.BOARD)
	while True:
		test()
