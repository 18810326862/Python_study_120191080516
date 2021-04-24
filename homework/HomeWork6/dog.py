#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:dog.py
# author:dell
# datetime:2021/4/18 13:04
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 五  请写一个小游戏，人狗大站;  规则:
#     1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人);
#         人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#     2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#         人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
#     3   对战规则:
#      A  随机决定,谁先开始攻击;
#      B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
# 提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 在写一个fight模块
# （也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
from HomeWork6.person import Person
class Dog(object):
    # blood = 80
    # fight = 15
    allnoblood=False
    allnofight=False
    dog_list=[]
    def __init__(self,name):
        self.name=name
        self.blood=80
        self.fight=15
        Dog.dog_list.append(self)
    def attack(self,p):

        p.blood-=self.fight

        print('{}被{}攻击,{}当前血量为{}'.format(p.name,self.name,p.name,p.blood))

    def minattack(self,p):
        self.fight -= 3
        if(self.fight<0):
            self.fight=0
        print('{}被{}攻击,{}当前攻击力为{}'.format(self.name,p.name,self.name,self.fight))

    @classmethod
    def bloodjudge(cls):
        flag=0
        for i in Dog.dog_list:
            if(i.blood==0):
                flag+=1
        if(flag== len(Dog.dog_list)):
            return True
        else:
            return False



    @classmethod
    def fightjudge(cls):
        flag=0
        for i in Dog.dog_list:
            if(i.fight==0):
                flag+=1
        if(flag==len(Dog.dog_list)):
            return True
        else:
            return False


