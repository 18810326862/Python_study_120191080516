#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/3/29 16:59
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
# 将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
list1=[]
with open('f1.txt','a',encoding='utf-8') as f:
    while True:
        i=input()
        if not i:
            break
        else:
            list1.append(i)
    for i in list1:
        f.write(i+'\n')
