#!/usr/bin/env python
# coding:utf-8
# 创建对象的基类:
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class OrderInfo(Base):
    __tablename__ =  'order_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    create_time = Column(Date)
    update_time = Column(Date)
    version = Column(Integer)


