#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work7.py
# author:dell
# datetime:2021/3/27 14:26
# software: PyCharm
'''
this is functiondescription
'''
#
# 7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
#     A---成绩>=90;
#     B-->成绩在 [80,90)
#     C-->成绩在 [70,80)
#     D-->成绩<70
# import module your need
import random
def studentScore(dic):
    i=1
    for key,value in dic.items():
        if value>=90:
            print(key,':A',end="  ")
        elif value>=80 and value<90:
            print(key,':B',end="  ")
        elif value>=70 and value<80:
            print(key,':C',end="  ")
        else:
            print(key,':D',end="  ")
        i+=1
        if i==5:
            print()
            i=1
if __name__ == '__main__':
    dic={x:random.randint(0,100) for x in range(0,20)}
    print(dic)
    studentScore(dic)