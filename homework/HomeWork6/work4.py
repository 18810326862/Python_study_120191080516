#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/4/18 12:51
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class studentclass(object):
    name=''
    age=0
    sex='男'
    englishscore=0
    mathscore=0
    chinesescore=0

    def __init__(self,name,age,sex,englishscore,mathscore,chinesescore):
        self.name=name
        self.age=age
        self.sex=sex
        self.englishscore=englishscore
        self.mathscore=mathscore
        self.chinesescore=chinesescore

    def getallsocre(self):
        print('总成绩为：%d'%(self.chinesescore+self.mathscore+self.englishscore))
    def getavg(self):
        print('平均成绩为：%f'%((self.englishscore+self.mathscore+self.chinesescore)/3))
    def getmessage(self):
        print('姓名{},性别{},年龄{},语文成绩{},数学成绩{},英语成绩{}'.format(self.name,self.sex,self.age,
                                                           self.chinesescore,self.mathscore,self.englishscore))

