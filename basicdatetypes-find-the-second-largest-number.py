#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author   : Rancho Cooper
# @date     : 2016-10-26 01:36
# @email    : ranchocooper@gmail.com

n = int(input())
l = [int(x) for x in input().split()]
r = [0, 0]

for i in range(n):
    if l[i] > r[1]:
        r
