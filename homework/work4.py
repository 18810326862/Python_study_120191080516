#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/3/4 20:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def judge(year):
    i=0
    if (year%4==0&year%100!=0)|(year%400==0):
        i=1
    return i
while 1:
    print("请输入年份")
    year=input();
    if judge(int(year))==1:
        print("yes")
    else:
        print("no")
    print("继续（y|n）")
    c=input()
    if c=='y':
        continue
    elif c=='n':
        break
    else:
        print("输入错误")
        break