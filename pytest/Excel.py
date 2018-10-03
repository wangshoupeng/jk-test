#! _*_ coding:utf-8 _*_
#xlrd主要是用来读取excel文件
import xlrd
#xlwt主要是用来写excel文件
import xlwt
#xlutils结合xlrd可以达到修改excel文件目的
import xlrd
from xlutils.copy import copy
#openpyxl可以对excel文件进行读写操作
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.writer.excel import ExcelWriter
#xlsxwriter可以写excel文件并加上图表
import xlsxwriter
#:https://www.cnblogs.com/lingwang3/p/6416023.html

import requests
# Ctrl+/:注释
# Ctrl+F：搜索
# Ctrl+R：替换
# Tab：缩进
# Shift+Tab：取消缩进
url = 'http://www.baidu.com'
response = requests.get(url)
print(response.content)