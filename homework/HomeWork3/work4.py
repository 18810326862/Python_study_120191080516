#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work4.py
# author:dell
# datetime:2021/4/13 16:16
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 4  编写装饰器来实现，对目标函数进行装饰,计算函数的运行耗时，
#     分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
import time
import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

#A
def outerA(func):
    def innerA():
        start=time.time()
        func()
        end=time.time()
        print('执行时间',(end-start))
    return innerA

@outerA
def printPrimeA():
    for i in range(2,20000):
        if isPrime(i):
            print(i,' ')


#B

def outerB(func):
    def innerB():
        start=time.time()
        temp=func()
        end=time.time()
        print('执行时间',(end-start))
        return temp
    return innerB
@outerB
def printPrimeB():
    sum=0
    for i in range(2,10000):
        if isPrime(i):
            sum+=1
    return sum
#C



def outerC(func):
    def innerC(*args,**kwargs):
        start=time.time()
        temp=func(*args,**kwargs)
        end=time.time()
        print('执行时间',(end-start))
        return  temp
    return innerC

@outerC
def printPrimeC(M):
    if M<2:
        raise Exception('输入大于1')
        return
    sum=0
    for i in range(2,M):
        if isPrime(i):
            sum+=1
    return sum

if __name__ == '__main__':
    #printPrimeA()
    print(printPrimeB())
    print(printPrimeC(1000))
