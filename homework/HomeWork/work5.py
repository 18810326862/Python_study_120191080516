#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work5.py
# author:dell
# datetime:2021/3/27 9:56
# software: PyCharm
'''
this is functiondescription
'''

# 5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
# import module your need

def func(dic):
    for key,vaule in dic.items():
        if(len(vaule)>2):
            dic[key]=vaule[0:2]

dic={1:"123",2:"666"}
func(dic)
print(dic)