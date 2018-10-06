#! _*_ coding:utf-8 _*_
import tornado.web
from tornado import web
from tornado import httpserver
from tornado import ioloop
#tornado框架搭建一个http服务器的固定写法
#application = web.Application

#逻辑处理模块
class IndexHandler(web.RedirectHandler):
    def get(self,*args,**kwargs):
        self.write('王守鹏')
#路由
application = web.Application([
            (r"/", IndexHandler),
        ])
if __name__ == '__main__':
        http_server = httpserver.HTTPServer(application)
        http_server.listen(8080)
        ioloop.IOLoop.current().start()
