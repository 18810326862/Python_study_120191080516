from flask import Flask
from models import User
from flask import render_template,flash,request,abort

app = Flask(__name__)
app.secret_key='123'
@app.route('/123456')
def myfunc():
    return 'Hello World'
@app.route('/')
def hello_world():
    flash('Hello World')
    return render_template("消息提示.html")

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user=None
    if int(user_id)==1:
        user=User(1,'123')
    return render_template('判断语句.html',user=user)

@app.route('/users')
def user_list():
    users=[]
    for i in range(1,11):
        user=User(i,'me'+i)
        users.append(user)
    return render_template("循环语句.html",users=users)
@app.route('/one')
def one_base():
    return render_template("继承子类.html")

@app.route('/two')
def two_base():
    return render_template("继承子类1.html")

@app.route('/login',methods=['POST','GET'])
def login():
    form=request.form
    username=form.get('username')
    password=form.get('password')

    if not username:
        flash('please input username')
        return render_template('index.html')
    if not password:
        flash('please input password')
        return render_template('index.html')
    if username=='admin' and password=='123456':
        flash('login success')
        return render_template('index.html')
    else:
        flash('username or password is wrong')
        return render_template('index.html')


@app.errorhandler(404)
def not_fount():
    return render_template('404.html')

@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id)==1:
        return render_template('user.html')
    else:
        abort(404)
if __name__ == '__main__':
    app.run()
