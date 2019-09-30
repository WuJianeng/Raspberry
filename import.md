## import技巧

```python
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
```

对于自己创建的函数，可以将其添加到路径当中，然后再import

```python
from time import sleep

sleep(3)
```

使用该方式`import`后，可以简化函数的调用，不用写成`time.sleep(3)`

## 函数测试与调用

```python
if __name__ == '__main__':
	#GPIO.setmode(GPIO.BOARD)
	while True:
		test()
```

使用`if __name__ == '__main__'`方式：

​	**只有直接执行该模块时，该部分才会执行**

​	**如果只是以`import`方式调用该模块，该部分不会执行**

## 异常处理

```python
try:
except KeyboardInterrupt:
finally：
```

遇到键盘输入`CTRL+C`时退出。