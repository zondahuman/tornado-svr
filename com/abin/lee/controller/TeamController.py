#!/usr/bin/env python
# coding:utf-8

import tornado
import tornado.gen
import tornado.httpclient
import tornado.httputil
import tornado.web

from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.service import TeamService


class TeamAddHandler(tornado.web.RequestHandler):
    def post(self):
        messageEnum = MessageEnum.INIT
        id = self.get_argument('id')
        teamName= self.get_argument('teamName')
        orderId= self.get_argument('orderId')
        source = self.request.headers['source']
        print "id=", id , " ,teamName=" , teamName , " ,orderId=" , orderId
        teamService = TeamService.TeamInfoService()
        messageEnum = teamService.insert(id, teamName, orderId)
        self.write(messageEnum.__str__())


















