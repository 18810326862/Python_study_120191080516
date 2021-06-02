#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework_test.py
# author:dell
# datetime:2021/5/29 17:04
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object('config')
db = SQLAlchemy(app)


class NoteList(db.Model):
    __tablename__ = 'notelist'

    # 表的结构:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(), nullable=False)
    isdone = db.Column(db.String())


def model_to_dict(result):
    from collections.abc import Iterable
    # 转换完成后，删除 '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')


@app.route('/', methods=['POST', 'GET'])
def home():
    # if request.method == 'POST':
    #     pass
    datas = db.session.query(NoteList).all()
    datas = model_to_dict(datas)
    return render_template('note_templates.html', notes=datas)


@app.route('/add', methods=['POST', 'GET'])
def add():
    datas = db.session.query(NoteList).all()
    datas = model_to_dict(datas)
    number = len(datas)
    title = request.form['title']
    note1 = NoteList()
    note1.title = title
    note1.isdone = 'no'
    note1.id = number+1
    db.session.add(note1)
    db.session.commit()
    datas = db.session.query(NoteList).all()
    datas = model_to_dict(datas)
    return render_template('note_templates.html', notes=datas)


@app.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    # myform=request.form
    # print(myform)
    #print(request.args)
    title = request.form['title' + id]
    #print(title)
    #print(request.form['done'+id])
    note1 = db.session.query(NoteList).filter(NoteList.id == id).first()
    note1.title = title
    #
    # if request.form['done'+id] == 'Done':
    #     note1.isdone = 'no'
    # else:
    #     note1.isdone = 'yes'

    db.session.commit()
    datas = db.session.query(NoteList).all()
    datas = model_to_dict(datas)
   # datas = model_to_dict(datas)
    return render_template('note_templates.html', notes=datas)


@app.route('/search', methods=['POST', 'GET'])
def search():
    data = request.form['search']
    datas = db.session.query(NoteList).filter(NoteList.title.like(f"%{data}%")).all()



    return render_template('note_templates.html', notes=datas,text=data)


@app.route('/remove/<id>', methods=['POST', 'GET'])
def remove(id):
    note1 = db.session.query(NoteList).filter(NoteList.id == id).first()
    db.session.delete(note1)
    db.session.commit()
    datas = db.session.query(NoteList).all()
    datas = model_to_dict(datas)
    return render_template('note_templates.html', notes=datas)


@app.route('/all', methods=['POST', 'GET'])
def all():
    return redirect('/')

@app.route('/done/<id>',methods=['POST','GET'])
def done(id):
    note1 = db.session.query(NoteList).filter(NoteList.id == id).first()
    if note1.isdone == 'yes':
        note1.isdone = 'no'
    else:
        note1.isdone = 'yes'
    db.session.commit()
    datas = db.session.query(NoteList).all()
    datas = model_to_dict(datas)
    # datas = model_to_dict(datas)
    return render_template('note_templates.html', notes=datas)



if __name__ == '__main__':
    app.run()
