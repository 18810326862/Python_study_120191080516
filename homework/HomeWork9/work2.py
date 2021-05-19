#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/5/18 20:40
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；

import socket
def UDPtest():

    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',8888))
    while True:
        data,addr=s.recvfrom(1024)
        print(data.decode('gbk'))

def TCPtest():

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',8888))
    s.listen(5)#不能少
    sock,addr=s.accept()
    print(addr)
    print('连接成功')
    while True:
        data=sock.recv(1024)
        print(data.decode('gbk'))

if __name__ == '__main__':
    TCPtest()
