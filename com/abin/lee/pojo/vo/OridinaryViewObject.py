#!/usr/bin/env python
# coding:utf-8

class OrderInfoVo(object):
    def __init__(self, id, name, age, create_time, update_time, version):
        self.id = id
        self.name = name
        self.age = age
        self.create_time = create_time
        self.update_time = update_time
        self.version = version

def encode_json_bean(object):
    if isinstance(object, OrderInfoVo):
        return object.__dict__

        # or, alternatively ...
        return {
            'id': object.id,
            'name': object.name,
            'age': object.age,
            'create_time': object.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'update_time': object.update_time.strftime('%Y-%m-%d %H:%M:%S'),
            'version': object.version,
        }
        raise TypeError('Cannot serialize object of type %s' % type(object))
