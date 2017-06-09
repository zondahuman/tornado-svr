#!/usr/bin/env python
# coding:utf-8
import textwrap

import tornado.web

#curl http://localhost:8080/
#curl http://localhost:8080/?greeting=ligang
#Tornado的请求处理函数类, 当处理一个请求时，Tornado将这个类实例化，并调用与HTTP请求方法所对应的方法。这里只定义了get()
#也就是说处理函数将对http的GET请求作出响应;


class Indexhandler(tornado.web.RequestHandler):
    def get(self):#默认调用，通过url ？传递参数
        greeting = self.get_argument('greeting', 'Hello')#默认参数
        self.write(greeting + ', friendly user!')#参数作为http返回，写到http响应中;

class ReverseHandle(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class Wraphandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width= self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

#  http://localhost:8080/step?id=5&name=abin
class Stephandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id')
        name= self.get_argument('name', "lee")
        print "id=", id , " ,name=" , name