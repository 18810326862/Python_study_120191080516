#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:config.py
# author:dell
# datetime:2021/5/29 18:18
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'python_test'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
