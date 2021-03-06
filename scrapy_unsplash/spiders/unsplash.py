# -*- coding: utf-8 -*-
import os
import json
import sqlite3
import threading
import scrapy
from scrapy.spiders import CrawlSpider

path_database = os.path.abspath('database/link.db')  #获取 database/link.db 的绝对路径

class UnsplashSpider(CrawlSpider):
    name = "unsplash"

    def start_requests(self):  # Scrapy启动时调用该函数
        createDB()  # 创建数据库
        pre = "https://api.unsplash.com/photos/?client_id="  #
        key = "fa60305aa82e74134cabc7093ef54c8e2c370c47e73152f72371c828daedfcd7"
        aft = "&page="
        lst = "&per_page=30"
        
        begin = 1  # 设定开始页面
        end = 3    # 设定结束页面
        
        conn = sqlite3.connect(path_database)  # 连接数据库
        semaphore = threading.Semaphore(1)  # 引入线程信号量，避免写入数据库时死锁
        for i in range(begin, begin + end):
            # 下面的lambda函数实现了传入信号量以及数据库连接到回调函数中
            yield scrapy.Request(url=pre + key + aft + str(i) + lst,
                                 callback=lambda response, conn=conn, semaphore=semaphore: self.toDB(response, conn,
                                                                                                     semaphore))

    def parse(self, response):  # 基本函数，不实现会报Exception
        pass

    def toDB(self, response, conn, semaphore):  # 存储到数据库中
        js = json.loads(response.body_as_unicode())  # 读取响应body，并转化成可读取的json
        for j in js:
            link = j["urls"]["raw"]
            sql = "INSERT INTO LINK(LINK) VALUES ('%s');" % link  # 将link插入数据库
            conn.execute(sql)
        semaphore.acquire()  # P操作
        conn.commit()  # 写入数据库，此时数据库文件独占
        semaphore.release()  # V操作


def createDB():  # 创建数据库
    conn = sqlite3.connect(path_database)  # Sqlite是一个轻量数据库，不占端口，够用
    conn.execute("DROP TABLE IF EXISTS LINK;")  # 重新运行删掉数据库
    conn.execute("CREATE TABLE LINK ("  # 创建属性ID：主键自增；属性LINK：存放图片链接
                 "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "LINK VARCHAR(255));")
