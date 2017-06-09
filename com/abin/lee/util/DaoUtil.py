#!/usr/bin/env python
# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DaoGeneric():

    def getSession(self):
        ENGINE = create_engine("mysql+pymysql://root:root@172.16.2.133:3306/trade?charset=utf8", convert_unicode=True)
        Session = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)
        session = Session()
        return session
