#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/4/16 12:33
# software: PyCharm
'''
this is functiondescription
'''


# import module your need

# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#        实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class Dog(object):
    dog_list = [{'color': 'blue', 'num': 30, 'price': 100},
                {'color': 'red', 'num': 20, 'price': 200.6}, {'color': 'green', 'num': 30, 'price': 150}]

    def __init__(self, color):
        self.color = color

    def buyDog(self):
        num = 0
        for i in Dog.dog_list:
            if i['color'] == self.color:
                num = i['price']
                i['num'] -= 1
        print('color:%s,price:%s' % (self.color, num))


if __name__ == '__main__':
    dog1 = Dog('red')
    dog2 = Dog('blue')
    dog3 = Dog('green')
    dog1.buyDog()
    dog2.buyDog()
    dog3.buyDog()
    print(Dog.dog_list)
