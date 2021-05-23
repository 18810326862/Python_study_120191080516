#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/5/22 20:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

'''4 数据序列化和处理练习；给定一个json格式的数据；
  [
    {
        "name":"Frank",
        "age":15,
        "isEmployed":true
    },
    {
        "name":"zhagnsan",
        "age":39,
        "isEmployed":true
    },
    {
        "name":"李四",
        "age":39,
        "isEmployed":true
    },
    {
        "name":"王五",
        "age":39,
        "isEmployed":true
    }
]
   '''
import json
data= [
    {
        "name":"Frank",
        "age":15,
        "isEmployed":True
    },
    {
        "name":"zhagnsan",
        "age":39,
        "isEmployed":True
    },
    {
        "name":"李四",
        "age":39,
        "isEmployed":True
    },
    {
        "name":"王五",
        "age":39,
        "isEmployed":True
    }
]
with open('data.txt','w') as f:
    json.dump(data,f)
with open('data.txt','r')as f:
    text=json.load(f)
    print(text)
    print()
    for i in text:
        print(i)