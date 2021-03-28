#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e4.py
# author:dell
# datetime:2021/3/28 18:59
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

f=open('test5.txt','r',encoding='utf-8')

list1=f.readlines()

for i in list1:
    print(i)

f.close()