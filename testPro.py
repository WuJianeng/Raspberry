#!/usr/bin/env python
# -- coding:utf-8 --
#import RPi.GPIO as GPIO
#import time
#import commands
#import lightMode
import sys
import time
sys.path.append(r"/home/py/lightMan")
sys.path.append(r"/home/py/tempMan")
sys.path.append(r"/home/py/mailMan")
import lightMode
import tempMode
import sendMail

temp_Threshold = 65
lightMode.close()
while True:
	cpu_temp = tempMode.cpu_temp()
	tempContent = str(cpu_temp)+ "°C"
	if cpu_temp > temp_Threshold:
		try:
			mailContent = open("/home/py/mailMan/config.txt","w")
			mailContent.write(tempContent)
			mailContent.close()
		except IOError:
			print ("Error: 没找到config.txt文件或写入失败%n")
		else:
			sendMail.sendMail()


		print("Caution!\nCpu temparature: " + tempContent)
		lightMode.tempWarn()
		lightMode.close()
		time.sleep(10)
	else: 
		#print("Normal temparature: " + str(cpu_temp))
		#time.sleep(20)
		lightMode.normal()
GPIO.cleanup()
