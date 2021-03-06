#!/usr/bin/env python
# coding:utf-8

from com.abin.lee.enums.GlobalConstants import OrderEnum
from com.abin.lee.model.PersistentModel import OrderInfo
from com.abin.lee.util import DaoUtil,DictUtil


class OrderInfoDao():
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
                    'id': row.id,
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
                result_list.append(DictUtil.object_as_dict(row))
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return result_list

    def find_by_params(self, key, value):
        result = []
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(OrderInfo).filter_by(name=value).all():
                result.append(DictUtil.object_as_dict(row))
                print result
            session.commit()
        except Exception, e:
            print e
            session.rollback()
        return result


    def update_by_id(self, id, key, value):
        result = OrderEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            session.query(OrderInfo).filter(OrderInfo.id == id).update({key: value})
            session.flush()
            session.commit()
            result = OrderEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result
