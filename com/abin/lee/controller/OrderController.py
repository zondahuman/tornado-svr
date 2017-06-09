#!/usr/bin/env python
# coding:utf-8

#  http://localhost:8080/step?id=5&name=abin
import datetime
import json

import tornado
import tornado.web
import tornado.gen
import tornado.httpclient

from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.service import BaseService

#  http://localhost:8080/orderAdd?id=5&name=abin&age=25&version=0
class OrderHandler(tornado.web.RequestHandler):
    def get(self):
        orderEnum = OrderEnum.EXCEPTION
        id = self.get_argument('id')
        name= self.get_argument('name')
        age= self.get_argument('age')
        version= self.get_argument('version', 0)
        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        source = self.request.headers['source']
        print "id=", id , " ,name=" , name , " ,create_time=" , create_time , " ,update_time=" , update_time , " ,version=" , version , " ,source=" , source
        orderService = BaseService.OrderService()
        orderEnum = orderService.insertObj(id, name, age, create_time, update_time, version)
        self.write(orderEnum)



class OrderAddPostHandler(tornado.web.RequestHandler):
    def post(self):
        orderEnum = OrderEnum.EXCEPTION
        id = self.get_argument('id')
        name= self.get_argument('name')
        age= self.get_argument('age')
        version= self.get_argument('version', 0)
        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        source = self.request.headers['source']
        print "id=", id , " ,name=" , name , " ,create_time=" , create_time , " ,update_time=" , update_time , " ,version=" , version , " ,source=" , source
        orderService = BaseService.OrderService()
        orderEnum = orderService.insertObj(id, name, age, create_time, update_time, version)
        self.write(orderEnum)

class OrderAddPostJsonHandler(tornado.web.RequestHandler):
    def post(self):
        orderEnum = OrderEnum.EXCEPTION
        encode_json  = self.request.body
        print 'encode_json ',encode_json
        dictOrder = json.loads(encode_json )
        id = dictOrder['id']
        name = dictOrder['name']
        age = dictOrder['age']
        version = dictOrder['version']
        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        source = self.request.headers['source']
        print "id=", id , " ,name=" , name , " ,create_time=" , create_time , " ,update_time=" , update_time , " ,version=" , version , " ,source=" , source
        orderService = BaseService.OrderService()
        orderEnum = orderService.insertObj(id, name, age, create_time, update_time, version)
        self.write(orderEnum)

class OrderFindByIdandler(tornado.web.RequestHandler):
    def post(self):
        id = self.get_argument('id')
        print "id=", id
        orderService = BaseService.OrderService()
        orderInfo = orderService.find_by_id(id)
        result = json.dumps(orderInfo)
        self.write(result)

class OrderFindAllHandler(tornado.web.RequestHandler):
    def post(self):
        orderService = BaseService.OrderService()
        orderInfo = orderService.find_by_all()
        result = json.dumps(orderInfo)
        self.write(result)












