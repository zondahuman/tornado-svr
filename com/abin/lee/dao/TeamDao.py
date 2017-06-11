#!/usr/bin/env python
# coding:utf-8
from sqlalchemy import update

from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.model.ExternalModel import LendInfo
from com.abin.lee.util import DaoUtil


class TeamInfoDao():

    def insert(self, teamInfo):
        result = MessageEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.add(teamInfo)
            session.commit()
            result = MessageEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result

