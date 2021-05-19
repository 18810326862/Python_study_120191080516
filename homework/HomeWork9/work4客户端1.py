#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4客户端1.py
# author:dell
# datetime:2021/5/19 16:58
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import socket
import threading
import os

class myClient:
    def __init__(self):
        self.sever_addr=('127.0.0.1',8888)
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    def recv_message(self):
        print("连接成功！现在可以接收消息！\n")
        while True:
            try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
                response = self.sock.recv(1024)
                print(response.decode("gbk"))
            except ConnectionResetError:
                print("服务器关闭，聊天已结束！")
                self.sock.close()
                break
        os._exit(0)



    def send_message(self):
        print("连接成功！现在可以发送消息！\n")
        print("输入消息按回车来发送")
        print("输入esc来退出聊天")
        while True:
            msg = input()
            if msg == "esc":
                print("你退出了聊天")
                self.sock.close()
                break
            self.sock.send(msg.encode("gbk"))
        os._exit(0)

    def start_client(self):
        self.sock.connect(self.sever_addr)
        threads = [threading.Thread(target=self.recv_message), threading.Thread(target=self.send_message)]
        for t in threads:
            t.start()

if __name__ == '__main__':
    client1 = myClient()
    client1.start_client()


