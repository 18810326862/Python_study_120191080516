#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/4/5 14:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，
# 能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
import datetime

def schoolcal():
    dic1={1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'日'}
    days=datetime.datetime.strptime(input('日期2021 4 10\n'),"%Y %m %d")
    i=days.isocalendar()[1]

    j=datetime.datetime.isocalendar(datetime.datetime(2021,2,17))[1]

    print('第{}周的周{}'.format(i-j,dic1[days.isoweekday()]))

if __name__ == '__main__':
    schoolcal()
