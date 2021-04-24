#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e3.py
# author:dell
# datetime:2021/4/22 18:31
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 练习:  定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;


def decorator(f):
    print(f.__name__)
    return f

@decorator
def myadd(i,j):
    return i+j

print(myadd(1,2))
