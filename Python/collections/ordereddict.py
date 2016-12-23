#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-02 01:17
# @email    : ranchocooper@gmail.com

from collections import OrderedDict

n = int(input())
r = OrderedDict()
for _ in range(n):
    temp = input().split()
    name, value = ' '.join(temp[:-1]), int(temp[-1])

    if r.get(name):
        r[name] += value
    else:
        r[name] = value

for k, v in r.items():
    print(k, v)

