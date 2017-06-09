#!/usr/bin/env python
# coding:utf-8
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.util import DaoUtil


class OrderDao():

    def insert(self, orderInfo):
        result = OrderEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.add(orderInfo)
            session.commit()
            result = OrderEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result