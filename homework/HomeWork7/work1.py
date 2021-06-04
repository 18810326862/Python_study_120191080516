#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/5/24 21:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有10000行，注意控制每次读取的行数；
'''


import re
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
mutex=Lock()
def read_web():
    with open('webspiderUrl.txt','r',encoding='utf8')as f:
        for data in f:

            yield data

# http://www.bjtiangu.com

def judge_web(read_web,f):
    for i in range(2000):
       try:
            mutex.acquire()
            s=next(read_web)

            mutex.release()
            #web=re.search(r"http://www.[\w]+\.[com,con,net]{1,3}$",s)
            #web=re.search(r"http://www\.[\w]+\.(com|cn|net)",s)
            web=re.search(r"http://www.\w+.(com|cn|net)",s)
            #web=re.search(r"((((https|http|ftp|file|rtsp|mms)://)|www\\.)([a-zA-Z0-9\-]))|^localhost|^((2(5[0-5]|[0-4]\\d))|[0-1]?\\d{1,2})(\\.((2(5[0-5]|[0-4]\\d))|[0-1]?\\d{1,2})){3}|(([a-zA-Z0-9])(\\.(com|cn|io|html|htm|top|ltd|net|xin|vip|store|shop|wang|cloud|xyz|ren|tech|online|site|ink|link|love|art|fun|club|cc|website|press|space|beer|luxe|video|group|fit|yoga|net|org|pro|biz|info|design|work|mobi|kim|pub|org|name|tv|co|asia|red|live|wiki|gov|cn|life|world|run|show|city|gold|today|plus|cool|icu|中国|网店|中文网|公司|网络|集团|商城|招聘|佛山|广东|网址|在线|我爱你|商标|餐厅))(:[0-9]{1,4})?(/?))$",s)
            #web=re.search(r"(?=^.{3,255}$)(http(s)?:\/\/)?(www\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(:\d+)*(\/\w+\.\w+)*$",s)
            if web:
                print(web.group())
                mutex.acquire()
                f.write(web.group()+'\n')
                mutex.release()
       except StopIteration:
           pass

if __name__ == '__main__':
    read=read_web()
    #judge_web(read)
    with open('webspiderUrl_result.txt','w',encoding='utf8')as f:#1
        with ThreadPoolExecutor(max_workers=10) as t :#2   1 2顺序不能换

            for i in range(5):
                t.submit(judge_web,read,f)
























#from itertools import islice


#islice() 类似于切片

# with open('webspiderUrl.txt','r',encoding='utf8') as f:
#     num = 0
#     while True:
#         #for i in islice(f,0,6):
#         #print(islice(f,0,6).__next__())
#         #print('************')
#         it=islice(f,0,6)
#         for i in it:
#             print(num,i)
#             num+=1
#         # if num==10000:
#         #     break
#         if not it:
#             break


# with open('webspiderUrl.txt','r',encoding='utf8') as f:
#     print(print(f.readline()))

#with open('webspiderUrl.txt','r',encoding='utf8')as f:
    #print(f.read())
    # try:
    #     while True:
    #         s=f.readline()
    #         print(s)
    # except:
    #     pass



    # for data in f:
    #     print(data)



    # while True:
    #     s=f.readline()
    #     if not s:
    #         break
    #     else:
    #         print(s)






