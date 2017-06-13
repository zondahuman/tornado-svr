#!/usr/bin/env python
# coding:utf-8
from sqlalchemy import update

from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model.PersistentModel import OrderInfo
from com.abin.lee.util import DaoUtil,ModelUtil
from com.abin.lee.pojo.vo import OridinaryViewObject
from com.abin.lee.util.switch import switch


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
        result_list = []
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(OrderInfo).filter_by(id=id).all():
                   result_list.append({
                    'id':row.id,
                    'name': row.name,
                    'age': row.age,
                    'create_time': row.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'update_time': row.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'version': row.version
                })
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return result_list

    def find_all(self):
        result_list = []
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(OrderInfo).all():
                result_list.append({
                    'id':row.id,
                    'name': row.name,
                    'age': row.age,
                    'create_time': row.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'update_time': row.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'version': row.version
                })
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return  result_list

    def find_by_params(self, key, value):
        result = []
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(OrderInfo).filter_by(name=value).all():
                # orderInfoVo = OridinaryViewObject.OrderInfoVo(id=row.id, name=row.name, age=row.age,create_time=row.create_time,update_time=row.update_time,version=row.version)
                # result.append(orderInfoVo)
                result.append(row[0])
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return  result

    def update_by_id(self, id, key, value):
        result = OrderEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.query(OrderInfo).filter(OrderInfo.id == id).update({key : value})
            session.flush()
            session.commit()
            result = OrderEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return  result













