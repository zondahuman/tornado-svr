#!/usr/bin/env python
# coding:utf-8
import datetime
import json

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