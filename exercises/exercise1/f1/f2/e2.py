#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e2.py
# author:dell
# datetime:2021/3/28 15:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

f=open('test2.txt','r')
print(f.read())
f.close()
print()
f=open('f3/test3.txt','r')
print(f.read())
f.close()
print()
f=open('../test1.txt','r')
print(f.readlines())
print()