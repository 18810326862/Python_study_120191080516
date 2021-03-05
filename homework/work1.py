#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/3/4 16:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import math
def isPrime(count):
    i = 2;
    is_prime=1;
    while i<=math.sqrt(count):
        if count%i==0:
            is_prime=0

            break

        i=i+1
    return is_prime


jishu=[]
oushu=[]
zhishu=[]
chushu=[]
i=0
while(i<=50):
    if i%2==0:
        oushu.append(i)
    if i%2!=0:
        jishu.append(i)
    if isPrime(i)==1:
        zhishu.append(i)
    if i%2==0&i%3==0:
        chushu.append(i)
    i=i+1
print("0-50之间的奇数有"+"\n")
for i in jishu:
    print(str(i)+",",end=" ")
print("\n0-50之间的偶数有\n")
for i in oushu:
    print(str(i)+",",end=" ")
print("\n0-50之间的质数有\n")
for i in zhishu:
    print(str(i)+",",end=" ")
print("\n0-50之间能被2和3同时整除的数\n")
for i in chushu:
    print(str(i)+",",end=" ")
