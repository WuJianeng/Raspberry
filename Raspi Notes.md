# Raspi Notes

## GPIO控制

cat /proc/cpuinfo #查看CPU信息
vcgencmd measure_temp #see temparature of device

### **操作GPIO接口 shell 方式**

```shell
	sudo su //root 
	ls /sys/class/gpio
	cd /sys/class/gpio
	 echo 18 > export
	cd gpio18
	ls
	echo out > direction //方向输出
	echo 1 > value //output 1
	echo 0 > value //output 0
	echo 18 > unexport
```

### **操作GPIO接口，python方式**

sudo apt-get install python-rpi.gpio
code:
	

```python
#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	import RPI.GPIO as GPIO
	import time
	GPIO.setmode(GPIO.BOARD)//initialize
	#need to set up every channel which are 	
    #using as an input or output
	GPIO.setup(11,GPIO.OUT)
    while True:
	GPIO.output(11, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(11, GPIO.LOW)
	time.sleep(1)
```

### GPIO使用注意

```python
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
```

在每次GPIO引脚规范后，将GPIO警告关闭。

否则可能会导致调用多个GPIO模块后出现重复命名警告，导致程序无法运行。

## 树莓派SSH

将树莓派`Hostname`命名为`Raspi`。

这样在以后使用**SSH**方式时，只要是位于**同一个局域网**都可以以`Hostname`登录。

账号：**Raspi**   (在同一个局域网下登录)

## 输入法

### 安装fctix中文输入法

```sh
sudo apt install fcitx
sudo apt install fcitx-googlepinyin
```

安装完成后，**重启系统**

