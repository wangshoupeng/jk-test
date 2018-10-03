import xlrd
book = xlrd.open_workbook('app_student.xls')
sheet = book.sheet_by_index(0)
# sheet2 = book.sheet_by_name('shee1')
# print(sheet.cell(0,0).value) #指定sheet页里面行和lie获取数据
# print(sheet.cell(1,0).value) #指定sheet页里面行和lie获取数据
# print(sheet.row_values(0)) #这个获取到第几行的内容
# print(sheet.row_values(1)) #这个获取到第几行的内容
# print(sheet.nrows) #获取到excel里面总共有多少行
# for i in range(sheet.nrows):  #循环获取到每行数据
# 	print(sheet.row_values(i))
print(sheet.ncols)  #总共多少列
print(sheet.col_values(1)) #取第几列的数据


