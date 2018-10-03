#! user/bin/env python
#! _*_ coding:utf-8 _*_
# auther:王守鹏
import time as t
import datetime
from flask import Flask
from flask import render_template#模板引擎  渲染引擎
# server = Flask(__name__)
# @server.route('/')
# def login():
#     return '王守鹏'
# @server.route('/index',methods=['GET','POST'])#flask默认是get请求
# def index():
#     return '1'
# if __name__ == '__main__':
#     server.run(debug=True)


'''
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('API.html')

if __name__ == '__main__':
    app.run(debug=True,port=1000)

'''
print(t.ctime())
print(t.localtime())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%m:%S'))
print(t.strftime('%Y-%m-%d %H:%m:%S'))
print(datetime.datetime.now().strftime('%F %T'))