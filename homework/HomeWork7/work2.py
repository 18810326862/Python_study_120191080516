#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/5/28 19:05
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
'''
import requests
from bs4 import BeautifulSoup
import  re

def printurl(url):
    try:
        #print(url)
        r = requests.get(url=url,timeout=1)
        demo = r.text
        soup = BeautifulSoup(demo, "html.parser")
        print(url+':')
        for link in soup.find_all('a', string=re.compile(r"企业介绍|关于我们|企业发展|发展历史|企业概括|history|about")):
            # if link.get('value')=='关于我们':
            print(link.get('href'))
    except:
         print('错误')

def getallurl():
    with open('webspiderUrl_result.txt','r',encoding='utf8')as f:
        while True:
            url = f.readline()

            if  url:
                printurl(url.strip())
            else:
               break

if __name__ == '__main__':
    getallurl()



# with open('webspiderUrl_result.txt','r',encoding='utf8')as f:
#     url = f.readline()
#     print(url.encode('gbk'))
#     # r = requests.get(url)
#     # print(r)
