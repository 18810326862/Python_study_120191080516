#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work8.py
# author:dell
# datetime:2021/4/7 20:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 8 京东二面笔试题
# # 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# # 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random
import collections

with open('ip.txt','w',encoding='utf-8')as f:
    for i in range(0,1200):
        f.write('172.25.254.{}\n'.format(random.randint(1,254)))


with open('ip.txt','r',encoding='utf-8')as f:
    # ip_list=[]
    # while True:
    #
    #         ip_list.append(f.read())
    ip_list=f.readlines()
for i in range(0,len(ip_list)):
    ip_list[i]=ip_list[i].strip()

dict1=collections.Counter(ip_list)
# print(dict1)
# print(dict1.most_common(10))
for i in dict1.most_common(10):
    print(i)

