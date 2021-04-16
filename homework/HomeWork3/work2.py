#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/4/13 16:16
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；

def outer(func):
    def inner():
        print('调用%s函数'%(func.__name__))
        with open('func.txt','a',encoding='utf-8')as f:
            f.write('调用{}函数'.format(func.__name__))
            f.write('\n')
        func()
    return inner

@outer
def myfunc():
    print('123')

@outer
def myfunc1():
    print('123')

if __name__ == '__main__':
    myfunc()
    myfunc1()
