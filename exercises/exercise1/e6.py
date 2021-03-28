#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e6.py
# author:dell
# datetime:2021/3/28 19:51
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import pickle
stu=[{'学号':123450,'姓名':'www','年龄':20},
     {'学号':123451,'姓名':'qqq','年龄':20},
     {'学号':123452,'姓名':'eee','年龄':20},
     {'学号':123453,'姓名':'rrr','年龄':20},
     {'学号':123454,'姓名':'ttt','年龄':20},
     {'学号':123455,'姓名':'yyy','年龄':20},
     {'学号':123456,'姓名':'uuu','年龄':20},]
with open('test.txt','wb')as f:
    pickle.dump(stu,f)
with open('test.txt','rb')as f:
    s=pickle.load(f)

for i in s:
    print(i)