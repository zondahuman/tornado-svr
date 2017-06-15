#!/usr/bin/env python
# coding:utf-8
import json
import unittest

from com.abin.lee.util import TimeStampUtil
from com.abin.lee.util.HttpClientUtil import HttpService

class LendTest(unittest.TestCase):

    def test_lend_bank_post_add_params(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["bankNo"] = "6228480402564890018"
        dictOrder["bankName"] = 'ICBC'
        http_url = "http://localhost:7600/lendBankAdd"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result



    def test_lend_bank_find_all(self):
        dictOrder = {}
        dictOrder["id"] = 1
        http_url = "http://localhost:7600/lendBankFindAll"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        print "result=", result






































