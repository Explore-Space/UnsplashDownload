# UnsplashDownload

[![Build Status](https://travis-ci.org/Explore-Space/UnsplashDownload.svg?branch=master)](https://travis-ci.org/Explore-Space/UnsplashDownload)

- [English version](https://github.com/Explore-Space/UnsplashDownload/blob/master/README.md)

## 0x00 简介

**[Unsplash](https://unsplash.com/)**

>Make something awesome

[![Unsplash](https://images.unsplash.com/moment-1544716590524-4fc5a168786e?dpr=3&auto=format&fit=crop&w=600&q=60 "Unsplash")](https://unsplash.com/)

> 美丽，免费的图像和照片，您可以下载和用于任何项目，比任何免版权或素材图片都好。

## 0x01 目的

获取取Unsplah指定页面所有图片的链接，并下载到本地

## 0x02 依赖

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

- [scrapy](https://scrapy.org/) - 一个开放源码的协作框架，用于从网站中提取您需要的数据
- [threadpool](https://pypi.org/project/threadpool/) - 易于使用面向对象的线程池框架

## 0x03 运行
1.克隆该存储库并进入文件根目录

```
git clone https://github.com/Explore-Space/UnsplashDownload.git
```

```
cd UnsplashDownload/
```

2.安装依赖

```
pip3 install -r requirements.txt
```

3.运行scrapy获取图片链接并存储在数据库中

```
scrapy crawl unsplash
```

运行后生成数据库文件保存于 [***database***](https://github.com/Explore-Space/UnsplashDownload/tree/master/database) 中

4.运行多线程下载器

```
python3 download.py
```

运行后下载图片保存于 [***images***](https://github.com/Explore-Space/UnsplashDownload/tree/master/images) 中

## 0x04 说明

1.scrapy默认获取Unsplash前三页图片的链接，如有需要请修改 [*scrapy_unsplash/spiders/unsplash.py*](https://github.com/Explore-Space/UnsplashDownload/blob/master/scrapy_unsplash/spiders/unsplash.py) 中line 21与line 22的值

2.多线程下载器默认运行50个线程，如有需要请修改[*download.py*](https://github.com/Explore-Space/UnsplashDownload/blob/master/download.py) 中line 39的值

## 0x05 测试

测试环境：

- 操作系统： Ubuntu 18.04
- Python版本： 3.6.8
- Scrapy版本： 1.6
- 最后测试时间 ： 2019-07-08

## 0x06 致谢

项目参考：

- [UnsplashDownloader](https://github.com/hating/UnsplashDownloader) by  [hating](https://github.com/hating)
- [Scrapy-Unsplash](https://github.com/00wendi00/Scrapy-Unsplash) by [00wendi00](https://github.com/00wendi00)
