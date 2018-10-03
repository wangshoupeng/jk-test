#! _*_ coding:utf-8 _*_
# import math
import random
import numpy as np
import pandas as pd
import time
import threading
import turtle
import requests
import re
import pytesseract
import PIL
import xlwt
import xlsxwriter
import math
import xlrd #读Excel
'''
def function(x):
    def function2(y):
        return x+y
    return x
    print('函数回调成功')
    return function2
'''

#随机生成[0,1)之间的小数
#print(random.random())
#随机生成[1,10)之间的整数
#print(random.choice(range(10)))
#print(random.randrange(1,100))
#print(random.uniform(8,9))
#list = [1,2,3,4,5,]
#可以对列表无序排序
#random.shuffle(list)
#print(list)
#随机输出[3,9]之间的小数
#print(random.uniform(3,9))
#print(int("-123"))
#数学功能：
#取绝对值  abs(n)
#print(abs(-4.23))
#求X的Y次方
#print(pow(2,5))
#四舍五入(整数),round(x,[n]),[n]代表保留到小数点后几位，可有可无，如果没有则保留整数
#print(round(3.55))
#四舍五入(保留小数点后几位)
#print(round(3.4531436,3))
#向上取整
#print(math.ceil(18.1))
#向上取整
#print(math.floor(18.1))
#开平方
#print(math.sqrt(16))
'''
list = [valus for valus in range(1,101)]
for i in list:
    if i % 2 == 0:
        print("偶数为：",i)
    else:
        print("基数为：",i)
'''
#永久排序（升序 ）
#a.sort()
#永久倒叙排列
#a.sort(reverse=True)
#临时排序
#sorted(reverse=True(a))
#倒叙排列
# reversed(a)
# print(a[-1])
# print(5|7)

#拷贝：
#栈区：系统自动分配，程序运行的结束 终点能够释放内存空间
#堆区：需要程序员手动开辟，手动释放内存
#浅拷贝 (浅拷贝的时候修改list2的值，list2的值也会被修改)
#list1 = [1,2,3,4,5,6,7,8,9,10]
#list2 = list1
#list1[1] = 200
#print(list1)
#print(list2)
#浅拷贝的时候两个列表的ID号是一样的
#print(id(list1))
#print(id(list2))

#深拷拷贝：（内存拷贝）
#list3 = [1,2,3,4,5,6]
#list4 = list3.copy()
#list4[2] = 100
#print(list3)
#print(list4)
#print(id(list3))
#print(id(list4))
#空格处理
#str = "     fanning is my leader       "
#print(str)
#print(str.strip())
#print(str.lstrip())
#print(str.rstrip())
#（布尔类型）判断是小写 ，如果是小写，返回True，否则返回False
# print(str.strip().islower())
# #（布尔类型）判断是大写 ，如果是大写，返回True，否则返回False
# print(str.strip().isupper())

# while True:
#     age = int(input("请输入您的年龄："))
#     if age < 12:
#         print("%d岁还是未成年" % age)
#     elif age >=12 and age < 24:
#         print("%d岁是未婚" % age)
#     elif age >=24 and age <= 30:
#         print("%d岁是中年男子" % age)
#     else:
#         break
# for index,m in enumerate([22,58,69,53,485]):
#     print(index,m)

# a = {"a":100,"b":200,"c":100}
# for key,value in a.items():
#     if value==100:
#         print(key,end='\t')
#乌龟画图
# boot = turtle.Turtle()#创建一个海龟对象
# boot.pu()#抬起笔尖=up()
# boot.goto(-200,200)
# boot.speed(5)#设置海龟速度
# boot.pensize(1)#设置笔尖粗细
# boot.pencolor('green')#设置笔尖颜色
# boot.pd()#落下笔尖=down()
# for i in range(4):
#     boot.fd(100)
#     boot.rt(90)
# boot.fd(50)
# boot.rt(90)
# boot.fd(100)
# boot.bk(50)
# boot.rt(90)
# boot.fd(50)
# boot.bk(100)
# boot.pu()
# boot.goto(0,0)#移动海龟坐标
# boot.pd()
# #填充颜色
# boot.begin_fill()#开始填充
# boot.fillcolor('blue')#要填充的颜色
# boot.circle(100)#要填充颜色的图形
# boot.end_fill()#结束填充
# boot.undo()#撤销上一次操作
# boot.hideturtle()#影藏海龟对象
# time.sleep(2)
# boot.showturtle()#显示海龟
# turtle.mainloop()#或者turtle.done()也可以
#文件读写
# f = open(r'C:\Users\shoupeng.wang\Desktop\自动化\wsp.csv','w')
# f.seek(1024*1024*1-1)
# f.write('姓名,年龄,性别\t')
# f.write('姓名,年龄,性别\n')
# name = ['王超','王守鹏','范宁','幺莉',]
# age = ['15','16','17','18']
# sex = ['男','男','女','女',]
# for i,j,k in zip(name,age,sex):
#     f.write('%s,%s,%s\n' % (i,j,k))
# f.close()
#数据分析
# df_dict = {"a":[1,2,3,4,5],"b":["a","b","c","d","e"]}
# df = pd.DataFrame(df_dict)
# print(df)
# names = ["D","G","A","E"]
# data = np.random.randint(0,100,(4,4))
# # #print(data)
# data1 = pd.DataFrame(data=data,index=("%s" % i for i in names),columns=("python","C++","Shell","Java"))
# print(data1)
#print(data1.dtypes)#查看每列数据类型
#print(data1.head(2))#查看前两行数据
# print(data1.index)#行名称
# print(data1.columns)#列名称
#print(data1.tail(2))#c查看最后两行数据
# print(data1.values)#查看数据（值）=上面的print(data)

