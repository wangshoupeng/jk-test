# -*- coding:gbk -*-
'''
class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name+' has opened today')
		
	def open_restaurant(self):
		print(self.cuisine_type)
'''

'''
with open(file) as test:
	a = test.readlines()
print(a)
b = ''
for i in a:
	b += i.rstrip() 
print(b+'.....')
print(len(b))
'''
'''
b.replace('dmsuicdaod','66666666')
print(b+'.....')
while True:
	bri = input('�������ַ�����')
	if bri in b:
		print('����')
		break
	else:
		print('������')
'''
file = r'D:\geany\python_work\file_1.txt'

while True:
	name = input('����������������')
	if name == 'shoupeng':
		break
	else:
		with open(file,'a') as test1:
			test1.write(name+'\n')
with open(file,'r') as a:
	b = a.read()
	print(b)
	
	
	
	
	
