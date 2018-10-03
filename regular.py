#! _*_ coding:utf-8 _*_
import re
import math
from urllib import  request
first_url = 'http://www.quanshuwang.com/book/9/9055/'
html = request.urlopen(first_url).read().decode('gbk')
print(html)
nove_info = {}
nove_info['title'] = re.findall(r'<div class="chapName"><span class="r">.*?</span><strong>(.*?)</strong>',html)
print('                                                      '+nove_info['title'][0])
nove_info['autho'] = re.findall(r'<div class="chapName"><span class="r">(.*?)</span><strong>.*?</strong>',html)
print('                                                             '+nove_info['autho'][0])
div_nove = re.findall(r'<DIV class="clearfix dirconone">(.*?)</div>',html,re.S|re.I)[0]
print(div_nove)
tag_a = re.findall(r'<a href="http://www.quanshuwang.com/book/9/9055/(.*?)" title="',div_nove)
print(tag_a)
for result in tag_a:
    print(result)
    print("%s%s" %  (first_url,result))
capter = re.findall(r'<a href="http://www.quanshuwang.com/book/9/9055/.*?" title="(.*?)，',div_nove)
print(capter)
for title in capter:
    print(title)

