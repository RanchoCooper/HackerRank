#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-23 13:19
# @email    : ranchocooper@gmail.com

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

r = OrderedCounter(input() for _ in range(int(input())))

print(len(d))

print(*d.values)
