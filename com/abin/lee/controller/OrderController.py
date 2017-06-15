#!/usr/bin/env python
# coding:utf-8
import datetime
import json

import simplejson
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.service import BaseService
from com.abin.lee.pojo.vo import OridinaryViewObject

#  http://localhost:8080/orderAdd?id=5&name=abin&age=25&version=0
from com.abin.lee.util import DateUtil


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
        self.write(orderEnum.__str__())



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
        self.write(orderEnum.__str__())

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
        self.write(orderEnum.__str__())

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
        # result = simplejson.dumps(orderInfo, default= OridinaryViewObject.encode_json_bean)
        result = simplejson.dumps(orderInfo)
        self.write(result)

class OrderFindByParamHandler(tornado.web.RequestHandler):
    def post(self):
        key = self.get_argument('key')
        value = self.get_argument('value')
        print "key=", key, ", value=", value
        orderService = BaseService.OrderService()
        orderInfo = orderService.find_by_params(key, value)
        result = json.dumps(orderInfo, default= OridinaryViewObject.encode_json_bean)
        self.write(result)

class OrderUpdateByIdHandler(tornado.web.RequestHandler):
    def post(self):
        orderEnum = OrderEnum.EXCEPTION
        id = self.get_argument('id')
        key = self.get_argument('key')
        value = self.get_argument('value')
        print "key=", key, ", value=", value
        orderService = BaseService.OrderService()
        orderEnum = orderService.update_by_id(id, key, value)
        self.write(orderEnum.__str__())
























