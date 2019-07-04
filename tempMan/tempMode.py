#!/usr/bin/env python
# -- coding:utf-8 --
import commands

def cpu_temp():
	file = open("/sys/class/thermal/thermal_zone0/temp")
	cpu_temp = file.read()
	file.close()
	return float(cpu_temp) / 1000
	#uncomment the next line if you want tot get the temparature in Fahrenheie
	#return float(cpu_temp * 1.8) + 32
