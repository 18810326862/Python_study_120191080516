#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/5/18 20:40
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    datainput=input('请输入内容')
    s.sendto(bytes(datainput,'utf8'),('127.0.0.1',8888))
    data,addr=s.recvfrom(1024)
    print(data.decode('utf8'))

