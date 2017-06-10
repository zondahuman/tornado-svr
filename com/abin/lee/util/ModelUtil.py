#!/usr/bin/env python
# coding:utf-8
import json

import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import class_mapper


def to_dict(model_instance, query_instance=None):
    if hasattr(model_instance, '__table__'):
        return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
    else:
        cols = query_instance.column_descriptions
        return { cols[i]['name'] : model_instance[i]  for i in range(len(cols)) }

def from_dict(dict, model_instance):
    for c in model_instance.__table__.columns:
        setattr(model_instance, c.name, dict[c.name])

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

def row2dictCall(c):
    row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
    return row2dict

def row2dictCall(row):
    dictret = dict(row.__dict__); dictret.pop('_sa_instance_state', None)
    return row2dict

def object_to_dict(obj, found=None):
    if found is None:
        found = set()
    mapper = class_mapper(obj.__class__)
    columns = [column.key for column in mapper.columns]
    get_key_value = lambda c: (c, getattr(obj, c).isoformat()) if isinstance(getattr(obj, c), datetime) else (c, getattr(obj, c))
    out = dict(map(get_key_value, columns))
    for name, relation in mapper.relationships.items():
        if relation not in found:
            found.add(relation)
            related_obj = getattr(obj, name)
            if related_obj is not None:
                if relation.uselist:
                    out[name] = [object_to_dict(child, found) for child in related_obj]
                else:
                    out[name] = object_to_dict(related_obj, found)
    return out



def deep_dict(self, relations={}):
    """Output a dict of an SA object recursing as deep as you want.

    Takes one argument, relations which is a dictionary of relations we'd
    like to pull out. The relations dict items can be a single relation
    name or deeper relation names connected by sub dicts

    Example:
        Say we have a Person object with a family relationship
            person.deep_dict(relations={'family':None})
        Say the family object has homes as a relation then we can do
            person.deep_dict(relations={'family':{'homes':None}})
            OR
            person.deep_dict(relations={'family':'homes'})
        Say homes has a relation like rooms you can do
            person.deep_dict(relations={'family':{'homes':'rooms'}})
            and so on...
    """
    mydict =  dict((c, str(a)) for c, a in
                    self.__dict__.items() if c != '_sa_instance_state')
    if not relations:
        # just return ourselves
        return mydict

    # otherwise we need to go deeper
    if not isinstance(relations, dict) and not isinstance(relations, str):
        raise Exception("relations should be a dict, it is of type {}".format(type(relations)))

    # got here so check and handle if we were passed a dict
    if isinstance(relations, dict):
        # we were passed deeper info
        for left, right in relations.items():
            myrel = getattr(self, left)
            if isinstance(myrel, list):
                mydict[left] = [rel.deep_dict(relations=right) for rel in myrel]
            else:
                mydict[left] = myrel.deep_dict(relations=right)
    # if we get here check and handle if we were passed a string
    elif isinstance(relations, str):
        # passed a single item
        myrel = getattr(self, relations)
        left = relations
        if isinstance(myrel, list):
            mydict[left] = [rel.deep_dict(relations=None)
                                 for rel in myrel]
        else:
            mydict[left] = myrel.deep_dict(relations=None)

    return mydict



def object_to_dict(obj, found=None):
    if found is None:
        found = set()
    mapper = class_mapper(obj.__class__)
    columns = [column.key for column in mapper.columns]
    get_key_value = lambda c: (c, getattr(obj, c).isoformat()) if isinstance(getattr(obj, c), datetime) else (c, getattr(obj, c))
    out = dict(map(get_key_value, columns))
    for name, relation in mapper.relationships.items():
        if relation not in found:
            found.add(relation)
            related_obj = getattr(obj, name)
            if related_obj is not None:
                if relation.uselist:
                    out[name] = [object_to_dict(child, found) for child in related_obj]
                else:
                    out[name] = object_to_dict(related_obj, found)
    return out


def sa_obj_to_dict(obj, filtrate=None, rename=None):
    """
    sqlalchemy 对象转为dict
    :param filtrate: 过滤的字段
    :type filtrate: list or tuple
    :param rename: 需要改名的,改名在过滤之后处理, key为原来对象的属性名称，value为需要更改名称
    :type rename: dict
    :rtype: dict
    """

    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        #该类的相关类型，即直接与间接父类
        cla = obj.__class__.__mro__
        #过滤不需要的父类
        cla = filter(lambda c: hasattr(c, '__table__'), filter(lambda c: isinstance(c, DeclarativeMeta), cla))
        columns = []
        map(lambda c: columns.extend(c.__table__.columns), cla[::-1])
        # columns = obj.__table__.columns
        if filtrate and isinstance(filtrate, (list, tuple)):
            fields = dict(map(lambda c: (c.name, getattr(obj, c.name)), filter(lambda c: not c.name in filtrate, columns)))
        else:
            fields = dict(map(lambda c: (c.name, getattr(obj, c.name)), columns))
        # fields = dict([(c.name, getattr(obj, c.name)) for c in obj.__table__.columns])
        if rename and isinstance(rename, dict):
            #先移除key和value相同的项
            _rename = dict(filter(lambda (k, v): str(k) != str(v), rename.iteritems()))
            #如果原始key不存在，那么新的key对应的值默认为None
            #如果新的key已存在于原始key中，那么原始key的值将被新的key的值覆盖
            # map(lambda (k, v): fields.setdefault(v, fields.pop(k, None)), _rename.iteritems())
            map(lambda (k, v): fields.update({v: fields.pop(k, None)}), _rename.iteritems())
        #
        return fields
    else:
        return {}