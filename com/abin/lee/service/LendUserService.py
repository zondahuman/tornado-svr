#!/usr/bin/env python
# coding:utf-8
import datetime

from com.abin.lee.dao import LendUserDao
from com.abin.lee.enums.GlobalConstants import OrderEnum, MessageEnum
from com.abin.lee.model import ExternalModel


class LendUserInfoInfoService():

    def insert(self,lendId, userName, email, age, idNo, userId):
        schedule = MessageEnum.EXCEPTION
        try:
            current_time = datetime.datetime.now()
            lendUser = ExternalModel.LendUser(lendId=lendId, userName = userName, email = email, age = age, idNo = idNo, userId = userId, createTime=current_time, updateTime=current_time, version=0)
            lendDao = LendUserDao.LendUserInfoDao()
            schedule  = lendDao.insert(lendUser)
            id = lendUser.id
            print "schedule", schedule, ", id=", id
        except Exception, e:
            print e
        return schedule

