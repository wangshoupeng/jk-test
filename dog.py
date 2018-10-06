# -*- coding:GBK -*-
class Dog():
	"""一次尝试模拟小狗"""
	def __init__(self,name,age):
		self.last = name
		self.first = str(age)
	def sit(self):
		print(self.last.title()+', '+self.first+' '+str(self.rabbit)+', is now sitting')
	def roll_over(self):
		print(self.last+', rolled over')
	def full_gas(self):
		print('abc ')
class Batery():
	def __init__(self,batery_size=70):
		self.batery_size = batery_size
	def describe_batery(self):
		print(str(self.batery_size)+', rolled over')
class Car(Dog):
	def __init__(self,name,age):
		super().__init__(name,age)
		self.rabbit = 0
		self.batery = Batery()
	def full_gas(self):
		print('ok ')
my_car = Car('whille','6')

my_car.batery.describe_batery()
	

		
	
