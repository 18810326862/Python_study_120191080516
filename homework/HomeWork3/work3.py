#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/4/13 16:16
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

import time
def outer(func):
    def inner():
        name=input('请输入账号')
        password=input('请输入密码')
        if name=='admin' and password=='123456':
            print('登陆成功')
            func()
        else:
            print('账号或密码错误')
    return inner
@outer
def myfunc():
    time.sleep(1)
    print('myfunc')


if __name__ == '__main__':
    myfunc()