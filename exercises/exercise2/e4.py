#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e4.py
# author:dell
# datetime:2021/4/22 18:39
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time


def decorator(func):
    def inner(*args,**kwargs):
        start=time.time()
        func(*args,**kwargs)
        time.sleep(1)
        end=time.time()
        print('运行时间为：',end-start-1)
    return inner

@decorator
def add1(i,j):
    print(i+j)

@decorator
def add2(i,j,k):
    print(i+j+k)


if __name__ == '__main__':
    add1(1,2)
    add2(1,2,3)




