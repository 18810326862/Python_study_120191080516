#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:class3.py
# author:dell
# datetime:2021/3/6 9:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need




s=input();
i=0
l = []
while i < len(s):
    l.append(s[i])
    i=i+1
#字符串
print(s[-1::-1])

#列表
l=l[-1::-1]
s="".join(l)
print(s)
