#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:work3.py
# author:dell
# datetime:2021/4/18 12:32
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass(object):
    def __init__(self,dict):
        self.dict=dict
    def del_dict(self,key):
        if self.dict[key] in self.dict.keys():
            del self.dict[key]


    def get_dict(self,key):
        if self.dict[key] in self.dict.keys():
            return self.dict[key]
        else :
            return"not found"

    def get_key(self):
        return list(self.dict.keys())

    def update_dict(self,mydict):
        self.dict.update(mydict)
        return list(self.dict.values())

if __name__ == '__main__':
    dictclass1=dictclass({1:1,2:2,3:3})
    print(dictclass1.update_dict({3: 3, 4: 4, 5: 5}))

