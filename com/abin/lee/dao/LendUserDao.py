#!/usr/bin/env python
# coding:utf-8

from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.util import DaoUtil


class LendUserInfoDao():

    def insert(self, lendUser):
        result = MessageEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.add(lendUser)
            session.commit()
            result = MessageEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result

