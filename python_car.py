# -*- coding:GBK -*-
#import hello_world   #����hello_world�ļ�
#from hello_world import vccs_acct

def city_country(city,country,):
	print('�����ǣ�'+city.title()+', '+'�����ǣ�'+country.title())
while True:
	print('\nPlease tell me the city and the country you are in?')
	n_name = input('City :')
	s_name = input('Country: :')
	if  n_name == '' and s_name == '':
		print('��������к͹�����!')
		city_country('allnull','null')
	elif n_name == '':
		print('�����������!')
		city_country('beijing',s_name)
	elif s_name == '':
		print('�����������!')
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
