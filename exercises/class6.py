#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:class6.py
# author:dell
# datetime:2021/3/6 10:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
movie='流浪地球'
ticket=45.9

count=15
total=ticket*count
ticket=format(ticket,'.6f')
s=f'电影：{movie}\n人数：{count}\n单价：{ticket}\n总票价：{total}'
print(s)