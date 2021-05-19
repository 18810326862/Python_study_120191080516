#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/5/18 20:41
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
#   参考文档：https://blog.csdn.net/CxsGhost/article/details/103319864

import socket
import threading
import datetime
import os

class myServer:
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addr=('127.0.0.1',8888)
        self.users={}

    def start_server(self):
        self.sock.bind(self.addr)
        self.sock.listen(5)
        print("服务器已开启，等待连接...")
        print("在空白处输入stop sever并回车，来关闭服务器")
        threading.Thread(target=self.socket_accpet).start()

    def socket_accpet(self):
        while True:
            s,addr=self.sock.accept()
            self.users[addr]=s
            print('用户{}连接，总共{}名用户'.format(addr,len(self.users)))
            threading.Thread(target=self.rec_data, args=(s, addr)).start()




    def rec_data(self,sock,addr):
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("gbk")
                msg = "{}用户{}发来消息：{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), addr, response)


                for client in self.users.values():
                    client.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break
    def close_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    sever=myServer()
    sever.start_server()
    while True:
        cmd = input()
        if cmd == "stop sever":
            sever.close_sever()
        else:
            print("输入命令无效，请重新输入！")




