#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e5.py
# author:dell
# datetime:2021/4/22 18:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 练习:
#  定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样(打打印提示语句, XXX狗在叫,来体现叫声不一样);
#  然后实例化几条狗, 然后统计实例化狗的数量

class Dog():
    count=0
    def __init__(self,name):
        self.name=name
        Dog.count+=1
    def fork(self):
        print(f'{self.name}在叫')

if __name__ == '__main__':
    dog1=Dog('1')
    dog2=Dog('2')
    print(Dog.count)


    dog1.fork()
    dog2.fork()