#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:work6.py
# author:dell
# datetime:2021/4/18 13:03
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 六  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;

import pickle


class StudentInfo():
    sclass = ''
    sid = ''
    sname = ''
    spythonscore = 0

    def __init__(self, sclass, sid, sname, spythonscore):
        self.sclass = sclass
        self.sid = sid
        self.sname = sname
        self.spythonscore = spythonscore

    # @property
    # def spythonscore(self):
    #     return self.spythonscore
    #
    # @spythonscore.setter
    # def spythonscore(self,score):
    #     if not isinstance(score, int):
    #         raise ValueError('score must be an integer!')
    #     if score < 0 or score > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self.spythonscore=score

    def __eq__(self, other):
        if self.spythonscore == other.spythonscore and self.sname == other.sname and \
                self.sclass == other.sclass and self.sid == other.sid:
            return True
        else:
            return False

    def printInfo(self):
        print(f'name:{self.sname},id:{self.sid},class:{self.sclass},score:{self.spythonscore}')


def addinfo(student):
    # info_list=[]
    # with open('StudentInfo.txt','rb')as f:
    #     while True:
    #         try:
    #             info_list.append(pickle.load(f))
    #
    #
    #         except EOFError:
    #             break
    # with open('StudentInfo.txt','wb')as f:
    #     for i in info_list:
    #         pickle.dump(i,f)
    #     pickle.dump(student,f)
    with open('StudentInfo.txt', 'ab')as f:
        pickle.dump(student, f)


def deleteInfoByObject(student):
    info_list = []
    flag = False
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break
    for i in info_list:
        if i == student:
            info_list.remove(i)
            flag = True
            break

    if (flag):
        with open('StudentInfo.txt', 'wb')as f:
            for i in info_list:
                pickle.dump(i, f)
    else:
        print('未找到相关信息')


def deleteInfoByIndex(index):
    info_list = []
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break

    if index > len(info_list):
        print('位置有误')
        return
    info_list.pop(index - 1)
    with open('StudentInfo.txt', 'wb')as f:
        for i in info_list:
            pickle.dump(i, f)


def foundInfoByIndex(index):
    info_list = []
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break

    if index > len(info_list):
        print('位置有误')
        return
    return info_list[index - 1]


def foundInfoByObject(student):
    info_list = []
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break
    i = 0
    while (i < len(info_list)):
        if (info_list[i] == student):
            return i
        i += 1

    if (i == len(info_list)):
        print('未找到')
        return -1


def updateInfo(index, student):
    info_list = []
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break
    info_list[index - 1] = student

    with open('StudentInfo.txt', 'wb')as f:
        for i in info_list:
            pickle.dump(i, f)


def insertInfo(index, student):
    info_list = []
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break

    info_list.insert(index - 1, student)

    with open('StudentInfo.txt', 'wb')as f:
        for i in info_list:
            pickle.dump(i, f)


def printInfo():
    info_list = []
    with open('StudentInfo.txt', 'rb')as f:
        while True:
            try:
                info_list.append(pickle.load(f))


            except EOFError:
                break

    for i in info_list:
        i.printInfo()


def menu():
    while True:
        print('1增加学生信息')
        print('2删除学生信息(按编号)')
        print('3查找学生信息(按编号)')
        print('4修改学生信息(按编号)')
        print('5插入学生信息(按编号)')
        print('6输出学生信息')
        print('0退出')
        i = input('请选择')
        if i.strip() == '1':
            student = StudentInfo(input('class').strip(), input('id').strip(), input('name').strip(),
                                  input('score').strip())
            addinfo(student)
        elif i.strip() == '2':
            index = input('请输入删除位置(从1开始)')
            deleteInfoByIndex(int(index))
        elif i.strip() == '3':
            index = input('请输入查找位置')
            student = foundInfoByIndex(int(index))
            student.printInfo()


        elif i.strip() == '4':
            index = input('请输入修改位置')
            student = StudentInfo(input('class').strip(), input('id').strip(), input('name').strip(),
                                  input('score').strip())
            updateInfo(int(index), student)

        elif i.strip() == '5':

            index = input('请输入插入位置')
            student = StudentInfo(input('class').strip(), input('id').strip(), input('name').strip(),
                                  input('score').strip())
            insertInfo(int(index), student)

        elif i.strip() == '6':
            printInfo()

        elif i.strip() == '0':
            break

        else:
            print('输入有误')


# s1=StudentInfo('class','id','name')
# s2=StudentInfo('class','id','name')
# print(s1==s2)
# c++

if __name__ == '__main__':
    # stu1=StudentInfo('1','1','1',99)
    # stu2=StudentInfo('2','2','2',99)
    # stu3=StudentInfo('3','3','3',99)
    # addinfo(stu1)
    # addinfo(stu2)
    # addinfo(stu3)
    menu()
