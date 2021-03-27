#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/3/27 14:13
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def getlen(s):
    return len(s)
if __name__ == '__main__':

    str='12345'
    list1=[1,2,3,4,5]
    tup=(1,2,3,4,5)
    print(getlen(str),getlen(list1),getlen(tup))
    

