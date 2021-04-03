#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/3/29 19:25
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 4 题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.


import os
with open('1.png','rb') as f:
    str=f.read()
# for i in range(10):
#    os.remove('p{}.jpg'.format(i))


os.chdir('image')
for i in range(10):
    with open('p{}.jpg'.format(i),'wb') as f:
        f.write(str)
print(os.listdir('.'))
for i in os.listdir('.'):
    if i[-3:]=='jpg':
        os.rename(i,i[:-3]+'png')


