#!/usr/bin/env python
# coding:utf-8

from com.abin.lee.enums.GlobalConstants import MessageEnum
from com.abin.lee.model.PersistentModel import TeamInfo, OrderInfo
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


    def find(self, id):
        result = []
        result = MessageEnum.EXCEPTION
        orderDao = DaoUtil.DaoGeneric()
        session = orderDao.getSession()
        try:
            for row in session.query(TeamInfo.id,TeamInfo.orderId,TeamInfo.teamName,OrderInfo.name, OrderInfo.age, TeamInfo.version).join(OrderInfo).filter(TeamInfo.orderId==id).all():
                result.append({
                    'id':row.id,
                    'orderId': row.orderId
                    'age': row.age,
                    'create_time': row.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'update_time': row.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'version': row.version
                })
            session.commit()
            result = MessageEnum.SUCCESS
        except Exception, e:
            print e
            session.rollback()
        return result