#以下排序方法还有问题，有待研究
#print(data1.sort_values(by="D",axis=1,ascending=True))#根据第一行数据从左至右升序排序，
#print(data1.sort_values(by="D",axis=1,ascending=False))#根据第一行数据从左至右倒序排序，
# print(data1.sort_index(axis=0,ascending=True))#升序，根据行名称排序
# print(data1.sort_index(axis=1,ascending=False))#倒序，根据行名称排序，


# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# header = {'Host': 'www.lagou.com',
#         'Connection': 'keep-alive',
#         'Content-Length': '26',
#         'Origin': 'https://www.lagou.com',
#         'X-Anit-Forge-Code': '0',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'X-Requested-With': 'XMLHttpRequest',
#         'X-Anit-Forge-Token': 'None',
#         'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Cookie': 'JSESSIONID=ABAAABAAAFCAAEGE10474775ACF7363A85CACE43AF4DB33; user_trace_token=20180718224058-c05824cc-8a80-4456-9c4c-dc15723430e2; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531924874; X_HTTP_TOKEN=8fa3fc72facf0c978de9b5f5fd8ef3e5; _ga=GA1.2.1422147910.1531924961; _gid=GA1.2.1887919394.1531924961; LGSID=20180718224237-d0a940d4-8a98-11e8-9e0d-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D111.194.50.90; LGUID=20180718224237-d0a94345-8a98-11e8-9e0d-5254005c3644; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531925158; SEARCH_ID=ae876176f360451fa5730f52ac3ef38a; LGRID=20180718224604-4c16c9a6-8a99-11e8-9cea-525400f775ce' \
#         }
# for n in range(1,11):
#     print('                             开始进入第{}页'.format(n))
#     #time.sleep(3)
#     data = {'first': 'false',
#             'pn': n,
#             'kd': 'python'
#             }
#     html = requests.post(url=url,data=data,headers=header)
#     print(html.raise_for_status())
#     #print(html.json()['content']['positionResult']['result'])
#     print('开始写入数据。。。。')
#     for i in range(len(html.json()['content']['positionResult']['result'])):
#         pisitionNameList = html.json()['content']['positionResult']['result'][i]['positionName']
#         #print(html.json()['content']['positionResult']['result'][i]['positionName'])
#         print('正在写入的是第{}页的第{}个职位：{}'.format(n,i,pisitionNameList))
#         with open(r'C:\Users\shoupeng.wang\Desktop\aaaaa.txt','a') as f:
#             f.write(pisitionNameList+'\n')
#
    # for i in reg_list:
    #     if i != '':
    #         print(i)
    #     else:
    #         continue

# sd = pd.Series([1,2,3,4])
# print(sd)
# print(sd.tolist(),type(sd))
# data = {"a":[1,2,3,4],"b":["wqgfsdrsdr","wafesarfasfw","safeasfeafsrr","feasfasefyy"]}
# print(pd.DataFrame(data))

# data = np.random.randint(100,1000,(4,3))
# #print(data)
# data1 = pd.DataFrame(data=data,index=["Row_%s" % i for i in range(1,5)],
#                      columns=["Python","C++","Java",])
# print(data1)
# data= xlrd.open_workbook(r'C:\Users\shoupeng.wang\Desktop\images\workplace\Worksheet.xlsx')
# worksheet = data.sheet_names()#获取表名(sheet)
# print(worksheet)
# for i in worksheet:
#     sheet2 = data.sheet_by_name(i)
#     row = sheet2.row_values(3)#获取第4行的值
#     col = sheet2.col_values(2)#获取第3列的值
#     print (row)
#     print(col)
#
# book = xlwt.Workbook()
# sheet = book.add_sheet('练习表 1')
# list = [
#     ['id','name','age','工号','时间'],
#     ['01','yaoli','28','27111',time.strftime('%Y-%M-%d %H:%M:%S',time.localtime(time.time()))],
#     ['02','fanjing','27','27112',time.strftime('%Y-%M-%d %H:%M:%S',time.localtime(time.time()))],
#     ['03','wangsp','26','27113',time.strftime('%Y-%M-%d %H:%M:%S',time.localtime(time.time()))],
#     ['04','wangchao','25','27114',time.strftime('%Y-%M-%d %H:%M:%S',time.localtime(time.time()))]
# ]
# for i in range(5):
#     for j in range(5):
#         sheet.write(i,j,list[i][j])#指定行、列、值三项
# book.save(r'C:\Users\shoupeng.wang\Desktop\images\workplace\练习表.xls')