import time,sys
from PyQt5.QtWidgets import QApplication,QLCDNumber,QWidget,QDesktopWidget,QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class MY_TIME(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()

    def update_time(self):
        # 设置时间元祖  time.localtime()  获取本地时间
        self.lcd.display(time.strftime('%X', time.localtime()))
    def init_timer(self):
        self.timer = QTimer()
        #设置定时器，每一秒触发一次 timeout  信号
        self.timer.setInterval(1000)
        #启动定时器
        self.timer.start()
        self.timer.timeout.connect(self.update_time)
    def initUI(self):
        self.resize(250,100)
        self.setWindowTitle('王守鹏')
        self.move_center()
        self.lcd = QLCDNumber()
        #设置要显示的数字个数
        self.lcd.setDigitCount(10)
        #采用的是十进制模式
        self.lcd.setMode(QLCDNumber.Dec)
        #设置平面模式
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        #设置时间元祖  time.localtime()  获取本地时间
        self.lcd.display(time.strftime('%X',time.localtime()))
        #构建一个盒子布局
        self.main_layout = QVBoxLayout()
        #把上面的组件添加进盒子布局
        self.main_layout.addWidget(self.lcd)
        #设置组件居中
        self.main_layout.setAlignment(Qt.AlignCenter)
        #设置给顶层布局
        self.setLayout(self.main_layout)
        #设置界面颜色
        self.main_bg = QPalette()
        #设置颜色为蓝色
        self.main_bg.setColor(QPalette.Background,Qt.darkGreen)
        #设置自动填充背景颜色
        self.setAutoFillBackground(True)
        #把颜色设置给顶级窗口
        self.setPalette(self.main_bg)
    def move_center(self):
        #设置矩形
        m_rect = self.frameGeometry()
        #获取这个屏幕的中心点
        w_center_point = QDesktopWidget().availableGeometry().center()
        m_rect.moveCenter(w_center_point)
        #从左上角开始移动，直到中间
        self.move(m_rect.topLeft())
        self.show()
if __name__ ==  '__main__':
    app = QApplication(sys.argv)
    m_time = MY_TIME()
    sys.exit(app.exec_())
'''
import requests
url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
param = {'theRegionCode':'3113'}
respnose = requests.get(url=url,params=param)
print (respnose.text)
url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
'''