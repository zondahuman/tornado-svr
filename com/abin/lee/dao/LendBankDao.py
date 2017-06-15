#!/usr/bin/env python
# coding:utf-8
from sqlalchemy import inspect

from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.model.ExternalModel import LendBank
from com.abin.lee.model.PersistentModel import TeamInfo, OrderInfo
from com.abin.lee.util import DaoUtil,DictUtil


class LendBankInfoDao():

    def insert(self, lendBank):
        result = MessageEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.add(lendBank)
            session.commit()
            result = MessageEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result


    def findAll(self):
        result = []
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(LendBank).all():
                result.append(DictUtil.object_as_dict(row))
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return result


