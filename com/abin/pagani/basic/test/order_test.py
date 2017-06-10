#!/usr/bin/env python
# coding:utf-8
import json
import unittest
from com.abin.lee.util.HttpClientUtil import HttpService

class OrderTest(unittest.TestCase):

    def test_order_insert(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["name"] = "stevenjohn"
        dictOrder["age"] = 19
        dictOrder["version"] = 0
        http_url = "http://localhost:8080/orderInsert"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_order_insert_json(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["name"] = "stevenjohn"
        dictOrder["age"] = 19
        dictOrder["version"] = 0
        http_url = "http://localhost:8080/orderPostInsert"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post_json(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_order_find_by_Id(self):
        dictOrder = {}
        dictOrder["id"] = 48
        http_url = "http://localhost:8080/orderFindById"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_order_find_all(self):
        dictOrder = {}
        dictOrder["id"] = 48
        http_url = "http://localhost:8080/orderFindAll"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_order_find_by_param(self):
        dictOrder = {}
        dictOrder["key"] = 'name'
        dictOrder["value"] = 'abin'
        http_url = "http://localhost:8080/orderFindByParam"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_order_add_params(self):
        dictOrder = {}
        dictOrder["id"] = 1
        dictOrder["name"] = "stevenjohn"
        dictOrder["age"] = 19
        dictOrder["version"] = 0
        http_url = "http://localhost:8080/orderAdd"
        content = json.dumps(dictOrder)
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        # result = httpService.http_post(http_url,content, dictHeader)
        result = httpService.http_get_param(http_url,dictOrder, dictHeader)
        print "result=", result

    def test_order_add(self):
        http_url = "http://localhost:8080/orderAdd?id=5&name=abin&age=25&version=0"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        # result = httpService.http_post(http_url,content, dictHeader)
        result = httpService.http_get(http_url, dictHeader)
        print "result=", result

    def test_order_add(self):
        http_url = "http://localhost:8080/call"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST1"
        httpService = HttpService()
        # result = httpService.http_post(http_url,content, dictHeader)
        result = httpService.http_get(http_url, dictHeader)
        print "result=", result



    def test_order_update_by_id(self):
        dictOrder = {}
        dictOrder["id"] = 29
        dictOrder["key"] = 'name'
        dictOrder["value"] = 'paul'
        http_url = "http://localhost:8080/orderUpdateById"
        dictHeader = {}
        dictHeader["source"] = "UNITTEST"
        httpService = HttpService()
        result = httpService.http_post(http_url,dictOrder, dictHeader)
        print "result=", result





















































