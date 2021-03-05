#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work9.py
# author:dell
# datetime:2021/3/4 20:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

N=10
guesstrue=50
while N>0:
    print("请输入数字(0-100)")
    guess=input()
    if int(guess)==guesstrue:
        print("正确")
        break
    elif int(guess)>guesstrue:
        print("大了")
    elif int(guess)<guesstrue:
        print("小了")
    N=N-1

