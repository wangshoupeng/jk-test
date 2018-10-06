#! _*_ coding:utf-8 _*_
import requests
#下载验证码
Verification_Code = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.7871458614808138'
session = requests.Session()
response = session.get(Verification_Code)
print(response.content)
fp = open('Verification.png','wb')
fp.write(response.content)
fp.close()
#验证码校验
check = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
code = input("请输入验证码坐标：")
data = {'answer':code.split(),
        'login_site': 'E',
        'rand': 'sjrand',
        }
reg = session.post(check,data=data)
print(reg.json())
# if reg.json()['result_code'] != 4:
#     exit("验证码错误！")
#登陆操作
Land = 'https://kyfw.12306.cn/passport/web/login'
'''
header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '49',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_passport_session=fc33ea052e6f4eb9acdd8859ce7fdc405916; \
        _passport_ct=ceeac30b174e418180ef4229953e1ac4t3224; route=9036359bb8a8a461c164a04f8f50b252;\
        BIGipServerpassport=988283146.50215.0000;\
        RAIL_EXPIRATION=1532669181457;\
        RAIL_DEVICEID=RHCc_jpOhG5fGMLax_AtmwrEhsCr_e9zF7DGh8gFXqTPhUidw7ReUhQ2qf0DR3vJVE022QVcODGlnkDfrgih6K5N3KOfKNOgAP4U820CLPCkkvCSblewzG-adIaTJJ5dUcdpy0lBqk_vGHCFCERQveucqgoJPZcp; \
        BIGipServerpool_passport=183304714.50215.0000; BIGipServerotn=149946890.24610.0000',
        'Host': 'kyfw.12306.cn',
        'Origin': 'https://kyfw.12306.cn',
        'Referer': 'https://kyfw.12306.cn/otn/login/init',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
          }
          '''
dat = {'username': 15718880624,
        'password': 'wsp738852',
        'appid': 'otn',
        }
Landlogin = session.post(url=Land,data=dat)
print("-----------------------")
print(Landlogin.json())


