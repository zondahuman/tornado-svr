#!/usr/bin/env python
# coding:utf-8
import json
import unittest

from com.abin.lee.util import TimeStampUtil
from com.abin.lee.util.HttpClientUtil import HttpService

class LendTest(unittest.TestCase):

    def test_lend_get_add_params(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["user_id"] = TimeStampUtil.getTimestamp()
        dictOrder["token"] = '9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
        http_url = "http://localhost:8080/externalRegion"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result


    def test_lend_get_body(self):
        http_url = "http://api.openweathermap.org/data/2.5/weather"
        input = "London,uk"
        http_url = http_url + "?" + input
        print "http_url", http_url
        httpService = HttpService()
        result = httpService.http_get_body1(http_url)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_call_nasa(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["user_id"] = TimeStampUtil.getTimestamp()
        dictOrder["token"] = '9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
        http_url = "http://localhost:8080/externalNasa"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        result = httpService.http_get_body(http_url)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result


    def test_call_ip(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["user_id"] = TimeStampUtil.getTimestamp()
        dictOrder["token"] = '9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
        http_url = "http://localhost:8080/externalIp"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        result = httpService.http_get_body(http_url)
        # result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result





























