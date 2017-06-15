#!/usr/bin/env python
# coding:utf-8
from sqlalchemy import inspect


def object_as_dict(obj):
    result = {instance.key: getattr(obj, instance.key)  for instance in inspect(obj).mapper.column_attrs}
    print result
    return result