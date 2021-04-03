#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/3/29 17:10
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
# #第一行： xxxx
# #第二行： xxxx

with open('input.txt','r',encoding='utf-8') as f:
    list1=f.readlines()
for i in list1:
    print('#第一行:{}'.format(i))