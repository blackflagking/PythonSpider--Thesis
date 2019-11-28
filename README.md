基于Scrapy实现Thesis跨境物流论文爬虫
===


![项目部分截图](./Object--Picture/100ec.jpg)  

### 爬取的网站：http://www.100ec.cn/

# 项目简介
这是关于跨境物流方面的一个爬虫实例  
主要用来爬去关于跨境物流等相关信息   
以供朋友论文作为参考资料！！！
爬取比较简单，并没有遇到ajax操作便不再此做过多介绍。。。

如果有问题，请提issue

在参考本项目之前，也可先阅读[Scapy文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)，熟悉了解Scrapy!
# 交流分享

- 作者微信  
![作者微信](./Object--Picture/vxhead.jpg)


# 问题集锦

    Q:为什么爬取下来的是乱码？
    A:爬完的数据需要用Excel进行转码，字符集由于当时时间紧迫就没有转换。（推荐pull者可使用Word转码功能便可显示中文）

# 安装scrapy
此项目使用的是Windows操作系统，仅以此为例
MAC操作系统可自行百度，过程大同小异！

```
   pip install scrapy
```


# 使用

### 初始化 API

爬取保存到本地，可在pipelines.py配置自己的保存路径

```
    def __init__(self):
        filename = "C:\\Users\\Administrator\\Desktop\\Thesis\\跨境物流论文.txt"
        filename = unicode(filename, "utf8")
        self.file = codecs.open(filename, 'a', encoding='utf-8')
```


### 启动Scrapy爬取热点数据

```
   scrapy crawl lw.py
```

# 微信公众号

咖啡是每个程序员的最爱！  
有了咖啡的陪伴，一个人才能度过coding之夜,
有了咖啡的陪伴，一个人的夜晚才算得上是完美。

本人，业余爱好咖啡，  
并经营一些咖啡相关商品，  
如果您也有喝咖啡的习惯，  
赶快来关注我的公众号吧，  
---加我有优惠哦---



![公众号](./Object--Picture/vxplatform.png) 




# TODO  

- [x] 爬取有关此网站的所有与跨境物流有关的论文
