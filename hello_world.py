# -*- coding:GBK -*-
names = list(range(1,11))
print(names)
'''
def vccs_acct(names,*toppings):
	for s in toppings:
		print(s.upper())
		print(s.lower())
		print(s.title())
vccs_acct('shoupeng.wang','meijuan.cai','chao.wang','yang.xu')

#列表：
names = ['shoupeng.wang','meijuan.cai','chao.wang','yang.xu']
print(names[1].title()+', wufafuyue\n')
names[1] = 'guobing.wu'
for dada in names:
	print(dada.title()+', ganjinlaiba\n')
names.insert(0,'xiaonan.liu')
print(names)
names.append('heng.wang')
print(names)
list = []
for i in names:
	print(i.title()+', jiuchanile')
while len(names) > 2:
	greater_than = names.pop()
	list.append(greater_than)
print(names)
print(list)
del names[:]
print(names)

for Surplus in names:
	print('Invitation:  '+Surplus)
for Eject in list:
	print(Eject.title()+', Sorry')

#字典：
Dictionaries = {'names':'car','bay':'cicle'}
print(Dictionaries.keys())
print(Dictionaries.values())
print(Dictionaries.items())
print(Dictionaries)
'''


