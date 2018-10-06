#! _*_ coding:utf-8 _*_
from aip import AipOcr
from aip import AipImageClassify
#百度aip开放平台地址：aip.baidu.com
#登录百度账号：15718880624/wangsp,680103
""" 你的 APPID AK SK """
APP_ID = '11569106'
API_KEY = 'd8lI6UNbQGfXwRBttDnZTBZC'
SECRET_KEY = '75GLdHmOccThl9DTKFyUrpudb6yktGVY'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#python文字识别

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'C:\Users\shoupeng.wang\Desktop\images\timg.jpg')

""" 调用通用物体识别 """
message=client.basicGeneral(image)
print(message)
print(message['words_result'][0]['words'])

