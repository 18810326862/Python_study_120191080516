#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:work1.py
# author:dell
# datetime:2021/5/19 21:53
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

'''# 1 数据库查询练习：
#    针对我们给大家的2张表（学生表和班级表），做以下查询；（查询脚本放在一个文件中，
#    创建一个SQL文件夹，放到这个里面，最有提交到代码仓库）
# ① 查询所有男生的姓名，年龄，所在班级名称；
# ② 查询所有查询编号小于4或没被删除的学生；
# ③ 查询姓黄并且“名”是一个字的学生；
# ④ 查询编号是1或3或8的学生
# ⑤ 查询编号为3至8的学生
# ⑥ 查询未删除男生信息，按年龄降序
# ⑦  查询女生的总数
# ⑧  查询学生的平均年龄
# ⑨ 分别统计性别为男/女的人年龄平均值
# ⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
#         | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
# 	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
# 	| 中性   | 金星                                                       |
# 	| 保密   | 凤姐
'''

import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", passwd="123456", db="python_test")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# cursor.execute('select * from studentinfo')
# cursor.execute('select * from studentinfo where ID=1')
# for i in cursor:
#     print(i)
# def quest1():
#     cursor.execute('select name,age,classID where sex="男"')
# cursor.execute("select name,age,classID from studentinfo where sex='男'")
# for i in cursor:
#     print(i)
classIDdict = {}
cursor.execute('select * from classinfo')
for tup1 in cursor:
    classIDdict[tup1[0]] = tup1[1]


# print(classIDdict)
# ① 查询所有男生的姓名，年龄，所在班级名称；
def quest1():
    cursor.execute("select name,age,classID from studentinfo where sex='男'")
    print('name    age     class')
    for tup in cursor:
        print(f'{tup[0]}    {tup[1]}    {classIDdict[tup[2]]}')


# ② 查询所有查询编号小于4或没被删除的学生；
def quest2():
    cursor.execute("select * from studentinfo where ID<4")
    print('ID   name   age   class     sex')
    for tup in cursor:
        print(f'{tup[0]}    {tup[1]}   {tup[2]}    {classIDdict[tup[3]]}   {tup[4]}')


# ③ 查询姓黄并且“名”是一个字的学生；
def quest3():
    cursor.execute("select * from studentinfo where REGEXP_LIKE(name,'[黄]{1}.$')")
    print('ID   name   age   class     sex')
    for tup in cursor:
        print(f'{tup[0]}    {tup[1]}   {tup[2]}    {classIDdict[tup[3]]}   {tup[4]}')


# ④ 查询编号是1或3或8的学生
def quest4():
    cursor.execute("select * from studentinfo where ID=1||ID=3||ID=8")
    for tup in cursor:
        print(f'{tup[0]}    {tup[1]}   {tup[2]}    {classIDdict[tup[3]]}   {tup[4]}')


# ⑤ 查询编号为3至8的学生
def quest5():
    cursor.execute("select * from studentinfo where ID>=3&&ID<=8")
    for tup in cursor:
        print(f'{tup[0]}    {tup[1]}   {tup[2]}    {classIDdict[tup[3]]}   {tup[4]}')


# ⑥ 查询未删除男生信息，按年龄降序
def quest6():
    cursor.execute("select * from studentinfo where sex='男' order by age desc ")
    for tup in cursor:
        print(f'{tup[0]}    {tup[1]}   {tup[2]}    {classIDdict[tup[3]]}   {tup[4]}')


# ⑦  查询女生的总数
def quest7():
    cursor.execute("select sex from studentinfo where sex='女'")
    num = 0
    for i in cursor:
        num += 1
    print(f'女生总数为:{num}')


# ⑧  查询学生的平均年龄
def quest8():
    cursor.execute('select age from studentinfo')
    count = 0
    num = 0
    for age in cursor:
        count += age[0]
        num += 1
    print(f'平均年龄为:{count / num}')


# ⑨ 分别统计性别为男/女的人年龄平均值
def quest9():
    cursor.execute("select age from studentinfo where sex='男'")
    allage = 0
    num = 0
    for age in cursor:
        allage += age[0]
        num += 1
    print(f'男生平均年龄为:{allage / num}')
    cursor.execute("select age from studentinfo where sex='女'")
    allage = 0
    num = 0
    for age in cursor:
        allage += age[0]
        num += 1
    print(f'女生平均年龄为:{allage / num}')


# ⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
#         | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
# 	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
# 	| 中性   | 金星                                                       |
# 	| 保密   | 凤姐

def quest10():
    cursor.execute("select sex from studentinfo group by sex")
    sexlist=[]
    for sex in cursor:
        sexlist.append(sex[0])
        # print(sex[0])
    for sex in sexlist:
        cursor.execute(f"select name from studentinfo where sex='{sex}'")
        print('|'+sex+'|',end=' ')
        for name in cursor:
            print(name[0],end=',')
        print()


if __name__ == '__main__':
    # quest1()
    #    quest2()
    #    quest3()
    #    quest4()
    #    quest5()
    #   quest6()
    #    quest7()
    quest8()
    #quest9()
    #quest10()
    db.close()

#     cursor.execute('select count(*)')
#     for i in cursor:
#         print(i)
