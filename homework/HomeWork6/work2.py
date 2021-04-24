#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/4/16 12:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 二 定义一个学生Student类。有下面的类属性：
# # 1 姓名 name
# # 2 年龄 age
# # 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# # 类方法：
# # 1 获取学生的姓名：get_name() 返回类型:str
# # 2 获取学生的年龄：get_age() 返回类型:int
# # 3 返回3门科目中最高的分数。get_course() 返回类型:int
# # 写好类以后，可以定义2个同学测试下:

class Student:
    name = ''
    age = 0
    score = (0,0,0)
    def __init__(self,name,age,score):
        self.name=name;
        self.age=age;
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score)


if __name__ == '__main__':
    student1=Student('1',20,(90,90,90))
    student2=Student('2',20,(90,92,99))
    student3=Student('3',20,(98,99,96))

    print(student1.get_course())
    print(student2.get_course())

