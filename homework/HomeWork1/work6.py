#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work6.py
# author:dell
# datetime:2021/3/30 16:23
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#
# 6  对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；
#         英文小说"老人与海"     链接：https://pan.baidu.com/s/1goqK3zF8VBUFuD_2ezfZ7Q   提取码：mv04
#     提示：
#     1 可以先定义一个函数，专门来处理英文文章的读取问题；读取时，解决大小写问题，以及标点符号问题（如，将标点符号都替换成空格）；
import collections

def getText():
    with open('《老人与海》[英文版].txt','r',encoding='utf-8')as f:
        txt=f.read()
        txt=txt.lower()
        for ch in '!"#$%&()*+,-./;:<=>?@[\\]^_‘{|}~':
            txt=txt.replace(ch," ")
    return txt

txt=getText()
def counttxt(txt):
    list1=list(txt.split())


    dict1=dict(collections.Counter(list1))
    # for key,value in dict1.items():
    #     print(key,'  ',value)

    list2=list(zip(dict1.keys(),dict1.values()))
    # print(type(list2))
    list2.sort(key=lambda x:x[1],reverse=True)
    return list2
list2=counttxt(txt)
for i in range(20):
    print(i+1,'.',list2[i][0],':',list2[i][1])

