#!/usr/bin/env python
# coding:utf-8
from sqlalchemy import update

from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model.ExternalModel import LendInfo
from com.abin.lee.util import DaoUtil


class LendDao():

    def insert(self, lendInfo):
        result = OrderEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.add(lendInfo)
            session.commit()
            result = OrderEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result


    def update_by_id(self, id, key, value):
        result = OrderEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.query(LendInfo).filter(LendInfo.id == id).update({key : value})
            session.flush()
            session.commit()
            result = OrderEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return  result

    def update_params_by_id(self, id, lendDict):
        result = OrderEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.query(LendInfo).filter(LendInfo.id == id).update(lendDict)
            session.flush()
            session.commit()
            result = OrderEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return  result