# python爬虫

## 必备技能：

web前端、web后端

爬虫原理

基本模块

多线程、多进程、协程

mongdb

scrapy、分布式的爬虫部署

redis

网络编程

框架/工具	二次开发

整合运维平台

python	脚本语言	代替shell

web后端开发	运维平台

------



## 爬虫防被禁

Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0

User-Agent判断是否为浏览器请求

控制爬取的频率

------



## 正则表达式

```python
import urllib2

def getUrlList(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    
    res = urllib2.urlopen(req)
    html = res.read()	
    reg = r'data-title="(.*?)"'
    #.代表除了换行符和制表符以外的其他任何字符
    #*表示任意多个.
    #?表示最短的匹配结果
    #()建立索引，将正则结果取出
    urlList = re.findall(reg, html)
    #从html变量中进行reg格式的正则匹配，并将结果返回给urlList
```

------



## 下载静态资源	

```python
urllib.urlretrieve(url, 'mp4.1.mp4')
#url为链接地址， 'mp4/1.mp4'为存储的地址和文件名
```

------



#### 循环下载的文件命名

##### 1.累进命名

```python
n = 1
for url in urlList:
    urllib.urlretrieve(url, 'mp4/%d.mp4' %n)
    n += 1
```

##### 2.将url的命名部分作为文件名

**python分割函数split()，**

```python
for url in urlList:
    urllib.urlretrieve(url, 'mp4/%s.mp4'%url.split('/')[-1])
```

------



#### 注意事项

​	<u>在爬取网站信息时，应当使用考虑**异常**</u>

​	<u>爬取速度不应过快，否则会导致ip被封</u>**（使用time.sleep()函数）**

​	**<u>使用urllib.urlretrieve()函数时应当首先确定文件夹存在，否则会出现异常</u>**

​	<u>正则匹配应当注意空格等不明显的符号，可以采用**复制**的方式</u>



## 爬淘宝店铺

https://s.taobao.com/search?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%B9%A6%E7%B1%8D&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306

#### 第三方模块

requests	xlwt

```python
pip install requests, xlwt
```

#### 系统模块

re，json

#### 爬虫分类

-通用爬虫

​	搜索整个网络，用于搜索引擎

-聚焦爬虫

​	专注于某一个方面

-增量爬虫

​	每隔一段时间更新

-深层爬虫

​	需要登陆，需要提交数据

## 二.写爬虫的步骤

### 1.爬虫目的

​	-需要爬哪些网站

​	-爬哪些信息

​	-存在哪个地方

### 2.分析

###### 	-分析网页加载流程

​		1.直接加载

​		2.动态加载

​			-ajax

​			-js生成

​				-直接生成

​				-jsonp方式

​	(理论上，所有网站都可以爬，只是时间问题)

​		3.工具： 谷歌、Firfox

###### -分析待爬取页面结构

​		-re，正则表达式

​		-Beautifulsoup

###### 	-提取信息

### 3.实现

​	-根据分析的结果，代码实现

​	-requests，urllib

​	

## 三.写一个爬虫需要哪些知识

```python
https://s.taobao.com/search?q=study&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
```

```
https://s.taobao.com/search?q=go&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
```

