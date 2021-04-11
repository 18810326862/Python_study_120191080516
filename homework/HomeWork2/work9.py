#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work9.py
# author:dell
# datetime:2021/4/7 20:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 9 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）

from urllib import request
import os

# https://game.gtimg.cn/images/lol/act/img/skin/big34007.jpg

with request.urlopen('https://game.gtimg.cn/images/lol/act/img/skin/big34007.jpg') as f:
    s=f.read()

with open('image.jpg','wb')as f:
    f.write(s)