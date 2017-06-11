#!/usr/bin/env python
# coding:utf-8
import json
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.httputil

from com.abin.lee.enums.GlobalConstants import OrderEnum, MessageEnum
from com.abin.lee.service import LendUserService


class LendUserInfoHandler(tornado.web.RequestHandler):
    def post(self):
        messageEnum = MessageEnum.INIT
        lendId= self.get_argument('lendId')
        userName= self.get_argument('userName')
        email= self.get_argument('email')
        age= self.get_argument('age')
        idNo= self.get_argument('idNo')
        userId= self.get_argument('userId')
        source = self.request.headers['source']
        print "lendId=" , lendId , " ,userName=" , userName, " ,email=" , email, " ,age=" , age, " ,idNo=" , idNo, " ,userId=" , userId, " ,source=" , source
        lendUserService = LendUserService.LendUserInfoInfoService()
        messageEnum = lendUserService.insert(lendId, userName, email, age, idNo, userId)
        self.write(messageEnum)




