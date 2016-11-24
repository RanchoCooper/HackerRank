#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-11-24 20:33
# @email    : ranchocooper@gmail.com


n = int(input())
a = [int(x, 10) for x in input().split()]

m = max(a)
while max(a) == m:
    a.remove(max(a))
print(max(a))
