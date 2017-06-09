#!/usr/bin/env python
# coding:utf-8


import json
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient


class ExternalCall():

    def spliceParam(self):
        data = {}
        data['city'] = '北京市'
        province = "北京"
        data['province'] = province
        address = "北京"
        data['address'] = address
        body = json.dumps(data, ensure_ascii=True)
        return body


    def callThird(self):
        return