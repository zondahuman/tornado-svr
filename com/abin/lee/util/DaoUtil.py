#!/usr/bin/env python
# coding:utf-8

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker, scoped_session
from tornado.gen import engine

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base(metadata=MetaData(), metaclass=DeclarativeMeta)
Base.query = db_session.query_property()

class DaoGeneric():

    def getSession(self):
        ENGINE = create_engine("mysql+pymysql://root:root@172.16.2.133:3306/trade?charset=utf8", convert_unicode=True)
        Session = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)
        session = Session()
        return session
