#!/usr/bin/env python
# coding:utf-8
# 创建对象的基类:
import json

from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base=declarative_base()
DBSession = scoped_session(sessionmaker())

# Base = sqlalchemy.ext.declarative.declarative_base()
from com.abin.lee.util import DaoUtil


class OrderInfo(DaoUtil.Base):
    __tablename__ =  'order_info'
    # __table__ =  'order_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    create_time = Column(Date)
    update_time = Column(Date)
    version = Column(Integer)
    # query = DBSession.query_property()

    def __repr(self):
        return "<OrderInfo('%s','%s','%s','%s','%s','%s')>"%(self.id,self.name,self.age,self.create_time,self.update_time,self.version)


class TeamInfo(DaoUtil.Base):
    __tablename__ =  'team_info'

    id = Column("id", Integer, primary_key=True)
    teamName = Column("team_name",String(100))
    orderId = Column("order_id",Integer)
    createTime = Column("create_time", DateTime)
    updateTime = Column("update_time", DateTime)
    version = Column("version", Integer)


    def __repr(self):
        return "<OrderInfo('%s','%s','%s','%s','%s','%s')>"%(self.id,self.teamName,self.orderId,self.createTime,self.updateTime,self.version)

























