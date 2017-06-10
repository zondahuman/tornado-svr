#!/usr/bin/env python
# coding:utf-8

import json
import urllib
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers



#  http://www.cnblogs.com/111testing/p/6079565.html
class HttpService():

    # application/x-www-form-urlencoded
    def http_post(self, http_url, body, headersDict):
        body_value  = urllib.urlencode(body)
        request = urllib2.Request(http_url, body_value)
        for (key, value) in headersDict.items():
            request.add_header(key, value)
        result = urllib2.urlopen(request).read()
        return result

    # multipart/form-data
    def http_post_form(self, http_url, body, headersDict):
        register_openers()
        datagen, re_headers = multipart_encode(body)
        request = urllib2.Request(http_url, datagen, re_headers)
        # 如果有请求头数据，则添加请求头
        for (key, value) in headersDict.items():
            request.add_header(key, value)
        result = urllib2.urlopen(request ).read()
        return result


    # multipart/form-data
    def http_post_json(self, http_url, body, headersDict):
        register_openers()
        body_value = json.dumps(body)
        request = urllib2.Request(http_url, body_value)
        # headers = {'Content-Type': 'application/json'}
        request.add_header('Content-Type', 'application/json')
        for (key, value) in headersDict.items():
            request.add_header(key, value)
        result = urllib2.urlopen(request).read()
        return result


    def http_get_header(self, http_url,headersDict):
        request = urllib2.Request(http_url)
        for (key, value) in headersDict.items():
            request.add_header(key, value)
        response = urllib2.urlopen(request)
        result = response.read()
        return result


    def http_get_param(self, http_url, body, headersDict):
        body_value  = urllib.urlencode(body)
        request = urllib2.Request(http_url+"?%s" % body_value)
        for (key, value) in headersDict.items():
            request.add_header(key, value)
        response = urllib2.urlopen(request)
        result = response.read()
        return result


    def http_get_param_body(self, http_url, body):
        body_value  = urllib.urlencode(body)
        request = urllib2.Request(http_url+"?%s" % body_value)
        # for (key, value) in headersDict.items():
        #     request.add_header(key, value)
        response = urllib2.urlopen(request)
        result = response.read()
        return result


    def http_get_body(self, http_url):
        request = urllib2.Request(http_url)
        response = urllib2.urlopen(request)
        result = response.read()
        return result


    def http_get_body1(self, http_url):
        response = urllib.urlopen(http_url)
        result = response.read()
        return result







































