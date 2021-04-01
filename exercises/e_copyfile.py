#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e_copyfile.py
# author:dell
# datetime:2021/4/1 19:01
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os

# print(os.path.basename('f3/test3.txt'))
# print(type(os.path.join('f3','test3.txt')))
def renamefile(str,j):
    list1=list(str)
    i=list1.index('.')
    list1.insert(i,'(%d)'%j)
    return ''.join(list1)


def mycopy(url1,url2):
    if not os.path.exists(url1):
        print('不存在此路径')
        return
    with open(url1,'r',encoding='utf-8') as f:
        str=f.read()
    url=os.path.join(url2,os.path.basename(url1))
    if os.path.exists(url):
        for i in range(1,10):
            url3=os.path.join(url2, renamefile(os.path.basename(url1), i))
            if not os.path.exists(url3):
                with open(url3,'w',encoding='utf-8')as f:
                    f.write(str)
                break
    else:
        with open(url,'w',encoding='utf-8')as f:
            f.write(str)
if __name__ == '__main__':
    mycopy('f2/test2.txt','f2/f3')





