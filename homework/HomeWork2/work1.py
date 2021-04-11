#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/4/5 14:24
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
# 用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#     提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
import datetime
import time
from collections import deque
list1=[0,1,2,3,4,5,6,7,8,9]
now1=datetime.datetime.now()
list1.insert(0,0)
list1.append(10)
time.sleep(1)
now2=datetime.datetime.now()
s=datetime.timedelta(seconds=1)
print('程序运行时间：',now2-now1-s)

q=deque([0,1,2,3,4,5,6,7,8,9])
now1=datetime.datetime.now()
q.appendleft(0)
q.append(10)

time.sleep(1)
now2=datetime.datetime.now()
s=datetime.timedelta(seconds=1)
print("程序运行时间：",now2-now1-s)



