#!/usr/bin/env python
# coding:utf-8
import datetime

from com.abin.lee.dao import TeamDao
from com.abin.lee.enums.GlobalConstants import OrderEnum, MessageEnum
from com.abin.lee.model import PersistentModel


class TeamInfoService():

    def insert(self, id, teamName, orderId):
        schedule = MessageEnum.EXCEPTION
        try:
            current_time = datetime.datetime.now()
            teamInfo = PersistentModel.TeamInfo(teamName=teamName, orderId = orderId, createTime=current_time, updateTime=current_time, version=0)
            teamDao = TeamDao.TeamInfoDao()
            schedule  = teamDao.insert(teamInfo)
            id = teamInfo.id
            print "schedule", schedule, ", id=", id
        except Exception, e:
            print e
        return schedule






























