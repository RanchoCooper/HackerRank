#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-28 12:18
# @email    : ranchocooper@gmail.com

s = set(map(int, input().split()))
r = True

for _ in range(int(input())):
    t = set(map(int, input().split()))
    if s.union(t) > s:
        r = False

print(r)
