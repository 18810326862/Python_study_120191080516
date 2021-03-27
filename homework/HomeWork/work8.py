#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work8.py
# author:dell
# datetime:2021/3/27 14:26
# software: PyCharm
'''
this is functiondescription
'''

# 8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
#  例如，输入 aaaabbc，输出：a:4
# import module your need

def counts(str):
    dic={}
    for s in str:
        if s in dic.keys():
            dic[s]+=1
        else:
            dic[s]=1
    for key,value in dic.items():
        if value==max(dic.values()):
            print(key,':',value)
            break

if __name__ == '__main__':
    str='1112223333334abc'
    counts(str)
