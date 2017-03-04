#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-12-24 12:13
# @email    : ranchocooper@gmail.com

n, x = map(int, input().split())
s = []
for _ in range(x):
    s.append(list(map(float, input().split())))

print(*[sum(item) // x for item in zip(*s)], sep='\n')
# only when using / the code was ak
