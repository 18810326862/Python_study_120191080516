#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:fight.py
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
from HomeWork6.dog import Dog

from random import randint
def fighttest():
    # Dog[3]={'dog1','dog2','dog3'}
    dog_list=[]
    person_list=[]
    for i in range(3):
        dog_list.append(Dog('dog{}'.format(i+1)))
    for i in range(2):
        person_list.append(Person('person{}'.format(i+1)))

    flag=randint(0,1)
    if flag==0:
        while True:
            i=randint(0,1)
            if(person_list[i].blood>0):
                j=randint(0,2)
                if dog_list[j].blood>0:
                    person_list[i].attack(dog_list[j])
                    dog_list[j].minattack(person_list[i])

            j=randint(0,2)
            if(dog_list[j].blood>0):
                i=randint(0,1)
                if person_list[i].blood>0:
                    dog_list[j].attack(person_list[i])
                    person_list[i].minattack(dog_list[j])




    else:

        while True:
            j = randint(0, 2)
            if (dog_list[j].blood > 0):
                i = randint(0, 1)
                if person_list[i].blood > 0:
                    dog_list[j].attack(person_list[i])
                    person_list[i].minattack(dog_list[j])

            i = randint(0, 1)
            if (person_list[i].blood > 0):
                j = randint(0, 2)
                if dog_list[j].blood > 0:
                    person_list[i].attack(dog_list[j])
                    dog_list[j].minattack(person_list[i])

            if(Dog.bloodjudge() or Person.bloodjudge() or
                    Dog.fightjudge()and not Person.bloodjudge() or Person.fightjudge() and not Dog.bloodjudge()):
                break

if __name__ == '__main__':
    fighttest()
