#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work6.py
# author:dell
# datetime:2021/3/27 14:25
# software: PyCharm
'''
this is functiondescription
'''

# 6  定义一个函数, 打印输出n以内的斐波那契数列;
# import module your need

def Fibonacci(n):
    a=0
    b=1

    while(1):
        if a>n:
            break
        print(a,end=" ")
        a,b=b,a+b
if __name__ == '__main__':
    Fibonacci(20)
