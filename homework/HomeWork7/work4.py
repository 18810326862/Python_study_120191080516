#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/6/4 16:10
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
4 爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
    文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

  参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
   大家看完这篇文档后，再开始动手做这道题；


https://www.programcreek.com/python/index/1200/flask
'''

from bs4 import BeautifulSoup
import requests


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
    }

def getherf():


    url = 'https://www.programcreek.com/python/index/1200/flask'

    # 伪装成浏览器


    # 发送请求
    r = requests.get(url, headers=headers).content.decode('utf-8')
    # print(r)

    # 解析html文档
    soup = BeautifulSoup(r, 'html.parser')  # 这里用lxml会出错
    # print(type(soup))

    # 查找每个练习的a链接href属性获取对应的链接地址
    re_a = soup.find(id='api-list').find_all('a')  # 返回的是100个a标签的列表

    # 创建一个列表保存url
    list = []
    for i in re_a:
        list.append(i.attrs['href'])

    return list

def savedata(list):
    for a in list:

        test = requests.get(a.strip(), headers=headers).content.decode('utf-8')
        soup_test = BeautifulSoup(test, 'html.parser')
        s=''
        for pre in soup_test.find_all(class_='prettyprint'):
            # name = 'pre', attrs = {'class': 'prettyprint'}
            # s = ''
            # for data in pre.find_all('span'):
            #     s += data.text
            s+=pre.text
            print(s)
            with open('infomation.txt','a+',encoding='utf8')as f:
                f.write(s)
                f.write('\n')

if __name__ == '__main__':
    herflist = getherf()
    savedata(herflist)
