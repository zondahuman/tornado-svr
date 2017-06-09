#!/usr/bin/env python
# coding:utf-8
# 创建对象的基类:
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
# Base = sqlalchemy.ext.declarative.declarative_base()


class OrderInfo(Base):
    __tablename__ =  'order_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    create_time = Column(Date)
    update_time = Column(Date)
    version = Column(Integer)




    #
    # def to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    # Base.to_dict = to_dict
    # def column_dict(self):
    #     model_dict = dict(self.__dict__)
    #     del model_dict['_sa_instance_state']
    #     return model_dict
    # Base.column_dict = column_dict