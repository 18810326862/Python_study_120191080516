#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work5.py
# author:dell
# datetime:2021/3/29 22:01
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 请完成以下文件综合编程迷你项目（提示：可以利用list的insert函数）。
# （1）创建一个文件Blowing in the wind.txt,其内容是：
# How many roads must a man walk down
# Before they call him a man
# How many seas must a white dove sail
# Before she sleeps in the sand
# How many times must the cannon balls fly
# Before they're forever banned
# The answer my friend is blowing in the wind
# The answer is blowing in the wind
# (2)在文件头部插入歌名“Blowin'in the wind”
# （3）在歌名后插入歌手名“Bob Dylan”
# （4）在文件末尾加上字符串“1962 by Warner Bros.Inc.”
# （5）在屏幕上打印文件内容

with open('Blowing in the wind.txt','w',encoding='utf-8') as f:
    str='''How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind'''
    f.write(str)
list1=[]
with open('Blowing in the wind.txt','r',encoding='utf-8')as f:
    for i in f:
        list1.append(i)
list1.insert(0,'Blowin’in the wind\n')
list1.append('\n1962 by Warner Bros.Inc.')
with open('Blowing in the wind.txt','w',encoding='utf-8')as f:
    for i in list1:
        f.write(i)
with open('Blowing in the wind.txt','r',encoding='utf-8')as f:
    for i in f:
        print(i,end='')



