#!/usr/bin/env python
# coding:utf-8
import simplejson
import tornado
import tornado.gen
import tornado.httpclient
import tornado.httputil
import tornado.web

from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.service import LendBankService


class LendBankAddHandler(tornado.web.RequestHandler):
    def post(self):
        messageEnum = MessageEnum.INIT
        id = self.get_argument('id')
        bankName = self.get_argument('bankName')
        bankNo = self.get_argument('bankNo')
        source = self.request.headers['source']
        print "id=", id, " ,bankName=", bankName, " ,bankNo=", bankNo, " ,source=", source
        lendBankService = LendBankService.LendBankInfoService()
        messageEnum = lendBankService.insert(id, bankName, bankNo)
        self.write(messageEnum.__str__())


class LendBankFindAllHandler(tornado.web.RequestHandler):
    def post(self):
        lendBankService = LendBankService.LendBankInfoService()
        lendBankList = lendBankService.findAll()
        # result = simplejson.dumps(orderInfo, default= OridinaryViewObject.encode_json_bean)
        # result = simplejson.dumps(lendBankList.__str__())
        self.write(lendBankList.__str__())
