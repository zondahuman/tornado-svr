#!/usr/bin/env python
# coding:utf-8
import datetime
import json

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient

from com.abin.lee.dao import ExternalDao
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model import ExternalModel
from com.abin.lee.util import UuidUtil
from com.abin.lee.util.HttpClientUtil import HttpService


class LendService():

    def insert(self, id,  user_id, token):
        orderEnum = OrderEnum.EXCEPTION
        try:
            lend_id = UuidUtil.getUuid()
            current_time = datetime.datetime.now()
            lendInfo = ExternalModel.LendInfo(lend_id=lend_id, request_content = '', response_content='', status=OrderEnum.INIT , create_time=current_time, update_time=current_time, version=0)
            lendDao = ExternalDao.LendDao()
            orderEnum  = lendDao.insert(lendInfo)
            id = lendInfo.id
            print "orderEnum", orderEnum, ", id=", id
            lendDict, result = self.callInternalWeather(token)
            input = json.dumps(lendDict)
            print "input=", input, "result=", result
            if result != None:
                lendDict = {}
                lendDict["status"] = OrderEnum.SUCCESS
                lendDict["request_content"] = input
                lendDict["response_content"] = result
                lendDao.update_params_by_id(id, lendDict)
            else:
                lendDao.update_by_id(id, "status", OrderEnum.ERROR)
        except Exception, e:
            lendDao.update_by_id(id, "status", OrderEnum.EXCEPTION)
            print e
        return orderEnum

    # http://api.openweathermap.org/data/2.5/weather?q=London,uk
    # http://api.openweathermap.org/data/2.5/weather?q=London
    def callInternalWeather(self,token):
        http_url = "http://apiv3.iucnredlist.org/api/v3/country/list"
        lendDict = {}
        lendDict["token"] = token
        httpService = HttpService()
        result = httpService.http_get_param_body(http_url, lendDict)
        print "result=", result
        return (lendDict, result)



    def callNasa(self):
        http_url = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"
        http_client = AsyncHTTPClient() # we initialize our http client instance
        response = yield http_client.fetch(http_url, self.handle_request) # here we try
        # ioloop.IOLoop.instance().start()
        self.on_response(response)



    def callIp(self):
        http_url = "http://ip.jsontest.com"
        http_client = AsyncHTTPClient() # we initialize our http client instance
        http_client.fetch(http_url, self.handle_response) # here we try
        # ioloop.IOLoop.instance().start()

    def on_response(self, resp):
         body = json.loads(resp.body)
         print 'body=',body
         if body == None:
             self.write('error')
         else:
             self.write(body)
             # self.write("SUCCESS")
         return

    def handle_response(self, response):
        '''callback needed when a response arrive'''
        if response.error:
            print "Error:", response.error
            # self.
        else:
            print 'called'
            print response.body
            self.write(response.body)


































