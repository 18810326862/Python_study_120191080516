#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/5/10 21:00
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 4 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；


from multiprocessing import Queue,Process

# def writeData(q):
#     while True:
#         q.put(input('请输入消息'))

def readData(q):
    while True:
        print(q.get())
        print()


if __name__ == '__main__':
    q=Queue()

    p1=Process(target=readData,args=(q,))

    p1.start()

    while True:
        q.put(input())



