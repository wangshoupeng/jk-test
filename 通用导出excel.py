import pymysql,xlwt
def export_excel(table_name):
	host, user, passwd, db = '118.24.3.40', 'jxz', '123456', 'jxz'
	coon = pymysql.connect(user=user, host=host, port=3306, passwd=passwd, db=db, charset='utf8')
	cur = coon.cursor()  # 建立游标,指定cursor类型返回的是字典
	sql = 'select * from %s ;'%table_name
	cur.execute(sql)  # 执行sql

	print(cur.description)

	fileds = [filed[0] for filed in cur.description]  #所有的字段
	all_data = cur.fetchall()
	book = xlwt.Workbook()
	sheet  = book.add_sheet('sheet1')
	for col,filed in enumerate(fileds):   #写表头的
		sheet.write(0,col,filed)
	row = 1  #行数
	for data in all_data:  #行
		for col, filed in enumerate(data):  # 控制列
			sheet.write(row, col, filed)
		row+=1#每次写完一行，行就加1
	book.save('%s.xls'%table_name)



export_excel('app_student')


