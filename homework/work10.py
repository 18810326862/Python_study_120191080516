#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work10.py
# author:dell
# datetime:2021/3/4 20:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import re
def go_split(s, symbol):

    result = re.split(symbol, s)

    return [x for x in result if x]



def dictory(s):

    symbol='[. ,?!]'
    ss=go_split(s,symbol)
    print(ss)
    i=0
    dic={}
    while i<len(ss):
      ss[i]=ss[i].lower()
      ss[i]=ss[i].strip()
      flag=0
      for key,value in dic.items():
          if ss[i]==key:
                dic[key]=value+1
                flag=1
      if flag==0:
         dic[ss[i]]=1
         flag=0


      i=i+1
    print(dic)
dictory('123,456.789?666!777  ABC  123')







































