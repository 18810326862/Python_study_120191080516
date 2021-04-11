#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work7.py
# author:dell
# datetime:2021/4/7 20:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 7 使用python代码统计一个文件夹中所有文件的总大小
import os
def totalsize(url):
    try:
        if os.path.isfile(url):
            print('不是文件夹')
            return
        size=0
        for i in os.listdir(url):
            s=os.path.join(url,i)
            if os.path.isfile(s):
                size+=os.path.getsize(s)
            else:
                totalsize(s)
        return size
    except FileNotFoundError:
        print('文件不存在')

if __name__ == '__main__':
    print(totalsize('f1'))