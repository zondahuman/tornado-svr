#!/usr/bin/env python
# coding:utf-8
import json
import unittest

from com.abin.lee.util import TimeStampUtil
from com.abin.lee.util.HttpClientUtil import HttpService

class LendTest(unittest.TestCase):

    def test_team_post_add_params(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["orderId"] = 52
        dictOrder["teamName"] = 'KTV'
        http_url = "http://localhost:8080/teamAdd"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result










































