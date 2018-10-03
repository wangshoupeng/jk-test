import xlrd
from xlutils import copy
book = xlrd.open_workbook('app_student.xls')
#先用xlrd模块，打开一个excel
new_book = copy.copy(book)
#通过xlutils这个模块里面copy方法，复制一份excel
sheet = new_book.get_sheet(0) #获取sheet页
lis = ['编号','名字','性别','年龄','地址','班级','手机号','金币']
for col,filed in enumerate(lis):
	sheet.write(0,col,filed)

new_book.save('app_student.xls')
