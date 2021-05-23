#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work2.py
# author:dell
# datetime:2021/5/21 22:35
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

'''2  设计一个留言版的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；'''
#ID  text name1  date1  isdelete

import pymysql
import datetime
db=pymysql.connect(host='localhost',user='root',passwd='123456',db='python_test')
cursor=db.cursor()
# cursor.execute('select * from BBS_1')
# for i in cursor:
#     print(i)

def myadd(text,name1,isdelete):
    try:
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(dt)
        cursor.execute("insert into bbs_1(text,name1,date1,isdelete) values ('%s','%s','%s','%s')"%(text,name1,dt,isdelete))
        db.commit()
        print('插入成功')
    except:
         print('error')
         db.rollback()
    finally:
         db.close()
def mydelete(ID):
    try:
        cursor.execute("delete from bbs_1 where ID='%s'"%ID)
        db.commit()
        print('删除成功')
    except:
        print('error')
    finally:
        db.close()

def myupdate(text,name1,isdelete,ID):
    try:
        cursor.execute("update bbs_1 set text='%s',name1='%s',isdelete='%s' where ID='%s'"%(text,name1,isdelete,ID))
        db.commit()
        print('更新成功')
    except:
        print('error')
    finally:
        db.close()

def myfound(ID):
    try:
        cursor.execute(f"select * from bbs_1 where ID='{ID}'")

        for data in cursor:
            print(f"{data[0]}  {data[1]}  {data[2]}  {data[3]} {data[4]}")
    except:
        print('error')
    finally:
        db.close()



if __name__ == '__main__':
    # myadd('lalala','小黄','no')
    #mydelete(2)
    #myupdate('bbb','小兰','no',1)
    myfound(1)