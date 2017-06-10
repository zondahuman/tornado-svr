#!/usr/bin/env python
# coding:utf-8
import json
import unittest

from com.abin.lee.util import DateUtil
from com.abin.lee.util.HttpClientUtil import HttpService

class OrderTest(unittest.TestCase):

    def test_list_to_dict(self):
        keys = ['id', 'name', 'age']
        values1 = [1, 'abin1', 51]
        dictionary = dict(zip(keys, values1))
        values2 = [2, 'abin2', 52]
        dictionary = dict(zip(keys, values2))
        print "dictionary=", dictionary


    def test_dict_to_list(self):
        keys = ['id', 'name', 'age']
        values1 = [1, 'abin1', 51]
        dictionary = dict(zip(keys, values1))
        values2 = [2, 'abin2', 52]
        dictionary = dict(zip(keys, values2))
        print "dictionary=", dictionary

    def test_dlist_add(self):
        keys = []
        for i in range(10):
            keys.append('abin'+str(i))
        print "keys=", keys

class Player(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number


def encode_json(o):
    if isinstance(o, Player):
        return o.__dict__

        # or, alternatively ...
        return {
            'name': o.name,
            'number': o.number,
        }

    raise TypeError('Cannot serialize object of type %s' % type(o))

    def test_dlist_add_json(self):
        keys = []
        for i in range(10):
            foo = Player(name="abin"+str(i),number=i)
            keys.append(foo)
        print "keys=", keys
        # print "keys=", json.dumps(keys, DateUtil.DateEncoder)
        print "keys=", json.dumps(keys, default=encode_json)



class Foo(json.JSONEncoder):
    def __init__(self, *values):
        self.some_sequence = values

    def __iter__(self):
        for key in self.some_sequence:
            yield (key, 'Value for {}'.format(key))
































