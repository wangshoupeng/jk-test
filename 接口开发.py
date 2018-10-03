import flask,json
# __name__,代表当前这个python文件
server = flask.Flask(__name__) #把咱们当前这个python文件，当做一个服务
# def my_db(sql):
# 	import pymysql
# 	coon = pymysql.connect(
# 		host='118.24.3.40', user='jxz', passwd='123456',
# 		port=3306, db='jxz', charset='utf8')
# 	cur = coon.cursor() #建立游标
# 	cur.execute(sql)#执行sql
# 	if sql.strip()[:6].upper()=='SELECT':
# 		res =  cur.fetchall()
# 	else:
# 		coon.commit()
# 		res = 'ok'
# 	cur.close()
# 	coon.close()
# 	return res


@server.route('/index',methods=['get'])
def index():
	res = {'msg':'这是我开发的第一个接口','msg_code':0}
	return json.dumps(res,ensure_ascii=False)

@server.route('/reg',methods=['post'])
def reg():
	username = flask.request.values.get('username')#
	pwd = flask.request.values.get('passwd')
	print('username..',username)
	if username and pwd:
		sql = 'select * from my_user where username="%s";'%username
		# res = my_db(sql)
		if my_db(sql):
			res = {'msg':'用户已存在','msg_code':2001}
		else:
			insert_sql = 'insert into my_user (username,passwd,is_admin) values ("%s","%s",0);'%(username,pwd)
			my_db(insert_sql)
			res = {'msg':'注册成功！','msg_code':0}
	else:
		res = {'msg':'必填字段未填，请查看接口文档！','msg_code':1001}
		# 1001必填字段未填
	return json.dumps(res,ensure_ascii=False)

server.run(port=7777,debug=True,host='0.0.0.0')  #debug=True，改了代码之后，不用重启它会自动帮你重启
# host=0.0.0.0表示别人访问的时候，用你的ip就可以访问了。
# 127.0.0.1
# 192.168.
#脚本
