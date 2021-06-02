#!/usr/bin/env python
#-*- coding:utf-8 -*-

# file:login.py
# author:dell
# datetime:2021/5/29 9:02
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

from flask import Flask,request,render_template,redirect

app=Flask(__name__)

@app.route("/user",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username=="user" and password=="password":
            return redirect("http://www.baidu.com")
        else:
            message="Failed Login"
            return render_template('login.html',message=message)
        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)