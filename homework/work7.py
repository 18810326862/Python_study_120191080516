#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work7.py
# author:dell
# datetime:2021/3/4 20:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

i=1
j=1
while i<=9:
    j=1
    while j<=i:

        print(str(i)+"*"+str(j)+"="+str(i*j).ljust(6," "),end=" ")
        j=j+1
    print("\n")
    i=i+1
