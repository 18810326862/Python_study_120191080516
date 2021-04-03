#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/3/29 17:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
list1=[]
list2=[]
with open('f3.txt','r',encoding='utf-8') as f:
    for line in f:
        list1.append(line.strip().split())
    i=1
    while(i<len(list1)):
        list2.append(list1[i])
        i+=1
    list2.sort(key=lambda x:x[2])
    for i in list1[0]:
        print(i+"       ",end="")
    print()
    for i in list2:
        for j in i:
            print(j+"      ",end="")
        print()