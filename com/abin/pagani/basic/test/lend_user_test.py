#!/usr/bin/env python
# coding:utf-8
import json
import unittest

from com.abin.lee.util import TimeStampUtil
from com.abin.lee.util.HttpClientUtil import HttpService

class LendTest(unittest.TestCase):

    def test_team_post_add_params(self):
        dictOrder = {}
        dictOrder["lendId"] = '302ae01c-9551-4fba-b545-4e6c5b104bab'
        dictOrder["userName"] = '特朗普'
        dictOrder["email"] = 'trump@gmail.com'
        dictOrder["age"] = 15
        dictOrder["idNo"] = '140827199208236617'
        dictOrder["userId"] = 102
        http_url = "http://localhost:8080/lendUserAdd"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result
















