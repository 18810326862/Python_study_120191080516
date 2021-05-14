#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/5/8 20:37
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；
import random
import threading
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
mutex=Lock()
def func():
    for i in range(20):
        mutex.acquire()
        print(random.randint(0,100))
        mutex.release()



# t1=threading.Thread(target=func)
# t2=threading.Thread(target=func)
# t3=threading.Thread(target=func)
# t4=threading.Thread(target=func)
# t5=threading.Thread(target=func)

for i in range(5):
    t=threading.Thread(target=func)
    t.start()


# threadpool=ThreadPoolExecutor(max_workers=5)
#
# for i in range(5):
#     threadpool.submit()
# threadpool.shutdown()

with ThreadPoolExecutor(max_workers=5) as t:
    for i in range(5):
        t.submit(func)
