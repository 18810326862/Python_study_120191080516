#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:高阶函数练习.py
# author:dell
# datetime:2021/4/8 14:55
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):

    # return a/b
    try:
        return a/b
    except:
        print('ERROR')
def highfunction(a,b,f):
    return f(a,b)



if __name__ == '__main__':
    print(highfunction(3,0,div))
    print(highfunction(3,0,mul))
    print(highfunction(3,0,sub))
    print(highfunction(3,0,add))