#! user/bin/env python
#! _*_ coding:utf-8 _*_
# auther:王守鹏
import pymysql
import requests
db = pymysql.connect(host = 'localhost',user = 'root',passwd = 'root',port = 3306,db = 'db',charset = 'utf8')
cursor = db.cursor()
cursor.execute("select url_address from pachong limit 50")
DoutuList = cursor.fetchall()
print(DoutuList)
a = 1
for i in DoutuList:
    #print(i[0])
    url = i[0]
    response = requests.get(url)
    #print(response.content)
    f = open(r'C:\Users\shoupeng.wang\Desktop\images\image_{}.png'.format(a),'wb')
    print("开始写入第{}张图片".format(a))
    f.write(response.content)
    f.close()
    a += 1



