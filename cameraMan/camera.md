### Raspi照相功能

> https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

#### 1.新建文件

​	新建一个`camera.py`文件

#### 2.Import包

```python
from picamera import PiCamera
from time import sleep
```

#### 3.预览模式（`preview`）

##### 3.1预览模式基本函数

注意：**使用`preview`函数只能够在Raspi的window界面显示，`SSH`方式无法看到。

```python
camera = PiCamera()

camera.start_preview()
sleep(10)
camera.stop_preview()
```

##### 3.2旋转画面(`rotation`)

```python
camera.rotation = 180
camera.start_preview()
sleep(10)
camera.stop_preview()
```

##### 3.3透明度(`transparency`)

```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()
```

***`alpha`***取值范围：0~255

#### 4.拍照(still pictures)

```python
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
```

*****在拍照之前（capture）应当调用preview()函数至少2s，使得相机可以调整亮度水平

#### 5.录像（Recording video)

```python
camera.start_preview()
camera.start_recording('/home/Desktop/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
```

*****观看录像时，需要使用`omplayer`

**A.**打开终端`terminal`

**B.**输入命令

```shell
omplayer video.h264
```

**C.**注意，由于omplayer帧率较高，导致视频播放速度可能比较快

#### 6.相机设置

##### 6.1分辨率(`resolution`和帧率（`frame rate`）

```python
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
```

照相最大分辨率：`2592 x 1944`

录像最大分辨率：`1920 x 1080`

最小分辨率：`64 x 64`

##### 6.2注释文本

###### 6.2.1基本实现

```python
camera.start_preview()
camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()
```

###### 6.2.2设置文本大小

```python
camera.annotate_text_size = 50
```

6.2.3设置文本颜色

首先需要导入颜色（**color**）包

```python
from picamera import PiCamera, Color
```

然后修改参数

```python
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
```



##### 6.3亮度

```python
camera.start_preview()
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()
```

亮度范围：0-100，默认50

##### 6.4对比度

```python
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
```

#### 7.相机模式

##### 7.1模式A

```python
camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()
```

<u>**存在以下几种模式**：</u>

`none`, `negative`, `solarize`, `sketch`, `denoise`, `emboss`, `oilpaint`, `hatch`, `gpen`, `pastel`, `watercolor`, `film`, `blur`, `saturation`, `colorswap`, `washedout`, `posterise`, `colorpoint`, `colorbalance`, `cartoon`, `deinterlace1`, and `deinterlace2` 

默认为`none`

##### 7.2模式B

You can use `camera.awb_mode` to set the auto white balance to a preset mode to apply a particular effect. The options are: `off`, `auto`, `sunlight`, `cloudy`, `shade`, `tungsten`, `fluorescent`, `incandescent`, `flash`, and `horizon`. The default is `auto`. Pick one and try it out:

```python
camera.start_preview()
camera.awb_mode = 'sunlight'
sleep(5)
camera.capture('/home/pi/Desktop/sunlight.jpg')
camera.stop_preview()
```

##### 7.3模式C

You can use `camera.exposure_mode` to set the exposure to a preset mode to apply a particular effect. The options are: `off`, `auto`, `night`, `nightpreview`, `backlight`, `spotlight`, `sports`, `snow`, `beach`, `verylong`, `fixedfps`, `antishake`, and `fireworks`. The default is `auto`. Pick one and try it out:

```python
camera.start_preview()
camera.exposure_mode = 'beach'
sleep(5)
camera.capture('/home/pi/Desktop/beach.jpg')
camera.stop_preview()
```

