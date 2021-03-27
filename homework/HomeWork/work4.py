#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/3/27 14:25
# software: PyCharm
'''
this is functiondescription
'''

# 4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
# import module your need

def countStr(str):
    i=0
    j=0
    k=0
    m=0
    '12'
    for s in str:
        if s>='0'and s<='9':
            i+=1
        elif s>='a' and s<='z'or s>='A'and s<='Z':
            j+=1
        elif s==' ':
            k+=1;
        else:
            m+=1;
    print("数字数：{}字母数：{}空格数：{}其他字符：{}".format(i,j,k,m))
if __name__ == '__main__':
    str='123   456  rgk ,;.'
    countStr(str)