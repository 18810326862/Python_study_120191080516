#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work8.py
# author:dell
# datetime:2021/4/1 22:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 8
# 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
# 请读取文章内容, 进行词频的统计;
# 并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词, 重复了5个, 相似度就是50 %;
# 重复了6个, 相似度就是60 %, ......);
import collections

def getText(url):
    with open(url,'r',encoding='utf-8')as f:
        txt=f.read()
        txt=txt.lower()
        for ch in '!"#$%&()*+,-./;:<=>?@[\\]^_‘{|}~':
            txt=txt.replace(ch," ")
    return txt

def counttxt(txt):
    list1=list(txt.split())


    dict1=dict(collections.Counter(list1))
    # for key,value in dict1.items():
    #     print(key,'  ',value)

    list2=list(zip(dict1.keys(),dict1.values()))
    # print(type(list2))
    list2.sort(key=lambda x:x[1],reverse=True)
    return list2

list1=counttxt(getText('1.txt'))
list2=counttxt(getText('3.txt'))
with open('11.txt','w',encoding='utf-8')as f:
    for i in list1:
        f.write(str(i[0])+':'+str(i[1]))


with open('33.txt','w',encoding='utf-8')as f:
    for i in list2:
        f.write(str(i[0])+':'+str(i[1]))


count=0
for i in range(10):
    for j in range(10):
        if(list1[i][0]==list2[j][0]):
            count+=1
            break
count*=10
print('相似度：',count,'%')





