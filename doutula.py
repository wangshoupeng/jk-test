#! _*_ coding:utf-8 _*_
import requests
import re
import pymysql
#连接数据库
db = pymysql.connect(host = 'localhost',user = 'root',passwd = 'root',port = 3306,db = 'db',charset = 'utf8')
# #创建游标
cursor = db.cursor()
# cursor.execute("insert into pachong(`url_name`,`url_address`)values('2','3')")
# db.commit()
# print(cursor.fetchall())

def getImagesList(page):
    #date = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = 'https://www.fabiaoqing.com/bqb/lists/page/{}.html'.format(page)
    html = requests.get(url=url).text
    reg = r'data-original="(.*?)" alt="(.*?) -.*?"'
    reg = re.compile(reg,re.S)
    getImagesLists = re.findall(reg,html)
    for i in getImagesLists:
        url_adress = i[0]
        url_name = i[1]
        if len(url_adress)<=255 and len(url_name)<=255:
            try:
                cursor.execute("insert into pachong(`url_name`,`url_address`)values('{}','{}')".format(url_name,url_adress))
                print("正在保存第{}页 :\t{}\t{}".format(page, url_adress, url_name))
                db.commit()
            except:
                pass
        else:
            pass
        #print(url_adress,url_name)

for j in range(0,31):
    print("正在打印第{}页".format(j))
    getImagesList(j)

    print("第{}页打印结束".format(j))
#关闭游标
cursor.close()
#关闭数据库
db.close()