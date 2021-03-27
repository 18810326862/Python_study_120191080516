#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/3/27 14:14
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#2 编写一个函数,接收n个数字，求这些参数数字的和;
def mySum(*i):
    sum=0
    for a in i:
        sum+=a
    return sum

if __name__ == '__main__':
    print(mySum(1,2,3,4,5,6,7,8,9))