#!/usr/bin/env/ python3
# -*- encoding:utf-8 -*-
import os
import sqlite3  #管理数据库
import urllib.request  #下载文件
import threadpool  #线程池

path_database = os.path.abspath('database/link.db')  #获取 database/link.db(数据库) 的绝对路径
path_images = os.path.abspath('images')  #获取 images(图片存储文件夹) 的绝对路径

class Downloader:
    def __init__(self, urls, folder, threads=10):  # 初始化函数
        self.urls = urls  # 需要下载的网址list
        self.folder = folder  # 保存的文件目录
        self.threads = threads  # 并发线程数

    def run(self):
        pool = threadpool.ThreadPool(self.threads)  # 新建线程池
        requests = threadpool.makeRequests(self.downloader, self.urls)  # 新建请求
        [pool.putRequest(i) for i in requests]  # 将请求装入线程池
        pool.wait()  # 等待运行完成

    def downloader(self, url):
        pre = url.split('/')[-1]
        name = pre[:19] + ".jpg"  # 文件名
        print(self.folder + "/" + name)
        self.auto_down(url, self.folder + "/" + name)  # 下载

    def auto_down(self, url, filename):  # 处理出现网络不好的问题，重新下载
        try:
            urllib.request.urlretrieve(url, filename)
        except urllib.request.URLError as e:
            print(str(e) + 'Network Error,redoing download :' + url)
            self.auto_down(url, filename)  # 递归


if __name__ == "__main__":
    
    num_threads = 50  #下载器默认线程数为50

    urls = []
    conn = sqlite3.connect(path_database)  # 连接数据库
    cursor = conn.execute("SELECT LINK FROM LINK WHERE ID <= 4000")  # 选择总数
    for row in cursor:
        urls.append(row[0])
    pd = Downloader(urls, path_images, threads=num_threads)  # 新建下载器
    pd.run()