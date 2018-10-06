#! user/bin/env python
#! _*_ coding:utf-8 _*_
# auther:王守鹏
from tkinter import *
import tkinter.filedialog
import random
import requests
def upload():
    filename = tkinter.filedialog.askopenfilename(title='选择文件')
    file = open(filename,'rb').read()
    url = ''


gui = Tk()
gui.title('首个gui页面开发')
gui.geometry('+400+150')
ent = Entry(gui,width=50)
ent.grid()
but_up = Button(gui,text='上传',command=upload)
but_wd = Button(gui,text='下载')
but_up.grid()
but_wd.grid()

mainloop()