#!/usr/bin/env python
# coding:utf-8

import json
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.httputil

# http://localhost:8080/call
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.service import ExternalService


class CallHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        httpUrl = 'http://python.loan.com/rules/region'

        externalService = ExternalService.ExternalCall()
        body = externalService.spliceParam()
        print  'requestBody=', body
        headers = {"Content-Type":"application/json",'Cookie': 'rules_session_id=64b713c52c7511e6a4519801a7928995','RRDSource': 'TL'}
        # headers = tornado.httputil.HTTPHeaders({"content-type": "application/json charset=utf-8",
        #                                         'Cookie': 'rules_session_id=64b713c52c7511e6a4519801a7928995',
        #                                         'RRDSource': 'TL'})
        # content_type = GlobalConstant.CONTENT_TYPE
        # cookie = GlobalConstant.COOKIE
        # source = GlobalConstant.SOURCE
        # print  'content_type=', content_type, 'cookie=', cookie, 'source=', source
        # headers = tornado.httputil.HTTPHeaders({content_type, cookie, source})

        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch(httpUrl, method='POST', headers=headers, body=body)
        self.on_response(response)

    def on_response(self, resp):
         body = json.loads(resp.body)
         print 'body=',body
         if body == None:
             self.write('error')
         else:
             self.write(body)
             # self.write("SUCCESS")
         return




class ExternalHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        httpUrl = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk'

        externalService = ExternalService.ExternalCall()
        body = externalService.spliceParam()
        print  'requestBody=', body
        headers = {"Content-Type":"application/json",'Cookie': 'rules_session_id=64b713c52c7511e6a4519801a7928995','RRDSource': 'TL'}
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch(httpUrl, method='POST', headers=headers, body=body)
        self.on_response(response)

    def on_response(self, resp):
         body = json.loads(resp.body)
         print 'body=',body
         if body == None:
             self.write('error')
         else:
             self.write(body)
             # self.write("SUCCESS")
         return


class ExternalWeatherHandler(tornado.web.RequestHandler):
    def post(self):
        orderEnum = OrderEnum.EXCEPTION
        id = self.get_argument('id')
        user_id= self.get_argument('user_id')
        token= self.get_argument('token')
        source = self.request.headers['source']
        print "id=", id , " ,user_id=" , user_id , " ,token=" , token, " ,source=" , source
        externalService = ExternalService.LendService()
        orderEnum = externalService.insert(id, user_id, token)
        self.write(orderEnum)






# if __name__ == '__main__':
#     print GlobalConstant.HttpEnum.CONTENT_TYPE.value
#     headers = tornado.httputil.HTTPHeaders({GlobalConstant.HttpEnum.CONTENT_TYPE.value, GlobalConstant.HttpEnum.COOKIE.value, GlobalConstant.HttpEnum.SOURCE.value})
#     print headers
#     headers1 = {GlobalConstant.CONTENT_TYPE, GlobalConstant.COOKIE, GlobalConstant.SOURCE}
#     print headers1
