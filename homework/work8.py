#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work8.py
# author:dell
# datetime:2021/3/4 20:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


emp0={'id':1001,'name':'xiaozhang','age':12,'sal':8000.0}
emp1={'id':1002,'name':'xiaowang','age':12,'sal':9000.0}
emp2={'id':1003,'name':'xiaoli','age':12,'sal':7000.0}
emp3={'id':1004,'name':'xiaoming','age':12,'sal':30000.0}
emp4={'id':1005,'name':'xiaohong','age':12,'sal':6000.0}
emp5={'id':1006,'name':'xiaohua','age':12,'sal':40000.0}
emp6={'id':1007,'name':'xiaolan','age':12,'sal':50000.0}
emp7={'id':1008,'name':'xiaozi','age':12,'sal':70000.0}
emp8={'id':1009,'name':'xiaowen','age':12,'sal':100000.0}
emp9={'id':1000,'name':'xiaoliu','age':12,'sal':90000.0}

list1=[emp0,emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9]

i=0


while i< len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]['sal']>list1[j]['sal']:
            d=list1[i]
            list1[i]=list1[j]
            list1[j]=d
        j=j+1
    i=i+1
print(list1)


