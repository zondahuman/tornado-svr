#!/usr/bin/env python
# coding:utf-8
import json
import unittest
from unittest import TestCase

class TupleTest(unittest.TestCase):

    def test_tuple1(self):
        list = []
        list.append(1)
        list.append(4)
        list.append(7)
        # list.append(1).append(4).append(7)
        print list

    def test_tuple2(self):
        list = [2]
        list.append(1)
        list.append(4)
        list.append(7)
        # list.append(1).append(4).append(7)
        list.extend([5])
        print list

    def test_tuple3(self):
        list = [2]
        list.append(1)
        list.append(4)
        list.append(7)
        # list.append(1).append(4).append(7)
        list.extend([5])
        print list
        list.insert(1, 9)
        print list

    def test_tuple4(self):
        list = [2]
        list.append(1)
        list.append(4)
        list.append(7)
        print list
        list.extend([5])
        print tuple(list)
        list.insert(1, 9)
        print list
        print tuple(list)