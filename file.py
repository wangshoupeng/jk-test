# -*- coding:gbk -*-
import json
import os
from time import *
import re
'''
filepath=r'D:\geany\python_work\file_1.json'

while True:
	username = input('����������������')
	if username == 'q':
		break
	with open(filepath,'a') as a:
		b = json.dump(username,a)
	with open(filepath,'r') as c:
		d = c.read().title()
		print('�ļ��е������ǣ�'+d)
		path = os.path.getsize(filepath)
		print(path)
		if path >= 100:
			with open(filepath,'w') as e:
				json.dump(username,e)
			with open(filepath) as y:
				f = y.read().title()
			print('��д��'+f)

def function(x):
	def function2(y):
		print(x+y)
	return function2
function2 = function(2)
function2(2)
'''
a = '���򷢵�����'
'''
print('Ӧ�������90%')
print('�༶�ļ������� %d%%��' % a)
print('Ӧ�������0090')
print('�༶�ļ������� %04d��' % a)
print('Ӧ�������90.000000')
print('�༶�ļ������� %f��' % a)
print('Ӧ�������90.0000000')
print('�༶�ļ������� %.07f��' % a)
print('Ӧ�������90.00')
print('�༶�ļ������� %. 02f��' % a)

���� = '������'
���� = 24
��� = 180
QQ = 1451738852
Email = '@qq.com'
print('���������ǣ�%s---->\n\
���������ǣ�%d---->\n\
��������ǣ�%d---->\n\
����QQ�ǣ�%d---->\n\
����Email�ǣ�%d%s��' \
% (����,����,���,QQ,QQ,Email))

def counts(s):
	print('��ʼ���')
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



