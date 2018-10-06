# -*- coding:gbk -*-
import json
import os
from time import *
import re
'''
filepath=r'D:\geany\python_work\file_1.json'

while True:
	username = input('请输入您的姓名：')
	if username == 'q':
		break
	with open(filepath,'a') as a:
		b = json.dump(username,a)
	with open(filepath,'r') as c:
		d = c.read().title()
		print('文件中的姓名是：'+d)
		path = os.path.getsize(filepath)
		print(path)
		if path >= 100:
			with open(filepath,'w') as e:
				json.dump(username,e)
			with open(filepath) as y:
				f = y.read().title()
			print('重写：'+f)

def function(x):
	def function2(y):
		print(x+y)
	return function2
function2 = function(2)
function2(2)
'''
a = '发打发第三方'
'''
print('应该输出：90%')
print('班级的及格率是 %d%%：' % a)
print('应该输出：0090')
print('班级的及格率是 %04d：' % a)
print('应该输出：90.000000')
print('班级的及格率是 %f：' % a)
print('应该输出：90.0000000')
print('班级的及格率是 %.07f：' % a)
print('应该输出：90.00')
print('班级的及格率是 %. 02f：' % a)

姓名 = '王守鹏'
年龄 = 24
身高 = 180
QQ = 1451738852
Email = '@qq.com'
print('您的姓名是：%s---->\n\
您的年龄是：%d---->\n\
您的身高是：%d---->\n\
您的QQ是：%d---->\n\
您的Email是：%d%s；' \
% (姓名,年龄,身高,QQ,QQ,Email))

def counts(s):
	print('开始输出')
	while s >0:
		yield s
		s -= 1
c = counts(15)
list = []
for i in range(15):
	a = c.__next__()
	list.append(a)
print(list)
'''



