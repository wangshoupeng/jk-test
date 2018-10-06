#! _*_ coding:utf-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException #超时异常
from bs4 import BeautifulSoup
search = input('请输入要搜索的商品 ：')
print('正在搜索，请等待。。。。')
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.set_page_load_timeout()
driver.maximize_window()
try:
    element = WebDriverWait(driver,20,0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#kw'))
    )
    element2 = WebDriverWait(driver,20,0.5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#su'))
    )
    #element3 = WebDriverWait(driver, 20, 0.5).until(EC.title_contains('百度一下'))
    # element4 = driver.title
    # element5 = driver.current_url
    # element6 = driver.current_window_handle
    # element7 = driver.command_executor
except Exception as e:
    print(e)
    driver.quit()
else:
    element.send_keys(search)
    element2.click()
print(driver.title)
print(driver.current_url)
print('源代码如下 :\n {}'.format(driver.page_source))
#html = driver.page_source#获取哦源代码
#print(html)
# time.sleep(2)
#webdriver.ActionChains(driver).double_click("要定位的元素").perform()
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(2)
driver.find_element_by_id('kw').clear()
time.sleep(2)
driver.find_element_by_id('kw').send_keys('QQ空间')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
'''
#对时间控件的处理
方法一：原生js，移除readonly属性
js = "document.getElementById('train_date').removeAttribute('readonly')"
方法二：jQuery，移除readonly属性
js = "$('input[id=train_date]').removeAttr('readonly')"
方法三：jQuery，设置属性为false
js = "$('input[id=train_date]').attr('readonly',false)"
方法四：jQuery，设置属性为空
js = "$('input[id=train_date]').attr('readonly',’ ‘)"
然后，
driver.execute_script(js)
driver.find_element_by_id('train_date').clear()
driver.find_element_by_id('train_date').send_keys('2017-09-30')
'''