#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-25 09:35
# @email    : ranchocooper@gmail.com

s, n = input(), int(input())

for part in zip(*[iter(s)] * n):
    d = dict()
    print(''.join([d.setdefault(c, c) for c in part if c not in d]))
