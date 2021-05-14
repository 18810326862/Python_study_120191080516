#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/5/9 13:21
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
# import math
#
# def judgePrime(m)
#     i=2
#     while(i<=math.sqrt(m)):
import math
import time
from multiprocessing import Pool,Queue
def printPrime(start,end):
    count=0
    while(start<=end):
        i=2
        while(i<=math.sqrt(start)):
            if start%i==0 :

                break
            else:
                i+=1
        if i>math.sqrt(start) and start!=1:
            # print(start,end=' ')
            count+=1
        start+=1
    return count

def couter(fun):

    def inner(i,j):
        start=time.time()
        r=fun(i,j)
        end=time.time()
        print()
        print('耗时：', (end - start))
        return r,end-start
    return inner

def out(start,end):
    s=time.time()
    r=printPrime(start,end)
    e=time.time()
    print()
    print('耗时：', (e - s))
    return r,e-s
if __name__ == '__main__':

    printp=couter(printPrime)
    print(printp(1, 1000000))
    p=Pool(20)
    result_list=[]
    start=time.time()
    get_list=[]
    for i in range(20):
        get_list.append(p.apply_async(out,(1+50000*i,50000*(i+1))))

    for i in range(20):
        result_list.append(get_list[i].get())
    p.close()
    p.join()
    end=time.time()
    alltime=0
    count=0
    for i in result_list:
        alltime+=i[1]
        count+=i[0]
    print('--------',count,end-start)

    p = Pool(5)
    result_list = []
    start = time.time()
    get_list = []
    for i in range(5):
        get_list.append(p.apply_async(out, (1 + 200000 * i, 200000 * (i + 1))))

    for i in range(5):
        result_list.append(get_list[i].get())
    p.close()
    p.join()
    end = time.time()
    alltime = 0
    count = 0
    for i in result_list:
        alltime += i[1]
        count += i[0]
    print('--------', count, end - start)
















