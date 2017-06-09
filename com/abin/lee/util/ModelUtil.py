#!/usr/bin/env python
# coding:utf-8



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









