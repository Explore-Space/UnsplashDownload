# UnsplashDownload

[![Build Status](https://travis-ci.org/Explore-Space/UnsplashDownload.svg?branch=master)](https://travis-ci.org/Explore-Space/UnsplashDownload)

- [中文版](https://github.com/Explore-Space/UnsplashDownload/blob/master/README_CN.md)

## 0x00 Introduction

**[Unsplash](https://unsplash.com/)**

>Make something awesome

[![Unsplash](https://images.unsplash.com/moment-1544716590524-4fc5a168786e?dpr=3&auto=format&fit=crop&w=600&q=60 "Unsplash")](https://unsplash.com/)

> Beautiful, free images and photos that you can download and use for any project. Better than any royalty free or stock photos.

## 0x01 Target

Get links to all images on the Unsplah specified page and download them locally

## 0x02 Requirements

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

- [scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites
- [threadpool](https://pypi.org/project/threadpool/) - Easy to use object-oriented thread pool framework

## 0x03 Run
1.Clone the repository and enter the file root directory

```
git clone https://github.com/Explore-Space/UnsplashDownload.git
```

```
cd UnsplashDownload/
```

2.Install requirements

```
pip3 install -r requirements.txt
```

3.Run scrapy to get picture links and store them in the database

```
scrapy crawl unsplash
```

The database file generated after running is saved in [***database***](https://github.com/Explore-Space/UnsplashDownload/tree/master/database) 

4.Run multithreaded Downloader

```
python3 download.py
```

Pictures downloaded after running are saved in [***images***](https://github.com/Explore-Space/UnsplashDownload/tree/master/images) 

## 0x04 Note

1.Scrapy gets links to the first three pages of Unsplash images by default. If needed， modify the value of lines 21 and 22 of [*scrapy_unsplash/spiders/unsplash.py*](https://github.com/Explore-Space/UnsplashDownload/blob/master/scrapy_unsplash/spiders/unsplash.py) 

2.Multithreaded downloader runs 50 threads by default. If needed， modify the value of line 39 of [*download.py*](https://github.com/Explore-Space/UnsplashDownload/blob/master/download.py)

## 0x05 Test

Test Environment：

- OS： Ubuntu 18.04
- Python version： 3.6.8
- Scrapy version： 1.6
- Last test time ： 2019-06-28

## 0x06 Acknowledgements

Project reference：

- [UnsplashDownloader](https://github.com/hating/UnsplashDownloader) by  [hating](https://github.com/hating)
- [Scrapy-Unsplash](https://github.com/00wendi00/Scrapy-Unsplash) by [00wendi00](https://github.com/00wendi00)

