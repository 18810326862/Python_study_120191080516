#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work9.py
# author:dell
# datetime:2021/3/27 14:27
# software: PyCharm
'''
this is functiondescription
'''

# 9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
# import module your need

def mySort(list):
    list.sort()
if __name__ == '__main__':
    list1=[1,3,5,6,2,7]
    mySort(list1)
    print(list1)