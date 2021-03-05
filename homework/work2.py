#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/3/4 18:42
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

studentinfo={1001:100,1002:60,
             1003:90,1004:66,1005:65.5,
             1006:76.3,1007:77.5,
             1008:99.5,1009:96.5,1010:80}
for key, vaule in studentinfo.items():
    if int(vaule)>80:
        print(str(key)+":"+str(vaule)+"\n")