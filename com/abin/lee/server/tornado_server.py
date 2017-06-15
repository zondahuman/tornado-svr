#!/usr/bin/env python
# coding:utf-8
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options

import tornado.web

#python filename --port=8000  //run py
from tornado.options import define, options

#从命令行种读取设置。
#如果一个与define语句中同名的设置在命令行中被给出，那么它将成为全局的options的一个属性 即 options.port 相当于define的url的port
from com.abin.lee.controller import OrderController,ExternalController
from com.abin.lee.controller.BaseController import Indexhandler,Wraphandler,Stephandler, ReverseHandle
from com.abin.lee.controller.ExternalController import ExternalNasaHandler, ExternalIpHandler, ExternalRegionHandler
from com.abin.lee.controller.LendUserController import LendUserInfoHandler
from com.abin.lee.controller.TeamController import TeamAddHandler

define ("port", default=7600, help="run on the given port", type=int)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    handlers=[
            (r'/', Indexhandler),
             (r'/wrap', Wraphandler),
             (r'/step', Stephandler),
             (r'/orderAdd', OrderController.OrderHandler),
             (r'/orderInsert', OrderController.OrderAddPostHandler),
             (r'/orderPostInsert', OrderController.OrderAddPostJsonHandler),
             (r'/orderFindById', OrderController.OrderFindByIdandler),
             (r'/orderFindAll', OrderController.OrderFindAllHandler),
             (r'/orderFindByParam', OrderController.OrderFindByParamHandler),
             (r'/orderUpdateById', OrderController.OrderUpdateByIdHandler),
             (r'/call', ExternalController.CallHandler),
             (r'/reverse/(\w+)' , ReverseHandle),
             (r'/externalRegion' , ExternalRegionHandler),
             (r'/externalNasa' , ExternalNasaHandler),
             (r'/externalIp' , ExternalIpHandler),
             (r'/teamAdd' , TeamAddHandler),
             (r'/lendUserAdd' , LendUserInfoHandler),
            ]
    app = tornado.web.Application(handlers)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

