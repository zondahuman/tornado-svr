#!/usr/bin/env python
# coding:utf-8
import json
import tornado
from com.abin.lee.dao import BaseDao
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model import PersistentModel


class OrderService():

    def insertObj(self, id, name, age, create_time, update_time, version):
        orderEnum = OrderEnum.EXCEPTION
        try:
            orderInfo = PersistentModel.OrderInfo(name=name, age = age, create_time=create_time, update_time=update_time, version=version)
            orderDao = BaseDao.OrderDao()
            orderEnum  = orderDao.insert(orderInfo)
            print "orderEnum", orderEnum
        except Exception, e:
            print e
        return orderEnum




