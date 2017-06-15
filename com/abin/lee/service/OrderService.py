#!/usr/bin/env python
# coding:utf-8
import json
import tornado
from com.abin.lee.dao import OrderDao
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model import PersistentModel


class OrderInfoService():

    def insertObj(self, id, name, age, create_time, update_time, version):
        orderEnum = OrderEnum.EXCEPTION
        try:
            orderInfo = PersistentModel.OrderInfo(name=name, age = age, create_time=create_time, update_time=update_time, version=version)
            orderDao = OrderDao.OrderInfoDao()
            orderEnum  = orderDao.insert(orderInfo)
            print "orderEnum", orderEnum
        except Exception, e:
            print e
        return orderEnum

    def find_by_id(self, id):
        orderInfo = None
        try:
            orderDao = OrderDao.OrderInfoDao()
            orderInfo  = orderDao.find_by_id(id)
            print "orderInfo", orderInfo
        except Exception, e:
            print e
        return orderInfo


    def find_by_all(self):
        result_list = None
        try:
            orderDao = OrderDao.OrderInfoDao()
            result_list  = orderDao.find_all()
            print "result_list", result_list
        except Exception, e:
            print e
        return result_list


    def find_by_params(self, key, value):
        orderInfoList = None
        try:
            orderDao = OrderDao.OrderInfoDao()
            orderInfoList  = orderDao.find_by_params(key, value)
            print "orderInfoList", orderInfoList
        except Exception, e:
            print e
        return orderInfoList

    def update_by_id(self, id, key, value):
        orderEnum = OrderEnum.EXCEPTION
        try:
            orderDao = OrderDao.OrderInfoDao()
            orderEnum  = orderDao.update_by_id(id, key, value)
            print "orderEnum", orderEnum
        except Exception, e:
            print e
        return orderEnum