#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e5.py
# author:dell
# datetime:2021/3/28 19:09
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

with open('test5.txt','r',encoding='utf-8') as f:
    list1=f.readlines()
list2=[]
for i in list1:
    list2.append(list(i.split()))
print(list2)

list3=[]
list3.append(list2[0])
list4=[]
for i in range(len(list2)):
    if i>0:
        list4.append(list2[i])
list4.sort(key=lambda x:x[2])
print(list4)

for i in list4:
    list3.append(i)
print(list3)
with open('test5_1.txt','w',encoding='utf-8')as f:
    for i in list3:
        f.writelines('{}      {}      {}\n'.format(i[0],i[1],i[2]))





