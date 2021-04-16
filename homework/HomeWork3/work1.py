#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/4/13 16:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 1  编写一个装饰器，能计算其他函数的运行时间；
import time
def outer(fun):
    def inner():
        start=time.time()
        fun()
        time.sleep(1)
        end=time.time()
        print('运行时间为%s'%(end-start-1))
    return inner

def func():
    time.sleep(1)

if __name__ == '__main__':
    func=outer(func)
    func()#这时候执行inner
