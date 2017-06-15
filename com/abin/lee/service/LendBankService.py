#!/usr/bin/env python
# coding:utf-8
import datetime

from com.abin.lee.dao import LendBankDao
from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.model import ExternalModel


class LendBankInfoService():

    def insert(self, id, bankName, bankNo):
        schedule = MessageEnum.EXCEPTION
        try:
            current_time = datetime.datetime.now()
            lendBank = ExternalModel.LendBank(bankNo=bankNo,bankName=bankName, createTime=current_time, updateTime=current_time, version=0)
            lendBankDao = LendBankDao.LendBankInfoDao()
            schedule  = lendBankDao.insert(lendBank)
            id = lendBank.id
            print "schedule", schedule, ", id=", id
        except Exception, e:
            print e
        return schedule


    def findAll(self):
        result = None
        try:
            current_time = datetime.datetime.now()
            lendBankDao = LendBankDao.LendBankInfoDao()
            result  = lendBankDao.findAll()
            print "result=", result
        except Exception, e:
            print e
        return result





























