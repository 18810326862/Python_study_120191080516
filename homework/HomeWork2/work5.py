#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work5.py
# author:dell
# datetime:2021/4/7 20:21
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 5  通过Python来模拟实现一个txt文件的拷贝过程;
import os

def mycopy(url):

    try:
        with open(url,'r',encoding='utf-8')as f:
            s=f.readlines()
    except FileNotFoundError:
        print('文件不存在')
        return
    with open(os.path.dirname(url)+'copy.txt','w',encoding='utf-8')as f:
        for i in s:
            f.write(i)

mycopy('stu.txt')