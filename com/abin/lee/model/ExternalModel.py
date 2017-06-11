#!/usr/bin/env python
# coding:utf-8
# 创建对象的基类:
import json

import datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from com.abin.lee.util import DaoUtil

Base=declarative_base()
DBSession = scoped_session(sessionmaker())


class LendInfo(DaoUtil.Base):
    __tablename__ =  'lend_info'

    id = Column("id", Integer, primary_key=True)
    lend_id = Column("Lend_id", String(100))
    request_content = Column("request_content", String(500))
    response_content = Column("response_content", Text)
    status = Column("status", String(100))
    user_id = Column("user_id", Integer)
    create_time = Column("create_time", DateTime)
    update_time = Column("update_time", DateTime)
    version = Column("version", Integer)

class LendUser(DaoUtil.Base):
    __tablename__ =  'lend_user'

    id = Column("id", Integer, primary_key=True)
    lendId = Column("Lend_id", String(100), nullable=False)
    userName = Column("user_name", String(500))
    email = Column("email", Text)
    age = Column("age", Integer)
    idNo = Column("id_no", String(100))
    userId = Column("user_id", Integer)
    createTime = Column("create_time", DateTime)
    updateTime = Column("update_time", DateTime)
    version = Column("version", Integer)
