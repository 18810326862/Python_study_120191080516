#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/3/27 14:17
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#    数字列表请用随机数函数生成;
import random
def jishu(s):
    print(s)
    for a in s:
        if int(a)%2!=0:
            print(a,end=" ")
if __name__ == '__main__':

    list1=[random.randint(0,100) for x in range(0,10)]
    print(list1)
    jishu(list1)
