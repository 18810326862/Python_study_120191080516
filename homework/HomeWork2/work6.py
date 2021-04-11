#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work6.py
# author:dell
# datetime:2021/4/7 20:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
#     名称         日期                   类型（文件夹或者 文件）       大小
import os
import datetime
print('名称       日期           类型           大小')
url='f1'
for i in os.listdir(url):
    s=os.path.join(url,i)
    if os.path.isfile(s):
        print('{}     {}     {}     {}'.format(os.path.basename(s),datetime.datetime.fromtimestamp(os.path.getctime(s)).replace(microsecond=0),'file',os.path.getsize(s)))
    else:
        print('{}     {}     {}     /'.format(os.path.basename(s),datetime.datetime.fromtimestamp(os.path.getctime(s)).replace(microsecond=0),'dir'))