#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/5/8 21:18
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
#    def getHtmlText(url):
#     try:        # 网络连接有风险，异常处理很重要
#         r = requests.get(url,timeout=30)    # 查一下这个方法的使用
#         r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#          return "产生异常"
#   数据文件（1000个网址）：

# with open('url_data.txt','r',encoding='gbk') as f:
#     url_list=f.readlines()
#
# for i in url_list:
#     print(i.strip())
import requests
import threading
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import time
# index=0
def read_url():
    with open('url_data.txt', 'r', encoding='gbk') as f:
        try:
            while True:
                yield f.readline().strip()
        except:
            pass
mutex=Lock()


# ru=read_url()
#
# print(next(ru))
# print(next(ru))
# print(next(ru))
# print(next(ru))
# print(next(ru))

def judge_url(read_url,j):
    start_time=time.ctime()
    for i in range(20):
        try:
            mutex.acquire()
            s=next(read_url)
            mutex.release()
            if (requests.get(s,timeout=5).status_code == 200):
                print('%d.%d:可以访问此网址:%s'%(j,i,s))
            else:
                print('%d.%d:Error1:%s'%(j,i,s))
        except StopIteration:
            pass
        except:
            print('%d.%d:Error2:%s'%(j,i,s))

    print('用时：%s'%time.ctime()-start_time)


if __name__ == '__main__':
    ru = read_url()
    # for i in range(10):
    #     t=threading.Thread(target=judge_url,args=(ru,))
    #     t.start()
    with ThreadPoolExecutor(max_workers=10) as t:
        for i in range(50):
            t.submit(judge_url,ru,i)

