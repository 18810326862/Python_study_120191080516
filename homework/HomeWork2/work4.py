#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/4/7 20:21
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 4  (继续上面的练习) 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,
# 提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
import base64
with open('stu.txt','r',encoding='utf-8') as f:
    stu=f.readlines()
list1=[]
for i in stu:
    list1.append(i.strip().split())
s1=input('请输入同学姓名')
# for i in range(1,6):
#     list1.append(stu[i].strip().split())
# for i in range(1,6):
#     if s1.strip()==list1[i][0]:
flag=False
for data in list1:
    # print(data)

    if data[0]==s1.strip():
        flag=True
        s2=input('请输入学生账号')
        if s2.strip()==data[1]:
            s3=input('请输入密码')
            if base64.b64encode(s3.strip().encode())==data[2].encode():
                print('登陆成功')
                break;
            else:
                print('密码错误')
                break
        else:
            print('账号错误')
            break
if not flag:
    print('姓名不存在')

