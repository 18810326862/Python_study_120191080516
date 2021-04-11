#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/4/7 20:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX

import base64

# stulist=[]
with open('stu.txt','wb') as f:
   # f.write('姓名      账号         密码\n')
    for i in range(5):
        # stulist.append([{'姓名':input('姓名')}])
        # stulist.append([{'账号':input('账号')}])
        # stulist.append([{'密码':input('密码')}])
        f.write((input('姓名') + '      ').encode())
        f.write((input('账号') + '      ').encode())
        f.write(base64.b64encode(input('密码').encode())+'      '.encode())
        f.write('\n'.encode())




