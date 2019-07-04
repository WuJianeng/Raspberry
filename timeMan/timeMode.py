#!/usr/bin/env python
# -- coding:utf-8 --
import time

def timeNow():
	nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	return nowTime

