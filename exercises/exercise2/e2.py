#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:e2.py
# author:dell
# datetime:2021/4/22 6:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 练习1
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# # -*- coding: utf-8 -*-
#
# # 测试:
# ******
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def createCounter():
#     def inner():
#         def inner1(i):
#             def inner2():
#                 return i
#             return inner2
#         fs=[]
#         for i in range(1,10):
#             fs.append(inner1(i))
#         return fs
#     return inner

# def inner():
#     def inner1(i):
#         def inner2():
#             return i
#         return inner2
#     fs=[]
#     for i in range(1,10):
#         fs.append(inner1(i))
#     return fs

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# def createCounter():
#     def inner(j):
#         def inner1():
#             return j
#         return inner
#     fs=[]
#     for i in range(1,10):
#         fs.append(inner(i))
#     return fs
# def createCounter():
#
#     # def counterA():
#     #     i+=1
#     #
#     #     return i;
#     # return counterA
#     i=0
#     def inner(j):
#         def CounterA():
#             return j+1
#         return CounterA
#
#
#
#
#
#
#     return inner(i)

def createCounter():
    def counterA():
        i=0
        def f(i):
            i=i+1
            return i
        return f(i)

    return counterA




if __name__ == '__main__':
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
    # # print(counterA())
    # f1,f2,f3=count()
    # print(f1())
