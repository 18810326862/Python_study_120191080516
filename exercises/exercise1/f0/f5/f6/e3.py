#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e3.py
# author:dell
# datetime:2021/3/28 15:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

f=open('test6.txt','w',encoding='gbk')
f.write('我')
f.close()
f=open('test6.txt','r')
# str=f.read().decode('gbk').encode('utf-8')
str=f.read().encode('utf-8')
print(str)
f.close()