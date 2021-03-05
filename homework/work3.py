#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/3/4 20:03
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def sameinlist(list1,list2):
    list3=[]
    for list11 in list1:
        for list22 in list2:
            if list22==list11:
                list3.append(list22)

    for l in set(list3):
        print(str(l)+" ",end=" ")
list1=['1','2','3','4','5']
list2=['6','7','8','3','9','0','1']
sameinlist(list1,list2)