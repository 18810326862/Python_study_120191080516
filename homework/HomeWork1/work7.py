#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work7.py
# author:dell
# datetime:2021/4/1 22:22
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 7 对一篇中文文献, ;利用jieba库,进行词频统计分析找出文章的关键词(取词频最高的前10个词语,作为文章的关键字);

import jieba
import collections
import pdfplumber
import docx
from win32com.client import Dispatch
import os

# def getkeyword(url):
#     with open(url,'r',encoding='utf-8')as f:
#         txt=f.read()
#     txtlist=jieba.lcut(txt)
#     dictcount=dict(collections.Counter(txtlist))
#     return dictcount

def getkeyword(txt):
    txtlist=jieba.lcut(txt)
    dictcount=dict(collections.Counter(txtlist))
    return dictcount

def pdfread(url):
    with pdfplumber.open(url)as p:
        txt=''
        for i in range(0, 100):
            try:
                p.pages[i]
            except:
                break
            page = p.pages[i]
            txt+=str(page.extract_text())#!!!
    return txt

def docxread(url):
    txt=''
    file = docx.Document(url)
    for p in file.paragraphs:
        txt+=p.text
    return txt
def docread(url):
    wd = Dispatch('Word.application')
    wd.Visible = 0
    wd.DisplayAlerts = 0
    doc = wd.Documents.Open(url)  # 绝对路径
    filename=os.path.basename(url)
    filename1=filename+'x'
    doc.SaveAs("F:/python_test/python_study_exercise1/练习/123/"+filename1, 12)
    doc.Close()
    wd.Quit()
    return docxread("F:/python_test/python_study_exercise1/练习/123/"+filename1)




if __name__ == '__main__':

# print(getkeyword('../练习/新建文本文档.txt'))
#     print(docread("F:/python_test/python_study_exercise1/练习/123.doc"))
    filetxt=pdfread('123.pdf')
    dict1=getkeyword(filetxt)
    for ch in '\n ,().。:>!"#$%&()*+,-./;:<=>?@[\\]^_‘{|}~，：\'‘':
        dict1[ch]=0

    list1=list(dict1.items())#!!!
    list1.sort(key=lambda x:x[1],reverse=True)


    for i in range(0,10):
        print(list1[i])



