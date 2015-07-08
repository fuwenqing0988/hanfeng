#coding:utf-8

from tornado.web import RequestHandler

class DemoHandler(RequestHandler):
    def get(self):
        self.render('index.html')