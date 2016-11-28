#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-25 19:56
# @email    : ranchocooper@gmail.com

m, mset = int(input()), set(map(int, input().split()))
n, nset = int(input()), set(map(int, input().split()))

sdiff = mset.difference(nset).union(nset.difference(mset))

for item in sorted(sdiff):
    print(item)
