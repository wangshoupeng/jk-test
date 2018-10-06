# -*- coding:GBK -*-
#import hello_world   #导入hello_world文件
#from hello_world import vccs_acct

def city_country(city,country,):
	print('城市是：'+city.title()+', '+'国家是：'+country.title())
while True:
	print('\nPlease tell me the city and the country you are in?')
	n_name = input('City :')
	s_name = input('Country: :')
	if  n_name == '' and s_name == '':
		print('请输入城市和国家名!')
		city_country('allnull','null')
	elif n_name == '':
		print('请输入城市名!')
		city_country('beijing',s_name)
	elif s_name == '':
		print('请输入国家名!')
		city_country(n_name,'china')
	else:
		city_country(n_name,s_name)
		break
'''
def ccs_acct(start_name,last_name,middle_name=''):
	if middle_name:
		print(start_name+', '+last_name+', '+middle_name)
	else:
		full_name = start_name+', '+last_name
		print(full_name)
ccs_acct('shoupeng','meijuan')
'''
