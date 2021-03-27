#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work10.py
# author:dell
# datetime:2021/3/27 14:27
# software: PyCharm
'''
this is functiondescription
'''

# 10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
# import module your need

def cal(a,b):
    print('a+b=',a+b)
    print('a-b=',a-b)
    print('a*b=',a*b)
    print('a/b=',a/b)

if __name__ == '__main__':
    a,b=input('请输入两个数\n').split()
    cal(float(a),float(b))