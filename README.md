# UnsplashDownload

[![Build Status](https://travis-ci.org/Explore-Space/UnsplashDownload.svg?branch=master)](https://travis-ci.org/Explore-Space/UnsplashDownload)

## 0x00 简介

**[Unsplash](https://unsplash.com/)**

>Make something awesome

[![Unsplash](https://images.unsplash.com/moment-1544716590524-4fc5a168786e?dpr=3&auto=format&fit=crop&w=600&q=60 "Unsplash")](https://unsplash.com/)

> Beautiful, free images and photos that you can download and use for any project. Better than any royalty free or stock photos.

## 0x01 目的

爬取Unsplah指定页面所有图片的链接，并下载到本地

## 0x02 依赖

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

- [scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites
- [threadpool](https://pypi.org/project/threadpool/) - Easy to use object-oriented thread pool framework

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

3.运行scrapy抓取图片链接并存储在数据库中

```
scrapy crawl unsplash
```

运行后生成数据库文件保存于 [***database***](https://github.com/Explore-Space/UnsplashDownload/tree/master/database) 中

4.运行多线程下载器

```python3 download.py```

运行后下载图片保存于 [***images***](https://github.com/Explore-Space/UnsplashDownload/tree/master/images) 中

## 0x04 说明

1.scrapy默认抓取Unsplash前三页图片的链接，如有需要请修改 [*scrapy_unsplash/spiders/unsplash.py*](https://github.com/Explore-Space/UnsplashDownload/blob/master/scrapy_unsplash/spiders/unsplash.py) 中line 21与line 22的值

2.多线程下载器默认运行50个线程，如有需要请修改[*download.py*](https://github.com/Explore-Space/UnsplashDownload/blob/master/download.py) 中line 39的值

## 0x05 测试

测试环境：

- 操作系统： Ubuntu 18.04
- Python版本： 3.6.8
- Scrapy版本： 1.6
- 测试时间 ： 2019-06-28

## 0x06 感谢

项目参考：

- [UnsplashDownloader](https://github.com/hating/UnsplashDownloader) by  [hating](https://github.com/hating)
- [Scrapy-Unsplash](https://github.com/00wendi00/Scrapy-Unsplash) by [00wendi00](https://github.com/00wendi00)


[![forthebadge](https://forthebadge.com/images/badges/powered-by-jeffs-keyboard.svg)](https://forthebadge.com)
