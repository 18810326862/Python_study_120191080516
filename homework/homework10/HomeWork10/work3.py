#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/5/22 9:13
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

'''2  设计一个留言版的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

3  对2中的表结构，用SQLAchemy模块来实现同样的操作；'''
#ID  text name1  date1  isdelete
import datetime
from sqlalchemy import create_engine,Column,Integer,DateTime,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationships
HOST='localhost'
USERNAME='root'
PASSWORD='123456'
DBNAME='python_test'
PORT=3306
engine=create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,HOST,PORT,DBNAME))
#print(engine)
BASE=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()
#print(session,type(session))
class BBS_1(BASE):
    __tablename__='bbs_1'
    ID=Column(Integer,primary_key=True,autoincrement=True)
    text=Column(String)
    name1=Column(String)
    date1=Column(DateTime)
    isdelete=Column(String)
    def __repr__(self):
        return"<{}  ID={},text={},name={},date={},isdelete={}>".format(__class__.__name__,self.ID,self.text,self.name1,self.date1,self.isdelete)


# datas=session.query(BBS_1)
# print(datas.count())
# for i in datas:
#     print(i)

# b1=session.query(BBS_1).filter(BBS_1.ID==1).one()
# session.commit()

# print(b1.ID)
# session.close()


# datas=session.query(BBS_1).all()
# for data in datas:
#     print(data.ID)
# session.close()

#ID  text name1  date1  isdelete
def myadd(text,name,isdelete):
    try:
        session.add(BBS_1(text=text,name1=name,isdelete=isdelete,date1=datetime.datetime.now()))
        session.commit()
    except:
        print('error')
    finally:
        session.close()

def mydelete(ID):
    try:
        data1=session.query(BBS_1).filter(BBS_1.ID==ID).first()
        session.delete(data1)
        session.commit()
    except:
        print('error')
    finally:
        session.close()

def myupdate(ID,text,name,isdelete):
    try:
        data1=session.query(BBS_1).filter(BBS_1.ID==ID).first()
        data1.name1=name
        data1.text=text
        data1.isdelete=isdelete
        session.add(data1)
        session.commit()

    except:
        print('error')
    finally:
        session.close()


def myfound(ID):
    try:

        datas=session.query(BBS_1).filter(BBS_1.ID==ID)
        for data in datas:
            print(data)


    except:
        print('error')
    finally:
        session.close()

if __name__ == '__main__':
    #myadd('123','小亮','no')
    #mydelete(4)
    #myupdate(1,'666','小小','no')
    myfound(1)


