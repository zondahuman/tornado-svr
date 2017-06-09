#!/usr/bin/env python
# coding:utf-8
from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model.PersistentModel import OrderInfo
from com.abin.lee.util import DaoUtil,ModelUtil


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


    def find_by_id(self, id):
        row_as_dict = {}
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(OrderInfo).filter_by(id=id).all():
                row_as_dict = ModelUtil.row2dict(row)
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return row_as_dict

    def find_all(self):
        row_as_dict = {}
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(OrderInfo).all():
                row_as_dict.append(ModelUtil.row2dict(row))
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return row_as_dict