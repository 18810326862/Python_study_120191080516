#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e1.py
# author:dell
# datetime:2021/3/28 15:01
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import os
print(os.path.abspath('test.txt'))
print(os.path.join('f1','test1'))
print(os.path.basename('/f1/f2/test2.txt'))
print(os.path.split('ff/ttt.txt'))
print(os.getcwd())
os.chdir('f0/f5')
print(os.getcwd())
os.mkdir('f6')