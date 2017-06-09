#!/usr/bin/env python
# coding:utf-8

import json
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.httputil

# http://localhost:8080/call
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



# if __name__ == '__main__':
#     print GlobalConstant.HttpEnum.CONTENT_TYPE.value
#     headers = tornado.httputil.HTTPHeaders({GlobalConstant.HttpEnum.CONTENT_TYPE.value, GlobalConstant.HttpEnum.COOKIE.value, GlobalConstant.HttpEnum.SOURCE.value})
#     print headers
#     headers1 = {GlobalConstant.CONTENT_TYPE, GlobalConstant.COOKIE, GlobalConstant.SOURCE}
#     print headers1
