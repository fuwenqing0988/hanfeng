#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from py_web import *
from py_serve import *

from tornado.options import define,options
from setproctitle import setproctitle
define("port",default=9997,help="run on the given port",type=int)
setproctitle('linyi_web:server')


if __name__=='__main__':
    tornado.options.parse_command_line()
    settings = {
        'cookie_secret': "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        'template_path':os.path.join(os.path.dirname(__file__),"templates"),
        'static_path':os.path.join(os.path.dirname(__file__),"static")
    }
    page_list=[
        (r'/demo',DemoHandler),
    ]

    ajax_list=[

    ]

    handlers_list=page_list+ajax_list
    app=tornado.web.Application(
        handlers=handlers_list,
        **settings
    )

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()